#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import datetime as dt
import html
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DETAIL = ROOT / "detail"
ENGINEERING = ROOT / "audit_work" / "engineering"
ENGINEERING.mkdir(parents=True, exist_ok=True)

TS = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
UA = "protein-scout-TEreg-finding/1.0 (+local audit)"
REQUEST_TIMEOUT = 10
HEAD_TIMEOUT = 8

HPA_IF_START = "<!-- HPA_IF_REPAIR_START -->"
HPA_IF_END = "<!-- HPA_IF_REPAIR_END -->"
PAE_START = "<!-- AF_PAE_REPAIR_START -->"
PAE_END = "<!-- AF_PAE_REPAIR_END -->"

IF_NEGATIVE_RE = re.compile(
    r"HPA\s*IF\s*原图未可靠获取|subcellular\s*IF\s*原图|"
    r"HPA\s*无\s*IF\s*图像|HPA\s*暂无\s*IF|暂无\s*IF|无\s*IF\s*图像|"
    r"未下载本地\s*IF\s*图像|HPA\s*未检测到可靠\s*IF\s*图像信号|"
    r"Pending cell analysis|待细胞分析|no_image_detected|IF thumbnail only",
    re.I,
)
PAE_NEGATIVE_RE = re.compile(
    r"PAE\s*图像暂无数据|PAE\s*暂无数据|未生成本地图片或未可靠获取|"
    r"PAE\s*图像未生成本地文件|PAE\s*图像下载跳过",
    re.I,
)
IMAGE_RE = re.compile(
    r"(?:https?:)?//images\.proteinatlas\.org/[A-Za-z0-9_./%-]+?"
    r"(?:blue_red_green|red_green)\.jpg",
    re.I,
)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def request_text(url: str, timeout: int | None = None) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    timeout = REQUEST_TIMEOUT if timeout is None else timeout
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="replace")


def head_ok(url: str, timeout: int | None = None) -> bool:
    req = urllib.request.Request(url, headers={"User-Agent": UA}, method="HEAD")
    timeout = HEAD_TIMEOUT if timeout is None else timeout
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return 200 <= resp.status < 300
    except Exception:
        return False


def gene_from_path(path: Path) -> str:
    return path.parent.name


def has_if_gap(text: str) -> bool:
    text = strip_repair_blocks(text)
    for line in text.splitlines():
        if IF_NEGATIVE_RE.search(line) and re.search(r"HPA|IF|Protein Atlas|cell analysis", line, re.I):
            return True
    return False


def has_pae_gap(text: str) -> bool:
    text = strip_repair_blocks(text)
    return bool(PAE_NEGATIVE_RE.search(text))


def strip_repair_blocks(text: str) -> str:
    for start, end in [(HPA_IF_START, HPA_IF_END), (PAE_START, PAE_END)]:
        text = re.sub(re.escape(start) + r".*?" + re.escape(end), "", text, flags=re.S)
    return text


def extract_hpa_base(gene: str, text: str) -> str | None:
    m = re.search(r"https://www\.proteinatlas\.org/(ENSG\d+-[A-Za-z0-9_.-]+)(?:[/\s)]|$)", text)
    if m:
        return f"https://www.proteinatlas.org/{m.group(1)}"

    search_url = f"https://www.proteinatlas.org/search/{urllib.parse.quote(gene)}"
    try:
        page = request_text(search_url)
    except Exception:
        return None
    escaped_gene = re.escape(gene)
    patterns = [
        rf"/(ENSG\d+-{escaped_gene})(?:[/?\"'#<])",
        r"/(ENSG\d+-[A-Za-z0-9_.-]+)(?:[/?\"'#<])",
    ]
    for pat in patterns:
        m = re.search(pat, page, re.I)
        if m:
            return f"https://www.proteinatlas.org/{m.group(1)}"
    return None


def normalize_image_urls(page: str) -> list[str]:
    page = html.unescape(page).replace("\\/", "/")
    urls: list[str] = []
    seen: set[str] = set()
    for m in IMAGE_RE.finditer(page):
        url = m.group(0)
        if url.startswith("//"):
            url = "https:" + url
        url = url.replace("http://", "https://")
        if url not in seen:
            seen.add(url)
            urls.append(url)
    # Prefer multichannel display images, but keep red_green because HPA often
    # exposes those as the stable clickable originals.
    return sorted(urls, key=lambda u: (0 if "blue_red_green" in u else 1, u))


def extract_hpa_location(page: str) -> str:
    text = re.sub(r"<[^>]+>", " ", html.unescape(page))
    text = re.sub(r"\s+", " ", text)
    for pat in [
        r"Localized to the ([^.]+?\([^)]+\))",
        r"Main location.*?([A-Z][A-Za-z ,&+-]+?\s*\((?:approved|enhanced|supported|uncertain)\))",
    ]:
        m = re.search(pat, text, re.I)
        if m:
            return m.group(1).strip()
    return ""


def fetch_hpa_if(gene: str, report_text: str, max_images: int) -> dict[str, object]:
    base = extract_hpa_base(gene, report_text)
    if not base:
        return {"hpa_base": "", "subcell_url": "", "if_urls": [], "hpa_location": "", "hpa_error": "hpa_entry_not_found"}
    subcell = base.rstrip("/") + "/subcellular"
    try:
        page = request_text(subcell)
    except Exception as exc:
        return {"hpa_base": base, "subcell_url": subcell, "if_urls": [], "hpa_location": "", "hpa_error": f"{type(exc).__name__}: {exc}"}
    urls = normalize_image_urls(page)[:max_images]
    return {"hpa_base": base, "subcell_url": subcell, "if_urls": urls, "hpa_location": extract_hpa_location(page), "hpa_error": ""}


def extract_uniprot(text: str) -> str:
    patterns = [
        r"alphafold\.ebi\.ac\.uk/entry/([A-Z0-9]+)",
        r"uniprot(?:kb)?[/:\s]+([A-Z0-9]{6,10})",
        r"\bUniProt\b[^A-Z0-9]{0,20}([A-Z0-9]{6,10})",
    ]
    for pat in patterns:
        m = re.search(pat, text, re.I)
        if m:
            return m.group(1).upper()
    return ""


def fetch_pae_url(text: str) -> tuple[str, str]:
    uniprot = extract_uniprot(text)
    if not uniprot:
        return "", "uniprot_not_found"
    for version in ["v6", "v5", "v4", "v3", "v2", "v1"]:
        url = f"https://alphafold.ebi.ac.uk/files/AF-{uniprot}-F1-predicted_aligned_error_{version}.png"
        if head_ok(url):
            return url, ""
    return "", f"pae_png_not_found_for_{uniprot}"


def replace_block(text: str, start: str, end: str, block: str) -> str:
    rx = re.compile(re.escape(start) + r".*?" + re.escape(end), re.S)
    if rx.search(text):
        return rx.sub(block, text)
    return text.rstrip() + "\n\n" + block + "\n"


def rewrite_false_if_lines(text: str) -> str:
    out = []
    for line in text.splitlines():
        if IF_NEGATIVE_RE.search(line) and re.search(r"HPA|IF|Protein Atlas|cell analysis", line, re.I):
            if line.strip().startswith("|"):
                out.append("| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |")
            elif "IF 图像说明" in line:
                out.append("**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。")
            elif "HPA IF 状态" in line:
                out.append("**HPA IF 状态**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。")
            else:
                out.append("HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。")
        else:
            out.append(line)
    return "\n".join(out) + ("\n" if text.endswith("\n") else "")


def rewrite_false_pae_lines(text: str) -> str:
    out = []
    for line in text.splitlines():
        if PAE_NEGATIVE_RE.search(line):
            out.append("**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。")
        else:
            out.append(line)
    return "\n".join(out) + ("\n" if text.endswith("\n") else "")


def hpa_if_block(gene: str, subcell_url: str, location: str, urls: list[str]) -> str:
    loc = location or "HPA subcellular location available; see source page"
    lines = [
        HPA_IF_START,
        f"**HPA IF 图像修正（{dt.date.today().isoformat()}）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: {loc}。来源: {subcell_url}",
        "",
    ]
    lines.extend(f"![]({url})" for url in urls)
    lines.append(HPA_IF_END)
    return "\n".join(lines)


def pae_block(url: str) -> str:
    return "\n".join([
        PAE_START,
        f"**PAE 图像修正（{dt.date.today().isoformat()}）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。",
        "",
        f"![]({url})",
        PAE_END,
    ])


def process(path: Path, apply: bool, include_pae: bool, max_images: int) -> dict[str, str]:
    gene = gene_from_path(path)
    text = read(path)
    if_candidate = has_if_gap(text)
    pae_candidate = include_pae and has_pae_gap(text)
    hpa_result = {"hpa_base": "", "subcell_url": "", "if_urls": [], "hpa_location": "", "hpa_error": ""}
    pae_url = ""
    pae_error = ""
    new_text = text
    changed = False

    if if_candidate:
        hpa_result = fetch_hpa_if(gene, text, max_images)
        urls = hpa_result.get("if_urls") or []
        if urls:
            new_text = rewrite_false_if_lines(new_text)
            new_text = replace_block(new_text, HPA_IF_START, HPA_IF_END, hpa_if_block(gene, str(hpa_result["subcell_url"]), str(hpa_result["hpa_location"]), list(urls)))
            changed = True

    if pae_candidate:
        pae_url, pae_error = fetch_pae_url(text)
        if pae_url:
            new_text = rewrite_false_pae_lines(new_text)
            new_text = replace_block(new_text, PAE_START, PAE_END, pae_block(pae_url))
            changed = True

    if apply and changed and new_text != text:
        path.write_text(new_text, encoding="utf-8")

    return {
        "gene": gene,
        "report_path": str(path.relative_to(ROOT)),
        "if_candidate": str(if_candidate),
        "hpa_images_found": str(len(hpa_result.get("if_urls") or [])),
        "hpa_location": str(hpa_result.get("hpa_location") or ""),
        "hpa_subcell_url": str(hpa_result.get("subcell_url") or ""),
        "hpa_image_urls": ";".join(hpa_result.get("if_urls") or []),
        "hpa_error": str(hpa_result.get("hpa_error") or ""),
        "pae_candidate": str(pae_candidate),
        "pae_url": pae_url,
        "pae_error": pae_error,
        "changed": str(changed),
        "applied": str(bool(apply and changed)),
    }


def main() -> None:
    global REQUEST_TIMEOUT, HEAD_TIMEOUT
    parser = argparse.ArgumentParser(description="Audit and repair false HPA IF/AlphaFold PAE missing statements in detail reports.")
    parser.add_argument("--apply", action="store_true", help="Write repairs to detail reports. Default is audit-only.")
    parser.add_argument("--include-pae", action="store_true", help="Also repair missing AlphaFold PAE image statements when a PAE PNG URL exists.")
    parser.add_argument("--include-pending", action="store_true", help="Include Pending cell analysis reports in addition to explicit no-IF statements.")
    parser.add_argument("--pae-only", action="store_true", help="Only process reports with missing AlphaFold PAE statements.")
    parser.add_argument("--limit", type=int, default=0, help="Limit candidate count for pilot runs.")
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--max-images", type=int, default=6)
    parser.add_argument("--genes", default="", help="Comma-separated gene symbols to process.")
    parser.add_argument("--request-timeout", type=int, default=10)
    parser.add_argument("--head-timeout", type=int, default=8)
    args = parser.parse_args()
    REQUEST_TIMEOUT = args.request_timeout
    HEAD_TIMEOUT = args.head_timeout
    selected_genes = {g.strip().casefold() for g in args.genes.split(",") if g.strip()}

    explicit_rx = re.compile(r"HPA\s*IF\s*原图未可靠获取|subcellular\s*IF\s*原图|HPA\s*无\s*IF\s*图像|HPA\s*暂无\s*IF|暂无\s*IF|无\s*IF\s*图像|no_image_detected|IF thumbnail only", re.I)
    pending_rx = re.compile(r"Pending cell analysis|待细胞分析", re.I)

    reports = sorted(DETAIL.glob("*/*/*-evaluation.md"))
    candidates: list[Path] = []
    for path in reports:
        if selected_genes and gene_from_path(path).casefold() not in selected_genes:
            continue
        text = read(path)
        scan_text = strip_repair_blocks(text)
        is_if = (not args.pae_only) and has_if_gap(scan_text)
        is_pae = args.include_pae and has_pae_gap(scan_text)
        if is_if or is_pae:
            candidates.append(path)
    if args.limit:
        candidates = candidates[: args.limit]

    rows: list[dict[str, str]] = []
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        futures = [pool.submit(process, path, args.apply, args.include_pae, args.max_images) for path in candidates]
        for i, fut in enumerate(as_completed(futures), start=1):
            rows.append(fut.result())
            if i == 1 or i % 10 == 0 or i == len(futures):
                print(f"progress={i}/{len(futures)}", flush=True)
            if i % 25 == 0:
                time.sleep(0.2)

    fields = [
        "gene", "report_path", "if_candidate", "hpa_images_found", "hpa_location",
        "hpa_subcell_url", "hpa_image_urls", "hpa_error", "pae_candidate",
        "pae_url", "pae_error", "changed", "applied",
    ]
    mode = "apply" if args.apply else "audit"
    tsv = ENGINEERING / f"hpa_if_pae_gap_repair_{mode}_{TS}.tsv"
    with tsv.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(sorted(rows, key=lambda r: r["report_path"]))

    changed = sum(1 for r in rows if r["changed"] == "True")
    hpa_found = sum(1 for r in rows if int(r["hpa_images_found"] or "0") > 0)
    pae_found = sum(1 for r in rows if r["pae_url"])
    summary = ENGINEERING / f"hpa_if_pae_gap_repair_{mode}_{TS}.summary.md"
    summary.write_text(
        "\n".join([
            "# HPA IF / PAE Gap Repair",
            "",
            f"- Mode: {mode}",
            f"- Candidates: {len(candidates)}",
            f"- HPA IF images found: {hpa_found}",
            f"- PAE URLs found: {pae_found}",
            f"- Reports changed: {changed}",
            f"- TSV: {tsv.relative_to(ROOT)}",
        ]),
        encoding="utf-8",
    )
    print(f"mode={mode} candidates={len(candidates)} hpa_found={hpa_found} pae_found={pae_found} changed={changed} tsv={tsv}")


if __name__ == "__main__":
    if ROOT.name != "protein-scout-TEreg-finding":
        raise SystemExit(f"Unexpected project root: {ROOT}")
    main()

# 05 继续新蛋白：Safe New Protein Evaluation

你是 Claude Code 中的 protein-scout 新蛋白评估 agent。只有在旧报告质量审计、数据缺失审计、误淘汰审计都稳定后，才使用本协议继续 Sheet3/Sheet4。

本协议目标是继续评估剩余蛋白，同时避免再次产生残缺报告、误报无数据、误淘汰和总表污染。

## 路径

项目路径：
`/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested`

Excel：
`/Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data/Final_TE_finding.xlsx`

harvester：
`/Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data/protein_scout_harvest.py`

harvest packet：
`/Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data/harvest_packets`

## 前置门槛

继续新蛋白前必须满足：

1. 已运行 `01_repair_incomplete_reports.md`，且最新 `broken_report_audit_*.tsv` 没有 CRITICAL/HIGH。
2. 已运行 `02_check_data_absence_mismatch.md`，且最新 `data_absence_mismatch_audit_*.tsv` 没有 CRITICAL/HIGH。
3. 已运行 `04_recheck_false_rejections.md` 第一阶段，且最新 `false_rejection_candidates_*.tsv` 没有 HIGH，或 HIGH 均有人工复核说明。
4. `python3 protein_gate.py --all` 为 0 error。
5. 新增/修复报告无禁止词。
6. 用户或 Codex 明确允许继续。

如果以上任一不满足，停止，不评估新蛋白，并输出需要先运行哪个协议。

## 范围

继续 Sheet3「研究很多」剩余未评估蛋白。Sheet3 完成后继续 Sheet4「重新pa一下」。

Mouse-only 不跳过，做 mouse-aware 评估。

## 队列生成

每次运行先生成新的队列：
`audit_work/new_protein_queue_YYYYMMDD_HHMMSS.tsv`

字段：

| sheet | row | gene | species_note | existing_report | existing_status | action | reason |
|---|---:|---|---|---|---|---|---|

规则：

- 如果已有完整合格报告，跳过并记录 reason。
- 如果已有残缺报告，不继续新评估，转入 `01` 或 `03` 修复。
- 如果是 mouse-only，仍评估，但报告必须明确 mouse/human ortholog 证据。
- 每批最多选择 5 个 gene。

## 每批数量

每次最多 5 个 gene。

## 每个 gene 完整闭环

1. 检查是否已有报告。
2. 生成/更新 harvest packet。
3. 独立查询 PubMed，不准只读 Excel。
4. 查询 HPA，并执行 IF image rescue。
5. 查询 AlphaFold/PAE/PDB。
6. 查询 InterPro/Pfam/domain。
7. 查询 STRING + IntAct/BioGrid/UniProt interaction。
8. 写完整报告。
9. 运行 targeted strict。
10. 检查禁止词。
11. 写 log。
12. 每 5 个 gene 后运行 full gate。
13. 每 5 个 gene 后运行 `01/02/04` 的审计逻辑，确认本批没有残缺、误报无数据或误淘汰。
14. 全部通过后才进入下一批。

## HPA 规则

HPA 是核定位核心证据。每个报告必须写：

- HPA reliability
- main location
- additional location
- IF image status
- image candidates 数量
- 是否 embedded

不要因为第一种 URL 找不到就写无图。

必须从 HPA page 和 `/subcellular` page 抽取：

- `images.proteinatlas.org`
- `_blue_red_green.jpg`
- `_red_green.jpg`
- `selected_medium`
- `medium`
- thumbnail

只要有图就嵌入。没有完整图但有 thumbnail，也可以嵌入并标注。

## PAE 规则

- 有 `<GENE>-PAE.png` 必须嵌入。
- AlphaFold 有 PAE URL 就下载。
- 真无数据才写缺失说明，并写明已检查来源。

## PPI 规则

每个报告必须有真实 PPI 表：

| Partner | 来源 | 方法/score/PMID | 功能类别 | 调控相关？ |
|---|---|---|---|---|

禁止：

- 需进一步查询
- 暂无详细
- 待补充
- 基于基因家族推断
- IntAct有限记录
- IntAct 有限记录
- 无记录 | — | —

## PubMed 规则

必须独立检索 PubMed。

报告必须记录：

- strict query
- broad query
- strict count
- broad count
- 关键文献
- 文献与 TE regulation/nuclear regulation 的关系

## 分类规则

分类由定位证据和功能证据共同决定。

- Nucleolus main 或强核仁证据，归 nucleolus，不要混入普通 nucleoplasm。
- Nuclear speckles main 或剪接斑点强证据，归 nuclear-speckle。
- Chromatin/DNA-binding/chromatin complex 强证据，归 chromatin。
- Nuclear body 强证据，归 nuclear-body。
- Nuclear envelope/membrane 强证据，归 nuclear-envelope。
- 多 compartment 且 cytoplasm 证据强，才考虑 nucleus-cytoplasm。
- HPA/UniProt/GO 有核定位证据时，不能轻易 rejected。

## rejected 规则

rejected 也不能只有一行。

每个 rejected 报告至少要包含：

- 基本信息
- 淘汰原因
- HPA/UniProt/GO-CC 定位证据
- PubMed strict/broad
- AlphaFold/PAE/PDB 简述
- PPI 简述
- 为什么不应保留
- 是否需要人工复核

如果 HPA main/additional 包含：

- Nucleoplasm
- Nuclear speckles
- Nucleolus
- Nuclear bodies
- Nuclear membrane
- Chromatin

必须详细讨论，不能轻易淘汰。

## 每个 gene 后检查

运行：

```bash
python3 validate_strict.py --gene <GENE>
```

检查禁止词：

```bash
rg "需进一步查询|暂无详细|待补充|基于基因家族推断|IntAct有限记录|IntAct 有限记录|无记录 \\| — \\| —|网络限制|未能获取" detail/*/<GENE>/<GENE>-evaluation.md
```

每 5 个 gene 后：

```bash
python3 protein_gate.py --all
```

## 批次后审计

每批完成后，必须生成新的：

- `audit_work/broken_report_audit_YYYYMMDD_HHMMSS.tsv`
- `audit_work/data_absence_mismatch_audit_YYYYMMDD_HHMMSS.tsv`
- `audit_work/false_rejection_candidates_YYYYMMDD_HHMMSS.tsv`

本批 genes 不得出现 CRITICAL/HIGH。若出现，停止继续新蛋白，回到对应修复协议。

## Log

创建：
`log/claude_continue_safe_eval_YYYYMMDD_HHMMSS.md`

每个 gene 立即记录：

- sheet
- row
- gene
- category/status
- report path
- HPA reliability/main/additional
- IF candidates/downloaded/embedded
- PAE status
- PDB status
- PubMed strict/broad
- PPI partner counts
- classification rationale
- targeted strict result
- forbidden phrase grep result
- 批次后 01/02/04 audit 结果

## 完成后只输出

- new protein queue 路径
- log 路径
- 完成 genes
- scored/rejected 列表
- IF embedded 数量
- PAE embedded 数量
- PPI queried/repaired 数量
- 批次后三个 audit 路径
- full gate 结果
- 是否允许进入下一批
- 需要人工判断的问题

# 01 修残缺质量：Incomplete Report Audit And Repair

你是 Claude Code 中的 protein-scout 修复 agent。当前任务是通用的残缺质量审计与小批修复。

核心原则：**先审计生成坏报告清单，再按清单小批修复。没有 audit 队列时禁止直接修。**

## 路径

项目路径：
`/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested`

harvest packet 目录：
`/Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data/harvest_packets`

harvester：
`/Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data/protein_scout_harvest.py`

## 阶段 A：生成/更新坏报告 audit

每次执行本协议，先生成新的 audit，不要复用旧时间戳文件作为唯一依据。

输出：
`audit_work/broken_report_audit_YYYYMMDD_HHMMSS.tsv`

扫描所有：
`detail/*/*/*-evaluation.md`

字段：

| gene | category | status | char_count | risk | flags | has_hpa_details | has_if_or_rescue | has_plddt | has_pae_or_note | has_pdb_info | has_real_ppi | has_pubmed_counts | has_key_lit | rejection_lines | lazy_phrases |
|---|---|---|---:|---|---|---|---|---|---|---|---|---|---|---:|---|

## 风险分级

### CRITICAL

任一满足：

- scored 报告 `<3500` 字符。
- scored 报告含占位词：
  - `需进一步查询`
  - `暂无详细`
  - `待补充`
  - `基于基因家族推断`
  - `IntAct有限记录`
  - `IntAct 有限记录`
  - `无记录 | — | —`
- scored 报告缺评分总览。
- scored 报告缺 HPA details。
- scored 报告缺 PubMed strict。
- scored 报告缺真实 PPI 表。
- scored 报告缺 AlphaFold/pLDDT 且无明确不可用原因。
- scored 报告缺 PAE 图或 PAE 缺失说明。
- rejected 报告 `<1200` 字符。
- rejected 报告只有一两行淘汰理由。

### HIGH

任一满足：

- scored 报告 `<6000` 字符。
- 缺 HPA reliability/main/additional。
- 缺 IF 图像且缺 image rescue 记录。
- 缺 PDB 查询结果。
- 缺 key literature。
- rejected 中有核定位线索但解释不足。

### MED

格式或局部内容不足，但不是明显残缺。

### LOW

仅轻微格式问题。

## 阶段 B：选择修复队列

生成 audit 后，只修本轮队列，不超过 10 个 gene。

选择顺序：

1. 用户明确点名的 gene。
2. `risk=CRITICAL` 且 `status=scored`。
3. `risk=CRITICAL` 且 `status=rejected`。
4. `risk=HIGH` 且 `status=scored`。
5. `risk=HIGH` 且 `status=rejected`。

如果某个 gene 已经在最近 log 中完整修复并通过 targeted strict 与禁止词检查，可以跳过，但必须在 log 说明。

## 禁止

- 禁止全量修复。
- 禁止一次处理超过 10 个 gene。
- 禁止批量往大量报告里插模板。
- 禁止只为通过 gate 塞最小字段。
- 禁止继续 Sheet3/Sheet4 新蛋白。
- 禁止写占位句。
- 禁止说“暂无数据”但没有实际检查来源。

## 每个 scored 报告最低结构

每个 scored 报告必须包含：

- frontmatter
- 基本信息表
- 完整评分总览
- 3.1 核定位证据，含 HPA reliability/main/additional
- IF 图像或明确 rescue 失败说明
- 3.2 蛋白大小
- 3.3 PubMed strict/broad + 关键文献
- 3.4 AlphaFold + pLDDT + PAE + PDB
- 3.5 InterPro/Pfam/domain
- 3.6 PPI 表格
- 3.7 多库互证
- 总体评价
- 数据来源

## rejected 报告最低结构

即使仍然 rejected，也不能只有一行。必须包含：

- frontmatter
- 基本信息
- 淘汰原因
- HPA/UniProt/GO-CC 定位证据
- PubMed strict/broad
- AlphaFold/PAE/PDB 简述
- PPI 简述
- 为什么不应保留
- 是否需要人工复核

## 必查数据源

每个 gene 必须重新核查：

- UniProt
- HPA / Protein Atlas
- HPA IF image rescue
- AlphaFold pLDDT
- PAE 图
- PDB / PDBe / RCSB
- InterPro / Pfam / domain
- STRING
- IntAct / BioGrid / UniProt interaction
- GO-CC
- PubMed strict/broad
- 关键文献

## HPA IF rescue

不要轻易写无图。必须尝试：

1. 打开 HPA gene page 和 `/subcellular` page。
2. 提取所有 `images.proteinatlas.org` 的 jpg。
3. 优先下载/嵌入：
   - `*_blue_red_green.jpg`
   - `*_red_green.jpg`
   - `selected_medium`
   - thumbnail / medium jpg
4. 只要有 red_green 或 blue_red_green 就下载并嵌入。
5. 如果只有 thumbnail，也可以嵌入，但必须说明是 thumbnail。
6. 如果仍失败，必须写：
   `暂无数据（HPA IF 原图未可靠获取；已检查 HPA subcellular page 和 image URL candidates），核定位判定主要基于 HPA localization/reliability + UniProt + GO-CC`

## PPI 格式

PPI 必须是真表，不允许占位：

| Partner | 来源 | 方法/score/PMID | 功能类别 | 调控相关？ |
|---|---|---|---|---|

没有结果也要写真实查询来源和返回情况，不得写 `无记录 | — | —`。

## 执行闭环

逐 gene 执行：

1. 读取原报告和 audit flags。
2. 重新核查数据源。
3. 重写或补全报告，不可只补一句。
4. 运行：

```bash
python3 validate_strict.py --gene <GENE>
```

5. 检查禁止词：

```bash
rg "需进一步查询|暂无详细|待补充|基于基因家族推断|IntAct有限记录|IntAct 有限记录|无记录 \\| — \\| —|网络限制|未能获取" detail/*/<GENE>/<GENE>-evaluation.md
```

6. 必须无禁止词。
7. 每修完一个 gene 立即写 log。
8. 每 5 个 gene 运行：

```bash
python3 protein_gate.py --all
```

## 阶段 C：修复后复审

本批修复完成后，必须再次生成：

`audit_work/broken_report_audit_YYYYMMDD_HHMMSS.tsv`

并在 log 中写：

- 修复前 CRITICAL/HIGH 数
- 修复后 CRITICAL/HIGH 数
- 本批 gene 是否仍在 CRITICAL/HIGH

## Log

创建：
`log/claude_audit_queue_repair_YYYYMMDD_HHMMSS.md`

每个 gene 记录：

- gene
- 原 category/status
- audit flags
- 修复后 category/status
- 是否改分类/改分
- HPA reliability/main/additional
- IF candidates/downloaded/embedded
- AlphaFold/PAE
- PDB
- PPI partner 数
- PubMed strict/broad
- validate_strict result
- 禁止词 grep result
- 是否进入 protein-finding.md

## 完成后只输出

- 新 audit TSV 路径
- log 路径
- 本批修复 genes
- 每个报告路径
- 改分类/改分列表
- IF rescue 成功/失败统计
- PAE/PDB 修复统计
- PPI 修复统计
- targeted strict 结果
- full gate 结果
- 修复后 CRITICAL/HIGH 统计
- 仍需人工判断的问题


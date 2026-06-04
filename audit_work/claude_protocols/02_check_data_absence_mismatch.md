# 02 检查数据缺失：Data Absence Mismatch Audit

你是 Claude Code 中的 protein-scout 数据缺失审计 agent。当前任务只审计，不修复任何报告。

本协议是通用工具，不依赖任何旧 TSV。每次运行都必须生成新的 mismatch audit。

## 路径

项目路径：
`/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested`

harvest packet 目录：
`/Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data/harvest_packets`

## 目标

扫描所有已生成报告，找出“报告声称无数据/未获取/暂无记录，但本地文件、harvest packet 或公开来源显示可能有数据”的 mismatch。

重点数据源：

- HPA / IF 图像
- AlphaFold / PAE
- PDB / experimental structure
- STRING / IntAct / BioGrid / UniProt interaction
- PubMed 文献数量和关键文献

不要只检查少数示例。SETMAR 这类已知问题必须被 audit 捕获，但本协议目标是全量发现同类问题。

## 输出

必须生成新的：
`audit_work/data_absence_mismatch_audit_YYYYMMDD_HHMMSS.tsv`

字段：

| gene | category | status | report_path | mismatch_type | risk | report_claim | actual_evidence | packet_evidence | source_checked | candidates_count | local_files_count | action_suggestion | notes |
|---|---|---|---|---|---|---|---|---|---|---:|---:|---|---|

同一个 gene 可以有多行，例如 IF mismatch 和 PPI mismatch 各一行。

## 审计流程

1. 枚举 `detail/*/*/*-evaluation.md` 和 `detail/rejected/*/*-evaluation.md`。
2. 从路径识别 gene、category、status。
3. 读取报告文本，提取所有“无数据/暂无/未获取/占位”声明。
4. 检查 gene 目录中已有文件：
   - `IF_images/*.jpg`
   - `IF_images/*.png`
   - `<GENE>-PAE.png`
   - 其它结构图或截图
5. 检查 harvest packet：
   - HPA URL / Ensembl ID
   - IF image URLs / medium URLs / thumbnail URLs
   - AlphaFold accession / PAE URL
   - STRING / IntAct / interaction records
   - PubMed strict/broad counts
   - PDB candidates
6. 必要时访问公开来源验证候选是否存在，但不要下载大批图片。
7. 写入新的 audit TSV。
8. 写 log，并总结 HIGH 队列。

## HPA / IF mismatch

标记 HIGH：

报告写以下任一：

- `暂无数据`
- `IF unavailable`
- `Pending cell analysis`
- `HPA IF 原图未可靠获取`
- `no_image_detected`
- `无 IF`
- `未获取 IF`
- `未能获取`

但满足任一：

- `IF_images/` 已有 jpg/png
- harvest packet 中有 `if_image_urls`
- harvest packet 中有 `medium_image_urls`
- harvest packet 中有 `thumbnail_urls`
- HPA page 或 `/subcellular` page 能提取到 `images.proteinatlas.org/*.jpg`
- Protein Atlas 页面存在 `red_green`、`blue_red_green`、`selected_medium`、`thumbnail`、`medium`

如果 HPA 有定位文本但图像未取到，标记 MED 或 HIGH：

- HPA 定位是判定核定位的核心证据，不能因为图片缺失而忽略 HPA 文本证据。
- 若报告连 HPA reliability/main/additional 都缺失，标记 HIGH。

## PAE mismatch

标记 HIGH：

报告写 PAE 暂无/不可用，但满足任一：

- 本地存在 `<GENE>-PAE.png`
- packet 中有 AlphaFold/PAE URL
- AlphaFold API 返回 PAE image / JSON / CIF

## PPI mismatch

标记 HIGH：

报告写无 PPI / 无记录 / 需进一步查询 / IntAct 有限记录，但满足任一：

- STRING API 返回 partner
- IntAct 返回 tab27 records
- BioGrid/UniProt interaction 有记录
- 报告已有 partner 文字，但 PPI 表写成无记录
- PPI 表缺失或不是规范表格

## PDB mismatch

标记 MED 或 HIGH：

报告写无 PDB，但 PDBe/RCSB/UniProt cross-reference 检出 PDB entry。

若报告完全缺少 AlphaFold/PDB/PAE 结构段，标记 HIGH。

## PubMed mismatch

标记 MED 或 HIGH：

- 报告只复述 Excel 中的 PubMed 数，不独立搜索。
- strict/broad counts 缺失。
- 关键文献段缺失。
- 报告说“暂无关键文献”，但 PubMed strict 或 broad 检索有明显相关文献。

## 风险等级

- CRITICAL：报告极短、核心段落缺失，同时存在明显可获取数据。
- HIGH：报告声称无数据，但至少一个核心来源显示有数据；或 HPA/结构/PPI/PubMed 核心段缺失。
- MED：数据可能存在但需进一步确认；或格式不规范影响判断。
- LOW：轻微格式或说明问题。

## 禁止

- 禁止修复报告。
- 禁止编辑 `detail/`。
- 禁止编辑 `protein-finding.md`。
- 禁止批量下载图片。
- 禁止把未验证的猜测写成已证实数据。

只生成 TSV 和 log。

## Log

创建：
`log/claude_data_absence_mismatch_audit_YYYYMMDD_HHMMSS.md`

记录：

- audit TSV 路径
- 总报告数
- HPA/IF mismatch 数
- PAE mismatch 数
- PPI mismatch 数
- PDB mismatch 数
- PubMed mismatch 数
- HIGH/CRITICAL 数
- SETMAR 是否进入队列及其行内容
- HIGH 前 50 个 gene
- 下一步建议：是否运行 `03_repair_false_absence.md`

## 完成后只输出

- audit TSV 路径
- log 路径
- mismatch 统计
- SETMAR 行
- HIGH/CRITICAL 前 50 个 gene
- 是否建议进入修复协议

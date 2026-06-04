# 03 修误报无数据：False Absence Repair

你是 Claude Code 中的 protein-scout 数据修复 agent。当前任务只修复“报告说无数据但实际有数据”的 mismatch，不继续新蛋白，不做全量重写。

本协议必须接在 `02_check_data_absence_mismatch.md` 后运行。

## 路径

项目路径：
`/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested`

harvest packet 目录：
`/Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data/harvest_packets`

## 前置门槛

1. 找到最新的：
   `audit_work/data_absence_mismatch_audit_*.tsv`
2. 如果不存在 mismatch audit，停止，不修复，并提示先运行 `02_check_data_absence_mismatch.md`。
3. 如果最新 audit 明显不是本轮生成或内容为空，停止，不修复。
4. 从最新 audit 中筛选 risk 为 CRITICAL/HIGH 的行。
5. 若没有 CRITICAL/HIGH，只处理 MED 中明确影响判断的行；否则停止。

## 目标

按最新 mismatch audit 修复前 10 个 gene。

排序规则：

1. CRITICAL 优先。
2. HIGH 优先。
3. 同一 gene 多个 mismatch 合并处理。
4. HPA/IF、PAE、PPI、PDB、PubMed 任何一个核心数据源误报缺失，都必须同 gene 一次性补齐。
5. 如果 SETMAR 在 audit 队列中，必须包含 SETMAR。

本轮最多修复 10 个 gene。

## 禁止

- 禁止一次修复超过 10 个 gene。
- 禁止全量修复。
- 禁止继续新蛋白。
- 禁止只改一句话而不补齐对应段落、图片、表格和证据。
- 禁止把“有数据但没下载到”写成“无数据”。
- 禁止没有查询就写“暂无数据”。
- 禁止删除用户已有人工判断，除非新证据明确推翻，且 log 中说明。

## HPA / IF rescue

对每个 gene：

1. 读取 packet 中的 HPA URL/Ensembl ID。
2. 访问：
   - `https://www.proteinatlas.org/<ENSEMBL>-<GENE>`
   - `https://www.proteinatlas.org/<ENSEMBL>-<GENE>/subcellular`
3. 从 HTML 中提取所有 `images.proteinatlas.org` jpg。
4. 优先级：
   - `*_blue_red_green.jpg`
   - `*_red_green.jpg`
   - `selected_medium`
   - `medium`
   - thumbnail
5. 只要有 red_green 或 blue_red_green，就下载到：
   `detail/<category>/<GENE>/IF_images/`
6. 如果只有 thumbnail，也允许嵌入，但必须标注 thumbnail。
7. 报告中必须嵌入 1-2 张代表性 IF 图像。
8. 如果下载失败，可临时嵌入远程 URL，并在 log 说明。
9. 即使 IF 图像仍无法获取，也必须写 HPA reliability/main/additional 和定位解释。

## PAE rescue

- 如果本地有 `<GENE>-PAE.png`，必须嵌入。
- 如果没有但 AlphaFold 有 PAE URL，下载。
- 如果 AlphaFold 有模型但无 PAE 图，写清 checked source。
- 只有确认不可用，才写明确缺失原因。

## PPI rescue

必须重查 STRING + IntAct/BioGrid/UniProt interaction。

PPI 表格式：

| Partner | 来源 | 方法/score/PMID | 功能类别 | 调控相关？ |
|---|---|---|---|---|

无结果也要写真实查询来源、查询式、候选数量，不允许占位。

## PDB rescue

如果报告写无 PDB，但 PDBe/RCSB/UniProt 有结果：

- 列 PDB ID
- 方法
- 分辨率
- 覆盖区域
- 与评分的关系

如果无 PDB，也必须保留 AlphaFold/PAE 结构评估。

## PubMed rescue

必须独立检索 PubMed，不准只读取 Excel 中的值。

至少记录：

- strict query
- broad query
- strict count
- broad count
- 2-5 篇关键文献或“未发现直接相关文献”的真实依据

## 每个 gene 完成后

运行：

```bash
python3 validate_strict.py --gene <GENE>
```

检查禁止词：

```bash
rg "需进一步查询|暂无详细|待补充|基于基因家族推断|IntAct有限记录|IntAct 有限记录|无记录 \\| — \\| —|网络限制|未能获取" detail/*/<GENE>/<GENE>-evaluation.md
```

如果确实无数据，可以保留“暂无数据”，但同段必须写明已检查哪些来源、查询式、候选数量和失败原因。

每修 5 个 gene，运行：

```bash
python3 protein_gate.py --all
```

## 修复后再审计

本批修复完成后，必须再次运行 `02_check_data_absence_mismatch.md` 的审计逻辑，生成新的：
`audit_work/data_absence_mismatch_audit_YYYYMMDD_HHMMSS.tsv`

确认本批修复 genes 不再出现同类 HIGH/CRITICAL mismatch。若仍出现，继续修本批问题，不要进入新蛋白。

## Log

创建：
`log/claude_data_absence_mismatch_repair_YYYYMMDD_HHMMSS.md`

每个 gene 写：

- gene
- mismatch 类型：IF/PAE/PPI/PDB/PubMed
- 原报告错误句
- 实际发现的数据
- IF candidates 数
- IF downloaded/embedded
- HPA reliability/main/additional
- PAE downloaded/embedded
- PPI partners 数
- PDB entries
- PubMed strict/broad counts
- 修复后路径
- validate result
- 禁止词 grep result
- 修复后再次审计结果
- 是否更新总表

## 完成后只输出

- 使用的 mismatch audit TSV 路径
- 修复后新 audit TSV 路径
- repair log 路径
- 修复 genes
- 仍有 HIGH/CRITICAL 的 genes
- SETMAR 修复结果，如果适用
- IF rescue 成功/失败统计
- PAE rescue 统计
- PPI rescue 统计
- PDB rescue 统计
- PubMed rescue 统计
- full gate 结果

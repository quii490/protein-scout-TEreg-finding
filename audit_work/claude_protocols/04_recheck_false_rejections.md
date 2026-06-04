# 04 修误淘汰：False Rejection Recheck

你是 Claude Code 中的 protein-scout 误淘汰复审 agent。当前任务只复审 rejected 报告中可能被错杀的核蛋白，不继续新蛋白，不做全量改写。

本协议是通用工具。每次运行都必须先生成新的 false rejection audit，再按 audit 队列小批修复。

## 路径

项目路径：
`/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested`

harvest packet 目录：
`/Users/quii/Desktop/projects/TE-regulated proteins finding/protein_data/harvest_packets`

## 第一阶段：生成误淘汰候选清单

先审计所有 rejected 报告，生成新的：
`audit_work/false_rejection_candidates_YYYYMMDD_HHMMSS.tsv`

字段：

| gene | report_path | char_count | rejection_reason | hpa_main | hpa_additional | hpa_reliability | uniprot_location | go_cc_nuclear | pubmed_strict | pubmed_broad | structure_status | ppi_status | risk | rationale | action_suggestion |
|---|---|---:|---|---|---|---|---|---|---:|---:|---|---|---|---|---|

## 审计来源

对每个 rejected gene 检查：

- rejected 报告文本
- gene 目录已有文件
- harvest packet
- HPA reliability/main/additional
- HPA IF 图像候选
- UniProt subcellular location
- GO cellular component
- PubMed strict/broad
- AlphaFold/PAE/PDB
- STRING/IntAct/BioGrid/UniProt interaction

## HIGH 标记规则

标记 HIGH：

- rejected 报告少于 1200 字符。
- rejected 只有一行或接近一行。
- rejected 报告没有 HPA/UniProt/GO-CC/PubMed/结构/PPI 基本段落。
- HPA/UniProt/GO-CC 有强核定位线索：
  - Nucleoplasm main
  - Nuclear speckles
  - Nucleolus main
  - Nuclear bodies
  - Nuclear membrane main
  - Chromatin
  - DNA binding
  - transcription factor
  - RNA polymerase
  - spliceosome
  - chromatin complex
  - GO nucleus / nucleoplasm / chromatin / nuclear speck
- PubMed strict <=100 且存在核定位或调控相关线索，不应直接按低优先级淘汰。
- HPA main/additional 是 nuclear 相关，但 rejected 理由没有充分解释。

如果只是 HPA additional nucleoplasm，而 main 是 cytosol/plasma membrane，且 UniProt/GO/PubMed 不支持，可以保持 rejected，但报告必须充分解释。

## 第二阶段：小批复审修复

生成 audit 后，只修复 HIGH 前 10 个 gene。

如果没有 HIGH：

- 不修复。
- 输出 audit 路径、统计和“无 HIGH 误淘汰候选”。

每个可能误淘汰的 gene 必须完整重评：

- HPA reliability/main/additional
- IF image rescue
- UniProt location
- GO-CC
- PubMed strict/broad
- AlphaFold/PAE/PDB
- InterPro/domain
- STRING/IntAct/BioGrid/UniProt interaction
- 关键文献
- 与 TE regulation / nuclear regulation 的关系

## rejected 报告最低要求

即使仍然 rejected，也不能只有一行。必须包含：

- 基本信息
- 淘汰原因
- HPA/UniProt/GO-CC 定位证据
- PubMed strict/broad
- AlphaFold/PAE/PDB 简述
- PPI 简述
- 为什么不应保留
- 是否需要人工复核

## 如果恢复为 scored

如果复审后应恢复：

- 移动到正确分类目录。
- 写完整 scored 报告。
- 分类必须按核定位和功能证据判断，不要把 nucleolus 错归成普通 nucleoplasm。
- 更新总表只能通过 gate/rebuild。
- log 中标明 `recovered_from_rejected: yes`。

## 每个 gene 后检查

运行：

```bash
python3 validate_strict.py --gene <GENE>
```

检查禁止词：

```bash
rg "需进一步查询|暂无详细|待补充|基于基因家族推断|IntAct有限记录|IntAct 有限记录|无记录 \\| — \\| —|网络限制|未能获取" detail/*/<GENE>/<GENE>-evaluation.md
```

每修 5 个 gene 后：

```bash
python3 protein_gate.py --all
```

## 修复后再审计

本批复审完成后，必须再次运行本协议第一阶段，生成新的：
`audit_work/false_rejection_candidates_YYYYMMDD_HHMMSS.tsv`

确认本批 genes 不再是 HIGH，或者 log 中有充分解释为什么仍需人工判断。

## Log

创建：
`log/claude_false_rejection_recheck_YYYYMMDD_HHMMSS.md`

每个 gene 写：

- gene
- 原 rejected 理由
- 复审核定位证据
- PubMed strict/broad
- IF rescue 结果
- 结构证据
- PPI 证据
- 是否恢复
- 修复后分类
- targeted strict result
- 禁止词 grep result
- 再审计结果
- 是否需要人工判断

## 完成后只输出

- false rejection audit TSV 路径
- 修复后新 audit TSV 路径
- log 路径
- 复审 genes
- 从 rejected 恢复的 genes
- 保持 rejected 但补全报告的 genes
- 需要人工判断的 genes
- full gate 结果

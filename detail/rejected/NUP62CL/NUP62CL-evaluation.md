---
type: protein-evaluation
gene: "NUP62CL"
date: 2026-06-04
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NUP62CL — REJECTED (数据不可用)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | NUP62CL |
| 数据状态 | 无 harvest packet |
| 评估日期 | 2026-06-04 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 数据不可用 | — | — | — | 无 harvest packet，无法评分 |
| **原始总分** | | | **N/A/180** | |
| **归一化总分** | | | **N/A/100** | |

### 3. 淘汰理由

**数据不可用**: 该基因在 harvest_packets 目录中无对应 JSON 文件，无法进行 /180 标准评分。可能原因包括：
- 该基因未被纳入原始 harvest pipeline
- UniProt 中无对应的人类蛋白条目
- 基因符号命名变化

### 4. 后续建议

- [ ] 确认基因符号是否为新命名（检查 HGNC 最新命名规范）
- [ ] 在 UniProt 检索对应的人类蛋白条目
- [ ] 如找到有效条目，重新运行 harvest pipeline 生成数据包

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/?query=NUP62CL
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NUP62CL
- Protein Atlas: https://www.proteinatlas.org/search/NUP62CL
- AlphaFold: https://alphafold.ebi.ac.uk/search?q=NUP62CL

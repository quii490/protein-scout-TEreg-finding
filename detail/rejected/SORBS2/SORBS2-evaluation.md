---
type: protein-evaluation
gene: "SORBS2"
date: 2026-06-28
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SORBS2 — REJECTED (核定位证据不足 (核定位得分 1/10))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | SORBS2 |
| 蛋白名称 | Sorbin and SH3 domain-containing protein 2 (ArgBP2) |
| 蛋白大小 | 1100 aa / ~124 kDa |
| UniProt ID | O94875 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 1/10 | ×4 | 4 | LOCATION: 黏着斑/胞质，衔接蛋白 |
| 蛋白大小 | 6/10 | ×1 | 6 | 1100 aa |
| 研究新颖性 | 5/10 | ×5 | 25 | PubMed~200 |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold pLDDT 中低（大蛋白柔性区多） |
| 调控结构域 | 5/10 | ×2 | 10 | SoHo, 3×SH3 (IPR001452) |
| PPI 网络 | 4/10 | ×3 | 12 | PPI degree=9 |
| **加权总分** | | | **69/180** | |
| **归一化总分** | | | **38/100** | |

### 3. 详细分析

#### 3.1 核定位证据

**GO Cellular Component**:
- focal adhesion (GO:0005925)
- cytoplasm (GO:0005737)
- cytoskeleton (GO:0005856)

**结论**: 该蛋白定位于黏着斑和细胞质，是一种衔接蛋白（adaptor protein），通过SH3结构域介导细胞骨架-整合素信号。无核定位信号，HPA IHC显示胞质/膜染色。

#### 3.2 蛋白大小、研究现状、结构、结构域、PPI（各1-2行简要说明）

- **蛋白大小**: 1100 aa，~124 kDa，大蛋白但位于黏着斑/胞质。
- **研究现状**: PubMed约200篇，研究集中于心肌重构、肿瘤抑制、癫痫中的作用，无核功能报道。
- **三维结构**: 含SoHo和3个SH3结构域，为固有无序蛋白含多个柔性区段。
- **调控结构域**: SH3结构域介导蛋白-蛋白互作，与细胞骨架重排相关，无DNA结合域。
- **PPI 网络**: PPI degree=9，与细胞骨架蛋白及信号分子互作，无核蛋白互作。

### 4. 总体评价

**推荐等级**: REJECTED

**核心结论**: SORBS2 — 黏着斑衔接蛋白，通过SH3结构域参与整合素-细胞骨架信号。该蛋白定位于黏着斑和胞质，无核定位证据。不建议作为核蛋白研究目标。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O94875
- Protein Atlas: https://www.proteinatlas.org/search/SORBS2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SORBS2
- AlphaFold: https://alphafold.ebi.ac.uk/search/text/SORBS2

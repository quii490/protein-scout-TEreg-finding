---
type: protein-evaluation
gene: "TMPRSS2"
date: 2026-06-28
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TMPRSS2 — REJECTED (核定位证据不足 (核定位得分 0/10))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | TMPRSS2 |
| 蛋白名称 | Transmembrane serine protease 2 (TMPRSS2, type II transmembrane serine protease) |
| 蛋白大小 | 492 aa / ~54 kDa |
| UniProt ID | O15393 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 0/10 | ×4 | 0 | 质膜跨膜蛋白，非核 |
| 蛋白大小 | 4/10 | ×1 | 4 | 492 aa |
| 研究新颖性 | 3/10 | ×5 | 15 | PubMed=~800 (COVID热门) |
| 三维结构 | 6/10 | ×3 | 18 | PDB条目较多 |
| 调控结构域 | 5/10 | ×2 | 10 | Serine protease domain |
| PPI 网络 | 3/10 | ×3 | 9 | PPI degree=13 |
| **加权总分** | | | **56/180** | |
| **归一化总分** | | | **31/100** | |

### 3. 详细分析

#### 3.1 核定位证据

**GO Cellular Component**:
- plasma membrane (GO:0005886)
- extracellular region (GO:0005576)
- integral component of plasma membrane (GO:0005887)

**结论**: 该蛋白为II型跨膜丝氨酸蛋白酶，定位于细胞质膜，通过其蛋白酶活性剪切病毒刺突蛋白（如SARS-CoV-2 Spike），促进病毒进入宿主细胞。明确为膜蛋白，无核定位证据。

#### 3.2 蛋白大小、研究现状、结构、结构域、PPI（各1-2行简要说明）

- **蛋白大小**: 492 aa，含跨膜区和胞外蛋白酶结构域。
- **研究现状**: 因COVID-19研究而极度热门，PubMed超800篇，新颖性极低。
- **三维结构**: 胞外蛋白酶结构域有多条PDB晶体结构，结构信息丰富。
- **结构域**: 跨膜区、LDL受体A类结构域、SRCR结构域、丝氨酸蛋白酶结构域。
- **PPI**: PPI度=13，主要与病毒刺突蛋白和宿主受体ACE2相关。

### 4. 总体评价

**推荐等级**: REJECTED

**核心结论**: TMPRSS2 — 细胞表面跨膜丝氨酸蛋白酶。该蛋白明确为质膜蛋白，作为SARS-CoV-2进入细胞的关键辅助因子已被广泛研究。非核蛋白，不建议作为核蛋白研究目标。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O15393
- Protein Atlas: https://www.proteinatlas.org/search/TMPRSS2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TMPRSS2
- AlphaFold: https://alphafold.ebi.ac.uk/search/text/TMPRSS2

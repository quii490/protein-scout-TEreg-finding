---
type: protein-evaluation
gene: "PXK"
date: 2026-06-28
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PXK — REJECTED (核定位证据不足 (核定位得分 1/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | PXK |
| 蛋白名称 | PX domain-containing protein kinase-like protein |
| 蛋白大小 | 578 aa / ~65 kDa |
| UniProt ID | Q7Z7A4 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 1/10 | ×4 | 4 | 内体/胞质: PX结构域结合PI3P膜, 内吞体分选功能 |
| 蛋白大小 | 8/10 | ×1 | 8 | 578 aa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed≈65篇 |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold预测良好, 无序区域有限 |
| 调控结构域 | 5/10 | ×2 | 10 | PX结构域(IPR001683) + 伪激酶结构域 + WH2肌动蛋白结合模体 |
| PPI 网络 | 3/10 | ×3 | 9 | PPI degree=6 |
| **加权总分** | | | **82/180** | |
| **归一化总分** | | | **45.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

**GO Cellular Component**:
- cytosol (GO:0005829)
- endosome membrane (GO:0010008)
- early endosome (GO:0005769)

**结论**: 该蛋白为PX结构域含有的伪激酶(又名MONaKA)，通过PX结构域结合PI3P定位于早期内体膜，参与内吞体分选和受体回收。非核蛋白。

#### 3.2 蛋白大小、研究现状、结构、结构域、PPI（各1-2行简要说明）

- **蛋白大小**: 578 aa，中等大小，适合结构/生化研究。
- **研究现状**: PubMed约65篇，以SNX蛋白家族和内吞体分选研究为主，研究基础中等。
- **三维结构**: AlphaFold预测整体良好，PX结构域折叠明确，伪激酶结构域(无催化活性)。
- **结构域**: PX结构域(膜结合) + 蛋白激酶样结构域(无催化活性) + WH2肌动蛋白结合模体。
- **PPI**: 6个配体(source STRING)，涉及内吞体转运相关互作蛋白。

### 4. 总体评价

**推荐等级**: REJECTED

**核心结论**: PXK — PX结构域含有的伪激酶，定位于内体/胞质，参与膜转运和内吞体分选。无核定位证据，不建议作为核蛋白研究目标。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z7A4
- Protein Atlas: https://www.proteinatlas.org/search/PXK
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PXK
- AlphaFold: https://alphafold.ebi.ac.uk/search/text/PXK

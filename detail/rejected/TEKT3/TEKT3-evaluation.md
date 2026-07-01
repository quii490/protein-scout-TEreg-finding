---
type: protein-evaluation
gene: "TEKT3"
date: 2026-06-28
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TEKT3 — REJECTED (核定位证据不足 (核定位得分 1/10))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | TEKT3 |
| 蛋白名称 | Tektin-3 |
| 蛋白大小 | 490 aa / ~57 kDa |
| UniProt ID | Q9BXF9 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 1/10 | ×4 | 4 | LOCATION: 纤毛/鞭毛轴丝，顶体膜 |
| 蛋白大小 | 6/10 | ×1 | 6 | 490 aa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed~50 |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold pLDDT 中等，coiled-coil |
| 调控结构域 | 3/10 | ×2 | 6 | Tektin (IPR000435) |
| PPI 网络 | 2/10 | ×3 | 6 | PPI degree=5 |
| **加权总分** | | | **54/180** | |
| **归一化总分** | | | **30/100** | |

### 3. 详细分析

#### 3.1 核定位证据

**GO Cellular Component**:
- cilium axoneme (GO:0005930)
- sperm flagellum (GO:0036126)
- acrosomal membrane (GO:0002080)

**结论**: 该蛋白为纤毛和鞭毛轴丝的结构蛋白（tektin家族成员），与TEKT2类似，在微管壁内形成丝状聚合体。TEKT3还定位于精子顶体膜，参与精子结构和运动功能。无任何核定位信号，为高度特化的纤毛/鞭毛蛋白。

#### 3.2 蛋白大小、研究现状、结构、结构域、PPI（各1-2行简要说明）

- **蛋白大小**: 490 aa，~57 kDa，tektin家族保守成员。
- **研究现状**: PubMed约50篇，研究集中于精子鞭毛结构、男性不育、纤毛结构，无核功能报道。
- **三维结构**: 含多个coiled-coil区域，预测形成纤维状结构，无实验结构。
- **调控结构域**: Tektin结构域（IPR000435），为微管壁纤维状聚合物结构组分，无DNA结合域。
- **PPI 网络**: PPI degree=5，仅与tektin家族（TEKT1/2/4）及少量轴丝蛋白互作。

### 4. 总体评价

**推荐等级**: REJECTED

**核心结论**: TEKT3 — 纤毛/鞭毛微管结构蛋白tektin-3，定位于精子鞭毛轴丝和顶体膜。该蛋白为高度特化的纤毛/鞭毛结构蛋白，无核定位证据。不建议作为核蛋白研究目标。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BXF9
- Protein Atlas: https://www.proteinatlas.org/search/TEKT3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TEKT3
- AlphaFold: https://alphafold.ebi.ac.uk/search/text/TEKT3

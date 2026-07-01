---
type: protein-evaluation
gene: "TEKT2"
date: 2026-06-28
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TEKT2 — REJECTED (核定位证据不足 (核定位得分 1/10))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | TEKT2 |
| 蛋白名称 | Tektin-2 (TEKTB1) |
| 蛋白大小 | 430 aa / ~50 kDa |
| UniProt ID | Q9UIF3 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 1/10 | ×4 | 4 | LOCATION: 纤毛/鞭毛轴丝，微管相关 |
| 蛋白大小 | 6/10 | ×1 | 6 | 430 aa |
| 研究新颖性 | 5/10 | ×5 | 25 | PubMed~55 |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold pLDDT 中等，含coiled-coil |
| 调控结构域 | 3/10 | ×2 | 6 | Tektin (IPR000435) |
| PPI 网络 | 2/10 | ×3 | 6 | PPI degree=3 |
| **加权总分** | | | **59/180** | |
| **归一化总分** | | | **33/100** | |

### 3. 详细分析

#### 3.1 核定位证据

**GO Cellular Component**:
- cilium axoneme (GO:0005930)
- sperm flagellum (GO:0036126)
- microtubule cytoskeleton (GO:0015630)

**结论**: 该蛋白为纤毛和鞭毛轴丝的结构蛋白（tektin家族），在微管壁内形成丝状聚合体，是纤毛/鞭毛微管的结构组分。TEKT2在精子鞭毛中高表达，对精子运动至关重要。无任何核定位信号。

#### 3.2 蛋白大小、研究现状、结构、结构域、PPI（各1-2行简要说明）

- **蛋白大小**: 430 aa，~50 kDa，含tektin结构域的纤维结构蛋白。
- **研究现状**: PubMed约55篇，研究集中于精子鞭毛结构和男性不育，无核功能报道。
- **三维结构**: 含多个coiled-coil区域，预测形成延伸的纤维状结构，无实验结构。
- **调控结构域**: Tektin结构域（IPR000435），为纤毛/鞭毛微管的结构组分，无DNA结合域。
- **PPI 网络**: PPI degree=3，互作极少，仅与tektin家族成员和少量轴丝蛋白相关。

### 4. 总体评价

**推荐等级**: REJECTED

**核心结论**: TEKT2 — 纤毛/鞭毛微管结构蛋白tektin-2，在精子鞭毛轴丝中形成丝状聚合物。该蛋白为纤毛/鞭毛特异性结构蛋白，无核定位证据。不建议作为核蛋白研究目标。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UIF3
- Protein Atlas: https://www.proteinatlas.org/search/TEKT2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TEKT2
- AlphaFold: https://alphafold.ebi.ac.uk/search/text/TEKT2

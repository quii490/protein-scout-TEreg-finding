---
type: protein-evaluation
gene: "SCCPDH"
date: 2026-06-28
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SCCPDH — REJECTED (核定位证据不足 (核定位得分 1/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | SCCPDH |
| 蛋白名称 | Saccharopine dehydrogenase-like oxidoreductase |
| 蛋白大小 | 429 aa / ~47 kDa |
| UniProt ID | Q8NBX0 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 1/10 | ×4 | 4 | 线粒体: 线粒体基质, 酵母氨酸脱氢酶 |
| 蛋白大小 | 7/10 | ×1 | 7 | 429 aa |
| 研究新颖性 | 9/10 | ×5 | 45 | PubMed≈15篇, 极度新颖 |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold预测良好, 脱氢酶折叠保守 |
| 调控结构域 | 4/10 | ×2 | 8 | Saccharopine脱氢酶家族结构域(NAD+结合) |
| PPI 网络 | 3/10 | ×3 | 9 | PPI degree=8 |
| **加权总分** | | | **91/180** | |
| **归一化总分** | | | **50.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

**GO Cellular Component**:
- mitochondrion (GO:0005739)
- mitochondrial matrix (GO:0005759)
- lipid droplet (GO:0005811)

**结论**: 该蛋白为酵母氨酸脱氢酶家族成员，定位于线粒体基质，催化酵母氨酸氧化脱氢反应，参与赖氨酸降解途径。线粒体代谢酶，非核蛋白。

#### 3.2 蛋白大小、研究现状、结构、结构域、PPI（各1-2行简要说明）

- **蛋白大小**: 429 aa，中等大小，脱氢酶家族典型大小。
- **研究现状**: PubMed仅约15篇直接研究，极度新颖，功能注释尚不完整。
- **三维结构**: AlphaFold预测整体良好，NAD+结合Rossmann折叠保守。
- **结构域**: Saccharopine脱氢酶结构域(IPR005097) + NAD(P)结合结构域。
- **PPI**: 8个互作配体(source STRING)，主要来自高通量蛋白组学筛选结果。

### 4. 总体评价

**推荐等级**: REJECTED

**核心结论**: SCCPDH — 酵母氨酸脱氢酶样蛋白，定位于线粒体基质，参与赖氨酸降解代谢。极度新颖但非核蛋白，无核定位证据，不建议作为核蛋白研究目标。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NBX0
- Protein Atlas: https://www.proteinatlas.org/search/SCCPDH
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SCCPDH
- AlphaFold: https://alphafold.ebi.ac.uk/search/text/SCCPDH

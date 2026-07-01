---
type: protein-evaluation
gene: "SPPL2B"
date: 2026-06-28
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SPPL2B — REJECTED (核定位证据不足 (核定位得分 1/10))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | SPPL2B |
| 蛋白名称 | Signal peptide peptidase-like 2B (IMP-4) |
| 蛋白大小 | 592 aa / ~65 kDa |
| UniProt ID | Q8TCT7 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 1/10 | ×4 | 4 | LOCATION: 膜蛋白，高尔基体/内质网/溶酶体 |
| 蛋白大小 | 7/10 | ×1 | 7 | 592 aa |
| 研究新颖性 | 3/10 | ×5 | 15 | PubMed~25 |
| 三维结构 | 5/10 | ×3 | 15 | AlphaFold pLDDT 中等，含多次跨膜 |
| 调控结构域 | 4/10 | ×2 | 8 | Peptidase A22B (IPR007369), Presenilin |
| PPI 网络 | 4/10 | ×3 | 12 | PPI degree=8 |
| **加权总分** | | | **61/180** | |
| **归一化总分** | | | **34/100** | |

### 3. 详细分析

#### 3.1 核定位证据

**GO Cellular Component**:
- Golgi apparatus (GO:0005794)
- lysosomal membrane (GO:0005765)
- integral component of membrane (GO:0016021)

**结论**: 该蛋白为多次跨膜天冬氨酸蛋白酶，定位于高尔基体、溶酶体和内质网膜系统。属于presenilin家族膜内切割蛋白酶（intramembrane protease），无核定位证据。

#### 3.2 蛋白大小、研究现状、结构、结构域、PPI（各1-2行简要说明）

- **蛋白大小**: 592 aa，~65 kDa，多次跨膜蛋白。
- **研究现状**: PubMed约25篇，研究较少，主要关注其蛋白酶功能及在免疫中的作用，无转录调控报道。
- **三维结构**: 含多个跨膜螺旋，属于presenilin家族GxGD型天冬氨酸蛋白酶。
- **调控结构域**: Peptidase A22B结构域，跨膜蛋白酶催化域，无DNA结合或核定位信号。
- **PPI 网络**: PPI degree=8，主要与膜蛋白和底物互作，无核蛋白互作。

### 4. 总体评价

**推荐等级**: REJECTED

**核心结论**: SPPL2B — 高尔基体/溶酶体膜定位的跨膜天冬氨酸蛋白酶，参与膜蛋白的膜内切割。该蛋白为膜蛋白，无任何核定位证据。不建议作为核蛋白研究目标。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TCT7
- Protein Atlas: https://www.proteinatlas.org/search/SPPL2B
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SPPL2B
- AlphaFold: https://alphafold.ebi.ac.uk/search/text/SPPL2B

---
type: protein-evaluation
gene: "TECR"
date: 2026-06-28
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TECR — REJECTED (核定位证据不足 (核定位得分 1/10))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | TECR |
| 蛋白名称 | Trans-2,3-enoyl-CoA reductase (GPSN2/TER) |
| 蛋白大小 | 308 aa / ~36 kDa |
| UniProt ID | Q9NZ01 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 1/10 | ×4 | 4 | LOCATION: ER膜，多次跨膜 |
| 蛋白大小 | 4/10 | ×1 | 4 | 308 aa |
| 研究新颖性 | 3/10 | ×5 | 15 | PubMed~30 |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold pLDDT 中低，多次跨膜 |
| 调控结构域 | 3/10 | ×2 | 6 | 3-oxo-5α-steroid 4-dehydrogenase (IPR001104) |
| PPI 网络 | 5/10 | ×3 | 15 | PPI degree=17 |
| **加权总分** | | | **56/180** | |
| **归一化总分** | | | **31/100** | |

### 3. 详细分析

#### 3.1 核定位证据

**GO Cellular Component**:
- endoplasmic reticulum membrane (GO:0005789)
- integral component of membrane (GO:0016021)

**结论**: 该蛋白为内质网膜定位的多次跨膜还原酶，催化超长链脂肪酸延伸循环的最后一步（反式-2,3-烯酰辅酶A还原为酰基辅酶A）。定位于ER膜，无任何核定位证据，其酶活性完全在ER膜上进行。

#### 3.2 蛋白大小、研究现状、结构、结构域、PPI（各1-2行简要说明）

- **蛋白大小**: 308 aa，~36 kDa，含多个跨膜螺旋的膜蛋白。
- **研究现状**: PubMed约30篇，研究较少，主要关注脂肪酸延伸和神经发育疾病（MRT14），无转录调控报道。
- **三维结构**: 多次跨膜蛋白，属于类固醇5α-还原酶家族，无实验结构。
- **调控结构域**: 类固醇5α-还原酶/3-氧代-5α-类固醇4-脱氢酶结构域（IPR001104），催化结构域。
- **PPI 网络**: PPI degree=17，与脂肪酸延伸酶复合物成员（ELOVL1-7）互作，均在ER膜。

### 4. 总体评价

**推荐等级**: REJECTED

**核心结论**: TECR — ER膜定位的超长链脂肪酸还原酶，在ER膜上催化脂肪酸延伸反应。该蛋白为ER多次跨膜蛋白，无核定位证据。不建议作为核蛋白研究目标。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NZ01
- Protein Atlas: https://www.proteinatlas.org/search/TECR
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TECR
- AlphaFold: https://alphafold.ebi.ac.uk/search/text/TECR

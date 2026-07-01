---
type: protein-evaluation
gene: "TXN2"
date: 2026-06-28
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TXN2 — REJECTED (核定位证据不足 (核定位得分 0/10))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | TXN2 |
| 蛋白名称 | Thioredoxin 2 (TXN2, mitochondrial thioredoxin, TRX2) |
| 蛋白大小 | 166 aa / ~18 kDa |
| UniProt ID | Q99757 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 0/10 | ×4 | 0 | 线粒体蛋白，非核 |
| 蛋白大小 | 1/10 | ×1 | 1 | 166 aa |
| 研究新颖性 | 5/10 | ×5 | 25 | PubMed=~100 |
| 三维结构 | 6/10 | ×3 | 18 | PDB: 1UVZ |
| 调控结构域 | 3/10 | ×2 | 6 | Thioredoxin domain |
| PPI 网络 | 3/10 | ×3 | 9 | PPI degree=10 |
| **加权总分** | | | **59/180** | |
| **归一化总分** | | | **33/100** | |

### 3. 详细分析

#### 3.1 核定位证据

**GO Cellular Component**:
- mitochondrion (GO:0005739)
- mitochondrial matrix (GO:0005759)

**结论**: 该蛋白为线粒体硫氧还蛋白，含线粒体靶向序列，定位于线粒体基质。作为线粒体抗氧化系统的核心组分，通过二硫键还原酶活性维持线粒体氧化还原稳态。明确为线粒体蛋白，非核蛋白。

#### 3.2 蛋白大小、研究现状、结构、结构域、PPI（各1-2行简要说明）

- **蛋白大小**: 166 aa，非常小的蛋白，仅约18 kDa。
- **研究现状**: 中等热度（PubMed约100篇），为经典线粒体硫氧还蛋白，在凋亡、氧化应激和线粒体功能研究中常见。
- **三维结构**: PDB条目1UVZ（NMR结构），结构信息良好，典型硫氧还蛋白折叠。
- **结构域**: 硫氧还蛋白结构域，含C-G-P-C活性位点基序。
- **PPI**: PPI度=10，主要与线粒体内的氧化还原酶（如PRDX3）相互作用。

### 4. 总体评价

**推荐等级**: REJECTED

**核心结论**: TXN2 — 线粒体硫氧还蛋白2。该蛋白为经典的线粒体基质蛋白，参与氧化还原调控，明确为线粒体定位。无核定位证据，不建议作为核蛋白研究目标。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q99757
- Protein Atlas: https://www.proteinatlas.org/search/TXN2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TXN2+thioredoxin
- AlphaFold: https://alphafold.ebi.ac.uk/search/text/TXN2

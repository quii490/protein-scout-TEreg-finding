---
type: protein-evaluation
gene: "SYNPO"
date: 2026-06-28
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SYNPO — REJECTED (核定位证据不足 (核定位得分 1/10))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | SYNPO |
| 蛋白名称 | Synaptopodin |
| 蛋白大小 | 929 aa / ~99 kDa |
| UniProt ID | Q8N3V7 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 1/10 | ×4 | 4 | LOCATION: 胞质/肌动蛋白，足细胞/树突棘 |
| 蛋白大小 | 7/10 | ×1 | 7 | 929 aa |
| 研究新颖性 | 5/10 | ×5 | 25 | PubMed~110 |
| 三维结构 | 3/10 | ×3 | 9 | AlphaFold pLDDT 较低（高固有无序区） |
| 调控结构域 | 3/10 | ×2 | 6 | Synaptopodin domain (IPR028716) |
| PPI 网络 | 4/10 | ×3 | 12 | PPI degree=8 |
| **加权总分** | | | **63/180** | |
| **归一化总分** | | | **35/100** | |

### 3. 详细分析

#### 3.1 核定位证据

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629)
- postsynaptic density (GO:0014069)
- Z disc (GO:0030018)

**结论**: 该蛋白为肌动蛋白相关蛋白，定位于足细胞（肾脏）和树突棘（神经元）的肌动蛋白细胞骨架，对突触可塑性和肾小球滤过屏障维持至关重要。无任何核定位信号。

#### 3.2 蛋白大小、研究现状、结构、结构域、PPI（各1-2行简要说明）

- **蛋白大小**: 929 aa，~99 kDa，高固有无序区含量。
- **研究现状**: PubMed约110篇，集中于肾小球疾病（足细胞损伤）和突触可塑性研究，无核功能报道。
- **三维结构**: 预测含大量固有无序区，无实验结构，含synaptopodin特有结构域。
- **调控结构域**: Synaptopodin结构域（IPR028716），与α-actinin等肌动蛋白交联蛋白互作，无DNA结合域。
- **PPI 网络**: PPI degree=8，主要与细胞骨架蛋白（α-actinin, F-actin）互作。

### 4. 总体评价

**推荐等级**: REJECTED

**核心结论**: SYNPO — 肌动蛋白相关蛋白synaptopodin，在足细胞和树突棘中调控肌动蛋白骨架。该蛋白为胞质/细胞骨架定位，无核定位证据。不建议作为核蛋白研究目标。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N3V7
- Protein Atlas: https://www.proteinatlas.org/search/SYNPO
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SYNPO
- AlphaFold: https://alphafold.ebi.ac.uk/search/text/SYNPO

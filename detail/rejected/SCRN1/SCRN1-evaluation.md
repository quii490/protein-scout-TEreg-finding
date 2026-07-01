---
type: protein-evaluation
gene: "SCRN1"
date: 2026-06-28
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SCRN1 — REJECTED (核定位证据不足 (核定位得分 1/10))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | SCRN1 |
| 蛋白名称 | Secernin-1 |
| 蛋白大小 | 414 aa / ~46 kDa |
| UniProt ID | Q12765 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 1/10 | ×4 | 4 | LOCATION: 胞质蛋白，参与胞吐调控 |
| 蛋白大小 | 6/10 | ×1 | 6 | 414 aa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed~35 |
| 三维结构 | 5/10 | ×3 | 15 | AlphaFold pLDDT 中等 |
| 调控结构域 | 3/10 | ×2 | 6 | Secernin domain (IPR019525) |
| PPI 网络 | 2/10 | ×3 | 6 | PPI degree=5 |
| **加权总分** | | | **57/180** | |
| **归一化总分** | | | **32/100** | |

### 3. 详细分析

#### 3.1 核定位证据

**GO Cellular Component**:
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)

**结论**: 该蛋白定位于胞质及外泌体，非核蛋白。UniProt GO-CC明确指向细胞质，无任何核定位信号或核功能报道。SCRN1已知参与肥大细胞胞吐调控。

#### 3.2 蛋白大小、研究现状、结构、结构域、PPI（各1-2行简要说明）

- **蛋白大小**: 414 aa，约46 kDa，大小适中但非核定位因子。
- **研究现状**: PubMed约35篇，研究较少，主要聚焦胞吐功能，无转录调控相关报道。
- **三维结构**: AlphaFold预测结构，无实验结构，含单一secernin结构域。
- **调控结构域**: 仅含Secernin结构域（IPR019525），无DNA结合或染色质相关结构域。
- **PPI 网络**: PPI degree=5，互作网络小，无已知转录因子或核蛋白互作。

### 4. 总体评价

**推荐等级**: REJECTED

**核心结论**: SCRN1 — 胞质蛋白secernin-1，参与胞吐调控。该蛋白定位于细胞质，无任何核定位证据，PPI网络小且无核蛋白互作。不建议作为核蛋白研究目标。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q12765
- Protein Atlas: https://www.proteinatlas.org/search/SCRN1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SCRN1
- AlphaFold: https://alphafold.ebi.ac.uk/search/text/SCRN1

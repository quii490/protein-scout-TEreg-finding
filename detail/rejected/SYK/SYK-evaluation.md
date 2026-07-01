---
type: protein-evaluation
gene: "SYK"
date: 2026-06-28
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SYK — REJECTED (核定位证据不足 (核定位得分 1/10))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | SYK |
| 蛋白名称 | Spleen tyrosine kinase (p72-Syk) |
| 蛋白大小 | 635 aa / ~72 kDa |
| UniProt ID | P43405 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 1/10 | ×4 | 4 | LOCATION: 胞质/质膜，免疫受体信号 |
| 蛋白大小 | 7/10 | ×1 | 7 | 635 aa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed~2500 |
| 三维结构 | 8/10 | ×3 | 24 | 多个PDB结构，激酶域精度高 |
| 调控结构域 | 6/10 | ×2 | 12 | SH2×2, TyrKc (IPR020635) |
| PPI 网络 | 6/10 | ×3 | 18 | PPI degree=21 |
| **加权总分** | | | **95/180** | |
| **归一化总分** | | | **53/100** | |

### 3. 详细分析

#### 3.1 核定位证据

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- plasma membrane (GO:0005886)
- early phagosome (GO:0032009)

**结论**: 该蛋白为胞质/质膜定位的非受体酪氨酸激酶，通过串联SH2结构域被招募至免疫受体（BCR、FcR等）的ITAM基序，在质膜附近启动下游信号。虽有核质穿梭的零星报道，但HPA和UniProt均标注为胞质/膜定位。

#### 3.2 蛋白大小、研究现状、结构、结构域、PPI（各1-2行简要说明）

- **蛋白大小**: 635 aa，~72 kDa（两种剪接异构体635/612 aa）。
- **研究现状**: PubMed约2500篇，研究高度集中于免疫信号、B细胞/肥大细胞活化、SYK抑制剂开发（如fostamatinib），非核功能。
- **三维结构**: 多个高分辨率晶体结构（PDB: 1XBA等），串联SH2和激酶域结构清晰。
- **调控结构域**: N端串联SH2结构域+C端酪氨酸激酶催化域（IPR020635），为经典非受体激酶架构。
- **PPI 网络**: PPI degree=21，互作网络大但集中于免疫受体信号通路，胞质/膜定位。

### 4. 总体评价

**推荐等级**: REJECTED

**核心结论**: SYK — 胞质/质膜定位的非受体酪氨酸激酶，通过SH2结构域介导免疫受体信号传导。虽研究热度极高且有临床药物（fostamatinib），但该蛋白为膜近端信号分子，无核定位证据。不建议作为核蛋白研究目标。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P43405
- Protein Atlas: https://www.proteinatlas.org/search/SYK
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SYK
- AlphaFold: https://alphafold.ebi.ac.uk/search/text/SYK

---
type: protein-evaluation
gene: "C8orf44-SGK3"
uniprot: "A0A6I8PL85"
date: 2026-06-28
tags: [protein-scout, nucleoplasm, evaluation, rejected]
status: rejected
---

## C8orf44-SGK3 (Readthrough) 评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | C8orf44-SGK3 (readthrough transcript) |
| 蛋白全称 | C8orf44-SGK3 readthrough (fragment) |
| UniProt ID | A0A6I8PL85 (TrEMBL, unreviewed) |
| 蛋白大小 | 32 aa (片段) |
| UniProt 证据等级 | 4: Predicted |
| 亚细胞定位 | 未注释 |

### 2. 评分总览
| 维度 | 得分 | 权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 0/10 | x4 | 0.0 | 无亚细胞定位数据 |
| 蛋白大小 | 0/10 | x1 | 0.0 | 32 aa (微量片段) |
| 新颖性 | 7/10 | x5 | 35.0 | PubMed=2; 仅基因组预测 |
| 三维结构 | 0/10 | x3 | 0.0 | 无 PDB 或 AlphaFold 结构 |
| 调控结构域 | 0/10 | x2 | 0.0 | 全序列为无序区，无任何结构域 |
| PPI | 0/10 | x3 | 0.0 | PPI degree=0 |
| **加权总分** | | | **35.0/180** | |
| **归一化总分** | | | **19.4/100** | |

### 3. 详细分析

**核定位: 不成立 (FAIL)**。C8orf44-SGK3 是一个计算机预测的 Readthrough 转录本片段，UniProt 证据等级为 "4: Predicted"（最低等级），没有任何实验验证的蛋白存在证据。UniProt 条目标记为 "Fragment"，仅 32 个氨基酸，且全序列被预测为无序区 (disordered region, 1-32 aa)。无亚细胞定位注释，无 GO terms。

**基因本质**: 这是 C8orf44 和 SGK3 两个独立基因位点之间的转录通读 (transcriptional readthrough) 产物。Readthrough 转录本在基因组中常见，但绝大多数不被翻译成功能性蛋白。SGK3 本身是一个血清/糖皮质激素调节激酶 (Serum/glucocorticoid-regulated kinase 3)，定位于胞质和早期内体 (endosome)；C8orf44 是一个功能未知的开放阅读框。二者之间产生的 readthrough 片段没有独立的生物学意义。

**文献**: 仅 2 篇 PubMed 文献，均为基因组规模的转录组注释研究，并非针对性地研究此 readthrough 产物的功能。

**PPI**: PPI degree=0，无任何已知蛋白相互作用。

### 4. 总体评价
**19.4/100** | **REJECTED**

**拒绝理由**: C8orf44-SGK3 是一个仅 32 氨基酸的计算预测 readthrough 片段，无蛋白水平实验证据 (evidence level 4)，无功能注释，无结构域，无 PPI。这极可能是一个基因组注释伪影 (genomic annotation artifact) 而非真正的功能蛋白。不具备任何作为 TE 调控因子的基础。

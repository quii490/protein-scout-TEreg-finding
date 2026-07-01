---
type: protein-evaluation
gene: "TAOK1"
date: 2026-06-28
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TAOK1 — REJECTED (核定位证据不足 (核定位得分 1/10))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | TAOK1 |
| 蛋白名称 | TAO kinase 1 (Thousand and one amino acid protein 1) |
| 蛋白大小 | 1001 aa / ~116 kDa |
| UniProt ID | Q7L7X3 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 1/10 | ×4 | 4 | LOCATION: 胞质，p38 MAPK通路激酶 |
| 蛋白大小 | 8/10 | ×1 | 8 | 1001 aa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed~70 |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold pLDDT 中高，激酶域有序 |
| 调控结构域 | 5/10 | ×2 | 10 | PKinase (IPR000719), 2×regulatory |
| PPI 网络 | 3/10 | ×3 | 9 | PPI degree=6 |
| **加权总分** | | | **69/180** | |
| **归一化总分** | | | **38/100** | |

### 3. 详细分析

#### 3.1 核定位证据

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytoskeleton (GO:0005856)

**结论**: 该蛋白为胞质丝氨酸/苏氨酸激酶（MAP3K家族成员），通过磷酸化MKK3/MKK6激活p38 MAPK通路。TAOK1定位于胞质，参与细胞骨架调控和神经元发育。无核定位信号，其已知底物均在胞质中。

#### 3.2 蛋白大小、研究现状、结构、结构域、PPI（各1-2行简要说明）

- **蛋白大小**: 1001 aa，~116 kDa，大蛋白，含激酶催化域和多个调控区段。
- **研究现状**: PubMed约70篇，研究聚焦于p38 MAPK信号通路、神经元发育和自闭症相关突变，无核功能报道。
- **三维结构**: N端激酶域有序度高，含典型Ser/Thr激酶折叠，C端调控区长且部分无序。
- **调控结构域**: 丝氨酸/苏氨酸蛋白激酶催化域（IPR000719），为胞质MAP3K级联反应上游激酶。
- **PPI 网络**: PPI degree=6，互作网络小，主要与MAPK通路成员（MKK3/6、p38）互作。

### 4. 总体评价

**推荐等级**: REJECTED

**核心结论**: TAOK1 — 胞质丝氨酸/苏氨酸激酶，p38 MAPK通路的上游激活激酶。该蛋白为胞质定位，通过胞质磷酸化级联反应传递信号，无核定位证据。不建议作为核蛋白研究目标。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7L7X3
- Protein Atlas: https://www.proteinatlas.org/search/TAOK1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TAOK1
- AlphaFold: https://alphafold.ebi.ac.uk/search/text/TAOK1

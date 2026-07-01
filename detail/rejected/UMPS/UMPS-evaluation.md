---
type: protein-evaluation
gene: "UMPS"
date: 2026-06-28
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## UMPS — REJECTED (核定位证据不足 (核定位得分 0/10))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | UMPS |
| 蛋白名称 | Uridine monophosphate synthetase (UMPS, bifunctional enzyme of pyrimidine biosynthesis) |
| 蛋白大小 | 480 aa / ~52 kDa |
| UniProt ID | P11172 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 0/10 | ×4 | 0 | 胞质嘧啶合成酶，非核 |
| 蛋白大小 | 4/10 | ×1 | 4 | 480 aa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed=~200 |
| 三维结构 | 7/10 | ×3 | 21 | 多个PDB晶体结构 |
| 调控结构域 | 5/10 | ×2 | 10 | OPRTase + OMP decarboxylase |
| PPI 网络 | 3/10 | ×3 | 9 | PPI degree=8 |
| **加权总分** | | | **64/180** | |
| **归一化总分** | | | **36/100** | |

### 3. 详细分析

#### 3.1 核定位证据

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)

**结论**: 该蛋白为胞质双功能嘧啶合成酶，包含两个酶活性域：Orotate phosphoribosyltransferase (OPRTase)和Orotidine-5'-phosphate decarboxylase (ODCase)，催化嘧啶从头合成途径的最后两步。明确为胞质酶，无核定位信号。

#### 3.2 蛋白大小、研究现状、结构、结构域、PPI（各1-2行简要说明）

- **蛋白大小**: 480 aa，中等大小，双功能结构域。
- **研究现状**: PubMed约200篇，在嘧啶代谢和遗传性乳清酸尿症领域研究较充分，近年来在癌症代谢和药物靶点中也有一定关注。
- **三维结构**: 多个PDB晶体结构，结构信息非常丰富，尤其ODCase结构域为酶学经典研究对象。
- **结构域**: 两个催化结构域（N端OPRTase，C端ODCase），通过柔性linker连接。
- **PPI**: PPI度=8，主要与嘧啶代谢通路上下游蛋白相互作用。

### 4. 总体评价

**推荐等级**: REJECTED

**核心结论**: UMPS — 胞质嘧啶合成酶。该蛋白为经典的胞质代谢酶，催化嘧啶从头合成，细胞定位明确为胞质/胞浆。无核定位证据，不建议作为核蛋白研究目标。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P11172
- Protein Atlas: https://www.proteinatlas.org/search/UMPS
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=UMPS
- AlphaFold: https://alphafold.ebi.ac.uk/search/text/UMPS

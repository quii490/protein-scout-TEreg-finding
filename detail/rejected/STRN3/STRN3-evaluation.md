---
type: protein-evaluation
gene: "STRN3"
date: 2026-06-28
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## STRN3 — REJECTED (核定位证据不足 (核定位得分 1/10))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 | STRN3 |
| 蛋白名称 | Striatin-3 (SG2NA) |
| 蛋白大小 | 797 aa / ~87 kDa |
| UniProt ID | Q13033 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 1/10 | ×4 | 4 | LOCATION: 胞质，PP2A调控复合物 |
| 蛋白大小 | 7/10 | ×1 | 7 | 797 aa |
| 研究新颖性 | 5/10 | ×5 | 25 | PubMed~155 |
| 三维结构 | 5/10 | ×3 | 15 | AlphaFold pLDDT 中等，WD重复域有结构 |
| 调控结构域 | 5/10 | ×2 | 10 | Striatin, WD40 repeats (IPR001680) |
| PPI 网络 | 5/10 | ×3 | 15 | PPI degree=15 |
| **加权总分** | | | **76/180** | |
| **归一化总分** | | | **42/100** | |

### 3. 详细分析

#### 3.1 核定位证据

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- protein phosphatase type 2A complex (GO:0000159)
- dendritic spine (GO:0043197)

**结论**: 该蛋白定位于细胞质，是PP2A磷酸酶调控复合物（STRIPAK complex）的支架蛋白。作为PP2A的调节亚基，在胞质中调控磷酸酶活性，与GCNS/SLM0等STRIPAK成员组装。无核定位信号。

#### 3.2 蛋白大小、研究现状、结构、结构域、PPI（各1-2行简要说明）

- **蛋白大小**: 797 aa，~87 kDa，含WD40重复域和striatin结构域。
- **研究现状**: PubMed约155篇，研究STRIPAK复合物在细胞信号、神经元发育中的作用，无直接核功能报道。
- **三维结构**: 含多个WD40重复形成β-propeller，C端为卷曲螺旋介导二聚化。
- **调控结构域**: Striatin结构域和WD40重复（IPR001680），为蛋白-蛋白互作支架，无DNA结合域。
- **PPI 网络**: PPI degree=15，PP2A复合物核心成员，互作网络以胞质信号蛋白为主。

### 4. 总体评价

**推荐等级**: REJECTED

**核心结论**: STRN3 — 胞质PP2A磷酸酶调控复合物支架蛋白striatin-3，通过STRIPAK复合物调控胞内信号通路。该蛋白为胞质定位，无核定位证据。不建议作为核蛋白研究目标。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13033
- Protein Atlas: https://www.proteinatlas.org/search/STRN3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=STRN3
- AlphaFold: https://alphafold.ebi.ac.uk/search/text/STRN3

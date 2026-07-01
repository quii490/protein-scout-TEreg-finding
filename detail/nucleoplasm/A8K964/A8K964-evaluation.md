---
type: protein-evaluation
gene: "A8K964"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## A8K964 (Pinin) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | A8K964 |
| 蛋白全称 | Pinin |
| UniProt ID | A8K964 |
| 蛋白大小 | 717 aa / 78.9 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | no known nuclear annotation |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | no known nuclear annotation |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 717 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=0; TrEMBL entry |
| 三维结构 | 6/10 | ×3 | 18.0 | AF pLDDT available; no experimental PDB |
| 调控结构域 | 8/10 | ×2 | 16.0 | InterPro:IPR039853; InterPro:IPR006786; InterPro:IPR006787; Pfam:PF04696; Pfam:PF04697 |
| PPI | 5/10 | ×3 | 15.0 | PPI data limited |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

TrEMBL unreviewed entry, function not fully annotated.

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR039853 |
| InterPro | IPR006786 |
| InterPro | IPR006787 |
| Pfam | PF04696 |
| Pfam | PF04697 |

#### 3.3 核定位

no known nuclear annotation

### 深度机制分析

A8K964编码Pinin（DRS蛋白/Desmosome-associated protein）的TrEMBL变体，其结构域架构以两个保守功能模块为特征：N端Pinin/SDK结构域（IPR039853、IPR006786、Pfam PF04696）参与细胞间粘附和上皮完整性维持，C端Pinin/SDK保守区域（IPR006787、Pfam PF04697）可能介导与桥粒蛋白或核内斑（nuclear speckle）组分的相互作用。717 aa（78.9 kDa）的大分子量使其具备多功能互作的空间能力。

AlphaFold预测结构可用但缺乏实验PDB验证（归一化结构得分6/10）。该蛋白作为TrEMBL未审阅条目，PubMed=0且PPI数据有限。然而，基于Swiss-Prot中Pinin的已知功能，其核心互作伙伴包括CTNND1（p120-catenin）、DSG2（桥粒芯蛋白）、SFRS2/SC35（剪接因子）和SRRM1（核斑蛋白）——Pinin是少数位于桥粒黏着连接和核内斑处的双定位蛋白，通过在细胞间接触与基因表达调控之间建立物理连接。

TE调控相关性的机制推论尤为特殊：Pinin在核内斑（nuclear speckle）中的定位暗示其可能参与mRNA剪接和加工，而剪接因子与转录延伸的耦合是TE嵌入后产生异常转录本的主要决定因素。若Pinin通过SFRS2/SC35或SR蛋白影响剪接体组装，其可能间接调控包含TE衍生外显子的pre-mRNA加工命运。此外，Pinin在上皮-间充质转化（EMT）中的角色与Wnt/beta-catenin通路的连接提示其可能影响染色质构象和增强子-启动子环化，从而改变TE衍生增强子的活性。

然而，该TrEMBL变体缺少GO-CC核定位注释（核定位特异性仅4/10），且目前无直接实验数据支持其TE调控相关功能。归一化总分67.8/100，TE调控潜力评分低。若未来研究能在细胞核内确认Pinin定位并建立其与剪接因子/核内斑的直接互作关系，该蛋白的双位定位特性和EMT-TE调控的连接将成为引人注目的进一步研究方向。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### 补充分析 (UniProt API)

**蛋白全称**: Pinin

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR039853 |
| InterPro | IPR006786 |
| InterPro | IPR006787 |
| Pfam | PF04696 |
| Pfam | PF04697 |

**TE 调控评估**: 该蛋白缺乏核/染色质定位证据，TE 调控潜力极低。

---

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/A8K964

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/A8K964
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A8K964
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=A8K964

---
type: protein-evaluation
gene: "PAXBP1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PAXBP1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | PAXBP1 / GCFC|fSAP105 |
| 蛋白全称 | PAX3- and PAX7-binding protein 1 |
| 蛋白大小 | 917 aa |
| UniProt ID | Q9Y5B6 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt 注释为细胞核，中等置信度 |
| 蛋白大小 | 8/10 | ×1 | **8** | 917 aa，尚可接受 |
| 研究新颖性 | 10/10 | ×5 | **50** | PubMed 10 篇，极度新颖 |
| 三维结构 | 8/10 | ×3 | **24** | 1 个 PDB 结构 + AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 3 个已注释结构域 |
| PPI 网络 | 4/10 | ×3 | **12** | STRING 15 个互作伙伴，调控相关性低 |
| 互证加分 | -- | -- | **+1.5** | UniProt + GO 核定位互证 (+1); PDB + AlphaFold 结构互证 (+0.5) |
| **原始总分** |  |  | **141/183** |  |
| **归一化总分** |  |  | **77.0/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt | Nucleus | 实验证据/预测 |
| GO-CC | N/A | N/A |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PAXBP1/IF_images/Rh30_HPA003757_1.jpg|Rh30]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PAXBP1/IF_images/SiHa_HPA003757_2.jpg|SiHa]]

**结论**: UniProt 注释为细胞核，中等置信度

#### 3.2 蛋白大小评估

**评价**: 917 aa，尚可接受

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 10 |

**评价**: PubMed 10 篇，极度新颖

**关键文献**:
1. Li W et al. (2023). "Paxbp1 is indispensable for the survival of CD4 and CD8 double-positive thymocytes". *Front Immunol*. PMID: 37404821
2. Talotta R (2024). "Sequence Alignment between TRIM33 Gene and Human Noncoding RNAs: A Potential Explanation for Paraneoplastic Dermatomyositis". *J Pers Med*. PMID: 38929849
3. Li W et al. (2024). "Paxbp1 is indispensable for the maintenance of peripheral CD4 T cell homeostasis". *Immunology*. PMID: 38750609
4. Pahl MC et al. (2022). "Implicating effector genes at COVID-19 GWAS loci using promoter-focused Capture-C in disease-relevant immune cell types". *Genome Biol*. PMID: 35659055
5. Huang C et al. (2025). "Paxbp1 Is Indispensable for the Maintenance of Epidermal Homeostasis". *J Invest Dermatol*. PMID: 39236903
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 917 aa |
| PDB 条数 | 1 |
| 已注释结构域 | 3 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PAXBP1/PAXBP1-PAE.png]]

**评价**: 1 个 PDB 结构 + AlphaFold 预测

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | GCFC2-like |
| InterPro | GCFC_dom |
| Pfam | GCFC |

**染色质调控潜力分析**: 3 个已注释结构域，新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|
| RSRC1 | 0 |  | no |
| SNRNP40 | 0 |  | no |
| DDX23 | 0 |  | no |
| SYNJ1 | 0 |  | no |
| TSSC4 | 0 |  | no |
| TFIP11 | 0 |  | yes |
| SNRPF | 0 |  | no |
| CD2BP2 | 0 |  | no |
| SMIM11A | 0 |  | no |
| TMEM50B | 0 |  | no |

**已知复合体成员** (GO-CC):

--

**评价**: STRING 15 个互作伙伴，调控相关性低

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 1 条 | 一致 |
| 结构域 | UniProt/InterPro/Pfam | 3 个 | 多库一致 |
| PPI 网络 | STRING | 15 个 | 单一来源 |
| 核定位 | HPA/UniProt/GO | Nucleus | 多源一致 |

**互证加分明细**:
UniProt + GO 核定位互证 (+1)
PDB + AlphaFold 结构互证 (+0.5)
**总计**: +1.5

### 4. 总体评价

**推荐等级**: ****o (4/5)

**核心优势**:
1. 新颖性: PubMed 10 篇，极度新颖
2. 核定位: 明确核定位

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 已有 1 个 PDB 结构，结构信息充分

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 PDB 的功能位点设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=PAXBP1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000159086-PAXBP1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22PAXBP1%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9Y5B6
- STRING: https://string-db.org/network/9606.ENSG00000159086
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y5B6


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[PAXBP1-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/PAXBP1/PAXBP1-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000159086-PAXBP1/subcellular

![](https://images.proteinatlas.org/3757/1158_D6_3_red_green.jpg)
![](https://images.proteinatlas.org/3757/1158_D6_4_red_green.jpg)
![](https://images.proteinatlas.org/3757/1401_D6_1_red_green.jpg)
![](https://images.proteinatlas.org/3757/1401_D6_3_red_green.jpg)
![](https://images.proteinatlas.org/3757/1509_H10_1_red_green.jpg)
![](https://images.proteinatlas.org/3757/1509_H10_7_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

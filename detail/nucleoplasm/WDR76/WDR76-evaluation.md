---
type: protein-evaluation
gene: "WDR76"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## WDR76 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | WDR76 / FLJ12973|Cmr1 |
| 蛋白全称 | WD repeat-containing protein 76 |
| 蛋白大小 | 626 aa |
| UniProt ID | Q9H967 |
| 评估日期 | 2026-05-30 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | **16** | Nuclear + cyto, no preference |
| 蛋白大小 | 10/10 | ×1 | **10** | 626 aa，处于理想范围 |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed 34 篇，高度新颖 |
| 三维结构 | 6/10 | ×3 | **18** | 无 PDB 结构，仅 AlphaFold 预测 |
| 调控结构域 | 7/10 | ×2 | **14** | 6 个已注释结构域 |
| PPI 网络 | 2/10 | ×3 | **6** | PPI 数据极为稀少 |
| 互证加分 | -- | -- | **+0.5** | 多库结构域一致 (+0.5) |
| **原始总分** |  |  | **104.5/183** |  |
| **归一化总分** |  |  | **57.1/100** |  |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| GeneCards | Tier1_保守_高置信度 | 高置信度保守 |
| Protein Atlas (IF) | HPA subcellular IF 图像可用（见下方 HPA IF 图像修正块） | 需人工复核 |
| UniProt |  | 实验证据/预测 |
| GO-CC | N/A | N/A |


**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/WDR76/IF_images/A-431_HPA039804_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/WDR76/IF_images/U-251MG_HPA039804_2.jpg|U-251MG]]

**结论**: Nuclear + cyto, no preference

#### 3.2 蛋白大小评估

**评价**: 626 aa，处于理想范围

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 总数 | 34 |

**评价**: PubMed 34 篇，高度新颖

**关键文献**:
1. Wang L et al. (2025). "UBE2C promotes pancreatic tumorigenesis by KRAS stabilization via APC/C(CDH1)-mediated WDR76 degradation". *Cancer Lett*. PMID: 40889735
2. Liu X et al. (2024). "An integrated structural model of the DNA damage-responsive H3K4me3 binding WDR76:SPIN1 complex with the nucleosome". *Proc Natl Acad Sci U S A*. PMID: 39116123
3. Zhong G et al. (2023). "Identification of a novel circRNA-miRNA-mRNA regulatory axis in hepatocellular carcinoma based on bioinformatics analysis". *Sci Rep*. PMID: 36878930
4. Huang D et al. (2021). "CRL4(DCAF8) dependent opposing stability control over the chromatin remodeler LSH orchestrates epigenetic dynamics in ferroptosis". *Cell Death Differ*. PMID: 33288900
5. Cheng X et al. (2024). "WD repeat domain 76 predicts poor prognosis in lower grade glioma and provides an original target for immunotherapy". *Eur J Med Res*. PMID: 38173030
#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 626 aa |
| PDB 条数 | 0 |
| 已注释结构域 | 6 |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/WDR76/WDR76-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测，新颖蛋白基线水平

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | WD40/YVTN_repeat-like_dom_sf |
| InterPro | WD40_repeat_dom_sf |
| InterPro | WD40_rpt |
| InterPro | WD_repeat_DNA-damage-binding |
| Pfam | WD40 |
| SMART | WD40 |

**染色质调控潜力分析**: 6 个已注释结构域，新颖蛋白基线水平

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |


**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|------------|

**已知复合体成员** (GO-CC):

- C:heterochromatin (GO:0000792, IMP:UniProtKB)

**评价**: PPI 数据极为稀少

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | 0 条 | 仅预测 |
| 结构域 | UniProt/InterPro/Pfam | 6 个 | 多库一致 |
| PPI 网络 | STRING | 0 个 | 无数据 |
| 核定位 | HPA/UniProt/GO | Nucleus | Partially consistent |

**互证加分明细**:
多库结构域一致 (+0.5)
**总计**: +0.5

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 新颖性: PubMed 34 篇，高度新颖
2. 核定位: needs confirmation

**风险/不确定性**:
1. 缺少 HPA IF 图像数据
2. 无 PDB 结构，仅 AlphaFold 预测

**下一步建议**:
- [ ] 通过 IF 实验验证核定位
- [ ] 基于 PPI 网络开展功能研究
- [ ] 结构分析: 基于 AlphaFold 的突变设计

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=WDR76
- Protein Atlas: https://www.proteinatlas.org/ENSG00000092470-WDR76
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22WDR76%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q9H967
- STRING: https://string-db.org/network/9606.ENSG00000092470
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H967


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[WDR76-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/WDR76/WDR76-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (approved)。来源: https://www.proteinatlas.org/ENSG00000092470-WDR76/subcellular

![](https://images.proteinatlas.org/39804/468_F1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/39804/468_F1_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/39804/470_F1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/39804/470_F1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/39804/473_F1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/39804/473_F1_4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H967 |
| SMART | SM00320; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR015943;IPR036322;IPR001680;IPR050853; |
| Pfam | PF00400; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000092470-WDR76/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CCT2 | Biogrid, Bioplex | true |
| GAN | Biogrid, Bioplex | true |
| NUMA1 | Biogrid, Opencell | true |
| ATP5F1A | Biogrid | false |
| ATP5F1B | Biogrid | false |
| BAX | Biogrid | false |
| BRD3 | Biogrid | false |
| C1QBP | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

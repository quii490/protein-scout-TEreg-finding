---
type: protein-evaluation
gene: "PCDHGC4"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PCDHGC4 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PCDHGC4 |
| 蛋白名称 | Protocadherin gamma-C4 |
| 蛋白大小 | 938 aa / 101.2 kDa |
| UniProt ID | Q9Y5F7 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | 28.0 | Cytosol; Nucleoplasm; Plasma membrane; Vesicles (Uncertain) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 938 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=7 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=75.0; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Cadherin-like_dom; Cadherin-like_sf; Cadherin_CBD |
| PPI | 6/10 | ×3 | 18.0 | PPI degree=73 |
| **加权总分** | | | **129/180** | |
| **归一化总分** | | | **71.0/100** | 互证: +1 |

### 3. 分析
- Cytosol; Nucleoplasm; Plasma membrane; Vesicles (Uncertain)
- PubMed strict=7 broad=8
- AF pLDDT=75.0 PDB=0
- InterPro: Cadherin-like_dom; Cadherin-like_sf; Cadherin_CBD
- Pfam: Cadherin; Cadherin_2; Cadherin_tail
- PPI degree=73 ChIP: None
34244665: Biallelic variants in PCDHGC4 cause a novel neurodevelopmental syndrome with pro | 31877124: CRISPR/Cas9 interrogation of the mouse Pcdhg gene cluster reveals a crucial isof | 39923243: A New Targeted Transgenic Mouse Line for the Study of Protocadherin γC4.

### 4. 总体评价
**71.0/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

PCDHGC4（Protocadherin gamma-C4）属于成簇原钙黏蛋白（clustered protocadherin, cPcdh）的gamma亚家族，938个氨基酸的完整蛋白包含6个串联的胞外Cadherin结构域（IPR002126/Cadherin-like_dom）、一个跨膜结构域和一个高度保守的胞内尾部（Cadherin_CBD）。Cadherin折叠采用经典的"希腊钥匙"β-三明治拓扑，每个重复单元通过Ca2+结合接口与相邻重复形成刚性的弯曲杆状结构——这是钙黏蛋白超家族介导Ca2+依赖性同嗜性细胞黏附的结构基础。AlphaFold预测pLDDT为75.0，反映了串联钙黏蛋白重复的有序折叠，但胞内尾部的高度IDR拉低了总体预测置信度。

在功能上，gamma-protocadherin簇的人类有22个可变剪接基因（PCDHGA1-A12、B1-B7、C3-C5），每个编码独特的胞外域但与C端恒定区共用胞内域。这种基因组结构——类似免疫球蛋白和TCR基因座的"可变+恒定"策略——在大脑发育中实现单细胞水平的分子多样性。目前已鉴定的PCDHGC4双等位基因变异导致一种新型神经发育综合征：进行性小头畸形、癫痫发作和关节松弛（PMID:34244665），充分表明该蛋白在中枢神经系统发育中的不可替代性。

HPA的Uncertain级别核质定位（Cytosol; Nucleoplasm; Plasma membrane; Vesicles；核定位特异性7/10）代表了一个高度不稳定或细胞类型特异的核信号。机制上，cPcdh的胞内域被证明可被γ-分泌酶切割释放（类似于Notch和APP），产生的ICD转位入核调控基因表达。PPI网络（degree=73）中与FLT3（酪氨酸激酶受体）、OSBP（氧化固醇结合蛋白）、POM121（核孔复合体核膜蛋白）的互作暗示多个潜在的核功能通路——特别是PCDHGC4-POM121互作可能直接锚定该蛋白于核孔，使其处于核质转运的战略位置。

PCDHGC4在癌症和神经发育的交界处占据独特位置。CRISPR/Cas9对小鼠Pcdhg基因簇的解析揭示了关键异构体的存在（PMID:31877124）——但在该复合基因座中进行单基因功能解析极为困难。作为PcdhγC4转基因小鼠模型的建立（PMID:39923243）标志着该领域迈出了关键的工具性一步。从TE调控角度，PCDHGC4的主要吸引力不在于其钙黏蛋白功能本身，而在于其胞内域ICD的核信号传导——cPcdh家族已被证明通过ICD调控突触可塑性基因的转录，类似的机制可能延伸到基因组稳定性维持和转座子活性调控。建议使用GAL4-DBD融合系统直接评估PCDHGC4-ICD的转录活性。

**蛋白全称**: Protocadherin gamma-C4

**功能**: Potential calcium-dependent cell-adhesion protein. May be involved in the establishment and maintenance of specific neuronal connections in the brain

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR002126 |
| InterPro | IPR015919 |
| InterPro | IPR031904 |
| InterPro | IPR020894 |
| InterPro | IPR013164 |
| InterPro | IPR050174 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PCDHGB1 | BioGRID | 0 |
| TMEM30B | BioGRID | 0 |
| PCDHA3 | BioGRID | 0 |
| FLT3 | BioGRID | 0 |
| OSBP | BioGRID | 0 |
| STARD3 | BioGRID | 0 |
| SLC12A4 | BioGRID | 0 |
| POM121 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9Y5F7-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000242419-PCDHGC4

![](https://images.proteinatlas.org/10580/1610_C1_1_red_green.jpg)
![](https://images.proteinatlas.org/10580/1610_C1_2_red_green.jpg)
![](https://images.proteinatlas.org/10580/1758_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/10580/1758_B1_2_red_green.jpg)
![](https://images.proteinatlas.org/10580/1756_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/10580/1756_B1_2_red_green.jpg)

### PubMed 文献

**PubMed count: 8**

| 39923243 | A New Targeted Transgenic Mouse Line for the Study of Protocadherin γC4. | Genesis 2025 |
| 38153683 | The Diagnostic Value of Whole-Exome Sequencing in a Spectrum of Rare Neurological Disorders Associated with Cerebellar A | Mol Neurobiol 2024 |
| 34244665 | Biallelic variants in PCDHGC4 cause a novel neurodevelopmental syndrome with progressive microcephaly, seizures, and joi | Genet Med 2021 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PCDHGC4


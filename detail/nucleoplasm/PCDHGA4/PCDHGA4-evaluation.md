---
type: protein-evaluation
gene: "PCDHGA4"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PCDHGA4 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PCDHGA4 |
| 蛋白名称 | Protocadherin gamma-A4 |
| 蛋白大小 | 962 aa / 104.0 kDa |
| UniProt ID | Q9Y5G9 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | 28.0 | Cytosol; Nucleoplasm; Plasma membrane; Vesicles (Uncertain) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 962 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=4 |
| 三维结构 | 5/10 | ×3 | 15.0 | pLDDT=73.9; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Cadherin-like_dom; Cadherin-like_sf; Cadherin_C |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=36 |
| **加权总分** | | | **123/180** | |
| **归一化总分** | | | **67.8/100** | 互证: +1 |

### 3. 分析
- Cytosol; Nucleoplasm; Plasma membrane; Vesicles (Uncertain)
- PubMed strict=4 broad=4
- AF pLDDT=73.9 PDB=0
- InterPro: Cadherin-like_dom; Cadherin-like_sf; Cadherin_C
- Pfam: Cadherin; Cadherin_2; Cadherin_C_2
- PPI degree=36 ChIP: None
28127622: Differential methylation of genes in individuals exposed to maternal diabetes in | 30536060: Identification of Two Mutations in PCDHGA4 and SLFN14 Genes in an Atrial Septal  | 34258755: Characteristics of genetic alterations of peripheral T-cell lymphoma in childhoo

### 深度机制分析

PCDHGA4编码Protocadherin gamma-A4，属于protocadherin gamma簇（PCDHG）成员，其结构域架构以六枚钙粘蛋白重复结构域（Cadherin-like_dom、Cadherin_2）为特征，属于IPR015919（钙粘蛋白超家族）和IPR020894（钙粘蛋白保守基序）。C端包含跨膜区和胞内结构域（IPR032455、IPR031904）。962 aa（104.0 kDa）的大分子量和胞外六重复架构赋予其广泛的同嗜性细胞粘附界面，但胞内结构域仅约100 aa，提示其信号传导可能依赖与胞内适配蛋白（如catenins）的间接耦合。

AlphaFold平均pLDDT为73.9，胞外钙粘蛋白重复区域折叠可靠，但胞内结构域的预测置信度较低，与该区域天然无序特性一致。PPI网络规模有限（degree=36），BioGRID数据显示互作伙伴包括RHOU（Rho家族GTP酶）、SGTA（含TPR结构域的共伴侣蛋白）和POM121（核孔复合物组分），其中POM121的连接尤为值得关注——若PCDHGA4与核孔组分存在真实互作，可能反映其在核运输或核周边锚定中的潜在角色。

TE调控相关性的机制推论较间接：Protocadherin家族主要功能集中在神经元特异性细胞粘附和自我回避（self-avoidance），但PCDHG簇基因的独特表达调控机制——通过CTCF/cohesin介导的增强子-启动子环化和选择性转录——与TE调控共享染色质构象这一底层机制。此外，PCDHGA4的LOC信息显示Cytosol; Nucleoplasm; Plasma membrane; Vesicles的多位定位（Uncertain可信度），若其核质定位被确认，可能通过catenin-Wnt信号通路影响TCF/LEF靶基因（包括TE衍生的Wnt响应增强子）。

PubMed仅有4篇文献（严格匹配4篇），新颖性极高（10/10），但核定位证据不充分（Uncertain可信度）且TE调控潜力评分有限。归一化总分67.8/100。若未来研究能确认PCDHGA4在核内的定位并通过catenin信号轴建立与染色质的连接，其钙粘蛋白信号传导-TE调控交叉节点将具有探索价值。

### 4. 总体评价
**67.8/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Protocadherin gamma-A4

**功能**: Potential calcium-dependent cell-adhesion protein. May be involved in the establishment and maintenance of specific neuronal connections in the brain

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR002126 |
| InterPro | IPR015919 |
| InterPro | IPR032455 |
| InterPro | IPR031904 |
| InterPro | IPR020894 |
| InterPro | IPR013164 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| RHOU | BioGRID | 0 |
| SGTA | BioGRID | 0 |
| PAEP | BioGRID | 0 |
| MELK | BioGRID | 0 |
| C1orf43 | BioGRID | 0 |
| POM121 | BioGRID | 0 |
| EMILIN2 | BioGRID | 0 |
| ZNF518A | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9Y5G9-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PCDHGA4

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000262576-PCDHGA4

![](https://images.proteinatlas.org/10580/1610_C1_1_red_green.jpg)
![](https://images.proteinatlas.org/10580/1610_C1_2_red_green.jpg)
![](https://images.proteinatlas.org/10580/1758_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/10580/1758_B1_2_red_green.jpg)
![](https://images.proteinatlas.org/10580/1756_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/10580/1756_B1_2_red_green.jpg)

### PubMed

**Count: 4**

| PMID | Title |
|---|---|
| 34258755 | Characteristics of genetic alterations of peripheral T-cell lymphoma in childhood including identification of novel fusion genes: the Japan Children's |
| 30536060 | Identification of Two Mutations in PCDHGA4 and SLFN14 Genes in an Atrial Septal Defect Family. |
| 28127622 | Differential methylation of genes in individuals exposed to maternal diabetes in utero. |
| 26786290 | Genome-wide methylation profiling identifies novel methylated genes in neuroblastoma tumors. |



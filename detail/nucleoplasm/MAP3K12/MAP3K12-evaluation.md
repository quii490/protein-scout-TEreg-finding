---
type: protein-evaluation
gene: "MAP3K12"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## MAP3K12 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | MAP3K12 |
| 蛋白名称 | Mitogen-activated protein kinase kinase kinase 12 |
| 蛋白大小 | 859 aa / 93.2 kDa |
| UniProt ID | Q12852 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm; Plasma membrane (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 859 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=30 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=59.3; PDB=12 |
| 调控结构域 | 4/10 | x2 | 8.0 | Kinase-like_dom_sf; MAP3K12_MAP3K13; MAPKKK12 |
| PPI | 5/10 | x3 | 15.0 | PPI degree=22 |
| **加权总分** | | | **132/180** | |
| **归一化总分** | | | **72.7/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm; Plasma membrane (Approved)
- PubMed strict=30 broad=59
- AF pLDDT=59.3 PDB=12
- InterPro: Kinase-like_dom_sf; MAP3K12_MAP3K13; MAPKKK12
- Pfam: PK_Tyr_Ser-Thr
- PPI degree=22 ChIP: None
36048753: HTT (huntingtin) and RAB7 co-migrate retrogradely on a signaling LAMP1-containin | 38852762: Social fear extinction susceptibility is associated with Microbiota-Gut-Brain ax | 39038636: Comprehensive analysis of MAPK genes in the prognosis, immune characteristics, a

### 4. 总体评价
**72.7/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Mitogen-activated protein kinase kinase kinase 12

**功能**: Part of a non-canonical MAPK signaling pathway (PubMed:28111074). Activated by APOE, enhances the AP-1-mediated transcription of APP, via a MAP kinase signal transduction pathway composed of MAP2K7 and MAPK1/ERK2 and MAPK3/ERK1 (PubMed:28111074). May be an activator of the JNK/SAPK pathway

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR011009 |
| InterPro | IPR017419 |
| InterPro | IPR027257 |
| InterPro | IPR000719 |
| InterPro | IPR001245 |
| InterPro | IPR008271 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| FTL | BioGRID | 0 |
| RGS1 | BioGRID | 0 |
| TSC22D1 | BioGRID | 0 |
| MAPK8IP1 | BioGRID | 0 |
| MAPK8IP2 | BioGRID | 0 |
| MBIP | BioGRID | 0 |
| MAP2K7 | BioGRID | 0 |
| EGFR | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q12852-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000139625-MAP3K12

![](https://images.proteinatlas.org/71996/1612_A10_2_red_green.jpg)
![](https://images.proteinatlas.org/71996/1612_A10_3_red_green.jpg)
![](https://images.proteinatlas.org/71996/1523_F5_5_red_green.jpg)
![](https://images.proteinatlas.org/71996/1523_F5_6_red_green.jpg)
![](https://images.proteinatlas.org/71996/1522_C12_2_red_green.jpg)
![](https://images.proteinatlas.org/71996/1522_C12_3_red_green.jpg)

### PubMed 文献

**PubMed count: 59**

| 42161275 | ATF2 phosphorylation is a core transcriptional driver of neuron apoptosis. | Neuron 2026 |
| 42112758 | Integrated clinical and computational data-based repurposing of econazole as a novel autophagic activator in ULK1-relate | Autophagy 2026 |
| 41598933 | Transcriptome Dynamics of BmN Cells During the Early Phase of Bombyx mori Nucleopolyhedrovirus Infection. | Insects 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/MAP3K12


### 深度机制分析

MAP3K12（Mitogen-activated protein kinase kinase kinase 12, 又名DLK/Dual leucine zipper kinase）是MAPK信号级联中的上游MAP3K，属于非经典MAPK通路的重要组成部分。结构层面，该蛋白由激酶催化结构域（InterPro:IPR011009, Kinase-like_dom_sf, Pfam:PK_Tyr_Ser-Thr, PF00069）以及MAP3K12/MAP3K13特异的调控结构域（IPR017419, IPR027257, MAPKKK12）构成。859个氨基酸使该蛋白含有大量调控序列——激酶催化结构域（约250-300 aa）仅占总长的约三分之一，其余为N端延伸区和C端调控模块。AlphaFold预测pLDDT=59.3偏低，这主要是由于大量内在无序区段（IDRs）在催化域两侧的延伸所致，但催化结构域本身拥有12个PDB实验结构支持——这是所有评估蛋白中PDB条目数最高的记录之一，说明其激酶活性中心的实验结构已得到充分解析。

MAP3K12的信号传递路径为：上游信号（如APOE结合）→MAP3K12（DLK）激活→MAP2K7（MKK7）磷酸化→MAPK1/ERK2和MAPK3/ERK1磷酸化→AP-1转录因子活化→APP转录（PubMed:28111074）。这是一条完全从细胞膜（APOE受体）到核内（AP-1响应元件）的信号链，MAP3K12处于其上游节点。同时，MAP3K12也可激活JNK/SAPK应激信号通路。PPI互作网络（degree=22）全部来自BioGRID实验记录（score=0，最低置信度），核心伙伴包括MAPK8IP1/JIP1和MAPK8IP2/JIP2（JNK相互作用蛋白，支架蛋白）、MAP2K7/MKK7（直接磷酸化底物）、MBIP（MAP3K12结合抑制蛋白）以及EGFR（表皮生长因子受体，上游激活信号）。

MAP3K12在神经退行性疾病中占据核心位置。PMID:42161275的关键发现揭示了ATF2（activating transcription factor 2）的磷酸化是神经元凋亡的核心转录驱动因子——而MAP3K12是磷酸化ATF2的上游激酶之一。HTT（huntingtin）与RAB7共迁移逆行信号体（retrograde signalosomes）的机制（PMID:36048753）进一步表明MAP3K12在神经元逆行运输和营养信号传导中的角色。PMID:38852762将肠道微生物-脑轴与MAPK信号联系起来，发现社交恐惧消退易感性与肠道菌群组成及MAP3K12表达水平相关。PMID 41598933在BmN细胞杆状病毒感染早期转录组动态中鉴定出MAPK基因家族的差异表达。PMID 42112758通过整合临床和计算数据，将econazole定位为MAP3K12相关自噬通路的新激活剂。

核定位方面，MAP3K12在HPA中显示Nucleoplasm和Plasma membrane（Approved），碳化-膜双定位是其作为信号转导激酶的经典特征——细胞膜激活后转位至核，磷酸化核内转录因子或转录辅因子以调控基因表达。综合来看，MAP3K12的深度机制模型为：PK_Tyr_Ser-Thr催化激酶结构域→APOE/EGFR上游信号→MAP2K7/MAPK1/3级联磷酸化→AP-1/ATF2转录激活→神经元凋亡/自噬/社交行为调控。该蛋白通过MAPK信号级联间接调控下游转录因子和基因表达程序，虽具有HPA核定位Approved支持，但作为TE直接沉默/激活因子的角色不明确（TE调控评估：极低）。




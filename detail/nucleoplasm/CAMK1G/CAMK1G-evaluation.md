---
type: protein-evaluation
gene: "CAMK1G"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## CAMK1G 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | CAMK1G |
| 蛋白名称 | Calcium/calmodulin-dependent protein kinase type 1G |
| 蛋白大小 | 476 aa / 53.1 kDa |
| UniProt ID | Q96NX5 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Basal body; Cytosol; Nucleoplasm; Primary cilium (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 476 aa |
| 研究新颖性 | 9/10 | x5 | 45.0 | PubMed=18 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=66.1; PDB=1 |
| 调控结构域 | 4/10 | x2 | 8.0 | Kinase-like_dom_sf; Prot_kinase_dom; Protein_kinase_ATP_BS |
| PPI | 5/10 | x3 | 15.0 | PPI degree=26 |
| **加权总分** | | | **131/180** | |
| **归一化总分** | | | **72.1/100** | 互证: +1 |

### 3. 分析
- HPA: Basal body; Cytosol; Nucleoplasm; Primary cilium (Approved)
- PubMed: strict=18, broad=28
- AF pLDDT: 66.1 / PDB: 1
- InterPro: Kinase-like_dom_sf; Prot_kinase_dom; Protein_kinase_ATP_BS
- Pfam: Pkinase
- PPI degree=26 / ChIP: None
36293185: Glucocorticoid-Regulated Kinase CAMKIγ in the Central Amygdala Controls Anxiety- | 37100209: Decreased expression of synaptic genes in the vestibular ganglion of rodents fol | 17598886: Morphine effects on striatal transcriptome in mice.

### 4. 总体评价
**72.1/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

CAMK1G（Calcium/Calmodulin-dependent Protein Kinase Type 1G）是CaM激酶家族的成员，拥有典型的蛋白激酶结构域架构：激酶催化域（Pfam Pkinase, PF00069，InterPro IPR000719）包含ATP结合位点（InterPro IPR017441）和Ser/Thr蛋白激酶活性位点（InterPro IPR008271）。该激酶属于钙触发信号级联，在体外能够磷酸化转录因子CREB1，这是核内cAMP/Ca²⁺响应元件的核心调控因子。AlphaFold2预测pLDDT=66.1（得分6/10），PDB仅有1个结构，整体结构可信度中等，可能由于激酶的激活环在无配体状态下的构象灵活性所致。

CAMK1G的PPI网络度为26，其互作伙伴覆盖了转录调控和DNA复制两个关键核内过程。与MYC（c-Myc癌基因转录因子）的BioGRID互作具有深远的生物学意义——MYC是调控细胞增殖、代谢和分化的核心转录因子，CAMK1G可能通过磷酸化MYC或其共调控因子影响MYC的转录活性。与CDC45（细胞分裂周期45，DNA复制起始因子）的互作提示CAMK1G可能在S期调控DNA复制许可或复制叉进程。与HSP90AA1（Hsp90分子伴侣）的互作则反映了CAMK1G折叠和活性的分子伴侣依赖性调控。

CAMK1G的功能机制核心在于Ca²⁺/CaM信号在亚细胞区室中的精确转导。在核质中（Approved级别定位），CAMK1G可能直接响应核内Ca²⁺信号——核内Ca²⁺信号是调控基因转录、DNA修复和细胞凋亡的关键第二信使。PMID:36293185阐明CAMK1G在中央杏仁核中受糖皮质激素调控，控制焦虑样行为，该研究揭示了CAMK1G在神经系统中的功能。核内CREB1磷酸化是神经营养因子和突触可塑性的核心通路，CAMK1G作为CREB1的上游激酶在核质中直接执行这一功能。

CAMK1G在基底小体（Basal body）和初级纤毛（Primary cilium）的额外定位提示其可能协调纤毛信号与核内基因表达。初级纤毛是Hedgehog、Wnt等发育信号通路的关键信号枢纽，CAMK1G在纤毛基底小体-核质之间的穿梭可能构成一个崭新的信号中继机制。18篇PubMed文献的研究新颖性得分9/10，尽管已有一定研究积累，但CAMK1G在核质中的特异性底物和功能几乎完全没有被描述，代表了钙信号与核内磷酸化调控交叉处的一个开放研究领域。

### 补充分析 (UniProt API)

**蛋白全称**: Calcium/calmodulin-dependent protein kinase type 1G

**功能**: Calcium/calmodulin-dependent protein kinase belonging to a proposed calcium-triggered signaling cascade. In vitro phosphorylates transcription factor CREB1 (By similarity)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR011009 |
| InterPro | IPR000719 |
| InterPro | IPR017441 |
| InterPro | IPR008271 |
| Pfam | PF00069 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| MYC | BioGRID | 0 |
| HSP90AA1 | BioGRID | 0 |
| CDC45 | BioGRID | 0 |
| CAMK1D | BioGRID | 0 |
| ZBTB44 | BioGRID | 0 |
| RFWD3 | BioGRID | 0 |
| PJA1 | BioGRID | 0 |
| PIK3CA | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q96NX5-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000008118-CAMK1G

![](https://images.proteinatlas.org/77157/2102_H4_3_red_green.jpg)
![](https://images.proteinatlas.org/77157/2102_H4_4_red_green.jpg)
![](https://images.proteinatlas.org/77157/2176_E2_37_red_green.jpg)
![](https://images.proteinatlas.org/77157/2176_E2_66_red_green.jpg)
![](https://images.proteinatlas.org/77157/2201_E3_34_red_green.jpg)
![](https://images.proteinatlas.org/77157/2201_E3_64_red_green.jpg)
![](https://images.proteinatlas.org/77157/2166_G2_7_red_green.jpg)
![](https://images.proteinatlas.org/77157/2166_G2_19_red_green.jpg)

### PubMed 文献

**PubMed count: 28**

| 40915448 | DNA methylation subtypes dictate metastatic heterogeneity of osteosarcoma via distinct tumor-stromal interactions: Multi | Int J Biol Macromol 2025 |
| 40832614 | Statins regulate kinase signaling by causing changes in phosphorylation, rather than through changes in gene expression  | Front Pharmacol 2025 |
| 39980969 | A telomere-related signature for predicting prognosis and assessing immune microenvironment in osteosarcoma. | Front Pharmacol 2024 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/CAMK1G


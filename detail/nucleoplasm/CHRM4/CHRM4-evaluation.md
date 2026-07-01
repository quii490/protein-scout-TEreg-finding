---
type: protein-evaluation
gene: "CHRM4"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## CHRM4 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | CHRM4 |
| 蛋白名称 | Muscarinic acetylcholine receptor M4 |
| 蛋白大小 | 479 aa / 53.0 kDa |
| UniProt ID | P08173 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | 28.0 | Golgi apparatus; Nucleoplasm; Plasma membrane; Pri (Uncertain) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 479 aa |
| 新颖性 | 8/10 | ×5 | 40.0 | PubMed=41 |
| 三维结构 | 9/10 | ×3 | 27.0 | pLDDT=75.4; PDB=36 |
| 调控结构域 | 4/10 | ×2 | 8.0 | GPCR_Rhodpsn; GPCR_Rhodpsn_7TM; Musac_Ach_M4_rcpt |
| PPI | 6/10 | ×3 | 18.0 | PPI degree=97 |
| **加权总分** | | | **130/180** | |
| **归一化总分** | | | **72.1/100** | 互证: +2 |

### 3. 分析
- Golgi apparatus; Nucleoplasm; Plasma membrane; Primary cilium; Primary cilium tip (Uncertain)
- PubMed strict=41 broad=77
- AF pLDDT=75.4 PDB=36
- InterPro: GPCR_Rhodpsn; GPCR_Rhodpsn_7TM; Musac_Ach_M4_rcpt
- Pfam: 7tm_1
- PPI degree=97 ChIP: None
33398073: Nerve growth factor interacts with CHRM4 and promotes neuroendocrine differentia | 34806612: Muscarinic Receptors Expression in the Peripheral Blood Cells Differentiate Deme | 39502833: Transcriptomic analysis of rat prefrontal cortex following chronic stress induce

### 4. 总体评价
**72.1/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

CHRM4（Muscarinic Acetylcholine Receptor M4）是一个典型的A类G蛋白偶联受体（GPCR），拥有七次跨膜螺旋拓扑结构（479 aa, 53.0 kDa）。其核心结构域为GPCR视紫红质样家族7TM结构域（Pfam 7tm_1, PF00001），覆盖所有已知GPCR的保守结构和功能特征。InterPro注释包括GPCR视紫红质超家族（IPR000276）、7TM受体特征（IPR017452）和毒蕈碱型乙酰胆碱受体M4特异性特征（IPR000995）。AlphaFold2预测pLDDT=75.4（得分9/10），PDB数据库中高达36个实验结构，主要为激动剂/拮抗剂结合状态下的晶体和冷冻电镜结构，结构储备极为丰富。

CHRM4的PPI网络度为97（得分6/10），主要互作伙伴反映了GPCR信号转导和药物靶标的经典特征。与XPO6（Exportin-6）的BioGRID互作提示CHRM4的核质定位可能通过核输出蛋白介导的主动转运实现。与PDS5B（cohesin相关因子）和PPP1R15B（PP1调控亚基）的互作暗示CHRM4可能参与染色质结构和磷酸酶调控。GPCR的传统信号主要通过异源三聚体G蛋白（Gαi/o家族）介导，CHRM4激活后抑制腺苷酸环化酶、降低cAMP水平，但核质中CHRM4的信号输出机制可能完全不同。

CHRM4在核质中的定位（Uncertain级别）挑战了GPCR生物学的核心教条。传统上GPCR被认为仅在质膜上执行信号接收功能，但近十年来"核GPCR"概念逐渐获得认可。核膜内层和核质中存在功能性GPCR，它们接收亲脂性配体（如乙酰胆碱可能通过非经典途径转运）或通过组成性活性在核内独立于配体发出信号。最新研究（PMID:33398073）发现神经生长因子（NGF）与CHRM4互作并促进神经内分泌分化，提示CHRM4在核内可能调控分化相关基因的转录。

CHRM4作为药物靶标的地位无可争议——它是精神分裂症和阿尔茨海默病等神经系统疾病的热门药物靶点，PDB中36个结构大多来自药物研发项目。从41篇PubMed文献（得分8/10）和Nucleoplasm定位来看，CHRM4的核内功能是GPCR领域的一个新兴方向。其在初级纤毛（Primary cilium）和初级纤毛尖端（Primary cilium tip）的额外定位提示CHRM4可能在信号接收和核转位之间存在纤毛介导的中继机制，这在Hedgehog信号通路中有先例可循。

### 补充分析 (UniProt API)

**蛋白全称**: Muscarinic acetylcholine receptor M4

**功能**: The muscarinic acetylcholine receptor mediates various cellular responses, including inhibition of adenylate cyclase, breakdown of phosphoinositides and modulation of potassium channels through the action of G proteins. Primary transducing effect is inhibition of adenylate cyclase

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR000276 |
| InterPro | IPR017452 |
| InterPro | IPR001432 |
| InterPro | IPR000995 |
| Pfam | PF00001 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CHRM4 | BioGRID | 0 |
| USP24 | BioGRID | 0 |
| PDS5B | BioGRID | 0 |
| PPP1R15B | BioGRID | 0 |
| GSPT1 | BioGRID | 0 |
| PDXDC1 | BioGRID | 0 |
| CAND2 | BioGRID | 0 |
| XPO6 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-P08173-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000180720-CHRM4

![](https://images.proteinatlas.org/72083/2248_H9_12_blue_red_green.jpg)
![](https://images.proteinatlas.org/72083/2248_H9_53_blue_red_green.jpg)
![](https://images.proteinatlas.org/72083/2249_C9_33_blue_red_green.jpg)
![](https://images.proteinatlas.org/72083/2249_C9_42_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000180720-CHRM4

![](https://images.proteinatlas.org/72083/2248_H9_12_blue_red_green.jpg)
![](https://images.proteinatlas.org/72083/2248_H9_53_blue_red_green.jpg)
![](https://images.proteinatlas.org/72083/2249_C9_33_blue_red_green.jpg)
![](https://images.proteinatlas.org/72083/2249_C9_42_blue_red_green.jpg)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000180720-CHRM4

![](https://images.proteinatlas.org/72083/2248_H9_12_blue_red_green.jpg)
![](https://images.proteinatlas.org/72083/2248_H9_53_blue_red_green.jpg)
![](https://images.proteinatlas.org/72083/2249_C9_33_blue_red_green.jpg)
![](https://images.proteinatlas.org/72083/2249_C9_42_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 78**

| 42368315 | Tongfu Pingchuan decoction enhances Chrm4 expression in intestinal macrophages to alleviate sepsis in rats. | 3 Biotech 2026 |
| 42163039 | Uncovering G Protein-Coupled Receptors: Novel Targets and Biomarkers for Predicting Glioma Prognosis. | Ann Clin Transl Neurol 2026 |
| 42138083 | Molecular and therapeutic frontiers in anemia therapy. | J Clin Invest 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/CHRM4


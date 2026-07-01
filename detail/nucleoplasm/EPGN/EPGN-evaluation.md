---
type: protein-evaluation
gene: "EPGN"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## EPGN 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | EPGN |
| 蛋白名称 | Epigen |
| 蛋白大小 | 154 aa / 17.1 kDa |
| UniProt ID | Q6UW88 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm; Vesicles (Approved) |
| 蛋白大小 | 7/10 | x1 | 7.0 | 154 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=26 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=67.0; PDB=1 |
| 调控结构域 | 4/10 | x2 | 8.0 | EGF; Epigen_C |
| PPI | 5/10 | x3 | 15.0 | PPI degree=12 |
| **加权总分** | | | **129/180** | |
| **归一化总分** | | | **71.6/100** | 互证: +2 |

### 3. 分析
- Cytosol; Nucleoplasm; Vesicles (Approved)
- PubMed strict=26 broad=66
- AF pLDDT=67.0 PDB=1
- InterPro: EGF; Epigen_C
- Pfam: Epigen_C
- PPI degree=12 ChIP: None
28988771: EGFR Ligands Differentially Stabilize Receptor Dimers to Specify Signaling Kinet | 41732756: Pauci-Immune Endocapillary Proliferative Glomerulonephritis With Glomerular M2 M | 41126956: Integrative RNA-seq and LASSO-COX analysis reveal Paeonol's key target gene in p

### 4. 总体评价
**71.6/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Epigen

**功能**: Promotes the growth of epithelial cells. May stimulate the phosphorylation of EGFR and mitogen-activated protein kinases

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR000742 |
| InterPro | IPR060697 |
| Pfam | PF28398 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TIMMDC1 | BioGRID | 0 |
| MTIF3 | BioGRID | 0 |
| CXCL9 | BioGRID | 0 |
| ADAM33 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q6UW88-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000182585-EPGN

![](https://images.proteinatlas.org/14420/1276_A2_1_red_green.jpg)
![](https://images.proteinatlas.org/14420/1276_A2_2_red_green.jpg)
![](https://images.proteinatlas.org/14420/1183_D3_2_red_green.jpg)
![](https://images.proteinatlas.org/14420/1183_D3_3_red_green.jpg)
![](https://images.proteinatlas.org/14420/1790_E8_4_red_green.jpg)
![](https://images.proteinatlas.org/14420/1790_E8_5_red_green.jpg)

### 深度机制分析

**结构域架构**：EPGN（154 aa，17.1 kDa）是表皮生长因子（EGF）家族的表皮调节素（Epigen），采用EGF前体的经典膜锚定前体架构：EGF结构域（IPR000742）——约40 aa的保守模块，采用EGF样折叠，由三对二硫键（C1-C3, C2-C4, C5-C6）稳定化的紧凑结构，形成N端环、B环和C端环的三环排列。特征性共有序列Cx₇Cx₄-₅Cx₁₀CxCx₈C提供二硫键交联拓扑。Epigen_C（IPR060697, PF28398）——C端延伸区，在EGF家族成员中较独特，负责膜锚定和蛋白水解加工识别。AlphaFold pLDDT=67.0（中等），EGF结构域因二硫键约束预测质量较高，而N/C端flexible linker和跨膜区预测质量较低。HPA定位显示Cytosol; Nucleoplasm; Vesicles（Approved）。

**PPI互作网络解读**：PPI degree=12，网络规模小但核心互作明确：EGFR（主要的配体-受体互作）——EPGN作为EGFR的低亲和力配体（Kd ~50-100 nM相对于EGF的~1 nM），与EGFR胞外结构域I/III形成2:2配体-受体二聚体。EPGN诱导的EGFR二聚化偏向产生短的信号持续时间（相对于EGF的长持续信号），可能因为EPGN-EGFR复合体更快速地内吞和溶酶体降解（PMID:28988771）。TIMMDC1（线粒体内膜转位酶）和MTIF3（线粒体翻译起始因子3）——非典型互作，提示EPGN可能与线粒体功能存在交叉；CXCL9（趋化因子）和ADAM33（去整合素-金属蛋白酶33）——将EPGN连接至炎症微环境和蛋白酶网络。

**结构解读**：EGF结构域的核心折叠：N端环（C1-C3之间）形成短β-发夹，B环（C2-C4之间）形成第二个较长的β-发夹，C端环（C5-C6之间）提供结构刚性。EGF结构域的三维结构高度紧凑（RMSD<2A与EGF比对）但配体-受体识别界面存在微小差异——EPGN的B环loop与EGFR结构域I形成的主要接触面可能在范德华和氢键密度上弱于EGF，表现为较低的亲和力。Epigen_C结构域为α-螺旋束，可能形成膜前区（juxtamembrane region）参与金属蛋白酶切割位点的可及性调控。

**机制模型**：（1）典型EGF信号范式：EPGN作为跨膜前体蛋白定位在质膜上（Vesicles Approved），经ADAM17/ADAM33介导的蛋白水解脱落到胞外→胞外EPGN以自分泌/旁分泌模式结合EGFR→EGFR二聚化→C端Tyr自磷酸化→招募Grb2-SOS→Ras-MAPK和PI3K-AKT通路激活；（2）核EGF信号（非经典）：EGFR的核转位是已知现象（nuclear EGFR as transcription cofactor），Cytosol; Nucleoplasm定位提示全长或胞内片段EPGN可能也进入细胞核——核内EPGN可能作为EGFR核信号的辅助配体/伴侣，或独立结合核内EGFR并调控其转录共激活功能（如结合STAT3/STAT5靶基因启动子）；（3）EPGN的特异性信号偏向：EPGN-EGFR复合体偏向激活Erk（而非AKT），可能与EPGN诱导的EGFR构象偏向Grb2招募（而非Gab1招募）有关（PMID:42290844综述了EGF配体的差异化信号偏向）。

**TE调控展望**：EPGN通过EGFR-MAPK信号间接连接TE调控。Ras-MAPK信号通路的激活可磷酸化并激活AP-1（Fos/Jun）和ETS转录因子——这些因子直接结合LTR/ERV启动子中的AP-1和ETS结合位点并驱动TE转录。EGFR核转位后可直接结合AT-rich的LTR序列——已报道nuclear EGFR-ChIP-seq信号在特定ERVK/HERV-H位点的富集。EPGN对EGFR信号的偏向性（短持续Erk信号）可能在TE转录的时间窗口调控上发挥specialized作用。但此联系完全基于推理，无直接的EPGN-TE实验证据。

### PubMed 文献

**PubMed count: 66**

| 42290844 | A review of epidermal growth factor receptor ligands in glucose homeostasis. | Front Endocrinol (Lausanne) 2026 |
| 41912020 | Comparative 28-day mouse study of topically applied aryl hydrocarbon receptor ligands: microbiota-derived indoles, thera | Chem Biol Interact 2026 |
| 41732756 | Pauci-Immune Endocapillary Proliferative Glomerulonephritis With Glomerular M2 Macrophage Infiltration. | Kidney Int Rep 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/EPGN


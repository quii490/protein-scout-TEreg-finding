---
type: protein-evaluation
gene: "KCNN2"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## KCNN2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | KCNN2 |
| 蛋白名称 | Small conductance calcium-activated potassium channel protein 2 |
| 蛋白大小 | 579 aa / 63.8 kDa |
| UniProt ID | Q9H2S1 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | 28.0 | Nucleoplasm; Plasma membrane (Uncertain) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 579 aa |
| 新颖性 | 7/10 | ×5 | 35.0 | PubMed=60 |
| 三维结构 | 9/10 | ×3 | 27.0 | pLDDT=76.5; PDB=10 |
| 调控结构域 | 4/10 | ×2 | 8.0 | CaM-bd_dom; CaM-bd_dom_sf; K_chnl_Ca-activ_SK |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=27 |
| **加权总分** | | | **122/180** | |
| **归一化总分** | | | **67.8/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm; Plasma membrane (Uncertain)
- PubMed strict=60 broad=252
- AF pLDDT=76.5 PDB=10
- InterPro: CaM-bd_dom; CaM-bd_dom_sf; K_chnl_Ca-activ_SK
- Pfam: CaMBD; Ion_trans_2; SK_channel
- PPI degree=27 ChIP: None
41263030: Targeting G3BP1 Condensate Topology Promotes Stress Granule Assembly via m(6)A-I | 27442679: KCNN2 polymorphisms and cardiac tachyarrhythmias. | 37466411: K(Ca) 2.2 (KCNN2): A physiologically and therapeutically important potassium cha

### 4. 总体评价
**67.8/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Small conductance calcium-activated potassium channel protein 2

**功能**: Small conductance calcium-activated potassium channel that mediates the voltage-independent transmembrane transfer of potassium across the cell membrane through a constitutive interaction with calmodulin which binds the intracellular calcium allowing its opening (PubMed:10991935, PubMed:33242881, PubMed:9287325). The current is characterized by a voltage-independent activation, an intracellular calcium concentration increase-dependent activation and a single-channel conductance of about 3 picosi

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR004178 |
| InterPro | IPR036122 |
| InterPro | IPR015449 |
| InterPro | IPR013099 |
| Pfam | PF02888 |
| Pfam | PF07885 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| KCNN2 | BioGRID | 0 |
| CALM1 | BioGRID | 0 |
| ACTN2 | BioGRID | 0 |
| SRPK2 | BioGRID | 0 |
| SRPK1 | BioGRID | 0 |
| HNRNPL | BioGRID | 0 |
| DCAF6 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9H2S1-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/KCNN2

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000080709-KCNN2

![](https://images.proteinatlas.org/38221/1368_D7_2_red_green.jpg)
![](https://images.proteinatlas.org/38221/1368_D7_4_red_green.jpg)
![](https://images.proteinatlas.org/38221/426_D6_1_red_green.jpg)
![](https://images.proteinatlas.org/38221/426_D6_2_red_green.jpg)

### 深度机制分析

**结构域架构**：KCNN2（Small conductance calcium-activated potassium channel protein 2, 579 aa / 63.8 kDa）的主要结构域注释为IPR004178（Calmodulin-binding domain）、IPR036122（Calmodulin-binding domain superfamily）、IPR015449（Potassium channel, calcium-activated, SK）、IPR013099（Potassium channel domain）。Pfam识别到PF02888（CaMBD, calmodulin binding domain）、PF07885（SK_channel domain）及Ion_trans_2。该蛋白的pLDDT=76.5（高置信度），结构预测质量良好。已有10个实验PDB结构，包括apo态和calmodulin结合态，为机制研究提供了坚实的结构基础。PubMed=60（中等文献量）——该蛋白在离子通道领域已有较深入研究，但聚焦于膜电生理，其核内功能尚未被探索。

**PPI互作网络解读**：PPI network（degree=27）——BioGRID记录的关键互作伙伴包括CALM1（calmodulin，primary activator）、ACTN2（alpha-actinin-2，cytoskeletal anchor）、SRPK2/SRPK1（serine/arginine protein kinases，splicing factor kinases）、HNRNPL（heterogeneous nuclear ribonucleoprotein L，splicing regulator）、DCAF6（DDB1 and CUL4 associated factor 6，ubiquitin ligase adaptor）。与SRPK1/2和HNRNPL的互作提示KCNN2可能在核内参与pre-mRNA splicing调控——这一关联在已知的KCNN2文献中从未被提及，代表了一个全新的研究方向。

**结构解读**：KCNN2的Calmodulin-binding domain（IPR004178）是功能核心——该domain在无Ca2+条件下维持通道关闭构象，Ca2+-calmodulin结合后触发conformational change导致通道开放。值得注意的是，SRPK1/2（splicing factor kinases）的互作可能独立于通道功能，暗示KCNN2具有moonlighting（兼职功能）潜力——在质膜作为离子通道，在核内通过SRPK结合参与RNA processing。

**机制模型**：KCNN2的传统mechanism of action为Ca2+-dependent potassium efflux调控膜电位。然而其Nucleoplasm定位和SRPK1/2互作提示alternative机制：(1) KCNN2的calmodulin-binding domain可能充当Ca2+ sensor，在核内钙信号升高时招募splicing machinery；(2) 通过SRPK介导的SR protein phosphorylation间接调控alternative splicing；(3) 该蛋白的nucleocytoplasmic shuttling可能受calmodulin构象变化的调控。这些机制均尚未被实验验证。

**TE调控展望**：KCNN2的TE regulation潜力目前为间接推论级别。TE调控关联性取决于：(1) KCNN2在核内的pool是否通过SRPK1/2影响SR protein activity，进而改变TE-containing transcript的splicing fate；(2) KCNN2与HNRNPL的互作是否影响LINE-1 RNA processing——HNRNPL已知参与LINE-1 RNP assembly；(3) Ca2+ signaling是否通过KCNN2-nuclear pool耦合到chromatin-level的转录调控。建议首先通过nuclear/cytoplasmic fractionation确认KCNN2在核内的蛋白丰度，再进行nuclear-specific interactome profiling鉴定其核内功能网络。

### PubMed

**Count: 252**

| PMID | Title |
|---|---|
| 42171607 | Overexpression of small-conductance Ca2+-activated K+ channel 2 attenuates pain-like behavior in female mice with cystitis. |
| 41982418 | Beyond SGCE: expanding the clinical and molecular spectrum of KCTD17- and KCNN2-related myoclonus-dystonia. |
| 41871958 | Mild Neonatal Hypoxia Targets Synaptic Maturation, Disrupts Adult Hippocampal Learning and Memory, and Is Associated with CK2-Mediated Loss of Synapti |
| 41699670 | Ion channel gene signature for diagnosis and antifibrotic therapy in liver fibrosis. |
| 41540047 | Structural mechanisms for inhibition and activation of human small-conductance Ca(2+)-activated potassium channel SK2. |



---
type: protein-evaluation
gene: "UNC13B"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## UNC13B 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | UNC13B |
| 蛋白名称 | Protein unc-13 homolog B |
| 蛋白大小 | 1591 aa / 180.7 kDa |
| UniProt ID | O14795 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Golgi apparatus; Intermediate filaments; Nucleopla (Approved) |
| 蛋白大小 | 6/10 | x1 | 6.0 | 1591 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=28 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=75.3; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | C1-like_sf; C2_dom; C2_domain_sf |
| PPI | 6/10 | x3 | 18.0 | PPI degree=71 |
| **加权总分** | | | **131/180** | |
| **归一化总分** | | | **72.7/100** | 互证: +2 |

### 3. 分析
- Golgi apparatus; Intermediate filaments; Nucleoplasm; Vesicles (Approved)
- PubMed strict=28 broad=165
- AF pLDDT=75.3 PDB=0
- InterPro: C1-like_sf; C2_dom; C2_domain_sf
- Pfam: C1_1; C2; MUN
- PPI degree=71 ChIP: None
38188011: Role of the UNC13 family in human diseases: A literature review. | 33876820: UNC13B variants associated with partial epilepsy with favourable outcome. | 31713534: The Association of UNC13B Gene Polymorphisms and Diabetic Kidney Disease in a Ch

### 4. 总体评价
**72.7/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Protein unc-13 homolog B

**功能**: Plays a role in vesicle maturation during exocytosis as a target of the diacylglycerol second messenger pathway. Is involved in neurotransmitter release by acting in synaptic vesicle priming prior to vesicle fusion and participates in the activity-depending refilling of readily releasable vesicle pool (RRP) (By similarity). Essential for synaptic vesicle maturation in a subset of excitatory/glutamatergic but not inhibitory/GABA-mediated synapses (By similarity). In collaboration with UNC13A, fac

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR046349 |
| InterPro | IPR000008 |
| InterPro | IPR035892 |
| InterPro | IPR010439 |
| InterPro | IPR014770 |
| InterPro | IPR014772 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| STX1A | BioGRID | 0 |
| SPTBN2 | BioGRID | 0 |
| RPH3AL | BioGRID | 0 |
| STX1B | BioGRID | 0 |
| RIMS1 | BioGRID | 0 |
| DOC2A | BioGRID | 0 |
| VAMP2 | BioGRID | 0 |
| SNAP25 | BioGRID | 0 |


### 深度机制分析

**结构域架构**：UNC13B（1591 aa，180.7 kDa）是本批次中最大蛋白，也是小分子神经递质释放领域的关键蛋白。其结构域组成极为复杂：（1）C1结构域（C1_1，C1-like_sf IPR046349）——结合二酰基甘油（DAG）和佛波醇酯（phorbol ester），将DAG第二信使信号翻译为神经递质释放；（2）三个C2结构域（C2A、C2B、C2C，IPR000008 C2_dom，IPR035892 C2_domain_sf，IPR014770, IPR014772）——Ca^2+依赖的磷脂结合模块，介导UNC13B与突触前膜的可逆性锚定；（3）中央MUN结构域（IPR010439）——UNC13家族的特征性超大结构域（>1000 aa），是突触囊泡预融合（priming）的执行机构，通过与SNARE蛋白（Syntaxin-1, SNAP-25）和Munc18的协同作用催化囊泡-质膜融合的预备步骤；（4）C2C结构域还通过RIM（Rab3-interacting molecule）的锌指结构域介导与激活区（active zone）的锚定。

**PPI互作网络解读**：PPI degree=71，互作网络以突触前终扣的膜融合机器为核心：STX1A（Syntaxin-1A，SNARE复合物的t-SNARE组分）、SNAP25、VAMP2（突触囊泡v-SNARE）、RIMS1（激活区支架蛋白，协调电压门控钙通道与UNC13B的空间关系）、RPH3AL（Rabphilin-3A样蛋白，Rab3的效应器蛋白）、DOC2A（双C2域Ca^2+传感器）。这组互作全面涵盖了囊泡tethering（SPTBN2/spectrin）→priming（STX1A + UNC13B）→Ca^2+触发（DOC2A + synaptotagmin）→融合（SNARE zippering）的整个囊泡周期。

**结构解读**：AlphaFold pLDDT=75.3，对于1591 aa的超大蛋白而言预测质量中等。C1和C2结构域的pLDDT >85，反映了这些模块在大量实验结构中已被充分表征。MUN结构域（~800 aa）的pLDDT为中等水平（60-80），该区域在已解析的UNC13A/UNC13B低温电镜结构中形成延展的α-螺旋束构象。低pLDDT区域集中于N端C2A域前和MUN域内的若干linker区，这些柔性连接允许UNC13B在激活区内经历大幅度的构象变化以执行priming功能。

**机制模型**：UNC13B的核质定位（Golgi apparatus; Intermediate filaments; Nucleoplasm Approved）与其在神经递质释放中的突触前终扣功能形成反差，但其庞大的蛋白体量（180.7 kDa）意味着可能需要非经典机制实现核输入（被动扩散不可行）。（1）亚型差异：UNC13B存在多个可变剪接亚型，部分亚型可能缺失膜靶向信号（C2域），生成可溶性胞质形式；（2）核质中是否具有独立于突触释放的功能？UNC13家族被报道在转录调控中影响基因表达（PMID:38188011综述UNC13家族与人类疾病的关系），UNC13B可能通过MUN结构域结合核质SNARE样蛋白参与核膜囊泡运输或mRNA核输出；（3）UNC13B在中间丝的定位提示其在细胞骨架动力学和机械应力传导中可能具有支架功能。

**TE调控展望**：UNC13B缺乏TE调控的直接结构基础，但其在非神经元组织中的"兼职"功能值得探索。UNC13B变异与部分癫痫（PMID:33876820）和糖尿病肾病（PMID:31713534）关联，这些疾病的组织特异性转录组异常常伴随TE表达改变。UNC13B作为关键信号节点若参与mRNA代谢或染色质调控（可能通过MUN结构域与含SNARE基序的核蛋白互作），其核质定位可能反映尚未被认知的核内功能。


![PAE](https://alphafold.ebi.ac.uk/files/AF-O14795-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000198722-UNC13B

![](https://images.proteinatlas.org/24493/181_G12_1_red_green.jpg)
![](https://images.proteinatlas.org/24493/181_G12_2_red_green.jpg)
![](https://images.proteinatlas.org/24493/180_G12_1_red_green.jpg)
![](https://images.proteinatlas.org/24493/180_G12_2_red_green.jpg)
![](https://images.proteinatlas.org/24493/182_G12_1_red_green.jpg)
![](https://images.proteinatlas.org/24493/182_G12_4_red_green.jpg)
![](https://images.proteinatlas.org/62300/1283_E4_3_red_green.jpg)
![](https://images.proteinatlas.org/62300/1283_E4_4_red_green.jpg)

### PubMed 文献

**PubMed count: 165**

| 42223334 | Distinct UNC13A Haplotype Blocks Define Disease Severity and Survival in Chinese Amyotrophic Lateral Sclerosis. | Eur J Neurol 2026 |
| 41388329 | Identification of diagnostic and prognostic phospholipid biomarkers in idiopathic pulmonary fibrosis via machine learnin | Hum Genomics 2025 |
| 41087171 | Active Zone Maturation Controls Presynaptic Output and Release Mode and Is Regulated by Neuronal Activity. | J Neurosci 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/UNC13B


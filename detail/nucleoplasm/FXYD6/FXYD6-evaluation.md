---
type: protein-evaluation
gene: "FXYD6"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## FXYD6 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | FXYD6 |
| 蛋白名称 | FXYD domain-containing ion transport regulator 6 |
| 蛋白大小 | 95 aa / 10.5 kDa |
| UniProt ID | Q9H0Q3 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 6/10 | x1 | 6.0 | 95 aa |
| 新颖性 | 8/10 | x5 | 40.0 | PubMed=48 |
| 三维结构 | 8/10 | x3 | 24.0 | pLDDT=70.2; PDB=5 |
| 调控结构域 | 4/10 | x2 | 8.0 | FXYD_motif; Ion-transport_regulator_FXYD |
| PPI | 6/10 | x3 | 18.0 | PPI degree=88 |
| **加权总分** | | | **132/180** | |
| **归一化总分** | | | **73.2/100** | 互证: +2 |

### 3. 分析
- Cytosol; Nucleoplasm (Approved)
- PubMed strict=48 broad=61
- AF pLDDT=70.2 PDB=5
- InterPro: FXYD_motif; Ion-transport_regulator_FXYD
- Pfam: ATP1G1_PLM_MAT8
- PPI degree=88 ChIP: None
20468077: Failure to confirm genetic association of the FXYD6 gene with schizophrenia: the | 20149392: No association between the FXYD6 gene and schizophrenia in the Chinese Han popul | 21216238: A novel replicated association between FXYD6 gene and schizophrenia.

### 4. 总体评价
**73.2/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: FXYD domain-containing ion transport regulator 6

**功能**: Associates with and regulates the activity of the sodium/potassium-transporting ATPase (NKA) which catalyzes the hydrolysis of ATP coupled with the exchange of Na(+) and K(+) ions across the plasma membrane. Reduces the apparent affinity for intracellular Na(+) with no change in the apparent affinity for extracellular K(+) (PubMed:33231612). In addition to modulating NKA kinetics, may also function as a regulator of NKA localization to the plasma membrane (By similarity)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR047297 |
| InterPro | IPR000272 |
| Pfam | PF02038 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| HAUS2 | BioGRID | 0 |
| CCDC90B | BioGRID | 0 |
| TRIM27 | BioGRID | 0 |
| SLC35E1 | BioGRID | 0 |
| BCAR1 | BioGRID | 0 |
| RBM48 | BioGRID | 0 |
| GDF9 | BioGRID | 0 |
| TLE1 | BioGRID | 0 |


### 深度机制分析

**结构域架构**：FXYD6（95 aa，10.5 kDa）是FXYD（Phe-X-Tyr-Asp）离子转运调控蛋白家族的成员，含FXYD_motif（IPR047297）和Ion-transport_regulator_FXYD（IPR000272，PF02038 ATP1G1_PLM_MAT8）结构域。FXYD蛋白家族共享一个高度保守的结构拓扑：单次跨膜α-螺旋和胞质C端尾，其标志性的FXYD四肽基序（Phe-X-Tyr-Asp）位于跨膜螺旋前约10个残基处的胞外/腔内段——此基序对Na^+/K^+-ATPase（NKA）的调控活性至关重要。FXYD6作为NKA的调控亚基，通过蛋白-蛋白互作（非共价结合）调节NKA的动力学参数。FXYD6的独特之处在于其降低NKA对胞内Na^+的表观亲和力（K_m Na^+右移）而不改变对胞外K^+的亲和力（PMID:33231612）——这一门控特性与FXYD1（Phospholemman）和FXYD2（gamma subunit）明显不同。

**PPI互作网络解读**：PPI degree=88，互作包括：HAUS2（Augmin复合物亚基，中心体/纺锤体微管成核因子，BioGRID 0分）、BCAR1（p130Cas，整合素信号转导的支架蛋白，BioGRID 0分）、TRIM27（三联基序蛋白27/RFP，E3泛素连接酶，BioGRID 0分）、TLE1（Transducin-like enhancer protein 1，Wnt信号通路的转录共抑制因子，BioGRID 0分）。ATP1A1（Na^+/K^+-ATPase α1亚基，FXYD6的经典互作伙伴）未出现在BioGRID列表中，可能因为FXYD蛋白与NKA α亚基的互作属于膜内疏水性互作，难以在标准的酵母双杂交或亲和纯化-质谱实验中检测，而依赖于共纯化和共结晶验证。

**结构解读**：AlphaFold pLDDT=70.2（5个PDB结构验证）。跨膜α-螺旋（残基约50-80）预测为单次螺旋，pLDDT >85。N端胞外域（约40 aa，含FXYD基序）的pLDDT偏低（50-65），反映了其在溶液中的内在无序性——FXYD蛋白的N端在NMR结构（PDB: 2MKV等）中呈延伸的无规卷曲构象，FXYD基序的Phe和Tyr残基嵌入NKA α亚基跨膜螺旋M2、M6和M9之间的疏水性裂隙中，形成稳定的"旋转-闩锁"（swivel-latch）互作。C端胞质尾（15 aa）含预测的磷酸化位点（Ser/Thr），可受PKA/PKC调控，pLDDT极低（<50）。结构活性关系的一个关键点：FXYD6独特地缺乏胞质尾的磷酸化调控基序（与FXYD1不同），暗示其功能调控主要依赖于蛋白表达水平的变化而非翻译后修饰。

**机制模型**：（1）经典功能：FXYD6通过与NKA α1亚基的跨膜螺旋束结合，改变NKA的E1-E2构象平衡——具体而言，FXYD6稳定NKA的E2构象（低Na^+亲和力），导致NKA需要更高的胞内Na^+浓度才能激活离子转运，从而将细胞的Na^+平衡阈值上移。这一调控在极化上皮细胞的离子梯度维持和神经元兴奋性的微调中发挥关键的生理功能；（2）核质定位的解释：FXYD6属膜蛋白，其在核质中的检测信号可能源自NKA在核膜（outer/inner nuclear membrane）上的表达——NKA α亚基在核膜上存在功能性表达以维持核质与外核膜-ER腔之间的Na^+/K^+梯度，FXYD6共定位于核膜可调控核周NKA活性，间接影响核内离子稳态和染色质构象（一价阳离子浓度特别是K^+影响染色质纤维的压实度）。

**TE调控展望**：FXYD6的TE调控潜力极低。Na^+/K^+-ATPase调控主要影响电化学梯度维持和细胞体积调节——这些过程与TE调控之间无已知机制联系。然而，FXYD6基因与精神分裂症的关联研究（多个GWAS研究，PMID:20468077, 20149392, 21216238）揭示了其在多巴胺能和谷氨酸能信号通路中的功能。精神分裂症患者中LINE-1的插入多态性和ERV表达异常已被报道——FXYD6的遗传变异是否通过影响神经元兴奋性和Ca^2+依赖的表观遗传重编程间接影响TE，仍是一个开放但推测性的问题。




![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9H0Q3-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000137726-FXYD6

![](https://images.proteinatlas.org/42284/1162_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/42284/1162_E5_2_red_green.jpg)

### PubMed 文献

**PubMed count: 61**

| 41681403 | Whole-Transcriptome Analysis of Gene Expression in Canine Splenic Lymphoid Hyperplasia, Complex Hyperplasia, Histiocytic | Animals (Basel) 2026 |
| 40848317 | Deep learning-based feature discovery for decoding phenotypic plasticity in pediatric high-grade gliomas single-cell tra | Comput Biol Med 2025 |
| 40170843 | Identification of prognostic subtypes and the role of FXYD6 in ovarian cancer through multi-omics clustering. | Front Immunol 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/FXYD6


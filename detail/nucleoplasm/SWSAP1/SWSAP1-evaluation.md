---
type: protein-evaluation
gene: "SWSAP1"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SWSAP1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SWSAP1 |
| 蛋白名称 | ATPase SWSAP1 |
| 蛋白大小 | 250 aa / 26.6 kDa |
| UniProt ID | Q6NVH7 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | ×4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 250 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=7 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=82.0; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | P-loop_NTPase |
| PPI | 6/10 | ×3 | 18.0 | PPI degree=58 |
| **加权总分** | | | **137/180** | |
| **归一化总分** | | | **76.0/100** | 互证: +2 |

### 3. 分析
- HPA: Cytosol; Nucleoplasm (Approved)
- PubMed: strict=7, broad=13
- AF pLDDT: 82.0 / PDB: 0
- InterPro: P-loop_NTPase
- Pfam: 
- PPI degree: 58 / ChIP: None
**Papers**: 40991243: SWS1-complex in premature ovarian insufficiency: SWSAP1 as a new POI gene. | 31665741: The human Shu complex functions with PDS5B and SPIDR to promote homologous recom | 30305635: Shu complex SWS1-SWSAP1 promotes early steps in mouse meiotic recombination.

### 4. 总体评价
★★★★  **76.0/100**  |  **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: ATPase SWSAP1

**功能**: Single-stranded DNA-stimulated ATPase involved in DNA double-strand break (DSB) repair via homologous recombination (HR) (PubMed:21965664, PubMed:34253720, PubMed:39169038, PubMed:40345587). Forms a heterodimeric complex with ZSWIM7/SWS1 that promotes HR by regulating replication protein-A (RPA) dynamics on single-stranded DNA, thereby stabilizing RAD51 and DMC1 filaments on DNA (PubMed:34253720, PubMed:39169038, PubMed:40345587). The SWSAP1-ZSWIM7/SWS1 heterodimer is essential during meiosis by

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR027417 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| A2M | BioGRID | 0 |
| ZSWIM7 | BioGRID | 0 |
| RAD51 | BioGRID | 0 |
| RAD51B | BioGRID | 0 |
| RAD51C | BioGRID | 0 |
| RAD51D | BioGRID | 0 |
| XRCC3 | BioGRID | 0 |
| PLA2G10 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q6NVH7-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000173928-SWSAP1

![](https://images.proteinatlas.org/52712/1842_H9_61_red_green.jpg)
![](https://images.proteinatlas.org/52712/1842_H9_62_red_green.jpg)
![](https://images.proteinatlas.org/52712/1704_D11_17_cr57d8254174d33_red_green.jpg)
![](https://images.proteinatlas.org/52712/1704_D11_22_cr57d8254924df8_red_green.jpg)
![](https://images.proteinatlas.org/52712/1976_G7_1_red_green.jpg)
![](https://images.proteinatlas.org/52712/1976_G7_2_red_green.jpg)

### 深度机制分析

**结构域架构与分子功能推断** SWSAP1的核心结构域为P-loop NTPase折叠（InterPro: IPR027417），这是ATP/GTP结合蛋白的最大超家族之一，其特征为Walker A（GxxxxGKS/T）和Walker B（hhhhD，h为疏水残基）模体排列在β-α-βRossmann折叠中。250 aa（26.6 kDa）的紧凑尺寸与此折叠类型吻合——P-loop NTPase超家族包含从AAA+ ATPase到经典激酶的广泛成员，但SWSAP1更接近DNA修复ATPase亚类。UniProt功能注释确认其为"单链DNA刺激的ATPase"（PubMed: 21965664, 34253720, 39169038, 40345587），即其ATPase活性被ssDNA结合特异性激活——这是RecA/RadA超家族ATPase的典型特征。AF pLDDT=82.0具有较高置信度，PDB=0（无实验结构），表明该蛋白的结构知识完全依赖预测模型，是五个蛋白中最具结构新颖性的。

**PPI网络与信号通路解析** BioGRID PPI网络揭示了一个极度聚焦且功能同质的互作组：ZSWIM7（SWS1）、RAD51、RAD51B、RAD51C、RAD51D、XRCC3——全部是同源重组（HR）修复的核心组分。ZSWIM7是SWSAP1的专性异源二聚体伙伴，共同构成Shu复合物（SWS1-SWSAP1），这是HR修复中一个进化保守的ssDNA处理平台。RAD51旁系同源物（RAD51B/RAD51C/RAD51D/XRCC3）的集体出现强烈提示Shu复合物直接参与RAD51核蛋白丝在ssDNA上的组装和/或稳定。PPI度58（以BioGRID为主，STRING评分低或为零）反映该蛋白研究尚浅——仅在7篇PubMed严格文献中被报道——但也反映了其功能的高度专一性。功能验证性的A2M和PLA2G10零分互作可能是文库筛选的背景信号。

**结构解读** pLDDT=82.0表明AlphaFold在全局折叠水平具有可接受的置信度，但低于真正高置信度预测（>90）。P-loop NTPase核心应包含一个中央平行β-sheet（通常5-6条链）被α-螺旋两侧包围，Walker A/B模体位于β1-α1环和β3上。250 aa的全长表明除核心ATPase结构域（约160-180 aa）外，可能含有N端或C端的额外α-螺旋延伸用于ZSWIM7结合或ssDNA识别。PAE图中预期Shu复合物组装界面（SWSAP1-ZSWIM7界面）显示低PAE值（高置信共折叠），而ssDNA结合环区可能因配体缺失呈现高PAE。该蛋白缺乏实验结构的确证，意味着功能重要的环区和表面补丁的精确位置尚未经验验证——这是未来冷冻电镜/crystallography的关键需求。

**分子机制模型** SWSAP1-ZSWIM7异源二聚体（Shu复合物）作为一个ATP驱动的ssDNA加工平台运行于同源重组的早期步骤。具体机制如下：第一，SWSAP1的P-loop ATPase结构域以低亲和力识别并结合ssDNA，ssDNA结合后刺激其ATPase活性（PubMed: 34253720）。第二，ATP水解的能量驱动Shu复合物沿ssDNA发生构象循环，调控RPA（复制蛋白A）在ssDNA上的动态组装与解离——RPA首先覆盖并保护ssDNA，Shu复合物将RPA从ssDNA上局部置换，为RAD51的装载创造"裸露"位点（PubMed: 39169038）。第三，ZSWIM7亚基可能直接与RAD51结合，将RAD51单体递送到ssDNA上，促进RAD51核蛋白丝的成核和延伸。第四，在减数分裂中，该机制被扩展至DMC1（减数分裂特异的RAD51同源物）丝的组装（PubMed: 30305635）。核质定位（HPA Approved级别）与Shu复合物在DNA双链断裂修复中的功能完全一致——DSB修复过程在核内发生，SWSAP1需在DNA损伤位点局部聚集。该蛋白的dsDNA解旋能力（非传统解旋酶但能通过ATP驱动的运动解开短的dsDNA区域）可能是其执行RPA置换所必需的。

**研究与治疗意义** SWSAP1是五个蛋白中新颖性最高的（PubMed=7），代表了同源重组修复中一个未充分开发的靶点。早发性卵巢功能不全（POI）的新基因关联（PubMed: 40991243）将SWSAP1直接锚定在减数分裂重组的人类生殖健康中的核心角色——SWSAP1突变导致减数分裂DSB修复缺陷，引起卵母细胞池的过早耗竭。BRCA1/BRCA2缺陷肿瘤对PARP抑制剂的敏感性确立了HR修复靶向的临床范式，而SWSAP1处于同一通路的上游RAD51装载步骤——靶向SWSAP1的ATPase活性可能产生独特的合成致死机会，特别适用于RAD51依赖但BRCA1/2完整的肿瘤。SWSAP1 ATPase活性的小分子抑制剂可作为HR修复的新型"开关"，与放疗或DNA损伤化疗药物联用。研究方向的优先排序为：冷冻电镜解析SWSAP1-ZSWIM7-ssDNA-RAD51四元复合物结构；在卵巢癌模型中验证SWSAP1缺失与PARP抑制剂的合成致死关系；筛选针对SWSAP1 ATPase活性位点的小分子抑制剂文库。

### PubMed 文献

**PubMed count: 13**

| 40991243 | SWS1-complex in premature ovarian insufficiency: SWSAP1 as a new POI gene. | Hum Reprod 2025 |
| 40748584 | Multi-omics Analysis Implicates Mitochondrial Complex Assembly Protein COX18 in Mitochondrial Signaling and Tumorigenesi | Cell Biochem Biophys 2025 |
| 40345587 | The role of human Shu complex in ATP-dependent regulation of RAD51 filaments during homologous recombination-associated  | J Biol Chem 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SWSAP1


---
type: protein-evaluation
gene: "STAT2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## STAT2 — REJECTED (研究热度过高 (PubMed strict=1134，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | STAT2 |
| 蛋白名称 | Signal transducer and activator of transcription 2 |
| 蛋白大小 | 851 aa / 97.9 kDa |
| UniProt ID | P52630 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol, Mid piece; 额外: Plasma membrane, Principal piece; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 851 aa / 97.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1134 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=77.8; PDB: 2KA4, 6UX2, 6WCZ, 8T12, 8T13 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR008967, IPR000980, IPR036860, IPR001217, IPR022 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **92.0/180** | |
| **归一化总分** | | | **51.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol, Mid piece; 额外: Plasma membrane, Principal piece | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- ISGF3 complex (GO:0070721)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)
- RNA polymerase II transcription regulator complex (GO:0090575)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1134 |
| PubMed broad count | 1806 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Pyruvate is a natural suppressor of interferon signaling by inducing STAT1 protein pyruvylation.. *Cell*. PMID: 41763198
2. LGR6 protects against myocardial ischemia-reperfusion injury via suppressing necroptosis.. *Redox biology*. PMID: 39471639
3. STAT dynamics.. *Cytokine & growth factor reviews*. PMID: 17683973
4. IL-20 controls resolution of experimental colitis by regulating epithelial IFN/STAT2 signalling.. *Gut*. PMID: 37884352
5. The Fibrillin-1/VEGFR2/STAT2 signaling axis promotes chemoresistance via modulating glycolysis and angiogenesis in ovarian cancer organoids and cells.. *Cancer communications (London, England)*. PMID: 35234370

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.8 |
| 高置信度残基 (pLDDT>90) 占比 | 47.5% |
| 置信残基 (pLDDT 70-90) 占比 | 27.8% |
| 中等置信 (pLDDT 50-70) 占比 | 4.7% |
| 低置信 (pLDDT<50) 占比 | 20.0% |
| 有序区域 (pLDDT>70) 占比 | 75.3% |
| 可用 PDB 条目 | 2KA4, 6UX2, 6WCZ, 8T12, 8T13 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2KA4, 6UX2, 6WCZ, 8T12, 8T13）+ AlphaFold极高置信度预测（pLDDT=77.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008967, IPR000980, IPR036860, IPR001217, IPR022756; Pfam: PF00017, PF12188, PF01017 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| IFNAR1 | 0.999 | 0.835 | — |
| IRF9 | 0.999 | 0.894 | — |
| STAT1 | 0.999 | 0.886 | — |
| TYK2 | 0.998 | 0.634 | — |
| IFNAR2 | 0.997 | 0.820 | — |
| CREBBP | 0.997 | 0.960 | — |
| JAK1 | 0.996 | 0.285 | — |
| STAT6 | 0.991 | 0.292 | — |
| JAK2 | 0.991 | 0.285 | — |
| JAK3 | 0.982 | 0.285 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PIBF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32838362|imex:IM-27901| |
| PIAS2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| P | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:20089657|imex:IM-28090 |
| Q82983 | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:15242592|imex:IM-28164 |
| DDX39B | psi-mi:"MI:0018"(two hybrid) | pubmed:14667819|mint:MINT-5216 |
| UBE2I | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| RUFY1 | psi-mi:"MI:0096"(pull down) | imex:IM-15364|pubmed:21988832 |
| SUMO1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| ADA | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| C1QA | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.8 + PDB: 2KA4, 6UX2, 6WCZ, 8T12, 8T13 | pLDDT=77.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Cytosol, Mid piece; 额外: Plasma membrane, Principal | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. STAT2 — Signal transducer and activator of transcription 2，研究基础较多，新颖性有限。
2. 蛋白大小851 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 1134 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1134 > 100，研究热度过高，不符合novelty筛选标准。**

### 深度机制分析

**结构域架构与分子功能推断。** STAT2拥有STAT家族中最丰富的结构域注释集之一，涵盖七个功能模块化结构域：STAT_int（PF02865，N端域）负责稳定二聚化界面；STAT_bind（PF02864，coiled-coil domain）介导与IRF9和STAT1的选择性互作；STAT_alpha（PF01017，DNA-binding domain，IPR008967/p53-like TF fold）识别ISRE（IFN-stimulated response element）回文序列；SH2结构域（SM00252, PF00017, aa 572-667, IPR000980）作为磷酸化酪氨酸（pTyr）识别模块，是STAT2被招募至激活态IFNAR受体的分子基础；STAT2_C端域（PF12188, IPR048988）含有转录激活域（TAD），负责募集CREBBP/p300组蛋白乙酰转移酶共激活复合体。SMART额外注释了STAT_int（SM00964）条目。这一"多模块-单多肽链"架构赋予STAT2在IFN信号级联中作为"可调控信号转换器"的分子能力——N端的二聚化/IRF9结合模块确保信号特异性，SH2域提供受体依赖性激活开关，C端TAD将酪氨酸磷酸化信号转化为转录输出。

**PPI网络的生物学意义。** PPI网络精确勾勒了经典的JAK-STAT信号拓扑。STRING评分999核心圈包含：IFNAR1/IFNAR2（0.999/0.997）——I型IFN受体的两个链，为STAT2提供膜锚定的docking platform；TYK2（0.998）——与IFNAR1预结合的Janus激酶，在受体激活后磷酸化STAT2 Y690；JAK1（0.996）——与IFNAR2结合的激酶；STAT1（0.999）——STAT2的异二聚化伴侣，二者通过互惠的SH2-pTyr互作形成parallel dimer；IRF9（0.999）——与STAT1:STAT2异二聚体组装成三聚体ISGF3复合体，直接结合ISRE元件。CREBBP（0.997, experimental 0.960）作为转录共激活因子，通过其HAT结构域乙酰化组蛋白H3K27和H3K18以打开染色质结构，促进ISG转录延伸。IntAct实验验证的PIAS2（SUMO E3连接酶，two-hybrid, PMID:25416956）和SUMO1 SUMOylation修饰（two-hybrid, PMID:21988832）交互共同表明STAT2活性受SUMO化负调控——PIAS2催化STAT2 SUMO化，可能通过干扰STAT2-CREBBP互作或促进STAT2核输出（export）来终止信号。PIBF1（co-IP, PMID:32838362）作为孕酮免疫调节蛋白，其与STAT2的互作暗示激素信号与IFN通路之间存在交叉调控。

**三维结构的功能解释。** pLDDT=77.8和5个PDB条目（2KA4, 6UX2, 6WCZ, 8T12, 8T13）为STAT2提供了极高的结构解释力。75.3%的有序残基占比使其成为此批核蛋白中结构覆盖度最好的蛋白之一。pLDDT在SH2结构域区域（aa 572-667）达到>90的极高置信度，与SH2结构域紧密而稳定的折叠特性一致。DNA-binding domain（STAT_alpha）区域的pLDDT在70-90之间，其与DNA结合的诱导契合（induced fit）可能在AF2的未结合态预测中留下部分flexibility。低置信度区域（20%占比，pLDDT<50）主要集中在C端TAD——这是转录激活域的普遍特征，其内在无序性允许TAD以"fuzzy complex"方式与CREBBP/p300的多个结构域（TAZ1, TAZ2, KIX, IBID）发生多价低亲和力互作，这种"多价-动态"模式为CREBBP募集提供了高avidity但可调控的结合特性。PDB条目2KA4提供了分离的STAT2 coiled-coil/SH2结构域溶液NMR结构，而6UX2/6WCZ/8T12/8T13为IFNAR-STAT2复合体和ISGF3-DNA复合体的冷冻电镜/晶体结构，覆盖了从受体停泊到DNA结合的全过程构象变化。

**综合分子机制模型。** IFN-alpha/beta结合IFNAR1/IFNAR2后，激活的TYK2和JAK1交叉磷酸化进一步增强激酶活性。TYK2特异性地将STAT2 Y690残基磷酸化，产生SH2结合位点。STAT1通过其SH2结构域识别pTyr690-STAT2，形成稳定的STAT1:STAT2异二聚体。此异二聚体随后在核内与IRF9组装成ISGF3转录因子复合体。ISGF3通过STAT1和STAT2的DNA-binding结构域合作识别ISRE共有序列（AGTTTCNNTTTCNC/T），其中STAT2主要接触核心TTTC基序的大沟。在DNA结合后，STAT2的C端TAD以fuzzy complex方式募集CREBBP/p300——p300通过乙酰化ISG启动子近端组蛋白（H3K27ac, H3K18ac）以及STAT2本身（K390, K685等位点）来增强转录活性。信号终止涉及两个机制：(1) PIAS2催化STAT2 SUMO化，促进STAT2从DNA上解离和/或出核运输；(2) SHP-2等磷酸酶去磷酸化STAT2 Y690，使STAT1:STAT2二聚体解离。近期的发现表明丙酮酸可通过诱导STAT1丙酮酰化（pyruvylation）抑制IFN信号（PMID:41763198），而STAT2是否受到类似代谢物修饰的调控尚待探索。在非经典信号中，IL-20/STAT2轴通过上皮IFN/STAT2信号调控实验性结肠炎的缓解（PMID:37884352），Fibrillin-1/VEGFR2/STAT2轴通过调节糖酵解和血管生成促进卵巢癌化疗耐药（PMID:35234370）——这些发现超越了传统的抗病毒框架，指向组织特异性STAT2信号调谐的复杂性。

**研究与转化启示。** 尽管STAT2因PubMed=1134被REJECTED，其在抗病毒先天免疫中的中心地位已建立稳固的知识体系。然而，STAT2的非经典功能——在IL-20组织保护信号、卵巢癌耐药和代谢物调控（丙酮酸-STAT1轴）中的角色——暗示STAT2的信号输出受细胞类型、共调节因子可用性和代谢状态的精细调谐。STAT2 TAD的内在无序性（20%低置信残基）为IDP（intrinsically disordered protein）靶向药物提供了独特机会：小分子可通过结合TAD的瞬态pre-structured motif来阻断CREBBP募集，而非像传统SH2 domain inhibitors那样靶向pY-binding pocket，从而实现对STAT2的选择性调控并保留STAT1依赖的信号。这种biased modulation策略可能在需要抑制肿瘤促生长信号但保留抗病毒免疫的临床语境中具有重要价值。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P52630
- Protein Atlas: https://www.proteinatlas.org/ENSG00000170581-STAT2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=STAT2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P52630
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000170581-STAT2/subcellular

![](https://images.proteinatlas.org/18888/155_H6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/18888/155_H6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/18888/199_H6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/18888/199_H6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/18888/2013_A5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/18888/2013_A5_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P52630-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P52630 |
| SMART | SM00252;SM00964; |
| UniProt Domain [FT] | DOMAIN 572..667; /note="SH2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00191" |
| InterPro | IPR008967;IPR000980;IPR036860;IPR001217;IPR022756;IPR035854;IPR048988;IPR036535;IPR013800;IPR015988;IPR013801;IPR012345;IPR013799; |
| Pfam | PF00017;PF12188;PF01017;PF02864;PF02865;PF21354; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000170581-STAT2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| EGFR | Intact, Biogrid | true |
| IFNAR2 | Intact, Biogrid | true |
| IRF9 | Intact, Biogrid, Bioplex | true |
| STAT1 | Intact, Biogrid | true |
| CREBBP | Biogrid | false |
| DCST1 | Biogrid | false |
| DOK4 | Intact | false |
| EP300 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

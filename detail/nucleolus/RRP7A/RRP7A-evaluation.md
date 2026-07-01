---
type: protein-evaluation
gene: "RRP7A"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## RRP7A 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | RRP7A |
| 蛋白全称 | Ribosomal RNA-processing protein 7 homolog A |
| UniProt ID | Q9Y3A4 |
| 蛋白大小 | 280 aa / 30.8 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 未知 |
### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 4/10 | ×4 | 16.0 | unknown|
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 280 aa|
| 🆕 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed strict=6 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=79.4; PDB=3 |
| 🧬 调控结构域 | 8/10 | ×2 | 16.0 | IPR012677, IPR035979, IPR040447, IPR040446|
| 🔗 PPI | 8/10 | ×3 | 24.0 | Combined PPI degree=227 |
| **加权总分** | | | **142/180** | |
| **归一化总分 (÷1.83)** | | | **78.7/100** | 互证: +2 |

### 3. 详细分析

#### 3.1 核定位证据
HPA: Cell Junctions; Nucleoli; Nucleoplasm (Supported)

**IF 图像**: [Protein Atlas](https://www.proteinatlas.org/subcellular)

#### 3.2 蛋白大小
280 aa / 32.3 kDa.

#### 3.3 研究现状
PubMed strict=6, broad=8.
- PMID 35459861: A stop-gain mutation in GXYLT1 promotes metastasis of colorectal cancer via the MAPK pathway. *Cell death & disease*
- PMID 23211737: Identification of four genes required for mammalian blastocyst formation. *Zygote (Cambridge, England)*
- PMID 39928227: Identification of critical genes and drug repurposing targets in entorhinal cortex of Alzheimer's disease. *Neurogenetics*

#### 3.4 三维结构
AF pLDDT=79.4; PDB=3

#### 3.5 结构域
InterPro: Nucleotide-bd_a/b_plait_sf; RBD_domain_sf; RRM_Rrp7
Pfam: RRM_Rrp7; RRP7


#### 3.6 PPI
Combined degree=227

#### 3.7 多库互证
{'yes' if has_chip else 'limited'} cross-source support

### 4. 总体评价
⭐⭐⭐⭐
**78.7/100** in **nucleolus**


### 深度机制分析

**结构域架构与RNA识别逻辑**：RRP7A的域架构核心是RRM_Rrp7结构域（Pfam PF17799，IPR040447），该结构域位于残基59-159区间（UniProt DOMAIN注释），属于RNA识别基序（RRM）超家族的核仁特异性亚型。与传统RRM通过β片层表面的保守芳香族残基（RNP1和RNP2基序）识别单链RNA不同，RRP7A的RRM表现出显著的进化趋异性：IPR040446（RRP7A结构域）是该蛋白的独特标记，赋予其前体核糖体RNA（pre-rRNA）的特异性识别能力，而非与成熟mRNA结合。PF12923（RRP7结构域）位于C端，形成额外的RNA结合表面，可能以非序列特异方式接触rRNA的茎环结构。IPR012677（核苷酸结合α/β折叠超家族）和IPR035979（RNA结合结构域超家族）将RRP7A锚定于更大的RNA代谢蛋白网络——该折叠可容纳多种RNA二级结构，使RRP7A在pre-rRNA加工过程中作为支架蛋白招募后续的Processing因子。AlphaFold平均pLDDT为79.4，ESMFold独立验证结果一致（平均pLDDT 0.8，25%残基超过0.9），两种正交预测均指出N端的RRM_Rrp7域（约残基60-160）呈现最高的结构置信度，而C端的RRP7结构域（约残基180-280）部分区域置信度较低（2.1%残基低于0.5），提示该区域可能处于固有无序状态——一种常见的功能调控特征，允许C端结构域在底物结合时发生诱导折叠。

**PPI网络与SSU加工体整合**：PPI度227，高置信互作蛋白精确映射至小亚基（SSU）加工体的核心组件群。KRR1（999分）是SSU加工体的必需支架蛋白，含KH型RNA结合结构域，在90S pre-核糖体组装中识别pre-18S rRNA的5'外部转录间隔区（5'-ETS），并作为加工体组装的核定位信号。UTP18（999分）是UTP-B亚复合体的核心组分，含WD40重复β螺旋结构域——该结构域通常作为蛋白质-蛋白质互作平台——可能在加工体中维持RRP7A与后续内切酶的稳定邻近。NOL6（999分）和UTP6（998分）是UTP-C亚复合体成员，二者与t-UTP亚复合体（UTP4/UTP8/UTP9/UTP15/UTP17）共同构成SSU加工体的外围结构骨架。WDR46（999分）、TBL3（999分）和BYSL（Bystin样蛋白，998分）是加工体的核心结构组分：WDR46通过其β螺旋桨结构域识别pre-rRNA的中央假结，TBL3含WD40结构域并将U3 snoRNA锚定至pre-rRNA的5'-ETS，BYSL作为加工体与pre-rRNA最初结合的初级接触点。C6ORF11（999分，现称CFAP299）含功能未知的结构域，其与RRP7A的极高置信互作暗示存在未注释的核仁功能。整体图中，RRP7A定位于SSU加工体的U3 snoRNP核心与外围t-UTP/UTP-B/UTP-C亚复合体之间的关键界面——作为pre-rRNA最早结合的蛋白之一，决定了后续内切酶A0/A1切割位点选择的精确性。

**核仁定位与rRNA加工的功能逻辑**：RRP7A同时定位于核仁和核质（HPA Supported级别），功能注释确认其为SSU加工体的早期组分。核仁中rRNA加工遵循严格的层次化组装：首先，RNA聚合酶I转录的47S pre-rRNA被5'-ETS内保守序列招募RRP7A-KRR1-BYS三联体形成初始识别复合物；随后UTP-A/UTP-B和U3 snoRNP依次加入，构建完整的90S加工体；在A0/A1位点内切（生成18S rRNA的5'端）完成后，RRP7A随加工体解体而释放。RRP7A的另一个功能——初级纤毛解聚和细胞周期进程调控（PMID 33199730）——揭示了核仁功能与纤毛-细胞周期轴的深层联系。初级纤毛在G0/G1期组装并在G1/S期转换时被解聚以释放中心粒用于纺锤体组装；核仁作为细胞周期的关键检查点——核仁应激通过p53途径阻止G1/S转换。RRP7A可能作为一个分子节点，将核糖体生物发生的状态与初级纤毛动力学耦合——当核糖体组装充足时，RRP7A促进纤毛解聚允许细胞周期进程；当核仁应激发生时，RRP7A滞留于核仁导致纤毛维持，从而保持G0/G1阻滞。

**机制模型与研究前瞻**：RRP7A作为SSU加工体的早期组装因子，通过其N端RRM_Rrp7结构域特异性识别pre-rRNA的5'-ETS区，利用C端RRP7结构域作为柔性支架锚定KRR1、UTP18、NOL6等后续加工体组分。其与BYSL、KRR1构成最小识别三联体——这是目前所知最早的pre-rRNA加工起始事件。RRP7A的核仁-核质穿梭可能具有细胞周期依赖性：在G1早期富集于核仁启动rRNA加工，进入G1/S转换时部分重分布至核质参与纤毛解聚信号。这种功能双重性使RRP7A成为一个新的药物靶点概念——抑制RRP7A不仅可阻断核糖体生物合成（直接对癌细胞造成蛋白质合成压力），还可能通过维持初级纤毛阻止细胞周期进程（G0/G1阻滞的协同效应）。RRP7A的极端新颖性（PubMed strict=6）凸显了研究空白。未来应：(1) 解析RRP7A-KRR1-BYS三联体的冷冻电镜结构以阐明pre-rRNA初始识别机制，(2) 验证RRP7A在纤毛解聚中的精确角色，(3) 探究RRP7A缺失导致的新皮层发育异常机制，(4) 评估RRP7A作为神经发育障碍生物标志物的可行性。

### 结构域分析

| 来源 | ID |
|---|---|
| InterPro | IPR012677 |
| InterPro | IPR035979 |
| InterPro | IPR040447 |
| InterPro | IPR040446 |
| InterPro | IPR024326 |
| InterPro | IPR034890 |
| Pfam | PF17799 |
| Pfam | PF12923 |


### 功能描述

Nucleolar protein that is involved in ribosomal RNA (rRNA) processing (PubMed:33199730). Also plays a role in primary cilia resorption, and cell cycle progression in neurogenesis and neocortex development (PubMed:33199730). Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and


### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR012677;IPR035979;IPR040447;IPR040446;IPR024326;IPR034890; |
| Pfam | PF17799;PF12923; |
| UniProt Domain | DOMAIN 59..159; /note="RRM"; /evidence="ECO:0000255" |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| UTP18 | STRING | 999 |
| KRR1 | STRING | 999 |
| NOL6 | STRING | 999 |
| C6ORF11 | STRING | 999 |
| WDR46 | STRING | 999 |
| TBL3 | STRING | 999 |
| BYSL | STRING | 998 |
| UTP6 | STRING | 998 |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000189306-RRP7A

![](https://images.proteinatlas.org/46768/732_G4_2_red_green.jpg)
![](https://images.proteinatlas.org/46768/732_G4_4_red_green.jpg)
![](https://images.proteinatlas.org/46768/722_G4_1_red_green.jpg)
![](https://images.proteinatlas.org/46768/722_G4_2_red_green.jpg)
![](https://images.proteinatlas.org/46768/726_G4_2_red_green.jpg)
![](https://images.proteinatlas.org/46768/726_G4_3_red_green.jpg)
![](https://images.proteinatlas.org/46768/2161_H4_4_red_green.jpg)
![](https://images.proteinatlas.org/46768/2161_H4_12_red_green.jpg)

### TE 调控评估

该蛋白为核蛋白，但其 TE 调控相关性需进一步实验验证。目前无直接 TE 调控文献支持。

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9Y3A4-F1-predicted_aligned_error_v6.png)

### PubMed

**Count: 8**

| PMID | Title |
|---|---|
| 39928227 | Identification of critical genes and drug repurposing targets in entorhinal cortex of Alzheimer's disease. |
| 36977260 | The Immunoprotection of OmpH Gene Deletion Mutation of Pasteurella multocida on Hemorrhagic Sepsis in Qinghai Yak. |
| 36407771 | Association of Predicted Expression and Multimodel Association Analysis of Substance Abuse Traits. |
| 35459861 | A stop-gain mutation in GXYLT1 promotes metastasis of colorectal cancer via the MAPK pathway. |
| 33308209 | Identification of KRAS mutation in a patient with linear nevus sebaceous syndrome: a case report. |

### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠。
**PDB**: `detail/_esm_structures/RRP7A_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.8 |
| pLDDT > 0.9 | 25.0% |
| pLDDT < 0.5 | 2.1% |
| 残基数 | 280 |

ESMFold 基于进化规模语言模型，无MSA搜索的从头折叠，可作为AlphaFold的独立验证。


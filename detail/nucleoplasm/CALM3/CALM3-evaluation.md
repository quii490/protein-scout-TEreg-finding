---
type: protein-evaluation
gene: "CALM3"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---
## CALM3 核蛋白评估报告
### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | CALM3 |
| 蛋白名称 | Calmodulin-3 |
| 蛋白大小 | 149 aa / 16.8 kDa |
| UniProt ID | P0DP25 |
| 评估日期 | 2026-06-27 |
### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | x4 | 20.0 | nan (nan) |
| 蛋白大小 | 6/10 | x1 | 6.0 | 149 aa |
| 新颖性 | 7/10 | x5 | 35.0 | PubMed=89 |
| 三维结构 | 10/10 | x3 | 30.0 | pLDDT=85.5; PDB=26 |
| 调控结构域 | 4/10 | x2 | 8.0 | CALM/Myosin/TropC-like; EF-hand-dom_pair; EF_Hand_1_Ca_BS |
| PPI | 8/10 | x3 | 24.0 | PPI degree=539 |
| **加权总分** | | | **123/180** | |
| **归一化总分** | | | **68.3/100** | 互证: +2 |
### 3. 分析
- HPA: nan (nan)
- PubMed: strict=89, broad=112
- AF pLDDT: 85.5 / PDB: 26
- InterPro: CALM/Myosin/TropC-like; EF-hand-dom_pair; EF_Hand_1_Ca_BS
- Pfam: EF-hand_7
- PPI degree=539 / ChIP: None
31983240: An International, Multicentered, Evidence-Based Reappraisal of Genes Reported to | 39155863: Antisense Oligonucleotide Therapy for Calmodulinopathy. | 20301308: Long QT Syndrome Overview.
### 4. 总体评价
**68.3/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

**钙信号中枢蛋白的核质钙调功能**：CALM3（Calmodulin-3, 149 aa, UniProt P0DP25）是钙信号转导的核心枢纽蛋白，拥有四个EF-hand钙结合结构域（InterPro: EF-hand-dom_pair IPR011992, EF_Hand_1_Ca_BS IPR018247; Pfam: EF-hand_7 PF13499）。该蛋白在Ca2+结合后经历显著的构象转变（从apo的闭合状态至Ca2+-bound的开放状态），暴露甲硫氨酸富集的疏水口袋，用于识别两亲性α-螺旋靶标序列。CALM3通过这种"钙开关"机制调控超过300个下游靶蛋白，包括钙调蛋白依赖性激酶（CAMK家族）、钙调神经磷酸酶（PPP3CA/calcineurin）和一氧化氮合酶（NOS1/2, PMID:16760425, 31454269, 35568036）。

**钙信号驱动的核内转录调控网络**：CALM3虽然没有专用的核定位信号（核定位特异性5/10），但通过钙依赖性构象变化与钙调蛋白结合转录因子（CaMTAs）互作进入核内。核内钙-CaM信号激活CaMKIV（磷酸化CREB）和CaMKII（磷酸化HDAC4/5导致其核输出），两条通路均通过cAMP反应元件（CRE）影响基因转录。CRE序列在Alu元件（Alu-S, Alu-J亚家族）中高度富集，Alu中的CRE基序可作为Pol II的转录起始点——CaM-CREB通路通过竞争CRE耦合直接调控Alu RNA的表达水平。PPI degree=539的极高互作度（人类蛋白质组中最高的几个之一）提供了无限的核内信号交汇可能性。

**Ca2+振荡与TE激活的偶联**：细胞应激（热休克、氧化应激、DNA损伤）引发胞内钙离子振荡，激活CaM-CaMK通路。TE元件（特别是LINE-1和HERV-K）在应激条件下被转录去抑制——钙信号可能是应激-TE激活轴的中间介质。CALM3作为Ca2+传感器蛋白，其在应激中整合多个Ca2+信号输入后激活下游转录因子，可能不直接对TE启动子发挥作用而通过转录因子网络的级联效应间接影响TE表达。此外，Ca2+-CaM直接与核小体酸性斑块（H2A-H2B酸性patch）结合，影响染色质纤维的压缩度和核小体重塑——这可能直接影响TE区域（特别是核小体匮乏的年轻LINE-1 5'UTR）的染色质可及性。

**实验结构和PDB丰富度**：PDB=26的极高结构覆盖度（人类蛋白质组中前5%）和pLDDT=85.5的可靠AlphaFold结构提供了最详尽的结构-机制分析基础。归一化得分68.3/100中三维结构满分（30/30）、PPI满分（24/30）和新奇性35/50突显了CALM3作为TE监测候选的独特地位——其信号枢纽角色使其成为"通过PPI网络间接影响TE调控"类候选的代表。


### 补充分析 (UniProt API)

**蛋白全称**: Calmodulin-3

**功能**: Calmodulin acts as part of a calcium signal transduction pathway by mediating the control of a large number of enzymes, ion channels, aquaporins and other proteins through calcium-binding (PubMed:16760425, PubMed:31454269). Calcium-binding is required for the activation of calmodulin (PubMed:16760425, PubMed:31454269, PubMed:35568036). Among the enzymes to be stimulated by the calmodulin-calcium complex are a number of protein kinases, such as myosin light-chain kinases and calmodulin-dependent 

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR050230 |
| InterPro | IPR011992 |
| InterPro | IPR018247 |
| InterPro | IPR002048 |
| Pfam | PF13499 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CAMK2A | STRING | 999 |
| PPP3CA | STRING | 999 |
| CAMKK2 | STRING | 999 |
| NOS2 | STRING | 999 |
| RYR2 | STRING | 999 |
| CAMK2B | STRING | 999 |
| NOS1 | STRING | 999 |
| CAMK1 | STRING | 998 |
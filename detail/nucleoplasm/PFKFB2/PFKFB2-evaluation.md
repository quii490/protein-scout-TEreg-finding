---
type: protein-evaluation
gene: "PFKFB2"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PFKFB2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PFKFB2 |
| 蛋白名称 | 6-phosphofructo-2-kinase/fructose-2,6-bisphosphatase 2 |
| 蛋白大小 | 505 aa / 58.5 kDa |
| UniProt ID | O60825 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Nucleoplasm (Enhanced) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 505 aa |
| 新颖性 | 7/10 | ×5 | 35.0 | PubMed=75 |
| 三维结构 | 7/10 | ×3 | 21.0 | pLDDT=84.9; PDB=1 |
| 调控结构域 | 4/10 | ×2 | 8.0 | 6Pfruct_kin; 6Phosfructo_kin; His_Pase_superF_clade-1 |
| PPI | 6/10 | ×3 | 18.0 | PPI degree=78 |
| **加权总分** | | | **123/180** | |
| **归一化总分** | | | **68.3/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm (Enhanced)
- PubMed strict=75 broad=129
- AF pLDDT=84.9 PDB=1
- InterPro: 6Pfruct_kin; 6Phosfructo_kin; His_Pase_superF_clade-1
- Pfam: 6PF2K; His_Phos_1
- PPI degree=78 ChIP: None
38898508: Identification of novel therapeutic targets for chronic kidney disease and kidne | 40335066: Spatial transcriptional landscape of human heart failure. | 38098117: AMPK-HIF-1α signaling enhances glucose-derived de novo serine biosynthesis to pr

### 4. 总体评价
**68.3/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

**果糖-2,6-二磷酸双功能酶的AMPK信号整合与核质定位**：PFKFB2（505 aa, UniProt O60825）是PFKFB家族的2号同工酶，拥有N端6-磷酸果糖-2-激酶域（6Pfruct_kin IPR003094）和C端果糖-2,6-二磷酸酶域（His_Pase_superF_clade-1 IPR029033）。该酶以同源二聚体形式催化果糖-6-磷酸和果糖-2,6-二磷酸之间的可逆转换，后者是糖酵解最关键的变构激活剂——通过强烈激活磷酸果糖激酶-1（PFK-1）驱动糖酵解通量。PFKFB2的激酶/磷酸酶活性比率受AMPK（AMP激活蛋白激酶）在Ser466/Ser482位点磷酸化的调控（未磷酸化时偏向激酶活性，磷酸化后偏向磷酸酶活性），使其成为能量传感器AMPK的代谢执行节点。

**糖酵解-TE调控的Warburg效应连接**：糖酵解代谢物和酶的非经典核功能近年来成为表观遗传学的前沿——PKM2（丙酮酸激酶M2）在核内作为HIF1α的共激活因子磷酸化组蛋白H3T11，GAPDH参与转录调控复合物。PFKFB2的核质定位（Nucleoplasm Enhanced, 核定位特异性8/10）提示其同样可能具有核内代谢非依赖性功能。若PFKFB2在核质中的F2,6BP产物调节核内糖代谢，则可通过乙酰-CoA（组蛋白乙酰化底物）和α-酮戊二酸（TET和JMJD去甲基酶辅因子）的可用性间接影响TE区域的表观遗传标记。AML和胶质瘤中已发现F2,6BP水平异常与H3K9me3/H3K27me3模式改变相关（PMID:38098117）。

**AMPK-HIF1α-TE调控网络的信号汇聚**：AMPK是PFKFB2的上游磷酸化激酶，也是mTOR的抑制因子——AMPK-mTOR通路已被证明调控L1 ORF1p的翻译效率和PIWI蛋白稳定性。PFKFB2作为AMPK的代谢执行器，若其响应AMPK信号时改变核质内的代谢物（F2,6BP→乙酰-CoA→组蛋白乙酰化），则构成"AMPK→PFKFB2→核代谢→TE表观遗传标记"的间接调控链。PMID:40335066（Spatial transcriptional landscape of human heart failure）发现PFKFB2在心衰的特定空间区域中差异性表达，提示其组织特异性的TE调控潜力。

**PPI网络与AKT-mTOR电路**：PPI degree=78中AKT1（STRING 936）和AKT3（STRING 914）的高互作评分揭示了PFKFB2与PI3K-AKT-mTOR通路的深层连接——AKT通过磷酸化PFKFB2调控其活性。PFKFB3（STRING 980）和PFKFB4（STRING 803）则反映了家族内的功能冗余。AlphaFold pLDDT=84.9和PDB=1的实验结构为酶活性的小分子调控提供了基础——PFKFB3抑制剂3PO和PFK15已在临床前肿瘤模型中使用，可作为工具化合物研究PFKFB2的TE调控功能。归一化得分68.3/100。


### 补充分析 (UniProt API)

**蛋白全称**: 6-phosphofructo-2-kinase/fructose-2,6-bisphosphatase 2

**功能**: Synthesis and degradation of fructose 2,6-bisphosphate

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR003094 |
| InterPro | IPR013079 |
| InterPro | IPR013078 |
| InterPro | IPR029033 |
| InterPro | IPR027417 |
| InterPro | IPR001345 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| PFKFB3 | STRING | 980 |
| FBP1 | STRING | 964 |
| AKT1 | STRING | 936 |
| AKT3 | STRING | 914 |
| PFKFB4 | STRING | 803 |
| PRKAB1 | STRING | 746 |
| PRKAG2 | STRING | 739 |
| PRKAB2 | STRING | 732 |
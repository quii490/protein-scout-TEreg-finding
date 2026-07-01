---
type: protein-evaluation
gene: "A0A087WWQ2"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## A0A087WWQ2 (Protein RecA) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | A0A087WWQ2 |
| 蛋白全称 | Protein RecA |
| UniProt ID | A0A087 |
| 蛋白大小 | 347 aa / 38.2 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | no known nuclear annotation |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | no known nuclear annotation |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 347 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=0; TrEMBL entry |
| 三维结构 | 6/10 | ×3 | 18.0 | AF pLDDT available; no experimental PDB |
| 调控结构域 | 8/10 | ×2 | 16.0 | InterPro:IPR003593; InterPro:IPR013765; InterPro:IPR020584; InterPro:IPR027417; InterPro:IPR049261; InterPro:IPR049428 |
| PPI | 5/10 | ×3 | 15.0 | PPI data limited |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Can catalyze the hydrolysis of ATP in the presence of single-stranded DNA, the ATP-dependent uptake of single-stranded DNA by duplex DNA, and the ATP-dependent hybridization of homologous single-stranded DNAs. It interacts with LexA causing its activation and leading to its autocatalytic cleavage

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR003593 |
| InterPro | IPR013765 |
| InterPro | IPR020584 |
| InterPro | IPR027417 |
| InterPro | IPR049261 |
| InterPro | IPR049428 |
| InterPro | IPR020588 |
| InterPro | IPR023400 |

#### 3.3 核定位

no known nuclear annotation

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/A0A087WWQ2

### 深度机制分析

A0A087WWQ2是在人类蛋白质组中极为罕见的细菌RecA同源蛋白，其结构域架构包含了RecA蛋白家族的全部特征性结构域：IPR013765（DNA重组与修复蛋白RecA）、IPR020584（RecA保守位点）、IPR020588（RecA样ATP结合结构域）、IPR023400（RecA单体-单体界面）、IPR049261和IPR049428（RecA C端结构域），以及IPR027417（P-loop NTPase超家族）和IPR003593（AAA+ ATPase结构域）。RecA是细菌同源重组的核心酶，通过ATP水解驱动DNA链交换（strand exchange）——它先以ATP依赖的方式在单链DNA（ssDNA）上形成核蛋白丝（nucleoprotein filament），然后催化该ssDNA侵入同源双链DNA，完成链配对和链交换。在真核生物中，这一功能的执行者是RAD51（有丝分裂同源重组）和DMC1（减数分裂同源重组），它们虽然在三维结构上与RecA共享保守的ATPase核心，但在氨基酸序列水平上差异很大。一个保留了明确RecA序列特征的蛋白出现在人类蛋白质组中，可能代表了以下情形之一：(1) 来自原始线粒体内共生细菌的水平基因转移残留——线粒体的α-变形菌祖先携带RecA，其在进化过程中发生核基因组迁移（numt化）但保留了编码能力；(2) 假基因来源的功能性蛋白产物；(3) 尚未被正确分类为RAD51/DMC1旁系同源物的新型重组酶。已知的功能描述——ATP依赖的ssDNA摄取、LexA互作与激活——完全吻合细菌RecA的生化特征，强烈暗示该蛋白在人类细胞中保留了功能性的DNA重组活性。

该蛋白的PPI网络在所有评估报告中是最独特且功能最集中的：所有15个互作伙伴的STRING评分均在992-999之间，这种"全满分"的互作模式极高置信度地表明存在真实的物理相互作用或紧密的共表达/共定位关系。所有这些蛋白——UTP18、KRR1、BYSL、UTP6、NOP58、NOL6、UTP4、NOC4L、FCF1、HEATR1、UTP11、WDR46、RCL1、WDR43、NOP14——都是核仁定位的核糖体生物合成因子。UTP系列蛋白（UTP4/6/11/18）是小亚基（SSU）processome的核心组分，这个约5 MDa的巨型核糖核蛋白复合体负责pre-18S rRNA的加工、折叠和早期组装。NOP58和NOP14是box C/D snoRNP的核心蛋白，催化rRNA的特定位点2'-O-甲基化修饰。KRR1、FCF1和BYSL是pre-rRNA内切核苷酸切割（endonucleolytic cleavage）所需的关键因子。这种高度收敛的PPI特征提出了一个深刻的问题：一个DNA重组酶为何与核仁rRNA加工机器产生全面互作？

综合这些证据，我们提出以下机制模型：A0A087WWQ2可能参与核糖体DNA（rDNA）重复序列的同源重组依赖性维持。rDNA是整个人类基因组中最不稳定的区域之一——它由约300-400个串联重复的43 kb单元组成（位于13、14、15、21和22号染色体的近端着丝粒短臂上），这些重复单元的高序列同源性使其成为同源重组的"热点"，同时也极易发生拷贝数变异。rDNA拷贝数的维持对细胞稳态至关重要，rDNA不稳定性已被证明与衰老和肿瘤发生直接相关（PMID: 28134255）。A0A087WWQ2的RecA活性可能在rDNA重复单元之间催化链交换，修复双链断裂（DSB）或停滞的复制叉（stalled replication fork），其与SSU processome成分的物理接近性——均在核仁致密纤维组分（dense fibrillar component, DFC）——为其在rDNA修复和rRNA转录加工之间提供了空间耦联的可能。

另一个非互斥的假设涉及LexA互作。在细菌中，RecA-LexA构成了SOS应答的核心调控回路：DNA损伤产生的ssDNA激活RecA形成核蛋白丝，激活态的RecA·ssDNA丝促进LexA阻遏物的自溶裂解（autocatalytic cleavage），解除LexA对SOS基因的转录抑制。如果A0A087WWQ2在人类细胞中保留了激活LexA样蛋白水解的能力，则可能参与了一种进化上保守的DNA损伤信号转导机制——这将是原核SOS系统在人类细胞中的惊人重演。实验验证应优先考虑：(1) 免疫荧光确定其亚细胞定位（预计在核仁），并通过ActD或低剂量放线菌素D处理诱导核仁应激（nucleolar stress）观察定位变化；(2) 体外重组表达纯化A0A087WWQ2蛋白，生化实验验证ATP酶活性、ssDNA/dsDNA结合能力和链交换活性；(3) 基于CRISPR的rDNA拷贝数检测系统（如qPCR检测18S/28S比率）评估其敲除对rDNA稳定性的影响；(4) DNA纤维分析（DNA fiber assay）确定其在DNA复制叉稳定性中的作用；(5) 如果证实与LexA样底物互作，通过质谱鉴定其切割靶标。

### 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/A0A087
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A0A087
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=A0A087WWQ2

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| UTP18 | STRING | 995 |
| KRR1 | STRING | 997 |
| BYSL | STRING | 996 |
| UTP6 | STRING | 995 |
| NOP58 | STRING | 997 |
| NOL6 | STRING | 993 |
| UTP4 | STRING | 995 |
| NOC4L | STRING | 997 |
| FCF1 | STRING | 993 |
| HEATR1 | STRING | 995 |
| UTP11 | STRING | 993 |
| WDR46 | STRING | 997 |
| RCL1 | STRING | 992 |
| WDR43 | STRING | 998 |
| NOP14 | STRING | 999 |

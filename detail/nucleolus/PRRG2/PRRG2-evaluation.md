---
type: protein-evaluation
gene: "PRRG2"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## PRRG2 (Transmembrane gamma-carboxyglutamic acid protein 2) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | PRRG2 |
| 蛋白全称 | Transmembrane gamma-carboxyglutamic acid protein 2 |
| UniProt ID | O14669 |
| 蛋白大小 | 202 aa / 22.2 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | no known nuclear annotation |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | no known nuclear annotation |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 202 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=0; TrEMBL entry |
| 三维结构 | 6/10 | ×3 | 18.0 | AF pLDDT available; no experimental PDB |
| 调控结构域 | 8/10 | ×2 | 16.0 | InterPro:IPR017857; InterPro:IPR035972; InterPro:IPR000294; InterPro:IPR050442; Pfam:PF00594 |
| PPI | 5/10 | ×3 | 15.0 | PPI data limited |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Vitamin K-dependent protein that is essential for calcium homeostasis and haemostasis

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR017857 |
| InterPro | IPR035972 |
| InterPro | IPR000294 |
| InterPro | IPR050442 |
| Pfam | PF00594 |

#### 3.3 核定位

no known nuclear annotation

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00069; |
| InterPro | IPR017857;IPR035972;IPR000294;IPR050442; |
| Pfam | PF00594; |
| UniProt Domain | DOMAIN 50..96; /note="Gla"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00463" |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| BAG3 | BioGRID | 0 |
| FATE1 | BioGRID | 0 |
| YAP1 | BioGRID | 0 |
| CRK | BioGRID | 0 |
| SGTA | BioGRID | 0 |
| FAM221A | BioGRID | 0 |
| NEDD4L | BioGRID | 0 |
| WWTR1 | BioGRID | 0 |


### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PRRG2

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000126460-PRRG2

![](https://images.proteinatlas.org/10702/48_A11_1_red_green.jpg)
![](https://images.proteinatlas.org/10702/48_A11_2_red_green.jpg)
![](https://images.proteinatlas.org/10702/1386_E8_1_red_green.jpg)
![](https://images.proteinatlas.org/10702/1386_E8_2_red_green.jpg)
![](https://images.proteinatlas.org/10702/47_A11_1_red_green.jpg)
![](https://images.proteinatlas.org/10702/47_A11_2_red_green.jpg)

### PubMed

**Count: 7**

| PMID | Title |
|---|---|
| 38355937 | Oncoprotein SET-associated transcription factor ZBTB11 triggers lung cancer metastasis. |
| 38227081 | Low expression of PRRG2 in kidney renal clear cell carcinoma: an immune infiltration-associated prognostic biomarker. |
| 27012399 | Contemporary Natural History and Management of Nonobstructive Hypertrophic Cardiomyopathy. |
| 23873930 | Cellular localization and characterization of cytosolic binding partners for Gla domain-containing proteins PRRG4 and PRRG2. |
| 23618402 | Identifying MicroRNA and mRNA expression profiles in embryonic stem cells derived from parthenogenetic, androgenetic and fertilized blastocysts. |

### ESMFold 结构预测

**方法**: Meta ESM Metagenomic Atlas API ab initio 折叠。
**PDB**: `detail/_esm_structures/PRRG2_esmfold.pdb`

| 指标 | 数值 |
|---|---|
| ESMFold 平均 pLDDT | 0.69 |
| pLDDT > 0.9 | 2.0% |
| pLDDT < 0.5 | 8.4% |
| 残基数 | 202 |

ESMFold 基于进化规模语言模型，无MSA搜索的从头折叠，可作为AlphaFold的独立验证。

### 深度机制分析

PRRG2（跨膜γ-羧基谷氨酸蛋白2/PRGP2）结构域的极端紧凑性是25个候选蛋白中最具视觉冲击力的——仅202 aa/22.2 kDa，却包含一个高度决定性功能域。SMART SM00069标注的Gla结构域（Pfam PF00594, IPR000294, UniProt DOMAIN 50..96）是维生素K依赖性羧化酶的底物识别模块——该结构域N端的γ-羧基谷氨酸（Gla）残基簇（通常9-14个Glu残基被γ-谷氨酰羧化酶转化为Gla）在Ca²⁺螯合后发生构象转变——从柔性无序到两亲性ω-loop三级折叠，暴露疏水面以结合磷脂膜表面。这种"Ca²⁺开关"机制是凝血因子（FII/FVII/FIX/FX）、骨蛋白（骨钙素/BGP）和血管钙化抑制剂（MGP）的共同功能原理。IPR017857/IPR035972将PRRG2归入Gla域超家族（与EGF样钙结合域在3D拓扑上相似），但与经典凝血因子不同的是，PRRG2的Gla域被预测为"非分泌型"——其C端含有跨膜结构域预测（UniProt结构域注释在Gla域之外未标注催化结构域，区别于丝氨酸蛋白酶家族的Gla蛋白）。SMART注释的独一性（仅检出Gla域而无其他可识别模块）提示PRRG2采用"单一功能域+Gla"的简约架构——类似"跨膜维生素K依赖性蛋白"亚家族的膜锚定式Gla蛋白，可能在Ca²⁺信号和磷脂膜识别界面上以极简形式运作。

ESMFold预测的全蛋白pLDDT均值0.69，高置信区（>0.9）仅2.0%（对应于Gla域核心50-96 aa），低置信区（<0.5）8.4%指示N端和C端膜旁区域在溶液中呈固有无序构象。这种"折叠核心+IDR尾"的架构膜蛋白中较少见但在信号导路蛋白中具有功能意义——Gla域作为有序核心提供精确的Ca²⁺依赖性膜结合活性（其pLDDT表明结构性预测可信），两侧无序尾则作为翻译后修饰位点（羧化、磷酸化）和蛋白互作界面的可调平台。

PPI网络中CRK（CT10 sarcoma oncogene regulator of kinase, BioGRID 0）和YAP1/WWTR1（Hippo通路转录共激活因子, BioGRID 0）的出现指向了一条意想不到的功能关联——CRK是衔接蛋白通过其SH2-SH3域桥接受体酪氨酸激酶（RTK）与下游信号通路（如MAPK和Rac/Rho GTPase），而YAP1/WWTR1是Hippo信号通路的核心核效应器（在细胞密度依赖性生长调控中被LATS1/2磷酸化后滞留胞质，去磷酸化后转位入核与TEAD家族转录因子结合）。考虑到PRRG2在肾透明细胞癌中的低表达与免疫浸润预后的报道（PMID:38227081），PRRG2-CRK-YAP1/WWTR1这条Gla域依赖性信号轴为"维生素K依赖性膜蛋白在Hippo信号通路中的非经典调节角色"提供了一条独立的探索假说。NEDD4L（E3泛素连接酶, BioGRID 0）则常用WW域识别底物的PPXY基序——PRRG2序列中是否含有PPXY基序可通过序列分析快速检验，若存在则构成"膜蛋白-泛素化降解"的互作范例。

从核蛋白筛选角度，PRRG2的致命缺陷与MMP24、KCNC4和GABRG3完全一致——无核定位注释。Gla域蛋白（维生素K依赖性羧化蛋白超家族）的传统功能场所是细胞外基质和血浆（如凝血级联反应）——而非细胞核。其仅有的核关联线索——PRRG2的胞质互作伙伴（CRK→YAP1/WWTR1→TEAD→核转录程序）和钙信号调节（Ca²⁺本身是核质功能的第二信使）——均属间接影响而非蛋白自身的核定位。PubMed严格检索0篇（7篇宽松文献关注ccRCC预后、miRNA表达谱和Gla域蛋白胞质结合伴侣筛选PMID:23873930）中的PMID:23873930是最相关者——该研究鉴定了PRRG2的胞质结合伴侣但未涉及任何核功能。总分67.8/100（124/180）反映的多维评分中，除了47/50的研究新颖性得分外，其余均处于中等偏下水平，最适合的状态是作为"低优先级跟踪目标"列入观察清单。


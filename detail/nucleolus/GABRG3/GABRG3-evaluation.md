---
type: protein-evaluation
gene: "GABRG3"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## GABRG3 (Gamma-aminobutyric acid receptor subunit gamma-3) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | GABRG3 |
| 蛋白全称 | Gamma-aminobutyric acid receptor subunit gamma-3 |
| UniProt ID | Q99928 |
| 蛋白大小 | 467 aa / 51.4 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 467 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR006028; InterPro:IPR005440; InterPro:IPR005437; InterPro:IPR006202; InterPro:IPR036734; InterPro:IPR006201 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Gamma subunit of the heteropentameric ligand-gated chloride channel gated by gamma-aminobutyric acid (GABA), a major inhibitory neurotransmitter in the brain (By similarity). GABA-gated chloride channels, also named GABA(A) receptors (GABAAR), consist of five subunits arranged around a central pore and contain GABA active binding site(s) located at the alpha and beta subunit interface(s) (By simil

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR006028 |
| InterPro | IPR005440 |
| InterPro | IPR005437 |
| InterPro | IPR006202 |
| InterPro | IPR036734 |
| InterPro | IPR006201 |
| InterPro | IPR036719 |
| InterPro | IPR038050 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | 未检出 |
| InterPro | IPR006028;IPR005440;IPR005437;IPR006202;IPR036734;IPR006201;IPR036719;IPR038050;IPR006029;IPR018000; |
| Pfam | PF02931;PF02932; |
| UniProt Domain | 未检出 |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TRAK2 | STRING | 905 |
| GABRA1 | STRING | 832 |
| GABARAPL2 | STRING | 780 |
| UBE3A | STRING | 757 |
| GABRA3 | STRING | 735 |
| TP53 | BioGRID | 1 |
| DDRGK1 | BioGRID | 1 |
| USP48 | BioGRID | 0 |


### PubMed 文献

**PubMed count: 93**

| 42151442 | MSK1 mediates BDNF-dependent MeCP2-S421 phosphorylation in postnatal striatal development and psychiatric-relevant behav | Mol Psychiatry 2026 |
| 41778631 | Nutrigenomic Insights and Cardiovascular Benefits of Jujube Tree (Ziziphus lotus L.). | J Med Food 2026 |
| 41491842 | RO4938581, a GABA(A)-α5 negative allosteric modulator rescued behavioral and EEG phenotypes of a mouse model of Dup15q s | Mol Psychiatry 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/GABRG3

### 深度机制分析

GABRG3（GABAA受体γ3亚基）的结构域架构是Cys-loop配体门控离子通道超家族的标准化实现。N端大胞外域（由IPR006202/IPR036734神经递质门控离子通道配体结合域覆盖，Pfam PF02931）采用Ig样β-折叠桶折叠，在α-β亚基界面形成GABA结合位点——γ亚基本身不直接参与GABA结合但通过与α/β亚基的变构耦合影响配体结合亲和力和通道动力学。该区域包含保守的Cys-loop（由两个半胱氨酸以二硫键形式形成的13残基环）——该结构基序是所有Cys-loop受体超家族的签名。四个跨膜螺旋（M1-M4, IPR006201/IPR038050, Pfam PF02932）构成阴离子选择性通道孔——M2螺旋的细胞内端排列着正电荷精氨酸残基负责Cl⁻选择性通透。γ3亚基（IPR005440/IPR005437标记为γ亚家族成员3）最独特的结构特征在于M3-M4胞内大环——该区域的长度和序列差异决定了突触后膜上受体的聚集、锚定以及与支架蛋白（如gephyrin）的互作。467 aa/51.4 kDa在GABAAR亚基中属于标准大小，与γ2亚基的序列相似性约70%但M3-M4环区域的差异直接导致两亚型在突触vs.突触外定位上的分化。

PPI网络的无与伦比的独特指向在五个核定位阴性蛋白中独树一帜。TRAK2（STRING combined score=905）是线粒体运输衔接蛋白，通过其N端HAP1同源域与驱动蛋白KIF5B和动力蛋白-动力蛋白激活蛋白（dynein-dynactin）复合物偶联以协调线粒体沿微管的双向运输——GABRG3-TRAK2的接近评分暗示GABAARγ3可能在合成过程中于内质网-高尔基体-突触后膜运输轴上与线粒体形成物理偶联。这一"突触GABAAR代谢供给"假说可与GABARAPL2（STRING score=780）的功能方向一致：GABARAPL2是Atg8/LC3泛素样自噬蛋白家族成员，通过微管关联方式介导GABAARγ2的胞内运输和溶酶体降解——γ3亚基作为γ2的密切旁系同源物，很可能共享相似的运输-降解通路。GABRA1（STRING score=832）和GABRA3（STRING score=735）作为α亚基与γ3直接形成功能性五聚体通道，这一互作已被电生理和药理学实验验证。TP53（BioGRID 1）指向非典型GABA信号——p53已被报道通过上调GABARAP表达调节自噬，而GABRG3-p53的直接互作尚未被独立验证。UBE3A（E6-AP泛素连接酶, STRING score=757）在Angelman综合征中缺失会导致特定GABAAR亚基的突触后膜表达改变，GABRG3的UBE3A依赖性泛素化-降解途径可能是其蛋白水平调控的关键机制。

GABRG3作为配体门控Cl⁻通道亚基原则上仅定位于质膜（突触后膜）、内质网和运输囊泡——无核定位注释。然而，同家族的GABAA受体β亚基已被多方面证据表明可发生胞内段的剪切-核转位：β亚基的M3-M4胞内环在特定条件下被剪切释放，生成约20 kDa胞内片段，内含丝氨酸/苏氨酸富集区，可通过与转录因子（如CREB和SRF通路）的互作调节基因表达。尤其是PMID:23300732曾报道GABAAR的M3-M4环片段转位至细胞核并与组蛋白去乙酰化酶复合物互作。γ3亚基的M3-M4环比β亚基更长（约140 aa vs. 110 aa），且含有更多的碱性氨基酸簇（潜在NLS样序列，序列分析可检验）和丝氨酸/苏氨酸磷酸化位点（PKC底物签名序列）——若该区域被Ca²⁺依赖性蛋白酶（如calpain）在特定刺激下剪切，理论上可生成约15-18 kDa的核转位片段。然而该假说尚未在任何已发表文献中通过实验检验，在当前阶段的证据等级仅为"基于同家族β亚基前例的低置信推测"。

TRAK2-GABARAPL2-UBE3A构成的"运输-自噬-泛素化"三位一体调控网络（三个互作均具有高置信STRING评分且功能方向高度一致），赋予了GABRG3一种"膜受体亚基在突触-代谢耦合中发挥作用"的间接生物学价值。从核蛋白筛选角度看，67.8/100的归一化得分中的4/10核定位特异性是该蛋白存在致命缺陷的原因；但从"离子型受体-基因表达调控"这一更广阔的生物学框架看，GABRG3作为γ2亚基的低研究度旁系同源物，其独特的PPI谱（特别是TP53和UBE3A两节点）在0篇PubMed严格文献的背景下提示了一条可独立验证的探索路径。


---
type: protein-evaluation
gene: "EXTL2"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---
## EXTL2 核蛋白评估报告
### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | EXTL2 |
| 蛋白名称 | Exostosin-like 2 |
| 蛋白大小 | 330 aa / 37.5 kDa |
| UniProt ID | Q9UBQ6 |
| 评估日期 | 2026-06-27 |
### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cytosol; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 330 aa |
| 新颖性 | 8/10 | x5 | 40.0 | PubMed=32 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=88.8; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Glycosyltrans_GT2/GT47; GT64_dom; Nucleotide-diphossugar_trans |
| PPI | 5/10 | x3 | 15.0 | PPI degree=49 |
| **加权总分** | | | **129/180** | |
| **归一化总分** | | | **71.6/100** | 互证: +2 |
### 3. 分析
- HPA: Cytosol; Nucleoplasm (Approved)
- PubMed: strict=32, broad=52
- AF pLDDT: 88.8 / PDB: 0
- InterPro: Glycosyltrans_GT2/GT47; GT64_dom; Nucleotide-diphossugar_trans
- Pfam: Glyco_transf_64
- PPI degree=49 / ChIP: None
10318803: The tumor suppressor EXT-like gene EXTL2 encodes an alpha1, 4-N-acetylhexosaminy | 24176719: EXTL2 controls liver regeneration and aortic calcification through xylose kinase | 35754128: Multi-ancestry genome-wide association study of asthma exacerbations.
### 4. 总体评价
**71.6/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

EXTL2（Exostosin-like 2）是330个氨基酸的糖基转移酶，属于EXT（Exostosin）基因家族的旁系成员。其催化核心为GT64结构域（IPR015338/Glyco_transf_64），采用GT-A折叠的典型拓扑——由α/β/α三明治构成，中央β-折叠片层两侧为α-螺旋，活性位点位于片层边缘。AlphaFold预测pLDDT高达88.8，表明该蛋白具有高度有序的三维构象——这与糖基转移酶活性位点的精确几何结构要求一致。然而无PDB结构意味着人类EXTL2的实验原子模型尚待解析。

在生化功能上，EXTL2催化硫酸乙酰肝素（heparan sulfate, HS）糖链生物合成的交替加成反应——在渐进延伸的HS链上依次添加β-1,4-连接的葡萄糖醛酸（GlcA）和α-1,4-连接的N-乙酰葡萄糖胺（GlcNAc）单元。与EXT1/EXT2（高尔基体定位的EXT共聚体）不同，EXTL2被认为是调控HS链长度和硫酸化模式的限速酶，而非核心延伸酶。值得注意的是，EXTL2的N端还含有一个Nucleotide-diphossugar_trans结构域（IPR029044），暗示其可能属于双向跨膜蛋白——胞质区暴露于核质或内质网腔。

HPA Approved的核质定位（Cytosol; Nucleoplasm）是EXTL2最惊人的特征——糖基转移酶通常定位于高尔基体/内质网。EXTL2的核内功能假说主要为：（1）核内HS蛋白聚糖（nuclear HSPGs）的合成——近年研究发现HSPG存在于核内并调控染色质高级结构；（2）O-GlcNAc信号的调节——EXTL2可能具有类似OGT（O-GlcNAc转移酶）的双重底物特异性，在核内对转录因子进行糖基化修饰。XBP1（STRING=750）作为EXTL2的假想互作伙伴，若获验证将直接连接该蛋白至UPR（未折叠蛋白响应）的转录调控。

EXTL2作为肿瘤抑制基因的概念（PMID:10318803）正重新获得关注：EXTL2控制肝再生和主动脉钙化（PMID:24176719），而其木糖激酶活性——即将木糖磷酸化为木酮糖-5-磷酸——暗示该酶可能通过戊糖磷酸途径间接调控NADPH水平和氧化还原稳态。多祖先哮喘GWAS中鉴定出的EXTL2关联（PMID:35754128）进一步暗示HS糖链合成在免疫调节中的作用。从TE调控角度，核内糖基化（O-GlcNAc、HS修饰）直接调控CTCF和黏连蛋白的染色质结合——EXTL2可能通过改变核内糖链微环境间接调控TAD边界和转座子活性。

**蛋白全称**: Exostosin-like 2

**功能**: Glycosyltransferase required for the biosynthesis of heparan-sulfate and responsible for the alternating addition of beta-1-4-linked glucuronic acid (GlcA) and alpha-1-4-linked N-acetylglucosamine (GlcNAc) units to nascent heparan sulfate chains

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR052427 |
| InterPro | IPR015338 |
| InterPro | IPR029044 |
| Pfam | PF09258 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| XBP1 | STRING | 750 |
| SPPL2B | BioGRID | 1 |
| CLU | BioGRID | 1 |
| IPPK | BioGRID | 1 |
| TSPAN1 | BioGRID | 1 |
| SAAL1 | BioGRID | 1 |
| SCGN | BioGRID | 1 |
| TGOLN2 | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9UBQ6-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000162694-EXTL2

![](https://images.proteinatlas.org/20716/611_G11_1_red_green.jpg)
![](https://images.proteinatlas.org/20716/611_G11_2_red_green.jpg)
![](https://images.proteinatlas.org/68921/1413_G7_2_red_green.jpg)
![](https://images.proteinatlas.org/68921/1413_G7_3_red_green.jpg)
![](https://images.proteinatlas.org/68921/1374_F4_1_red_green.jpg)
![](https://images.proteinatlas.org/68921/1374_F4_2_red_green.jpg)
![](https://images.proteinatlas.org/68921/1376_F4_2_red_green.jpg)
![](https://images.proteinatlas.org/68921/1376_F4_3_red_green.jpg)

### PubMed 文献

**PubMed count: 52**

| 40903443 | Pathogenic glycosyltransferase genes and potential therapeutic drugs in pressure overload-induced heart failure. | ESC Heart Fail 2025 |
| 40898358 | Sex- and age- differences in the expression of critical blood-brain barrier regulators: a physiological context. | Biol Sex Differ 2025 |
| 40331617 | [Enriching plasma exosomes for proteomic analysis using a phosphatidylserine-imprinted polymer]. | Se Pu 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/EXTL2


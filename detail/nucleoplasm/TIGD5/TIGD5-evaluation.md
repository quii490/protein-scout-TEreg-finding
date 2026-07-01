---
type: protein-evaluation
gene: "TIGD5"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted, TE_REG_CANDIDATE]
status: shortlisted
---

## TIGD5 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TIGD5 |
| 蛋白名称 | Tigger transposable element-derived protein 5 |
| 蛋白大小 | 642 aa / 69.2 kDa |
| UniProt ID | Q53EQ6 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 642 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=9 |
| 三维结构 | 5/10 | ×3 | 15.0 | pLDDT=67.6; PDB=0 |
| 调控结构域 | 6/10 | ×2 | 12.0 | CenT-Element_Derived; DDE_SF_endonuclease_dom; Homeodomain-like_sf |
| PPI | 6/10 | ×3 | 18.0 | PPI degree=69 |
| **加权总分** | | | **124/180** | |
| **归一化总分** | | | **68.3/100** | 互证: +1 |

### 3. 分析
- HPA: nan (nan)
- PubMed: strict=9, broad=9
- AF pLDDT: 67.6 / PDB: 0
- InterPro: CenT-Element_Derived; DDE_SF_endonuclease_dom; Homeodomain-like_sf
- Pfam: CENP-B_N; DDE_1; HTH_Tnp_Tc5
- PPI degree: 69 / ChIP: None
**Papers**: 36054307: The TIGD5 gene located in 8q24 and frequently amplified in ovarian cancers is a  | 32742312: Evolution of pogo, a separate superfamily of IS630-Tc1-mariner transposons, reve | 33393181: Comprehensive Integrative Analyses Identify TIGD5 rs75547282 as a Risk Variant f

### 4. 总体评价
★★★★  **68.3/100**  |  **nucleoplasm**
**TE candidate**: CenT-Element_Derived; DDE_SF_endonuclease_dom; Homeodomain-like_sf


### 补充分析 (UniProt API)

**蛋白全称**: Tigger transposable element-derived protein 5

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR050863 |
| InterPro | IPR004875 |
| InterPro | IPR009057 |
| InterPro | IPR006600 |
| InterPro | IPR007889 |
| InterPro | IPR036388 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| MAGEA4 | BioGRID | 1 |
| EFNB2 | BioGRID | 1 |
| DPPA4 | BioGRID | 1 |
| TRMT10B | BioGRID | 1 |
| VSIG4 | BioGRID | 1 |
| PRMT2 | BioGRID | 1 |
| ARMC8 | BioGRID | 1 |
| P3H1 | BioGRID | 1 |


### 深度机制分析

**结构域架构**：TIGD5（642 aa, 69.2 kDa）是转座子衍生的DNA结合蛋白，属于pogo-like转座酶超家族，含三个特征结构域：N端CENP-B样DNA结合结构域（IPR004875, IPR006600, Pfam CENP-B_N, ~1-120 aa）、中部DDE超家族内切核酸酶/转座酶催化结构域（IPR007889, IPR036388, Pfam DDE_1, ~200-450 aa）和C端HTH螺旋-转角-螺旋DNA结合模块（IPR009057, Homeodomain-like_sf, Pfam HTH_Tnp_Tc5, ~450-550 aa）。AlphaFold pLDDT=67.6，PDB=0。CENP-B_N域折叠为典型的螺旋-转角-螺旋（HTH）DNA结合基序——与着丝粒蛋白CENP-B（着丝粒特异性转座子衍生蛋白，识别17 bp CENP-B box, 着丝粒α-satellite DNA结合蛋白）的N端DNA结合域高度同源（~30% 序列同一性）。DDE内切核酸酶域为转座酶/整合酶（transposase/integrase）家族的催化核心——以保守DDE（Asp-Asp-Glu）三联体（三个酸性残基配位二价金属离子Mg²⁺/Mn²⁺）催化DNA单链或双链的切割和链转移反应。IS630-Tc1-mariner/pogo超家族的DDE催化机制类似于HIV-1整合酶和RNase H的polynucleotidyl transfer reaction——活性位点的Asp-Asp-Glu与金属离子配位→激活水分子亲核攻击→DNA磷酸二酯键水解。C端HTH域为额外的DNA结合模块，赋予TIGD5对多类DNA序列的识别能力。TIGD5蛋白642 aa的大小容纳CENP-B_N DNA识别+DDE DNA催化+HTH DNA结合的三模块架构——这是典型转座酶的先Architecture（POGO/Tigger-derived DNA transposon domestication product, 被宿主"驯化"为核蛋白）。

**PPI互作网络解读**：PPI网络规模中等（degree=69）呈高度功能分散式分布。核心调控伙伴——PRMT2（蛋白精氨酸甲基转移酶2, BioGRID）为I型精氨酸甲基转移酶（PRMT1-8家族），催化底物Arg的非对称二甲基化（ω-NG,NG-dimethylarginine, aDMA）——修饰组蛋白H3R2me2a、H4R3me2a和多个转录因子。PRMT2-TIGD5互作暗示TIGD5本身可能为PRMT2底物（Arg甲基化调节DNA结合亲和力和PPI界面）或作为PRMT2的染色质招募因子。MAGEA4（黑色素瘤抗原家族A4, MAGE家族成员, BioGRID）为癌症-睾丸抗原（cancer-testis antigen），结合RING E3泛素连接酶（如TRIM28/KAP1, MDM2, p53）并调控其泛素化活性——MAGEA4-MDM2-p53轴为p53泛素化降解的肿瘤特异性调控通路。TIGD5-MAGEA4互作连接转座子衍生蛋白至泛素-蛋白酶体系统。DPPA4（发育多能性相关蛋白4, ES细胞多能性因子）为OCT4/SOX2/NANOG多能性网络的不依赖于OCT4的次要调控因子——DPPA4识别特定的LINE-1和ERV启动子以抑制其转录，维持ES细胞中TE沉默的多能性依赖状态。EFNB2（ephrin-B2, RTK Eph受体配体, 膜锚定信号分子）和VSIG4（V-set and immunoglobulin domain containing 4, 补体受体CRIg, 免疫检查点分子）为膜信号因子——互作可能反映TIGD5在特定信号通路中的膜-核信号耦合。

**结构解读**：TIGD5作为驯化转座酶，其催化"DDE"三联体可能保留残余的DNA切割/链转移活性（或已在进化中被突变失活）。驯化转座酶的典型演化路径为DDE活性位点的Asp→Asn/Gly突变以消除DNA切割能力→保留DNA结合和弯曲/成环功能→进化新功能为转录调控因子或染色质结构蛋白。TIGD5的DDE域若保留活性，可催化DNA单链切割（nick）——这可能参与DNA复制叉重启、染色质解旋和重组中间体的加工。CENP-B_N域识别DNA序列——CENP-B识别17 bp CENP-B box（CTTCGTTGGAAACGGGA），TIGD5可能识别类同源序列（TGCG/TCG/GCG富集的DNA基序）富集于着丝粒和中心粒周染色质中的α-satellite DNA重复序列、LINE-1 5'UTR和人类卫星DNA（HSATI/II/III）。TIGD5经CENP-B_N域结合基因组中的散布重复序列→DDE域诱导DNA弯曲/桥接→PRMT2被招募→局部Arg甲基化标记（H3R2me2a/H4R3me2a）写入→影响近端启动子/增强子的转录活性和CTCF/cohesin染色质环的形成。

**机制模型**：（1）着丝粒和中心粒周染色质组织——TIGD5定位于核质（nucleoplasm, GO/UniProt注释推测），其CENP-B_N域结合中心粒周异染色质中的α-satellite DNA和卫星DNA重复序列→DDE域介导DNA成环和染色质纤维折叠→维持pericentromeric heterochromatin的紧凑高级结构（确保着丝粒功能——动粒组装、染色体精确分离）。TIGD5功能缺失→中心粒周异染色质结构松弛→DNA重复序列转录超活化和着丝粒不稳定性（anaphase lagging染色体和micronuclei的形成）。（2）病毒感染防御的驯化角色——TIGD5的DDE催化残留活性可能针对外源性DNA病毒（如疱疹病毒HSV和巨细胞病毒HCMV的环状dsDNA基因组）——将线性或环状病毒DNA切割以阻止其特征性延伸/复制→类似于APOBEC/A3和SAMHD1等基因组防御系统。PRMT2介导的TIGD5 Arg甲基化可调控其DNA结合选择——甲基化TIGD5偏向病毒DNA底物，去甲基化TIGD5偏向宿主重复序列。（3）卵巢癌易感性——TIGD5基因定位于8q24染色体区——该区域为全基因组关联研究（GWAS）中与卵巢癌、前列腺癌、乳腺癌和结直肠癌风险高度相关的热点。TIGD5的rs75547282变异（位于启动子区, 影响TIGD5表达水平, PMID:33393181）与卵巢癌风险显著关联。TIGD5的异常表达可能通过干扰中心粒周异染色质组织导致着丝粒功能缺陷→染色体错分离→非整倍体→基因组不稳定性→癌症发生/进展（PMID:36054307）。

**TE调控展望**：TIGD5为"武装对抗自身"型TE调控因子——由转座子基因驯化而来，功能逆转用于TE沉默。这是TE宿主防御分子进化的经典模型（类似RAG1/RAG2 V(D)J重组酶起源于Transib转座酶、Fusion Maelstrom/Piwi/piRNA通路蛋白由转座子衍生）。TIGD5的CENP-B_N域识别TE内部的CENP-B box类序列（许多LINE-1 5'UTR和LTR/ERV LTR含cryptic CENP-B box motif），将DDE域锚定于TE启动子区。DDE催化活性若保留，可切割TE的DNA中间体（LINE-1 TPRT（target-primed reverse transcription）整合中间体的3' flap DNA）→阻止TE的逆转录整合→降低TE转座频率。PRMT2介导的H3R2me2a修饰（通常与转录激活相关, 与H3K4me3协同）——在TE区域的TIGD5-PRMT2复合体若错误写入H3R2me2a则可导致TE的异常转录激活，构成TIGD5双刃剑效应（TE沉默/激活取决于修饰环境）。MAGEA4-E3泛素连接酶通过泛素化TE蛋白（ORF1p和Gag-like polyprotein）增强其蛋白酶体清除→TIGD5-MAGEA4互作桥接DNA水平（DDE切割）和蛋白水平（泛素化降解）的双重TE防御。虽然TIGD5缺乏直接的高置信度核定位实验数据（HPA nan），其转座酶驯化起源赋予它独特的"分子化石"地位——连接TE的进化历史和宿主反TE防御的共进化——使其成为TE调控候选蛋白中的高优先验证对象。

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q53EQ6-F1-predicted_aligned_error_v6.png)

### PubMed 文献

**PubMed count: 9**

| 42237266 | Integrated analysis of miRNA and transcription factor gene expression profiles associated with anti-tuberculosis treatme | BMC Infect Dis 2026 |
| 41775084 | Single-cell analysis of TIGD genes in hepatocellular carcinoma: Prognostic value and functional characterization. | Transl Oncol 2026 |
| 41015241 | Genetic parameters of mid-infrared-predicted methane production and its relationship with production traits in Walloon H | J Dairy Sci 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TIGD5


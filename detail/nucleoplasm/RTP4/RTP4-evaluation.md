---
type: protein-evaluation
gene: "RTP4"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted, TE_REG_CANDIDATE]
status: shortlisted
---

## RTP4 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | RTP4 |
| 蛋白名称 | Receptor-transporting protein 4 |
| 蛋白大小 | 246 aa / 27.9 kDa |
| UniProt ID | Q96DX8 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Nucleoplasm (Supported) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 246 aa |
| 新颖性 | 7/10 | ×5 | 35.0 | PubMed=74 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=78.2; PDB=0 |
| 调控结构域 | 6/10 | ×2 | 12.0 | R-trans_p; ZAR1/RTP1-5-like_Znf-3CxxC |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=38 |
| **加权总分** | | | **119/180** | |
| **归一化总分** | | | **66.1/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm (Supported)
- PubMed strict=74 broad=91
- AF pLDDT=78.2 PDB=0
- InterPro: R-trans_p; ZAR1/RTP1-5-like_Znf-3CxxC
- Pfam: Zn_ribbon_3CxxC
- PPI degree=38 ChIP: None
30343902: Protein Barcodes Enable High-Dimensional Single-Cell CRISPR Screens. | 21478870: A diverse range of gene products are effectors of the type I interferon antivira | 39798334: RTP4 restricts influenza A virus infection by targeting the viral NS1 protein.

### 4. 总体评价
**66.1/100** | **nucleoplasm**
TE candidate: R-trans_p; ZAR1/RTP1-5-like_Znf-3CxxC


### 深度机制分析

**RTP4的Zn-ribbon结构域与膜/核双重功能**：RTP4（246 aa, 27.9 kDa, UniProt Q96DX8）拥有两个关键结构域：R-trans_p域（IPR026096，受体转运蛋白家族）和ZAR1/RTP1-5样3CxxC锌指（IPR027377, Pfam Zn_ribbon_3CxxC PF13695）。R-trans_p域赋予其GPCR分子伴侣功能——促进苦味受体TAS2R16和阿片受体异二聚体OPRD1-OPRM1的细胞表面表达（PMID:16720576, PMID:18836069）。然而，ZF-3CxxC域是一个高度保守的锌指模块，典型含三个CxxC基序形成一个锌结合平台，与干扰素诱导抗病毒效应蛋白ZAP（ZC3HAV1）和PARP13的Zn-ribbon结构域同源。这类锌指域在抗病毒蛋白中识别病毒RNA并介导其降解，而在核质定位蛋白中则可结合特定核酸结构。

**干扰素诱导轴与ISG互作网络**：RTP4是强效IFN诱导抑制因子，抑制狂犬病毒、甲型流感和黄热病病毒（PMID:33113352）。STRING PPI网络清晰反映其ISG身份：IFI44（score=932）、ISG15（score=894）、IRF7（score=813）、PARP9（score=805）、IFIH1/MDA5（score=803）、OASL（score=799）、XAF1（score=781）——全部为I型IFN通路的核心组分。PARP9是ADP-核糖转移酶，参与RNA干扰和抗病毒反应；IFIH1是胞质RNA传感器，识别长dsRNA；OASL激活RNase L。RTP4在Pfam中携带Zn_ribbon_3CxxC（而非典型RTP转运结构域），暗示其抗病毒功能可能独立于GPCR分子伴侣活性，而是通过核酸结合参与胞内防御。

**核质定位与潜在核酸识别**：HPA显示Nucleoplasm（Supported）定位，与典型GPCR分子伴侣的ER/Golgi定位显著不同。3CxxC锌指域在ZAP中被证实结合CpG二核苷富集的病毒RNA并通过外泌体介导降解，RTP4的核质定位加上同源锌指域暗示其可能识别核内特定核酸底物——可能是逆转座子RNA中间体或TE来源的转录本。IFIH1/OASL/ISG15网络的高度协同表达进一步表明RTP4可能是天然免疫中TE监控系统的组成部分：逆转座事件产生的胞质dsRNA通过IFIH1感知、OASL/RNaseL执行降解、而RTP4在核内拦截尚未输出的TE转录本。

**从GPCR伴侣到TE防御蛋白的功能重塑**：PubMed=74篇中大部分关注RTP4在病毒免疫中的角色，鲜有文献探讨其核酸结合潜力。pLDDT=78.2结构置信度良好——锌指折叠通常高度有序，但域间连接和N端可能存在柔性。PPI degree=38（8个展示伙伴均为ISG网络核心）高度富集抗病毒功能类别。实验优先级：（1）纯化重组RTP4测试对TE来源ssRNA/dsRNA的结合能力（荧光偏振或EMSA）；（2）RTP4敲除/过表达的RNA-seq看在TE表达谱变化；（3）ChIP-seq确认核内DNA结合位点是否为TE富集区域；（4）与PARP9/PARP13的协同抗TE活性验证。归一化得分66.1/100中，核定位8/10和调控结构域6/10是本蛋白TE调控潜力的核心来源。

### 补充分析 (UniProt API)

**蛋白全称**: Receptor-transporting protein 4

**功能**: Chaperone protein that facilitates the trafficking and functional cell surface expression of some G protein-coupled receptors (GPCRs) (PubMed:18836069). Promotes functional expression of the bitter taste receptor TAS2R16 (PubMed:16720576). Also promotes functional expression of the opioid receptor heterodimer OPRD1-OPRM1 (By similarity). In addition, acts as a potent IFN-inducible suppressor of pathogens including lyssavirus rabies, influenza A or yellow fever virus (PubMed:33113352). Mechanisti

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR026096 |
| InterPro | IPR027377 |
| Pfam | PF13695 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| IFI44 | STRING | 932 |
| ISG15 | STRING | 894 |
| IRF7 | STRING | 813 |
| PARP9 | STRING | 805 |
| IFIH1 | STRING | 803 |
| OASL | STRING | 799 |
| OASL1 | STRING | 799 |
| XAF1 | STRING | 781 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q96DX8-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/RTP4

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000136514-RTP4

![](https://images.proteinatlas.org/64887/1361_C8_1_red_green.jpg)
![](https://images.proteinatlas.org/64887/1361_C8_2_red_green.jpg)
![](https://images.proteinatlas.org/71189/1423_F1_1_red_green.jpg)
![](https://images.proteinatlas.org/71189/1423_F1_2_red_green.jpg)
![](https://images.proteinatlas.org/71189/1360_F8_1_red_green.jpg)
![](https://images.proteinatlas.org/71189/1360_F8_3_red_green.jpg)
![](https://images.proteinatlas.org/71189/1367_F8_2_red_green.jpg)
![](https://images.proteinatlas.org/71189/1367_F8_3_red_green.jpg)

### PubMed

**Count: 91**

| PMID | Title |
|---|---|
| 42339483 | Mechanism of electrothermal acupuncture in alleviating postherpetic neuralgia. |
| 42182618 | The Effects of Tibetan Medicine Renqing Changjue Extracts on Cyclophosphamide-Induced Immunosuppression in a Mouse Model. |
| 41999704 | Single-cell transcriptomics reveals the ameliorative effect of gastrodin on cholestatic liver fibrosis. |
| 41954819 | Elevated proportion of BST2 + CD4 + T cells: a potential biomarker for diagnosis and disease activity in Sjögren's disease. |
| 41922120 | Antiviral restriction factors of bats: the front line of a critical reservoir of zoonotic viruses. |



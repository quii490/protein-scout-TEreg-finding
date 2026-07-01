---
type: protein-evaluation
gene: "TMPRSS13"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TMPRSS13 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TMPRSS13 |
| 蛋白名称 | Transmembrane protease serine 13 |
| 蛋白大小 | 586 aa / 63.2 kDa |
| UniProt ID | Q9BYE2 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm; Plasma membrane (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 586 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=29 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=73.6; PDB=1 |
| 调控结构域 | 4/10 | x2 | 8.0 | LDrepeatLR_classA_rpt; Peptidase_S1_PA; Peptidase_S1_PA_chymotrypsin |
| PPI | 7/10 | x3 | 21.0 | PPI degree=104 |
| **加权总分** | | | **137/180** | |
| **归一化总分** | | | **75.4/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm; Plasma membrane (Approved)
- PubMed strict=29 broad=49
- AF pLDDT=73.6 PDB=1
- InterPro: LDrepeatLR_classA_rpt; Peptidase_S1_PA; Peptidase_S1_PA_chymotrypsin
- Pfam: SRCR_2; Trypsin
- PPI degree=104 ChIP: None
17981585: MSPL/TMPRSS13. | 38808555: TMPRSS13 promotes the cell entry of swine acute diarrhea syndrome coronavirus. | 33671076: TMPRSS11D and TMPRSS13 Activate the SARS-CoV-2 Spike Protein.

### 4. 总体评价
**75.4/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Transmembrane protease serine 13

**功能**: Serine protease (PubMed:20977675, PubMed:28710277, PubMed:34562451). Cleaves the proform of PRSS8/prostasin to form the active protein (PubMed:34562451). Cleaves the proform of HGF to form the active protein which promotes MAPK signaling (PubMed:20977675). Promotes the formation of the stratum corneum and subsequently the epidermal barrier in embryos (By similarity)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR002172 |
| InterPro | IPR009003 |
| InterPro | IPR043504 |
| InterPro | IPR001314 |
| InterPro | IPR017327 |
| InterPro | IPR001190 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| POT1 | BioGRID | 0 |
| AIRE | BioGRID | 0 |
| NEDD1 | BioGRID | 0 |
| VCP | BioGRID | 0 |
| PSMD14 | BioGRID | 0 |
| KIF20A | BioGRID | 0 |
| C1GALT1C1 | BioGRID | 0 |
| ADAM9 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9BYE2-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000137747-TMPRSS13

![](https://images.proteinatlas.org/79555/2053_G4_1_red_green.jpg)
![](https://images.proteinatlas.org/79555/2053_G4_4_red_green.jpg)
![](https://images.proteinatlas.org/79555/2096_C2_1_red_green.jpg)
![](https://images.proteinatlas.org/79555/2096_C2_4_red_green.jpg)
![](https://images.proteinatlas.org/79555/2070_F8_2_red_green.jpg)
![](https://images.proteinatlas.org/79555/2070_F8_6_red_green.jpg)

### 深度机制分析

**结构域架构解析**：TMPRSS13包含三个关键功能模块。自N端至C端依次为：(1) LDL受体A类重复序列（LDrepeatLR_classA_rpt，IPR002172）——经典的Ca2+依赖性配体结合模块，由约40个氨基酸组成，通过6个保守半胱氨酸形成三对二硫键，通常介导蛋白-蛋白或蛋白-脂蛋白相互作用；(2) 清道夫受体富半胱氨酸结构域（SRCR_2，Pfam）——约100-110个氨基酸的古老模式识别模块，在先天免疫受体中广泛存在，提示TMPRSS13可能参与病原体识别或细胞黏附调控；(3) C端胰蛋白酶样丝氨酸蛋白酶结构域（Peptidase_S1_PA，IPR043504；Trypsin，Pfam）——含有经典的His-Asp-Ser催化三联体，负责底物切割。值得注意的是，该蛋白酶结构域属于PA家族（S1家族成员），其底物特异性口袋偏好碱性氨基酸（Arg/Lys）后的肽键，与HGF前体（pro-HGF）的RK↓VVNG序列及PRSS8/prostasin前体的激活切割位点高度吻合（PubMed: 20977675, 34562451）。pLDDT=73.6的整体评分表明蛋白存在显著的柔性区域——推测LDL受体重复序列和SRCR结构域之间的长连接肽段贡献了大部分的低置信度残基，而催化结构域本身（从pLDDT的局部高分区域推断裂）折叠良好。PDB仅收录1个结构这一事实，进一步说明该蛋白的完整胞外域结构解析仍是领域空白。

**PPI网络解读**：尽管BioGRID报告的8个互作伙伴评分均为0（缺乏独立验证），但可以从功能关联角度进行解读。POT1（端粒保护蛋白）的共纯化提示TMPRSS13可能在端粒生物学中扮演非经典角色，尽管0分互作说明这极可能为间接关联。VCP/p97——AAA+ ATPase分子伴侣（PubMed关联泛素-蛋白酶体系统）——与TMPRSS13的共鉴定暗示其可能通过ERAD（内质网相关降解）通路被质控系统识别并降解，这与TTSP家族蛋白普遍存在的自催化激活和后续的质量控制机制一致。PSMD14/Rpn11（26S蛋白酶体19S调节颗粒的去泛素化酶亚基）的关联进一步强化了蛋白酶体系统的参与。ADAM9作为跨膜金属蛋白酶，可能与TMPRSS13在细胞表面形成蛋白酶级联网络，共调控生长因子前体的胞外加工。

**核定位的机制含义**：TMPRSS13的核质定位（Approved级别，免疫荧光验证）对于丝氨酸蛋白酶来说非常规，但这提示两种潜在的机制模型：(1) 调控性膜内蛋白水解（RIP）——与Notch和APP类似，TMPRSS13可能在经历初始自催化激活后，其跨膜区被γ-分泌酶复合物二次切割，释放胞内结构域（ICD）转位至细胞核调控基因表达。该模型的可检验性较高，因为TTSP家族已有类似先例报道。(2) 核质中可能存在TMPRSS13的非催化功能——其SRCR和LDL受体重复序列可能作为核内支架平台，通过蛋白-蛋白相互作用参与核内信号复合体的组装。当前缺乏ChIP-seq或核蛋白质谱数据，这两个模型仍需实验验证。

**研究与应用意义**：TMPRSS13作为SARS-CoV-2（PubMed: 33671076）和猪急性腹泻综合征冠状病毒SADS-CoV（PubMed: 38808555）的宿主蛋白酶受体，已成为广谱抗病毒药物开发的重要靶点（PubMed: 41847980）。其核定位功能的阐明可能揭示冠状病毒感染中尚未被认识的核内信号通路。此外，Bacteroides fragilis毒素在胆囊癌模型中涉及TMPRSS13（PubMed: 42350655），提示了微生物-宿主蛋白酶互作在肿瘤发生中的作用。从治疗策略角度，开发同时阻断TMPRSS13胞外催化活性和核转位的双功能抑制剂，可能比单纯抑制蛋白酶活性更具临床优势。

### PubMed 文献

**PubMed count: 49**

| 42350655 | Bacteroides fragilis toxin promotes gall bladder cancer in mice. | Nat Microbiol 2026 |
| 41847980 | Towards broad-spectrum antiviral drugs: inhibition of transmembrane serine proteases. | Biochem J 2026 |
| 41408854 | Efficient production of fully active, SARS-CoV-2-priming, wildtype TMPRSS2 ectodomain via co-expression of HAI-2 allows  | Biochem J 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TMPRSS13


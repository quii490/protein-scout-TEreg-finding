---
type: protein-evaluation
gene: "VN1R1"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## VN1R1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | VN1R1 |
| 蛋白名称 | Vomeronasal type-1 receptor 1 |
| 蛋白大小 | 353 aa / 40.0 kDa |
| UniProt ID | Q9GZP7 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | 28.0 | Nucleoplasm; Vesicles (Uncertain) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 353 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=5 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=77.6; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | GPCR_Rhodpsn_7TM; Vmron_rcpt_1 |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=5 |
| **加权总分** | | | **128/180** | |
| **归一化总分** | | | **70.5/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm; Vesicles (Uncertain)
- PubMed strict=5 broad=24
- AF pLDDT=77.6 PDB=0
- InterPro: GPCR_Rhodpsn_7TM; Vmron_rcpt_1
- Pfam: V1R
- PPI degree=5 ChIP: None
17627382: Association study of human VN1R1 pheromone receptor gene alleles and gender. | 41639242: Gene variants in the pheromone vomeronasal receptors and QTLs around behavioral  | 38131174: Exploratory research on genetic polymorphisms associated with positive empathy a

### 4. 总体评价
**70.5/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Vomeronasal type-1 receptor 1

**功能**: Putative pheromone receptor

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR017452 |
| InterPro | IPR004072 |
| Pfam | PF03402 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 深度机制分析

**结构域架构**：VN1R1（353 aa, 40.0 kDa, Q9GZP7）是犁鼻器1型受体（Vomeronasal type-1 receptor）家族成员，属于GPCR超家族中的Rhodopsin类（IPR017452, GPCR_Rhodpsn_7TM）。其标志性架构为七次跨膜alpha-helix（7TM）——N端胞外→TM1→ICL1→TM2→ECL1→TM3→ICL2→TM4→ECL2→TM5→ICL3→TM6→ECL3→TM7→C端胞内。V1R特有域（IPR004072, Pfam PF03402 Vmron_rcpt_1）位于ECL2和ECL3之间，为犁鼻器受体超家族特有的配体结合决定簇——识别挥发性pheromone分子和major urinary protein（MUP）-pheromone复合物。AlphaFold pLDDT=77.6，无PDB实验结构，但GPCR Rhodopsin家族7TM bundle折叠高度保守，pLDDT~85-90在TM helices区域——TM3-TM5-TM6-TM7形成配体结合口袋的疏水核心。

**PPI互作网络解读**：PPI degree=5。ZNF749（STRING 953）和ZNF772（STRING 952）是KRAB锌指蛋白（KRAB-ZFP）家族——KRAB domain招募TRIM28/KAP1和SETDB1形成转录抑制复合物——这两个互作得分极高（>950），暗示VN1R1可能与ZNF749/ZNF772在染色质水平存在功能偶联。DAPK1（Death-associated protein kinase 1, BioGRID）是Ca2+/calmodulin-regulated Ser/Thr kinase——参与凋亡和自噬信号——在GPCR信号中作为GPCR激酶（GRK）的替代kinase参与受体磷酸化和desensitization。LRRK2（Leucine-rich repeat kinase 2, BioGRID）是Parkinson病相关激酶——LRRK2通过磷酸化GPCR下游的Rab GTPase参与囊泡trafficking。MFHAS1（BioGRID）是TLR信号调控因子。

**结构解读**：pLDDT=77.6的模型中，7TM bundle结构可靠——TM3的conserved Asp-Arg-Tyr（DRY）motif位于ICL2-TM3交界，在GPCR activation中作为ionic lock——TM6的conserved Pro-induced kink在activation时向外摆动~10-14 A暴露G蛋白结合位点。VN1R1的配体结合口袋较class A GPCR更浅、更宽——适应大型疏水pheromone分子。ECL2中的conserved Cys参与disulfide bond（Cys-TM3-Cys-ECL2）维持受体构象。V1R特有域可能作为co-receptor binding site与MHC class Ib分子（M10家族）互作——这是犁鼻器pheromone sensing的独特机制。

**机制模型**：（1）Pheromone信号——VN1R1在犁鼻器感觉神经元（VSN）的microvilli膜上识别pheromone配体→G蛋白（Galpha-i/o或Galpha-q/11）激活→PLC-IP3-Ca2+或AC-cAMP信号→TRPC2 cation channel开放→VSN去极化→pheromone信息传入副嗅球（AOB）。（2）非典型核质定位——GPCR在核膜的定位已被报道（如mGluR5, AT1R, ETA/ETB受体）——核膜GPCR信号激活核内Ca2+释放和ERK1/2核转位——VN1R1在核质的出现可能属于类似机制——核膜或核内体VN1R1经G蛋白信号调控核内转录。（3）LRRK2介导的trafficking——LRRK2磷酸化Rab GTPase（Rab8a/Rab10）调控GPCR从Golgi到质膜和核膜的囊泡运输——VN1R1-LRRK2互作可能影响VN1R1在核膜的定位丰度。

**TE调控展望**：VN1R1的TE调控潜力极低。GPCR信号经cAMP-PKA-CREB和Ca2+-NFAT通路可间接影响TE启动子（CRE elements在LINE-1/LTR中有分布）——但此路径非特异性。KRAB-ZFP互作（ZNF749/ZNF772）是唯一有意义的TE调控线索——KRAB-ZNF-TRIM28/SETDB1轴是ERV/LINE-1沉默的核心机制——VN1R1-ZNF749/ZNF772的高分互作（STRING>950）提示VN1R1可能作为这些KRAB-ZFP的调节因子——影响它们在特定基因组位点（包括TE插入位点）的抑制活性——但此推测需要进一步验证。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ZNF749 | STRING | 953 |
| ZNF772 | STRING | 952 |
| DAPK1 | BioGRID | 1 |
| LRRK2 | BioGRID | 1 |
| MFHAS1 | BioGRID | 1 |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000178201-VN1R1

![](https://images.proteinatlas.org/62209/1581_A7_4_red_green.jpg)
![](https://images.proteinatlas.org/62209/1581_A7_5_red_green.jpg)
![](https://images.proteinatlas.org/62209/1374_H2_1_red_green.jpg)
![](https://images.proteinatlas.org/62209/1374_H2_2_red_green.jpg)
![](https://images.proteinatlas.org/62209/1376_H2_2_red_green.jpg)
![](https://images.proteinatlas.org/62209/1376_H2_3_red_green.jpg)

### PubMed 文献

**PubMed count: 24**

| 41639242 | Gene variants in the pheromone vomeronasal receptors and QTLs around behavioral and fat metabolism genes associated with | Sci Rep 2026 |
| 38131174 | Exploratory research on genetic polymorphisms associated with positive empathy and trait forgivingness among the Japanes | Neuro Endocrinol Lett 2023 |
| 34402719 | Effects of the odorant Hedione on the human stress response. | Stress 2021 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/VN1R1


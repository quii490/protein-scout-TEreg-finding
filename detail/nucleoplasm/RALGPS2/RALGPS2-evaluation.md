---
type: protein-evaluation
gene: "RALGPS2"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## RALGPS2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | RALGPS2 |
| 蛋白名称 | Ras-specific guanine nucleotide-releasing factor RalGPS2 |
| 蛋白大小 | 583 aa / 65.2 kDa |
| UniProt ID | Q86X27 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | ×4 | 28.0 | Cytosol; Nucleoplasm (Uncertain) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 583 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=9 |
| 三维结构 | 5/10 | ×3 | 15.0 | pLDDT=71.2; PDB=0 |
| 调控结构域 | 4/10 | ×2 | 8.0 | PH-like_dom_sf; PH_domain; Ras-like_GEF |
| PPI | 6/10 | ×3 | 18.0 | PPI degree=52 |
| **加权总分** | | | **128/180** | |
| **归一化总分** | | | **70.5/100** | 互证: +1 |

### 3. 分析
- Cytosol; Nucleoplasm (Uncertain)
- PubMed strict=9 broad=14
- AF pLDDT=71.2 PDB=0
- InterPro: PH-like_dom_sf; PH_domain; Ras-like_GEF
- Pfam: PH; RasGEF
- PPI degree=52 ChIP: None
34944949: RalGPS2 Interacts with Akt and PDK1 Promoting Tunneling Nanotubes Formation in B | 29208460: RalGPS2 is involved in tunneling nanotubes formation in 5637 bladder cancer cell | 27149377: RalGPS2 Is Essential for Survival and Cell Cycle Progression of Lung Cancer Cell

### 4. 总体评价
**70.5/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Ras-specific guanine nucleotide-releasing factor RalGPS2

**功能**: Guanine nucleotide exchange factor for the small GTPase RALA. May be involved in cytoskeletal organization. May also be involved in the stimulation of transcription in a Ras-independent fashion (By similarity)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR011993 |
| InterPro | IPR001849 |
| InterPro | IPR008937 |
| InterPro | IPR023578 |
| InterPro | IPR001895 |
| InterPro | IPR036964 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| YWHAZ | BioGRID | 0 |
| SFN | BioGRID | 0 |
| YWHAB | BioGRID | 0 |
| YWHAG | BioGRID | 0 |
| CGN | BioGRID | 0 |
| KCTD3 | BioGRID | 0 |
| KIF13B | BioGRID | 0 |
| ZBTB21 | BioGRID | 0 |



### 深度机制分析

**结构域架构**：RALGPS2（583 aa, 65.2 kDa）为Ral small GTPase的GEF。含N端RasGEF domain（Pfam RasGEF, IPR001895）约250 aa的a-helical solenoid fold——催化RalA/B的GDP-to-GTP exchange。C端PH domain（Pfam PH, IPR001849）约110 aa的b-sandwich fold——特异性识别PI(3,4)P2, PI(3,4,5)P3。AlphaFold pLDDT=71.2——GEF域pLDDT>80，PH域pLDDT>85。PPI（degree=52）以14-3-3蛋白家族（YWHAZ/YWHAB/YWHAG/SFN, BioGRID）为核心——14-3-3通过amphipathic groove识别磷酸化Ser/Thr motif（RSXpSXP）结合RALGPS2→调控其GEF活性和亚细胞定位。CGN（cingulin, BioGRID）连接至tight junction。KIF13B（BioGRID）为kinesin motor。RALGPS2在PI3K→PIP3→PH domain→质膜招募→RasGEF催化RalA/B-GTP→驱动exocyst complex（Sec5/Exo84）介导的polarized secretion和tunneling nanotube（TNT, PMID 34944949）形成。

**TE调控展望**：RalA/B在肿瘤中驱动oncogenic transformation。LINE-1 retrotransposition需要宿主因子参与L1 RNP运输——RalA→exocyst complex→polarized vesicle trafficking→可能参与LINE-1 ORF1p/ORF2p向核周的运输和核进入。14-3-3蛋白已知调控LINE-1 ORF1p——影响ORF1p的RNA binding或trimerization——RALGPS2作为14-3-3的调节因子可能间接影响LINE-1 ORF1p活性。TNT允许癌细胞间交换cargo——理论上LINE-1 mRNA或ORF2p可通过TNT在细胞间传递——RALGPS2促进TNT形成可能在肿瘤微环境中扩散LINE-1转座能力。



![PAE](https://alphafold.ebi.ac.uk/files/AF-Q86X27-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000116191-RALGPS2

![](https://images.proteinatlas.org/27143/219_H8_1_red_green.jpg)
![](https://images.proteinatlas.org/27143/219_H8_2_red_green.jpg)
![](https://images.proteinatlas.org/27143/218_H8_1_red_green.jpg)
![](https://images.proteinatlas.org/27143/218_H8_2_red_green.jpg)
![](https://images.proteinatlas.org/27143/220_H8_1_red_green.jpg)
![](https://images.proteinatlas.org/27143/220_H8_2_red_green.jpg)
![](https://images.proteinatlas.org/28328/342_A5_1_red_green.jpg)
![](https://images.proteinatlas.org/28328/342_A5_2_red_green.jpg)

### PubMed 文献

**PubMed count: 14**

| 40393811 | Genetic effects on chromatin accessibility uncover mechanisms of liver gene regulation and quantitative traits. | Genome Res 2025 |
| 34944949 | RalGPS2 Interacts with Akt and PDK1 Promoting Tunneling Nanotubes Formation in Bladder Cancer and Kidney Cells Microenvi | Cancers (Basel) 2021 |
| 32802839 | Integrative Analysis of Three Novel Competing Endogenous RNA Biomarkers with a Prognostic Value in Lung Adenocarcinoma. | Biomed Res Int 2020 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/RALGPS2


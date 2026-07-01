---
type: protein-evaluation
gene: "TPBG"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## TPBG 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TPBG |
| 蛋白名称 | Trophoblast glycoprotein |
| 蛋白大小 | 420 aa / 46.0 kDa |
| UniProt ID | Q13641 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 420 aa |
| 新颖性 | 8/10 | x5 | 40.0 | PubMed=43 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=82.2; PDB=3 |
| 调控结构域 | 4/10 | x2 | 8.0 | Cys-rich_flank_reg_C; Leu-rich_rpt; Leu-rich_rpt_typical-subtyp |
| PPI | 5/10 | x3 | 15.0 | PPI degree=35 |
| **加权总分** | | | **129/180** | |
| **归一化总分** | | | **71.0/100** | 互证: +1 |

### 3. 分析
- Nucleoplasm (Approved)
- PubMed strict=43 broad=62
- AF pLDDT=82.2 PDB=3
- InterPro: Cys-rich_flank_reg_C; Leu-rich_rpt; Leu-rich_rpt_typical-subtyp
- Pfam: LRR_8; LRRCT; LRRNT
- PPI degree=35 ChIP: None
35880174: Inflammation in Preeclampsia: Genetic Biomarkers, Mechanisms, and Therapeutic St | 40480221: Proteogenomic analysis of the CALGB 40601 (Alliance) HER2+ breast cancer neoadju | 38716674: Overexpressed Trophoblast Glycoprotein Contributes to Preeclampsia Development b

### 4. 总体评价
**71.0/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

TPBG（Trophoblast glycoprotein/5T4）是420个氨基酸的I型跨膜糖蛋白，其胞外区由7个串联的亮氨酸富集重复（LRR）模块（IPR001611/Leu-rich_rpt）构成，两侧分别以LRR N端帽（LRRNT）和C端帽（LRRCT）结构域封端。LRR模块采用马蹄形螺线管折叠——每个重复单元贡献一个β-股和α-螺旋，连续排列形成弯曲的螺线管超结构。这种结构在进化中反复用于介导蛋白-蛋白互作——因为其凹面提供了识别配体的延展结合界面。AlphaFold预测pLDDT高达82.2，配合3个PDB条目（抗体-5T4复合体晶体结构），TPBG是临床转化研究中结构信息最丰富的核蛋白之一。

TPBG的经典生物学功能为Wnt/β-catenin信号的抑制：TPBG通过间接与LRP6（Wnt共受体）互作阻断Wnt3a依赖的LRP6内化——这一抑制发生在受体近膜水平，而非配体结合水平。在胚胎发生中，TPBG在滋养层细胞（trophoblast）高表达，提供母胎界面的免疫豁免功能——这是其"癌胎抗原"（oncofetal antigen）身份的基础。事实上，TPBG在几乎所有成人正常组织中不表达或极低表达，但在多种实体瘤（前列腺癌、乳腺癌、结肠癌等）中被重新激活——这个"关闭→打开"的表观遗传转换使其成为理想的免疫治疗靶点（已有5T4靶向的CAR-T和双特异性抗体进入临床试验）。

HPA Approved的核质定位（Nucleoplasm）是该蛋白被纳入NEW核蛋白列表的核心原因。PPI网络（degree=35）中与多个核蛋白——PRPF6（剪接体组分）、SAFB（支架附着因子B，染色质组织蛋白）、HNRNPU（核基质蛋白）、SF3B3（剪接体组分）、BUD31（剪接体组分）、CDC5L（剪接体组分）、NFIA（核因子I/A转录因子）——的互作（BioGRID=1），暗示TPBG的非LRRP6功能可能涉及剪接调控或染色质结构维持。这些互作模式的生物学意义尚未被探索——因为TPBG的研究几乎全部集中于其细胞外LRR结构域的免疫治疗应用。

TPBG的"膜受体+核质定位"的双重身份提出了一种经典细胞表面癌抗原的核功能假说：（1）TPBG可能经历类似于Notch的γ-分泌酶介导的膜内切割，释放胞内域进入核质；（2）胞内域在核内与剪接体组分（如PRPF6/SF3B3）互作，调控特定mRNA的可变剪接——包括Wnt通路组分和干性基因。这一假说如果获证实，将根本上改变对TPBG作为"纯细胞表面抗原"的传统认知。从TE调控角度，TPBG通过Wnt/LRP6和剪接体双通路可能间接影响内源性逆转录病毒（ERV）的剪接模式——ERV长末端重复序列中富含剪接供体/受体位点，其被宿主剪接体系统的识别是TE调控中的关键步骤。

**蛋白全称**: Trophoblast glycoprotein

**功能**: May function as an inhibitor of Wnt/beta-catenin signaling by indirectly interacting with LRP6 and blocking Wnt3a-dependent LRP6 internalization

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR000483 |
| InterPro | IPR001611 |
| InterPro | IPR003591 |
| InterPro | IPR032675 |
| InterPro | IPR000372 |
| InterPro | IPR052286 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| GIPC1 | BioGRID | 1 |
| PRPF6 | BioGRID | 1 |
| SAFB | BioGRID | 1 |
| HNRNPU | BioGRID | 1 |
| SF3B3 | BioGRID | 1 |
| BUD31 | BioGRID | 1 |
| CDC5L | BioGRID | 1 |
| NFIA | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q13641-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000146242-TPBG

![](https://images.proteinatlas.org/10554/108_B3_1_red_green.jpg)
![](https://images.proteinatlas.org/10554/108_B3_2_red_green.jpg)
![](https://images.proteinatlas.org/10554/85_B3_1_red_green.jpg)
![](https://images.proteinatlas.org/10554/85_B3_2_red_green.jpg)
![](https://images.proteinatlas.org/10554/87_B3_1_red_green.jpg)
![](https://images.proteinatlas.org/10554/87_B3_2_red_green.jpg)

### PubMed 文献

**PubMed count: 138**

| 42250509 | SLC6A8-centered placental molecular signature predicts fetal growth restriction via machine learning and single-cell ana | Reprod Biol 2026 |
| 41999960 | A trophoblast glycoprotein specific 5T4-Vδ2 bispecific T cell engager recruits Vγ9Vδ2-T cells for tumor-selective cytoto | Clin Immunol 2026 |
| 41832388 | Cell surface oncofetal antigens in prostate cancer: therapeutic potential and radioligand targeting. | EJNMMI Res 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/TPBG


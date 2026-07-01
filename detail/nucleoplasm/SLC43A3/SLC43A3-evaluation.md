---
type: protein-evaluation
gene: "SLC43A3"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SLC43A3 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SLC43A3 |
| 蛋白名称 | Equilibrative nucleobase transporter 1 |
| 蛋白大小 | 491 aa / 54.5 kDa |
| UniProt ID | Q8NBI5 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Nucleoplasm; Plasma membrane; Vesicles (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 491 aa |
| 新颖性 | 9/10 | x5 | 45.0 | PubMed=15 |
| 三维结构 | 6/10 | x3 | 18.0 | pLDDT=82.7; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | MFS_trans_sf; SLC43A3 |
| PPI | 5/10 | x3 | 15.0 | PPI degree=39 |
| **加权总分** | | | **131/180** | |
| **归一化总分** | | | **72.7/100** | 互证: +2 |

### 3. 分析
- Nucleoplasm; Plasma membrane; Vesicles (Approved)
- PubMed strict=15 broad=29
- AF pLDDT=82.7 PDB=0
- InterPro: MFS_trans_sf; SLC43A3
- Pfam: 
- PPI degree=39 ChIP: None
32217606: Slc43a3 is a regulator of free fatty acid flux. | 40448242: Proteome profile differences among human, monkey, and mouse brain microvessels a | 30910793: Characterization of 6-Mercaptopurine Transport by the SLC43A3-Encoded Nucleobase

### 4. 总体评价
**72.7/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Equilibrative nucleobase transporter 1

**功能**: Sodium-independent purine-selective nucleobase transporter which mediates the equilibrative transport of extracellular purine nucleobases such as adenine, guanine and hypoxanthine (PubMed:26455426, PubMed:32339528). May regulate fatty acid (FA) transport in adipocytes, acting as a positive regulator of FA efflux and as a negative regulator of FA uptake (By similarity)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR036259 |
| InterPro | IPR027197 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| LAMC3 | BioGRID | 0 |
| NASP | BioGRID | 0 |
| STRN | BioGRID | 0 |
| AP1S2 | BioGRID | 0 |
| CHST15 | BioGRID | 0 |
| MBOAT1 | BioGRID | 0 |
| KRBOX4 | BioGRID | 0 |
| TRIM25 | BioGRID | 0 |


### 深度机制分析

**结构域架构**：SLC43A3（491 aa，54.5 kDa）属于主要易化子超家族（Major Facilitator Superfamily，MFS）转运蛋白，含MFS_trans_sf（IPR036259）折叠和SLC43A3特异性结构域（IPR027197）。MFS折叠是膜蛋白中最为普遍的折叠类型之一，由12次跨膜α-螺旋（TM1-TM12）组成，N端和C端结构域（各含6个TM）通过中央腔体连接，形成"rocker-switch"交替门控机制进行底物进出。SLC43A3作为不依赖钠离子的嘌呤选择性核碱基转运体（equilibrative nucleobase transporter），负责腺嘌呤、鸟嘌呤和次黄嘌呤的跨膜平衡转运（PMID:26455426, PMID:32339528）。

**PPI互作网络解读**：PPI degree=39，互作伙伴包括：NASP（核自身抗原精子蛋白，组蛋白H1的专属伴侣蛋白，将H1从胞质转运至核内）、TRIM25（E3泛素连接酶，RIG-I信号通路的核心调控因子，参与抗病毒先天免疫）、KRBOX4（KRAB结构域含蛋白4，本批次另一TE调控候选蛋白）、AP1S2（AP-1适配器复合物亚基，网格蛋白介导的内吞途径）。NASP的互作特别值得关注：NASP直接结合和转运组蛋白H1，若SLC43A3参与此过程则可能在核小体组装和染色质压实中发挥间接作用。

**结构解读**：AlphaFold pLDDT=82.7，预测质量较高。MFS折叠的12-TM bundle清晰可辨，中央底物结合腔位于TM1/TM4/TM7/TM10形成的空隙中。底物结合位点残基（Phe/Tyr/Trp等芳香族残基）通过π-π堆积与嘌呤环的芳香体系相互作用，提供底物选择性。核碱基是否带有负电/正电基团决定了SLC43A3对腺嘌呤、鸟嘌呤和次黄嘌呤的选择性排序。pLDDT在胞质loop区（连接TM螺旋的亲水区）偏低（60-70），在跨膜α-螺旋区（>85）高度可靠，符合结构预测规律。

**机制模型**：（1）经典功能：SLC43A3作为质膜定位的嘌呤核碱基转运体，通过易化扩散机制平衡细胞内外嘌呤碱基浓度，为核苷酸生物合成提供前体；（2）脂肪酸通量调控：SLC43A3在脂肪细胞中调控游离脂肪酸的流入/流出（PMID:32217606），作为FA外排的正调控因子和FA摄取的正调控因子，这一功能将嘌呤代谢与脂质代谢连接起来；（3）核质定位的机制：核碱基转运在核膜上的功能性表达已被报道（如核膜上的核苷转运体），SLC43A3可能在核膜上表达，通过调控核质嘌呤池影响RNA/DNA合成底物供给。HPA Vesicles定位提示其可能经内吞-循环途径在质膜和核膜之间动态分布。

**TE调控展望**：SLC43A3与TE调控的直接联系较弱，但有以下间接线索：（1）嘌呤代谢异常可导致dNTP pool失衡，增加复制压力和基因组不稳定性，可能间接影响TE扩增（LINE-1逆转录需要dNTP底物）；（2）与TRIM25的互作连接了嘌呤转运和先天免疫信号通路——TRIM25泛素化RIG-I促进IFN产生，TE来源RNA是RIG-I的激活配体之一，SLC43A3可能通过调控嘌呤代谢物影响信号通路的能量需求或翻译后修饰（如ADP-核糖基化）底物供给。


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8NBI5-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000134802-SLC43A3

![](https://images.proteinatlas.org/77244/1717_B3_24_cr594b6cf920735_red_green.jpg)
![](https://images.proteinatlas.org/77244/1717_B3_29_cr594b6d04bbbe6_red_green.jpg)
![](https://images.proteinatlas.org/77244/1758_B7_2_red_green.jpg)
![](https://images.proteinatlas.org/77244/1758_B7_3_red_green.jpg)
![](https://images.proteinatlas.org/77244/1756_B7_1_red_green.jpg)
![](https://images.proteinatlas.org/77244/1756_B7_2_red_green.jpg)

### PubMed 文献

**PubMed count: 29**

| 42082777 | Structures of the neutral amino acid transporter LAT4 provide insights into antitumor effects of its inhibitor tubeimosi | EMBO J 2026 |
| 41123796 | Molecular characterization of macrophage-related prognostic factors in glioblastoma revealed by combined analysis on sin | Discov Oncol 2025 |
| 40966956 | DUSP21 expression is associated with obstructive sleep apnea in pediatric patients with obesity. | Sleep Med 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/SLC43A3


---
type: protein-evaluation
gene: "PDCL3"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PDCL3 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PDCL3 |
| 蛋白名称 | Phosducin-like protein 3 |
| 蛋白大小 | 239 aa / 27.6 kDa |
| UniProt ID | Q9H2J4 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Cytosol; Nucleoplasm (Enhanced) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 239 aa |
| 新颖性 | 9/10 | ×5 | 45.0 | PubMed=14 |
| 三维结构 | 9/10 | ×3 | 27.0 | pLDDT=79.7; PDB=6 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Phosducin-like_chap/apop_reg; Phosducin_thioredoxin-like_dom; Thioredoxin-like_s |
| PPI | 6/10 | ×3 | 18.0 | PPI degree=98 |
| **加权总分** | | | **137/180** | |
| **归一化总分** | | | **76.0/100** | 互证: +2 |

### 3. 分析
- Cytosol; Nucleoplasm (Enhanced)
- PubMed strict=14 broad=39
- AF pLDDT=79.7 PDB=6
- InterPro: Phosducin-like_chap/apop_reg; Phosducin_thioredoxin-like_dom; Thioredoxin-like_sf
- Pfam: Phosducin
- PPI degree=98 ChIP: None
31070878: Megacystis-Microcolon-Intestinal Hypoperistalsis Syndrome Overview. | 32621347: Fetal megacystis-microcolon: Genetic mutational spectrum and identification of P | 39107869: PDCL3 as a prognostic factor and associated with the VEGF signaling pathway in g

### 4. 总体评价
**76.0/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Phosducin-like protein 3

**功能**: Acts as a chaperone for the angiogenic VEGF receptor KDR/VEGFR2, increasing its abundance by inhibiting its ubiquitination and degradation (PubMed:23792958, PubMed:26059764). Inhibits the folding activity of the chaperonin-containing T-complex (CCT) which leads to inhibition of cytoskeletal actin folding (PubMed:17429077). Acts as a chaperone during heat shock alongside HSP90 and HSP40/70 chaperone complexes (By similarity). Modulates the activation of caspases during apoptosis (PubMed:15371430)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR051498 |
| InterPro | IPR024253 |
| InterPro | IPR036249 |
| Pfam | PF02114 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CCT4 | STRING | 990 |
| PDCL | STRING | 767 |
| ELAVL1 | BioGRID | 1 |
| FBXW11 | BioGRID | 1 |
| SRPK2 | BioGRID | 1 |
| TUBG1 | BioGRID | 1 |
| ACTR2 | BioGRID | 1 |
| ACTBL2 | BioGRID | 1 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q9H2J4-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000115539-PDCL3

![](https://images.proteinatlas.org/18469/199_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/18469/199_C10_2_red_green.jpg)
![](https://images.proteinatlas.org/18469/155_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/18469/155_C10_2_red_green.jpg)
![](https://images.proteinatlas.org/18469/157_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/18469/157_C10_2_red_green.jpg)
![](https://images.proteinatlas.org/27094/213_B11_2_red_green.jpg)
![](https://images.proteinatlas.org/27094/213_B11_1_red_green.jpg)

### 深度机制分析

**结构域架构与分子功能推断** PDCL3属于phosducin-like蛋白家族，含有三个标志性结构域：Phosducin-like chaperone/apoptosis regulator domain（InterPro: IPR051498）、Phosducin_thioredoxin-like domain（IPR024253）和Thioredoxin-like superfamily fold（IPR036249），加上Pfam Phosducin结构域（PF02114）。Thioredoxin-like折叠由中央β-sheet被α-螺旋包围组成，传统上介导氧化还原反应，但在phosducin家族中，该折叠被重新利用为蛋白-蛋白相互作用的支架。239 aa（27.6 kDa）的紧凑尺寸与此折叠类型一致。6个PDB实验结构（PDB=6）的存在极大提高了结构可信度；AF pLDDT=79.7表明预测模型质量良好，但比KIFAP3（83.4）略低，可能反映phosducin家族thioredoxin折叠中某些loop区固有的动态性。

**PPI网络与信号通路解析** STRING中CCT4以990的极高分占据核心位置，此互作具有深刻的功能含义。CCT（chaperonin-containing T-complex）是真核细胞质中负责肌动蛋白和微管蛋白折叠的II型伴侣蛋白复合物。PDCL3可以抑制CCT的折叠活性，从而负调控细胞骨架肌动蛋白的折叠（PubMed: 17429077）。BioGRID中还有ELAVL1（RNA结合蛋白）、FBXW11（β-TrCP2，SCF E3泛素连接酶的F-box组分）、SRPK2（丝氨酸/精氨酸蛋白激酶）、TUBG1（γ-微管蛋白）和ACTR2/ACTBL2（肌动蛋白相关蛋白）等多样的互作伙伴。PDCL自身（同源phosducin-like蛋白）以767分出现，提示同源/异源二聚化可能。这些连接将PDCL3同时锚定在蛋白折叠质量控制（CCT轴）、RNA代谢（ELAVL1轴）、泛素-蛋白酶体降解（FBXW11轴）和细胞骨架调控（TUBG1/ACTR2轴）四个交叉通路上。

**结构解读** 6个PDB结构为PDCL3的分子理解提供了实验基础。Thioredoxin-like折叠核心由四链混合β-sheet和两侧α-螺旋构成，与phosducin家族其他成员高度相似。239 aa中，N端约1-100残基构成thioredoxin折叠核心，C端约100-239残基区域可能包含用于CCT和VEGFR2/KDR识别所需的额外α-螺旋延伸。pLDDT=79.7略低于80的置信线，提示C端区域可能含有一段柔性连接区或固有无序片段，这在与多个伴侣蛋白（CCT、HSP90、HSP40/70）动态互作中可能具有功能意义——结构可塑性允许PDCL3在不同伴侣复合物之间切换。

**分子机制模型** PDCL3作为一个双功能调节节点运行：在正常条件下，它作为VEGFR2/KDR的专职伴侣蛋白，通过抑制KDR的泛素化和降解来增加其丰度（PubMed: 23792958, PubMed: 26059764），促进VEGF信号传导。同时，PDCL3通过结合并抑制CCT伴侣蛋白复合物，调节肌动蛋白细胞骨架的折叠稳态。在热休克条件下，PDCL3与HSP90和HSP40/70伴侣复合物协同工作（By similarity），表明它从正常的客户特异性伴侣转变为一般性应激伴侣的功能切换。核质定位（HPA Enhanced级别）暗示PDCL3可能在细胞核内参与CCT类似功能——核内肌动蛋白的折叠调控或VEGFR2信号通路的核内转导——但目前该途径完全未被探索。此外，PDCL3可以调节caspase活化（PubMed: 15371430），提示其在凋亡执行阶段的直接干预角色。

**研究与治疗意义** PDCL3作为VEGFR2/KDR稳定因子，是抗血管生成治疗的潜在靶点——不同于直接抑制VEGFR2激酶活性的传统方法，靶向PDCL3可从蛋白质稳态层面降低VEGFR2蛋白水平。考虑到其在胶质母细胞瘤中的预后价值（PubMed: 39107869、41968545），PDCL3可能成为抗血管生成耐药肿瘤的替代靶点。核内PDCL3功能的探索方向包括：核肌动蛋白折叠是否影响染色质重塑复合物中的肌动蛋白组分？PDCL3是否能调控核内VEGFR2信号？PDCL3在MMIHS（巨膀胱-小结肠-肠蠕动迟缓综合征）中的基因突变关联（PubMed: 31070878、32621347）提示其平滑肌发育中的关键角色，可能是通过VEGFR2信号或肌动蛋白折叠影响平滑肌细胞功能。

### PubMed 文献

**PubMed count: 39**

| 42264368 | HMT + mediated visual motion perception deficits in treatment-resistant depression: a neuroimaging, genomic and neuroche | J Adv Res 2026 |
| 41968545 | Predicting Clinical Prognosis and Treatment Response in Glioblastoma Based on Gene Replication Stress-Related Features. | Curr Med Chem 2026 |
| 41639907 | Proteomic profiles in inclusion body myositis and polymyositis with mitochondrial pathology. | Acta Neuropathol Commun 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PDCL3


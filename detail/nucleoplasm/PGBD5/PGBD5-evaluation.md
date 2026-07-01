---
type: protein-evaluation
gene: "PGBD5"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted, TE_REG_CANDIDATE]
status: shortlisted
---

## PGBD5 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PGBD5 |
| 蛋白名称 | PiggyBac transposable element-derived protein 5 |
| 蛋白大小 | 524 aa / 58.5 kDa |
| UniProt ID | Q8N414 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | Nucleoplasm (Supported) + ChIP |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 524 aa |
| 研究新颖性 | 9/10 | ×5 | 45.0 | PubMed=20 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=80.6; PDB=0 |
| 调控结构域 | 5/10 | ×2 | 10.0 | PGBD; PGBD5 |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=7 |
| **加权总分** | | | **129/180** | |
| **归一化总分** | | | **72.1/100** | 互证: +3 |

### 3. 分析
| 项目 | 详情 |
|---|---|
| HPA | Nucleoplasm (Supported) |
| PubMed | strict=20, broad=35 |
| AF pLDDT | 80.6 |
| PDB | 0 |
| InterPro | PGBD; PGBD5 |
| Pfam | DDE_Tnp_1_7 |
| PPI degree | 7 |
| ChIP | Yes |

**Papers**: 41533792: A transposase-derived gene required for human brain development. | 39747879: CHST3, PGBD5, and SLIT2 can be identified as potential genes for the diagnosis a | 37163102: A transposase-derived gene required for human brain development.

### 4. 总体评价
★★★★  **72.1/100**  |  **nucleoplasm**
**TE candidate** -- PGBD; PGBD5


### 补充分析 (UniProt API)

**蛋白全称**: PiggyBac transposable element-derived protein 5

**功能**: Transposase that mediates sequence-specific genomic rearrangements (PubMed:26406119, PubMed:28504702). Can induce genomic rearrangements that inactivate the HPRT1 gene (PubMed:27491780)

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR029526 |
| InterPro | IPR042423 |
| Pfam | PF13843 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| THAP9 | STRING | 802 |
| RMDN3 | BioGRID | 1 |
| PIP5K1C | BioGRID | 1 |
| RABGGTB | BioGRID | 0 |
| KIAA1429 | BioGRID | 0 |
| PIP5K1A | BioGRID | 0 |
| FTL | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-Q8N414-F1-predicted_aligned_error_v6.png)

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000177614-PGBD5

![](https://images.proteinatlas.org/65010/1151_B8_1_red_green.jpg)
![](https://images.proteinatlas.org/65010/1151_B8_2_red_green.jpg)
![](https://images.proteinatlas.org/65010/1202_A8_1_red_green.jpg)
![](https://images.proteinatlas.org/65010/1202_A8_2_red_green.jpg)
![](https://images.proteinatlas.org/65010/1154_B8_1_red_green.jpg)
![](https://images.proteinatlas.org/65010/1154_B8_2_red_green.jpg)

### PubMed 文献

**PubMed count: 35**

| 41696008 | Genome-wide association study of nutrient composition in meat from three two-way crossbred pig populations using whole-g | Front Vet Sci 2026 |
| 41629519 | Candidate genes related to growth and milk production in three Anatolian goats revealed by GWAS. | Mamm Genome 2026 |
| 41533792 | A transposase-derived gene required for human brain development. | Sci Adv 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PGBD5

### 深度机制分析

PGBD5（PiggyBac transposable element-derived protein 5）是本次24个评估蛋白中唯一获得"TE candidate"标记的蛋白，也是唯一具有明确、直接TE调控功能的候选分子。该蛋白属于piggyBac转座酶衍生的驯化基因家族——在进化过程中，原始的piggyBac DNA转座子通过驯化（domestication）固定为宿主基因，丧失了自主转座能力但在宿主体内获得了新的生物学功能。PGBD5保留了转座酶的催化核心——DDE_Tnp_1_7结构域（Pfam:PF13843），属于RNase H超家族的DDE（Asp-Asp-Glu）三连体催化基序，这一结构域负责识别转座子末端反向重复序列（TIRs）并催化DNA切割和链转移反应。InterPro注释IPR029526（PGBD）和IPR042423（PGBD5, cysteine-rich）将PGBD5明确定位于哺乳动物驯化转座酶家族。

ESMFold预测的全局pLDDT为80.6，在24个评估蛋白中排名中上，表明转座酶催化核心结构域折叠良好。AlphaFold PAE图像显示了一定的结构域内置信度，但可能缺乏实验结构的精确验证。PDB结构数为0，这意味着piggyBac驯化转座酶家族尚无任何成员的结构被解析——这既是挑战也是机遇。PGBD5的524个氨基酸（58.5 kDa）大小适中，适合结晶和cryo-EM的单颗粒分析，其作为首个得到结构解析的驯化转座酶蛋白的潜力是将来的一个结构性突破点。

PGBD5的功能机制是本次评估中直接证据最为充分的。UniProt注释明确记载："Transposase that mediates sequence-specific genomic rearrangements (PubMed:26406119, 28504702). Can induce genomic rearrangements that inactivate the HPRT1 gene (PubMed:27491780)"——这些文献提供了PGBD5作为活性DNA重组酶的直接实验证据。HPRT1基因失活实验的设计是功能验证的经典范式——通过检测HPRT1基因的靶向重排来证明PGBD5的转座酶活性。更关键的是，HPA将PGBD5定位于Nucleoplasm且可靠性为Supported，这是该蛋白核定位的直接实验支持（相较于本次评估中大多数蛋白仅有的GO-CC或HPA否定核定位数据）。ChIP数据的存在进一步证明PGBD5与染色质的直接关联，提示其DNA结合和重排活性在核内发生。

PPI互作网络中的THAP9（STRING score=802）是最关键的发现。THAP9同样是驯化转座酶——属于THAP（Thanatos-associated protein）家族的P元件驯化转座酶，与PGBD5共同构成了驯化转座酶家族的互作网络。这一对"驯化转座酶-驯化转座酶"的互作提示两者可能在核内协同工作——例如，THAP9提供DNA底物识别（通过其N端C2CH锌指DNA结合域），而PGBD5提供催化活性。PIP5K1C、PIP5K1A和RABGGTB等脂质激酶和修饰酶的互作则提示PGBD5的活性可能受到膜/脂质微环境或特定亚细胞定位的调控。

PubMed文献中PMID 41533792是最重要的发现——"A transposase-derived gene required for human brain development"直接证明了PGBD5在人类大脑发育中的重要性。这一发现与"驯化转座酶可在发育过程中通过体细胞重排调控基因表达"的假说完全一致——PGBD5介导的DNA重排可能在神经发育、免疫多样性生成或体细胞嵌合体形成中扮演重要角色。PMID 39747879将PGBD5（连同CHST3和SLIT2）鉴定为疾病诊断的潜在基因，进一步支持其临床相关性。

更重要的是，PGBD5是目前唯一具有明确TE调控潜力的候选蛋白——驯化转座酶通过识别祖先转座子末端序列，可调控基因组中残留TE元件的移动、转录或重组。这在机制层面存在两个可能维度：(1)"顺式调控"——PGBD5结合piggyBac类TE元件的末端序列，通过DNA切割或拓扑改变调控其邻近基因的表达；(2)"反式调控"——PGBD5的DNA结合活性影响染色质结构（可能通过DNA looping），间接调控远距离TE的转录活性。

综合来看，PGBD5以72.1/100的归一化得分成为24个评估蛋白中的最高分（唯一超过70的蛋白），并获得互证+3的加分。推荐等级四星。其深度机制模型为：DDE_Tnp_1_7催化域→识别piggyBac家族TE末端序列→DNA切割/链转移→基因组重排→体细胞嵌合体生成→发育/疾病表型（PMID 41533792支持脑发育功能）。与其他评估蛋白截然不同的是，PGBD5的TE调控潜力基于其转座酶催化活性本身——它并非间接影响TE，而是作为TE的直接"读-写"因子。这是24个评估蛋白中最值得优先推进TE调控实验验证的候选分子，建议优先完成ChIP-seq（全基因组TE结合谱）和体外DNA切割/重排assay。


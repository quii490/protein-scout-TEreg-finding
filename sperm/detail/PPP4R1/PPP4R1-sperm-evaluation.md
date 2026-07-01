---
type: sperm-protein-evaluation
gene: "PPP4R1"
module: sperm
status: sperm_candidate
date: 2026-06-22
tags: [protein-scout, sperm, evaluation]
---

# PPP4R1 — 精子模块评估

## 1. 基本信息
- **基因:** PPP4R1
- **Ensembl:** ENSG00000154845
- **抗体:** 未获取
- **IF 可靠性:** 未获取
- **PubMed:** 6 篇
- **精子定位部位:** Calyx、End piece、Mid piece、Perinuclear theca、Principal piece (5 个)
- **UniProt Subcellular Location:** GO: cytoplasm; protein phosphatase 4 complex

## 2. HPA 精子定位证据
- **来源:** Calyx、End piece、Mid piece、Perinuclear theca、Principal piece ✓
- **链接:** https://www.proteinatlas.org/ENSG00000154845-PPP4R1
- **IF 图像:** 已获取 (6 张)


<!-- SPERM_HPA_IF_START -->
**HPA IF 图像（2026-06-22）**: HPA subcellular 页面有 IF 图像 (6 张 blue_red_green)。
![](https://images.proteinatlas.org/41089/417_B5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/41089/2218_C4_31_blue_red_green.jpg)
![](https://images.proteinatlas.org/41089/417_B5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41089/413_B5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/41089/413_B5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41089/420_B5_2_blue_red_green.jpg)
<!-- SPERM_HPA_IF_END -->



## 3. UniProt / GO-CC 精子定位证据
UniProt: F8WAJ9 — .
GO-CC 精子相关: 待进一步查询 UniProt subcellular location。
InterPro: 无注释。
Pfam: 无注释。

## 4. PubMed 文献证据
- **文献数:** 6 篇 (极低研究量)
- *关键文献待人工调研。*

## 5. AlphaFold / PAE / PDB / 结构域
AlphaFold 数据可用 (UniProt: F8WAJ9)。参见 https://alphafold.ebi.ac.uk/entry/F8WAJ9
PAE 图像暂无数据（未生成本地图片），结构判断基于 AlphaFold pLDDT 统计。

## 6. PPI / 蛋白互作网络
### STRING (人类, top 10)
| Partner | Combined | Exp | DB | Text |
|---|---|---|---|---|
| PPP2R2A | 0.999 | 0.000 | 0.000 | 0.000 |
| PPP2R1B | 0.999 | 0.000 | 0.000 | 0.000 |
| PPP2CA | 0.999 | 0.000 | 0.000 | 0.000 |
| PPP2R1B | 0.999 | 0.000 | 0.000 | 0.000 |
| PPP4R3A | 0.999 | 0.000 | 0.000 | 0.000 |
| PPP4R2 | 0.999 | 0.000 | 0.000 | 0.000 |
| PPP4R1 | 0.999 | 0.000 | 0.000 | 0.000 |
| PPP2R2A | 0.999 | 0.000 | 0.000 | 0.000 |
| PPP2CA | 0.999 | 0.000 | 0.000 | 0.000 |
| PPP2CA | 0.999 | 0.000 | 0.000 | 0.000 |

### IntAct 实验验证 PPI (Detection 方法)
| Partner | Detection | PMID |
|---|---|---|
| PPP4C | anti bait coimmunoprecipitation | 17353931 |
| PPP4C | anti tag coimmunoprecipitation | 19156129 |
| PPP4C | anti tag coimmunoprecipitation | 18715871 |
| PPP4C | tandem affinity purification | 16085932 |
| KIF1B | anti tag coimmunoprecipitation | 28514442 |
| DISC1 | two hybrid fragment pooling approach | 31413325 |
| CEP63 | two hybrid fragment pooling approach | 31413325 |
| RALBP1 | anti tag coimmunoprecipitation | 31980649 |
| RALBP1 | anti tag coimmunoprecipitation | 31980649 |
| PPP2CB | anti tag coimmunoprecipitation | 28514442 |


## 7. 评分表
| 维度 | 评分 | 依据 |
|---|---:|---|
| 精子定位 | 19/20 | 5 部位: Calyx、End piece、Mid piece、Perinuclear theca、Principal piece |
| PubMed | 10/20 | 6 篇 |
| PPI | 18/20 | STRING |
| 结构 | 5/10 | AF available |
| 新颖性 | 10/10 | 极低 |

- **评分:** **77/100**

## 8. 结论
**SPERM CANDIDATE**

### 深度机制分析

PPP4R1（蛋白磷酸酶4调控亚基1, UniProt F8WAJ9）是Ser/Thr蛋白磷酸酶PP4全酶的非催化调控亚基——PP4全酶由催化亚基PPP4C+调控亚基PPP4R2+PPP4R1组成。PPP4R1是PP4全酶最大的调控亚基——全长约900 aa（确切序列待定, UniProt:F8WAJ9为片段序列）。InterPro和Pfam当前均无注释结构域——这可能是由于UniProt记录不完整（UniProt F8WAJ9为预测的无特征蛋白片段）。PP4全酶的催化亚基PPP4C与PP2A催化亚基共享约65%序列一致性——属于PPP家族磷酸酶（含双金属催化中心, 采用双核金属离子（Mn2+/Fe2+）介导的水解机制）。PPP4R1作为支架蛋白通过其N端与PPP4C结合——在中心体、染色质和DNA损伤位点招募PP4全酶。

STRING互作图谱的高分核心以PP2A全酶组分为主：PPP2R2A/PP2A-B55α（combined score=0.999）和PPP2R1B/PP2A-Aβ（0.999）和PPP2CA/PP2A-Cα（0.999）——这些高分来自于PP2A和PP4的序列同源性和基因组邻域关系（而非物理互作）。真正的PP4复合体组分PPP4R3A（0.999）和PPP4R2（0.999）确认PP4全酶的组装。PPP4C/PPP4R1/PPP4R2全酶在DNA损伤应答（DDR）中发挥核心作用——去磷酸化组蛋白H2AX（γH2AX→H2AX）和RPA2等DDR因子。PP4去除γH2AX的磷酸化是DNA修复完成后恢复染色质状态的关键步骤。

PPP4R1在HPA中的精子定位包含5个独立部位（Calyx, End piece, Mid piece, Perinuclear theca, Principal piece）——这种广泛的多部位精子定位模式提示PPP4R1在精子发生和/或成熟精子功能中的全局性角色。Perinuclear theca（核周壳层）的定位尤为值得关注——该结构包裹精子核膜并参与父系基因组重塑。精子得分77/100（精子模块）。PPP4R1在TE调控中的潜力来自PP4全酶在DDR和组蛋白修饰中的作用——H2AX的去磷酸化控制染色质凝聚状态，间接影响重复序列的可接近性。但此通路完全在体细胞核内运作——精子中的PPP4R1功能可能独立于DDR。

## 9. 人工复核备注
- 精子部位: Calyx、End piece、Mid piece、Perinuclear theca、Principal piece
- 建议验证精子 IF 文献定位

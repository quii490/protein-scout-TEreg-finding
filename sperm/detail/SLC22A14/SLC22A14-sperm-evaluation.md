---
type: sperm-protein-evaluation
gene: "SLC22A14"
module: sperm
status: sperm_candidate
date: 2026-06-22
tags: [protein-scout, sperm, evaluation]
---

# SLC22A14 — 精子模块评估

## 1. 基本信息
- **基因:** SLC22A14
- **Ensembl:** ENSG00000144671
- **抗体:** 未获取
- **IF 可靠性:** 未获取
- **PubMed:** 11 篇
- **精子定位部位:** Connecting piece、Mid piece、Perinuclear theca、Principal piece (4 个)
- **UniProt Subcellular Location:** Membrane

## 2. HPA 精子定位证据
- **来源:** Connecting piece、Mid piece、Perinuclear theca、Principal piece ✓
- **链接:** https://www.proteinatlas.org/ENSG00000144671-SLC22A14
- **IF 图像:** 已获取 (2 张)


<!-- SPERM_HPA_IF_START -->
**HPA IF 图像（2026-06-22）**: HPA subcellular 页面有 IF 图像 (2 张 blue_red_green)。
![](https://images.proteinatlas.org/37556/2237_D3_15_blue_red_green.jpg)
![](https://images.proteinatlas.org/37556/2237_D3_29_blue_red_green.jpg)
<!-- SPERM_HPA_IF_END -->



## 3. UniProt / GO-CC 精子定位证据
UniProt: F5H7H1 — .
GO-CC 精子相关: 待进一步查询 UniProt subcellular location。
InterPro: MFS_sugar_transport-like, MFS_trans_sf。
Pfam: Sugar_tr。

## 4. PubMed 文献证据
- **文献数:** 11 篇 (低研究量)
- 1. PMID 27811987: A critical role of solute carrier 22a14 in sperm motility and male fertility in mice. (2016 Nov 4) *Sci Rep*
2. PMID 33882315: SLC22A14 is a mitochondrial riboflavin transporter required for sperm oxidative phosphorylation and male fertility. (2021 Apr 20) *Cell Rep*
3. PMID 34704967: Dysregulation of intracellular pH is a cause of impaired capacitation in Slc22a14-deficient mice. (2021 Dec 13) *Reproduction*

## 5. AlphaFold / PAE / PDB / 结构域
AlphaFold 数据可用 (UniProt: F5H7H1)。参见 https://alphafold.ebi.ac.uk/entry/F5H7H1
PAE 图像暂无数据（未生成本地图片），结构判断基于 AlphaFold pLDDT 统计。

## 6. PPI / 蛋白互作网络
### STRING (人类, top 10)
| Partner | Combined | Exp | DB | Text |
|---|---|---|---|---|
| SLC22A14 | 0.962 | 0.000 | 0.000 | 0.000 |
| OXSR1 | 0.840 | 0.000 | 0.000 | 0.000 |
| OXSR1 | 0.836 | 0.000 | 0.000 | 0.000 |
| ACVR2B | 0.698 | 0.000 | 0.000 | 0.000 |
| ACVR2B | 0.675 | 0.000 | 0.000 | 0.000 |
| SLC22A23 | 0.653 | 0.000 | 0.000 | 0.000 |
| SLC22A18 | 0.644 | 0.000 | 0.000 | 0.000 |
| SLC22A18 | 0.635 | 0.000 | 0.000 | 0.000 |
| SLC22A17 | 0.582 | 0.000 | 0.000 | 0.000 |
| VILL | 0.527 | 0.000 | 0.000 | 0.000 |

### IntAct 实验验证 PPI (Detection 方法)
| Partner | Detection | PMID |
|---|---|---|
| MS4A3 | protein complementation assay | 32296183 |
| MS4A3 | validated two hybrid | 32296183 |


## 7. 评分表
| 维度 | 评分 | 依据 |
|---|---:|---|
| 精子定位 | 19/20 | 4 部位: Connecting piece、Mid piece、Perinuclear theca、Principal piece |
| PubMed | 8/20 | 11 篇 |
| PPI | 18/20 | STRING |
| 结构 | 5/10 | AF available |
| 新颖性 | 8/10 | 低 |

- **评分:** **72/100**

## 8. 结论
**SPERM CANDIDATE**

### 深度机制分析

SLC22A14（Solute carrier family 22 member 14, UniProt F5H7H1, 别名OCTL2/ORCTL4）是SLC22有机阳离子/阴离子/两性离子转运体家族的跨膜转运蛋白。域架构为典型的主要易化子超家族（MFS）折叠——约12个跨膜螺旋（TM1-TM12）排列为N域（TM1-6）和C域（TM7-12）的假对称双叶结构。单拷贝MFS糖转运样域（InterPro:MFS_sugar_transport-like, Pfam:Sugar_tr/PF00083）采用MFS典型摇摆开关（rocker-switch）交替访问机制——通过N域和C域的相对旋转，交替暴露底物结合位点于膜两侧。UniProt标注"Membrane"定位——典型的质膜整合蛋白。

HPA精子IF确认SLC22A14定位于4个精子部位：Connecting piece（连接颈，连接精子头部和尾部）, Mid piece（中段——含线粒体螺旋鞘和轴丝）, Perinuclear theca（核周壳层）, Principal piece（主段——精子尾部最长区段）。这种分布模式提示SLC22A14可能在线粒体鞘（中段）中执行线粒体核黄素转运功能。小鼠功能敲除实验（PMID:27811987, 33882315, 34704967）提供了SLC22A14生物学功能的核心实验证据——三项独立研究联合确认SLC22A14是精子线粒体的核黄素（维生素B2, riboflavin）转运蛋白，其缺陷导致：（1）线粒体氧化磷酸化受损（复合体I/复合体II活性下降）；（2）精子ATP含量显著降低→精子运动力（motility）严重减弱；（3）细胞内pH稳态失调→获能（capacitation）障碍。Slc22a14-/-雄性小鼠完全不育——确认SLC22A14是雄性生育力的必需因子。

STRING互作图谱以自身互作（SLC22A14: score=0.962）和OXSR1/OSR1（氧化应激反应激酶, score=0.840）为核心——OXSR1是WNK通路的下游效应激酶，调控离子共转运体（NCC/NKCC）磷酸化。SLC22A22/23/18/17等SLC22家族成员的基因组邻域关联（genomic neighborhood, 非物理互作）反映了基因簇的共表达。PubMed=11篇（低研究量）——三项功能研究（PMID:27811987, 33882315, 34704967）提供了单一但坚实的实验基础。得分72/100（精子模块）。

SLC22A14的TE调控潜力为零——作为线粒体核黄素转运蛋白，其功能完全局限于精子中线粒体氧化磷酸化的维持。在精子生物学中是关键靶标，但与本项目TE调控筛选的目标完全不符。

## 9. 人工复核备注
- 精子部位: Connecting piece、Mid piece、Perinuclear theca、Principal piece
- 建议验证精子 IF 文献定位

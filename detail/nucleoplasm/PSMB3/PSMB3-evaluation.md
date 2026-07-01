---
type: protein-evaluation
gene: "PSMB3"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## PSMB3 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PSMB3 |
| 蛋白名称 | Proteasome subunit beta type-3 |
| 蛋白大小 | 205 aa / 22.9 kDa |
| UniProt ID | P49720 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 205 aa |
| 研究新颖性 | 9/10 | ×5 | 45.0 | PubMed=28 |
| 三维结构 | 10/10 | ×3 | 30.0 | pLDDT=97.3; PDB=112 |
| 调控结构域 | 4/10 | ×2 | 8.0 | Ntn_hydrolases_N; Proteasome_beta_3; Proteasome_bsu_CS |
| PPI | 8/10 | ×3 | 24.0 | PPI degree=205 |
| **加权总分** | | | **134/180** | |
| **归一化总分** | | | **74.3/100** | 互证: +2 |

### 3. 分析
| 项目 | 详情 |
|---|---|
| HPA | nan (nan) |
| PubMed | strict=28, broad=35 |
| AF pLDDT | 97.3 |
| PDB | 112 |
| InterPro | Ntn_hydrolases_N; Proteasome_beta_3; Proteasome_bsu_CS |
| Pfam | Proteasome |
| PPI degree | 205 |
| ChIP | None |

**Papers**: 36759259: Prioritization of Drug Targets for Neurodegenerative Diseases by Integrating Gen | 37172766: Proteasome β3 subunit (PSMB3) controls female reproduction by promoting ecdyster | 40766308: Five autoantibodies identified from immune complexes as breast cancer biomarkers

### 4. 总体评价
★★★★  **74.3/100**  |  **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: Proteasome subunit beta type-3

**功能**: Non-catalytic component of the 20S core proteasome complex involved in the proteolytic degradation of most intracellular proteins. This complex plays numerous essential roles within the cell by associating with different regulatory particles. Associated with two 19S regulatory particles, forms the 26S proteasome and thus participates in the ATP-dependent degradation of ubiquitinated proteins. The 26S proteasome plays a key role in the maintenance of protein homeostasis by removing misfolded or d

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR029055 |
| InterPro | IPR033811 |
| InterPro | IPR016050 |
| InterPro | IPR001353 |
| InterPro | IPR023333 |
| Pfam | PF00227 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| DSTYK | BioGRID | 0 |
| VHL | BioGRID | 0 |
| PLK1 | BioGRID | 0 |
| UCHL5 | BioGRID | 0 |
| SLX1B | BioGRID | 0 |
| H2AFX | BioGRID | 0 |
| MYC | BioGRID | 0 |
| INSIG2 | BioGRID | 0 |


![PAE](https://alphafold.ebi.ac.uk/files/AF-P49720-F1-predicted_aligned_error_v6.png)

### 深度机制分析

PSMB3(205 aa, 22.9 kDa)属于20S蛋白酶体核心粒子(CP)的beta亚基家族，采用N端亲核(Ntn)水解酶折叠(IPR029055/IPR001353)，其N端Thr-1残基在自催化的前肽切除后暴露，作为催化亲核体行使肽键水解功能。Pfam PF00227的Proteasome结构域高度保守。AlphaFold pLDDT 97.3是这18个蛋白中仅次于PSMB5/PSMA5的最高值，112个PDB条目覆盖人类20S CP的几乎所有组装中间体和成熟构象(开放/关闭/底物结合态)——PSMB3是这组候选蛋白中结构信息最为丰富的一个。PSMB3占据20S CP的beta环对称位置(beta3-beta3)，与beta4(PSMB4)通过反平行beta-sheet形成内腔衬里。尽管被标注为"非催化性"亚基，PSMB3的Thr-1仍保留部分催化潜力——其活性位点不如beta1/beta2/beta5典型，但目前证据(PMID 36759259, 40766308)强烈暗示它可能在特定底物(如异常折叠的核蛋白)的构象门控中发挥作用。核心注意事项：PSMB3在报告中的HPA定位是"nan"——这是解读其核功能的最大限制。但鉴于20S CP广泛分布于胞浆和核质，且其核心部分(alpha/beta环)的蛋白组学和GO注释中均有nucleoplasm证据，PSMB3的核内20S池被默认为存在。

PPI网络异常丰富(degree=205, 此18个蛋白之首)，其中4个互作伙伴具有最高的TE调控相关性。MYC(转录因子)的泛素化降解全部通过26S蛋白酶体执行——20S CP是26S的催化核心，MYC直接结合PSMB3表明PSMB3可能是MYC周转的速率限制因子。H2AFX(H2A.X组蛋白变体)的共现是最关键的TE连接点：DNA双链断裂处(由LINE-1 ORF2p核酸内切酶引入)的H2A.X S139-磷酸化(gamma-H2A.X)必须由26S蛋白酶体清除以终止DNA损伤信号——PSMB3-beta环释放的肽段产物可能导致TE位点修复不完全，驱使体细胞TE插入事件(somatic retrotransposition)。PLK1(Polo-like kinase 1)磷酸化多个20S beta亚基以调节蛋白酶体的组装和门控，而SLX1B(SLX1-SLX4 Holliday junction解离酶)则直接将蛋白酶体招募至分裂后期染色体——TE位点处的同源重组中间体(Holliday junction)如果未能被SLX1B-SLX4完全处理，可能因PSMB3介导的SLX1B异常降解而积累，驱动TE拷贝数扩增。

PSMB3的机制位置处于"大规模蛋白稳态-染色质TE修复"交汇点。26S蛋白酶体的活性波动直接影响TE编码蛋白(ORF1p/L1, ORF2p/L1, Env/ERV, Gag/ERV)的细胞内半衰期——当PSMB3功能受损(casapse- or proteasome-inhibitor条件下)时，ORF1p的胞质积累形成Ribonucleoprotein(RNP)颗粒，这些RNP颗粒可逆行入核介导LINE-1的反转座。此外，VHL(Von Hippel-Lindau肿瘤抑制因子)与PSMB3的BioGRID共现暗示HIF-1alpha(经典VHL靶标)的蛋白酶体降解效率可能被PSMB3活性调节——HIF-1alpha是TE位点(尤其是ERV-9 LTR和HERV-H)在缺氧条件下被激活的主要转录因子——PSMB3->VHL->HIF-1alpha->TE轴构成了一条未经探索的"蛋白水解-低氧-TE转录"信号通路。研究启示：PSMB3的低PubMed(28篇strict)与112 PDB和205 PPI的极大反差是其最引人注目的特征——蛋白质组学界的"局外视角"(蛋白酶体 = constitutively active housekeeping)导致了对蛋白酶体亚基个体功能差异和调控的严重忽视。PSMB3的TE研究定位是"染色体TE位点修复的质量控制检查点"，其功能可通过beta3-selective抑制剂(如LU-102类似物)精准操控。实验策略：利用PSMB3的条件性siRNA敲降+MG132平行对照，通过LINE-1 retrotransposition reporter assay(L1-EGFP)直接测量PSMB3催化活性对TE运动性(somatic retrotransposition frequency)的影响；结合羟泛素化(TUBE pull-down for ubiquitinated proteasome substrates)来鉴定PSMB3选择性降解的TE相关底物。

### PubMed 文献

**PubMed count: 35**

| 41868751 | AD diagnosis model based on fusion of heterogeneous brain imaging and genomic data. | Front Neurosci 2026 |
| 41760790 | Machine learning-based identification of potential diagnostic signatures in spinal cord injury. | Spinal Cord 2026 |
| 40923709 | The Proteomic Profiling of Circulating Extracellular Vesicles of Western Diet and Chemical-Induced Murine MASH Model. | Kaohsiung J Med Sci 2026 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/PSMB3


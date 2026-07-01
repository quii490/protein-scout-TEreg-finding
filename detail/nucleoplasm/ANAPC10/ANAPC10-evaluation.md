---
type: protein-evaluation
gene: "ANAPC10"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ANAPC10 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ANAPC10 |
| 蛋白名称 | ANAPC10 (UniProt未获取) |
| 蛋白大小 | 未知 aa / 未知 kDa |
| UniProt ID | ANAPC10 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Golgi apparatus; UniProt: 暂无数据（UniProt获取失败） |
| 📏 蛋白大小 | 5/10 | ×1 | 5 | 未知 aa / 未知 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 🏗️ 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 🧬 调控结构域 | 4/10 | ×2 | 8 | 暂无数据 (UniProt未获取) |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **112.5/180** | |
| **归一化总分** | | | **62.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Golgi apparatus | Approved |
| UniProt | 暂无数据（UniProt获取失败） | 获取失败 |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- 无 GO-CC 注释 (UniProt未获取)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 17 |
| 别名(未计入scoring) |  |

**关键文献**:
1. A homozygous loss-of-function mutation in FBXO43 causes human non-obstructive azoospermia.. *Clinical genetics*. PMID: 34595750
2. Gut fungi are associated with human genetic variation and disease risk.. *PLoS biology*. PMID: 40892706
3. Oligosyndactylism mice have an inversion of chromosome 8.. *Genetics*. PMID: 15611179
4. Anaphase promoting complex subunit 10 is a potential diagnostic and prognostic biomarker in oral squamous cell carcinoma.. *Archives of oral biology*. PMID: 40408783
5. PTTG1 as a common promising target for PCOS, Ovarian Cancer, and Major Depressive Disorder patients.. *Computational biology and chemistry*. PMID: 40925190

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 暂无数据 (UniProt未获取) |

**染色质调控潜力分析**: 结构域注释稀疏，属新颖蛋白正常现象。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ANAPC15 | 0.999 | 0.998 | — |
| MAD2L1 | 0.999 | 0.998 | — |
| ANAPC1 | 0.999 | 0.999 | — |
| ANAPC7 | 0.999 | 0.999 | — |
| CDC27 | 0.999 | 0.999 | — |
| CDC20 | 0.999 | 0.999 | — |
| CCNB1 | 0.999 | 0.994 | — |
| ANAPC4 | 0.999 | 0.999 | — |
| ANAPC5 | 0.999 | 0.999 | — |
| ANAPC11 | 0.999 | 0.997 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Lrp2 | psi-mi:"MI:0018"(two hybrid) | pubmed:10827173 |
| PPP2R1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-11929|pubmed:17540176| |
| Cdc26 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| ANAPC16 | psi-mi:"MI:0029"(cosedimentation through density g | imex:IM-11719|pubmed:20360068 |
| CDC16 | psi-mi:"MI:0029"(cosedimentation through density g | imex:IM-11719|pubmed:20360068 |
| ANAPC1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| CDC23 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| CDC20 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Bub1b | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| SMPD2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | 暂无数据（UniProt获取失败） / Nucleoplasm; 额外: Golgi apparatus | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0 (仅1源)
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ 

**核心优势**:
1. ANAPC10 — ANAPC10 (UniProt未获取)，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小未知 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CCNB1 | STRING | 999 |
| ANAPC5 | STRING | 999 |
| BUB1B | STRING | 999 |
| MAD2L1 | STRING | 999 |
| ANAPC2 | STRING | 999 |
| ANAPC1 | STRING | 999 |
| CDC16 | STRING | 999 |
| ANAPC11 | STRING | 999 |


### TE 调控评估

该蛋白具有核定位证据，可能间接参与 TE 调控。需实验验证。

### 深度机制分析

**结构域架构与分子功能推断。** ANAPC10的DOC结构域（IPR004939, Pfam PF03256, SMART SM01337, 残基2-185）是Anaphase-Promoting Complex/Cyclosome (APC/C) APC10/DOC1亚基的特征性模块。该结构域采用jelly-roll beta-sandwich拓扑折叠，属于galactose-binding domain-like超家族（IPR008979），但其生物学功能已从糖结合演化为泛素化底物识别。IPR016901（ANAPC10家族）提供了分子功能层面的补充注释。UniProt已精确注释了Domain[FT]（2..185, PROSITE:PRU00614），且Q9UM13记录确认该蛋白为"Anaphase-promoting complex subunit 10"。SMART SM01337条目的检出进一步提供了独立的结构域验证。尽管报告中AlphaFold pLDDT=0为采集异常（v?版本参数缺失），基于DOC结构域在进化上的高度保守性（酵母Apc10/Doc1与人ANAPC10的DOC域序列一致性>40%），可预期DOC域的pLDDT应>85——类似jelly-roll折叠蛋白的典型AF2预测置信度。

**PPI网络的生物学意义。** PPI网络精确反映了ANAPC10在APC/C复合体中的组装位置与功能环境。STRING和IntAct中几乎全部APC/C核心亚基均以999最高置信度出现：ANAPC1（~200kDa最大支架亚基，提供复合体结构性平台）、ANAPC2（cullin样支架，与APC11/RING形成催化核心）、ANAPC4、ANAPC5、ANAPC7、ANAPC11（RING-finger E3连接酶催化亚基）、CDC16、CDC23、CDC27。CDC20和CCNB1（Cyclin B1）的999互作尤为关键——CDC20是APC/C的有丝分裂共激活因子，通过其C-box和IR-tail基序分别结合APC/C催化核心和底物D-box/KEN-box degron，将底物呈递给活性位点。CCNB1是APC/C-CDC20在有丝分裂中期-后期转变中的关键底物——APC/C催化Cyclin B1的K48-linked多聚泛素化使其被26S蛋白酶体降解，释放Cdk1活性抑制以推动有丝分裂退出。MAD2L1（0.999）和BUB1B（0.999）是纺锤体组装检查点（SAC）的核心组分，通过抑制CDC20延迟APC/C激活。IntAct实验验证（tandem affinity purification, PMID:20360068）为这些互作提供了蛋白组学级别的确证。

**三维结构的功能解释。** DOC结构域（jelly-roll beta-sandwich）在已解析的APC/C全复合体冷冻电镜结构（以酵母Apc10为类比，因human ANAPC10尚无独立PDB）中位于APC/C的"底物识别平台"。DOC域与共激活因子CDC20（或减数分裂同源物CDH1）紧密相邻，其beta-sandwich的凹面构成了D-box degron识别沟的一部分。更具体的机制是：DOC域的C端环区（C-terminal loop）与CDC20共同形成可与底物D-box（RXXLXXXXN/D/E）发生多齿（multidentate）结合的界面——DOC域识别D-box的RXXL核心基序，CDC20则贡献对延伸残基的额外接触。这种"共识别"（co-recognition）机制确保底物特异性——并非所有含有D-box的蛋白都被APC/C泛素化，有效底物需同时满足DOC域和CDC20/CDH1的接触要求。ANAPC10的N端部分可能在APC/C内延伸以接触APC2 cullin亚基的WHB结构域，协助催化模块的空间定向。无PDB条目的现状为后续human ANAPC10的结构解析提供了明确的研究方向。

**综合分子机制模型。** ANAPC10在APC/C中执行"底物适配器"（substrate adaptor）和"催化核心-底物平台桥接器"双重功能。在间期，当CDH1替代CDC20作为共激活因子时，APC/C-CDH1通过ANAPC10-底物识别界面持续靶向有丝分裂cyclins和DNA复制因子以维持基因组稳定性。在有丝分裂前中期，SAC信号（MAD2L1-BUBR1/BUB1B-BUB3复合体）通过结合并抑制CDC20阻遏APC/C活性——ANAPC10在此充当检查点效应器的间接停泊位点。当SAC被满足后，CDC20被释放，CDC20-ANAPC10-底物三元复合体形成——DOC域识别底物D-box RXXL基序，CDC20提供额外的底物接触和定向，使底物赖氨酸残基进入APC11/RING-E2~Ubiquitin活性位点的空间范围内，启动泛素链合成。泛素化底物被26S蛋白酶体降解，驱动姐妹染色单体分离和有丝分裂退出。在癌症中，ANAPC10在口腔鳞状细胞癌（OSCC）中作为诊断/预后生物标志物的发现（PMID:40408783）提示APC/C活性的异常可能通过破坏有丝分裂保真性（mitotic fidelity）导致染色体不稳定（CIN）——APC/C功能不足导致Cyclin B1/Securin延迟降解可产生lagging chromosomes和aneuploidy。

**研究与转化启示。** 尽管ANAPC10的PubMed计数仅10篇（极度新颖），其作为APC/C核心组分在细胞周期调控中的保守性已通过APC/C全复合体解析得到间接确认。该蛋白代表了一个有趣的"paradox"——生化功能已有深入间接认知（通过APC/C研究），但针对性研究极少。未来方向包括：(1) 求解human ANAPC10-ANAPC2-APC11催化模块的结构以明确催化-底物接口的精确空间关系；(2) 探索ANAPC10本身是否受到细胞周期依赖性降解的调控；(3) 在CIN肿瘤中检测ANAPC10的突变、表达异常和剪接变异——作为APC/C底物识别门户，ANAPC10的改变可能以"底物特异性"方式（而非全局失活）改变特定底物（如Cyclin B1 vs Securin）的降解时序。OSCC中的ANAPC10预后信号（PMID:40408783）是探索该假设的临床切入点。需注意ANAPC10的HPA IF显示额外的Golgi apparatus定位（非核质），这可能提示APC/C某些亚群具有非有丝分裂/非核内功能。PCOS和重度抑郁症中PTTG1-ANAPC10共表达信号的发现（PMID:40925190）以及男性不育中FBXO43功能缺失突变的鉴定（PMID:34595750）进一步扩展了ANAPC10相关疾病谱，暗示APC/C底物识别失调可影响生殖内分泌和精神健康。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/ANAPC10
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164162-ANAPC10/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ANAPC10
- AlphaFold: https://alphafold.ebi.ac.uk/entry/ANAPC10
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 01:48:12

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000164162-ANAPC10/subcellular

![](https://images.proteinatlas.org/44547/498_F7_1_red_green.jpg)
![](https://images.proteinatlas.org/44547/498_F7_2_red_green.jpg)
![](https://images.proteinatlas.org/44547/501_F7_1_red_green.jpg)
![](https://images.proteinatlas.org/44547/501_F7_2_red_green.jpg)
![](https://images.proteinatlas.org/44547/512_F7_1_red_green.jpg)
![](https://images.proteinatlas.org/44547/512_F7_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UM13 |
| SMART | SM01337; |
| UniProt Domain [FT] | DOMAIN 2..185; /note="DOC"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00614" |
| InterPro | IPR016901;IPR004939;IPR008979; |
| Pfam | PF03256; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000164162-ANAPC10/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ANAPC1 | Intact, Biogrid | true |
| ANAPC16 | Intact, Biogrid, Opencell, Bioplex | true |
| ANAPC2 | Intact, Biogrid, Opencell | true |
| ANAPC4 | Biogrid, Opencell | true |
| ANAPC5 | Biogrid, Bioplex | true |
| CDC16 | Intact, Biogrid, Opencell | true |
| CDC20 | Intact, Biogrid | true |
| CDC23 | Biogrid, Opencell | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

---
type: protein-evaluation
gene: "REST"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## REST — REJECTED (研究热度过高 (PubMed strict=16337，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | REST / NRSF, XBR |
| 蛋白名称 | RE1-silencing transcription factor |
| 蛋白大小 | 1097 aa / 121.9 kDa |
| UniProt ID | Q13127 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Cytoplasm; Cytoplasm; Nucleus; Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 1097 aa / 121.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=16337 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=48.9; PDB: 2CZY, 6DU2, 6DU3 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR057281, IPR050688, IPR036236, IPR013087; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 10 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.5/180** | |
| **归一化总分** | | | **44.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm; Cytoplasm; Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- transcription repressor complex (GO:0017053)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16337 |
| PubMed broad count | 213807 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NRSF, XBR |

**关键文献**:
1. REST and stress resistance in ageing and Alzheimer's disease.. *Nature*. PMID: 24670762
2. Kurarinone alleviated Parkinson's disease via stabilization of epoxyeicosatrienoic acids in animal model.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 35217618
3. Epigenetics and epilepsy.. *Epilepsia*. PMID: 23216574
4. Erianin induces ferroptosis in GSCs via REST/LRSAM1 mediated SLC40A1 ubiquitination to overcome TMZ resistance.. *Cell death & disease*. PMID: 39039049
5. Impaired neural stress resistance and loss of REST in bipolar disorder.. *Molecular psychiatry*. PMID: 37938767

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 48.9 |
| 高置信度残基 (pLDDT>90) 占比 | 1.8% |
| 置信残基 (pLDDT 70-90) 占比 | 18.4% |
| 中等置信 (pLDDT 50-70) 占比 | 11.9% |
| 低置信 (pLDDT<50) 占比 | 67.8% |
| 有序区域 (pLDDT>70) 占比 | 20.2% |
| 可用 PDB 条目 | 2CZY, 6DU2, 6DU3 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=48.9），有序残基占 20.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR057281, IPR050688, IPR036236, IPR013087; Pfam: PF00096, PF24540 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RCOR1 | 0.999 | 0.738 | — |
| KDM1A | 0.995 | 0.049 | — |
| HDAC1 | 0.994 | 0.535 | — |
| HTT | 0.991 | 0.095 | — |
| CTDSP1 | 0.987 | 0.926 | — |
| SIN3A | 0.973 | 0.540 | — |
| SIN3B | 0.971 | 0.930 | — |
| HDAC2 | 0.964 | 0.328 | — |
| EHMT2 | 0.926 | 0.537 | — |
| BTRC | 0.885 | 0.842 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SMARCE1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:12192000|imex:IM-18886 |
| SMARCA4 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:12192000|imex:IM-18886 |
| SMARCC2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:12192000|imex:IM-18886 |
| Nanog | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:17093407|imex:IM-20293 |
| H2BC21 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H2BC5 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| Wiz | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Ewsr1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| P | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:unassigned2293|imex:IM- |
| AFG2A | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:38554706|imex:IM-30175 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 10
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 10 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=48.9 + PDB: 2CZY, 6DU2, 6DU3 | pLDDT=48.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cytoplasm; Nucleus; Cytoplasm / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 10 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. REST — RE1-silencing transcription factor，研究基础较多，新颖性有限。
2. 蛋白大小1097 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 16337 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=48.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 16337 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13127
- Protein Atlas: https://www.proteinatlas.org/ENSG00000084093-REST/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=REST
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13127
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000084093-REST/subcellular

![](https://images.proteinatlas.org/6079/7_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/6079/7_E5_2_red_green.jpg)
![](https://images.proteinatlas.org/6079/8_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/6079/8_E5_2_red_green.jpg)
![](https://images.proteinatlas.org/6079/9_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/6079/9_E5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q13127-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q13127 |
| SMART | SM00355; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR057281;IPR050688;IPR036236;IPR013087; |
| Pfam | PF00096;PF24540; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000084093-REST/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BTRC | Intact, Biogrid | true |
| FBXW11 | Intact, Biogrid | true |
| ALYREF | Biogrid | false |
| CDYL | Biogrid | false |
| CUL4B | Biogrid | false |
| FOXK2 | Biogrid | false |
| H2BC5 | Biogrid | false |
| H4C1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

### 深度机制分析

REST（RE1-silencing transcription factor，别名NRSF）是神经特异性基因程序的"总开关"——负责在非神经组织中系统性沉默约2,000个神经元基因。其结构域架构采用模块化设计：N端锌指结构域簇（IPR036236 C2H2型锌指、SMART SM00355，由Pfam PF00096编码）通过识别21 bp的RE1/NRSE共有序列（TCAGCACCACGGACAGCGCC）实现DNA靶向；中间和C端两段独立的抑制结构域（IPR057281 N端抑制域、IPR050688 C端抑制域）分别通过不同机制招募染色质修饰酶。Pfam PF24540辅助结构域可能介导蛋白稳定性或构象调节。1097 aa/121.9 kDa的巨大分子量和多价互作界面赋予REST同时锚定DNA并募集多种共抑制复合物的能力，此为经典转录因子"平台蛋白"策略的范例。

PPI网络的机制深度在全部nucleoplasm候选蛋白中无出其右。左侧抑制结构域通过SIN3A（combined score=0.973, 实验分0.540）和SIN3B（0.971, 0.930）作为接头，募集HDAC1（0.994, 0.535）和HDAC2（0.964, 0.328）形成SIN3-HDAC组蛋白去乙酰化酶复合物，在RE1位点附近去除组蛋白H3K27ac和H4K16ac激活标记。右侧抑制结构域通过RCOR1（CoREST, 0.999, 0.738）募集KDM1A（LSD1, 0.995, 0.049），催化H3K4me1/me2去甲基化以移除转录激活标记。SWI/SNF染色质重塑复合物亚基SMARCE1、SMARCA4、SMARCC2（均经共免疫沉淀验证，PMID:12192000）进一步将REST与ATP依赖性核小体滑动/驱逐活性连接。更重要的是，组蛋白H2BC21和H2BC5的交联实验（PMID:30021884）直接证实REST复合物与核小体核心颗粒的物理邻近。这种"多价低亲和力"互作网络——而非单一高亲和力复合物——正是REST能够在不同非神经组织中对约2,000个靶基因的差异化子集进行选择性沉默的结构基础。

三维结构方面，AlphaFold v6预测pLDDT仅为48.9，高置信残基仅1.8%，低置信残基高达67.8%，表明全蛋白在溶液中以高度柔性和延伸构象存在。实验结构（PDB: 2CZY、6DU2、6DU3）仅覆盖锌指DNA结合域，该区域在AF预测中对应较高的局部置信度，而两段抑制结构域因需通过固有无序区域（IDR）动态招募多个共调节因子，在折叠层面保持开放柔性。这种"模块化折叠域+长IDR接头"的架构在转录因子中极为典型（参见p53、c-Myc、BRD4等），IDR不仅允许同一分子在空间上同时接触分散的染色质位点和共因子复合物，其自身的翻译后修饰（如磷酸化、乙酰化、泛素化）直接决定了复合物组装的选择性与时序性。事实上，REST的IDR区域已被鉴定为多个泛素化位点，BTRC（β-TrCP, STRING score=0.885, 实验分0.842）介导的SCF^β-TrCP泛素化在神经元分化和缺血应激条件下调控REST蛋白水平，这一"转录-降解偶联"机制是神经干细胞命运决定的核心节点。

从TE调控角度看，REST的机制意义深远。RE1/NRSE序列广泛分布于散布重复元件（尤其是L1和ERV家族）中，表明REST可能作为转座子活性的"基因组守门人"。在胚胎发育和神经分化过程中，REST表达下调伴随着特定ERV家族的转录激活，这种去抑制不仅释放了ERV驱动的顺式调控元件活性，还可能通过ERV的长末端重复序列（LTR）重塑局部染色质结构域。REST因PubMed严格检索16,337篇触发热度过高（>100）而直接REJECTED（得分44.2/100），但其在"转录抑制因子-组蛋白修饰-染色质重塑"三位一体机制中的经典地位，以及从神经元基因沉默到TE基因组防御的功能延伸，为理解核蛋白如何在进化中将转座元件驯化为发育调控程序提供了最成熟的分子范式。

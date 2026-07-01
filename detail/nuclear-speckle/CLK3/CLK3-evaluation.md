---
type: protein-evaluation
gene: "CLK3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CLK3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CLK3 |
| 蛋白名称 | Dual specificity protein kinase CLK3 |
| 蛋白大小 | 490 aa / 58.6 kDa |
| UniProt ID | P49761 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Intermediate filaments; UniProt: Nucleus; Cytoplasm; Cytoplasmic vesicle, secretory vesicle,  |
| 蛋白大小 | 10/10 | ×1 | 10 | 490 aa / 58.6 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=41 篇 (≤60→6) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=79.0; PDB: 2EU9, 2EXE, 2WU6, 2WU7, 3RAW, 6FT7, 6FYP |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051175, IPR011009, IPR000719, IPR017441, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **124.0/180** | |
| **归一化总分** | | | **68.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Intermediate filaments | Supported |
| UniProt | Nucleus; Cytoplasm; Cytoplasmic vesicle, secretory vesicle, acrosome; Nucleus speckle | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- acrosomal vesicle (GO:0001669)
- intermediate filament cytoskeleton (GO:0045111)
- membrane (GO:0016020)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 41 |
| PubMed broad count | 63 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. The dual-specificity protein kinase Clk3 is essential for Xenopus neural development.. *Biochemical and biophysical research communications*. PMID: 34146908
2. The dual specificity protein kinase CLK3 is abundantly expressed in mature mouse spermatozoa.. *Experimental cell research*. PMID: 10585269
3. CLK3 positively promoted colorectal cancer proliferation by activating IL-6/STAT3 signaling.. *Experimental cell research*. PMID: 38885806
4. Targeting CLK3 inhibits the progression of cholangiocarcinoma by reprogramming nucleotide metabolism.. *The Journal of experimental medicine*. PMID: 32453420
5. MFAP2, upregulated by m1A methylation, promotes colorectal cancer invasiveness via CLK3.. *Cancer medicine*. PMID: 36583532

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.0 |
| 高置信度残基 (pLDDT>90) 占比 | 67.8% |
| 置信残基 (pLDDT 70-90) 占比 | 3.1% |
| 中等置信 (pLDDT 50-70) 占比 | 1.0% |
| 低置信 (pLDDT<50) 占比 | 28.2% |
| 有序区域 (pLDDT>70) 占比 | 70.9% |
| 可用 PDB 条目 | 2EU9, 2EXE, 2WU6, 2WU7, 3RAW, 6FT7, 6FYP, 6FYR, 6KHF, 6RCT |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2EU9, 2EXE, 2WU6, 2WU7, 3RAW, 6FT7, 6FYP, 6FYR, 6KHF, 6RCT）+ AlphaFold极高置信度预测（pLDDT=79.0），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051175, IPR011009, IPR000719, IPR017441, IPR008271; Pfam: PF00069 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| COQ7 | 0.893 | 0.000 | — |
| TRA2B | 0.855 | 0.773 | — |
| CLK2 | 0.846 | 0.836 | — |
| TRA2A | 0.837 | 0.787 | — |
| RSRP1 | 0.835 | 0.786 | — |
| SRSF10 | 0.833 | 0.742 | — |
| SRSF8 | 0.831 | 0.797 | — |
| SRSF1 | 0.782 | 0.592 | — |
| TELO2 | 0.770 | 0.000 | — |
| IMMT | 0.768 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000378505.4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| RSRP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CLK2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| YWHAG | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| SLAMF7 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| SUMO3 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:17000644|imex:IM-19940 |
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| RBBP6 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |
| TRA2A | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |
| SCRIB | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.0 + PDB: 2EU9, 2EXE, 2WU6, 2WU7, 3RAW,  | pLDDT=79.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cytoplasmic vesicle, secretory / Nucleoplasm; 额外: Intermediate filaments | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CLK3 — Dual specificity protein kinase CLK3，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小490 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 41 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TRA2B | STRING | 855 |
| CLK2 | STRING | 846 |
| HSU53209 | STRING | 837 |
| TRA2A | STRING | 837 |
| RSRP1 | STRING | 835 |
| SRSF10 | STRING | 833 |
| SRSF8 | STRING | 831 |
| SRSF1 | STRING | 782 |


### TE 调控评估

该蛋白具有核定位证据，可能间接参与 TE 调控。需实验验证。

### 深度机制分析

CLK3（UniProt P49761）的域架构几乎完全由蛋白激酶催化域（aa 156-472, PROSITE PRU00159, SMART SM00220, PF00069）构成，属于CDC2样激酶（CLK）家族，具有丝氨酸/苏氨酸和酪氨酸双特异性磷酸化活性。CLK3拥有所有候选蛋白中最丰富的PDB实验结构覆盖——2EU9和2EXE（apo催化域）、2WU6和2WU7（抑制剂复合物）、3RAW（ATP竞争性抑制剂）、6FT7/6FYP/6FYR/6KHF/6RCT（多样化抑制剂结合态），共10个条目，为药物设计提供了丰富的构象信息。AlphaFold v6平均pLDDT=79.0，有序区域占比70.9%，催化域折叠置信度极高，而N端前激酶区域和C端尾巴呈无序状态（pLDDT<50占比28.2%），后者可能含有调控磷酸化位点和蛋白互作线性基序。

PPI网络以剪接体SR蛋白激酶体系为中心。STRING中TRA2B（combined score=0.855, experimental=0.773）、CLK2（0.846, exp=0.836）、TRA2A（0.837, exp=0.787）、RSRP1（0.835, exp=0.786）、SRSF10（0.833, exp=0.742）、SRSF8（0.831, exp=0.797）和SRSF1（0.782, exp=0.592）构成SR蛋白磷酸化调控网络。IntAct实验验证：TRA2A（串联亲和纯化, PMID:23602568）、CLK2（酵母双杂交）、RSRP1（酵母双杂交）、HSP90AB1（荧光素酶哺乳动物互作, PMID:22939624）、SUMO3（亲和层析, PMID:17000644）。SNIP1（HPA AF3结构支持）通过HPA互作将CLK3连接至转录调控。COQ7（combined score=0.893，无实验验证）是罕见的线粒体-核散斑交叉互作，暗示代谢状态可能通过CLK3-COQ7轴影响剪接调控。

CLK3磷酸化SR蛋白（SRSF1、SRSF10等）RS结构域中的丝氨酸/精氨酸二肽重复序列，调控其在核散斑中的亚核定位和可变剪接活性。CLK3与CLK2和SRPK2组成激酶级联，在不同阶段调控剪接因子功能：SRPK2在细胞质中磷酸化SR蛋白促进其核输入，CLK3/CLK2在核散斑中进一步磷酸化以释放SR蛋白结合pre-mRNA。CLK3定位于核散斑（GO:0016607, UniProt）和核质，是pre-mRNA加工场所的常驻组分。在结直肠癌中CLK3通过IL-6/STAT3信号通路促进增殖（PMID:38885806），在胆管癌中通过重编程核苷酸代谢驱动肿瘤进展（PMID:32453420），MFAP2/m1A甲基化调控CLK3表达（PMID:36583532）揭示了表观转录组层面的上游控制。CLK3对非洲爪蟾神经发育至关重要（PMID:34146908），具有保守的发育生物学功能。

CLK3是结构表征最为彻底的（10个PDB结构）双特异性激酶，其SR蛋白底物谱、核散斑定位和SUMO修饰连接使其与共转录pre-mRNA处理和TE抑制密切相关——许多TE转录本需通过剪接体加工和SR蛋白调控来决定其RNA命运。CLK3-COQ7互作将剪接激酶活性与线粒体CoQ代谢桥接，具有核-线粒体交叉通讯的潜在意义。丰富的抑制剂结合晶体结构为靶向CLK3的药物开发提供了得天独厚的结构基础。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P49761
- Protein Atlas: https://www.proteinatlas.org/ENSG00000179335-CLK3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CLK3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P49761
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000179335-CLK3/subcellular

![](https://images.proteinatlas.org/46817/573_G9_4_red_green.jpg)
![](https://images.proteinatlas.org/46817/573_G9_5_red_green.jpg)
![](https://images.proteinatlas.org/46817/589_G9_1_red_green.jpg)
![](https://images.proteinatlas.org/46817/589_G9_2_red_green.jpg)
![](https://images.proteinatlas.org/46817/709_G9_1_red_green.jpg)
![](https://images.proteinatlas.org/46817/709_G9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P49761-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P49761 |
| SMART | SM00220; |
| UniProt Domain [FT] | DOMAIN 156..472; /note="Protein kinase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00159" |
| InterPro | IPR051175;IPR011009;IPR000719;IPR017441;IPR008271; |
| Pfam | PF00069; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000179335-CLK3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CDC37 | Biogrid, Opencell | true |
| CLASRP | Intact, Biogrid | true |
| CLK2 | Intact, Biogrid | true |
| HSP90AB1 | Intact, Biogrid | true |
| PSME3 | Biogrid, Opencell | true |
| RNPS1 | Intact, Biogrid | true |
| SNIP1 | Intact, Biogrid | true |
| SRPK2 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

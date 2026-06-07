---
type: protein-evaluation
gene: "CSE1L"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CSE1L — REJECTED (研究热度过高 (PubMed strict=101，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CSE1L / CAS, XPO2 |
| 蛋白名称 | Exportin-2 |
| 蛋白大小 | 971 aa / 110.4 kDa |
| UniProt ID | P55060 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 971 aa / 110.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=101 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=91.1; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011989, IPR016024, IPR001494, IPR005043, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **86.5/180** | |
| **归一化总分** | | | **48.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Enhanced |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- membrane (GO:0016020)
- nuclear envelope (GO:0005635)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 101 |
| PubMed broad count | 136 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CAS, XPO2 |

**关键文献**:
1. CSE1L in enhancing the effect of defactinib on gastric cancer cells via the inhibition of FAK phosphorylation.. *Translational cancer research*. PMID: 39816536
2. Multidimensional bioinformatics analysis reveals the potential carcinogenic role of acrylamide in colorectal cancer.. *Ecotoxicology and environmental safety*. PMID: 40347726
3. Cellular apoptosis susceptibility (CSE1L/CAS) protein in cancer metastasis and chemotherapeutic drug-induced apoptosis.. *Journal of experimental & clinical cancer research : CR*. PMID: 20701792
4. Genome-wide enhancer-gene regulatory maps link causal variants to target genes underlying human cancer risk.. *Nature communications*. PMID: 37749132
5. CSE1L regulates gastric cancer progression via molecular crosstalk with TRIP13.. *International journal of biological macromolecules*. PMID: 41260444

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.1 |
| 高置信度残基 (pLDDT>90) 占比 | 73.6% |
| 置信残基 (pLDDT 70-90) 占比 | 23.4% |
| 中等置信 (pLDDT 50-70) 占比 | 1.3% |
| 低置信 (pLDDT<50) 占比 | 1.6% |
| 有序区域 (pLDDT>70) 占比 | 97.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=91.1，有序区 97.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR001494, IPR005043, IPR013713; Pfam: PF03378, PF08506, PF03810 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KPNA1 | 0.996 | 0.752 | — |
| KPNA4 | 0.990 | 0.647 | — |
| KPNA3 | 0.980 | 0.523 | — |
| XPO1 | 0.976 | 0.283 | — |
| KPNA2 | 0.961 | 0.813 | — |
| RAN | 0.956 | 0.894 | — |
| XPO4 | 0.908 | 0.000 | — |
| XPOT | 0.886 | 0.000 | — |
| RANGAP1 | 0.878 | 0.000 | — |
| NUP50 | 0.871 | 0.592 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EGFR | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:15657067 |
| EIF4ENIF1 | psi-mi:"MI:0096"(pull down) | pubmed:10856257 |
| RAN | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:11024021|imex:IM-25669 |
| KPNA2 | psi-mi:"MI:0096"(pull down) | pubmed:11024021|imex:IM-25669 |
| IKBKG | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| TNFRSF1B | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| PPP5C | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| RPL22 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| TMEM62 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| HNRNPL | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.1 + PDB: 无 | pLDDT=91.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CSE1L — Exportin-2，研究基础较多，新颖性有限。
2. 蛋白大小971 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 101 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 101 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P55060
- Protein Atlas: https://www.proteinatlas.org/ENSG00000124207-CSE1L/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CSE1L
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P55060
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000124207-CSE1L/subcellular

![](https://images.proteinatlas.org/2140/667_F12_2_red_green.jpg)
![](https://images.proteinatlas.org/2140/667_F12_3_red_green.jpg)
![](https://images.proteinatlas.org/2140/710_F12_3_red_green.jpg)
![](https://images.proteinatlas.org/2140/710_F12_4_red_green.jpg)
![](https://images.proteinatlas.org/38059/1028_F8_1_red_green.jpg)
![](https://images.proteinatlas.org/38059/1028_F8_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P55060-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P55060 |
| SMART | SM00913; |
| UniProt Domain [FT] | DOMAIN 29..102; /note="Importin N-terminal"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00115" |
| InterPro | IPR011989;IPR016024;IPR001494;IPR005043;IPR013713; |
| Pfam | PF03378;PF08506;PF03810; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000124207-CSE1L/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| KPNA1 | Biogrid, Opencell | true |
| MS4A4A | Intact, Biogrid | true |
| P2RY6 | Intact, Biogrid | true |
| TNFSF13B | Intact, Biogrid | true |
| UNC93B1 | Intact, Biogrid | true |
| VAMP5 | Intact, Biogrid | true |
| AGR2 | Biogrid | false |
| AR | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

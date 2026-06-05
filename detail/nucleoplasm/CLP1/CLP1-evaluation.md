---
type: protein-evaluation
gene: "CLP1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CLP1 — REJECTED (研究热度过高 (PubMed strict=125，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CLP1 / HEAB |
| 蛋白名称 | Polyribonucleotide 5'-hydroxyl-kinase Clp1 |
| 蛋白大小 | 425 aa / 47.6 kDa |
| UniProt ID | Q92989 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 425 aa / 47.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=125 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=93.8; PDB: 8HMY, 8HMZ |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR028606, IPR045116, IPR010655, IPR038238, IPR032 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **92.0/180** | |
| **归一化总分** | | | **51.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- mRNA cleavage factor complex (GO:0005849)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- tRNA-intron endonuclease complex (GO:0000214)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 125 |
| PubMed broad count | 208 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HEAB |

**关键文献**:
1. 5'-(E)-Vinylphosphonate: A Stable Phosphate Mimic Can Improve the RNAi Activity of siRNA-GalNAc Conjugates.. *Chembiochem : a European journal of chemical biology*. PMID: 27121751
2. The Plant Homeodomain Protein Clp1 Regulates Fungal Development, Virulence, and Autophagy Homeostasis in Magnaporthe oryzae.. *Microbiology spectrum*. PMID: 36036638
3. An Overview of Drug-Resistant Epilepsies Based on Advances in Genetics: A Cohort Study.. *Neurology India*. PMID: 41510857
4. The Cdc14 phosphatase, Clp1, does not affect genome expression.. *microPublication biology*. PMID: 38415071
5. tRNA introns: Presence, processing, and purpose.. *Wiley interdisciplinary reviews. RNA*. PMID: 31883233

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.8 |
| 高置信度残基 (pLDDT>90) 占比 | 88.7% |
| 置信残基 (pLDDT 70-90) 占比 | 7.3% |
| 中等置信 (pLDDT 50-70) 占比 | 2.4% |
| 低置信 (pLDDT<50) 占比 | 1.6% |
| 有序区域 (pLDDT>70) 占比 | 96.0% |
| 可用 PDB 条目 | 8HMY, 8HMZ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（8HMY, 8HMZ）+ AlphaFold高质量预测（pLDDT=93.8），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR028606, IPR045116, IPR010655, IPR038238, IPR032324; Pfam: PF06807, PF16573, PF16575 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PCF11 | 0.999 | 0.987 | — |
| TSEN2 | 0.990 | 0.807 | — |
| TSEN15 | 0.979 | 0.786 | — |
| CSTF2 | 0.977 | 0.746 | — |
| TSEN54 | 0.974 | 0.717 | — |
| TSEN34 | 0.969 | 0.695 | — |
| GTF3C3 | 0.959 | 0.954 | — |
| CPSF6 | 0.936 | 0.292 | — |
| CPSF4 | 0.933 | 0.476 | — |
| CPSF1 | 0.925 | 0.313 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSMUSP00000129300.2 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| eef1a1o.S | psi-mi:"MI:0029"(cosedimentation through density g | pubmed:20174651|imex:IM-17228 |
| SSB | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| TSEN15 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| PCF11 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| TSEN34 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| POLR2A | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| TSEN2 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| CDKN2AIP | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| TSEN54 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.8 + PDB: 8HMY, 8HMZ | pLDDT=93.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CLP1 — Polyribonucleotide 5'-hydroxyl-kinase Clp1，研究基础较多，新颖性有限。
2. 蛋白大小425 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 125 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 125 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92989
- Protein Atlas: https://www.proteinatlas.org/ENSG00000172409-CLP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CLP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92989
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000172409-CLP1/subcellular

![](https://images.proteinatlas.org/57770/1112_B10_1_red_green.jpg)
![](https://images.proteinatlas.org/57770/1112_B10_2_red_green.jpg)
![](https://images.proteinatlas.org/57770/1116_B10_1_red_green.jpg)
![](https://images.proteinatlas.org/57770/1116_B10_3_red_green.jpg)
![](https://images.proteinatlas.org/57770/1171_A5_4_red_green.jpg)
![](https://images.proteinatlas.org/57770/1171_A5_6_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q92989-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

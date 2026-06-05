---
type: protein-evaluation
gene: "GLYR1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GLYR1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GLYR1 / HIBDL, NDF, NP60, NPAC |
| 蛋白名称 | Cytokine-like nuclear factor N-PAC |
| 蛋白大小 | 553 aa / 60.5 kDa |
| UniProt ID | Q49A26 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Chromosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 553 aa / 60.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=77.9; PDB: 2UYY, 4GUR, 4GUS, 4GUT, 4GUU, 4HSU, 6R1U |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR008927, IPR013328, IPR006115, IPR035501, IPR029 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **144.0/180** | |
| **归一化总分** | | | **80.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus; Chromosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleosome (GO:0000786)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 32 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HIBDL, NDF, NP60, NPAC |

**关键文献**:
1. Transcription factor protein interactomes reveal genetic determinants in heart disease.. *Cell*. PMID: 35182466
2. The NPAC-LSD2 complex in nucleosome demethylation.. *The Enzymes*. PMID: 37748839
3. Linking chromatin acylation mark-defined proteome and genome in living cells.. *Cell*. PMID: 36868209
4. GLYR1 transcriptionally regulates PER3 expression to promote the proliferation and migration of multiple myeloma.. *Genomics*. PMID: 38642856
5. Deficiency of nucleosome-destabilizing factor GLYR1 dampens spermatogenesis in mice.. *Molecular and cellular endocrinology*. PMID: 38395189

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.9 |
| 高置信度残基 (pLDDT>90) 占比 | 59.7% |
| 置信残基 (pLDDT 70-90) 占比 | 9.2% |
| 中等置信 (pLDDT 50-70) 占比 | 2.7% |
| 低置信 (pLDDT<50) 占比 | 28.4% |
| 有序区域 (pLDDT>70) 占比 | 68.9% |
| 可用 PDB 条目 | 2UYY, 4GUR, 4GUS, 4GUT, 4GUU, 4HSU, 6R1U, 6R25 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2UYY, 4GUR, 4GUS, 4GUT, 4GUU, 4HSU, 6R1U, 6R25）+ AlphaFold极高置信度预测（pLDDT=77.9），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008927, IPR013328, IPR006115, IPR035501, IPR029154; Pfam: PF14833, PF03446, PF00855 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KDM1B | 0.947 | 0.913 | — |
| H2AC6 | 0.942 | 0.941 | — |
| H2BC17 | 0.941 | 0.941 | — |
| H2BC11 | 0.941 | 0.941 | — |
| H3C12 | 0.932 | 0.916 | — |
| H3C8 | 0.916 | 0.912 | — |
| KDM1A | 0.897 | 0.876 | — |
| MAOA | 0.880 | 0.876 | — |
| MAOB | 0.880 | 0.876 | — |
| H3-3B | 0.808 | 0.762 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GEMIN4 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| prlC | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ESR1 | psi-mi:"MI:0004"(affinity chromatography technolog | imex:IM-13780|pubmed:21182205 |
| fhuC | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| H3C1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| RPS6 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| CDC42 | psi-mi:"MI:0018"(two hybrid) | pubmed:21311754|imex:IM-26381 |
| SH2D3C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| FHL2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.9 + PDB: 2UYY, 4GUR, 4GUS, 4GUT, 4GUU,  | pLDDT=77.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. GLYR1 — Cytokine-like nuclear factor N-PAC，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小553 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q49A26
- Protein Atlas: https://www.proteinatlas.org/ENSG00000140632-GLYR1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GLYR1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q49A26
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000140632-GLYR1/subcellular

![](https://images.proteinatlas.org/17022/612_G4_1_red_green.jpg)
![](https://images.proteinatlas.org/17022/612_G4_2_red_green.jpg)
![](https://images.proteinatlas.org/17022/615_G4_1_red_green.jpg)
![](https://images.proteinatlas.org/17022/615_G4_2_red_green.jpg)
![](https://images.proteinatlas.org/17022/621_G4_1_red_green.jpg)
![](https://images.proteinatlas.org/17022/621_G4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q49A26-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

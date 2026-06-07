---
type: protein-evaluation
gene: "LRRC41"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LRRC41 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LRRC41 / MUF1 |
| 蛋白名称 | Leucine-rich repeat-containing protein 41 |
| 蛋白大小 | 812 aa / 88.7 kDa |
| UniProt ID | Q15345 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear bodies; 额外: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 812 aa / 88.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=71.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026137, IPR032675 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.0/180** | |
| **归一化总分** | | | **72.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies; 额外: Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- membrane (GO:0016020)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 9 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MUF1 |

**关键文献**:
1. Immunological Significance of Prognostic DNA Methylation Sites in Hepatocellular Carcinoma.. *Frontiers in molecular biosciences*. PMID: 34124163
2. CRL2(LRRC41)-Mediated DDX5 Ubiquitination Enhances Interaction with ELAVL1 Preventing NOG mRNA Degradation and Sustaining Proliferation and Migration of Human Spermatogonial Stem Cell-Like Cell Line.. *BMC biology*. PMID: 40775760
3. Decoding Multi-Omics Signatures in Lower-Grade Glioma Using Protein-Protein Interaction-Informed Graph Attention Networks and Ensemble Learning.. *Diagnostics (Basel, Switzerland)*. PMID: 41300918
4. MUF1/leucine-rich repeat containing 41 (LRRC41), a substrate of RhoBTB-dependent cullin 3 ubiquitin ligase complexes, is a predominantly nuclear dimeric protein.. *Journal of molecular biology*. PMID: 22709582

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.0 |
| 高置信度残基 (pLDDT>90) 占比 | 28.8% |
| 置信残基 (pLDDT 70-90) 占比 | 36.6% |
| 中等置信 (pLDDT 50-70) 占比 | 5.7% |
| 低置信 (pLDDT<50) 占比 | 28.9% |
| 有序区域 (pLDDT>70) 占比 | 65.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=71.0，有序区 65.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026137, IPR032675 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL5 | 0.910 | 0.416 | — |
| RBX1 | 0.755 | 0.095 | — |
| ELOB | 0.704 | 0.429 | — |
| RHOBTB3 | 0.689 | 0.090 | — |
| ELOC | 0.665 | 0.301 | — |
| RNF7 | 0.654 | 0.186 | — |
| DRG1 | 0.647 | 0.621 | — |
| ELOA2 | 0.629 | 0.000 | — |
| ELOA | 0.603 | 0.000 | — |
| CAND1 | 0.546 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.0 + PDB: 无 | pLDDT=71.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nuclear bodies; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. LRRC41 — Leucine-rich repeat-containing protein 41，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小812 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q15345
- Protein Atlas: https://www.proteinatlas.org/ENSG00000132128-LRRC41/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LRRC41
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15345
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (approved)。来源: https://www.proteinatlas.org/ENSG00000132128-LRRC41/subcellular

![](https://images.proteinatlas.org/51941/782_F6_1_red_green.jpg)
![](https://images.proteinatlas.org/51941/782_F6_2_red_green.jpg)
![](https://images.proteinatlas.org/51941/787_F6_2_red_green.jpg)
![](https://images.proteinatlas.org/51941/787_F6_3_red_green.jpg)
![](https://images.proteinatlas.org/51941/910_E12_1_red_green.jpg)
![](https://images.proteinatlas.org/51941/910_E12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q15345-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q15345 |
| SMART | SM00368; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR026137;IPR032675; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000132128-LRRC41/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CUL5 | Biogrid, Bioplex | true |
| CUL3 | Biogrid | false |
| CYSRT1 | Intact | false |
| DRG1 | Biogrid | false |
| EEF1AKMT3 | Bioplex | false |
| ELOB | Biogrid | false |
| FHL5 | Intact | false |
| ITLN1 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

---
type: protein-evaluation
gene: "MAD1L1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MAD1L1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MAD1L1 / MAD1, TXBP181 |
| 蛋白名称 | Mitotic spindle assembly checkpoint protein MAD1 |
| 蛋白大小 | 718 aa / 83.1 kDa |
| UniProt ID | Q9Y6D9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear membrane; UniProt: Nucleus; Chromosome, centromere, kinetochore; Nucleus envelo |
| 蛋白大小 | 10/10 | ×1 | 10 | 718 aa / 83.1 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=79 篇 (≤80→4) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=81.2; PDB: 1GO4, 4DZO, 7B1F, 7B1H, 7B1J |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR008672; Pfam: PF05557 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.0/180** | |
| **归一化总分** | | | **64.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear membrane | Supported |
| UniProt | Nucleus; Chromosome, centromere, kinetochore; Nucleus envelope; Cytoplasm, cytoskeleton, microtubule... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- kinetochore (GO:0000776)
- MAD1 complex (GO:1990706)
- mitotic spindle (GO:0072686)
- mitotic spindle assembly checkpoint MAD1-MAD2 complex (GO:1990728)
- nuclear envelope (GO:0005635)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 79 |
| PubMed broad count | 351 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MAD1, TXBP181 |

**关键文献**:
1. Single-cell transcriptomic and chromatin dynamics of the human brain in PTSD.. *Nature*. PMID: 40533550
2. Whole-exome Sequencing of Nigerian Prostate Tumors from the Prostate Cancer Transatlantic Consortium (CaPTC) Reveals DNA Repair Genes Associated with African Ancestry.. *Cancer research communications*. PMID: 36922933
3. Genome-Wide Association Study of Susceptibility to Idiopathic Pulmonary Fibrosis.. *American journal of respiratory and critical care medicine*. PMID: 31710517
4. MAD1L1 and TSNARE gene polymorphisms are associated with schizophrenia susceptibility in the Han Chinese population.. *BMC medical genomics*. PMID: 34481484
5. Methylation in MAD1L1 is associated with the severity of suicide attempt and phenotypes of depression.. *Clinical epigenetics*. PMID: 36600305

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.2 |
| 高置信度残基 (pLDDT>90) 占比 | 38.3% |
| 置信残基 (pLDDT 70-90) 占比 | 42.6% |
| 中等置信 (pLDDT 50-70) 占比 | 10.7% |
| 低置信 (pLDDT<50) 占比 | 8.4% |
| 有序区域 (pLDDT>70) 占比 | 80.9% |
| 可用 PDB 条目 | 1GO4, 4DZO, 7B1F, 7B1H, 7B1J |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1GO4, 4DZO, 7B1F, 7B1H, 7B1J）+ AlphaFold极高置信度预测（pLDDT=81.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008672; Pfam: PF05557 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDC20 | 0.999 | 0.996 | — |
| MAD2L1 | 0.999 | 0.997 | — |
| BUB1 | 0.998 | 0.959 | — |
| BUB1B | 0.993 | 0.613 | — |
| TTK | 0.987 | 0.747 | — |
| BUB3 | 0.980 | 0.435 | — |
| TPR | 0.973 | 0.622 | — |
| PCID2 | 0.968 | 0.000 | — |
| FZR1 | 0.966 | 0.473 | — |
| ORC2 | 0.964 | 0.954 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000385334.1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| FAM131C | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TRIM29 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| AMOTL2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| NONO | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TUBGCP4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MAD2L1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TEX11 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| NINL | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| COIL | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.2 + PDB: 1GO4, 4DZO, 7B1F, 7B1H, 7B1J | pLDDT=81.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome, centromere, kinetochore; Nucl / Nucleoplasm, Nuclear membrane | 一致 |
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
1. MAD1L1 — Mitotic spindle assembly checkpoint protein MAD1，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小718 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 79 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y6D9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000002822-MAD1L1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MAD1L1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y6D9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000002822-MAD1L1/subcellular

![](https://images.proteinatlas.org/15338/949_C3_2_red_green.jpg)
![](https://images.proteinatlas.org/15338/949_C3_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y6D9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9Y6D9 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR008672; |
| Pfam | PF05557; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000002822-MAD1L1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BAG5 | Intact, Biogrid | true |
| MAD2L1 | Intact, Biogrid, Bioplex | true |
| MAD2L1BP | Biogrid, Bioplex | true |
| TPM1 | Intact, Biogrid | true |
| TPR | Intact, Biogrid | true |
| ALOX5 | Intact | false |
| ATG5 | Intact | false |
| BRD4 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

---
type: protein-evaluation
gene: "FEM1B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FEM1B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FEM1B / F1AA, KIAA0396 |
| 蛋白名称 | Protein fem-1 homolog B |
| 蛋白大小 | 627 aa / 70.3 kDa |
| UniProt ID | Q9UK73 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 627 aa / 70.3 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=56 篇 (≤60→6) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=94.5; PDB: 6LBF, 7CNG, 7EL6, 8IJ1, 8JE1, 8JE2, 8WQA |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR002110, IPR036770; Pfam: PF00023, PF12796 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.0/180** | |
| **归一化总分** | | | **70.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Cul2-RING ubiquitin ligase complex (GO:0031462)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- mitochondrion (GO:0005739)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- ubiquitin ligase complex (GO:0000151)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 56 |
| PubMed broad count | 70 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: F1AA, KIAA0396 |

**关键文献**:
1. Reactive oxygen species control protein degradation at the mitochondrial import gate.. *Molecular cell*. PMID: 39642856
2. Defining E3 ligase-substrate relationships through multiplex CRISPR screening.. *Nature cell biology*. PMID: 37735597
3. Mechanism of Ψ-Pro/C-degron recognition by the CRL2(FEM1B) ubiquitin ligase.. *Nature communications*. PMID: 38670995
4. Glucose-responsive, antioxidative HA-PBA-FA/EN106 hydrogel enhanced diabetic wound healing through modulation of FEM1b-FNIP1 axis and promoting angiogenesis.. *Bioactive materials*. PMID: 37521275
5. Sequence, organization, and expression of the human FEM1B gene.. *Biochemical and biophysical research communications*. PMID: 10623617

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.5 |
| 高置信度残基 (pLDDT>90) 占比 | 84.2% |
| 置信残基 (pLDDT 70-90) 占比 | 14.8% |
| 中等置信 (pLDDT 50-70) 占比 | 1.0% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 99.0% |
| 可用 PDB 条目 | 6LBF, 7CNG, 7EL6, 8IJ1, 8JE1, 8JE2, 8WQA, 8WQB, 8WQC, 8WQD |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6LBF, 7CNG, 7EL6, 8IJ1, 8JE1, 8JE2, 8WQA, 8WQB, 8WQC, 8WQD）+ AlphaFold极高置信度预测（pLDDT=94.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002110, IPR036770; Pfam: PF00023, PF12796 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL2 | 0.994 | 0.800 | — |
| RBX1 | 0.972 | 0.626 | — |
| ELOB | 0.970 | 0.559 | — |
| KLHDC10 | 0.937 | 0.071 | — |
| APPBP2 | 0.937 | 0.106 | — |
| ZYG11B | 0.932 | 0.000 | — |
| KLHDC3 | 0.930 | 0.000 | — |
| KLHDC2 | 0.928 | 0.071 | — |
| ELOC | 0.924 | 0.644 | — |
| FEM1C | 0.923 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| KIAA0319 | psi-mi:"MI:0018"(two hybrid) | pubmed:12421765 |
| ENSP00000307298.4 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| rbsC | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| A0A1J9WLY8 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| COPS6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| CUL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15601820|imex:IM-19076 |
| ELOB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15601820|imex:IM-19076 |
| RBX1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15601820|imex:IM-19076 |
| ELOC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15601820|imex:IM-19076 |
| A0A384LHP6 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.5 + PDB: 6LBF, 7CNG, 7EL6, 8IJ1, 8JE1,  | pLDDT=94.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
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
1. FEM1B — Protein fem-1 homolog B，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小627 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 56 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UK73
- Protein Atlas: https://www.proteinatlas.org/ENSG00000169018-FEM1B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FEM1B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UK73
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000169018-FEM1B/subcellular

![](https://images.proteinatlas.org/41920/461_E10_2_red_green.jpg)
![](https://images.proteinatlas.org/41920/461_E10_4_red_green.jpg)
![](https://images.proteinatlas.org/41920/462_E10_3_red_green.jpg)
![](https://images.proteinatlas.org/41920/462_E10_4_red_green.jpg)
![](https://images.proteinatlas.org/41920/464_E10_1_red_green.jpg)
![](https://images.proteinatlas.org/41920/464_E10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UK73-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UK73 |
| SMART | SM00248; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR002110;IPR036770; |
| Pfam | PF00023;PF12796; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000169018-FEM1B/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| COPS6 | Biogrid, Bioplex | true |
| CUL2 | Biogrid, Bioplex | true |
| HIF1AN | Intact, Biogrid | true |
| PPM1F | Intact, Biogrid | true |
| BEX2 | Biogrid | false |
| COPS3 | Bioplex | false |
| COPS5 | Biogrid | false |
| COPS8 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

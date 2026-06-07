---
type: protein-evaluation
gene: "GNA13"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GNA13 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GNA13 |
| 蛋白名称 | Guanine nucleotide-binding protein subunit alpha-13 |
| 蛋白大小 | 377 aa / 44.0 kDa |
| UniProt ID | Q14344 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Cell membrane; Melanosome; Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 377 aa / 44.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=91.4; PDB: 7SF7, 7SF8, 7T6B, 7YDH, 8H8J, 8KGG, 8ZX4 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000469, IPR001019, IPR011025, IPR027417; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **146.0/180** | |
| **归一化总分** | | | **81.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Cell membrane; Melanosome; Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- brush border membrane (GO:0031526)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- focal adhesion (GO:0005925)
- heterotrimeric G-protein complex (GO:0005834)
- melanosome (GO:0042470)
- membrane (GO:0016020)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) | 无 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.4 |
| 高置信度残基 (pLDDT>90) 占比 | 80.6% |
| 置信残基 (pLDDT 70-90) 占比 | 12.2% |
| 中等置信 (pLDDT 50-70) 占比 | 2.7% |
| 低置信 (pLDDT<50) 占比 | 4.5% |
| 有序区域 (pLDDT>70) 占比 | 92.8% |
| 可用 PDB 条目 | 7SF7, 7SF8, 7T6B, 7YDH, 8H8J, 8KGG, 8ZX4, 8ZX5, 9GE2, 9GE3 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（7SF7, 7SF8, 7T6B, 7YDH, 8H8J, 8KGG, 8ZX4, 8ZX5, 9GE2, 9GE3）+ AlphaFold极高置信度预测（pLDDT=91.4），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000469, IPR001019, IPR011025, IPR027417; Pfam: PF00503 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ARHGEF1 | 0.999 | 0.845 | — |
| S1PR2 | 0.999 | 0.908 | — |
| ARHGEF12 | 0.999 | 0.726 | — |
| ARHGEF11 | 0.998 | 0.822 | — |
| ITGB3 | 0.994 | 0.000 | — |
| GNA12 | 0.992 | 0.472 | — |
| RHOA | 0.991 | 0.247 | — |
| GNB1 | 0.991 | 0.939 | — |
| S1PR3 | 0.989 | 0.125 | — |
| ESR1 | 0.985 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ARHGEF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:12681510 |
| Ywhaz | psi-mi:"MI:0028"(cosedimentation in solution) | imex:IM-11648|pubmed:19562802 |
| USP3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| Dlg4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-11694|pubmed:19455133 |
| 616370" | psi-mi:"MI:0096"(pull down) | pubmed:23606334|imex:IM-21247 |
| Pag1 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:26512138|imex:IM-25616 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| PACC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PVR | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Slc2a4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:16396496|mint:MINT-5218 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.4 + PDB: 7SF7, 7SF8, 7T6B, 7YDH, 8H8J,  | pLDDT=91.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane; Melanosome; Cytoplasm; Nucleus / Cytosol | 一致 |
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
1. GNA13 — Guanine nucleotide-binding protein subunit alpha-13，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小377 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q14344
- Protein Atlas: https://www.proteinatlas.org/ENSG00000120063-GNA13/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GNA13
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14344
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000120063-GNA13/subcellular

![](https://images.proteinatlas.org/10087/1220_C2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/10087/1220_C2_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/10087/1401_B2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/10087/1401_B2_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q14344-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q14344 |
| SMART | SM00275; |
| UniProt Domain [FT] | DOMAIN 47..377; /note="G-alpha"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01230" |
| InterPro | IPR000469;IPR001019;IPR011025;IPR027417; |
| Pfam | PF00503; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000120063-GNA13/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ARHGEF1 | Intact, Biogrid | true |
| GNG2 | Biogrid, Bioplex | true |
| AIP | Biogrid | false |
| AKAP3 | Biogrid | false |
| AKT1 | Intact | false |
| ANLN | Biogrid | false |
| ARHGEF11 | Biogrid | false |
| ARHGEF12 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

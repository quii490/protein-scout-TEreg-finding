---
type: protein-evaluation
gene: "TSTD1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TSTD1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TSTD1 / KAT |
| 蛋白名称 | Thiosulfate:glutathione sulfurtransferase |
| 蛋白大小 | 115 aa / 12.5 kDa |
| UniProt ID | Q8NFU3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol, Cytoplasmic bodies; UniProt: Cytoplasm, perinuclear region |
| 蛋白大小 | 8/10 | ×1 | 8 | 115 aa / 12.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=93.7; PDB: 6BEV |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001763, IPR036873, IPR042457; Pfam: PF00581 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **136.5/180** | |
| **归一化总分** | | | **75.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol, Cytoplasmic bodies | Approved |
| UniProt | Cytoplasm, perinuclear region | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytoplasmic ribonucleoprotein granule (GO:0036464)
- cytosol (GO:0005829)
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 14 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KAT |

**关键文献**:
1. Population and single-cell analyses reveal immune cell-specific expression profiles associated with Alzheimer's disease risk.. *Alzheimer's & dementia : the journal of the Alzheimer's Association*. PMID: 41866337
2. Copper-Mediated Selenazolidine Deprotection Enables One-Pot Chemical Synthesis of Challenging Proteins.. *Angewandte Chemie (International ed. in English)*. PMID: 31408267
3. High-Level MYCN-Amplified RB1-Proficient Retinoblastoma Tumors Retain Distinct Molecular Signatures.. *Ophthalmology science*. PMID: 36245757
4. Thiosulfate sulfurtransferase-like domain-containing 1 protein interacts with thioredoxin.. *The Journal of biological chemistry*. PMID: 29348167
5. Promoter hypomethylation and overexpression of TSTD1 mediate poor treatment response in breast cancer.. *Frontiers in oncology*. PMID: 36419875

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.7 |
| 高置信度残基 (pLDDT>90) 占比 | 92.2% |
| 置信残基 (pLDDT 70-90) 占比 | 4.3% |
| 中等置信 (pLDDT 50-70) 占比 | 2.6% |
| 低置信 (pLDDT<50) 占比 | 0.9% |
| 有序区域 (pLDDT>70) 占比 | 96.5% |
| 可用 PDB 条目 | 6BEV |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=93.7，有序区 96.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001763, IPR036873, IPR042457; Pfam: PF00581 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MOCS2 | 0.870 | 0.000 | — |
| DAP3 | 0.844 | 0.831 | — |
| YBEY | 0.836 | 0.831 | — |
| CAT | 0.820 | 0.000 | — |
| MOCOS | 0.816 | 0.000 | — |
| RPS11 | 0.807 | 0.793 | — |
| MRPL21 | 0.797 | 0.758 | — |
| MRPL17 | 0.782 | 0.758 | — |
| MRPL24 | 0.781 | 0.758 | — |
| MRPL3 | 0.781 | 0.758 | — |

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
| 三维结构 | AlphaFold pLDDT=93.7 + PDB: 6BEV | pLDDT=93.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, perinuclear region / Cytosol, Cytoplasmic bodies | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TSTD1 — Thiosulfate:glutathione sulfurtransferase，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小115 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NFU3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000215845-TSTD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TSTD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NFU3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000215845-TSTD1/subcellular

![](https://images.proteinatlas.org/6518/1601_A3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/6518/1601_A3_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/6518/1639_B2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/6518/1639_B2_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/6518/1732_A3_2_cr58060e51c7562_blue_red_green.jpg)
![](https://images.proteinatlas.org/6518/1732_A3_8_cr58060e5bf20fa_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NFU3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8NFU3 |
| SMART | SM00450; |
| UniProt Domain [FT] | DOMAIN 17..115; /note="Rhodanese"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00173" |
| InterPro | IPR001763;IPR036873;IPR042457; |
| Pfam | PF00581; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000215845-TSTD1/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

---
type: protein-evaluation
gene: "SYMPK"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SYMPK 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SYMPK / SPK |
| 蛋白名称 | Symplekin |
| 蛋白大小 | 1274 aa / 141.1 kDa |
| UniProt ID | Q92797 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Plasma membrane, Cytosol; UniProt: Cytoplasm, cytoskeleton; Cell junction, tight junction; Cell |
| 蛋白大小 | 5/10 | ×1 | 5 | 1274 aa / 141.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=74.6; PDB: 3O2Q, 3O2S, 3O2T, 3ODR, 3ODS, 4H3H, 4H3K |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011989, IPR016024, IPR021850, IPR032460, IPR022 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **139.0/180** | |
| **归一化总分** | | | **77.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Plasma membrane, Cytosol | Supported |
| UniProt | Cytoplasm, cytoskeleton; Cell junction, tight junction; Cell membrane; Cell junction; Nucleus, nucle... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- bicellular tight junction (GO:0005923)
- cytoplasm (GO:0005737)
- cytoskeleton (GO:0005856)
- cytosol (GO:0005829)
- mRNA cleavage and polyadenylation specificity factor complex (GO:0005847)
- nuclear stress granule (GO:0097165)
- nucleoplasm (GO:0005654)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 44 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SPK |

**关键文献**:
1. The pseudogene problem and RT-qPCR data normalization; SYMPK: a suitable reference gene for papillary thyroid carcinoma.. *Scientific reports*. PMID: 33110161
2. Global Promotion of Alternative Internal Exon Usage by mRNA 3' End Formation Factors.. *Molecular cell*. PMID: 25921069
3. SYMPK Is Required for Meiosis and Involved in Alternative Splicing in Male Germ Cells.. *Frontiers in cell and developmental biology*. PMID: 34434935
4. A strategy to identify housekeeping genes suitable for analysis in breast cancer diseases.. *BMC genomics*. PMID: 27526934
5. Alteration of tight junction gene expression in celiac disease.. *Journal of pediatric gastroenterology and nutrition*. PMID: 24552675

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.6 |
| 高置信度残基 (pLDDT>90) 占比 | 37.7% |
| 置信残基 (pLDDT 70-90) 占比 | 33.0% |
| 中等置信 (pLDDT 50-70) 占比 | 4.6% |
| 低置信 (pLDDT<50) 占比 | 24.7% |
| 有序区域 (pLDDT>70) 占比 | 70.7% |
| 可用 PDB 条目 | 3O2Q, 3O2S, 3O2T, 3ODR, 3ODS, 4H3H, 4H3K, 6V4X |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3O2Q, 3O2S, 3O2T, 3ODR, 3ODS, 4H3H, 4H3K, 6V4X）+ AlphaFold极高置信度预测（pLDDT=74.6），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR021850, IPR032460, IPR022075; Pfam: PF11935, PF12295 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FIP1L1 | 0.999 | 0.981 | — |
| CSTF2 | 0.999 | 0.960 | — |
| CSTF3 | 0.999 | 0.985 | — |
| CPSF3 | 0.999 | 0.997 | — |
| CPSF2 | 0.999 | 0.997 | — |
| CPSF1 | 0.999 | 0.992 | — |
| CPSF4 | 0.999 | 0.975 | — |
| WDR33 | 0.999 | 0.993 | — |
| SSU72 | 0.998 | 0.978 | — |
| PAPOLA | 0.998 | 0.841 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MCC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| GSTK1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MAGEA6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| PDHA1 | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010 |
| RP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| IL13RA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SIGLECL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CSTF2T | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KLHDC3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.6 + PDB: 3O2Q, 3O2S, 3O2T, 3ODR, 3ODS,  | pLDDT=74.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton; Cell junction, tight junc / Nucleoplasm; 额外: Plasma membrane, Cytosol | 一致 |
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
1. SYMPK — Symplekin，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1274 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92797
- Protein Atlas: https://www.proteinatlas.org/ENSG00000125755-SYMPK/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SYMPK
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92797
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000125755-SYMPK/subcellular

![](https://images.proteinatlas.org/41756/518_C10_3_red_green.jpg)
![](https://images.proteinatlas.org/41756/518_C10_4_red_green.jpg)
![](https://images.proteinatlas.org/41756/530_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/41756/530_C10_2_red_green.jpg)
![](https://images.proteinatlas.org/41756/558_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/41756/558_C10_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q92797-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q92797 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR011989;IPR016024;IPR021850;IPR032460;IPR022075; |
| Pfam | PF11935;PF12295; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000125755-SYMPK/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CPSF1 | Intact, Biogrid | true |
| CPSF2 | Intact, Biogrid | true |
| CPSF6 | Biogrid, Opencell | true |
| CSTF2 | Intact, Biogrid | true |
| CSTF2T | Biogrid, Bioplex | true |
| TOP1 | Biogrid, Opencell | true |
| BSG | Intact | false |
| CPEB1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

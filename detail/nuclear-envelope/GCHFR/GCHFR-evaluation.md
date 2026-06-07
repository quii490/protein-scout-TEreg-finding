---
type: protein-evaluation
gene: "GCHFR"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GCHFR 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GCHFR / GFRP |
| 蛋白名称 | GTP cyclohydrolase 1 feedback regulatory protein |
| 蛋白大小 | 84 aa / 9.7 kDa |
| UniProt ID | P30047 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Nucleus membrane; Cytoplasm, cytosol |
| 蛋白大小 | 5/10 | ×1 | 5 | 84 aa / 9.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=97.9; PDB: 6Z80, 6Z85, 7ACC, 7AL9, 7ALA, 7ALB, 7ALC |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR036717, IPR009112; Pfam: PF06399 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 8 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **141.0/180** | |
| **归一化总分** | | | **78.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Nucleus membrane; Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- dendrite (GO:0030425)
- melanosome (GO:0042470)
- nuclear membrane (GO:0031965)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 47 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GFRP |

**关键文献**:
1. Integration of biobank-scale genetics and plasma proteomics reveals evidence for causal processes in asthma risk and heterogeneity.. *Cell genomics*. PMID: 40187354
2. Duodenal inflammation in common variable immunodeficiency has altered transcriptional response to viruses.. *The Journal of allergy and clinical immunology*. PMID: 36220400
3. Pet-1 Controls Tetrahydrobiopterin Pathway and Slc22a3 Transporter Genes in Serotonin Neurons.. *ACS chemical neuroscience*. PMID: 25642596
4. CpG methyl-seq and RNA-seq epigenomic and transcriptomic studies on the preventive effects of Moringa isothiocyanate in mouse epidermal JB6 cells induced by the tumor promoter TPA.. *The Journal of nutritional biochemistry*. PMID: 31030169
5. Multiomics Screening Identified CpG Sites and Genes That Mediate the Impact of Exposure to Environmental Chemicals on Cardiometabolic Traits.. *Epigenomes*. PMID: 39189255

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 97.9 |
| 高置信度残基 (pLDDT>90) 占比 | 97.6% |
| 置信残基 (pLDDT 70-90) 占比 | 2.4% |
| 中等置信 (pLDDT 50-70) 占比 | 0.0% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 100.0% |
| 可用 PDB 条目 | 6Z80, 6Z85, 7ACC, 7AL9, 7ALA, 7ALB, 7ALC, 7ALQ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6Z80, 6Z85, 7ACC, 7AL9, 7ALA, 7ALB, 7ALC, 7ALQ）+ AlphaFold极高置信度预测（pLDDT=97.9），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036717, IPR009112; Pfam: PF06399 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GCH1 | 0.998 | 0.968 | — |
| PTS | 0.712 | 0.000 | — |
| SPR | 0.707 | 0.000 | — |
| QDPR | 0.689 | 0.000 | — |
| PCBD1 | 0.653 | 0.000 | — |
| DNAJC12 | 0.558 | 0.000 | — |
| PAH | 0.516 | 0.000 | — |
| SPINK2 | 0.424 | 0.376 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GCH1 | psi-mi:"MI:0018"(two hybrid) | pubmed:16696853|imex:IM-20087 |
| OBSL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NEBL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EIF4G1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CBFB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DOCK11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| IRF2BP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PUSL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CAMKK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HBS1L | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 8，IntAct interactions: 15
- 调控相关比例: 1 / 8 = 12%

**评价**: STRING 8 个预测互作，IntAct 15 个实验互作。调控相关配体占比 12%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=97.9 + PDB: 6Z80, 6Z85, 7ACC, 7AL9, 7ALA,  | pLDDT=97.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus membrane; Cytoplasm, cytosol / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 8 + 15 interactions | 数据充分 |

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
1. GCHFR — GTP cyclohydrolase 1 feedback regulatory protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小84 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P30047
- Protein Atlas: https://www.proteinatlas.org/ENSG00000137880-GCHFR/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GCHFR
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P30047
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000137880-GCHFR/subcellular

![](https://images.proteinatlas.org/46258/1259_A1_4_red_green.jpg)
![](https://images.proteinatlas.org/46258/1259_A1_5_red_green.jpg)
![](https://images.proteinatlas.org/46258/566_D3_1_red_green.jpg)
![](https://images.proteinatlas.org/46258/566_D3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P30047-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P30047 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR036717;IPR009112; |
| Pfam | PF06399; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000137880-GCHFR/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

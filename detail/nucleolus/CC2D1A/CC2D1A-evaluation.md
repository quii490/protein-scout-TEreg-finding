---
type: protein-evaluation
gene: "CC2D1A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CC2D1A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CC2D1A / AKI1, LGD2 |
| 蛋白名称 | Coiled-coil and C2 domain-containing protein 1A |
| 蛋白大小 | 951 aa / 104.1 kDa |
| UniProt ID | Q6P1N0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nucleoli fibrillar center, Plasma membrane, Bas; UniProt: Cytoplasm; Nucleus; Cytoplasm, cytoskeleton, microtubule org |
| 蛋白大小 | 8/10 | ×1 | 8 | 951 aa / 104.1 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=70 篇 (≤80→4) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=73.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000008, IPR035892, IPR037772, IPR039725, IPR006 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **101.5/180** | |
| **归一化总分** | | | **56.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoli fibrillar center, Plasma membrane, Basal body | Supported |
| UniProt | Cytoplasm; Nucleus; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- ciliary basal body (GO:0036064)
- cytosol (GO:0005829)
- endosome membrane (GO:0010008)
- extracellular exosome (GO:0070062)
- fibrillar center (GO:0001650)
- glutamatergic synapse (GO:0098978)
- membrane (GO:0016020)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 70 |
| PubMed broad count | 100 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: AKI1, LGD2 |

**关键文献**:
1. The Freud-1/CC2D1A family: transcriptional regulators implicated in mental retardation.. *Journal of neuroscience research*. PMID: 17394259
2. The roles of CC2D1A and HTR1A gene expressions in autism spectrum disorders.. *Metabolic brain disease*. PMID: 26782176
3. Coiled-Coil and C2 Domain-Containing Protein 1A (CC2D1A) Promotes Chemotherapy Resistance in Ovarian Cancer.. *Frontiers in oncology*. PMID: 31632917
4. Autism-Related Cc2d1a Heterozygous Mice: Increased Levels of miRNAs Retained in DNA/RNA Hybrid Profiles (R-Loop).. *Biomolecules*. PMID: 39334949
5. CC2D1A, a DM14 and C2 domain protein, activates NF-kappaB through the canonical pathway.. *The Journal of biological chemistry*. PMID: 20529849

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.3 |
| 高置信度残基 (pLDDT>90) 占比 | 38.8% |
| 置信残基 (pLDDT 70-90) 占比 | 25.1% |
| 中等置信 (pLDDT 50-70) 占比 | 8.9% |
| 低置信 (pLDDT<50) 占比 | 27.1% |
| 有序区域 (pLDDT>70) 占比 | 63.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=73.3，有序区 63.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000008, IPR035892, IPR037772, IPR039725, IPR006608; Pfam: PF00168, PF21528 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CHMP4C | 0.932 | 0.408 | — |
| PRSS12 | 0.909 | 0.000 | — |
| CHMP4A | 0.867 | 0.230 | — |
| CHMP6 | 0.817 | 0.000 | — |
| CRBN | 0.802 | 0.000 | — |
| CHMP4B | 0.798 | 0.751 | — |
| VPS4A | 0.752 | 0.000 | — |
| VPS4B | 0.713 | 0.000 | — |
| CHMP5 | 0.704 | 0.000 | — |
| CHMP3 | 0.701 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| STK38L | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-26463|pubmed:30108113 |
| H2BC9 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| TSPAN3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CRYAB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SLC1A1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MRAP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Immt | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |
| CHMP4B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| CHMP4C | psi-mi:"MI:0018"(two hybrid) | imex:IM-24991|pubmed:16730941 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.3 + PDB: 无 | pLDDT=73.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Cytoplasm, cytoskeleton, micro / Cytosol; 额外: Nucleoli fibrillar center, Plasma mem | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CC2D1A — Coiled-coil and C2 domain-containing protein 1A，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小951 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 70 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6P1N0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000132024-CC2D1A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CC2D1A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6P1N0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000132024-CC2D1A/subcellular

![](https://images.proteinatlas.org/5436/2123_E3_19_blue_red_green.jpg)
![](https://images.proteinatlas.org/5436/2123_E3_42_blue_red_green.jpg)
![](https://images.proteinatlas.org/5436/2127_D3_19_blue_red_green.jpg)
![](https://images.proteinatlas.org/5436/2127_D3_59_blue_red_green.jpg)
![](https://images.proteinatlas.org/5436/2167_D5_52_blue_red_green.jpg)
![](https://images.proteinatlas.org/5436/2167_D5_66_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6P1N0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6P1N0 |
| SMART | SM00239;SM00685; |
| UniProt Domain [FT] | DOMAIN 637..771; /note="C2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00041" |
| InterPro | IPR000008;IPR035892;IPR037772;IPR039725;IPR006608; |
| Pfam | PF00168;PF21528; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000132024-CC2D1A/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CHMP4B | Intact, Biogrid | true |
| CAV1 | Biogrid | false |
| DCTN1 | Biogrid | false |
| NIN | Biogrid | false |
| NINL | Biogrid | false |
| PCM1 | Biogrid | false |
| SLC1A1 | Biogrid | false |
| SQSTM1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

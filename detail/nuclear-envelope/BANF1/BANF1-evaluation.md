---
type: protein-evaluation
gene: "BANF1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BANF1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BANF1 / BAF, BCRG1 |
| 蛋白名称 | Barrier-to-autointegration factor |
| 蛋白大小 | 89 aa / 10.1 kDa |
| UniProt ID | O75531 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Chromosome; Nucleus envelope; Cytoplasm |
| 蛋白大小 | 5/10 | ×1 | 5 | 89 aa / 10.1 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=71 篇 (≤80→4) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=96.8; PDB: 1CI4, 1QCK, 2BZF, 2EZX, 2EZY, 2EZZ, 2ODG |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR051387, IPR004122, IPR036617; Pfam: PF02961 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.0/180** | |
| **归一化总分** | | | **61.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus; Chromosome; Nucleus envelope; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- condensed chromosome (GO:0000793)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nuclear envelope (GO:0005635)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 71 |
| PubMed broad count | 215 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BAF, BCRG1 |

**关键文献**:
1. VRK1/BANF1/GLI1 Axis Regulates Tumor Development and Progression of Colorectal Cancer.. *International journal of biological sciences*. PMID: 40384864
2. Inhibition of tumor intrinsic BANF1 activates antitumor immune responses via cGAS-STING and enhances the efficacy of PD-1 blockade.. *Journal for immunotherapy of cancer*. PMID: 37620043
3. Decreased TMIGD1 aggravates colitis and intestinal barrier dysfunction via the BANF1-NF-κB pathway in Crohn's disease.. *BMC medicine*. PMID: 37542259
4. PYCR1, BANF1, and STARD8 Expression in Gastric Carcinoma: A Clinicopathologic, Prognostic, and Immunohistochemical Study.. *Applied immunohistochemistry & molecular morphology : AIMM*. PMID: 37982568
5. Barrier-to-Autointegration Factor 1 Protects against a Basal cGAS-STING Response.. *mBio*. PMID: 32156810

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 96.8 |
| 高置信度残基 (pLDDT>90) 占比 | 96.6% |
| 置信残基 (pLDDT 70-90) 占比 | 1.1% |
| 中等置信 (pLDDT 50-70) 占比 | 1.1% |
| 低置信 (pLDDT<50) 占比 | 1.1% |
| 有序区域 (pLDDT>70) 占比 | 97.7% |
| 可用 PDB 条目 | 1CI4, 1QCK, 2BZF, 2EZX, 2EZY, 2EZZ, 2ODG, 6GHD, 6RPR, 6UNT |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1CI4, 1QCK, 2BZF, 2EZX, 2EZY, 2EZZ, 2ODG, 6GHD, 6RPR, 6UNT）+ AlphaFold极高置信度预测（pLDDT=96.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051387, IPR004122, IPR036617; Pfam: PF02961 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EMD | 0.999 | 0.983 | — |
| SMARCA4 | 0.998 | 0.000 | — |
| LEMD3 | 0.998 | 0.303 | — |
| LMNA | 0.996 | 0.951 | — |
| TMPO | 0.967 | 0.623 | — |
| ACTL6A | 0.959 | 0.314 | — |
| H3C12 | 0.958 | 0.075 | — |
| H3-3B | 0.956 | 0.000 | — |
| H3-2 | 0.955 | 0.000 | — |
| H3-4 | 0.955 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CDK5RAP3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| HLA-B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| ATP6V1A | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:21674799|imex:IM-16565 |
| EMD | psi-mi:"MI:0397"(two hybrid array) | pubmed:25502805|imex:IM-26175| |
| SOD1 | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010 |
| VDAC1 | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010 |
| SDHA | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010 |
| SOAT1 | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010 |
| LMNA | psi-mi:"MI:0096"(pull down) | pubmed:29568061|imex:IM-26301 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=96.8 + PDB: 1CI4, 1QCK, 2BZF, 2EZX, 2EZY,  | pLDDT=96.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome; Nucleus envelope; Cytoplasm / Nucleoplasm; 额外: Cytosol | 一致 |
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
1. BANF1 — Barrier-to-autointegration factor，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小89 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 71 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75531
- Protein Atlas: https://www.proteinatlas.org/ENSG00000175334-BANF1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BANF1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75531
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000175334-BANF1/subcellular

![](https://images.proteinatlas.org/39242/857_A6_1_red_green.jpg)
![](https://images.proteinatlas.org/39242/857_A6_2_red_green.jpg)
![](https://images.proteinatlas.org/39242/867_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/39242/867_B1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O75531-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O75531 |
| SMART | SM01023; |
| UniProt Domain [FT] | DOMAIN 20..35; /note="HhH"; /evidence="ECO:0000269\|PubMed:10924106" |
| InterPro | IPR051387;IPR004122;IPR036617; |
| Pfam | PF02961; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000175334-BANF1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| EMD | Intact, Biogrid | true |
| HMGA1 | Biogrid, Opencell | true |
| LMNA | Biogrid, Opencell | true |
| NUMA1 | Biogrid, Opencell | true |
| PARP1 | Biogrid, Opencell | true |
| ACE2 | Biogrid | false |
| BANF2 | Biogrid | false |
| BRD4 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

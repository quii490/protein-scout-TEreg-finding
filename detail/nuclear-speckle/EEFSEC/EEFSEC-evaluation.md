---
type: protein-evaluation
gene: "EEFSEC"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EEFSEC 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EEFSEC / SELB |
| 蛋白名称 | Selenocysteine-specific elongation factor |
| 蛋白大小 | 596 aa / 65.3 kDa |
| UniProt ID | P57772 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear bodies; 额外: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 596 aa / 65.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=33 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=79.8; PDB: 5IZK, 5IZL, 5IZM, 7ZJW |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR049394, IPR049393, IPR050055, IPR004161, IPR027 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.0/180** | |
| **归一化总分** | | | **72.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear bodies; 额外: Cytosol | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)
- ribonucleoprotein complex (GO:1990904)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 33 |
| PubMed broad count | 50 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SELB |

**关键文献**:
1. On elongation factor eEFSec, its role and mechanism during selenium incorporation into nascent selenoproteins.. *Biochimica et biophysica acta. General subjects*. PMID: 29555379
2. Identifying compound heterozygous variants in the EEFSEC gene linked to progressive cerebellar atrophy.. *Journal of neurodevelopmental disorders*. PMID: 40652205
3. Functional characterization of promoter regions in selenoprotein synthesis-relevant genes (sbp2, eefsec and sepsecs) and their selenium-dependent regulation in yellow catfish Pelteobagrus fulvidraco.. *Biochimica et biophysica acta. Gene regulatory mechanisms*. PMID: 40618995
4. Structure of the mammalian ribosome as it decodes the selenocysteine UGA codon.. *Science (New York, N.Y.)*. PMID: 35709277
5. A novel protein domain induces high affinity selenocysteine insertion sequence binding and elongation factor recruitment.. *The Journal of biological chemistry*. PMID: 18948268

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.8 |
| 高置信度残基 (pLDDT>90) 占比 | 28.0% |
| 置信残基 (pLDDT 70-90) 占比 | 53.5% |
| 中等置信 (pLDDT 50-70) 占比 | 9.1% |
| 低置信 (pLDDT<50) 占比 | 9.4% |
| 有序区域 (pLDDT>70) 占比 | 81.5% |
| 可用 PDB 条目 | 5IZK, 5IZL, 5IZM, 7ZJW |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（5IZK, 5IZL, 5IZM, 7ZJW）+ AlphaFold高质量预测（pLDDT=79.8），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR049394, IPR049393, IPR050055, IPR004161, IPR027417; Pfam: PF21131, PF21208, PF00009 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SECISBP2 | 0.999 | 0.801 | — |
| FAU | 0.997 | 0.993 | — |
| PSTK | 0.993 | 0.000 | — |
| RPS3 | 0.989 | 0.961 | — |
| RPS6 | 0.985 | 0.948 | — |
| RPS11 | 0.983 | 0.953 | — |
| RPS15 | 0.981 | 0.955 | — |
| RPS28 | 0.979 | 0.946 | — |
| RPS18 | 0.978 | 0.954 | — |
| RPS19 | 0.978 | 0.949 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SET | psi-mi:"MI:0004"(affinity chromatography technolog | imex:IM-11935|pubmed:17309103 |
| eef1a1o.S | psi-mi:"MI:0029"(cosedimentation through density g | pubmed:20174651|imex:IM-17228 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| Gspt1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| SOX17 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| HNRNPU | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| PARD6B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Rpl35 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Rrbp1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| HSPA8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.8 + PDB: 5IZK, 5IZL, 5IZM, 7ZJW | pLDDT=79.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm, Nuclear bodies; 额外: Cytosol | 一致 |
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
1. EEFSEC — Selenocysteine-specific elongation factor，非常新颖，仅有少数基础研究。
2. 蛋白大小596 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 33 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P57772
- Protein Atlas: https://www.proteinatlas.org/ENSG00000132394-EEFSEC/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EEFSEC
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P57772
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000132394-EEFSEC/subcellular

![](https://images.proteinatlas.org/35795/2154_F1_5_red_green.jpg)
![](https://images.proteinatlas.org/35795/2154_F1_6_red_green.jpg)
![](https://images.proteinatlas.org/35795/380_E1_1_red_green.jpg)
![](https://images.proteinatlas.org/35795/380_E1_2_red_green.jpg)
![](https://images.proteinatlas.org/35795/382_E1_3_red_green.jpg)
![](https://images.proteinatlas.org/35795/382_E1_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P57772-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P57772 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 5..217; /note="tr-type G"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01059" |
| InterPro | IPR049394;IPR049393;IPR050055;IPR004161;IPR027417;IPR000795;IPR009000; |
| Pfam | PF21131;PF21208;PF00009;PF03144; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000132394-EEFSEC/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

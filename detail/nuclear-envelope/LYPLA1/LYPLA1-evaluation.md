---
type: protein-evaluation
gene: "LYPLA1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LYPLA1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LYPLA1 / APT1, LPL1 |
| 蛋白名称 | Acyl-protein thioesterase 1 |
| 蛋白大小 | 230 aa / 24.7 kDa |
| UniProt ID | O75608 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm; Cell membrane; Nucleus membrane; Endoplasmic reti |
| 蛋白大小 | 10/10 | ×1 | 10 | 230 aa / 24.7 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=53 篇 (≤60→6) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=95.5; PDB: 1FJ2, 5SYM, 6QGN, 6QGO, 6QGQ, 6QGS |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR029058, IPR050565, IPR003140; Pfam: PF02230 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.0/180** | |
| **归一化总分** | | | **70.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | Cytoplasm; Cell membrane; Nucleus membrane; Endoplasmic reticulum | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- endoplasmic reticulum (GO:0005783)
- extracellular exosome (GO:0070062)
- mitochondrion (GO:0005739)
- nuclear membrane (GO:0031965)
- nucleoplasm (GO:0005654)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 53 |
| PubMed broad count | 118 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: APT1, LPL1 |

**关键文献**:
1. Hypoxia-induced GPCPD1 depalmitoylation triggers mitophagy via regulating PRKN-mediated ubiquitination of VDAC1.. *Autophagy*. PMID: 36803235
2. Protein depalmitoylases.. *Critical reviews in biochemistry and molecular biology*. PMID: 29239216
3. Hepatocyte CD36 modulates UBQLN1-mediated proteasomal degradation of autophagic SNARE proteins contributing to septic liver injury.. *Autophagy*. PMID: 37014234
4. A defective lysophosphatidic acid-autophagy axis increases miscarriage risk by restricting decidual macrophage residence.. *Autophagy*. PMID: 35220880
5. Optimization and characterization of a triazole urea inhibitor for alpha/beta hydrolase domain-containing protein 11 (ABHD11): anti-probe for LYPLA1/LYPLA2 dual inhibitor ML211.. **. PMID: 23658953

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 95.5 |
| 高置信度残基 (pLDDT>90) 占比 | 93.5% |
| 置信残基 (pLDDT 70-90) 占比 | 3.0% |
| 中等置信 (pLDDT 50-70) 占比 | 0.9% |
| 低置信 (pLDDT<50) 占比 | 2.6% |
| 有序区域 (pLDDT>70) 占比 | 96.5% |
| 可用 PDB 条目 | 1FJ2, 5SYM, 6QGN, 6QGO, 6QGQ, 6QGS |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1FJ2, 5SYM, 6QGN, 6QGO, 6QGQ, 6QGS）+ AlphaFold极高置信度预测（pLDDT=95.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029058, IPR050565, IPR003140; Pfam: PF02230 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GPCPD1 | 0.951 | 0.000 | — |
| PLB1 | 0.936 | 0.000 | — |
| LPCAT3 | 0.935 | 0.000 | — |
| PLA2G15 | 0.932 | 0.000 | — |
| PNPLA6 | 0.928 | 0.000 | — |
| LCAT | 0.923 | 0.000 | — |
| MBOAT2 | 0.913 | 0.000 | — |
| PNPLA7 | 0.910 | 0.000 | — |
| LPCAT4 | 0.909 | 0.000 | — |
| MBOAT1 | 0.901 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| IKBKE | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| VHL | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| VCAM1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-17358|pubmed:22623428 |
| Slc2a4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:16396496|mint:MINT-5218 |
| NS | psi-mi:"MI:0018"(two hybrid) | imex:IM-13585|pubmed:20064372 |
| PRSS35 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| GOLGA2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| HSCB | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28380382|imex:IM-25655 |
| GTF2E2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TRIM11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=95.5 + PDB: 1FJ2, 5SYM, 6QGN, 6QGO, 6QGQ,  | pLDDT=95.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Cell membrane; Nucleus membrane; Endopl / Nucleoplasm, Cytosol | 一致 |
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
1. LYPLA1 — Acyl-protein thioesterase 1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小230 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 53 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75608
- Protein Atlas: https://www.proteinatlas.org/ENSG00000120992-LYPLA1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LYPLA1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75608
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000120992-LYPLA1/subcellular

![](https://images.proteinatlas.org/63151/1223_A8_1_red_green.jpg)
![](https://images.proteinatlas.org/63151/1223_A8_2_red_green.jpg)
![](https://images.proteinatlas.org/63151/1246_A5_2_red_green.jpg)
![](https://images.proteinatlas.org/63151/1246_A5_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O75608-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O75608 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029058;IPR050565;IPR003140; |
| Pfam | PF02230; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000120992-LYPLA1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| GOLGA2 | Intact | false |
| SFMBT2 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

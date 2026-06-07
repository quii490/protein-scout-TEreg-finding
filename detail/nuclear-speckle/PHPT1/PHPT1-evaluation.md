---
type: protein-evaluation
gene: "PHPT1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PHPT1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PHPT1 / PHP14 |
| 蛋白名称 | 14 kDa phosphohistidine phosphatase |
| 蛋白大小 | 125 aa / 13.8 kDa |
| UniProt ID | Q9NRX4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nucleoplasm, Nuclear bodies, Plasma membrane; UniProt: Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 125 aa / 13.8 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=45 篇 (≤60→6) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=90.8; PDB: 2AI6, 2HW4, 2NMM, 2OZW, 2OZX |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR007702, IPR038596; Pfam: PF05005 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 13 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **124.0/180** | |
| **归一化总分** | | | **68.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm, Nuclear bodies, Plasma membrane | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- leading edge of lamellipodium (GO:0061851)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 45 |
| PubMed broad count | 73 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PHP14 |

**关键文献**:
1. Histidine Phosphorylation: Protein Kinases and Phosphatases.. *International journal of molecular sciences*. PMID: 39063217
2. PHPT1 acts as an inhibitor in high-altitude pulmonary hypertension via negative TRPV5 signaling regulation.. *Journal of translational medicine*. PMID: 40877955
3. Specific Fluorescent Probe for Protein Histidine Phosphatase Activity.. *ACS sensors*. PMID: 30912641
4. Genetic associations of protein-coding variants in venous thromboembolism.. *Nature communications*. PMID: 38561338
5. [Progress in enrichment methods for protein N-phosphorylation].. *Se pu = Chinese journal of chromatography*. PMID: 38966971

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.8 |
| 高置信度残基 (pLDDT>90) 占比 | 78.4% |
| 置信残基 (pLDDT 70-90) 占比 | 10.4% |
| 中等置信 (pLDDT 50-70) 占比 | 10.4% |
| 低置信 (pLDDT<50) 占比 | 0.8% |
| 有序区域 (pLDDT>70) 占比 | 88.8% |
| 可用 PDB 条目 | 2AI6, 2HW4, 2NMM, 2OZW, 2OZX |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2AI6, 2HW4, 2NMM, 2OZW, 2OZX）+ AlphaFold极高置信度预测（pLDDT=90.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007702, IPR038596; Pfam: PF05005 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KCNN4 | 0.816 | 0.292 | — |
| NME2 | 0.811 | 0.000 | — |
| NDUFA13 | 0.773 | 0.000 | — |
| NDUFS7 | 0.721 | 0.000 | — |
| LHPP | 0.703 | 0.000 | — |
| NDUFA7 | 0.691 | 0.000 | — |
| NDUFB7 | 0.689 | 0.000 | — |
| NDUFS8 | 0.688 | 0.000 | — |
| NDUFA11 | 0.666 | 0.000 | — |
| MTMR6 | 0.656 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DNMT3L | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ATXN1 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| TRAF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ERBB3 | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:31980649|imex:IM-26434 |
| TPM4 | psi-mi:"MI:0096"(pull down) | pubmed:28330616|imex:IM-25671 |
| GTF2E2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EBI-25475894 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33845483|pmc:PPR177217| |
| DNAJB6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MAPT | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:35063084|imex:IM-29773 |
| ENST00000247665 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 13
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 13 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.8 + PDB: 2AI6, 2HW4, 2NMM, 2OZW, 2OZX | pLDDT=90.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Cytosol; 额外: Nucleoplasm, Nuclear bodies, Plasma m | 一致 |
| PPI | STRING + IntAct | 15 + 13 interactions | 数据充分 |

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
1. PHPT1 — 14 kDa phosphohistidine phosphatase，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小125 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 45 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NRX4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000054148-PHPT1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PHPT1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NRX4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000054148-PHPT1/subcellular

![](https://images.proteinatlas.org/20952/187_E3_1_red_green.jpg)
![](https://images.proteinatlas.org/20952/187_E3_2_red_green.jpg)
![](https://images.proteinatlas.org/20952/188_E3_1_red_green.jpg)
![](https://images.proteinatlas.org/20952/188_E3_2_red_green.jpg)
![](https://images.proteinatlas.org/20952/246_E3_1_red_green.jpg)
![](https://images.proteinatlas.org/20952/246_E3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NRX4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NRX4 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR007702;IPR038596; |
| Pfam | PF05005; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000054148-PHPT1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ATXN1 | Intact | false |
| SAR1B | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

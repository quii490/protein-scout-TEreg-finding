---
type: protein-evaluation
gene: "N4BP2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## N4BP2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | N4BP2 / B3BP, KIAA1413 |
| 蛋白名称 | NEDD4-binding protein 2 |
| 蛋白大小 | 1770 aa / 198.8 kDa |
| UniProt ID | Q86UW6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Plasma membrane, Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 5/10 | ×1 | 5 | 1770 aa / 198.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=48.7; PDB: 2D9I, 2VKC, 3BHB, 3FAU |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003892, IPR013899, IPR056718, IPR056719, IPR056 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **114.5/180** | |
| **归一化总分** | | | **63.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Plasma membrane, Cytosol | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 22 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: B3BP, KIAA1413 |

**关键文献**:
1. Surface Proteome of Extracellular Vesicles and Correlation Analysis Reveal Breast Cancer Biomarkers.. *Cancers*. PMID: 38339272
2. Analysing the relationship between lncRNA and protein-coding gene and the role of lncRNA as ceRNA in pulmonary fibrosis.. *Journal of cellular and molecular medicine*. PMID: 24702795
3. PMEL is a predictive biomarker for mTORC1 inhibitor treatment of renal angiomyolipoma in tuberous sclerosis complex patients.. *Heliyon*. PMID: 39170496
4. Haplotype of gene Nedd4 binding protein 2 associated with sporadic nasopharyngeal carcinoma in the Southern Chinese population.. *Journal of translational medicine*. PMID: 17626640
5. A large structural variant collection in Holstein cattle and associated database for variant discovery, characterization, and application.. *BMC genomics*. PMID: 39350025

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 48.7 |
| 高置信度残基 (pLDDT>90) 占比 | 15.0% |
| 置信残基 (pLDDT 70-90) 占比 | 13.6% |
| 中等置信 (pLDDT 50-70) 占比 | 5.1% |
| 低置信 (pLDDT<50) 占比 | 66.3% |
| 有序区域 (pLDDT>70) 占比 | 28.6% |
| 可用 PDB 条目 | 2D9I, 2VKC, 3BHB, 3FAU |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=48.7），有序残基占 28.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003892, IPR013899, IPR056718, IPR056719, IPR056720; Pfam: PF13671, PF08590, PF25124 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NDUFB7 | 0.703 | 0.483 | — |
| BCL3 | 0.675 | 0.295 | — |
| PLXNA4 | 0.591 | 0.000 | — |
| ZNF567 | 0.553 | 0.000 | — |
| PDS5A | 0.549 | 0.000 | — |
| NDUFA6 | 0.536 | 0.483 | — |
| NDUFS6 | 0.532 | 0.483 | — |
| NDUFA5 | 0.530 | 0.471 | — |
| CHD9 | 0.529 | 0.052 | — |
| NDUFS2 | 0.527 | 0.471 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| hrpA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| dapG2 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| TOLLIP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| ptsI | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ENSP00000261435.6 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| CAMK2D | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:29426014|imex:IM-26302| |
| PLEC | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| FAM136A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FAM98A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RPGRIP1L | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=48.7 + PDB: 2D9I, 2VKC, 3BHB, 3FAU | pLDDT=48.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm; 额外: Plasma membrane, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. N4BP2 — NEDD4-binding protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1770 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=48.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86UW6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000078177-N4BP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=N4BP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86UW6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000078177-N4BP2/subcellular

![](https://images.proteinatlas.org/42607/800_B9_1_red_green.jpg)
![](https://images.proteinatlas.org/42607/800_B9_2_red_green.jpg)
![](https://images.proteinatlas.org/42607/845_B9_1_red_green.jpg)
![](https://images.proteinatlas.org/42607/845_B9_2_red_green.jpg)
![](https://images.proteinatlas.org/72549/1779_F7_3_red_green.jpg)
![](https://images.proteinatlas.org/72549/1779_F7_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86UW6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q86UW6 |
| SMART | SM01162;SM00463; |
| UniProt Domain [FT] | DOMAIN 46..89; /note="CUE"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00468"; DOMAIN 1691..1770; /note="Smr"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00321" |
| InterPro | IPR003892;IPR013899;IPR056718;IPR056719;IPR056720;IPR052772;IPR041801;IPR027417;IPR002625;IPR036063;IPR009060; |
| Pfam | PF13671;PF08590;PF25124;PF25125;PF25126;PF01713; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000078177-N4BP2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DYNLL1 | Biogrid, Opencell | true |
| DYNLL2 | Biogrid, Opencell | true |
| BCL3 | Biogrid | false |
| HNRNPAB | Biogrid | false |
| RTCB | Opencell | false |
| SF3B1 | Opencell | false |
| SF3B3 | Opencell | false |
| VPS35 | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

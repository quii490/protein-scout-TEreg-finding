---
type: protein-evaluation
gene: "CRK"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CRK — REJECTED (研究热度过高 (PubMed strict=1026，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CRK |
| 蛋白名称 | Adapter molecule crk |
| 蛋白大小 | 304 aa / 33.8 kDa |
| UniProt ID | P46108 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane; 额外: Nucleoplasm, Actin filaments, Basal bod; UniProt: Cytoplasm; Cell membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 304 aa / 33.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1026 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.8; PDB: 1JU5, 2DVJ, 2EYV, 2EYW, 2EYX, 2EYY, 2EYZ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR035458, IPR035457, IPR000980, IPR036860, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Nucleoplasm, Actin filaments, Basal body | Approved |
| UniProt | Cytoplasm; Cell membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- membrane (GO:0016020)
- neuromuscular junction (GO:0031594)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1026 |
| PubMed broad count | 2307 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Cysteine-rich receptor-like protein kinases: emerging regulators of plant stress responses.. *Trends in plant science*. PMID: 37105805
2. A novel OsCRK14-OsRLCK57-MAPK signaling module activates OsbZIP66 to confer drought resistance in rice.. *Molecular plant*. PMID: 40676839
3. Paxillin interactions.. *Journal of cell science*. PMID: 11069756
4. Crk and CrkL as Therapeutic Targets for Cancer Treatment.. *Cells*. PMID: 33801580
5. Genetic Variation and Ultrafiltration with Peritoneal Dialysis: A Genome-Wide Association Study.. *Journal of the American Society of Nephrology : JASN*. PMID: 40669005

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.8 |
| 高置信度残基 (pLDDT>90) 占比 | 2.0% |
| 置信残基 (pLDDT 70-90) 占比 | 62.2% |
| 中等置信 (pLDDT 50-70) 占比 | 13.2% |
| 低置信 (pLDDT<50) 占比 | 22.7% |
| 有序区域 (pLDDT>70) 占比 | 64.2% |
| 可用 PDB 条目 | 1JU5, 2DVJ, 2EYV, 2EYW, 2EYX, 2EYY, 2EYZ, 2MS4, 5UL6, 6ATV |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=69.8），有序残基占 64.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR035458, IPR035457, IPR000980, IPR036860, IPR036028; Pfam: PF00017, PF00018, PF07653 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ABL1 | 0.999 | 0.986 | — |
| DOCK1 | 0.999 | 0.904 | — |
| PXN | 0.999 | 0.752 | — |
| RAPGEF1 | 0.999 | 0.907 | — |
| BCAR1 | 0.999 | 0.928 | — |
| SRC | 0.999 | 0.733 | — |
| CBL | 0.999 | 0.930 | — |
| ELMO1 | 0.998 | 0.465 | — |
| EGFR | 0.997 | 0.846 | — |
| PTK2 | 0.997 | 0.778 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DOCK1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| "fl | psi-mi:"MI:0397"(two hybrid array) | pubmed:unassigned1513|imex:IM- |
| LUBEL | psi-mi:"MI:0397"(two hybrid array) | pubmed:unassigned1513|imex:IM- |
| Dmel\CG6280 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:37061542|imex:IM-28761 |
| ey | psi-mi:"MI:0397"(two hybrid array) | pubmed:37061542|imex:IM-28761 |
| ATPsyndelta | psi-mi:"MI:0397"(two hybrid array) | pubmed:37061542|imex:IM-28761 |
| Grx5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:37061542|imex:IM-28761 |
| fok | psi-mi:"MI:0397"(two hybrid array) | pubmed:37061542|imex:IM-28761 |
| Aps | psi-mi:"MI:0397"(two hybrid array) | pubmed:37061542|imex:IM-28761 |
| miple1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:37061542|imex:IM-28761 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.8 + PDB: 1JU5, 2DVJ, 2EYV, 2EYW, 2EYX,  | pLDDT=69.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Cell membrane / Plasma membrane; 额外: Nucleoplasm, Actin filaments, | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CRK — Adapter molecule crk，研究基础较多，新颖性有限。
2. 蛋白大小304 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1026 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=69.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1026 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P46108
- Protein Atlas: https://www.proteinatlas.org/ENSG00000167193-CRK/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CRK
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P46108
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000167193-CRK/subcellular

![](https://images.proteinatlas.org/68087/1304_C12_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/68087/1304_C12_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/68087/1320_B10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/68087/1320_B10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/68087/1323_C12_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/68087/1323_C12_5_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P46108-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P46108 |
| SMART | SM00252;SM00326; |
| UniProt Domain [FT] | DOMAIN 13..118; /note="SH2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00191"; DOMAIN 132..192; /note="SH3 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00192"; DOMAIN 235..296; /note="SH3 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00192" |
| InterPro | IPR035458;IPR035457;IPR000980;IPR036860;IPR036028;IPR001452;IPR051184; |
| Pfam | PF00017;PF00018;PF07653; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000167193-CRK/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ABL1 | Intact, Biogrid | true |
| ABL2 | Intact, Biogrid | true |
| ARHGAP32 | Intact, Biogrid | true |
| ASAP1 | Intact, Biogrid | true |
| ASAP3 | Intact, Biogrid | true |
| ASB9 | Intact, Biogrid | true |
| ATXN1 | Intact, Biogrid | true |
| BCAR1 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

---
type: protein-evaluation
gene: "ABCA1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ABCA1 — REJECTED (研究热度过高 (PubMed strict=3196，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ABCA1 / ABC1, CERP |
| 蛋白名称 | Phospholipid-transporting ATPase ABCA1 |
| 蛋白大小 | 2261 aa / 254.3 kDa |
| UniProt ID | O95477 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Plasma membrane; 额外: Golgi apparatus; UniProt: Cell membrane; Endosome |
| 蛋白大小 | 2/10 | ×1 | 2 | 2261 aa / 254.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=3196 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=73.2; PDB: 5XJY, 7ROQ, 7TBW, 7TBY, 7TBZ, 7TC0, 7TDT |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003593, IPR013525, IPR003439, IPR017871, IPR026 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **74.0/180** | |
| **归一化总分** | | | **41.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Golgi apparatus | Supported |
| UniProt | Cell membrane; Endosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- basolateral plasma membrane (GO:0016323)
- endocytic vesicle (GO:0030139)
- endoplasmic reticulum membrane (GO:0005789)
- endosome (GO:0005768)
- external side of plasma membrane (GO:0009897)
- Golgi apparatus (GO:0005794)
- intracellular vesicle (GO:0097708)
- membrane raft (GO:0045121)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3196 |
| PubMed broad count | 5328 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ABC1, CERP |

**关键文献**:
1. ABCA1 and atherosclerosis.. *Vascular medicine (London, England)*. PMID: 16013195
2. History and Development of ABCA1.. *Current problems in cardiology*. PMID: 37595859
3. Is ABCA1 a lipid transfer protein?. *Journal of lipid research*. PMID: 29305383
4. Role of ABCA1 in Cardiovascular Disease.. *Journal of personalized medicine*. PMID: 35743794
5. ABCA1 and ABCG1 as potential therapeutic targets for the prevention of atherosclerosis.. *Journal of pharmacological sciences*. PMID: 35063134

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.2 |
| 高置信度残基 (pLDDT>90) 占比 | 5.7% |
| 置信残基 (pLDDT 70-90) 占比 | 61.3% |
| 中等置信 (pLDDT 50-70) 占比 | 24.3% |
| 低置信 (pLDDT<50) 占比 | 8.7% |
| 有序区域 (pLDDT>70) 占比 | 67.0% |
| 可用 PDB 条目 | 5XJY, 7ROQ, 7TBW, 7TBY, 7TBZ, 7TC0, 7TDT |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（5XJY, 7ROQ, 7TBW, 7TBY, 7TBZ, 7TC0, 7TDT）+ AlphaFold极高置信度预测（pLDDT=73.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003593, IPR013525, IPR003439, IPR017871, IPR026082; Pfam: PF12698, PF00005, PF23321 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| APOA1 | 0.999 | 0.697 | — |
| NR1H2 | 0.991 | 0.628 | — |
| APOE | 0.980 | 0.000 | — |
| NR1H3 | 0.967 | 0.049 | — |
| XPR1 | 0.940 | 0.000 | — |
| SREBF2 | 0.940 | 0.060 | — |
| SCARB1 | 0.934 | 0.000 | — |
| RXRA | 0.916 | 0.049 | — |
| LCAT | 0.912 | 0.000 | — |
| SREBF1 | 0.905 | 0.060 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SNTB2 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:16192269|imex:IM-20073 |
| SNTA1 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:16192269|imex:IM-20073 |
| SNTB1 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:16192269|imex:IM-20073 |
| UTRN | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:16192269|imex:IM-20073 |
| DTNB | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:16192269|imex:IM-20073 |
| DLG3 | psi-mi:"MI:0081"(peptide array) | pubmed:16192269|imex:IM-20073 |
| ARHGEF11 | psi-mi:"MI:0081"(peptide array) | pubmed:16192269|imex:IM-20073 |
| Lin7c | psi-mi:"MI:0081"(peptide array) | pubmed:16192269|imex:IM-20073 |
| Lin7a | psi-mi:"MI:0081"(peptide array) | pubmed:16192269|imex:IM-20073 |
| ARHGEF12 | psi-mi:"MI:0081"(peptide array) | pubmed:16192269|imex:IM-20073 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.2 + PDB: 5XJY, 7ROQ, 7TBW, 7TBY, 7TBZ,  | pLDDT=73.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane; Endosome / Plasma membrane; 额外: Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. ABCA1 — Phospholipid-transporting ATPase ABCA1，研究基础较多，新颖性有限。
2. 蛋白大小2261 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 3196 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 3196 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O95477
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165029-ABCA1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ABCA1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95477
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (supported)。来源: https://www.proteinatlas.org/ENSG00000165029-ABCA1/subcellular

![](https://images.proteinatlas.org/75201/1816_D4_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/75201/1816_D4_9_blue_red_green.jpg)
![](https://images.proteinatlas.org/75201/2154_H11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/75201/2154_H11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/75201/2225_G4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/75201/2225_G4_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O95477-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O95477 |
| SMART | SM00382; |
| UniProt Domain [FT] | DOMAIN 899..1131; /note="ABC transporter 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00434"; DOMAIN 1912..2144; /note="ABC transporter 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00434" |
| InterPro | IPR003593;IPR013525;IPR003439;IPR017871;IPR026082;IPR027417;IPR056264; |
| Pfam | PF12698;PF00005;PF23321; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000165029-ABCA1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| APOA1 | Intact, Biogrid | true |
| SNTB2 | Intact, Biogrid | true |
| ABCA12 | Intact | false |
| CANX | Intact | false |
| CDC42 | Intact | false |
| COPS2 | Biogrid | false |
| FADD | Biogrid | false |
| FLOT1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

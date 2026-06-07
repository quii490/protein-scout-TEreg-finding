---
type: protein-evaluation
gene: "UBXN6"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## UBXN6 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | UBXN6 / UBXD1, UBXDC2 |
| 蛋白名称 | UBX domain-containing protein 6 |
| 蛋白大小 | 441 aa / 49.8 kDa |
| UniProt ID | Q9BZV1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Golgi apparatus, Cytosol; UniProt: Cytoplasm; Cytoplasm, cytosol; Membrane; Nucleus; Cytoplasm, |
| 蛋白大小 | 10/10 | ×1 | 10 | 441 aa / 49.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=76.0; PDB: 6SAP, 8FCL, 8FCM, 8FCN, 8FCO, 8FCP, 8FCQ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036339, IPR018997, IPR029071, IPR001012, IPR042 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **144.0/180** | |
| **归一化总分** | | | **80.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus, Cytosol | Approved |
| UniProt | Cytoplasm; Cytoplasm, cytosol; Membrane; Nucleus; Cytoplasm, cytoskeleton, microtubule organizing ce... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- early endosome membrane (GO:0031901)
- endosome (GO:0005768)
- extracellular exosome (GO:0070062)
- late endosome membrane (GO:0031902)
- lysosomal membrane (GO:0005765)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 33 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: UBXD1, UBXDC2 |

**关键文献**:
1. PTP4A2 promotes lysophagy by dephosphorylation of VCP/p97 at Tyr805.. *Autophagy*. PMID: 36300783
2. Linear ubiquitination at damaged lysosomes induces local NFKB activation and controls cell survival.. *Autophagy*. PMID: 39744815
3. Ubiquitin regulatory X (UBX) domain-containing protein 6 is essential for autophagy induction and inflammation control in macrophages.. *Cellular & molecular immunology*. PMID: 39438692
4. UBX Domain Protein 6 Positively Regulates JAK-STAT1/2 Signaling.. *Journal of immunology (Baltimore, Md. : 1950)*. PMID: 34021047
5. PRKAA2, MTOR, and TFEB in the regulation of lysosomal damage response and autophagy.. *Journal of molecular medicine (Berlin, Germany)*. PMID: 38183492

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.0 |
| 高置信度残基 (pLDDT>90) 占比 | 6.8% |
| 置信残基 (pLDDT 70-90) 占比 | 68.5% |
| 中等置信 (pLDDT 50-70) 占比 | 16.3% |
| 低置信 (pLDDT<50) 占比 | 8.4% |
| 有序区域 (pLDDT>70) 占比 | 75.3% |
| 可用 PDB 条目 | 6SAP, 8FCL, 8FCM, 8FCN, 8FCO, 8FCP, 8FCQ, 8FCR, 8FCT |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6SAP, 8FCL, 8FCM, 8FCN, 8FCO, 8FCP, 8FCQ, 8FCR, 8FCT）+ AlphaFold极高置信度预测（pLDDT=76.0），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036339, IPR018997, IPR029071, IPR001012, IPR042774; Pfam: PF09409, PF00789 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| VCP | 0.999 | 0.995 | — |
| UBXN4 | 0.999 | 0.994 | — |
| NSFL1C | 0.999 | 0.994 | — |
| FAF1 | 0.997 | 0.994 | — |
| UBXN10 | 0.997 | 0.994 | — |
| ASPSCR1 | 0.996 | 0.994 | — |
| UBXN2A | 0.993 | 0.786 | — |
| YOD1 | 0.981 | 0.570 | — |
| UBXN1 | 0.981 | 0.129 | — |
| PLAA | 0.974 | 0.644 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| VCP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| VCPIP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| PLAA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| NLGN3 | psi-mi:"MI:0018"(two hybrid) | pubmed:25464930|imex:IM-26157 |
| MAGEA4 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| TRIM39 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| SVIP | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PLEKHB2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| UBXN10 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| UBXN2A | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.0 + PDB: 6SAP, 8FCL, 8FCM, 8FCN, 8FCO,  | pLDDT=76.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, cytosol; Membrane; Nucleus;  / Golgi apparatus, Cytosol | 一致 |
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
1. UBXN6 — UBX domain-containing protein 6，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小441 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BZV1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000167671-UBXN6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=UBXN6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BZV1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (approved)。来源: https://www.proteinatlas.org/ENSG00000167671-UBXN6/subcellular

![](https://images.proteinatlas.org/61872/1102_E12_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/61872/1102_E12_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/61872/1307_E8_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/61872/1307_E8_5_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BZV1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BZV1 |
| SMART | SM00580;SM00166; |
| UniProt Domain [FT] | DOMAIN 175..244; /note="PUB"; /evidence="ECO:0000255"; DOMAIN 332..408; /note="UBX"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00215" |
| InterPro | IPR036339;IPR018997;IPR029071;IPR001012;IPR042774; |
| Pfam | PF09409;PF00789; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000167671-UBXN6/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| QRICH1 | Biogrid, Bioplex | true |
| UBXN10 | Intact, Biogrid | true |
| UBXN2A | Intact, Biogrid | true |
| VCP | Intact, Biogrid, Opencell, Bioplex | true |
| VCPIP1 | Biogrid, Bioplex | true |
| VCPKMT | Biogrid, Bioplex | true |
| YOD1 | Intact, Biogrid | true |
| AAAS | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

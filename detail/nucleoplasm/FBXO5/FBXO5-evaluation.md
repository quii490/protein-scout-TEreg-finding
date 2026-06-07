---
type: protein-evaluation
gene: "FBXO5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FBXO5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBXO5 / EMI1, FBX5 |
| 蛋白名称 | F-box only protein 5 |
| 蛋白大小 | 447 aa / 50.1 kDa |
| UniProt ID | Q9UKT4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm; Cytoplasm, cytoskeleton, spindle |
| 蛋白大小 | 10/10 | ×1 | 10 | 447 aa / 50.1 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=48 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.4; PDB: 2M6N, 4UI9, 9GAW |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001810, IPR047147, IPR044064; Pfam: PF00646, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.5/180** | |
| **归一化总分** | | | **61.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Cytoplasm; Cytoplasm, cytoskeleton, spindle | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- meiotic spindle (GO:0072687)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- spindle (GO:0005819)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 48 |
| PubMed broad count | 144 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: EMI1, FBX5 |

**关键文献**:
1. Targeting the FBXO5-DOK6 axis to overcome temozolomide resistance in glioblastoma via proteasome-cytomechanics regulation.. *Cancer letters*. PMID: 41045986
2. FBXO5-mediated RNF183 degradation prevents endoplasmic reticulum stress-induced apoptosis and promotes colon cancer progression.. *Cell death & disease*. PMID: 38212299
3. Systematic analyses uncover endocrine-disrupting chemical-responsive genes linked to endometriosis.. *Reproductive toxicology (Elmsford, N.Y.)*. PMID: 41443441
4. The role of Fbxo5 in the development of human malignant tumors.. *American journal of cancer research*. PMID: 35530293
5. Prognostic Significance and Immunological Role of FBXO5 in Human Cancers: A Systematic Pan-Cancer Analysis.. *Frontiers in immunology*. PMID: 35720327

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.4 |
| 高置信度残基 (pLDDT>90) 占比 | 20.1% |
| 置信残基 (pLDDT 70-90) 占比 | 21.7% |
| 中等置信 (pLDDT 50-70) 占比 | 9.8% |
| 低置信 (pLDDT<50) 占比 | 48.3% |
| 有序区域 (pLDDT>70) 占比 | 41.8% |
| 可用 PDB 条目 | 2M6N, 4UI9, 9GAW |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=59.4），有序残基占 41.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001810, IPR047147, IPR044064; Pfam: PF00646, PF22191 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDC20 | 0.999 | 0.994 | — |
| ANAPC4 | 0.999 | 0.999 | — |
| FZR1 | 0.998 | 0.983 | — |
| SKP1 | 0.997 | 0.833 | — |
| BTRC | 0.992 | 0.651 | — |
| ANAPC2 | 0.989 | 0.986 | — |
| ANAPC10 | 0.986 | 0.967 | — |
| CDC23 | 0.985 | 0.965 | — |
| CUL1 | 0.985 | 0.616 | — |
| CDC27 | 0.984 | 0.971 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Dmel\CG11444 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Rca1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| olf413 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG13133 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| GILT3 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| ver | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG14151 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG15529 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| RpS10b | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| SkpA | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.4 + PDB: 2M6N, 4UI9, 9GAW | pLDDT=59.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cytoplasm, cytoskeleton, spind / Nucleoplasm | 一致 |
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
1. FBXO5 — F-box only protein 5，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小447 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 48 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=59.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UKT4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000112029-FBXO5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBXO5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UKT4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000112029-FBXO5/subcellular

![](https://images.proteinatlas.org/29048/564_B2_2_red_green.jpg)
![](https://images.proteinatlas.org/29048/572_B2_1_red_green.jpg)
![](https://images.proteinatlas.org/29048/572_B2_2_red_green.jpg)
![](https://images.proteinatlas.org/29048/587_B2_1_red_green.jpg)
![](https://images.proteinatlas.org/29048/587_B2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UKT4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UKT4 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 250..296; /note="F-box" |
| InterPro | IPR001810;IPR047147;IPR044064; |
| Pfam | PF00646;PF22191; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000112029-FBXO5/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ANAPC16 | Biogrid, Opencell | true |
| ANAPC2 | Biogrid, Opencell | true |
| ANAPC4 | Biogrid, Opencell | true |
| CDC16 | Biogrid, Opencell | true |
| CDC23 | Biogrid, Opencell | true |
| CDC26 | Biogrid, Opencell | true |
| CDC27 | Intact, Biogrid | true |
| EVI5 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

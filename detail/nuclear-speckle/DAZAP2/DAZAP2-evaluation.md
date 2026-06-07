---
type: protein-evaluation
gene: "DAZAP2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DAZAP2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DAZAP2 / KIAA0058, PRTB |
| 蛋白名称 | DAZ-associated protein 2 |
| 蛋白大小 | 168 aa / 17.3 kDa |
| UniProt ID | Q15038 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; UniProt: Cytoplasm; Nucleus; Nucleus speckle; Nucleus, nuclear body;  |
| 蛋白大小 | 8/10 | ×1 | 8 | 168 aa / 17.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=27 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR022730; Pfam: PF11029 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Supported |
| UniProt | Cytoplasm; Nucleus; Nucleus speckle; Nucleus, nuclear body; Cytoplasm, Stress granule | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytoplasmic stress granule (GO:0010494)
- nuclear body (GO:0016604)
- nuclear speck (GO:0016607)
- nucleus (GO:0005634)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 27 |
| PubMed broad count | 33 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0058, PRTB |

**关键文献**:
1. LncRNA MYOSLID contributes to PH via targeting BMPR2 signaling in pulmonary artery smooth muscle cell.. *Vascular pharmacology*. PMID: 39549862
2. Integrated multi-omics analyses identify anti-viral host factors and pathways controlling SARS-CoV-2 infection.. *Nature communications*. PMID: 38168026
3. DAZAP2 functions as a pan-coronavirus restriction factor by inhibiting viral entry and genomic replication.. *mBio*. PMID: 40833112
4. DAZAP2 acts as specifier of the p53 response to DNA damage.. *Nucleic acids research*. PMID: 33591310
5. The structure, expression and function prediction of DAZAP2, a down-regulated gene in multiple myeloma.. *Genomics, proteomics & bioinformatics*. PMID: 15629043

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.6 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 19.6% |
| 中等置信 (pLDDT 50-70) 占比 | 54.2% |
| 低置信 (pLDDT<50) 占比 | 26.2% |
| 有序区域 (pLDDT>70) 占比 | 19.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=58.6），有序残基占 19.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR022730; Pfam: PF11029 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DAZ1 | 0.970 | 0.292 | — |
| DAZAP1 | 0.938 | 0.000 | — |
| DAZL | 0.935 | 0.292 | — |
| BOLL | 0.835 | 0.000 | — |
| TXNL1 | 0.763 | 0.000 | — |
| RHOXF2 | 0.748 | 0.713 | — |
| IL17RB | 0.700 | 0.292 | — |
| ZFAND2B | 0.657 | 0.655 | — |
| BATF2 | 0.638 | 0.325 | — |
| RBFOX2 | 0.610 | 0.610 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000394699.2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| EXD3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| BAG3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CALCOCO2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| RNF208 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| WWP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| NDUFA5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| AATF | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| UBB | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TOLLIP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.6 + PDB: 无 | pLDDT=58.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Nucleus speckle; Nucleus, nucl / Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DAZAP2 — DAZ-associated protein 2，非常新颖，仅有少数基础研究。
2. 蛋白大小168 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 27 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=58.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q15038
- Protein Atlas: https://www.proteinatlas.org/ENSG00000183283-DAZAP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DAZAP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15038
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (supported)。来源: https://www.proteinatlas.org/ENSG00000183283-DAZAP2/subcellular

![](https://images.proteinatlas.org/45940/1457_F4_1_red_green.jpg)
![](https://images.proteinatlas.org/45940/1457_F4_2_red_green.jpg)
![](https://images.proteinatlas.org/45940/1476_G4_1_red_green.jpg)
![](https://images.proteinatlas.org/45940/1476_G4_2_red_green.jpg)
![](https://images.proteinatlas.org/45940/1483_F4_2_red_green.jpg)
![](https://images.proteinatlas.org/45940/1483_F4_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q15038-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q15038 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR022730; |
| Pfam | PF11029; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000183283-DAZAP2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ATXN1 | Intact, Biogrid | true |
| CALCOCO2 | Intact, Biogrid | true |
| DAZ1 | Intact, Biogrid | true |
| INCA1 | Intact, Biogrid | true |
| PLSCR1 | Intact, Biogrid | true |
| RBFOX2 | Intact, Biogrid | true |
| ROR2 | Intact, Biogrid | true |
| SMURF2 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

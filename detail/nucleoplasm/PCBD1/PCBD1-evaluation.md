---
type: protein-evaluation
gene: "PCBD1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PCBD1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PCBD1 / DCOH, PCBD |
| 蛋白名称 | Pterin-4-alpha-carbinolamine dehydratase |
| 蛋白大小 | 104 aa / 12.0 kDa |
| UniProt ID | P61457 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 104 aa / 12.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=30 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=96.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR036428, IPR001533; Pfam: PF01329 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Enhanced |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 30 |
| PubMed broad count | 42 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DCOH, PCBD |

**关键文献**:
1. Statistical evidence for high-penetrance MODY-causing genes in a large population-based cohort.. *Endocrinology, diabetes & metabolism*. PMID: 36208030
2. The art of magnesium transport.. *Magnesium research*. PMID: 26446763
3. Genotypic spectrum underlying tetrahydrobiopterin metabolism defects: Experience in a single Mexican reference center.. *Frontiers in genetics*. PMID: 36313470
4. Mutations in PCBD1 cause hypomagnesemia and renal magnesium wasting.. *Journal of the American Society of Nephrology : JASN*. PMID: 24204001
5. Assessing the causal relationship between the plasma proteome and epilepsy: A Mendelian randomization study.. *Epilepsia open*. PMID: 41165052

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 96.2 |
| 高置信度残基 (pLDDT>90) 占比 | 94.2% |
| 置信残基 (pLDDT 70-90) 占比 | 2.9% |
| 中等置信 (pLDDT 50-70) 占比 | 1.9% |
| 低置信 (pLDDT<50) 占比 | 1.0% |
| 有序区域 (pLDDT>70) 占比 | 97.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=96.2，有序区 97.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036428, IPR001533; Pfam: PF01329 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| QDPR | 0.996 | 0.000 | — |
| HNF1A | 0.995 | 0.971 | — |
| PAH | 0.992 | 0.230 | — |
| TPH1 | 0.987 | 0.000 | — |
| TH | 0.987 | 0.000 | — |
| TPH2 | 0.978 | 0.000 | — |
| PCBD2 | 0.959 | 0.519 | — |
| HNF1B | 0.892 | 0.771 | — |
| SPR | 0.852 | 0.000 | — |
| GCH1 | 0.850 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000299299.3 | psi-mi:"MI:0096"(pull down) | pubmed:16189514|imex:IM-16520| |
| ENSMUSP00000020298.7 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| GORASP2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| NIF3L1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| LNX1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| FXR2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| NTAQ1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| NUDT18 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| DVL2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| HNF1A | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=96.2 + PDB: 无 | pLDDT=96.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. PCBD1 — Pterin-4-alpha-carbinolamine dehydratase，非常新颖，仅有少数基础研究。
2. 蛋白大小104 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 30 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P61457
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166228-PCBD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PCBD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P61457
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000166228-PCBD1/subcellular

![](https://images.proteinatlas.org/37575/403_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/37575/403_G5_2_red_green.jpg)
![](https://images.proteinatlas.org/37575/406_G5_3_red_green.jpg)
![](https://images.proteinatlas.org/37575/406_G5_4_red_green.jpg)
![](https://images.proteinatlas.org/37575/408_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/37575/408_G5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P61457-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P61457 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR036428;IPR001533; |
| Pfam | PF01329; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000166228-PCBD1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FXR2 | Intact, Biogrid | true |
| GORASP2 | Intact, Biogrid | true |
| HNF1B | Intact, Biogrid | true |
| PCBD2 | Intact, Biogrid, Bioplex | true |
| ACIN1 | Intact | false |
| APP | Intact | false |
| DYRK1B | Biogrid | false |
| HNF1A | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

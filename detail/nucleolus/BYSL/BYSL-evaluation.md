---
type: protein-evaluation
gene: "BYSL"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BYSL 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BYSL / ENP1 |
| 蛋白名称 | Bystin |
| 蛋白大小 | 437 aa / 49.6 kDa |
| UniProt ID | Q13895 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli, Nucleoli rim, Mitotic chromosome; 额外: Nucleoplasm; UniProt: Cytoplasm; Nucleus, nucleolus |
| 蛋白大小 | 10/10 | ×1 | 10 | 437 aa / 49.6 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=38 篇 (≤40→8) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=77.4; PDB: 6G18, 6G4S, 6G4W, 7MQ8, 7MQ9, 7MQA, 7WTT |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR007955; Pfam: PF05291 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **134.0/180** | |
| **归一化总分** | | | **74.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Nucleoli rim, Mitotic chromosome; 额外: Nucleoplasm | Enhanced |
| UniProt | Cytoplasm; Nucleus, nucleolus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- apical part of cell (GO:0045177)
- chromosome (GO:0005694)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- membrane (GO:0016020)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- preribosome, small subunit precursor (GO:0030688)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 38 |
| PubMed broad count | 66 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ENP1 |

**关键文献**:
1. DDX10 and BYSL as the potential targets of chondrosarcoma and glioma.. *Medicine*. PMID: 34797290
2. Bystin is a Prognosis and Immune Biomarker: From Pan-Cancer Analysis to Validation in Breast Cancer.. *Breast cancer (Dove Medical Press)*. PMID: 40904351
3. Increased Expression and Prognostic Significance of BYSL in Melanoma.. *Journal of immunotherapy (Hagerstown, Md. : 1997)*. PMID: 38980088
4. BYSL contributes to tumor growth by cooperating with the mTORC2 complex in gliomas.. *Cancer biology & medicine*. PMID: 33628587
5. BYSL Promotes Glioblastoma Cell Migration, Invasion, and Mesenchymal Transition Through the GSK-3β/β-Catenin Signaling Pathway.. *Frontiers in oncology*. PMID: 33178594

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.4 |
| 高置信度残基 (pLDDT>90) 占比 | 49.4% |
| 置信残基 (pLDDT 70-90) 占比 | 20.6% |
| 中等置信 (pLDDT 50-70) 占比 | 10.3% |
| 低置信 (pLDDT<50) 占比 | 19.7% |
| 有序区域 (pLDDT>70) 占比 | 70.0% |
| 可用 PDB 条目 | 6G18, 6G4S, 6G4W, 7MQ8, 7MQ9, 7MQA, 7WTT, 7WTU, 7WTV, 7WTW |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（6G18, 6G4S, 6G4W, 7MQ8, 7MQ9, 7MQA, 7WTT, 7WTU, 7WTV, 7WTW）+ AlphaFold极高置信度预测（pLDDT=77.4），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007955; Pfam: PF05291 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UTP4 | 0.999 | 0.989 | — |
| RRP12 | 0.999 | 0.997 | — |
| DIMT1 | 0.999 | 0.991 | — |
| RPS6 | 0.999 | 0.991 | — |
| UTP15 | 0.999 | 0.991 | — |
| PNO1 | 0.999 | 0.995 | — |
| UTP6 | 0.999 | 0.991 | — |
| DCAF13 | 0.999 | 0.991 | — |
| KRR1 | 0.999 | 0.991 | — |
| WDR46 | 0.999 | 0.991 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TRIM37 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MAP3K14 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| COIL | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| Rpgrip1l | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| VCAM1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-17358|pubmed:22623428 |
| COPS5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| FBL | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| RPS6 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| RRP1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-26310|pubmed:20926688 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.4 + PDB: 6G18, 6G4S, 6G4W, 7MQ8, 7MQ9,  | pLDDT=77.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus, nucleolus / Nucleoli, Nucleoli rim, Mitotic chromosome; 额外: Nu | 一致 |
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
1. BYSL — Bystin，非常新颖，仅有少数基础研究。
2. 蛋白大小437 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 38 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13895
- Protein Atlas: https://www.proteinatlas.org/ENSG00000112578-BYSL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BYSL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13895
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (enhanced)。来源: https://www.proteinatlas.org/ENSG00000112578-BYSL/subcellular

![](https://images.proteinatlas.org/31217/1887_C2_1_red_green.jpg)
![](https://images.proteinatlas.org/31217/1887_C2_5_red_green.jpg)
![](https://images.proteinatlas.org/31217/330_C3_2_red_green.jpg)
![](https://images.proteinatlas.org/31217/330_C3_3_red_green.jpg)
![](https://images.proteinatlas.org/31217/333_C3_1_red_green.jpg)
![](https://images.proteinatlas.org/31217/333_C3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q13895-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q13895 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR007955; |
| Pfam | PF05291; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000112578-BYSL/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BUD23 | Biogrid, Opencell | true |
| COIL | Intact, Biogrid | true |
| CSNK1D | Biogrid, Opencell | true |
| ERBB4 | Intact, Biogrid | true |
| FAU | Biogrid, Opencell | true |
| FTSJ3 | Biogrid, Opencell | true |
| LTV1 | Intact, Biogrid, Opencell, Bioplex | true |
| NOB1 | Biogrid, Opencell | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

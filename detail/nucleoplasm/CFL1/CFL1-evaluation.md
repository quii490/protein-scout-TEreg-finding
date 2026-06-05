---
type: protein-evaluation
gene: "CFL1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CFL1 — REJECTED (研究热度过高 (PubMed strict=236，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CFL1 / CFL |
| 蛋白名称 | Cofilin-1 |
| 蛋白大小 | 166 aa / 18.5 kDa |
| UniProt ID | P23528 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane; UniProt: Nucleus matrix; Cytoplasm, cytoskeleton; Cell projection, ru |
| 蛋白大小 | 8/10 | ×1 | 8 | 166 aa / 18.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=236 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=87.6; PDB: 1Q8G, 1Q8X, 3J0S, 4BEX, 5HVK, 5L6W, 6UBY |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR002108, IPR029006, IPR017904; Pfam: PF00241 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **90.5/180** | |
| **归一化总分** | | | **50.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane | Approved |
| UniProt | Nucleus matrix; Cytoplasm, cytoskeleton; Cell projection, ruffle membrane; Cell projection, lamellip... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629)
- cell-cell junction (GO:0005911)
- cofilin-actin rod (GO:0090732)
- cortical actin cytoskeleton (GO:0030864)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- dendritic spine (GO:0043197)
- extracellular exosome (GO:0070062)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 236 |
| PubMed broad count | 471 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CFL |

**关键文献**:
1. Advances in multi-omics study of biomarkers of glycolipid metabolism disorder.. *Computational and structural biotechnology journal*. PMID: 36382190
2. PLD1 promotes spindle assembly and migration through regulating autophagy in mouse oocyte meiosis.. *Autophagy*. PMID: 38513669
3. Super-enhancer RNA m(6)A promotes local chromatin accessibility and oncogene transcription in pancreatic ductal adenocarcinoma.. *Nature genetics*. PMID: 37957340
4. Integrating machine learning and multi-omics analysis to reveal nucleotide metabolism-related immune genes and their functional validation in ischemic stroke.. *Frontiers in immunology*. PMID: 40207230
5. CircCDYL promotes glycolysis to drive the progression of nasopharyngeal carcinoma.. *Journal of advanced research*. PMID: 41016592

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.6 |
| 高置信度残基 (pLDDT>90) 占比 | 42.8% |
| 置信残基 (pLDDT 70-90) 占比 | 53.6% |
| 中等置信 (pLDDT 50-70) 占比 | 2.4% |
| 低置信 (pLDDT<50) 占比 | 1.2% |
| 有序区域 (pLDDT>70) 占比 | 96.4% |
| 可用 PDB 条目 | 1Q8G, 1Q8X, 3J0S, 4BEX, 5HVK, 5L6W, 6UBY, 6UC0, 6UC4, 6VAO |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1Q8G, 1Q8X, 3J0S, 4BEX, 5HVK, 5L6W, 6UBY, 6UC0, 6UC4, 6VAO）+ AlphaFold极高置信度预测（pLDDT=87.6），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002108, IPR029006, IPR017904; Pfam: PF00241 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ACTG1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| YWHAZ | psi-mi:"MI:0096"(pull down) | pubmed:12361576|mint:MINT-5215 |
| GRB2 | psi-mi:"MI:0096"(pull down) | pubmed:12577067|mint:MINT-5216 |
| ACTB | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MYCBP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ATXN1 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| TAGLN | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ENSP00000432660.1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EBI-1257125 | psi-mi:"MI:0096"(pull down) | pubmed:19463016|imex:IM-17246 |
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.6 + PDB: 1Q8G, 1Q8X, 3J0S, 4BEX, 5HVK,  | pLDDT=87.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus matrix; Cytoplasm, cytoskeleton; Cell proj / Plasma membrane | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CFL1 — Cofilin-1，研究基础较多，新颖性有限。
2. 蛋白大小166 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 236 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 236 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P23528
- Protein Atlas: https://www.proteinatlas.org/ENSG00000172757-CFL1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CFL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P23528
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000172757-CFL1/subcellular

![](https://images.proteinatlas.org/77782/1946_H7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/77782/1946_H7_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/77782/2053_F11_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/77782/2053_F11_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/77782/2101_H2_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/77782/2101_H2_4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P23528-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

---
type: protein-evaluation
gene: "CORO1C"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CORO1C — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CORO1C / CRN2, CRNN4 |
| 蛋白名称 | Coronin-1C |
| 蛋白大小 | 474 aa / 53.2 kDa |
| UniProt ID | Q9ULV4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane; Cell projection, lamellipodium; Cell projecti |
| 蛋白大小 | 10/10 | ×1 | 10 | 474 aa / 53.2 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=57 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=91.0; PDB: 7STY |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR015505, IPR015048, IPR015943, IPR019775, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **99.0/180** | |
| **归一化总分** | | | **55.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell membrane; Cell projection, lamellipodium; Cell projection, ruffle membrane; Cytoplasm, cytoskel... | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629)
- actin filament (GO:0005884)
- cell cortex (GO:0005938)
- endosome membrane (GO:0010008)
- flotillin complex (GO:0016600)
- focal adhesion (GO:0005925)
- lamellipodium (GO:0030027)
- lateral plasma membrane (GO:0016328)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 57 |
| PubMed broad count | 79 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CRN2, CRNN4 |

**关键文献**:
1. YBX1 gene silencing inhibits migratory and invasive potential via CORO1C in breast cancer in vitro.. *BMC cancer*. PMID: 28302118
2. Isolation and chromosomal assignment of a novel human gene, CORO1C, homologous to coronin-like actin-binding proteins.. *Cytogenetics and cell genetics*. PMID: 10828594
3. CORO1C, a novel PAK4 binding protein, recruits phospho-PAK4 at serine 99 to the leading edge and promotes the migration of gastric cancer cells.. *Acta biochimica et biophysica Sinica*. PMID: 35593474
4. Down-regulation of CORO1C mediated by lncMALAT1/miR-133a-3p axis contributes to trophoblast dysfunction and preeclampsia.. *Placenta*. PMID: 39278098
5. CircRNA CORO1C Regulates miR-654-3p/USP7 Axis to Mediate Laryngeal Squamous Cell Carcinoma Progression.. *Biochemical genetics*. PMID: 35064359

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.0 |
| 高置信度残基 (pLDDT>90) 占比 | 83.1% |
| 置信残基 (pLDDT 70-90) 占比 | 9.1% |
| 中等置信 (pLDDT 50-70) 占比 | 2.1% |
| 低置信 (pLDDT<50) 占比 | 5.7% |
| 有序区域 (pLDDT>70) 占比 | 92.2% |
| 可用 PDB 条目 | 7STY |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=91.0，有序区 92.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR015505, IPR015048, IPR015943, IPR019775, IPR036322; Pfam: PF08953, PF00400, PF16300 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CORO1B | 0.917 | 0.857 | — |
| ACTR2 | 0.899 | 0.690 | — |
| FLOT1 | 0.834 | 0.000 | — |
| PLS3 | 0.818 | 0.086 | — |
| CDH1 | 0.781 | 0.091 | — |
| FLOT2 | 0.745 | 0.000 | — |
| SLC6A3 | 0.724 | 0.000 | — |
| ACTB | 0.698 | 0.582 | — |
| IQGAP1 | 0.683 | 0.233 | — |
| RCC2 | 0.682 | 0.292 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MAP3K3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| RIPK3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| GRB2 | psi-mi:"MI:0096"(pull down) | pubmed:12577067|mint:MINT-5216 |
| MAP1LC3B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| VCAM1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-17358|pubmed:22623428 |
| USP45 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| Cdk1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Poc1b | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Cep76 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Sass6 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.0 + PDB: 7STY | pLDDT=91.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane; Cell projection, lamellipodium; Cel / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CORO1C — Coronin-1C，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小474 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 57 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9ULV4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000110880-CORO1C/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CORO1C
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9ULV4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9ULV4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

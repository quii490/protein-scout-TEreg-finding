---
type: protein-evaluation
gene: "MLLT3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MLLT3 — REJECTED (研究热度过高 (PubMed strict=145，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MLLT3 / AF9, YEATS3 |
| 蛋白名称 | Protein AF-9 |
| 蛋白大小 | 568 aa / 63.4 kDa |
| UniProt ID | P42568 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Chromosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 568 aa / 63.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=145 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.8; PDB: 2LM0, 2MV7, 2N4Q, 2NDF, 2NDG, 4TMP, 5HJB |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR040930, IPR038704, IPR055129, IPR052790; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus; Chromosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromosome (GO:0005694)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- transcription elongation factor complex (GO:0008023)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 145 |
| PubMed broad count | 316 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: AF9, YEATS3 |

**关键文献**:
1. Targeting the Menin-KMT2A interaction in leukemia: Lessons learned and future directions.. *International journal of cancer*. PMID: 39887730
2. Rearrangements involving 11q23.3/KMT2A in adult AML: mutational landscape and prognostic implications - a HARMONY study.. *Leukemia*. PMID: 38965370
3. MLLT3 Regulates Melanoma Stemness and Progression by Inhibiting HMGB1 Nuclear Entry and MAGEA1 M(5)C Modification.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 39716999
4. MLL-Rearranged Acute Lymphoblastic Leukemia.. *Current hematologic malignancy reports*. PMID: 32350732
5. The E3 ubiquitin ligase Herc1 modulates the response to nucleoside analogs in acute myeloid leukemia.. *Blood advances*. PMID: 39093953

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.8 |
| 高置信度残基 (pLDDT>90) 占比 | 31.2% |
| 置信残基 (pLDDT 70-90) 占比 | 4.6% |
| 中等置信 (pLDDT 50-70) 占比 | 8.1% |
| 低置信 (pLDDT<50) 占比 | 56.2% |
| 有序区域 (pLDDT>70) 占比 | 35.8% |
| 可用 PDB 条目 | 2LM0, 2MV7, 2N4Q, 2NDF, 2NDG, 4TMP, 5HJB, 5HJD, 5YYF, 6B7G |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=61.8），有序残基占 35.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR040930, IPR038704, IPR055129, IPR052790; Pfam: PF17793, PF03366 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AFF1 | 0.999 | 0.842 | — |
| ELL2 | 0.999 | 0.712 | — |
| ELL | 0.999 | 0.748 | — |
| AFF4 | 0.999 | 0.833 | — |
| MLLT1 | 0.999 | 0.832 | — |
| DOT1L | 0.998 | 0.873 | — |
| CCNT1 | 0.997 | 0.625 | — |
| ELL3 | 0.997 | 0.836 | — |
| MLLT10 | 0.996 | 0.510 | — |
| CDK9 | 0.996 | 0.857 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MCM6 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| APPBP2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CDK6 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:22094256|imex:IM-16628 |
| EBI-11060385 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:22094252|imex:IM-16588 |
| EBI-2891404 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:22094252|imex:IM-16588 |
| AFF4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-13603|pubmed:20153263 |
| DOT1L | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-13603|pubmed:20153263 |
| EAF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21729782|imex:IM-16559 |
| ELL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21729782|imex:IM-16559 |
| CCNT2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21729782|imex:IM-16559 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.8 + PDB: 2LM0, 2MV7, 2N4Q, 2NDF, 2NDG,  | pLDDT=61.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome / Nucleoplasm; 额外: Cytosol | 一致 |
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
1. MLLT3 — Protein AF-9，研究基础较多，新颖性有限。
2. 蛋白大小568 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 145 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=61.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 145 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P42568
- Protein Atlas: https://www.proteinatlas.org/ENSG00000171843-MLLT3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MLLT3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P42568
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000171843-MLLT3/subcellular

![](https://images.proteinatlas.org/1824/1846_A2_13_cr5ab931564bd66_red_green.jpg)
![](https://images.proteinatlas.org/1824/1846_A2_27_cr5ab931564be3a_red_green.jpg)
![](https://images.proteinatlas.org/1824/62_B10_1_red_green.jpg)
![](https://images.proteinatlas.org/1824/62_B10_2_red_green.jpg)
![](https://images.proteinatlas.org/1824/93_B10_1_red_green.jpg)
![](https://images.proteinatlas.org/1824/93_B10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P42568-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

---
type: protein-evaluation
gene: "ETNK2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ETNK2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ETNK2 / EKI2 |
| 蛋白名称 | Ethanolamine kinase 2 |
| 蛋白大小 | 386 aa / 44.8 kDa |
| UniProt ID | Q9NVF9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 386 aa / 44.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=87.7; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011009; Pfam: PF01633 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 17 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: EKI2 |

**关键文献**:
1. The ETNK2 gene promotes progression of papillary thyroid carcinoma through the HIPPO pathway.. *Journal of Cancer*. PMID: 35069898
2. ETNK2 Low-Expression Predicts Poor Prognosis in Renal Cell Carcinoma with Immunosuppressive Tumor Microenvironment.. *Journal of oncology*. PMID: 36866238
3. Hepatic metastasis of gastric cancer is associated with enhanced expression of ethanolamine kinase 2 via the p53-Bcl-2 intrinsic apoptosis pathway.. *British journal of cancer*. PMID: 33531692
4. Placental thrombosis and spontaneous fetal death in mice deficient in ethanolamine kinase 2.. *The Journal of biological chemistry*. PMID: 16861741
5. Dysregulated human renin expression in transgenic mice carrying truncated genomic constructs: evidence supporting the presence of insulators at the renin locus.. *American journal of physiology. Renal physiology*. PMID: 18632798

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.7 |
| 高置信度残基 (pLDDT>90) 占比 | 78.5% |
| 置信残基 (pLDDT 70-90) 占比 | 8.5% |
| 中等置信 (pLDDT 50-70) 占比 | 0.8% |
| 低置信 (pLDDT<50) 占比 | 12.2% |
| 有序区域 (pLDDT>70) 占比 | 87.0% |
| 可用 PDB 条目 | 无 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=87.7，有序区 87.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011009; Pfam: PF01633 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PCYT2 | 0.991 | 0.000 | — |
| ETNPPL | 0.943 | 0.053 | — |
| GPCPD1 | 0.907 | 0.000 | — |
| SELENOI | 0.748 | 0.000 | — |
| GOLT1A | 0.697 | 0.000 | — |
| PISD | 0.667 | 0.056 | — |
| CEPT1 | 0.650 | 0.000 | — |
| PCYT1A | 0.635 | 0.000 | — |
| PCYT1B | 0.608 | 0.000 | — |
| MAPKAP1 | 0.600 | 0.572 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NOL3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| UBE2A | psi-mi:"MI:0018"(two hybrid) | imex:IM-11696|pubmed:19549727 |
| MDFI | psi-mi:"MI:0397"(two hybrid array) | pubmed:19060904|imex:IM-20259 |
| RAB11B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CYSRT1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| HNRNPK | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KRTAP12-2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ATN1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| STX1A | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MID2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.7 + PDB: 无 | pLDDT=87.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. ETNK2 — Ethanolamine kinase 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小386 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NVF9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000143845-ETNK2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ETNK2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NVF9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NVF9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

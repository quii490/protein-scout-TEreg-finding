---
type: protein-evaluation
gene: "DYNLT3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DYNLT3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DYNLT3 / TCTE1L, TCTE1XL |
| 蛋白名称 | Dynein light chain Tctex-type 3 |
| 蛋白大小 | 116 aa / 13.1 kDa |
| UniProt ID | P51808 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus; Cytoplasm, cytoskeleton; Chromosome, centromere, ki |
| 蛋白大小 | 8/10 | ×1 | 8 | 116 aa / 13.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=20 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=91.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR005334, IPR038586; Pfam: PF03645 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **136.5/180** | |
| **归一化总分** | | | **75.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus; Cytoplasm, cytoskeleton; Chromosome, centromere, kinetochore | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytoplasmic dynein complex (GO:0005868)
- kinetochore (GO:0000776)
- mitotic spindle astral microtubule (GO:0061673)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 20 |
| PubMed broad count | 28 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TCTE1L, TCTE1XL |

**关键文献**:
1. Effects of dynein light chain Tctex-type 3 on the biological behavior of ovarian cancer.. *Cancer management and research*. PMID: 31308737
2. The role of DYNLT3 in breast cancer proliferation, migration, and invasion via epithelial-to-mesenchymal transition.. *Cancer medicine*. PMID: 37260179
3. Age-associated genes in human mammary gland drive human breast cancer progression.. *Breast cancer research : BCR*. PMID: 32539762
4. Copy number variations due to large genomic deletion in X-linked chronic granulomatous disease.. *PloS one*. PMID: 22383943
5. The DYNLT3 light chain directly links cytoplasmic dynein to a spindle checkpoint protein, Bub3.. *The Journal of biological chemistry*. PMID: 17289665

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.2 |
| 高置信度残基 (pLDDT>90) 占比 | 85.3% |
| 置信残基 (pLDDT 70-90) 占比 | 4.3% |
| 中等置信 (pLDDT 50-70) 占比 | 2.6% |
| 低置信 (pLDDT<50) 占比 | 7.8% |
| 有序区域 (pLDDT>70) 占比 | 89.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=91.2，有序区 89.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR005334, IPR038586; Pfam: PF03645 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DYNC1LI1 | 0.993 | 0.836 | — |
| DYNC1I2 | 0.983 | 0.927 | — |
| DYNC1I1 | 0.982 | 0.850 | — |
| WDR34 | 0.978 | 0.445 | — |
| WDR60 | 0.978 | 0.445 | — |
| DYNLL1 | 0.976 | 0.627 | — |
| DYNLRB2 | 0.970 | 0.545 | — |
| DYNLRB1 | 0.965 | 0.545 | — |
| DYNC2LI1 | 0.965 | 0.000 | — |
| DYNLL2 | 0.962 | 0.556 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000367841.4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TESC | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| DYNC1I2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| hrpA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| Bub3 | psi-mi:"MI:0018"(two hybrid) | pubmed:17289665|imex:IM-19822 |
| Dync1h1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| PMS1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CCL28 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| DYNLT2B | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| PAFAH1B1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.2 + PDB: 无 | pLDDT=91.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, cytoskeleton; Chromosome, cent / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DYNLT3 — Dynein light chain Tctex-type 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小116 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 20 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P51808
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165169-DYNLT3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DYNLT3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P51808
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P51808-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

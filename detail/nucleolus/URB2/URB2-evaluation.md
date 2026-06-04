---
type: protein-evaluation
gene: "URB2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## URB2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | URB2 / KIAA0133 |
| 蛋白名称 | Unhealthy ribosome biogenesis protein 2 homolog |
| 蛋白大小 | 1524 aa / 170.5 kDa |
| UniProt ID | Q14146 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoli; UniProt: Nucleus, nucleolus |
| 蛋白大小 | 5/10 | ×1 | 5 | 1524 aa / 170.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=82.3; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR052609, IPR018849; Pfam: PF10441 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.5/180** | |
| **归一化总分** | | | **76.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli | Enhanced |
| UniProt | Nucleus, nucleolus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- aggresome (GO:0016235)
- midbody (GO:0030496)
- nucleolus (GO:0005730)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 15 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0133 |

**关键文献**:
1. Maize Urb2 protein is required for kernel development and vegetative growth by affecting pre-ribosomal RNA processing.. *The New phytologist*. PMID: 29479724
2. URB2 as an important marker for glioma prognosis and immunotherapy.. *Frontiers in pharmacology*. PMID: 37033651
3. mTORC1 mediates the expansion of hematopoietic stem and progenitor cells through ribosome biogenesis protein Urb2 in zebrafish.. *Stem cell reports*. PMID: 39178846
4. Ribosome biogenesis protein Urb2 regulates hematopoietic stem cells development via P53 pathway in zebrafish.. *Biochemical and biophysical research communications*. PMID: 29470984
5. Regulatory network analysis of hypertension and hypotension microarray data from mouse model.. *Clinical and experimental hypertension (New York, N.Y. : 1993)*. PMID: 29400567

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.3 |
| 高置信度残基 (pLDDT>90) 占比 | 26.7% |
| 置信残基 (pLDDT 70-90) 占比 | 60.4% |
| 中等置信 (pLDDT 50-70) 占比 | 8.0% |
| 低置信 (pLDDT<50) 占比 | 4.9% |
| 有序区域 (pLDDT>70) 占比 | 87.1% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=82.3，有序区 87.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052609, IPR018849; Pfam: PF10441 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| URB1 | 0.890 | 0.000 | — |
| DDX31 | 0.780 | 0.000 | — |
| NOL8 | 0.762 | 0.707 | — |
| MARS2 | 0.654 | 0.000 | — |
| POLR1B | 0.638 | 0.000 | — |
| GEMIN4 | 0.624 | 0.000 | — |
| TAF1B | 0.589 | 0.000 | — |
| WDR1 | 0.578 | 0.438 | — |
| PPRC1 | 0.503 | 0.000 | — |
| UTP15 | 0.502 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ARX1 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| ARG1 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| DBP6 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| RSA3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| URB1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| URA2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| SSA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SWA2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| KAR2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSZ1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.3 + PDB: 无 | pLDDT=82.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus, nucleolus / Nucleoli | 一致 |
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
1. URB2 — Unhealthy ribosome biogenesis protein 2 homolog，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1524 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q14146
- Protein Atlas: https://www.proteinatlas.org/ENSG00000135763-URB2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=URB2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14146
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

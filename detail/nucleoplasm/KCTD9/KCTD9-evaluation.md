---
type: protein-evaluation
gene: "KCTD9"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KCTD9 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KCTD9 |
| 蛋白名称 | BTB/POZ domain-containing protein KCTD9 |
| 蛋白大小 | 389 aa / 42.6 kDa |
| UniProt ID | Q7L273 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Intermediate filaments, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 389 aa / 42.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=89.8; PDB: 5BXH |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001646, IPR000210, IPR036572, IPR021789, IPR051 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.5/180** | |
| **归一化总分** | | | **76.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Intermediate filaments, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 24 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. KCTD9 inhibits the Wnt/β-catenin pathway by decreasing the level of β-catenin in colorectal cancer.. *Cell death & disease*. PMID: 36055981
2. TAF1 acetyltransferase promotes colorectal carcinoma metastasis by catalyzing β-hydroxybutyrylation of KCTD9.. *Oncogene*. PMID: 41309931
3. [KCTD9, a novel potassium channel related gene, was highly expressed in hepatic NK cells and T cells of fulminant hepatitis mice induced by MHV-3].. *Zhonghua gan zang bing za zhi = Zhonghua ganzangbing zazhi = Chinese journal of hepatology*. PMID: 22433305
4. Structural Insights into KCTD Protein Assembly and Cullin3 Recognition.. *Journal of molecular biology*. PMID: 26334369
5. Anti-cancer effects of Coix seed extract through KCTD9-mediated ubiquitination of TOP2A in lung adenocarcinoma.. *Cell division*. PMID: 38374109

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.8 |
| 高置信度残基 (pLDDT>90) 占比 | 72.8% |
| 置信残基 (pLDDT 70-90) 占比 | 18.8% |
| 中等置信 (pLDDT 50-70) 占比 | 4.9% |
| 低置信 (pLDDT<50) 占比 | 3.6% |
| 有序区域 (pLDDT>70) 占比 | 91.6% |
| 可用 PDB 条目 | 5BXH |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=89.8，有序区 91.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001646, IPR000210, IPR036572, IPR021789, IPR051082; Pfam: PF02214, PF11834, PF00805 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL3 | 0.893 | 0.743 | — |
| TOP2B | 0.735 | 0.602 | — |
| TOP2A | 0.734 | 0.602 | — |
| KCTD1 | 0.697 | 0.000 | — |
| KCTD11 | 0.646 | 0.000 | — |
| NUP35 | 0.607 | 0.604 | — |
| PPP1R16B | 0.529 | 0.126 | — |
| TMEM159 | 0.517 | 0.000 | — |
| KCTD19 | 0.514 | 0.000 | — |
| LZIC | 0.487 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000221200.4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| EGFR | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:20029029|imex:IM-17166 |
| NSS | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:22810585|imex:IM-17331 |
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| NUP35 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GORASP2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:29892012|doi:10.1038/s4 |
| PICK1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ZNF76 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| EPM2AIP1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SPG21 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.8 + PDB: 5BXH | pLDDT=89.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Intermediate filaments, Cytosol | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. KCTD9 — BTB/POZ domain-containing protein KCTD9，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小389 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7L273
- Protein Atlas: https://www.proteinatlas.org/ENSG00000104756-KCTD9/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KCTD9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7L273
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000104756-KCTD9/subcellular

![](https://images.proteinatlas.org/42468/504_H8_1_red_green.jpg)
![](https://images.proteinatlas.org/42468/504_H8_2_red_green.jpg)
![](https://images.proteinatlas.org/42468/506_H8_1_red_green.jpg)
![](https://images.proteinatlas.org/42468/506_H8_2_red_green.jpg)
![](https://images.proteinatlas.org/42468/840_F7_1_red_green.jpg)
![](https://images.proteinatlas.org/42468/840_F7_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7L273-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

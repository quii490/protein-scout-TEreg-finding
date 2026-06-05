---
type: protein-evaluation
gene: "SPI1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SPI1 — REJECTED (研究热度过高 (PubMed strict=1133，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SPI1 |
| 蛋白名称 | Transcription factor PU.1 |
| 蛋白大小 | 270 aa / 31.1 kDa |
| UniProt ID | P17947 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 270 aa / 31.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1133 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.5; PDB: 8E3K, 8E3R, 8E4H, 8E5Y, 8EBH, 8EE9, 8EJ6 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000418, IPR046328, IPR036388, IPR036390; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.5/180** | |
| **归一化总分** | | | **49.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1133 |
| PubMed broad count | 1695 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. ATF3/SPI1/SLC31A1 Signaling Promotes Cuproptosis Induced by Advanced Glycosylation End Products in Diabetic Myocardial Injury.. *International journal of molecular sciences*. PMID: 36675183
2. SIRT5-related lysine demalonylation of GSTP1 contributes to cardiomyocyte pyroptosis suppression in diabetic cardiomyopathy.. *International journal of biological sciences*. PMID: 38169591
3. METTL14 Inhibits Hematopoietic Stem/Progenitor Differentiation and Promotes Leukemogenesis via mRNA m(6)A Modification.. *Cell stem cell*. PMID: 29290617
4. Bidirectional epigenetic editing reveals hierarchies in gene regulation.. *Nature biotechnology*. PMID: 38760566
5. PRDM1/BLIMP1 induces cancer immune evasion by modulating the USP22-SPI1-PD-L1 axis in hepatocellular carcinoma cells.. *Nature communications*. PMID: 36509766

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.5 |
| 高置信度残基 (pLDDT>90) 占比 | 32.6% |
| 置信残基 (pLDDT 70-90) 占比 | 1.9% |
| 中等置信 (pLDDT 50-70) 占比 | 27.8% |
| 低置信 (pLDDT<50) 占比 | 37.8% |
| 有序区域 (pLDDT>70) 占比 | 34.5% |
| 可用 PDB 条目 | 8E3K, 8E3R, 8E4H, 8E5Y, 8EBH, 8EE9, 8EJ6, 8EJ8, 8EK3, 8EK8 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=65.5），有序残基占 34.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000418, IPR046328, IPR036388, IPR036390; Pfam: PF00178 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| IRF8 | 0.999 | 0.635 | — |
| IRF4 | 0.998 | 0.635 | — |
| GATA1 | 0.996 | 0.512 | — |
| GATA2 | 0.993 | 0.627 | — |
| JUN | 0.993 | 0.301 | — |
| RUNX1 | 0.993 | 0.292 | — |
| CSF1R | 0.992 | 0.000 | — |
| CEBPA | 0.990 | 0.516 | — |
| RARA | 0.978 | 0.292 | — |
| ITGAM | 0.977 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TEF1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| YEF3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| TMX1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| Smad3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:22036565|imex:IM-16644 |
| EBI-5259819 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:22036565|imex:IM-16644 |
| EBI-5259219 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:22036565|imex:IM-16644 |
| EBI-5259793 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:22036565|imex:IM-16644 |
| SOST | psi-mi:"MI:0096"(pull down) | pubmed:22206666|imex:IM-17213 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| HOXA10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:18692240|imex:IM-20278 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.5 + PDB: 8E3K, 8E3R, 8E4H, 8E5Y, 8EBH,  | pLDDT=65.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
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
1. SPI1 — Transcription factor PU.1，研究基础较多，新颖性有限。
2. 蛋白大小270 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1133 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=65.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1133 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P17947
- Protein Atlas: https://www.proteinatlas.org/ENSG00000066336-SPI1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SPI1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P17947
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000066336-SPI1/subcellular

![](https://images.proteinatlas.org/44653/1676_D3_2_red_green.jpg)
![](https://images.proteinatlas.org/44653/1676_D3_5_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P17947-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

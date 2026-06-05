---
type: protein-evaluation
gene: "MAGEC2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MAGEC2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MAGEC2 / HCA587, MAGEE1 |
| 蛋白名称 | Melanoma-associated antigen C2 |
| 蛋白大小 | 373 aa / 41.2 kDa |
| UniProt ID | Q9UBF1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 373 aa / 41.2 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=68 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR037445, IPR041898, IPR041899, IPR002190; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 10 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **100.0/180** | |
| **归一化总分** | | | **55.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 68 |
| PubMed broad count | 136 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HCA587, MAGEE1 |

**关键文献**:
1. Establishment of MAGEC2-knockout cells and functional investigation of MAGEC2 in tumor cells.. *Cancer science*. PMID: 27636589
2. MageC2 protein is upregulated by oncogenic activation of MAPK pathway and causes impairment of the p53 transactivation function.. *Biochimica et biophysica acta. Molecular cell research*. PMID: 33279609
3. A Genome-Wide Association Study Reveals Two Genetic Markers for Chondromalacia.. *Cartilage*. PMID: 36068934
4. MAGEC2 Correlates With Unfavorable Prognosis And Promotes Tumor Development In HCC Via Epithelial-Mesenchymal Transition.. *OncoTargets and therapy*. PMID: 31576142
5. Cancer‑testis antigen HCA587/MAGEC2 interacts with the general transcription coactivator TAF9 in cancer cells.. *Molecular medicine reports*. PMID: 29257297

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.1 |
| 高置信度残基 (pLDDT>90) 占比 | 20.9% |
| 置信残基 (pLDDT 70-90) 占比 | 26.0% |
| 中等置信 (pLDDT 50-70) 占比 | 13.9% |
| 低置信 (pLDDT<50) 占比 | 39.1% |
| 有序区域 (pLDDT>70) 占比 | 46.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=65.1），有序残基占 46.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037445, IPR041898, IPR041899, IPR002190; Pfam: PF01454 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TRIM28 | 0.992 | 0.837 | — |
| RBX1 | 0.859 | 0.292 | — |
| SAGE1 | 0.812 | 0.000 | — |
| MAGEC1 | 0.795 | 0.000 | — |
| SSX1 | 0.743 | 0.358 | — |
| PAGE5 | 0.737 | 0.000 | — |
| SPA17 | 0.736 | 0.070 | — |
| CRK | 0.729 | 0.000 | — |
| CRKL | 0.697 | 0.000 | — |
| SSX2 | 0.695 | 0.171 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| P4HA3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| MAGEB10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PBX3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| SSX1 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |
| SSX2 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |
| SPRED1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| YARS1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| GLE1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| TSC1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:32814053|imex:IM-28217| |
| MAGEB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 10
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 10 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.1 + PDB: 无 | pLDDT=65.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 10 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. MAGEC2 — Melanoma-associated antigen C2，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小373 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 68 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=65.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UBF1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000046774-MAGEC2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MAGEC2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UBF1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000046774-MAGEC2/subcellular

![](https://images.proteinatlas.org/62230/1300_A6_3_red_green.jpg)
![](https://images.proteinatlas.org/62230/1300_A6_4_red_green.jpg)
![](https://images.proteinatlas.org/62230/1364_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/62230/1364_A3_3_red_green.jpg)
![](https://images.proteinatlas.org/62230/1854_H6_5_red_green.jpg)
![](https://images.proteinatlas.org/62230/1854_H6_7_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UBF1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

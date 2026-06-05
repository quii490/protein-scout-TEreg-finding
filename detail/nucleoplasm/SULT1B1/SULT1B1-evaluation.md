---
type: protein-evaluation
gene: "SULT1B1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SULT1B1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SULT1B1 / ST1B2, SULT1B2 |
| 蛋白名称 | Sulfotransferase 1B1 |
| 蛋白大小 | 296 aa / 34.9 kDa |
| UniProt ID | O43704 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Golgi apparatus; 额外: Nucleoplasm; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 296 aa / 34.9 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=67 篇 (≤80→4) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=97.8; PDB: 2Z5F, 3CKL |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR027417, IPR000863; Pfam: PF00685 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **100.0/180** | |
| **归一化总分** | | | **55.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nucleoplasm | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 67 |
| PubMed broad count | 117 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ST1B2, SULT1B2 |

**关键文献**:
1. Histone tyrosine sulfation by SULT1B1 regulates H4R3me2a and gene transcription.. *Nature chemical biology*. PMID: 36805701
2. Integrative causal inference illuminates gene-environment interactions linking endocrine disruptors to female infertility.. *Ecotoxicology and environmental safety*. PMID: 40663944
3. Systematic analyses uncover endocrine-disrupting chemical-responsive genes linked to endometriosis.. *Reproductive toxicology (Elmsford, N.Y.)*. PMID: 41443441
4. Postnatal ontogeny and hormonal regulation of sulfotransferase SULT1B1 in male and female rats.. *The Journal of pharmacology and experimental therapeutics*. PMID: 10381794
5. Author Correction: Histone tyrosine sulfation by SULT1B1 regulates H4R3me2a and gene transcription.. *Nature chemical biology*. PMID: 40890508

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 97.8 |
| 高置信度残基 (pLDDT>90) 占比 | 97.0% |
| 置信残基 (pLDDT 70-90) 占比 | 2.4% |
| 中等置信 (pLDDT 50-70) 占比 | 0.7% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 99.4% |
| 可用 PDB 条目 | 2Z5F, 3CKL |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2Z5F, 3CKL）+ AlphaFold高质量预测（pLDDT=97.8），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027417, IPR000863; Pfam: PF00685 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CHST6 | 0.902 | 0.000 | — |
| NDST1 | 0.893 | 0.000 | — |
| PAPSS2 | 0.855 | 0.000 | — |
| HS3ST1 | 0.845 | 0.000 | — |
| PAPSS1 | 0.839 | 0.000 | — |
| HS3ST3A1 | 0.833 | 0.000 | — |
| SULT2A1 | 0.832 | 0.590 | — |
| HS3ST3B1 | 0.825 | 0.000 | — |
| NDST2 | 0.815 | 0.000 | — |
| CHST5 | 0.759 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| - | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| LRP4 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| SULT2B1 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-25511|pubmed:25910212 |
| SULT2A1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SDCBP | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |
| TARS1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| UQCRC1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:32814053|imex:IM-28217| |
| VBP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:32814053|imex:IM-28217| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 8
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 8 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=97.8 + PDB: 2Z5F, 3CKL | pLDDT=97.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Golgi apparatus; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 8 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. SULT1B1 — Sulfotransferase 1B1，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小296 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 67 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43704
- Protein Atlas: https://www.proteinatlas.org/ENSG00000173597-SULT1B1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SULT1B1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43704
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (approved)。来源: https://www.proteinatlas.org/ENSG00000173597-SULT1B1/subcellular

![](https://images.proteinatlas.org/2107/1642_E2_1_red_green.jpg)
![](https://images.proteinatlas.org/2107/1642_E2_2_red_green.jpg)
![](https://images.proteinatlas.org/2107/33_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/2107/33_B4_2_red_green.jpg)
![](https://images.proteinatlas.org/2107/34_B4_1_red_green.jpg)
![](https://images.proteinatlas.org/2107/34_B4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O43704-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

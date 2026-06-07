---
type: protein-evaluation
gene: "SSX3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SSX3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SSX3 |
| 蛋白名称 | Protein SSX3 |
| 蛋白大小 | 188 aa / 21.7 kDa |
| UniProt ID | Q99909 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: Nucleoplasm, Nucleoli; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 188 aa / 21.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=18 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003655, IPR001909, IPR036051, IPR019041; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.5/180** | |
| **归一化总分** | | | **73.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 23 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Whole-genome sequencing identifies new candidate genes for nonobstructive azoospermia.. *Andrology*. PMID: 36017582
2. Identification and Validation of the Prognostic Stemness Biomarkers in Bladder Cancer Bone Metastasis.. *Frontiers in oncology*. PMID: 33816287
3. The cancer-related protein SSX2 interacts with the human homologue of a Ras-like GTPase interactor, RAB3IP, and a novel nuclear protein, SSX2IP.. *Genes, chromosomes & cancer*. PMID: 12007189
4. Higher Expression Levels of SSX1 and SSX2 in Patients with Colon Cancer: Regulated In Vitro by the Inhibition of Methylation and Histone Deacetylation.. *Medicina (Kaunas, Lithuania)*. PMID: 37241221
5. Serum Proteomic Signatures of Male Breast Cancer.. *Cancer genomics & proteomics*. PMID: 30850364

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.2 |
| 高置信度残基 (pLDDT>90) 占比 | 25.5% |
| 置信残基 (pLDDT 70-90) 占比 | 12.8% |
| 中等置信 (pLDDT 50-70) 占比 | 45.2% |
| 低置信 (pLDDT<50) 占比 | 16.5% |
| 有序区域 (pLDDT>70) 占比 | 38.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=67.2），有序残基占 38.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003655, IPR001909, IPR036051, IPR019041; Pfam: PF09514 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SSX2 | 0.936 | 0.718 | — |
| SSX2IP | 0.832 | 0.096 | — |
| SSX1 | 0.755 | 0.000 | — |
| SS18 | 0.718 | 0.000 | — |
| SSX7 | 0.703 | 0.699 | — |
| ZNF117 | 0.645 | 0.000 | — |
| ZNF83 | 0.641 | 0.000 | — |
| RAB3IP | 0.630 | 0.000 | — |
| PRRG3 | 0.544 | 0.000 | — |
| MIPOL1 | 0.518 | 0.518 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.2 + PDB: 无 | pLDDT=67.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SSX3 — Protein SSX3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小188 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=67.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q99909
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165584-SSX3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SSX3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99909
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000165584-SSX3/subcellular

![](https://images.proteinatlas.org/45683/1397_A4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/45683/1397_A4_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/45683/1402_A4_10_blue_red_green.jpg)
![](https://images.proteinatlas.org/45683/1402_A4_11_blue_red_green.jpg)
![](https://images.proteinatlas.org/45683/1440_H11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/45683/1440_H11_5_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q99909-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q99909 |
| SMART | SM00349; |
| UniProt Domain [FT] | DOMAIN 20..83; /note="KRAB-related"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00120" |
| InterPro | IPR003655;IPR001909;IPR036051;IPR019041; |
| Pfam | PF09514; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000165584-SSX3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AGTRAP | Intact | false |
| C10orf88 | Bioplex | false |
| CEP63 | Intact | false |
| CEP70 | Intact | false |
| CMTM5 | Intact | false |
| KRT27 | Intact | false |
| MED4 | Intact | false |
| MEOX2 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

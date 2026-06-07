---
type: protein-evaluation
gene: "DPH6"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DPH6 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DPH6 / ATPBD4 |
| 蛋白名称 | Diphthine--ammonia ligase |
| 蛋白大小 | 267 aa / 30.3 kDa |
| UniProt ID | Q7L8W6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli, Nucleoli rim; 额外: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 267 aa / 30.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=90.0; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR002761, IPR030662, IPR014729; Pfam: PF01902 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.0/180** | |
| **归一化总分** | | | **70.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Nucleoli rim; 额外: Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 15 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ATPBD4 |

**关键文献**:
1. Decoding the biosynthesis and function of diphthamide, an enigmatic modification of translation elongation factor 2 (EF2).. *Microbial cell (Graz, Austria)*. PMID: 28357244
2. The amidation step of diphthamide biosynthesis in yeast requires DPH6, a gene identified through mining the DPH1-DPH5 interaction network.. *PLoS genetics*. PMID: 23468660
3. Genome-wide association study and pathway analysis for carcass fatness in Nellore cattle measured by ultrasound.. *Animal genetics*. PMID: 34370325
4. Comparative genomic analysis of the DUF71/COG2102 family predicts roles in diphthamide biosynthesis and B12 salvage.. *Biology direct*. PMID: 23013770
5. Clinical and Genetic Factors Associated with Intraoperative Minimum Alveolar Concentration Ratio: A Single-center Retrospective Cohort and Genome-wide Association Study.. *Anesthesiology*. PMID: 40489632

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.0 |
| 高置信度残基 (pLDDT>90) 占比 | 77.5% |
| 置信残基 (pLDDT 70-90) 占比 | 11.6% |
| 中等置信 (pLDDT 50-70) 占比 | 5.6% |
| 低置信 (pLDDT<50) 占比 | 5.2% |
| 有序区域 (pLDDT>70) 占比 | 89.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=90.0，有序区 89.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002761, IPR030662, IPR014729; Pfam: PF01902 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DPH5 | 0.972 | 0.000 | — |
| EEF2 | 0.888 | 0.142 | — |
| DPH7 | 0.852 | 0.000 | — |
| DPH2 | 0.815 | 0.000 | — |
| DPH3 | 0.811 | 0.000 | — |
| DPH1 | 0.809 | 0.000 | — |
| DNAJC24 | 0.761 | 0.000 | — |
| RIDA | 0.512 | 0.000 | — |
| MFSD4B | 0.502 | 0.496 | — |
| ELP5 | 0.494 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.0 + PDB: 无 | pLDDT=90.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoli, Nucleoli rim; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DPH6 — Diphthine--ammonia ligase，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小267 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7L8W6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000134146-DPH6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DPH6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7L8W6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000134146-DPH6/subcellular

![](https://images.proteinatlas.org/42976/762_C2_1_red_green.jpg)
![](https://images.proteinatlas.org/42976/762_C2_2_red_green.jpg)
![](https://images.proteinatlas.org/42976/765_C5_1_red_green.jpg)
![](https://images.proteinatlas.org/42976/765_C5_3_red_green.jpg)
![](https://images.proteinatlas.org/42976/771_C5_5_red_green.jpg)
![](https://images.proteinatlas.org/42976/771_C5_6_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7L8W6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q7L8W6 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR002761;IPR030662;IPR014729; |
| Pfam | PF01902; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000134146-DPH6/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CT55 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

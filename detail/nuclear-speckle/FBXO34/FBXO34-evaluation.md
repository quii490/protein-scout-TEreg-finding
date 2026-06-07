---
type: protein-evaluation
gene: "FBXO34"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FBXO34 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBXO34 / FBX34 |
| 蛋白名称 | F-box only protein 34 |
| 蛋白大小 | 711 aa / 78.7 kDa |
| UniProt ID | Q9NWN3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 711 aa / 78.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=48.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036047, IPR001810, IPR039594; Pfam: PF12937 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.5/180** | |
| **归一化总分** | | | **71.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles; 额外: Cytosol | Approved |
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
| PubMed strict count | 5 |
| PubMed broad count | 5 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FBX34 |

**关键文献**:
1. HIV-1 latency: From acquaintance to confidant.. *Journal of virus eradication*. PMID: 40497153
2. Genome-wide association study of hospitalized COVID-19 patients in the United Arab Emirates.. *EBioMedicine*. PMID: 34775353
3. FBXO34 Regulates the G2/M Transition and Anaphase Entry in Meiotic Oocytes.. *Frontiers in cell and developmental biology*. PMID: 33842473
4. FBXO34 promotes latent HIV-1 activation by post-transcriptional modulation.. *Emerging microbes & infections*. PMID: 36285453
5. Exome-Wide Association Study Reveals Host Genetic Variants Likely Associated with the Severity of COVID-19 in Patients of European Ancestry.. *Life (Basel, Switzerland)*. PMID: 36143338

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 48.7 |
| 高置信度残基 (pLDDT>90) 占比 | 1.0% |
| 置信残基 (pLDDT 70-90) 占比 | 13.8% |
| 中等置信 (pLDDT 50-70) 占比 | 13.2% |
| 低置信 (pLDDT<50) 占比 | 72.0% |
| 有序区域 (pLDDT>70) 占比 | 14.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=48.7），有序残基占 14.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036047, IPR001810, IPR039594; Pfam: PF12937 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL1 | 0.870 | 0.637 | — |
| MYO6 | 0.782 | 0.779 | — |
| SKP1 | 0.759 | 0.359 | — |
| FBXO30 | 0.704 | 0.696 | — |
| FBXO28 | 0.597 | 0.000 | — |
| GSN | 0.591 | 0.591 | — |
| KRTAP12-4 | 0.591 | 0.591 | — |
| FBXO42 | 0.529 | 0.000 | — |
| FBXO36 | 0.474 | 0.000 | — |
| FBXO5 | 0.455 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SKP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| COA7 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ITGB1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| NCBP1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| DISC1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| MTUS2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| KRTAP10-5 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| ALPP | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| KRTAP12-4 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=48.7 + PDB: 无 | pLDDT=48.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nuclear speckles; 额外: Cytosol | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FBXO34 — F-box only protein 34，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小711 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=48.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NWN3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000178974-FBXO34/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBXO34
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NWN3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000178974-FBXO34/subcellular

![](https://images.proteinatlas.org/52592/783_C8_1_red_green.jpg)
![](https://images.proteinatlas.org/52592/783_C8_2_red_green.jpg)
![](https://images.proteinatlas.org/52592/785_C8_1_red_green.jpg)
![](https://images.proteinatlas.org/52592/785_C8_2_red_green.jpg)
![](https://images.proteinatlas.org/52592/868_F4_1_red_green.jpg)
![](https://images.proteinatlas.org/52592/868_F4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NWN3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NWN3 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 572..624; /note="F-box"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00080" |
| InterPro | IPR036047;IPR001810;IPR039594; |
| Pfam | PF12937; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000178974-FBXO34/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ALPP | Intact | false |
| COL8A1 | Intact | false |
| CUL1 | Biogrid | false |
| ERLEC1 | Bioplex | false |
| HNRNPU | Biogrid | false |
| HSP90AA1 | Biogrid | false |
| KRT40 | Intact | false |
| KRTAP10-11 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

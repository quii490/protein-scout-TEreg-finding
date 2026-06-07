---
type: protein-evaluation
gene: "DOLK"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DOLK 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DOLK / KIAA1094, TMEM15 |
| 蛋白名称 | Dolichol kinase |
| 蛋白大小 | 538 aa / 59.3 kDa |
| UniProt ID | Q9UPQ8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Nucleoli; 额外: Cytosol; UniProt: Endoplasmic reticulum membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 538 aa / 59.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=23 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=90.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR032974 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **114.0/180** | |
| **归一化总分** | | | **63.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli; 额外: Cytosol | Supported |
| UniProt | Endoplasmic reticulum membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- endoplasmic reticulum membrane (GO:0005789)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 23 |
| PubMed broad count | 432 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1094, TMEM15 |

**关键文献**:
1. CDG Therapies: From Bench to Bedside.. *International journal of molecular sciences*. PMID: 29702557
2. A Novel Compound Heterozygous Gene Mutation of Dolichol Kinase Deficiency (DOLK-CDG).. *Endocrine, metabolic & immune disorders drug targets*. PMID: 35674301
3. Perspectives on Retinal Dolichol Metabolism, and Visual Deficits in Dolichol Metabolism-Associated Inherited Disorders.. *Advances in experimental medicine and biology*. PMID: 37440071
4. Congenital Disorders of N-Linked Glycosylation and Multiple Pathway Overview.. **. PMID: 20301507
5. Phylogenetic analysis of promoter regions of human Dolichol kinase (DOLK) and orthologous genes using bioinformatics tools.. *Open life sciences*. PMID: 37250845

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.1 |
| 高置信度残基 (pLDDT>90) 占比 | 73.2% |
| 置信残基 (pLDDT 70-90) 占比 | 20.8% |
| 中等置信 (pLDDT 50-70) 占比 | 3.3% |
| 低置信 (pLDDT<50) 占比 | 2.6% |
| 有序区域 (pLDDT>70) 占比 | 94.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=90.1，有序区 94.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR032974 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DPM2 | 0.982 | 0.000 | — |
| DPM3 | 0.982 | 0.000 | — |
| SRD5A3 | 0.981 | 0.000 | — |
| DOLPP1 | 0.974 | 0.088 | — |
| DPAGT1 | 0.971 | 0.000 | — |
| ALG5 | 0.952 | 0.069 | — |
| PMM2 | 0.890 | 0.000 | — |
| CDIPT | 0.860 | 0.000 | — |
| CRLS1 | 0.847 | 0.000 | — |
| DPM1 | 0.817 | 0.075 | — |

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
| 三维结构 | AlphaFold pLDDT=90.1 + PDB: 无 | pLDDT=90.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane / Nucleoplasm, Nucleoli; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DOLK — Dolichol kinase，非常新颖，仅有少数基础研究。
2. 蛋白大小538 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 23 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UPQ8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000175283-DOLK/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DOLK
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UPQ8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000175283-DOLK/subcellular

![](https://images.proteinatlas.org/66767/1211_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/66767/1211_A3_2_red_green.jpg)
![](https://images.proteinatlas.org/66767/1217_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/66767/1217_A3_2_red_green.jpg)
![](https://images.proteinatlas.org/68706/1346_G11_3_red_green.jpg)
![](https://images.proteinatlas.org/68706/1346_G11_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UPQ8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UPQ8 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR032974; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000175283-DOLK/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| KCNA3 | Intact, Biogrid | true |
| KCNA6 | Intact, Biogrid, Bioplex | true |
| LRRC4C | Intact, Biogrid | true |
| APPBP2 | Intact | false |
| CD79A | Intact | false |
| CHODL | Intact | false |
| CREB3L1 | Intact | false |
| EDA | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

---
type: protein-evaluation
gene: "COG7"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## COG7 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COG7 |
| 蛋白名称 | Conserved oligomeric Golgi complex subunit 7 |
| 蛋白大小 | 770 aa / 86.3 kDa |
| UniProt ID | P83436 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Golgi apparatus; UniProt: Golgi apparatus membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 770 aa / 86.3 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=32 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=82.6; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR019335; Pfam: PF10191 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.5/180** | |
| **归一化总分** | | | **63.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus | Supported |
| UniProt | Golgi apparatus membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Golgi apparatus (GO:0005794)
- Golgi membrane (GO:0000139)
- Golgi transport complex (GO:0017119)
- nucleolus (GO:0005730)
- trans-Golgi network membrane (GO:0032588)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 32 |
| PubMed broad count | 50 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. COG7 deficiency in Drosophila generates multifaceted developmental, behavioral and protein glycosylation phenotypes.. *Journal of cell science*. PMID: 28883096
2. Mutations in Cog7 affect Golgi structure, meiotic cytokinesis and sperm development during Drosophila spermatogenesis.. *Journal of cell science*. PMID: 22946051
3. Congenital Disorders of N-Linked Glycosylation and Multiple Pathway Overview.. **. PMID: 20301507
4. COG-imposed Golgi functional integrity determines the onset of dark-induced senescence.. *Nature plants*. PMID: 37884654
5. Cog5-Cog7 crystal structure reveals interactions essential for the function of a multisubunit tethering complex.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 25331899

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.6 |
| 高置信度残基 (pLDDT>90) 占比 | 29.5% |
| 置信残基 (pLDDT 70-90) 占比 | 56.8% |
| 中等置信 (pLDDT 50-70) 占比 | 8.3% |
| 低置信 (pLDDT<50) 占比 | 5.5% |
| 有序区域 (pLDDT>70) 占比 | 86.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=82.6，有序区 86.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019335; Pfam: PF10191 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| COG8 | 0.999 | 0.857 | — |
| COG1 | 0.999 | 0.904 | — |
| COG3 | 0.999 | 0.930 | — |
| COG6 | 0.999 | 0.909 | — |
| COG5 | 0.999 | 0.920 | — |
| COG4 | 0.999 | 0.892 | — |
| COG2 | 0.999 | 0.910 | — |
| GOLGA5 | 0.964 | 0.000 | — |
| VPS53 | 0.893 | 0.000 | — |
| GOSR1 | 0.872 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| COG5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| COG3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| COG4 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| COG8 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| Hrs | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| COG1 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| COG2 | psi-mi:"MI:0096"(pull down) | pubmed:15932880|imex:IM-18939 |
| COG6 | psi-mi:"MI:0096"(pull down) | pubmed:15932880|imex:IM-18939 |
| SSA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSA2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.6 + PDB: 无 | pLDDT=82.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus membrane / Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. COG7 — Conserved oligomeric Golgi complex subunit 7，非常新颖，仅有少数基础研究。
2. 蛋白大小770 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 32 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P83436
- Protein Atlas: https://www.proteinatlas.org/ENSG00000168434-COG7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COG7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P83436
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (supported)。来源: https://www.proteinatlas.org/ENSG00000168434-COG7/subcellular

![](https://images.proteinatlas.org/40758/493_C6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/40758/493_C6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/40758/502_C6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/40758/502_C6_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/40758/557_C6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/40758/557_C6_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P83436-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P83436 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR019335; |
| Pfam | PF10191; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000168434-COG7/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| COG1 | Biogrid, Bioplex | true |
| COG2 | Biogrid, Bioplex | true |
| COG3 | Biogrid, Bioplex | true |
| COG5 | Intact, Biogrid | true |
| COG8 | Biogrid, Bioplex | true |
| TRAF5 | Biogrid, Bioplex | true |
| CD40 | Bioplex | false |
| CLOCK | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

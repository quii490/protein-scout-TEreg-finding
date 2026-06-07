---
type: protein-evaluation
gene: "FAM53B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM53B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM53B / KIAA0140, SMP |
| 蛋白名称 | Protein FAM53B |
| 蛋白大小 | 422 aa / 45.8 kDa |
| UniProt ID | Q14153 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 422 aa / 45.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=18 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=52.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029356; Pfam: PF15242 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 10 partners; IntAct 14 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 21 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0140, SMP |

**关键文献**:
1. Transcriptome profile of subsynaptic myonuclei at the neuromuscular junction in embryogenesis.. *Journal of neurochemistry*. PMID: 37994470
2. Fathers' preconception smoking and offspring DNA methylation.. *Clinical epigenetics*. PMID: 37649101
3. Clinical M2 macrophages-related genes to aid therapy in pancreatic ductal adenocarcinoma.. *Cancer cell international*. PMID: 34717651
4. FAM53B promotes pancreatic ductal adenocarcinoma metastasis by regulating macrophage M2 polarization.. *World journal of gastrointestinal oncology*. PMID: 38660645
5. Super-Enhancer Associated Five-Gene Risk Score Model Predicts Overall Survival in Multiple Myeloma Patients.. *Frontiers in cell and developmental biology*. PMID: 33344452

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 52.4 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 7.6% |
| 中等置信 (pLDDT 50-70) 占比 | 39.6% |
| 低置信 (pLDDT<50) 占比 | 52.8% |
| 有序区域 (pLDDT>70) 占比 | 7.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=52.4），有序残基占 7.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029356; Pfam: PF15242 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SFN | 0.612 | 0.612 | — |
| YWHAE | 0.595 | 0.595 | — |
| YWHAZ | 0.556 | 0.556 | — |
| CNIH3 | 0.550 | 0.000 | — |
| SNW1 | 0.510 | 0.000 | — |
| ZXDC | 0.483 | 0.000 | — |
| CYFIP2 | 0.462 | 0.000 | — |
| ZNF646 | 0.448 | 0.000 | — |
| KLK4 | 0.444 | 0.000 | — |
| MMP13 | 0.407 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| YWHAH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAZ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAQ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MEOX2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CBY1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| DYNLL1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| YWHAG | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |
| SFN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 10，IntAct interactions: 14
- 调控相关比例: 0 / 10 = 0%

**评价**: STRING 10 个预测互作，IntAct 14 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=52.4 + PDB: 无 | pLDDT=52.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Cytosol | 一致 |
| PPI | STRING + IntAct | 10 + 14 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FAM53B — Protein FAM53B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小422 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=52.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q14153
- Protein Atlas: https://www.proteinatlas.org/ENSG00000189319-FAM53B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM53B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14153
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000189319-FAM53B/subcellular

![](https://images.proteinatlas.org/37752/450_A3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/37752/450_A3_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/37752/453_A3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/37752/453_A3_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q14153-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q14153 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029356; |
| Pfam | PF15242; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000189319-FAM53B/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| YWHAE | Biogrid, Opencell | true |
| YWHAZ | Intact, Biogrid, Opencell | true |
| DYRK1A | Biogrid | false |
| SFN | Intact | false |
| YWHAG | Biogrid | false |
| YWHAH | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

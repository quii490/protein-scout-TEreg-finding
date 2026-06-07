---
type: protein-evaluation
gene: "YY1AP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## YY1AP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | YY1AP1 / HCCA2, YY1AP |
| 蛋白名称 | YY1-associated protein 1 |
| 蛋白大小 | 796 aa / 87.9 kDa |
| UniProt ID | Q9H869 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli fibrillar center; UniProt: Cytoplasm; Nucleus; Nucleus, nucleoplasm; Nucleus, nucleolus |
| 蛋白大小 | 10/10 | ×1 | 10 | 796 aa / 87.9 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=24 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=53.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR052435 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.0/180** | |
| **归一化总分** | | | **66.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli fibrillar center | Approved |
| UniProt | Cytoplasm; Nucleus; Nucleus, nucleoplasm; Nucleus, nucleolus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- fibrillar center (GO:0001650)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 24 |
| PubMed broad count | 509 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HCCA2, YY1AP |

**关键文献**:
1. Epigenetic regulation of autophagy-related genes: Implications for neurodevelopmental disorders.. *Autophagy*. PMID: 37674294
2. Prognostic significance of high YY1AP1 and PCNA expression in colon adenocarcinoma.. *Biochemical and biophysical research communications*. PMID: 29037809
3. Spontaneous Coronary Artery Dissection: Insights on Rare Genetic Variation From Genome Sequencing.. *Circulation. Genomic and precision medicine*. PMID: 33125268
4. Loss-of-Function Mutations in YY1AP1 Lead to Grange Syndrome and a Fibromuscular Dysplasia-Like Vascular Disease.. *American journal of human genetics*. PMID: 27939641
5. Integrative genomics identifies YY1AP1 as an oncogenic driver in EpCAM(+) AFP(+) hepatocellular carcinoma.. *Oncogene*. PMID: 25597408

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 53.7 |
| 高置信度残基 (pLDDT>90) 占比 | 14.4% |
| 置信残基 (pLDDT 70-90) 占比 | 16.5% |
| 中等置信 (pLDDT 50-70) 占比 | 6.9% |
| 低置信 (pLDDT<50) 占比 | 62.2% |
| 有序区域 (pLDDT>70) 占比 | 30.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=53.7），有序残基占 30.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052435 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ASH1L | 0.945 | 0.076 | — |
| YY1 | 0.823 | 0.523 | — |
| MCM3AP | 0.660 | 0.045 | — |
| ZNF496 | 0.647 | 0.551 | — |
| SS18L2 | 0.625 | 0.625 | — |
| ZNF579 | 0.622 | 0.612 | — |
| ZMYM4 | 0.579 | 0.472 | — |
| ACAD9 | 0.566 | 0.000 | — |
| SETDB1 | 0.465 | 0.076 | — |
| ZNF524 | 0.451 | 0.436 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EWSR1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ATXN1 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| ZFAT | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| PRKAB2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| MAPK14 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| ENSP00000295566.4 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| secA2 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| VHL | psi-mi:"MI:0018"(two hybrid) | pubmed:17986458 |
| bamB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| gltB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=53.7 + PDB: 无 | pLDDT=53.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Nucleus, nucleoplasm; Nucleus, / Nucleoli fibrillar center | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. YY1AP1 — YY1-associated protein 1，非常新颖，仅有少数基础研究。
2. 蛋白大小796 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 24 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=53.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H869
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163374-YY1AP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=YY1AP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H869
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli fibrillar center (approved)。来源: https://www.proteinatlas.org/ENSG00000163374-YY1AP1/subcellular

![](https://images.proteinatlas.org/64249/1164_B3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/64249/1164_B3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/64249/1174_B3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/64249/1174_B3_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/64249/1192_C3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/64249/1192_C3_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H869-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H869 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR052435; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000163374-YY1AP1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ATXN1 | Intact, Biogrid | true |
| EWSR1 | Intact, Biogrid | true |
| MAPK14 | Intact, Biogrid | true |
| MAD2L2 | Biogrid | false |
| SS18L2 | Biogrid | false |
| YY1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

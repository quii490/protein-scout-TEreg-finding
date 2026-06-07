---
type: protein-evaluation
gene: "FAM117B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM117B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM117B / ALS2CR13 |
| 蛋白名称 | Protein FAM117B |
| 蛋白大小 | 589 aa / 62.0 kDa |
| UniProt ID | Q6P1L5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Centrosome; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 589 aa / 62.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=52.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026642; Pfam: PF15388 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.5/180** | |
| **归一化总分** | | | **71.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Centrosome | Approved |
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
| PubMed strict count | 8 |
| PubMed broad count | 10 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ALS2CR13 |

**关键文献**:
1. FAM117B promotes gastric cancer growth and drug resistance by targeting the KEAP1/NRF2 signaling pathway.. *The Journal of clinical investigation*. PMID: 36719368
2. Inhibition of gastric adenocarcinoma proliferation by WSGC@MS: Role of KEAP1/NRF2 signaling pathway and autophagy regulation.. *Materials today. Bio*. PMID: 40688680
3. Genome-wide association study of cerebral small vessel disease reveals established and novel loci.. *Brain : a journal of neurology*. PMID: 31430377
4. Genome-wide association for sarcoidosis identifies novel risk loci and genetic heritability in African and European ancestries: a meta-analysis from the Finngen, Million Veteran Program, UK Biobank, and Biobank Japan datasets.. *Orphanet journal of rare diseases*. PMID: 41466414
5. Identification of Immune-Relevant Factors Conferring Sarcoidosis Genetic Risk.. *American journal of respiratory and critical care medicine*. PMID: 26051272

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 52.6 |
| 高置信度残基 (pLDDT>90) 占比 | 1.4% |
| 置信残基 (pLDDT 70-90) 占比 | 9.0% |
| 中等置信 (pLDDT 50-70) 占比 | 36.2% |
| 低置信 (pLDDT<50) 占比 | 53.5% |
| 有序区域 (pLDDT>70) 占比 | 10.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=52.6），有序残基占 10.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026642; Pfam: PF15388 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DYRK1A | 0.882 | 0.841 | — |
| DCAF7 | 0.779 | 0.597 | — |
| DYNLL1 | 0.695 | 0.673 | — |
| ICA1L | 0.655 | 0.000 | — |
| NBEAL1 | 0.654 | 0.000 | — |
| TSC22D2 | 0.637 | 0.627 | — |
| DYRK1B | 0.630 | 0.567 | — |
| RNF169 | 0.625 | 0.000 | — |
| DYNLL2 | 0.623 | 0.611 | — |
| TROAP | 0.606 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| DYRK1A | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |
| DYRK1B | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |
| YWHAH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAZ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAQ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAG | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAE | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| BANP | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=52.6 + PDB: 无 | pLDDT=52.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Centrosome | 待确认 |
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
1. FAM117B — Protein FAM117B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小589 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=52.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6P1L5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000138439-FAM117B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM117B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6P1L5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000138439-FAM117B/subcellular

![](https://images.proteinatlas.org/28746/1055_D10_1_red_green.jpg)
![](https://images.proteinatlas.org/28746/1055_D10_2_red_green.jpg)
![](https://images.proteinatlas.org/28746/1142_F9_1_red_green.jpg)
![](https://images.proteinatlas.org/28746/1142_F9_3_red_green.jpg)
![](https://images.proteinatlas.org/28746/1178_F7_1_red_green.jpg)
![](https://images.proteinatlas.org/28746/1178_F7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6P1L5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6P1L5 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR026642; |
| Pfam | PF15388; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000138439-FAM117B/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DCAF7 | Intact, Biogrid | true |
| DYNLL1 | Intact, Biogrid, Opencell | true |
| DYNLL2 | Intact, Biogrid, Opencell | true |
| KEAP1 | Intact, Biogrid | true |
| YWHAG | Biogrid, Opencell | true |
| AGR2 | Intact | false |
| ATP5PB | Intact | false |
| BANP | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

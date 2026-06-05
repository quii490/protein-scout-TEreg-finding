---
type: protein-evaluation
gene: "BCL7C"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BCL7C 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BCL7C / 无 |
| 蛋白名称 | B-cell CLL/lymphoma 7 protein family member C |
| 蛋白大小 | 217 aa / 23.5 kDa |
| UniProt ID | Q8WUZ0 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 03:32:29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 10/10 | x4 | 40 | HPA: Nucleoplasm |
| 蛋白大小 | 10/10 | x1 | 10 | 217 aa / 23.5 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=17 篇 (<=20->10) |
| 三维结构 | 5/10 | x3 | 15 | AlphaFold v6 pLDDT=62.4 |
| 调控结构域 | 5/10 | x2 | 10 | InterPro: 1; Pfam: 1; IPR006804 |
| PPI 网络 | 10/10 | x3 | 30 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 1.0 | STRING + IntAct 双源验证: +0.5; 结构域 + AlphaFold 质量: +0.5 |
| **原始总分** | | | **156.0/180** | |
| **归一化总分 (/1.83)** | | | **85.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoplasm | Approved |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- chromatin (GO:0000785)
- GBAF complex (GO:0140288)
- nucleoplasm (GO:0005654)
- SWI/SNF complex (GO:0016514)

**结论**: 核定位证据充分，多个数据源一致支持核定位，定位特异性高。

#### 3.2 蛋白大小评估

**评价**: 217 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17 |
| PubMed broad count | 21 |

**关键文献**:
1. Bcl7b and Bcl7c subunits of BAF chromatin remodeling complexes are largely dispensable for hematopoiesis.. *Experimental hematology*. PMID: 40187480
2. BCL7C suppresses ovarian cancer growth by inactivating mutant p53.. *Journal of molecular cell biology*. PMID: 33306126
3. Genome-wide association study identifies four pan-ancestry loci for suicidal ideation in the Million Veteran Program.. *PLoS genetics*. PMID: 36940203
4. The BCL7 gene family: deletion of BCL7B in Williams syndrome.. *Gene*. PMID: 9931421
5. Comprehensive synergy mapping links a BAF- and NSL-containing "supercomplex" to the transcriptional silencing of HIV-1.. *Cell reports*. PMID: 37682714

**评价**: 极度新颖，几乎未被系统研究（PubMed <= 20篇）。新颖性评分 10/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.4 |
| 高置信度残基 (pLDDT>90) 占比 | 15.7% |
| 置信残基 (pLDDT 70-90) 占比 | 8.3% |
| 中等置信 (pLDDT 50-70) 占比 | 46.1% |
| 低置信 (pLDDT<50) 占比 | 30.0% |
| 有序区域 (pLDDT>70) 占比 | 24.0% |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold中等质量预测（pLDDT=62.4），存在部分低置信区域。三维结构评分 5/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006804; Pfam: PF04714 |

**染色质调控潜力分析**: 存在 2 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score > 0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SMARCD3 | 0.991 | 0.840 | -- |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HIF1AN | anti tag coimmunoprecipitation | pubmed:29426014|imex:IM-26302|doi:10.1016/j.jmb.2018.01.021 |
| SMARCB1 | pull down | imex:IM-26463|pubmed:30108113 |
| BCL7A | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| DPF1 | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| ARID1A | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| MYO1B | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| PHACTR2 | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| ACTL6B | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| ACTL6A | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| GSN | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15

**评价**: 互作网络丰富：STRING 15 预测 + IntAct 15 实验互作。PPI 评分 10/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold v6 | pLDDT=62.4 | 单一来源 |
| 定位 | HPA | Nucleoplasm | 单一来源 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
**总分**: +1.0 / max +3

### 4. 总体评价

**归一化总分**: 85.2/100

**核心优势**:
1. BCL7C -- B-cell CLL/lymphoma 7 protein family member C，极度新颖，几乎未被系统研究（PubMed <= 20篇）。
2. 蛋白大小217 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。
3. 存在 2 个已知结构域，有明确的结构-功能切入点。
4. 核定位信号明确，多个数据源一致支持。

**风险/不确定性**:
1. 暂无PDB实验结构，结构证据完全依赖AlphaFold预测

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] 考虑通过AlphaFold预测 + MD模拟获取结构信息

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q8WUZ0
- Protein Atlas: https://www.proteinatlas.org/search/BCL7C
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BCL7C
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WUZ0
- STRING: https://string-db.org/network/9606.BCL7C
- Packet data timestamp: 2026-06-03 03:32:29

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000099385-BCL7C/subcellular

![](https://images.proteinatlas.org/52654/833_B10_1_red_green.jpg)
![](https://images.proteinatlas.org/52654/833_B10_2_red_green.jpg)
![](https://images.proteinatlas.org/52654/838_F12_2_red_green.jpg)
![](https://images.proteinatlas.org/52654/838_F12_3_red_green.jpg)
![](https://images.proteinatlas.org/52654/915_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/52654/915_E5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8WUZ0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

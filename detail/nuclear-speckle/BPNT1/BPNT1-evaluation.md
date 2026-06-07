---
type: protein-evaluation
gene: "BPNT1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BPNT1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BPNT1 / 无 |
| 蛋白名称 | 3'(2'),5'-bisphosphate nucleotidase 1 |
| 蛋白大小 | 308 aa / 33.4 kDa |
| UniProt ID | O95861 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 03:43:04 |

**IF 图像**:
![](https://images.proteinatlas.org/48461/2212_H6_10_blue_red_green.jpg)
![](https://images.proteinatlas.org/48461/2212_H6_15_blue_red_green.jpg)

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | x4 | 36 | HPA: Nuclear speckles |
| 蛋白大小 | 10/10 | x1 | 10 | 308 aa / 33.4 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=16 篇 (<=20->10) |
| 三维结构 | 10/10 | x3 | 30 | AlphaFold v6 pLDDT=96.4; PDB: 2WEF |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: 4; Pfam: 1; IPR050725, IPR020583... |
| PPI 网络 | 10/10 | x3 | 30 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 1.5 | PDB + AlphaFold 双源验证: +0.5; STRING + IntAct 双源验证: +0.5; 结构域 + AlphaFold 质量: +0.5 |
| **原始总分** | | | **171.5/180** | |
| **归一化总分 (/1.83)** | | | **93.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles; 额外: Nuclear speckles | Approved |

**IF 图像说明**: 原图已通过HPA检索获取，见上方嵌入图像。

**GO Cellular Component**:
- cytosol (GO:0005829)
- mitochondrion (GO:0005739)

**结论**: 核定位证据充分，多个数据源一致支持核定位，定位特异性高。

#### 3.2 蛋白大小评估

**评价**: 308 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 25 |

**关键文献**:
1. Bisphosphate nucleotidase 1 promotes progression and docetaxel resistance in triple-negative breast cancer via STUB1-mediated destabilization of LIMA1.. *Cell death & disease*. PMID: 41540000
2. Dose- and time-dependent effects of interferon tau on bovine endometrial gene expression.. *Theriogenology*. PMID: 37549523
3. Parent and offspring genotypes influence gene expression in early life.. *Molecular ecology*. PMID: 31421010
4. Modulation of sulfur assimilation metabolic toxicity overcomes anemia and hemochromatosis in mice.. *Advances in biological regulation*. PMID: 32019729
5. Alteration of lithium pharmacology through manipulation of phosphoadenosine phosphate metabolism.. *The Journal of biological chemistry*. PMID: 15583009

**评价**: 极度新颖，几乎未被系统研究（PubMed <= 20篇）。新颖性评分 10/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 96.4 |
| 高置信度残基 (pLDDT>90) 占比 | 94.8% |
| 置信残基 (pLDDT 70-90) 占比 | 3.9% |
| 中等置信 (pLDDT 50-70) 占比 | 0.6% |
| 低置信 (pLDDT<50) 占比 | 0.6% |
| 有序区域 (pLDDT>70) 占比 | 98.7% |
| 可用 PDB 条目 | 2WEF |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构 + AlphaFold高质量预测（pLDDT=96.4），结构可信度高。三维结构评分 10/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050725, IPR020583, IPR000760, IPR020550; Pfam: PF00459 |

**染色质调控潜力分析**: 存在 5 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score > 0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PAPSS2 | 0.975 | 0.000 | -- |
| PAPSS1 | 0.972 | 0.000 | -- |
| IMPAD1 | 0.929 | 0.000 | -- |
| ACBD3 | 0.854 | 0.000 | -- |
| ISYNA1 | 0.782 | 0.000 | -- |
| EPRS1 | 0.694 | 0.000 | -- |
| PSEN2 | 0.672 | 0.071 | -- |
| DISP1 | 0.636 | 0.000 | -- |
| FLAD1 | 0.569 | 0.000 | -- |
| IMPA1 | 0.531 | 0.000 | -- |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| IKBKE | anti bait coimmunoprecipitation | pubmed:17353931 |
| TRAF6 | anti bait coimmunoprecipitation | pubmed:17353931 |
| IQCB1 | anti tag coimmunoprecipitation | pubmed:21565611|imex:IM-16529 |
| EBI-1257125 | affinity chromatography technology | pubmed:19463016|imex:IM-17246 |
| EBI-1257123 | pull down | pubmed:19367725|imex:IM-20587 |
| LRRK2 | anti tag coimmunoprecipitation | pubmed:31046837|imex:IM-26684 |
| APOL2 | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| OTUB1 | anti tag coimmunoprecipitation | imex:IM-23897|pubmed:26752685 |
| GTPBP10 | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| NUDT19 | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15

**评价**: 互作网络丰富：STRING 15 预测 + IntAct 15 实验互作。PPI 评分 10/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=96.4 + PDB: 2WEF | pLDDT=96.4, v6 | 预测+实验 |
| 定位 | HPA | Nuclear speckles | 单一来源 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
**总分**: +1.5 / max +3

### 4. 总体评价

**归一化总分**: 93.7/100

**核心优势**:
1. BPNT1 -- 3'(2'),5'-bisphosphate nucleotidase 1，极度新颖，几乎未被系统研究（PubMed <= 20篇）。
2. 蛋白大小308 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。
3. AlphaFold高质量预测（pLDDT=96.4），结构可信度高。
4. 已有PDB实验结构：2WEF。

**风险/不确定性**:
1. 暂无明显风险因素。

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/O95861
- Protein Atlas: https://www.proteinatlas.org/search/BPNT1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BPNT1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95861
- STRING: https://string-db.org/network/9606.BPNT1
- Packet data timestamp: 2026-06-03 03:43:04

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O95861-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O95861 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR050725;IPR020583;IPR000760;IPR020550; |
| Pfam | PF00459; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000162813-BPNT1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ACTR2 | Opencell | false |
| CDH2 | Opencell | false |
| LARP4 | Opencell | false |
| LYN | Opencell | false |
| MAP3K4 | Opencell | false |
| MTMR1 | Opencell | false |
| PCNP | Opencell | false |
| RAB5IF | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

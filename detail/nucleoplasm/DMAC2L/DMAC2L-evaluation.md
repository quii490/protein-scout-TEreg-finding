---
type: protein-evaluation
gene: "DMAC2L"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DMAC2L 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DMAC2L / ATP5S, ATPW |
| 蛋白名称 | ATP synthase subunit s, mitochondrial |
| 蛋白大小 | 200 aa / 23.2 kDa |
| UniProt ID | Q99766 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Mitochondria; UniProt: Mitochondrion; Mitochondrion inner membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 200 aa / 23.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=91.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR032675 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **124.0/180** | |
| **归一化总分** | | | **68.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Mitochondria | Approved |
| UniProt | Mitochondrion; Mitochondrion inner membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- mitochondrial inner membrane (GO:0005743)
- mitochondrion (GO:0005739)
- proton-transporting ATP synthase complex (GO:0045259)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 5 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ATP5S, ATPW |

**关键文献**:
1. Transcriptional alterations of genes related to fertility decline in male rats induced by chronic sleep restriction.. *Systems biology in reproductive medicine*. PMID: 32040351
2. Identification of the role of immune-related genes in the diagnosis of bipolar disorder with metabolic syndrome through machine learning and comprehensive bioinformatics analysis.. *Frontiers in psychiatry*. PMID: 37860165

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.1 |
| 高置信度残基 (pLDDT>90) 占比 | 85.0% |
| 置信残基 (pLDDT 70-90) 占比 | 4.0% |
| 中等置信 (pLDDT 50-70) 占比 | 1.5% |
| 低置信 (pLDDT<50) 占比 | 9.5% |
| 有序区域 (pLDDT>70) 占比 | 89.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=91.1，有序区 89.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR032675 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ATP5PB | 0.998 | 0.994 | — |
| ATP5PD | 0.872 | 0.095 | — |
| ATP5MF | 0.841 | 0.000 | — |
| ATP5PO | 0.819 | 0.000 | — |
| ATP5MC3 | 0.818 | 0.000 | — |
| ATP5PF | 0.786 | 0.099 | — |
| ATP5ME | 0.786 | 0.095 | — |
| ATP5MC1 | 0.776 | 0.000 | — |
| ATP5F1C | 0.774 | 0.000 | — |
| ATP5F1B | 0.765 | 0.099 | — |

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
| 三维结构 | AlphaFold pLDDT=91.1 + PDB: 无 | pLDDT=91.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Mitochondrion; Mitochondrion inner membrane / Nucleoplasm, Mitochondria | 一致 |
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
1. DMAC2L — ATP synthase subunit s, mitochondrial，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小200 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q99766
- Protein Atlas: https://www.proteinatlas.org/ENSG00000125375-DMAC2L/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DMAC2L
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99766
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000125375-DMAC2L/subcellular

![](https://images.proteinatlas.org/62690/2212_G4_29_blue_red_green.jpg)
![](https://images.proteinatlas.org/62690/2212_G4_9_blue_red_green.jpg)
![](https://images.proteinatlas.org/62690/1199_D8_1_red_green.jpg)
![](https://images.proteinatlas.org/62690/1199_D8_3_red_green.jpg)
![](https://images.proteinatlas.org/62690/1232_D8_1_red_green.jpg)
![](https://images.proteinatlas.org/62690/1232_D8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q99766-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q99766 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR032675; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000125375-DMAC2L/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

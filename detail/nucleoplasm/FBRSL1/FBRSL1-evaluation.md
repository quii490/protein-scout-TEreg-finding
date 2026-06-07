---
type: protein-evaluation
gene: "FBRSL1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FBRSL1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBRSL1 / AUTS2L, KIAA1545, XTP9 |
| 蛋白名称 | Fibrosin-1-like protein |
| 蛋白大小 | 1045 aa / 110.9 kDa |
| UniProt ID | Q9HCM7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Cytosol; 额外: Plasma membrane; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 1045 aa / 110.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=45.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR023246; Pfam: PF15336 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **115/180** | |
| **归一化总分** | | | **63.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Plasma membrane | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 22 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: AUTS2L, KIAA1545, XTP9 |

**关键文献**:
1. De novo mutations in FBRSL1 cause a novel recognizable malformation and intellectual disability syndrome.. *Human genetics*. PMID: 32424618
2. Comparing a Novel Malformation Syndrome Caused by Pathogenic Variants in FBRSL1 to AUTS2 Syndrome.. *Frontiers in cell and developmental biology*. PMID: 34805182
3. Mapping cell diversity in human sporadic cerebral cavernous malformations.. *Gene*. PMID: 38788816
4. De novo truncating variant in the FBRSL1 gene caused neurodevelopmental disorders, epilepsy, congenital heart disease, and facial dysmorphism.. *Experimental neurology*. PMID: 41232796
5. Fbrsl1 is required for heart development in Xenopus laevis and de novo variants in FBRSL1 can cause human heart defects.. *Disease models & mechanisms*. PMID: 38501224

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 45.6 |
| 高置信度残基 (pLDDT>90) 占比 | 0.2% |
| 置信残基 (pLDDT 70-90) 占比 | 7.1% |
| 中等置信 (pLDDT 50-70) 占比 | 14.0% |
| 低置信 (pLDDT<50) 占比 | 78.8% |
| 有序区域 (pLDDT>70) 占比 | 7.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=45.6），有序残基占 7.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR023246; Pfam: PF15336 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RYBP | 0.888 | 0.848 | — |
| DCAF7 | 0.849 | 0.801 | — |
| YAF2 | 0.826 | 0.749 | — |
| CSNK2A2 | 0.825 | 0.810 | — |
| PCGF5 | 0.745 | 0.375 | — |
| PCGF3 | 0.731 | 0.375 | — |
| CSNK2A1 | 0.629 | 0.598 | — |
| CSNK2B | 0.518 | 0.422 | — |
| UPF1 | 0.501 | 0.000 | — |
| OR4N5 | 0.492 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=45.6 + PDB: 无 | pLDDT=45.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Cytosol; 额外: Plasma membrane | 待确认 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FBRSL1 — Fibrosin-1-like protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1045 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=45.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9HCM7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000112787-FBRSL1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBRSL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HCM7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000112787-FBRSL1/subcellular

![](https://images.proteinatlas.org/49880/722_C8_1_red_green.jpg)
![](https://images.proteinatlas.org/49880/722_C8_2_red_green.jpg)
![](https://images.proteinatlas.org/49880/726_C8_1_red_green.jpg)
![](https://images.proteinatlas.org/49880/726_C8_2_red_green.jpg)
![](https://images.proteinatlas.org/49880/732_C8_1_red_green.jpg)
![](https://images.proteinatlas.org/49880/732_C8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9HCM7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9HCM7 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR023246; |
| Pfam | PF15336; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000112787-FBRSL1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DCAF7 | Biogrid, Bioplex | true |
| CSNK2A1 | Biogrid | false |
| CSNK2A2 | Biogrid | false |
| FANCD2OS | Bioplex | false |
| NFIC | Biogrid | false |
| PCGF3 | Biogrid | false |
| PCGF5 | Biogrid | false |
| RNF2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

---
type: protein-evaluation
gene: "ADPRM"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ADPRM 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ADPRM / C17orf48 |
| 蛋白名称 | Manganese-dependent ADP-ribose/CDP-alcohol diphosphatase |
| 蛋白大小 | 342 aa / 39.5 kDa |
| UniProt ID | Q3LIE5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; UniProt: 无注释 |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 342 aa / 39.5 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=1 篇 (≤20→10) |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=94.5; PDB: 无 |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR004843, IPR029052, IPR041869; Pfam: PF00149 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 1 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- cytosol (GO:0005829)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1 |
| PubMed broad count | 5 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C17orf48 |

**关键文献**:
1. Combined transcriptome and metabolome analyses reveal the effects of selenium on the growth and quality of Lilium lancifolium.. *Frontiers in plant science*. PMID: 38828223

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.5 |
| 高置信度残基 (pLDDT>90) 占比 | 91.5% |
| 置信残基 (pLDDT 70-90) 占比 | 2.9% |
| 中等置信 (pLDDT 50-70) 占比 | 1.2% |
| 低置信 (pLDDT<50) 占比 | 4.4% |
| 有序区域 (pLDDT>70) 占比 | 94.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=94.5，有序区 94.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004843, IPR029052, IPR041869; Pfam: PF00149 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GPAM | 0.921 | 0.000 | — |
| GPD2 | 0.911 | 0.000 | — |
| PRPS1L1 | 0.904 | 0.000 | — |
| PRPS2 | 0.904 | 0.000 | — |
| PRPS1 | 0.904 | 0.000 | — |
| GPD1 | 0.902 | 0.000 | — |
| NUDT5 | 0.902 | 0.000 | — |
| PGM2 | 0.902 | 0.000 | — |
| GPD1L | 0.902 | 0.000 | — |
| GPAT4 | 0.901 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| rep | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:34232536|imex:IM-29365 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 1
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.5 + PDB: 无 | pLDDT=94.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 1 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ 

**核心优势**:
1. ADPRM — Manganese-dependent ADP-ribose/CDP-alcohol diphosphatase，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小342 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q3LIE5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000170222-ADPRM/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ADPRM
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q3LIE5
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 02:52:14

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000170222-ADPRM/subcellular

![](https://images.proteinatlas.org/69342/1757_F6_3_red_green.jpg)
![](https://images.proteinatlas.org/69342/1757_F6_4_red_green.jpg)
![](https://images.proteinatlas.org/69342/1776_D8_2_red_green.jpg)
![](https://images.proteinatlas.org/69342/1776_D8_3_red_green.jpg)
![](https://images.proteinatlas.org/69342/1822_G4_2_red_green.jpg)
![](https://images.proteinatlas.org/69342/1822_G4_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q3LIE5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q3LIE5 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR004843;IPR029052;IPR041869; |
| Pfam | PF00149; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000170222-ADPRM/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

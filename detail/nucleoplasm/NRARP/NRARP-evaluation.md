---
type: protein-evaluation
gene: "NRARP"
date: 2026-06-04
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NRARP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NRARP |
| 蛋白名称 | Notch-regulated ankyrin repeat-containing protein |
| 蛋白大小 | 114 aa / 12.5 kDa |
| UniProt ID | Q7Z6K4 |
| 评估日期 | 2026-06-04 |

**功能简介** (UniProt): Downstream effector of Notch signaling. Involved in the regulation of liver cancer cells self-renewal (PubMed:25985737). Involved in angiogenesis acting downstream of Notch at branch points to regulate vascular density. Proposed to integrate endothelial Notch and Wnt signaling to control stalk cell proliferation and to stablilize new endothelial connections during angiogenesis (PubMed:19154719). D...

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cytosol; 额外: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 114 aa / 12.5 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=36 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=83.9; PDB: 6PY8 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR002110, IPR036770, IPR051226; Pfam: PF12796 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **114.5/180** | |
| **归一化总分** | | | **63.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像**: HPA 记录中该基因有可用 IF 图像（`if_display_images_available`），但未生成本地 IF 嵌入。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 36 |
| PubMed broad count | 50 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. The Notch-regulated ankyrin repeat protein is required for proper anterior-posterior somite patterning in mice.. *Genesis (New York, N.Y. : 2000)*. PMID: 21998026
2. The Nrarp gene encodes an ankyrin-repeat protein that is transcriptionally regulated by the notch signaling pathway.. *Developmental biology*. PMID: 11783997
3. Nrarp coordinates endothelial Notch and Wnt signaling to control vessel density in angiogenesis.. *Developmental cell*. PMID: 19154719
4. Downregulation of Notch-regulated Ankyrin Repeat Protein Exerts Antitumor Activities against Growth of Thyroid Cancer.. *Chinese medical journal*. PMID: 27364790
5. Direct regulation of the Nrarp gene promoter by the Notch signaling pathway.. *Biochemical and biophysical research communications*. PMID: 15325262

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.9 |
| 高置信度残基 (pLDDT>90) 占比 | 50.0% |
| 置信残基 (pLDDT 70-90) 占比 | 31.6% |
| 中等置信 (pLDDT 50-70) 占比 | 16.7% |
| 低置信 (pLDDT<50) 占比 | 1.8% |
| 有序区域 (pLDDT>70) 占比 | 81.6% |
| 可用 PDB 条目 | 6PY8 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=83.9，有序区 81.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002110, IPR036770, IPR051226; Pfam: PF12796 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NOTCH1 | 0.975 | 0.905 | — |
| RBPJ | 0.960 | 0.902 | — |
| HEY1 | 0.835 | 0.071 | — |
| DTX1 | 0.773 | 0.053 | — |
| JAG1 | 0.749 | 0.098 | — |
| HES5 | 0.739 | 0.000 | — |
| DLL4 | 0.733 | 0.098 | — |
| MAML1 | 0.706 | 0.078 | — |
| NOTCH3 | 0.700 | 0.098 | — |
| LFNG | 0.696 | 0.043 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 3
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%，尚无实验验证互作。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.9 + PDB: 6PY8 | pLDDT=83.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Cytosol; 额外: Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 15 + 3 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. NRARP — Notch-regulated ankyrin repeat-containing protein，非常新颖，仅有少数基础研究。
2. 蛋白大小114 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 36 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z6K4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198435-NRARP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NRARP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7Z6K4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live via harvest pipeline; evaluated 2026-06-04

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7Z6K4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q7Z6K4 |
| SMART | SM00248; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR002110;IPR036770;IPR051226; |
| Pfam | PF12796; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000198435-NRARP/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| GTF2E1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

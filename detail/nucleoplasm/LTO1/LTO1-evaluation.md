---
type: protein-evaluation
gene: "LTO1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LTO1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LTO1 / ORAOV1, TAOS1 |
| 蛋白名称 | Protein LTO1 homolog |
| 蛋白大小 | 137 aa / 15.4 kDa |
| UniProt ID | Q8WV07 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 137 aa / 15.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=84.5; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR019191, IPR052436; Pfam: PF09811 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **141.5/180** | |
| **归一化总分** | | | **78.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 40 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ORAOV1, TAOS1 |

**关键文献**:
1. LTO1 and YAE1 regulate MHC-I expression via nonsense-mediated RNA decay in tumor cells.. *Journal for immunotherapy of cancer*. PMID: 40987494
2. A chloroplast membrane protein LTO1/AtVKOR involving in redox regulation and ROS homeostasis.. *Plant cell reports*. PMID: 23689258
3. Functional redox links between lumen thiol oxidoreductase1 and serine/threonine-protein kinase STN7.. *Plant physiology*. PMID: 33620491
4. The function of ORAOV1/LTO1, a gene that is overexpressed frequently in cancer: essential roles in the function and biogenesis of the ribosome.. *Oncogene*. PMID: 23318452
5. The chloroplast protein LTO1/AtVKOR is involved in the xanthophyll cycle and the acceleration of D1 protein degradation.. *Journal of photochemistry and photobiology. B, Biology*. PMID: 24300993

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.5 |
| 高置信度残基 (pLDDT>90) 占比 | 52.6% |
| 置信残基 (pLDDT 70-90) 占比 | 30.7% |
| 中等置信 (pLDDT 50-70) 占比 | 11.7% |
| 低置信 (pLDDT<50) 占比 | 5.1% |
| 有序区域 (pLDDT>70) 占比 | 83.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=84.5，有序区 83.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019191, IPR052436; Pfam: PF09811 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| YAE1 | 0.948 | 0.791 | — |
| ABCE1 | 0.913 | 0.840 | — |
| FGF19 | 0.910 | 0.000 | — |
| FGF3 | 0.768 | 0.000 | — |
| FGF4 | 0.767 | 0.000 | — |
| PYCR1 | 0.757 | 0.000 | — |
| PPFIA1 | 0.755 | 0.000 | — |
| CCND1 | 0.709 | 0.000 | — |
| MYEOV | 0.675 | 0.000 | — |
| MMS19 | 0.661 | 0.292 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| YAE1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| ATP7 | psi-mi:"MI:0096"(pull down) | pubmed:14690591 |
| BNI1 | psi-mi:"MI:0096"(pull down) | pubmed:14690591 |
| URB1 | psi-mi:"MI:0096"(pull down) | pubmed:14690591 |
| IRA1 | psi-mi:"MI:0096"(pull down) | pubmed:14690591 |
| SSA4 | psi-mi:"MI:0096"(pull down) | pubmed:14690591 |
| UBC7 | psi-mi:"MI:0397"(two hybrid array) | pubmed:14690591 |
| SSA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSA2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSB1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.5 + PDB: 无 | pLDDT=84.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. LTO1 — Protein LTO1 homolog，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小137 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WV07
- Protein Atlas: https://www.proteinatlas.org/ENSG00000149716-LTO1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LTO1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WV07
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000149716-LTO1/subcellular

![](https://images.proteinatlas.org/62696/1191_D11_1_red_green.jpg)
![](https://images.proteinatlas.org/62696/1191_D11_2_red_green.jpg)
![](https://images.proteinatlas.org/62696/1194_D11_1_red_green.jpg)
![](https://images.proteinatlas.org/62696/1194_D11_2_red_green.jpg)
![](https://images.proteinatlas.org/62696/1246_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/62696/1246_G5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8WV07-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8WV07 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR019191;IPR052436; |
| Pfam | PF09811; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000149716-LTO1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ABCE1 | Biogrid, Opencell | true |
| YAE1 | Intact, Biogrid | true |
| GSC2 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

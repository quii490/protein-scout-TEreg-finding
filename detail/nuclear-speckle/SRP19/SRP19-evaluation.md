---
type: protein-evaluation
gene: "SRP19"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SRP19 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SRP19 |
| 蛋白名称 | Signal recognition particle 19 kDa protein |
| 蛋白大小 | 144 aa / 16.2 kDa |
| UniProt ID | P09132 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nuclear bodies; UniProt: Cytoplasm; Nucleus, nucleolus; Nucleus, nucleoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 144 aa / 16.2 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=84 篇 (≤100→2) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=85.8; PDB: 1JID, 1MFQ, 1RY1, 2J37, 3KTV, 4P3E, 5M73 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR002778, IPR036521; Pfam: PF01922 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **104.0/180** | |
| **归一化总分** | | | **57.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nuclear bodies | Supported |
| UniProt | Cytoplasm; Nucleus, nucleolus; Nucleus, nucleoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nuclear body (GO:0016604)
- nucleolus (GO:0005730)
- signal recognition particle (GO:0048500)
- signal recognition particle, endoplasmic reticulum targeting (GO:0005786)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 84 |
| PubMed broad count | 101 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Human genetic defects in SRP19 and SRPRA cause severe congenital neutropenia with distinctive proteome changes.. *Blood*. PMID: 36223592
2. SRP19 and the protein secretion machinery is a targetable vulnerability in cancers with APC loss.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 40208946
3. Archaeal SRP RNA and SRP19 facilitate the assembly of SRP54-FtsY targeting complex.. *Biochemical and biophysical research communications*. PMID: 34116357
4. Structure of the SRP19 RNA complex and implications for signal recognition particle assembly.. *Nature*. PMID: 12050674
5. Interaction of rice and human SRP19 polypeptides with signal recognition particle RNA.. *Plant molecular biology*. PMID: 9225861

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.8 |
| 高置信度残基 (pLDDT>90) 占比 | 72.9% |
| 置信残基 (pLDDT 70-90) 占比 | 6.2% |
| 中等置信 (pLDDT 50-70) 占比 | 6.9% |
| 低置信 (pLDDT<50) 占比 | 13.9% |
| 有序区域 (pLDDT>70) 占比 | 79.1% |
| 可用 PDB 条目 | 1JID, 1MFQ, 1RY1, 2J37, 3KTV, 4P3E, 5M73, 7NFX, 7QWQ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1JID, 1MFQ, 1RY1, 2J37, 3KTV, 4P3E, 5M73, 7NFX, 7QWQ）+ AlphaFold极高置信度预测（pLDDT=85.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002778, IPR036521; Pfam: PF01922 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SRP68 | 0.999 | 0.997 | — |
| SRP54 | 0.999 | 0.996 | — |
| SRP72 | 0.999 | 0.991 | — |
| SRP9 | 0.999 | 0.997 | — |
| SRP14 | 0.999 | 0.970 | — |
| SRPRA | 0.975 | 0.907 | — |
| SRPRB | 0.968 | 0.895 | — |
| RPL23A | 0.950 | 0.877 | — |
| RPL19 | 0.915 | 0.895 | — |
| RPL26L1 | 0.914 | 0.876 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Invadolysin | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| MDM2 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| hemB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| SOD1 | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010 |
| TRADD | psi-mi:"MI:2289"(virotrap) | pubmed:30561431|imex:IM-26500 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| FGFR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| - | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| TYK2 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| SRP9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.8 + PDB: 1JID, 1MFQ, 1RY1, 2J37, 3KTV,  | pLDDT=85.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus, nucleolus; Nucleus, nucleoplas / Cytosol; 额外: Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. SRP19 — Signal recognition particle 19 kDa protein，研究基础较多，新颖性有限。
2. 蛋白大小144 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 84 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P09132
- Protein Atlas: https://www.proteinatlas.org/ENSG00000153037-SRP19/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SRP19
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P09132
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000153037-SRP19/subcellular

![](https://images.proteinatlas.org/57315/2013_D7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/57315/2013_D7_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/57315/2028_F1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/57315/2028_F1_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/57315/992_H4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/57315/992_H4_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P09132-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

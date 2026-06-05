---
type: protein-evaluation
gene: "XPOT"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## XPOT 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | XPOT |
| 蛋白名称 | Exportin-T |
| 蛋白大小 | 962 aa / 110.0 kDa |
| UniProt ID | O43592 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 962 aa / 110.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=20 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=91.4; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011989, IPR016024, IPR013598, IPR045546, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **136.5/180** | |
| **归一化总分** | | | **75.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Enhanced |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nuclear matrix (GO:0016363)
- nuclear pore (GO:0005643)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 20 |
| PubMed broad count | 50 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Exportin-T promotes tumor proliferation and invasion in hepatocellular carcinoma.. *Molecular carcinogenesis*. PMID: 30334580
2. Insights into the Structural Dynamics of Nucleocytoplasmic Transport of tRNA by Exportin-t.. *Biophysical journal*. PMID: 27028637
3. PAUSED encodes the Arabidopsis exportin-t ortholog.. *Plant physiology*. PMID: 12913168
4. TBK1 and flanking genes in human retina.. *Ophthalmic genetics*. PMID: 23421332
5. XPOT Disruption Suppresses TNBC Growth through Inhibition of Specific tRNA Nuclear Exportation and TTC19 Expression to Induce Cytokinesis Failure.. *International journal of biological sciences*. PMID: 37928256

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.4 |
| 高置信度残基 (pLDDT>90) 占比 | 75.7% |
| 置信残基 (pLDDT 70-90) 占比 | 22.3% |
| 中等置信 (pLDDT 50-70) 占比 | 2.0% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 98.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=91.4，有序区 98.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR013598, IPR045546, IPR001494; Pfam: PF19282, PF03810, PF08389 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RAN | 0.999 | 0.948 | — |
| XPO4 | 0.976 | 0.000 | — |
| XPO1 | 0.953 | 0.088 | — |
| CSE1L | 0.886 | 0.000 | — |
| RANGAP1 | 0.878 | 0.000 | — |
| NCBP1 | 0.872 | 0.000 | — |
| ADGRD1 | 0.857 | 0.820 | — |
| XPO5 | 0.832 | 0.071 | — |
| IPO7 | 0.830 | 0.000 | — |
| RANBP2 | 0.808 | 0.298 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Akt2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Ap3b1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| MAP3K3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| EGFR | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:15657067 |
| TNFRSF1A | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| TNFRSF1B | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| IQCB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:17314511 |
| Aire | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-13587|pubmed:20085707 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.4 + PDB: 无 | pLDDT=91.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm; 额外: Cytosol | 一致 |
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
1. XPOT — Exportin-T，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小962 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 20 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43592
- Protein Atlas: https://www.proteinatlas.org/ENSG00000184575-XPOT/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=XPOT
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43592
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000184575-XPOT/subcellular

![](https://images.proteinatlas.org/48067/700_H8_2_red_green.jpg)
![](https://images.proteinatlas.org/48067/700_H8_6_red_green.jpg)
![](https://images.proteinatlas.org/48067/824_D10_3_red_green.jpg)
![](https://images.proteinatlas.org/48067/824_D10_4_red_green.jpg)
![](https://images.proteinatlas.org/48067/884_D10_1_red_green.jpg)
![](https://images.proteinatlas.org/48067/884_D10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O43592-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

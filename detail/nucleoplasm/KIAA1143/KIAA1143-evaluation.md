---
type: protein-evaluation
gene: "KIAA1143"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KIAA1143 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KIAA1143 |
| 蛋白名称 | Uncharacterized protein KIAA1143 |
| 蛋白大小 | 154 aa / 17.5 kDa |
| UniProt ID | Q96AT1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytokinetic bridge; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 154 aa / 17.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=1 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=72.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR027911, IPR040219; Pfam: PF15377 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.0/180** | |
| **归一化总分** | | | **72.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytokinetic bridge | Enhanced |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1 |
| PubMed broad count | 1 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Weighted gene co-expression network analysis and drug-gene interaction bioinformatics uncover key genes associated with various presentations of malaria infection in African children and major drug candidates.. *Infection, genetics and evolution : journal of molecular epidemiology and evolutionary genetics in infectious diseases*. PMID: 33444859

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.3 |
| 高置信度残基 (pLDDT>90) 占比 | 16.2% |
| 置信残基 (pLDDT 70-90) 占比 | 38.3% |
| 中等置信 (pLDDT 50-70) 占比 | 35.1% |
| 低置信 (pLDDT<50) 占比 | 10.4% |
| 有序区域 (pLDDT>70) 占比 | 54.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=72.3，有序区 54.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027911, IPR040219; Pfam: PF15377 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TMEM204 | 0.721 | 0.000 | — |
| EAPP | 0.697 | 0.691 | — |
| CCDC12 | 0.669 | 0.591 | — |
| ECD | 0.636 | 0.628 | — |
| GPATCH1 | 0.632 | 0.627 | — |
| SNRNP200 | 0.629 | 0.627 | — |
| BUD31 | 0.628 | 0.609 | — |
| PPIE | 0.627 | 0.621 | — |
| KLF12 | 0.617 | 0.000 | — |
| WDR83 | 0.616 | 0.616 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NS | psi-mi:"MI:0018"(two hybrid) | imex:IM-13585|pubmed:20064372 |
| C1orf162 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LMNA | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| H3C1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| CEP76 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| FGB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| AQR | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CDC40 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SNRNP200 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PRPF6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.3 + PDB: 无 | pLDDT=72.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Cytokinetic bridge | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. KIAA1143 — Uncharacterized protein KIAA1143，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小154 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 1 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96AT1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163807-KIAA1143/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KIAA1143
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96AT1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000163807-KIAA1143/subcellular

![](https://images.proteinatlas.org/61799/1138_A6_1_red_green.jpg)
![](https://images.proteinatlas.org/61799/1138_A6_4_red_green.jpg)
![](https://images.proteinatlas.org/61799/1149_A6_1_red_green.jpg)
![](https://images.proteinatlas.org/61799/1149_A6_2_red_green.jpg)
![](https://images.proteinatlas.org/61799/1169_D3_4_red_green.jpg)
![](https://images.proteinatlas.org/61799/1169_D3_6_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96AT1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

---
type: protein-evaluation
gene: "SIX2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SIX2 — REJECTED (研究热度过高 (PubMed strict=221，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SIX2 |
| 蛋白名称 | Homeobox protein SIX2 |
| 蛋白大小 | 291 aa / 32.3 kDa |
| UniProt ID | Q9NPC8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Nuclear membrane; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 291 aa / 32.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=221 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=74.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001356, IPR017970, IPR009057, IPR031701; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **91.5/180** | |
| **归一化总分** | | | **50.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear membrane | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 221 |
| PubMed broad count | 431 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Transcriptional and open chromatin analysis of bovine skeletal muscle development by single-cell sequencing.. *Cell proliferation*. PMID: 36855961
2. A NIK-SIX signalling axis controls inflammation by targeted silencing of non-canonical NF-κB.. *Nature*. PMID: 30894749
3. Generation and characterization of Six2 conditional mice.. *Genesis (New York, N.Y. : 2000)*. PMID: 32277572
4. Crucial and Overlapping Roles of Six1 and Six2 in Craniofacial Development.. *Journal of dental research*. PMID: 30905259
5. Six2 regulates Pax9 expression, palatogenesis and craniofacial bone formation.. *Developmental biology*. PMID: 31765609

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.1 |
| 高置信度残基 (pLDDT>90) 占比 | 46.0% |
| 置信残基 (pLDDT 70-90) 占比 | 13.7% |
| 中等置信 (pLDDT 50-70) 占比 | 13.4% |
| 低置信 (pLDDT<50) 占比 | 26.8% |
| 有序区域 (pLDDT>70) 占比 | 59.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=74.1，有序区 59.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR017970, IPR009057, IPR031701; Pfam: PF00046, PF16878 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EYA1 | 0.972 | 0.670 | — |
| EYA2 | 0.940 | 0.606 | — |
| EYA3 | 0.881 | 0.576 | — |
| SALL1 | 0.862 | 0.000 | — |
| EYA4 | 0.795 | 0.673 | — |
| CITED1 | 0.784 | 0.000 | — |
| PAX2 | 0.784 | 0.000 | — |
| FOXD1 | 0.750 | 0.000 | — |
| WT1 | 0.735 | 0.048 | — |
| WNT9B | 0.711 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Eya1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-17347|pubmed:20956555 |
| CLIP4 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| TLE5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TLE3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| EYA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EYA4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CHMP2A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ANKRD17 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KPNB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PRKD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.1 + PDB: 无 | pLDDT=74.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Nuclear membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. SIX2 — Homeobox protein SIX2，研究基础较多，新颖性有限。
2. 蛋白大小291 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 221 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 221 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NPC8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000170577-SIX2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SIX2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NPC8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000170577-SIX2/subcellular

![](https://images.proteinatlas.org/56958/1060_H1_1_red_green.jpg)
![](https://images.proteinatlas.org/56958/1060_H1_3_red_green.jpg)
![](https://images.proteinatlas.org/56958/1105_H1_1_red_green.jpg)
![](https://images.proteinatlas.org/56958/1105_H1_2_red_green.jpg)
![](https://images.proteinatlas.org/56958/1165_F7_1_red_green.jpg)
![](https://images.proteinatlas.org/56958/1165_F7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NPC8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NPC8 |
| SMART | SM00389; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001356;IPR017970;IPR009057;IPR031701; |
| Pfam | PF00046;PF16878; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000170577-SIX2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CLIP4 | Intact | false |
| ERCC6L | Bioplex | false |
| EYA1 | Biogrid | false |
| EYA4 | Biogrid | false |
| KPNB1 | Bioplex | false |
| PSME3IP1 | Bioplex | false |
| PSMG3 | Bioplex | false |
| TLE3 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

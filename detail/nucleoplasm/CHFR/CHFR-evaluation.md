---
type: protein-evaluation
gene: "CHFR"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CHFR — REJECTED (研究热度过高 (PubMed strict=207，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CHFR / RNF196 |
| 蛋白名称 | E3 ubiquitin-protein ligase CHFR |
| 蛋白大小 | 664 aa / 73.4 kDa |
| UniProt ID | Q96EP1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear bodies, Microtubules; UniProt: Nucleus, PML body |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 664 aa / 73.4 kDa |
| 🆕 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=207 篇 (>100→REJECTED) |
| 🏗️ 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=72.0; PDB: 1LGP, 1LGQ, 2XOC, 2XOY, 2XOZ, 2XP0 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR040909, IPR052256, IPR000253, IPR008984, IPR001 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies, Microtubules | Uncertain |
| UniProt | Nucleus, PML body | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleus (GO:0005634)
- PML body (GO:0016605)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 207 |
| PubMed broad count | 309 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RNF196 |

**关键文献**:
1. CHFR and Paclitaxel Sensitivity of Ovarian Cancer.. *Cancers*. PMID: 34885153
2. FHA-RING ubiquitin ligases in cell division cycle control.. *Cellular and molecular life sciences : CMLS*. PMID: 18597043
3. DNMT1 is required for efficient DSB repair and maintenance of replication fork stability, and its loss reverses resistance to PARP inhibitors in cancer cells.. *Oncogene*. PMID: 40234721
4. Emerging evidence for CHFR as a cancer biomarker: from tumor biology to precision medicine.. *Cancer metastasis reviews*. PMID: 24375389
5. Association between CHFR gene hypermethylation and gastric cancer risk: a meta-analysis.. *OncoTargets and therapy*. PMID: 27994471

**评价**: 有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.0 |
| 高置信度残基 (pLDDT>90) 占比 | 47.9% |
| 置信残基 (pLDDT 70-90) 占比 | 14.2% |
| 中等置信 (pLDDT 50-70) 占比 | 4.2% |
| 低置信 (pLDDT<50) 占比 | 33.7% |
| 有序区域 (pLDDT>70) 占比 | 62.1% |
| 可用 PDB 条目 | 1LGP, 1LGQ, 2XOC, 2XOY, 2XOZ, 2XP0 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1LGP, 1LGQ, 2XOC, 2XOY, 2XOZ, 2XP0）+ AlphaFold预测（pLDDT=72.0），实验结构可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR040909, IPR052256, IPR000253, IPR008984, IPR001841; Pfam: PF00498, PF13923, PF17979 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| APLF | 0.979 | 0.000 | — |
| PARP1 | 0.897 | 0.830 | — |
| APTX | 0.830 | 0.000 | — |
| UBE2D2 | 0.825 | 0.778 | — |
| UBE2D3 | 0.792 | 0.612 | — |
| PLK1 | 0.784 | 0.634 | — |
| XRCC1 | 0.770 | 0.000 | — |
| LIG3 | 0.758 | 0.000 | — |
| UBE2D1 | 0.755 | 0.709 | — |
| UBE2N | 0.732 | 0.395 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EEF1G | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| BRD4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| GABBR1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ITGAE | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| WDR47 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| UBE2E3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| UBE2D4 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| UBE2W | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| UBE2D1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-11696|pubmed:19549727 |
| UBE2D2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-11696|pubmed:19549727 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.0 + PDB: 1LGP, 1LGQ, 2XOC, 2XOY, 2XOZ,  | pLDDT=72.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, PML body / Nuclear bodies, Microtubules | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CHFR — E3 ubiquitin-protein ligase CHFR，有一定研究基础，但仍存在niche空间。
2. 蛋白大小664 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 207 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 207 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96EP1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000072609-CHFR/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CHFR
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96EP1
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 04:54:38

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (uncertain)。来源: https://www.proteinatlas.org/ENSG00000072609-CHFR/subcellular

![](https://images.proteinatlas.org/45768/698_H9_1_red_green.jpg)
![](https://images.proteinatlas.org/45768/698_H9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96EP1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96EP1 |
| SMART | SM00240;SM00184; |
| UniProt Domain [FT] | DOMAIN 38..89; /note="FHA"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00086" |
| InterPro | IPR040909;IPR052256;IPR000253;IPR008984;IPR001841;IPR013083;IPR017907; |
| Pfam | PF00498;PF13923;PF17979; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000072609-CHFR/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PARP1 | Biogrid, Opencell | true |
| UBE2D1 | Intact, Biogrid | true |
| UBE2D2 | Intact, Biogrid | true |
| UBE2N | Intact, Biogrid | true |
| AURKA | Biogrid | false |
| GRB14 | Biogrid | false |
| HDAC1 | Biogrid | false |
| HDAC2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

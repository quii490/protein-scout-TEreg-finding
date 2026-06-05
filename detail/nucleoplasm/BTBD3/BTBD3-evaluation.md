---
type: protein-evaluation
gene: "BTBD3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BTBD3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BTBD3 / KIAA0952 |
| 蛋白名称 | BTB/POZ domain-containing protein 3 |
| 蛋白大小 | 522 aa / 58.4 kDa |
| UniProt ID | Q9Y2F9 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/BTBD3/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/BTBD3/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles; UniProt: Cytoplasm, cytosol; Nucleus |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 522 aa / 58.4 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=17 篇 (≤20→10) |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=83.5; PDB: 无 |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011705, IPR000210, IPR012983, IPR038648, IPR011 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **135.5/180** | |
| **归一化总分** | | | **75.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles | Supported |
| UniProt | Cytoplasm, cytosol; Nucleus | Swiss-Prot/TrEMBL |



**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17 |
| PubMed broad count | 21 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0952 |

**关键文献**:
1. Btbd3 expression regulates compulsive-like and exploratory behaviors in mice.. *Translational psychiatry*. PMID: 31501410
2. [Whole-transcriptome sequencing analysis of placental differential miRNA expression profile in Down syndrome].. *Nan fang yi ke da xue xue bao = Journal of Southern Medical University*. PMID: 35426807
3. E3 ubiquitin ligase BTBD3 inhibits tumorigenesis of colorectal cancer by regulating the TYRO3/Wnt/β-catenin signaling axis.. *Cancer cell international*. PMID: 39227913
4. Typing characteristics of metabolism-related genes in osteoporosis.. *Frontiers in pharmacology*. PMID: 36188607
5. Genetic Dissection of Temperament Personality Traits in Italian Isolates.. *Genes*. PMID: 35052345

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.5 |
| 高置信度残基 (pLDDT>90) 占比 | 71.5% |
| 置信残基 (pLDDT 70-90) 占比 | 9.2% |
| 中等置信 (pLDDT 50-70) 占比 | 3.1% |
| 低置信 (pLDDT<50) 占比 | 16.3% |
| 有序区域 (pLDDT>70) 占比 | 80.7% |
| 可用 PDB 条目 | 无 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=83.5，有序区 80.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011705, IPR000210, IPR012983, IPR038648, IPR011333; Pfam: PF07707, PF00651, PF08005 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TRIM2 | 0.545 | 0.000 | — |
| DLGAP1 | 0.500 | 0.000 | — |
| CUL3 | 0.491 | 0.456 | — |
| TASP1 | 0.485 | 0.000 | — |
| GMEB2 | 0.462 | 0.000 | — |
| BTBD6 | 0.449 | 0.437 | — |
| KIF16B | 0.443 | 0.000 | — |
| SYT1 | 0.432 | 0.000 | — |
| NAA25 | 0.421 | 0.000 | — |
| DOC2A | 0.419 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| D3DW19 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PLXNB3 | psi-mi:"MI:0018"(two hybrid) | pubmed:12421765 |
| dal1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| CDC37 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| UBE2I | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MEOX2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SUMO1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| RNF4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| BTBD6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CUL3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 14，IntAct interactions: 15
- 调控相关比例: 0 / 14 = 0%

**评价**: STRING 14 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.5 + PDB: 无 | pLDDT=83.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Nucleus / Vesicles | 一致 |
| PPI | STRING + IntAct | 14 + 15 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. BTBD3 — BTB/POZ domain-containing protein 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小522 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 17 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y2F9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000132640-BTBD3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BTBD3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y2F9
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 04:18:12

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y2F9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

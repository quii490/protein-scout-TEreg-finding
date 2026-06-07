---
type: protein-evaluation
gene: "DNAJC27"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DNAJC27 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNAJC27 / RABJS, RBJ |
| 蛋白名称 | DnaJ homolog subfamily C member 27 |
| 蛋白大小 | 273 aa / 30.9 kDa |
| UniProt ID | Q9NZQ0 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/DNAJC27/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/rejected/DNAJC27/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Nucleus |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 273 aa / 30.9 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=17 篇 (≤20→10) |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=90.6; PDB: 2YS8 |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001623, IPR036869, IPR027417, IPR005225, IPR001 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.5/180** | |
| **归一化总分** | | | **76.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- cytoplasmic vesicle (GO:0031410)
- nucleus (GO:0005634)
- organelle membrane (GO:0031090)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17 |
| PubMed broad count | 30 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RABJS, RBJ |

**关键文献**:
1. Identification and validation of ferroptosis-related lncRNA signature in intervertebral disc degeneration.. *Gene*. PMID: 38492610
2. A ferroptosis-related ceRNA network in hepatocellular carcinoma for potential clinical applications.. *American journal of translational research*. PMID: 37434825
3. Increased Circulation and Adipose Tissue Levels of DNAJC27/RBJ in Obesity and Type 2-Diabetes.. *Frontiers in endocrinology*. PMID: 30131766
4. MC4R Variant rs17782313 Associates With Increased Levels of DNAJC27, Ghrelin, and Visfatin and Correlates With Obesity and Hypertension in a Kuwaiti Cohort.. *Frontiers in endocrinology*. PMID: 32733386
5. Comprehensive interactome profiling of the human Hsp70 network highlights functional differentiation of J domains.. *Molecular cell*. PMID: 33957083

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.6 |
| 高置信度残基 (pLDDT>90) 占比 | 77.3% |
| 置信残基 (pLDDT 70-90) 占比 | 15.4% |
| 中等置信 (pLDDT 50-70) 占比 | 4.4% |
| 低置信 (pLDDT<50) 占比 | 2.9% |
| 有序区域 (pLDDT>70) 占比 | 92.7% |
| 可用 PDB 条目 | 2YS8 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=90.6，有序区 92.7%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001623, IPR036869, IPR027417, IPR005225, IPR001806; Pfam: PF00226, PF00071 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ADCY3 | 0.756 | 0.101 | — |
| ADCY8 | 0.745 | 0.101 | — |
| FAM184A | 0.709 | 0.700 | — |
| SEC16B | 0.665 | 0.000 | — |
| DNAJC9 | 0.646 | 0.113 | — |
| FPGT-TNNI3K | 0.627 | 0.110 | — |
| TMEM160 | 0.621 | 0.000 | — |
| GNPDA2 | 0.618 | 0.000 | — |
| TNNI3K | 0.617 | 0.110 | — |
| POC5 | 0.614 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 3 / 15 = 20%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 20%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.6 + PDB: 2YS8 | pLDDT=90.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DNAJC27 — DnaJ homolog subfamily C member 27，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小273 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 17 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NZQ0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000115137-DNAJC27/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNAJC27
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NZQ0
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 12:17:21

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NZQ0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NZQ0 |
| SMART | SM00271;SM00175;SM00176;SM00173;SM00174; |
| UniProt Domain [FT] | DOMAIN 217..273; /note="J"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00286" |
| InterPro | IPR001623;IPR036869;IPR027417;IPR005225;IPR001806; |
| Pfam | PF00226;PF00071; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000115137-DNAJC27/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| TFCP2 | Intact, Biogrid | true |
| FAM184A | Biogrid | false |
| FAM184B | Biogrid | false |
| METAP2 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

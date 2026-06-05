---
type: protein-evaluation
gene: "PDS5A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PDS5A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PDS5A / KIAA0648, PDS5 |
| 蛋白名称 | Sister chromatid cohesion protein PDS5 homolog A |
| 蛋白大小 | 1337 aa / 150.8 kDa |
| UniProt ID | Q29RF7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 5/10 | ×1 | 5 | 1337 aa / 150.8 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=32 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=81.8; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011989, IPR016024, IPR039776; Pfam: PF20168 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.5/180** | |
| **归一化总分** | | | **66.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- chromosome (GO:0005694)
- chromosome, centromeric region (GO:0000775)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 32 |
| PubMed broad count | 54 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0648, PDS5 |

**关键文献**:
1. The cohesin-associated protein Pds5A governs the meiotic spindle assembly via deubiquitination of Kif5B in oocytes.. *Science advances*. PMID: 40215310
2. PDS5A and PDS5B in Cohesin Function and Human Disease.. *International journal of molecular sciences*. PMID: 34070827
3. DCAF15 control of cohesin dynamics sustains acute myeloid leukemia.. *Nature communications*. PMID: 38961054
4. PDS5A and PDS5B differentially affect gene expression without altering cohesin localization across the genome.. *Epigenetics & chromatin*. PMID: 35986423
5. Cohesin mutations in myeloid malignancies.. *Blood*. PMID: 34157074

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.8 |
| 高置信度残基 (pLDDT>90) 占比 | 64.2% |
| 置信残基 (pLDDT 70-90) 占比 | 18.0% |
| 中等置信 (pLDDT 50-70) 占比 | 1.0% |
| 低置信 (pLDDT<50) 占比 | 16.8% |
| 有序区域 (pLDDT>70) 占比 | 82.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=81.8，有序区 82.2%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR039776; Pfam: PF20168 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| WAPL | 0.999 | 0.877 | — |
| STAG1 | 0.999 | 0.731 | — |
| STAG2 | 0.999 | 0.895 | — |
| RAD21 | 0.999 | 0.953 | — |
| CDCA5 | 0.999 | 0.709 | — |
| SMC3 | 0.999 | 0.936 | — |
| SMC1A | 0.998 | 0.927 | — |
| NIPBL | 0.998 | 0.321 | — |
| ESCO1 | 0.994 | 0.516 | — |
| MAU2 | 0.988 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| E9Q656 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| WAPL | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12007|pubmed:17113138 |
| SMC3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12007|pubmed:17113138 |
| STAG1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12007|pubmed:17113138 |
| STAG2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12007|pubmed:17113138 |
| SMC1A | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12007|pubmed:17113138 |
| RAD21 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12007|pubmed:17113138 |
| GSTK1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| BRF2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MYC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 2 / 15 = 13%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 13%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.8 + PDB: 无 | pLDDT=81.8, v6 | 仅预测 |
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

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PDS5A — Sister chromatid cohesion protein PDS5 homolog A，非常新颖，仅有少数基础研究。
2. 蛋白大小1337 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 32 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q29RF7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000121892-PDS5A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PDS5A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q29RF7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000121892-PDS5A/subcellular

![](https://images.proteinatlas.org/36661/551_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/36661/551_C10_2_red_green.jpg)
![](https://images.proteinatlas.org/36661/554_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/36661/554_C10_2_red_green.jpg)
![](https://images.proteinatlas.org/36661/560_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/36661/560_C10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q29RF7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

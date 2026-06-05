---
type: protein-evaluation
gene: "PDS5B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PDS5B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PDS5B / APRIN, AS3, KIAA0979 |
| 蛋白名称 | Sister chromatid cohesion protein PDS5 homolog B |
| 蛋白大小 | 1447 aa / 164.7 kDa |
| UniProt ID | Q9NTI5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 5/10 | ×1 | 5 | 1447 aa / 164.7 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=40 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=80.5; PDB: 5HDT |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011989, IPR016024, IPR039776; Pfam: PF20168 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **124.0/180** | |
| **归一化总分** | | | **68.9/100** | |

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

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 40 |
| PubMed broad count | 97 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: APRIN, AS3, KIAA0979 |

**关键文献**:
1. PDS5A and PDS5B in Cohesin Function and Human Disease.. *International journal of molecular sciences*. PMID: 34070827
2. PDS5A and PDS5B differentially affect gene expression without altering cohesin localization across the genome.. *Epigenetics & chromatin*. PMID: 35986423
3. A chromatin-remodeling-independent role for ATRX in protecting centromeric cohesion.. *The EMBO journal*. PMID: 40437074
4. Pds5A and Pds5B Display Non-redundant Functions in Mitosis and Their Loss Triggers Chk1 Activation.. *Frontiers in cell and developmental biology*. PMID: 32760717
5. Cohesin-mediated stabilization of the CCAN complex at kinetochores in mitosis.. *Current biology : CB*. PMID: 40730158

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.5 |
| 高置信度残基 (pLDDT>90) 占比 | 68.6% |
| 置信残基 (pLDDT 70-90) 占比 | 7.7% |
| 中等置信 (pLDDT 50-70) 占比 | 0.6% |
| 低置信 (pLDDT<50) 占比 | 23.1% |
| 有序区域 (pLDDT>70) 占比 | 76.3% |
| 可用 PDB 条目 | 5HDT |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=80.5，有序区 76.3%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR039776; Pfam: PF20168 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| WAPL | 0.999 | 0.984 | — |
| RAD21 | 0.998 | 0.967 | — |
| SMC1A | 0.997 | 0.927 | — |
| SMC3 | 0.997 | 0.943 | — |
| STAG2 | 0.996 | 0.857 | — |
| STAG1 | 0.990 | 0.916 | — |
| CDCA5 | 0.990 | 0.733 | — |
| NIPBL | 0.989 | 0.321 | — |
| PDS5A | 0.971 | 0.835 | — |
| BRCA2 | 0.939 | 0.563 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| WAPL | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12007|pubmed:17113138 |
| SMC3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12007|pubmed:17113138 |
| STAG1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12007|pubmed:17113138 |
| STAG2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12007|pubmed:17113138 |
| RAD21 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12007|pubmed:17113138 |
| SMC1A | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12007|pubmed:17113138 |
| MYC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| metA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| CDCA5 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:21111234|imex:IM-15284 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 3 / 15 = 20%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 20%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.5 + PDB: 5HDT | pLDDT=80.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PDS5B — Sister chromatid cohesion protein PDS5 homolog B，非常新颖，仅有少数基础研究。
2. 蛋白大小1447 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 40 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NTI5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000083642-PDS5B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PDS5B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NTI5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000083642-PDS5B/subcellular

![](https://images.proteinatlas.org/39513/421_C9_1_red_green.jpg)
![](https://images.proteinatlas.org/39513/421_C9_3_red_green.jpg)
![](https://images.proteinatlas.org/39513/425_C9_1_red_green.jpg)
![](https://images.proteinatlas.org/39513/425_C9_2_red_green.jpg)
![](https://images.proteinatlas.org/39513/427_C9_1_red_green.jpg)
![](https://images.proteinatlas.org/39513/427_C9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NTI5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

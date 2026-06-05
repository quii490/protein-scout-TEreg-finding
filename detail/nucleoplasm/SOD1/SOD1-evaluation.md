---
type: protein-evaluation
gene: "SOD1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SOD1 — REJECTED (研究热度过高 (PubMed strict=7083，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SOD1 |
| 蛋白名称 | Superoxide dismutase [Cu-Zn] |
| 蛋白大小 | 154 aa / 15.9 kDa |
| UniProt ID | P00441 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 154 aa / 15.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=7083 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=97.9; PDB: 1AZV, 1BA9, 1DSW, 1FUN, 1HL4, 1HL5, 1KMG |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR036423, IPR024134, IPR018152, IPR001424; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Enhanced |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- axon cytoplasm (GO:1904115)
- cytoplasm (GO:0005737)
- cytoplasmic vesicle (GO:0031410)
- cytosol (GO:0005829)
- dendrite cytoplasm (GO:0032839)
- dense core granule (GO:0031045)
- extracellular exosome (GO:0070062)
- extracellular region (GO:0005576)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7083 |
| PubMed broad count | 12536 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. SOD1 mutations associated with amyotrophic lateral sclerosis analysis of variant severity.. *Scientific reports*. PMID: 34996976
2. Silence superoxide dismutase 1 (SOD1): a promising therapeutic target for amyotrophic lateral sclerosis (ALS).. *Expert opinion on therapeutic targets*. PMID: 32125907
3. SOD1 Function and Its Implications for Amyotrophic Lateral Sclerosis Pathology: New and Renascent Themes.. *The Neuroscientist : a review journal bringing neurobiology, neurology and psychiatry*. PMID: 25492944
4. Tofersen.. **. PMID: 37603661
5. Amyotrophic lateral sclerosis caused by SOD1 variants: from genetic discovery to disease prevention.. *The Lancet. Neurology*. PMID: 39706636

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 97.9 |
| 高置信度残基 (pLDDT>90) 占比 | 98.1% |
| 置信残基 (pLDDT 70-90) 占比 | 1.9% |
| 中等置信 (pLDDT 50-70) 占比 | 0.0% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 100.0% |
| 可用 PDB 条目 | 1AZV, 1BA9, 1DSW, 1FUN, 1HL4, 1HL5, 1KMG, 1L3N, 1MFM, 1N18 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1AZV, 1BA9, 1DSW, 1FUN, 1HL4, 1HL5, 1KMG, 1L3N, 1MFM, 1N18）+ AlphaFold极高置信度预测（pLDDT=97.9），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036423, IPR024134, IPR018152, IPR001424; Pfam: PF00080 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CCS | 0.999 | 0.997 | — |
| BCL2 | 0.998 | 0.329 | — |
| PARK7 | 0.997 | 0.643 | — |
| VDAC1 | 0.996 | 0.000 | — |
| SOD2 | 0.994 | 0.661 | — |
| FUS | 0.992 | 0.000 | — |
| TARDBP | 0.989 | 0.000 | — |
| NEFL | 0.976 | 0.045 | — |
| HSPA5 | 0.975 | 0.236 | — |
| DERL1 | 0.964 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CCS1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| P32 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| sstn | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Chgb | psi-mi:"MI:0018"(two hybrid) | imex:IM-14528|pubmed:16369483 |
| Chga | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-14528|pubmed:16369483 |
| Tgoln1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-14528|pubmed:16369483 |
| Invs | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| SMAD2 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| EEF1D | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| Ccs | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9552|pubmed:19079254 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=97.9 + PDB: 1AZV, 1BA9, 1DSW, 1FUN, 1HL4,  | pLDDT=97.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
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
1. SOD1 — Superoxide dismutase [Cu-Zn]，研究基础较多，新颖性有限。
2. 蛋白大小154 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 7083 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 7083 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P00441
- Protein Atlas: https://www.proteinatlas.org/ENSG00000142168-SOD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SOD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P00441
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000142168-SOD1/subcellular

![](https://images.proteinatlas.org/1401/2166_A3_19_blue_red_green.jpg)
![](https://images.proteinatlas.org/1401/2166_A3_47_blue_red_green.jpg)
![](https://images.proteinatlas.org/1401/29_D2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/1401/29_D2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/1401/30_D2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/1401/30_D2_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P00441-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

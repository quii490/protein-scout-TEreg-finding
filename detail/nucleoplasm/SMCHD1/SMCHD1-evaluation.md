---
type: protein-evaluation
gene: "SMCHD1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SMCHD1 — REJECTED (研究热度过高 (PubMed strict=151，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SMCHD1 / KIAA0650 |
| 蛋白名称 | Structural maintenance of chromosomes flexible hinge domain-containing protein 1 |
| 蛋白大小 | 2005 aa / 226.4 kDa |
| UniProt ID | A6NHR9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: Nucleoplasm; 额外: Nuclear bodies; UniProt: Chromosome |
| 蛋白大小 | 2/10 | ×1 | 2 | 2005 aa / 226.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=151 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=80.8; PDB: 6MW7 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR036890, IPR058611, IPR058612, IPR058613, IPR058 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **85.0/180** | |
| **归一化总分** | | | **47.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear bodies | Supported |
| UniProt | Chromosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Barr body (GO:0001740)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- site of double-strand break (GO:0035861)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 151 |
| PubMed broad count | 203 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0650 |

**关键文献**:
1. Facioscapulohumeral muscular dystrophy.. *Handbook of clinical neurology*. PMID: 29478599
2. Facioscapulohumeral muscular dystrophy.. *Biochimica et biophysica acta*. PMID: 24882751
3. Facioscapulohumeral Muscular Dystrophy.. *Comprehensive Physiology*. PMID: 28915324
4. SMCHD1 has separable roles in chromatin architecture and gene silencing that could be targeted in disease.. *Nature communications*. PMID: 37749075
5. Facioscapulohumeral Muscular Dystrophies.. *Continuum (Minneapolis, Minn.)*. PMID: 31794465

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.8 |
| 高置信度残基 (pLDDT>90) 占比 | 19.5% |
| 置信残基 (pLDDT 70-90) 占比 | 68.1% |
| 中等置信 (pLDDT 50-70) 占比 | 7.6% |
| 低置信 (pLDDT<50) 占比 | 4.8% |
| 有序区域 (pLDDT>70) 占比 | 87.6% |
| 可用 PDB 条目 | 6MW7 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=80.8，有序区 87.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036890, IPR058611, IPR058612, IPR058613, IPR058614; Pfam: PF13589, PF26194, PF26195 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LRIF1 | 0.966 | 0.434 | — |
| DUX4 | 0.872 | 0.000 | — |
| EMILIN2 | 0.831 | 0.000 | — |
| CBX3 | 0.670 | 0.166 | — |
| PDS5A | 0.651 | 0.000 | — |
| MVB12A | 0.628 | 0.627 | — |
| NUDCD1 | 0.622 | 0.619 | — |
| METTL4 | 0.620 | 0.000 | — |
| ZSCAN4 | 0.588 | 0.045 | — |
| H4C6 | 0.587 | 0.510 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| rpoB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| VCAM1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-17358|pubmed:22623428 |
| ENSP00000326603.7 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| rnfB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| FN1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-14135|pubmed:19738201 |
| H3C1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| LMNA | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| GNL3L | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| SGTB | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| DACT2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.8 + PDB: 6MW7 | pLDDT=80.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Chromosome / Nucleoplasm; 额外: Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. SMCHD1 — Structural maintenance of chromosomes flexible hinge domain-containing protein 1，研究基础较多，新颖性有限。
2. 蛋白大小2005 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 151 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 151 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A6NHR9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000101596-SMCHD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SMCHD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A6NHR9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000101596-SMCHD1/subcellular

![](https://images.proteinatlas.org/39341/1949_A7_2_red_green.jpg)
![](https://images.proteinatlas.org/39341/1949_A7_3_red_green.jpg)
![](https://images.proteinatlas.org/39341/2173_B10_1_red_green.jpg)
![](https://images.proteinatlas.org/39341/2173_B10_5_red_green.jpg)
![](https://images.proteinatlas.org/39341/2214_B2_1_red_green.jpg)
![](https://images.proteinatlas.org/39341/2214_B2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A6NHR9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

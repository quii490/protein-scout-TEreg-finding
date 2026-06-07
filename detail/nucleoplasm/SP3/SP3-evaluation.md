---
type: protein-evaluation
gene: "SP3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SP3 — REJECTED (研究热度过高 (PubMed strict=1686，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SP3 |
| 蛋白名称 | Transcription factor Sp3 |
| 蛋白大小 | 781 aa / 81.9 kDa |
| UniProt ID | Q02447 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Nucleus, PML body |
| 蛋白大小 | 10/10 | ×1 | 10 | 781 aa / 81.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1686 篇 (>100→REJECTED) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v6 pLDDT=37.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036236, IPR013087; Pfam: PF00096 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **74.0/180** | |
| **归一化总分** | | | **41.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus; Nucleus, PML body | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- PML body (GO:0016605)
- protein-DNA complex (GO:0032993)
- transcription repressor complex (GO:0017053)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1686 |
| PubMed broad count | 5886 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Single-pot, solid-phase-enhanced sample preparation for proteomics experiments.. *Nature protocols*. PMID: 30464214
2. Endothelial Sp1/Sp3 are essential to the effect of captopril on blood pressure in male mice.. *Nature communications*. PMID: 37735515
3. Specificity Proteins (Sp) and Cancer.. *International journal of molecular sciences*. PMID: 36982239
4. Glucocorticoid receptor and specificity protein 1 (Sp1) or Sp3 transactivate HSV-1 ICP0 promoter sequences but a GC-rich binding antibiotic, Mithramycin A, impairs reactivation from latency.. *Virus research*. PMID: 39490590
5. Glucocorticoid receptor and specificity protein 1 (Sp1) or Sp3, but not the antibiotic Mithramycin A, stimulates human alphaherpesvirus 1 (HSV-1) replication.. *Antiviral research*. PMID: 38556059

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 37.9 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 10.9% |
| 中等置信 (pLDDT 50-70) 占比 | 2.6% |
| 低置信 (pLDDT<50) 占比 | 86.6% |
| 有序区域 (pLDDT>70) 占比 | 10.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=37.9），有序残基占 10.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036236, IPR013087; Pfam: PF00096 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SP1 | 0.912 | 0.835 | — |
| HDAC1 | 0.873 | 0.829 | — |
| ESR1 | 0.840 | 0.529 | — |
| HDAC2 | 0.827 | 0.644 | — |
| EP300 | 0.735 | 0.648 | — |
| E2F1 | 0.699 | 0.300 | — |
| NXNL1 | 0.696 | 0.000 | — |
| PUM2 | 0.691 | 0.095 | — |
| TP53 | 0.684 | 0.512 | — |
| RELA | 0.675 | 0.331 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSMUSP00000099750.4 | psi-mi:"MI:0413"(electrophoretic mobility shift as | pubmed:16339759|imex:IM-19639 |
| Ryr1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| WHR1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14667819|mint:MINT-5216 |
| Neto | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Hinfp | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Ar6 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| EBI-972534 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:16339759|imex:IM-19639 |
| GCH1 | psi-mi:"MI:0018"(two hybrid) | pubmed:16696853|imex:IM-20087 |
| ENSP00000310301.6 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:19505873|imex:IM-20483 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=37.9 + PDB: 无 | pLDDT=37.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, PML body / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. SP3 — Transcription factor Sp3，研究基础较多，新颖性有限。
2. 蛋白大小781 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1686 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=37.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1686 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q02447
- Protein Atlas: https://www.proteinatlas.org/ENSG00000172845-SP3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SP3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q02447
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000172845-SP3/subcellular

![](https://images.proteinatlas.org/32146/2013_D10_1_red_green.jpg)
![](https://images.proteinatlas.org/32146/2013_D10_2_red_green.jpg)
![](https://images.proteinatlas.org/32146/2064_H8_1_red_green.jpg)
![](https://images.proteinatlas.org/32146/2064_H8_3_red_green.jpg)
![](https://images.proteinatlas.org/32146/680_A9_1_red_green.jpg)
![](https://images.proteinatlas.org/32146/680_A9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q02447-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q02447 |
| SMART | SM00355; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR036236;IPR013087; |
| Pfam | PF00096; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000172845-SP3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ESR1 | Intact, Biogrid | true |
| GABPA | Intact, Biogrid | true |
| ABCB1 | Biogrid | false |
| CEBPB | Biogrid | false |
| CIB3 | Intact | false |
| E2F1 | Biogrid | false |
| EP300 | Biogrid | false |
| HDAC1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

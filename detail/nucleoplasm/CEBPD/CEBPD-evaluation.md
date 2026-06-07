---
type: protein-evaluation
gene: "CEBPD"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CEBPD — REJECTED (研究热度过高 (PubMed strict=273，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CEBPD |
| 蛋白名称 | CCAAT/enhancer-binding protein delta |
| 蛋白大小 | 269 aa / 28.5 kDa |
| UniProt ID | P49716 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 269 aa / 28.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=273 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR004827, IPR046347, IPR031106, IPR016468; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.0/180** | |
| **归一化总分** | | | **48.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- RNA polymerase II transcription regulator complex (GO:0090575)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 273 |
| PubMed broad count | 548 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Molecular and genetic insights into human ovarian aging from single-nuclei multi-omics analyses.. *Nature aging*. PMID: 39578560
2. Stabilization of E-cadherin adhesions by COX-2/GSK3β signaling is a targetable pathway in metastatic breast cancer.. *JCI insight*. PMID: 36757813
3. CEBPD is a master transcriptional factor for hypoxia regulated proteins in glioblastoma and augments hypoxia induced invasion through extracellular matrix-integrin mediated EGFR/PI3K pathway.. *Cell death & disease*. PMID: 37059730
4. Single-cell RNA sequencing identifies critical transcription factors of tumor cell invasion induced by hypoxia microenvironment in glioblastoma.. *Theranostics*. PMID: 37441593
5. NOX1 is essential for TNFα-induced intestinal epithelial ROS secretion and inhibits M cell signatures.. *Gut*. PMID: 36191961

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.1 |
| 高置信度残基 (pLDDT>90) 占比 | 23.4% |
| 置信残基 (pLDDT 70-90) 占比 | 11.2% |
| 中等置信 (pLDDT 50-70) 占比 | 34.2% |
| 低置信 (pLDDT<50) 占比 | 31.2% |
| 有序区域 (pLDDT>70) 占比 | 34.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=65.1），有序残基占 34.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004827, IPR046347, IPR031106, IPR016468; Pfam: PF07716 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CEBPB | 0.994 | 0.459 | — |
| KLF5 | 0.950 | 0.091 | — |
| PPARG | 0.925 | 0.045 | — |
| CELF1 | 0.908 | 0.000 | — |
| CELF3 | 0.900 | 0.000 | — |
| CELF2 | 0.893 | 0.000 | — |
| CELF4 | 0.891 | 0.000 | — |
| SMAD4 | 0.860 | 0.292 | — |
| TNNT2 | 0.832 | 0.000 | — |
| CELF5 | 0.831 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EEF1D | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| SNAP23 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| MYL3 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| EEF1B2 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| IDH2 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| BASP1 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| NOLC1 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| CCDC85B | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| CDC37 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| MTHFD1L | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.1 + PDB: 无 | pLDDT=65.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
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
1. CEBPD — CCAAT/enhancer-binding protein delta，研究基础较多，新颖性有限。
2. 蛋白大小269 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 273 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=65.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 273 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P49716
- Protein Atlas: https://www.proteinatlas.org/ENSG00000221869-CEBPD/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CEBPD
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P49716
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000221869-CEBPD/subcellular

![](https://images.proteinatlas.org/67581/1331_C11_2_red_green.jpg)
![](https://images.proteinatlas.org/67581/1331_C11_3_red_green.jpg)
![](https://images.proteinatlas.org/67581/1339_A5_2_red_green.jpg)
![](https://images.proteinatlas.org/67581/1339_A5_3_red_green.jpg)
![](https://images.proteinatlas.org/67581/1345_C11_3_red_green.jpg)
![](https://images.proteinatlas.org/67581/1345_C11_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P49716-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P49716 |
| SMART | SM00338; |
| UniProt Domain [FT] | DOMAIN 191..254; /note="bZIP"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00978" |
| InterPro | IPR004827;IPR046347;IPR031106;IPR016468; |
| Pfam | PF07716; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000221869-CEBPD/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FANCD2 | Intact, Biogrid | true |
| IPO4 | Intact, Biogrid | true |
| CEBPB | Biogrid | false |
| FBXW7 | Biogrid | false |
| HDAC1 | Biogrid | false |
| HDAC3 | Biogrid | false |
| SMAD3 | Biogrid | false |
| SMAD4 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

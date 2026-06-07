---
type: protein-evaluation
gene: "CREB3L1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CREB3L1 — REJECTED (研究热度过高 (PubMed strict=165，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CREB3L1 / OASIS |
| 蛋白名称 | Cyclic AMP-responsive element-binding protein 3-like protein 1 |
| 蛋白大小 | 519 aa / 57.0 kDa |
| UniProt ID | Q96BA8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Endoplasmic reticulum membrane; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 519 aa / 57.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=165 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR004827, IPR046347; Pfam: PF00170 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Endoplasmic reticulum membrane; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 165 |
| PubMed broad count | 269 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: OASIS |

**关键文献**:
1. Sclerosing Epithelioid Fibrosarcoma.. *Surgical pathology clinics*. PMID: 38278601
2. C5a-C5aR1 induces endoplasmic reticulum stress to accelerate vascular calcification via PERK-eIF2α-ATF4-CREB3L1 pathway.. *Cardiovascular research*. PMID: 37603848
3. CREB3L1 deficiency impairs odontoblastic differentiation and molar dentin deposition partially through the TMEM30B.. *International journal of oral science*. PMID: 39384739
4. Sclerosing epithelioid fibrosarcoma.. *Wiener medizinische Wochenschrift (1946)*. PMID: 27631873
5. CREB3L1 facilitates pancreatic tumor progression and reprograms intratumoral tumor-associated macrophages to shape an immunotherapy-resistance microenvironment.. *Journal for immunotherapy of cancer*. PMID: 39762079

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.1 |
| 高置信度残基 (pLDDT>90) 占比 | 12.5% |
| 置信残基 (pLDDT 70-90) 占比 | 7.5% |
| 中等置信 (pLDDT 50-70) 占比 | 23.3% |
| 低置信 (pLDDT<50) 占比 | 56.6% |
| 有序区域 (pLDDT>70) 占比 | 20.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=55.1），有序残基占 20.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004827, IPR046347; Pfam: PF00170 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CREB3L2 | 0.955 | 0.514 | — |
| CREB3L3 | 0.950 | 0.345 | — |
| CREB3 | 0.947 | 0.321 | — |
| CREB1 | 0.938 | 0.101 | — |
| ATF6B | 0.931 | 0.071 | — |
| ATF4 | 0.929 | 0.000 | — |
| CREB3L4 | 0.928 | 0.000 | — |
| MBTPS2 | 0.926 | 0.000 | — |
| CREBBP | 0.923 | 0.073 | — |
| CREB5 | 0.919 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MRPL12 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| TMEM218 | psi-mi:"MI:0397"(two hybrid array) | pubmed:29892012|doi:10.1038/s4 |
| GPR25 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| TMEM147 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| TSPO | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| FAM3C | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| PLP1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CSGALNACT2 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| TMEM120B | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| SLC13A3 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.1 + PDB: 无 | pLDDT=55.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
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
1. CREB3L1 — Cyclic AMP-responsive element-binding protein 3-like protein 1，研究基础较多，新颖性有限。
2. 蛋白大小519 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 165 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=55.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 165 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96BA8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000157613-CREB3L1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CREB3L1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96BA8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000157613-CREB3L1/subcellular

![](https://images.proteinatlas.org/62116/1241_C7_2_red_green.jpg)
![](https://images.proteinatlas.org/62116/1241_C7_4_red_green.jpg)
![](https://images.proteinatlas.org/62116/1245_C7_1_red_green.jpg)
![](https://images.proteinatlas.org/62116/1245_C7_2_red_green.jpg)
![](https://images.proteinatlas.org/62116/1743_H10_18_cr57fe209ee29bb_red_green.jpg)
![](https://images.proteinatlas.org/62116/1743_H10_27_cr57fe20a9219aa_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96BA8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96BA8 |
| SMART | SM00338; |
| UniProt Domain [FT] | DOMAIN 290..353; /note="bZIP"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00978" |
| InterPro | IPR004827;IPR046347; |
| Pfam | PF00170; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000157613-CREB3L1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PGAP2 | Intact, Biogrid | true |
| PLP1 | Intact, Biogrid | true |
| PRKAB2 | Intact, Biogrid | true |
| TMEM218 | Intact, Biogrid | true |
| ADGRE2 | Intact | false |
| ADIPOQ | Intact | false |
| AGPAT3 | Intact | false |
| AGPAT4 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

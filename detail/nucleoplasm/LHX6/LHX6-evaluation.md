---
type: protein-evaluation
gene: "LHX6"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## LHX6 — REJECTED (研究热度过高 (PubMed strict=108，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LHX6 / LHX6.1 |
| 蛋白名称 | LIM/homeobox protein Lhx6 |
| 蛋白大小 | 363 aa / 40.0 kDa |
| UniProt ID | Q9UPM6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 363 aa / 40.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=108 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001356, IPR017970, IPR009057, IPR050453, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.0/180** | |
| **归一化总分** | | | **48.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 108 |
| PubMed broad count | 234 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: LHX6.1 |

**关键文献**:
1. Lhx6 deficiency causes human embryonic palatal mesenchymal cell mitophagy dysfunction in cleft palate.. *Molecular medicine (Cambridge, Mass.)*. PMID: 39438838
2. Downregulation of tumor-suppressor gene LHX6 in cancer: a systematic review.. *Romanian journal of internal medicine = Revue roumaine de medecine interne*. PMID: 29533904
3. Modulation of pain sensitivity by Ascl1- and Lhx6-dependent GABAergic neuronal function in streptozotocin diabetic mice.. *Molecular therapy : the journal of the American Society of Gene Therapy*. PMID: 39741412
4. The development of MGE-derived cortical interneurons: An Lhx6 tale.. *The International journal of developmental biology*. PMID: 34881792
5. The exon 12-containing LHX6 isoforms promote cervical cancer cell proliferation by regulating the MAPK signaling pathway.. *Cancer medicine*. PMID: 35384355

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.1 |
| 高置信度残基 (pLDDT>90) 占比 | 38.8% |
| 置信残基 (pLDDT 70-90) 占比 | 14.3% |
| 中等置信 (pLDDT 50-70) 占比 | 7.7% |
| 低置信 (pLDDT<50) 占比 | 39.1% |
| 有序区域 (pLDDT>70) 占比 | 53.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=67.1），有序残基占 53.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR017970, IPR009057, IPR050453, IPR001781; Pfam: PF00046, PF00412 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LDB1 | 0.966 | 0.836 | — |
| PDE1C | 0.890 | 0.000 | — |
| RAB2A | 0.827 | 0.054 | — |
| SST | 0.814 | 0.000 | — |
| NKX2-1 | 0.807 | 0.045 | — |
| SSBP4 | 0.798 | 0.797 | — |
| SSBP3 | 0.794 | 0.794 | — |
| DLX2 | 0.793 | 0.045 | — |
| CALB2 | 0.768 | 0.100 | — |
| PVALB | 0.764 | 0.100 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| LDB1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| FIGLA | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| KLF3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ROR2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| NRF1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CPNE1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ZNF138 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| FAM90A1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ZNF76 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SSBP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.1 + PDB: 无 | pLDDT=67.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
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
1. LHX6 — LIM/homeobox protein Lhx6，研究基础较多，新颖性有限。
2. 蛋白大小363 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 108 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=67.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 108 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UPM6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000106852-LHX6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LHX6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UPM6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000106852-LHX6/subcellular

![](https://images.proteinatlas.org/2269/2180_F7_1_red_green.jpg)
![](https://images.proteinatlas.org/2269/2180_F7_2_red_green.jpg)
![](https://images.proteinatlas.org/2269/2198_H5_1_red_green.jpg)
![](https://images.proteinatlas.org/2269/2198_H5_2_red_green.jpg)
![](https://images.proteinatlas.org/2269/2208_D1_1_red_green.jpg)
![](https://images.proteinatlas.org/2269/2208_D1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UPM6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

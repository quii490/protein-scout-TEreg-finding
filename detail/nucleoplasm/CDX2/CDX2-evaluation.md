---
type: protein-evaluation
gene: "CDX2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CDX2 — REJECTED (研究热度过高 (PubMed strict=1799，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CDX2 / CDX3 |
| 蛋白名称 | Homeobox protein CDX-2 |
| 蛋白大小 | 313 aa / 33.5 kDa |
| UniProt ID | Q99626 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Vesicles, Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 313 aa / 33.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1799 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.6; PDB: 5LTY, 6ES2, 6ES3, 7Q4N |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR006820, IPR047152, IPR001356, IPR020479, IPR017 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 10 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **86.0/180** | |
| **归一化总分** | | | **47.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles, Cytosol | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- condensed nuclear chromosome (GO:0000794)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- transcription repressor complex (GO:0017053)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1799 |
| PubMed broad count | 3884 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CDX3 |

**关键文献**:
1. CDX2 inhibits the proliferation and tumor formation of colon cancer cells by suppressing Wnt/β-catenin signaling via transactivation of GSK-3β and Axin2 expression.. *Cell death & disease*. PMID: 30631044
2. Cdx2 Animal Models Reveal Developmental Origins of Cancers.. *Genes*. PMID: 31739541
3. CDX2 and Reg IV expression and correlation in gastric cancer.. *BMC gastroenterology*. PMID: 33639844
4. Alpha lipoamide inhibits diabetic kidney fibrosis via improving mitochondrial function and regulating RXRα expression and activation.. *Acta pharmacologica Sinica*. PMID: 36347997
5. Expression and significance of CDX2, FXR, and TGR5 in esophageal cancer.. *International journal of clinical and experimental pathology*. PMID: 36237638

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.6 |
| 高置信度残基 (pLDDT>90) 占比 | 19.2% |
| 置信残基 (pLDDT 70-90) 占比 | 7.3% |
| 中等置信 (pLDDT 50-70) 占比 | 35.5% |
| 低置信 (pLDDT<50) 占比 | 38.0% |
| 有序区域 (pLDDT>70) 占比 | 26.5% |
| 可用 PDB 条目 | 5LTY, 6ES2, 6ES3, 7Q4N |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=61.6），有序残基占 26.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006820, IPR047152, IPR001356, IPR020479, IPR017970; Pfam: PF04731, PF00046 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| H1-5 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| KRTAP4-12 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CFAP206 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ENSP00000370408.6 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:22326557|imex:IM-24349 |
| MEP1A | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:22326557|imex:IM-24349 |
| Zfp292 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| Alx4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| Dlx5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| Hltf | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| ENST00000381020 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 10
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 10 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.6 + PDB: 5LTY, 6ES2, 6ES3, 7Q4N | pLDDT=61.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Vesicles, Cytosol | 一致 |
| PPI | STRING + IntAct | 0 + 10 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CDX2 — Homeobox protein CDX-2，研究基础较多，新颖性有限。
2. 蛋白大小313 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1799 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=61.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1799 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q99626
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165556-CDX2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CDX2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99626
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000165556-CDX2/subcellular

![](https://images.proteinatlas.org/45669/1027_E11_4_red_green.jpg)
![](https://images.proteinatlas.org/45669/1027_E11_6_red_green.jpg)
![](https://images.proteinatlas.org/45669/681_A11_1_red_green.jpg)
![](https://images.proteinatlas.org/45669/681_A11_2_red_green.jpg)
![](https://images.proteinatlas.org/45669/765_E6_1_red_green.jpg)
![](https://images.proteinatlas.org/45669/765_E6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q99626-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q99626 |
| SMART | SM00389; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR006820;IPR047152;IPR001356;IPR020479;IPR017970;IPR009057;IPR000047; |
| Pfam | PF04731;PF00046; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000165556-CDX2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ATM | Biogrid | false |
| CFAP206 | Intact | false |
| EP300 | Biogrid | false |
| KDM5B | Biogrid | false |
| KRTAP4-12 | Intact | false |
| PAX6 | Biogrid | false |
| RELA | Biogrid | false |
| SMARCA2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

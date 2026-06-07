---
type: protein-evaluation
gene: "RRM2B"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## RRM2B — REJECTED (研究热度过高 (PubMed strict=113，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RRM2B / P53R2 |
| 蛋白名称 | Ribonucleoside-diphosphate reductase subunit M2 B |
| 蛋白大小 | 351 aa / 40.7 kDa |
| UniProt ID | Q7LG56 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 351 aa / 40.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=113 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=85.5; PDB: 2VUX, 3HF1, 4DJN |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR009078, IPR012348, IPR033909, IPR030475, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **93.0/180** | |
| **归一化总分** | | | **51.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Enhanced |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- mitochondrion (GO:0005739)
- nucleoplasm (GO:0005654)
- ribonucleoside-diphosphate reductase complex (GO:0005971)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 113 |
| PubMed broad count | 260 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: P53R2 |

**关键文献**:
1. Mitochondrial Retinopathy.. *Ophthalmology. Retina*. PMID: 34257060
2. New perspective in diagnostics of mitochondrial disorders: two years' experience with whole-exome sequencing at a national paediatric centre.. *Journal of translational medicine*. PMID: 27290639
3. Phenotypic and Genotypic Heterogeneity of RRM2B Variants.. *Neuropediatrics*. PMID: 29241262
4. Gene aberrations of RRM1 and RRM2B and outcome of advanced breast cancer after treatment with docetaxel with or without gemcitabine.. *BMC cancer*. PMID: 24215511
5. Mitochondrial DNA maintenance defects.. *Biochimica et biophysica acta. Molecular basis of disease*. PMID: 28215579

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.5 |
| 高置信度残基 (pLDDT>90) 占比 | 74.6% |
| 置信残基 (pLDDT 70-90) 占比 | 6.3% |
| 中等置信 (pLDDT 50-70) 占比 | 5.4% |
| 低置信 (pLDDT<50) 占比 | 13.7% |
| 有序区域 (pLDDT>70) 占比 | 80.9% |
| 可用 PDB 条目 | 2VUX, 3HF1, 4DJN |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2VUX, 3HF1, 4DJN）+ AlphaFold高质量预测（pLDDT=85.5），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009078, IPR012348, IPR033909, IPR030475, IPR000358; Pfam: PF00268 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RRM1 | 0.999 | 0.902 | — |
| RRM2 | 0.997 | 0.816 | — |
| TP53 | 0.992 | 0.625 | — |
| POLG | 0.943 | 0.000 | — |
| AK9 | 0.941 | 0.000 | — |
| DTYMK | 0.941 | 0.000 | — |
| AK3 | 0.937 | 0.000 | — |
| GUK1 | 0.934 | 0.000 | — |
| POLG2 | 0.932 | 0.000 | — |
| DGUOK | 0.932 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000251810.3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:25502805|imex:IM-26175| |
| RNF41 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-25511|pubmed:25910212 |
| RRM1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TMOD2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FZR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| INPPL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SPAG9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TPM2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RRM2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ORC4 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.5 + PDB: 2VUX, 3HF1, 4DJN | pLDDT=85.5, v6 | 预测+实验 |
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
1. RRM2B — Ribonucleoside-diphosphate reductase subunit M2 B，研究基础较多，新颖性有限。
2. 蛋白大小351 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 113 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 113 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7LG56
- Protein Atlas: https://www.proteinatlas.org/ENSG00000048392-RRM2B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RRM2B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7LG56
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/RRM2B/IF_images/RRM2B_IF_red_green.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000048392-RRM2B/subcellular

![](https://images.proteinatlas.org/28812/273_E7_1_red_green.jpg)
![](https://images.proteinatlas.org/28812/273_E7_2_red_green.jpg)
![](https://images.proteinatlas.org/28812/274_E7_1_red_green.jpg)
![](https://images.proteinatlas.org/28812/274_E7_2_red_green.jpg)
![](https://images.proteinatlas.org/28812/275_E7_1_red_green.jpg)
![](https://images.proteinatlas.org/28812/275_E7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7LG56-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q7LG56 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR009078;IPR012348;IPR033909;IPR030475;IPR000358; |
| Pfam | PF00268; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000048392-RRM2B/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ATM | Intact | false |
| CDKN1A | Biogrid | false |
| CSNK2A1 | Biogrid | false |
| MDM2 | Biogrid | false |
| ORC4 | Intact | false |
| RNF41 | Intact | false |
| RRM1 | Biogrid | false |
| RRM2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

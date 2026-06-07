---
type: protein-evaluation
gene: "NFKBIZ"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NFKBIZ — REJECTED (研究热度过高 (PubMed strict=136，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NFKBIZ / IKBZ, INAP, MAIL |
| 蛋白名称 | NF-kappa-B inhibitor zeta |
| 蛋白大小 | 718 aa / 78.1 kDa |
| UniProt ID | Q9BYH8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; 额外: Cytoplasmic bodies; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 718 aa / 78.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=136 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.7; PDB: 9BOR |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR002110, IPR036770, IPR047571; Pfam: PF12796 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 11 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.5/180** | |
| **归一化总分** | | | **44.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles; 额外: Cytoplasmic bodies | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasmic ribonucleoprotein granule (GO:0036464)
- nuclear speck (GO:0016607)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 136 |
| PubMed broad count | 284 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: IKBZ, INAP, MAIL |

**关键文献**:
1. Membrane Fusion-Mediated Loading of Therapeutic siRNA into Exosome for Tissue-Specific Application.. *Advanced materials (Deerfield Beach, Fla.)*. PMID: 38889294
2. Identification of core genes in intervertebral disc degeneration using bioinformatics and machine learning algorithms.. *Frontiers in immunology*. PMID: 39050860
3. Regulation of lymphoid-myeloid lineage bias through regnase-1/3-mediated control of Nfkbiz.. *Blood*. PMID: 37922454
4. Regulation of NFKBIZ gene promoter activity by STAT3, C/EBPβ, and STAT1.. *Biochemical and biophysical research communications*. PMID: 35537286
5. Analyses of non-coding somatic drivers in 2,658 cancer whole genomes.. *Nature*. PMID: 32025015

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.7 |
| 高置信度残基 (pLDDT>90) 占比 | 24.8% |
| 置信残基 (pLDDT 70-90) 占比 | 15.5% |
| 中等置信 (pLDDT 50-70) 占比 | 5.0% |
| 低置信 (pLDDT<50) 占比 | 54.7% |
| 有序区域 (pLDDT>70) 占比 | 40.3% |
| 可用 PDB 条目 | 9BOR |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=57.7），有序残基占 40.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002110, IPR036770, IPR047571; Pfam: PF12796 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NFKB1 | 0.988 | 0.364 | — |
| RELA | 0.969 | 0.098 | — |
| AKIRIN2 | 0.928 | 0.095 | — |
| STAT3 | 0.859 | 0.363 | — |
| REL | 0.840 | 0.098 | — |
| RELB | 0.832 | 0.098 | — |
| ZC3H12A | 0.831 | 0.292 | — |
| NFKB2 | 0.830 | 0.423 | — |
| PLAAT5 | 0.790 | 0.000 | — |
| TNFAIP3 | 0.788 | 0.049 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NFKB1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| STAT3 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| ERP29 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| IL6 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | imex:IM-24629|pubmed:26226212 |
| NFKB2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| Elf5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| Ehf | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| Ikbkg | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| ENST00000326172 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 11
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 11 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.7 + PDB: 9BOR | pLDDT=57.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nuclear speckles; 额外: Cytoplasmic bodies | 一致 |
| PPI | STRING + IntAct | 15 + 11 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. NFKBIZ — NF-kappa-B inhibitor zeta，研究基础较多，新颖性有限。
2. 蛋白大小718 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 136 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=57.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 136 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BYH8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000144802-NFKBIZ/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NFKBIZ
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BYH8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (supported)。来源: https://www.proteinatlas.org/ENSG00000144802-NFKBIZ/subcellular

![](https://images.proteinatlas.org/75363/1541_B6_1_red_green.jpg)
![](https://images.proteinatlas.org/75363/1541_B6_2_red_green.jpg)
![](https://images.proteinatlas.org/75363/1542_B6_1_red_green.jpg)
![](https://images.proteinatlas.org/75363/1542_B6_2_red_green.jpg)
![](https://images.proteinatlas.org/75363/1638_E2_1_red_green.jpg)
![](https://images.proteinatlas.org/75363/1638_E2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BYH8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BYH8 |
| SMART | SM00248; |
| UniProt Domain [FT] | DOMAIN 108..130; /note="OCA"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01347" |
| InterPro | IPR002110;IPR036770;IPR047571; |
| Pfam | PF12796; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000144802-NFKBIZ/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| NFKB1 | Biogrid | false |
| STAT3 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

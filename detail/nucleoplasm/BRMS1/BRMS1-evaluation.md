---
type: protein-evaluation
gene: "BRMS1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BRMS1 — REJECTED (研究热度过高 (PubMed strict=159，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BRMS1 |
| 蛋白名称 | Breast cancer metastasis-suppressor 1 |
| 蛋白大小 | 246 aa / 28.5 kDa |
| UniProt ID | Q9HCU9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Centrosome; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 246 aa / 28.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=159 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=78.6; PDB: 2XUS, 4AUV |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR013907; Pfam: PF08598 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.5/180** | |
| **归一化总分** | | | **49.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Centrosome | Approved |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- Sin3-type complex (GO:0070822)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 159 |
| PubMed broad count | 227 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. BRMS1 in Gliomas-An Expression Analysis.. *Cancers*. PMID: 37296870
2. Exploring the prognostic value of BRMS1 + microglia based on single-cell anoikis regulator patterns in the immunologic microenvironment of GBM.. *Journal of neuro-oncology*. PMID: 39143438
3. BRMS1 gene expression may be associated with clinico-pathological features of breast cancer.. *Bioscience reports*. PMID: 28533425
4. [Expression of gene BRMS1 and CD44v6 protein in supraglottic laryngeal carcinoma and its clinical significance].. *Lin chuang er bi yan hou tou jing wai ke za zhi = Journal of clinical otorhinolaryngology head and neck surgery*. PMID: 19621595
5. Location, location, location: the BRMS1 protein and melanoma progression.. *BMC medicine*. PMID: 22356729

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.6 |
| 高置信度残基 (pLDDT>90) 占比 | 50.8% |
| 置信残基 (pLDDT 70-90) 占比 | 9.8% |
| 中等置信 (pLDDT 50-70) 占比 | 23.2% |
| 低置信 (pLDDT<50) 占比 | 16.3% |
| 有序区域 (pLDDT>70) 占比 | 60.6% |
| 可用 PDB 条目 | 2XUS, 4AUV |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2XUS, 4AUV）+ AlphaFold高质量预测（pLDDT=78.6），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013907; Pfam: PF08598 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ARID4A | 0.999 | 0.811 | — |
| HDAC1 | 0.992 | 0.853 | — |
| SAP30 | 0.987 | 0.784 | — |
| SIN3A | 0.983 | 0.810 | — |
| ING2 | 0.978 | 0.828 | — |
| ING1 | 0.976 | 0.732 | — |
| SINHCAF | 0.958 | 0.733 | — |
| SIN3B | 0.952 | 0.642 | — |
| RBBP7 | 0.948 | 0.741 | — |
| ARID4B | 0.929 | 0.095 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.6 + PDB: 2XUS, 4AUV | pLDDT=78.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Centrosome | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. BRMS1 — Breast cancer metastasis-suppressor 1，研究基础较多，新颖性有限。
2. 蛋白大小246 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 159 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 159 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9HCU9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000174744-BRMS1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BRMS1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HCU9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Centrosome (approved)。来源: https://www.proteinatlas.org/ENSG00000174744-BRMS1/subcellular

![](https://images.proteinatlas.org/19637/174_E12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/19637/174_E12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/19637/175_E12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/19637/175_E12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/19637/176_E12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/19637/176_E12_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9HCU9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9HCU9 |
| SMART | SM01401; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR013907; |
| Pfam | PF08598; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000174744-BRMS1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ARID4A | Intact, Biogrid | true |
| DNAJB6 | Intact, Biogrid | true |
| HDAC1 | Intact, Biogrid, Bioplex | true |
| HDAC2 | Intact, Biogrid | true |
| NMI | Intact, Biogrid | true |
| RBBP7 | Biogrid, Bioplex | true |
| SAP30 | Biogrid, Bioplex | true |
| SINHCAF | Biogrid, Bioplex | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

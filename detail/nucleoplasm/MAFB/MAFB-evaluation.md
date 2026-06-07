---
type: protein-evaluation
gene: "MAFB"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MAFB — REJECTED (研究热度过高 (PubMed strict=480，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MAFB / KRML |
| 蛋白名称 | Transcription factor MafB |
| 蛋白大小 | 323 aa / 35.8 kDa |
| UniProt ID | Q9Y5Q3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Nucleoli, Golgi apparatus, Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 323 aa / 35.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=480 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR004827, IPR004826, IPR046347, IPR013592, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.0/180** | |
| **归一化总分** | | | **48.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli, Golgi apparatus, Cytosol | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)
- RNA polymerase II transcription regulator complex (GO:0090575)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 480 |
| PubMed broad count | 834 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KRML |

**关键文献**:
1. Single-cell RNA-Seq analysis reveals cell subsets and gene signatures associated with rheumatoid arthritis disease activity.. *JCI insight*. PMID: 38954480
2. Molecular Pathogenesis of Multiple Myeloma: Clinical Implications.. *Hematology/oncology clinics of North America*. PMID: 38199896
3. MafB-restricted local monocyte proliferation precedes lung interstitial macrophage differentiation.. *Nature immunology*. PMID: 36928411
4. Duane Syndrome.. **. PMID: 20301369
5. Microglia development follows a stepwise program to regulate brain homeostasis.. *Science (New York, N.Y.)*. PMID: 27338705

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.6 |
| 高置信度残基 (pLDDT>90) 占比 | 28.5% |
| 置信残基 (pLDDT 70-90) 占比 | 3.4% |
| 中等置信 (pLDDT 50-70) 占比 | 21.7% |
| 低置信 (pLDDT<50) 占比 | 46.4% |
| 有序区域 (pLDDT>70) 占比 | 31.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=62.6），有序残基占 31.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004827, IPR004826, IPR046347, IPR013592, IPR008917; Pfam: PF03131, PF08383 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| JUN | 0.991 | 0.132 | — |
| FOS | 0.983 | 0.633 | — |
| ETS1 | 0.870 | 0.000 | — |
| CTCF | 0.857 | 0.045 | — |
| NKX6-1 | 0.813 | 0.000 | — |
| IRF6 | 0.806 | 0.000 | — |
| BACH1 | 0.766 | 0.741 | — |
| IRF8 | 0.763 | 0.000 | — |
| NCOA6 | 0.761 | 0.297 | — |
| CCND3 | 0.750 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000362410.2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| ZWINT | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| KRTAP4-2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CCL2 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:22820162|imex:IM-23654 |
| EBI-10049836 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:22820162|imex:IM-23654 |
| EBI-2677274 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | imex:IM-24736|pubmed:24472656 |
| IL7R | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | imex:IM-24736|pubmed:24472656 |
| STAT3 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | imex:IM-24736|pubmed:24472656 |
| TMED8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ERBIN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.6 + PDB: 无 | pLDDT=62.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Nucleoli, Golgi apparatus, Cytoso | 一致 |
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
1. MAFB — Transcription factor MafB，研究基础较多，新颖性有限。
2. 蛋白大小323 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 480 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=62.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 480 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y5Q3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000204103-MAFB/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MAFB
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y5Q3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000204103-MAFB/subcellular

![](https://images.proteinatlas.org/5653/1179_A1_1_red_green.jpg)
![](https://images.proteinatlas.org/5653/1179_A1_2_red_green.jpg)
![](https://images.proteinatlas.org/5653/1790_C1_2_red_green.jpg)
![](https://images.proteinatlas.org/5653/1790_C1_4_red_green.jpg)
![](https://images.proteinatlas.org/5653/32_F6_1_red_green.jpg)
![](https://images.proteinatlas.org/5653/32_F6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y5Q3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9Y5Q3 |
| SMART | SM00338; |
| UniProt Domain [FT] | DOMAIN 238..301; /note="bZIP"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00978" |
| InterPro | IPR004827;IPR004826;IPR046347;IPR013592;IPR008917;IPR024874; |
| Pfam | PF03131;PF08383; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000204103-MAFB/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BACH1 | Intact, Biogrid | true |
| DDB1 | Biogrid | false |
| FOS | Intact | false |
| IRF3 | Intact | false |
| KRTAP4-2 | Intact | false |
| MAF | Intact | false |
| USP7 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

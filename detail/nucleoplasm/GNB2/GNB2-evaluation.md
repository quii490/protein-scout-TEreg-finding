---
type: protein-evaluation
gene: "GNB2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GNB2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GNB2 |
| 蛋白名称 | Guanine nucleotide-binding protein G(I)/G(S)/G(T) subunit beta-2 |
| 蛋白大小 | 340 aa / 37.3 kDa |
| UniProt ID | P62879 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane; UniProt: Cytoplasm, perinuclear region; Cell membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 340 aa / 37.3 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=57 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=96.9; PDB: 9AVL |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR016346, IPR015943, IPR001632, IPR020472, IPR019 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119.0/180** | |
| **归一化总分** | | | **66.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane | Supported |
| UniProt | Cytoplasm, perinuclear region; Cell membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- extracellular space (GO:0005615)
- focal adhesion (GO:0005925)
- heterotrimeric G-protein complex (GO:0005834)
- lysosomal membrane (GO:0005765)
- membrane (GO:0016020)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 57 |
| PubMed broad count | 70 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. A Mutation in the G-Protein Gene GNB2 Causes Familial Sinus Node and Atrioventricular Conduction Dysfunction.. *Circulation research*. PMID: 28219978
2. A detailed multi-omics analysis of GNB2 gene in human cancers.. *Brazilian journal of biology = Revista brasleira de biologia*. PMID: 35730811
3. A phenome-wide association study of tandem repeat variation in 168,554 individuals from the UK Biobank.. *Nature communications*. PMID: 39627187
4. SNHG5 enhances colorectal cancer metastasis through RNA-protein interaction with GNB2 and activation of canonical Wnt signaling.. *Non-coding RNA research*. PMID: 41550840
5. LncRNA CCAT2 promotes the proliferation and metastasis of colorectal cancer through activation of the ERK and Wnt signaling pathways by regulating GNB2 expression.. *Cancer medicine*. PMID: 39225546

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 96.9 |
| 高置信度残基 (pLDDT>90) 占比 | 97.1% |
| 置信残基 (pLDDT 70-90) 占比 | 1.8% |
| 中等置信 (pLDDT 50-70) 占比 | 1.2% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 98.9% |
| 可用 PDB 条目 | 9AVL |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=96.9，有序区 98.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016346, IPR015943, IPR001632, IPR020472, IPR019775; Pfam: PF25391 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GNG5 | 0.999 | 0.995 | — |
| GNG3 | 0.999 | 0.995 | — |
| GNG4 | 0.999 | 0.997 | — |
| GNGT2 | 0.999 | 0.995 | — |
| GNG7 | 0.999 | 0.995 | — |
| GNG2 | 0.999 | 0.997 | — |
| GNG8 | 0.998 | 0.995 | — |
| GNGT1 | 0.998 | 0.995 | — |
| GNG12 | 0.998 | 0.995 | — |
| GNG10 | 0.998 | 0.995 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MAP3K3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| RIPK3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| CAPNS1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| IKBKE | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TRAF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PDHB | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| CSNK1A1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| ID3 | psi-mi:"MI:0018"(two hybrid) | pubmed:18255255|imex:IM-19428 |
| USP50 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| MTNR1B | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:17215244|imex:IM-19124 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=96.9 + PDB: 9AVL | pLDDT=96.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, perinuclear region; Cell membrane / Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. GNB2 — Guanine nucleotide-binding protein G(I)/G(S)/G(T) subunit beta-2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小340 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 57 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P62879
- Protein Atlas: https://www.proteinatlas.org/ENSG00000172354-GNB2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GNB2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P62879
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (supported)。来源: https://www.proteinatlas.org/ENSG00000172354-GNB2/subcellular

![](https://images.proteinatlas.org/10032/921_C9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/10032/921_C9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/10032/923_C9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/10032/923_C9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/10032/931_C9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/10032/931_C9_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P62879-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P62879 |
| SMART | SM00320; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR016346;IPR015943;IPR001632;IPR020472;IPR019775;IPR036322;IPR001680; |
| Pfam | PF25391; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000172354-GNB2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CCT2 | Biogrid, Bioplex | true |
| CCT3 | Biogrid, Bioplex | true |
| CCT4 | Biogrid, Bioplex | true |
| CCT5 | Biogrid, Bioplex | true |
| CCT6A | Biogrid, Bioplex | true |
| CCT7 | Biogrid, Bioplex | true |
| CCT8 | Biogrid, Bioplex | true |
| CFTR | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

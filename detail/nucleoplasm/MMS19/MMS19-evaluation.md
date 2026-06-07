---
type: protein-evaluation
gene: "MMS19"
date: 2026-06-03
tags: [protein-scout, nucleoplasm, re-evaluation, recovery]
status: scored
category: nucleoplasm
normalized_score: 63.7
raw_score: 116.5
nuclear_score: 7
---

## MMS19 核蛋白评估报告 (Full Re-evaluation)


### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MMS19 / MMS19L |
| 蛋白名称 | MMS19 nucleotide excision repair protein homolog |
| 蛋白大小 | 1030 aa / 113.3 kDa |
| UniProt ID | Q96T76 |
| PubMed (strict) | 51 |
| PubMed (broad) | 73 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm, cytoskeleton, spindle; Cytoplasm, cytosk |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 1030 aa / 113.3 kDa |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=51 篇 (41-60→6) |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=90.8，PDB: 无 |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011989, IPR016024, IPR039920, IPR024687, IPR029 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners, IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.5/183** | |
| **归一化总分** | | | **63.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus; Cytoplasm, cytoskeleton, spindle; Cytoplasm, cytoskeleton, microtubule ... | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- centrosome (GO:0005813)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- cytosolic [4Fe-4S] assembly targeting complex (GO:0097361)
- membrane (GO:0016020)
- MMXD complex (GO:0071817)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持，部分数据源提示非核定位但核信号主导。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 51 |
| PubMed broad count | 73 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MMS19L |

**关键文献**:
1. CIAO1 and MMS19 deficiency: A lethal neurodegenerative phenotype caused by cytosolic Fe-S cluster protein assembly disorders.. *Genetics in medicine : official journal of the American College of Medical Genetics*. PMID: 38411040
2. The Cytosolic Iron-Sulfur Cluster Assembly Protein MMS19 Regulates Transcriptional Gene Silencing, DNA Repair, and Flowering Time in Arabidopsis.. *PloS one*. PMID: 26053632
3. CIAO1 loss of function causes a neuromuscular disorder with compromise of nucleocytoplasmic Fe-S enzymes.. *The Journal of clinical investigation*. PMID: 38950322
4. Dual requirement for the yeast MMS19 gene in DNA repair and RNA polymerase II transcription.. *Molecular and cellular biology*. PMID: 8943333
5. The mammalian proteins MMS19, MIP18, and ANT2 are involved in cytoplasmic iron-sulfur cluster protein assembly.. *The Journal of biological chemistry*. PMID: 23150669

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.8 |
| 高置信度残基 (pLDDT>90) 占比 | 74.2% |
| 置信残基 (pLDDT 70-90) 占比 | 20.4% |
| 中等置信 (pLDDT 50-70) 占比 | 4.1% |
| 低置信 (pLDDT<50) 占比 | 1.4% |
| 有序区域 (pLDDT>70) 占比 | 94.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=90.8，有序区 94.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR039920, IPR024687, IPR029240; Pfam: PF12460, PF14500 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ERCC2 | 0.999 | 0.946 | — |
| CIAO1 | 0.999 | 0.958 | — |
| CIAO2B | 0.999 | 0.984 | — |
| CIAO3 | 0.998 | 0.625 | — |
| CIAO2A | 0.996 | 0.696 | — |
| SLC25A5 | 0.994 | 0.000 | — |
| ERCC3 | 0.993 | 0.292 | — |
| RTEL1 | 0.979 | 0.836 | — |
| BRIP1 | 0.961 | 0.768 | — |
| GTF2H1 | 0.952 | 0.292 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ATP2 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| CIA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| MET18 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| RAD3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| MPA43 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| PTP4A3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| CDK4 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MYC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PHLDA3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| GIPC1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**已知复合体成员** (GO Cellular Component):
- centrosome (GO:0005813)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- cytosolic [4Fe-4S] assembly targeting complex (GO:0097361)
- membrane (GO:0016020)
- MMXD complex (GO:0071817)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.8 + PDB: 无 | pLDDT=90.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, cytoskeleton, spindle; Cytopla / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. MMS19 — MMS19 nucleotide excision repair protein homolog，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小1030 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 51 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96T76
- Protein Atlas: https://www.proteinatlas.org/ENSG00000155229-MMS19
- Protein Atlas Subcellular: https://www.proteinatlas.org/ENSG00000155229-MMS19/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MMS19
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96T76
- STRING: https://string-db.org/network
- IntAct: https://www.ebi.ac.uk/intact/search?query=MMS19
- Packet data timestamp: 2026-06-03 21:46:30

---

*本报告基于最新的 harvest packet 数据（2026-06-03 21:46:30），各数据库实时抓取。评分严格遵循 /180 加权评分体系：核定位×4 + 大小×1 + 新颖性×5 + 结构×3 + 结构域×2 + PPI×3 + 互证加分（max+3）。PubMed>100 或 核定位≤3 为 REJECTED。*

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000155229-MMS19/subcellular

![](https://images.proteinatlas.org/51936/1028_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/51936/1028_E5_2_red_green.jpg)
![](https://images.proteinatlas.org/51936/802_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/51936/802_E5_2_red_green.jpg)
![](https://images.proteinatlas.org/51936/840_C8_1_red_green.jpg)
![](https://images.proteinatlas.org/51936/840_C8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96T76-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96T76 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR011989;IPR016024;IPR039920;IPR024687;IPR029240; |
| Pfam | PF12460;PF14500; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000155229-MMS19/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BRIP1 | Intact, Biogrid | true |
| CIAO1 | Intact, Biogrid, Bioplex | true |
| CIAO2B | Intact, Biogrid, Bioplex | true |
| CIAO3 | Intact, Biogrid | true |
| DNA2 | Biogrid, Bioplex | true |
| ERCC2 | Intact, Biogrid | true |
| MYC | Intact, Biogrid | true |
| POLD1 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

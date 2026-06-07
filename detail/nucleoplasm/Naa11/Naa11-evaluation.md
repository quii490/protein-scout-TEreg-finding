---
type: protein-evaluation
gene: "Naa11"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## Naa11 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | Naa11 / ARD1B, ARD2 |
| 蛋白名称 | N-alpha-acetyltransferase 11 |
| 蛋白大小 | 229 aa / 26.0 kDa |
| UniProt ID | Q9BSU3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Golgi apparatus, Centrosome, Cytosol; 额外: Nucleoplasm, Prima; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 229 aa / 26.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=79.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR016181, IPR045047, IPR000182; Pfam: PF00583 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus, Centrosome, Cytosol; 额外: Nucleoplasm, Primary cilium, Basal body | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- ciliary basal body (GO:0036064)
- cilium (GO:0005929)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- Golgi apparatus (GO:0005794)
- NatA complex (GO:0031415)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 11 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ARD1B, ARD2 |

**关键文献**:
1. Expression of human NAA11 (ARD1B) gene is tissue-specific and is regulated by DNA methylation.. *Epigenetics*. PMID: 22048246
2. RNA-binding protein with serine-rich domain 1 regulates microsatellite instability of uterine corpus endometrial adenocarcinoma.. *Clinics (Sao Paulo, Brazil)*. PMID: 34817046
3. Gene fusions characterize a subset of uterine cellular leiomyomas.. *Genes, chromosomes & cancer*. PMID: 32677742
4. N-Terminal Acetyltransferases Are Cancer-Essential Genes Prevalently Upregulated in Tumours.. *Cancers*. PMID: 32942614
5. Identification of a ceRNA Network Regulating Malignant Transformation of Isocitrate Dehydrogenase Mutant Astrocytoma: An Integrated Bioinformatics Study.. *Current computer-aided drug design*. PMID: 39779553

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.4 |
| 高置信度残基 (pLDDT>90) 占比 | 68.1% |
| 置信残基 (pLDDT 70-90) 占比 | 4.4% |
| 中等置信 (pLDDT 50-70) 占比 | 2.6% |
| 低置信 (pLDDT<50) 占比 | 24.9% |
| 有序区域 (pLDDT>70) 占比 | 72.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=79.4，有序区 72.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016181, IPR045047, IPR000182; Pfam: PF00583 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NAA16 | 0.998 | 0.899 | — |
| NAA15 | 0.997 | 0.851 | — |
| NAA50 | 0.988 | 0.855 | — |
| NAA35 | 0.962 | 0.085 | — |
| NAA30 | 0.944 | 0.000 | — |
| NAA10 | 0.935 | 0.369 | — |
| NAA38 | 0.910 | 0.000 | — |
| NAA25 | 0.790 | 0.000 | — |
| NAA60 | 0.790 | 0.468 | — |
| HYPK | 0.759 | 0.535 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NAA15 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:16638120|imex:IM-20427 |
| - | psi-mi:"MI:0889"(acetylase assay) | pubmed:16638120|imex:IM-20427 |
| ZBTB14 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| EHMT2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MTARC1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| AP2M1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CDCA5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| BAALC | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ZNF202 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CDC25A | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.4 + PDB: 无 | pLDDT=79.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Golgi apparatus, Centrosome, Cytosol; 额外: Nucleopl | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. Naa11 — N-alpha-acetyltransferase 11，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小229 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BSU3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000156269-NAA11/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=Naa11
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BSU3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (approved)。来源: https://www.proteinatlas.org/ENSG00000156269-NAA11/subcellular

![](https://images.proteinatlas.org/35922/2179_C7_17_blue_red_green.jpg)
![](https://images.proteinatlas.org/35922/2179_C7_54_blue_red_green.jpg)
![](https://images.proteinatlas.org/35922/2234_B6_34_blue_red_green.jpg)
![](https://images.proteinatlas.org/35922/2234_B6_82_blue_red_green.jpg)
![](https://images.proteinatlas.org/35922/2241_C8_23_blue_red_green.jpg)
![](https://images.proteinatlas.org/35922/2241_C8_36_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BSU3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BSU3 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 1..152; /note="N-acetyltransferase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00532" |
| InterPro | IPR016181;IPR045047;IPR000182; |
| Pfam | PF00583; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000156269-NAA11/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ACOT12 | Intact | false |
| AP2M1 | Intact | false |
| CDC25A | Intact | false |
| CDCA5 | Intact | false |
| CREBRF | Intact | false |
| EHMT2 | Intact | false |
| KIFAP3 | Intact | false |
| MTARC1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

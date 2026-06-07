---
type: protein-evaluation
gene: "PER1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PER1 — REJECTED (研究热度过高 (PubMed strict=1678，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PER1 / KIAA0482, PER, RIGUI |
| 蛋白名称 | Period circadian protein homolog 1 |
| 蛋白大小 | 1290 aa / 136.2 kDa |
| UniProt ID | O15534 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nucleoplasm; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 5/10 | ×1 | 5 | 1290 aa / 136.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1678 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=52.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000014, IPR035965, IPR013655, IPR057310, IPR048 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **75.0/180** | |
| **归一化总分** | | | **41.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1678 |
| PubMed broad count | 2599 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0482, PER, RIGUI |

**关键文献**:
1. Disrupting Circadian Rhythm via the PER1-HK2 Axis Reverses Trastuzumab Resistance in Gastric Cancer.. *Cancer research*. PMID: 35255118
2. Circadian Rhythm Disruption Exacerbates Autoimmune Uveitis: The Essential Role of PER1 in Treg Cell Metabolic Support for Stability and Function.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 39823532
3. A Period1 inducer specifically advances circadian clock in mice.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 41576083
4. Circadian rhythm disruption upregulating Per1 in mandibular condylar chondrocytes mediating temporomandibular joint osteoarthritis via GSK3β/β-CATENIN pathway.. *Journal of translational medicine*. PMID: 39010104
5. Age and sex influence diurnal memory oscillations, circadian rhythmicity, and Per1 expression.. *Biology of sex differences*. PMID: 41088450

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 52.1 |
| 高置信度残基 (pLDDT>90) 占比 | 15.5% |
| 置信残基 (pLDDT 70-90) 占比 | 12.5% |
| 中等置信 (pLDDT 50-70) 占比 | 9.1% |
| 低置信 (pLDDT<50) 占比 | 62.9% |
| 有序区域 (pLDDT>70) 占比 | 28.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=52.1），有序残基占 28.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000014, IPR035965, IPR013655, IPR057310, IPR048814; Pfam: PF23170, PF08447, PF21353 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CRY1 | 0.998 | 0.989 | — |
| CRY2 | 0.998 | 0.978 | — |
| PER2 | 0.997 | 0.968 | — |
| PER3 | 0.997 | 0.968 | — |
| CSNK1E | 0.996 | 0.897 | — |
| ARNTL | 0.985 | 0.954 | — |
| CSNK1D | 0.984 | 0.758 | — |
| BTRC | 0.962 | 0.560 | — |
| FBXW11 | 0.938 | 0.397 | — |
| CLOCK | 0.913 | 0.746 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSMUSP00000132635.2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| RIPOR2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| Btrc | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-11930|pubmed:17462724 |
| Timeless | psi-mi:"MI:0096"(pull down) | pubmed:10231394|imex:IM-19198 |
| SSB1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| Cry1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Csnk1e | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Cry2 | psi-mi:"MI:0018"(two hybrid) | pubmed:23555304|imex:IM-20564 |
| CSNK2B | psi-mi:"MI:0018"(two hybrid) | pubmed:23555304|imex:IM-20564 |
| BHLHE40 | psi-mi:"MI:0018"(two hybrid) | pubmed:23555304|imex:IM-20564 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=52.1 + PDB: 无 | pLDDT=52.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Cytosol; 额外: Nucleoplasm | 一致 |
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
1. PER1 — Period circadian protein homolog 1，研究基础较多，新颖性有限。
2. 蛋白大小1290 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 1678 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=52.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1678 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O15534
- Protein Atlas: https://www.proteinatlas.org/ENSG00000179094-PER1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PER1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O15534
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000179094-PER1/subcellular

![](https://images.proteinatlas.org/47947/1468_B5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/47947/1468_B5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/47947/1470_B5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/47947/1470_B5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/47947/1553_E5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/47947/1553_E5_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O15534-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O15534 |
| SMART | SM00091; |
| UniProt Domain [FT] | DOMAIN 208..275; /note="PAS 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00140"; DOMAIN 348..414; /note="PAS 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00140"; DOMAIN 422..465; /note="PAC" |
| InterPro | IPR000014;IPR035965;IPR013655;IPR057310;IPR048814;IPR022728;IPR050760; |
| Pfam | PF23170;PF08447;PF21353;PF12114; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000179094-PER1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CRY1 | Intact, Biogrid, Bioplex | true |
| CSNK1E | Biogrid, Bioplex | true |
| PER2 | Biogrid, Bioplex | true |
| PER3 | Intact, Biogrid | true |
| BRK1 | Intact | false |
| BTRC | Biogrid | false |
| CASP6 | Intact | false |
| CCT7 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

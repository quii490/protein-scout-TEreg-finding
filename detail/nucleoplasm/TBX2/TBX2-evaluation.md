---
type: protein-evaluation
gene: "TBX2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TBX2 — REJECTED (研究热度过高 (PubMed strict=333，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TBX2 |
| 蛋白名称 | T-box transcription factor TBX2 |
| 蛋白大小 | 712 aa / 75.1 kDa |
| UniProt ID | Q13207 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 712 aa / 75.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=333 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR008967, IPR046360, IPR036960, IPR022582, IPR048 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 333 |
| PubMed broad count | 497 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Integrated Single-Cell Atlas of Endothelial Cells of the Human Lung.. *Circulation*. PMID: 34030460
2. NF-Y in invertebrates.. *Biochimica et biophysica acta. Gene regulatory mechanisms*. PMID: 27793714
3. omb and circumstance.. *Journal of neurogenetics*. PMID: 19052953
4. Cardiac Transcription Factors and Regulatory Networks.. *Advances in experimental medicine and biology*. PMID: 38884718
5. Identification of transcription factors that regulate placental sFLT1 expression.. *Molecular human reproduction*. PMID: 40632597

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.4 |
| 高置信度残基 (pLDDT>90) 占比 | 24.4% |
| 置信残基 (pLDDT 70-90) 占比 | 2.8% |
| 中等置信 (pLDDT 50-70) 占比 | 7.3% |
| 低置信 (pLDDT<50) 占比 | 65.4% |
| 有序区域 (pLDDT>70) 占比 | 27.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=56.4），有序残基占 27.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008967, IPR046360, IPR036960, IPR022582, IPR048387; Pfam: PF00907, PF20627, PF12598 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NKX2-5 | 0.842 | 0.075 | — |
| HAND2 | 0.758 | 0.066 | — |
| ISL1 | 0.721 | 0.071 | — |
| GJA5 | 0.721 | 0.000 | — |
| NPPA | 0.713 | 0.000 | — |
| H3-3B | 0.665 | 0.000 | — |
| H3-5 | 0.664 | 0.000 | — |
| H3-2 | 0.661 | 0.000 | — |
| H3C13 | 0.661 | 0.000 | — |
| H3-4 | 0.656 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Q0WG89 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| truA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ENSP00000240328.3 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| CYSRT1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CIDEB | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CNOT2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ATXN1L | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TTC19 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| LMO2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.4 + PDB: 无 | pLDDT=56.4, v6 | 仅预测 |
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
1. TBX2 — T-box transcription factor TBX2，研究基础较多，新颖性有限。
2. 蛋白大小712 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 333 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=56.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 333 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13207
- Protein Atlas: https://www.proteinatlas.org/ENSG00000121068-TBX2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TBX2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13207
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000121068-TBX2/subcellular

![](https://images.proteinatlas.org/8586/1081_A6_1_red_green.jpg)
![](https://images.proteinatlas.org/8586/1081_A6_2_red_green.jpg)
![](https://images.proteinatlas.org/8586/41_E9_1_red_green.jpg)
![](https://images.proteinatlas.org/8586/41_E9_2_red_green.jpg)
![](https://images.proteinatlas.org/8586/43_E9_1_red_green.jpg)
![](https://images.proteinatlas.org/8586/43_E9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q13207-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q13207 |
| SMART | SM00425; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR008967;IPR046360;IPR036960;IPR022582;IPR048387;IPR002070;IPR001699;IPR018186; |
| Pfam | PF00907;PF20627;PF12598; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000121068-TBX2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ATXN1L | Intact | false |
| CIDEB | Intact | false |
| CNOT2 | Intact | false |
| CYSRT1 | Intact | false |
| DDB2 | Biogrid | false |
| EGR1 | Biogrid | false |
| KRTAP6-3 | Intact | false |
| SOX2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

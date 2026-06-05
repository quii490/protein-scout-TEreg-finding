---
type: protein-evaluation
gene: "NCOA2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NCOA2 — REJECTED (研究热度过高 (PubMed strict=250，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NCOA2 / BHLHE75, SRC2, TIF2 |
| 蛋白名称 | Nuclear receptor coactivator 2 |
| 蛋白大小 | 1464 aa / 159.2 kDa |
| UniProt ID | Q15596 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear bodies; UniProt: Nucleus |
| 蛋白大小 | 5/10 | ×1 | 5 | 1464 aa / 159.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=250 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=47.6; PDB: 1GWQ, 1GWR, 1M2Z, 1MV9, 1MVC, 1MZN, 1P93 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011598, IPR056193, IPR036638, IPR010011, IPR032 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **76.5/180** | |
| **归一化总分** | | | **42.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear bodies | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- protein-containing complex (GO:0032991)
- RNA polymerase II transcription regulator complex (GO:0090575)
- transcription regulator complex (GO:0005667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 250 |
| PubMed broad count | 678 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BHLHE75, SRC2, TIF2 |

**关键文献**:
1. HEY1-NCOA2 expression modulates chondrogenic differentiation and induces mesenchymal chondrosarcoma in mice.. *JCI insight*. PMID: 37212282
2. VGLL2-NCOA2 leverages developmental programs for pediatric sarcomagenesis.. *Cell reports*. PMID: 36656711
3. Tai/NCOA2 suppresses the Hedgehog pathway by directly targeting the transcription factor Ci/GLI.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 39531503
4. HNF4A mitigates sepsis-associated lung injury by upregulating NCOR2/GR/STAB1 axis and promoting macrophage polarization towards M2 phenotype.. *Cell death & disease*. PMID: 39979267
5. Molecular diagnostics in the management of rhabdomyosarcoma.. *Expert review of molecular diagnostics*. PMID: 28058850

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 47.6 |
| 高置信度残基 (pLDDT>90) 占比 | 10.0% |
| 置信残基 (pLDDT 70-90) 占比 | 9.8% |
| 中等置信 (pLDDT 50-70) 占比 | 8.6% |
| 低置信 (pLDDT<50) 占比 | 71.5% |
| 有序区域 (pLDDT>70) 占比 | 19.8% |
| 可用 PDB 条目 | 1GWQ, 1GWR, 1M2Z, 1MV9, 1MVC, 1MZN, 1P93, 1T63, 1T65, 1UHL |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=47.6），有序残基占 19.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR056193, IPR036638, IPR010011, IPR032565; Pfam: PF23172, PF07469, PF16279 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ESR1 | 0.999 | 0.992 | — |
| AR | 0.999 | 0.989 | — |
| RXRA | 0.999 | 0.991 | — |
| PPARG | 0.998 | 0.965 | — |
| EP300 | 0.998 | 0.641 | — |
| NR3C1 | 0.998 | 0.988 | — |
| NCOA3 | 0.997 | 0.510 | — |
| CREBBP | 0.997 | 0.796 | — |
| NCOA1 | 0.997 | 0.735 | — |
| CARM1 | 0.994 | 0.547 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| AR | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:15563469 |
| tkt2 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ENSP00000399968.2 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| spo0J | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| TAF9 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| TP53 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| flgH2 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| 35828 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| SLA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NR1I3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=47.6 + PDB: 1GWQ, 1GWR, 1M2Z, 1MV9, 1MVC,  | pLDDT=47.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. NCOA2 — Nuclear receptor coactivator 2，研究基础较多，新颖性有限。
2. 蛋白大小1464 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 250 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=47.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 250 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q15596
- Protein Atlas: https://www.proteinatlas.org/ENSG00000140396-NCOA2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NCOA2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15596
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000140396-NCOA2/subcellular

![](https://images.proteinatlas.org/60243/1468_H10_1_red_green.jpg)
![](https://images.proteinatlas.org/60243/1468_H10_3_red_green.jpg)
![](https://images.proteinatlas.org/60243/1470_H10_2_red_green.jpg)
![](https://images.proteinatlas.org/60243/1470_H10_5_red_green.jpg)
![](https://images.proteinatlas.org/60243/1482_D8_1_red_green.jpg)
![](https://images.proteinatlas.org/60243/1482_D8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q15596-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

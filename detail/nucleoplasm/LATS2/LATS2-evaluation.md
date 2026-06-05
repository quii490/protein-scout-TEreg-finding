---
type: protein-evaluation
gene: "LATS2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## LATS2 — REJECTED (研究热度过高 (PubMed strict=384，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LATS2 / KPM |
| 蛋白名称 | Serine/threonine-protein kinase LATS2 |
| 蛋白大小 | 1088 aa / 120.1 kDa |
| UniProt ID | Q9NRM7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Centriolar satellite, Cytosol; UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, cent |
| 蛋白大小 | 8/10 | ×1 | 8 | 1088 aa / 120.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=384 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.8; PDB: 4ZRI |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000961, IPR011009, IPR017892, IPR000719, IPR017 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **78.5/180** | |
| **归一化总分** | | | **43.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Centriolar satellite, Cytosol | Approved |
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Cytoplasm; Cytoplasm, cytoskelet... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centriolar satellite (GO:0034451)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleus (GO:0005634)
- spindle pole (GO:0000922)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 384 |
| PubMed broad count | 731 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KPM |

**关键文献**:
1. Extracellular vesicles in fatty liver promote a metastatic tumor microenvironment.. *Cell metabolism*. PMID: 37172577
2. The Hippo pathway kinases LATS1 and LATS2 attenuate cellular responses to heavy metals through phosphorylating MTF1.. *Nature cell biology*. PMID: 35027733
3. A LATS2 and ALKBH5 positive feedback loop supports their oncogenic roles.. *Cell reports*. PMID: 38568805
4. Extracellular vesicles miR-31-5p promotes pancreatic cancer chemoresistance via regulating LATS2-Hippo pathway and promoting SPARC secretion from pancreatic stellate cells.. *Journal of extracellular vesicles*. PMID: 39104296
5. JCAD promotes arterial thrombosis through PI3K/Akt modulation: a translational study.. *European heart journal*. PMID: 36469488

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.8 |
| 高置信度残基 (pLDDT>90) 占比 | 17.6% |
| 置信残基 (pLDDT 70-90) 占比 | 17.6% |
| 中等置信 (pLDDT 50-70) 占比 | 6.0% |
| 低置信 (pLDDT<50) 占比 | 58.7% |
| 有序区域 (pLDDT>70) 占比 | 35.2% |
| 可用 PDB 条目 | 4ZRI |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=55.8），有序残基占 35.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000961, IPR011009, IPR017892, IPR000719, IPR017441; Pfam: PF00069, PF00433 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| YAP1 | 0.999 | 0.962 | — |
| SAV1 | 0.998 | 0.827 | — |
| MOB1A | 0.997 | 0.898 | — |
| MOB1B | 0.996 | 0.840 | — |
| NF2 | 0.996 | 0.980 | — |
| LATS1 | 0.989 | 0.780 | — |
| WWTR1 | 0.989 | 0.653 | — |
| AJUBA | 0.983 | 0.745 | — |
| STK3 | 0.973 | 0.723 | — |
| WWC1 | 0.970 | 0.510 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSMUSP00000022531.8 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:24255178|imex:IM-21541 |
| MOB1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:19739119|imex:IM-16954 |
| MOB1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:19739119|imex:IM-16954 |
| YAP1 | psi-mi:"MI:0424"(protein kinase assay) | imex:IM-17872|pubmed:22863277 |
| YWHAH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DCAF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-22994|pubmed:25026211 |
| FHL3 | psi-mi:"MI:2215"(barcode fusion genetics two hybri | doi:10.15252/msb.20156660|pubm |
| GRAP2 | psi-mi:"MI:2215"(barcode fusion genetics two hybri | doi:10.15252/msb.20156660|pubm |
| LIMD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:24255178|imex:IM-21541 |
| CPVL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:24255178|imex:IM-21541 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.8 + PDB: 4ZRI | pLDDT=55.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, microtubule organizing ce / Centriolar satellite, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. LATS2 — Serine/threonine-protein kinase LATS2，研究基础较多，新颖性有限。
2. 蛋白大小1088 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 384 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=55.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 384 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NRM7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000150457-LATS2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LATS2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NRM7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Centriolar satellite (approved)。来源: https://www.proteinatlas.org/ENSG00000150457-LATS2/subcellular

![](https://images.proteinatlas.org/49037/793_C2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/49037/793_C2_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/49037/800_C2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/49037/800_C2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/49037/845_C2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/49037/845_C2_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NRM7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

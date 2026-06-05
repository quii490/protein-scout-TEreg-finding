---
type: protein-evaluation
gene: "DUX4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DUX4 — REJECTED (研究热度过高 (PubMed strict=517，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DUX4 / DUX10 |
| 蛋白名称 | Double homeobox protein 4 |
| 蛋白大小 | 424 aa / 44.9 kDa |
| UniProt ID | Q9UBX2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli; 额外: Golgi apparatus, Cytosol; UniProt: Nucleus; Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 424 aa / 44.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=517 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.4; PDB: 5Z2S, 5Z2T, 5Z6Z, 5ZFW, 5ZFY, 5ZFZ, 6A8R |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001356, IPR051306, IPR009057, IPR000047; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli; 额外: Golgi apparatus, Cytosol | Approved |
| UniProt | Nucleus; Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- Golgi apparatus (GO:0005794)
- nuclear membrane (GO:0031965)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 517 |
| PubMed broad count | 777 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DUX10 |

**关键文献**:
1. The genomic landscape of pediatric acute lymphoblastic leukemia.. *Nature genetics*. PMID: 36050548
2. Facioscapulohumeral Muscular Dystrophy.. *Continuum (Minneapolis, Minn.)*. PMID: 36537978
3. Facioscapulohumeral muscular dystrophy: the road to targeted therapies.. *Nature reviews. Neurology*. PMID: 36627512
4. Genomic Profiling of Adult and Pediatric B-cell Acute Lymphoblastic Leukemia.. *EBioMedicine*. PMID: 27428428
5. Identification of ETV6-RUNX1-like and DUX4-rearranged subtypes in paediatric B-cell precursor acute lymphoblastic leukaemia.. *Nature communications*. PMID: 27265895

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.4 |
| 高置信度残基 (pLDDT>90) 占比 | 28.8% |
| 置信残基 (pLDDT 70-90) 占比 | 5.0% |
| 中等置信 (pLDDT 50-70) 占比 | 12.7% |
| 低置信 (pLDDT<50) 占比 | 53.5% |
| 有序区域 (pLDDT>70) 占比 | 33.8% |
| 可用 PDB 条目 | 5Z2S, 5Z2T, 5Z6Z, 5ZFW, 5ZFY, 5ZFZ, 6A8R, 6DFY, 6E8C, 6U81 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=61.4），有序残基占 33.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR051306, IPR009057, IPR000047; Pfam: PF00046 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FRG2 | 0.940 | 0.000 | — |
| FRG1 | 0.927 | 0.000 | — |
| SMCHD1 | 0.872 | 0.000 | — |
| ETV5 | 0.861 | 0.000 | — |
| ZNF384 | 0.796 | 0.069 | — |
| ETV1 | 0.789 | 0.000 | — |
| TRIM43 | 0.776 | 0.051 | — |
| ZSCAN4 | 0.774 | 0.069 | — |
| LEUTX | 0.749 | 0.071 | — |
| MYOD1 | 0.729 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Des | psi-mi:"MI:0018"(two hybrid) | imex:IM-25050|pubmed:26816005 |
| Trip6 | psi-mi:"MI:0018"(two hybrid) | imex:IM-25050|pubmed:26816005 |
| Cap1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-25050|pubmed:26816005 |
| Pi4k2a | psi-mi:"MI:0018"(two hybrid) | imex:IM-25050|pubmed:26816005 |
| Lmcd1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-25050|pubmed:26816005 |
| Tpt1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-25050|pubmed:26816005 |
| Cenpa | psi-mi:"MI:0018"(two hybrid) | imex:IM-25050|pubmed:26816005 |
| Tubgcp6 | psi-mi:"MI:0018"(two hybrid) | imex:IM-25050|pubmed:26816005 |
| Rbm3 | psi-mi:"MI:0018"(two hybrid) | imex:IM-25050|pubmed:26816005 |
| C1qbp | psi-mi:"MI:0018"(two hybrid) | imex:IM-25050|pubmed:26816005 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.4 + PDB: 5Z2S, 5Z2T, 5Z6Z, 5ZFW, 5ZFY,  | pLDDT=61.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Nucleus / Nucleoplasm, Nucleoli; 额外: Golgi apparatus, Cytoso | 一致 |
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
1. DUX4 — Double homeobox protein 4，研究基础较多，新颖性有限。
2. 蛋白大小424 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 517 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=61.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 517 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UBX2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000260596-DUX4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DUX4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UBX2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000260596-DUX4/subcellular

![](https://images.proteinatlas.org/58451/1702_A2_4_cr57ea949c20b81_red_green.jpg)
![](https://images.proteinatlas.org/58451/1702_A2_9_cr57ea94a378635_red_green.jpg)
![](https://images.proteinatlas.org/58451/1709_F7_13_cr58048bf818621_red_green.jpg)
![](https://images.proteinatlas.org/58451/1709_F7_7_cr58048bef2f5c2_red_green.jpg)
![](https://images.proteinatlas.org/58451/1762_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/58451/1762_H6_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UBX2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

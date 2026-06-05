---
type: protein-evaluation
gene: "TRIM24"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TRIM24 — REJECTED (研究热度过高 (PubMed strict=176，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TRIM24 / RNF82, TIF1, TIF1A |
| 蛋白名称 | Transcription intermediary factor 1-alpha |
| 蛋白大小 | 1050 aa / 116.8 kDa |
| UniProt ID | O15164 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm; Mitochondrion |
| 蛋白大小 | 8/10 | ×1 | 8 | 1050 aa / 116.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=176 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.6; PDB: 2YYN, 3O33, 3O34, 3O35, 3O36, 3O37, 4YAB |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003649, IPR001487, IPR036427, IPR018359, IPR019 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.5/180** | |
| **归一化总分** | | | **44.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus; Cytoplasm; Mitochondrion | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- euchromatin (GO:0000791)
- male germ cell nucleus (GO:0001673)
- mitochondrion (GO:0005739)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- perichromatin fibrils (GO:0005726)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 176 |
| PubMed broad count | 262 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RNF82, TIF1, TIF1A |

**关键文献**:
1. Deregulation of SPOP in Cancer.. *Cancer research*. PMID: 36512624
2. Development of small-molecule tropomyosin receptor kinase (TRK) inhibitors for NTRK fusion cancers.. *Acta pharmaceutica Sinica. B*. PMID: 33643817
3. TRIM24 directs replicative stress responses to maintain ALT telomeres via chromatin signaling.. *Molecular cell*. PMID: 40614724
4. Cytoplasmic TRIM24 promotes colorectal cancer cell proliferation by activating Wnt/β-catenin signaling.. *Nature communications*. PMID: 41022821
5. Readout of histone methylation by Trim24 locally restricts chromatin opening by p53.. *Nature structural & molecular biology*. PMID: 37386214

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.6 |
| 高置信度残基 (pLDDT>90) 占比 | 24.5% |
| 置信残基 (pLDDT 70-90) 占比 | 22.0% |
| 中等置信 (pLDDT 50-70) 占比 | 7.7% |
| 低置信 (pLDDT<50) 占比 | 45.8% |
| 有序区域 (pLDDT>70) 占比 | 46.5% |
| 可用 PDB 条目 | 2YYN, 3O33, 3O34, 3O35, 3O36, 3O37, 4YAB, 4YAD, 4YAT, 4YAX |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=62.6），有序残基占 46.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003649, IPR001487, IPR036427, IPR018359, IPR019786; Pfam: PF00439, PF00628, PF00643 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| H3C12 | 0.989 | 0.950 | — |
| H3C13 | 0.980 | 0.907 | — |
| H3-2 | 0.980 | 0.907 | — |
| H3C1 | 0.979 | 0.978 | — |
| TRIM28 | 0.962 | 0.812 | — |
| ESR1 | 0.960 | 0.836 | — |
| H3C3 | 0.952 | 0.950 | — |
| TRIM33 | 0.951 | 0.863 | — |
| H3C8 | 0.951 | 0.950 | — |
| H3C11 | 0.951 | 0.950 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Cbx1 | psi-mi:"MI:0018"(two hybrid) | pubmed:8978696 |
| Cbx5 | psi-mi:"MI:0018"(two hybrid) | pubmed:8978696 |
| Rxra | psi-mi:"MI:0018"(two hybrid) | pubmed:8978696 |
| Rara | psi-mi:"MI:0018"(two hybrid) | pubmed:8978696 |
| Esr1 | psi-mi:"MI:0018"(two hybrid) | pubmed:8978696 |
| Vdr | psi-mi:"MI:0018"(two hybrid) | pubmed:8978696 |
| Pgr | psi-mi:"MI:0018"(two hybrid) | pubmed:8978696 |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| BRCA1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| UBE2U | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9597|pubmed:19690564 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.6 + PDB: 2YYN, 3O33, 3O34, 3O35, 3O36,  | pLDDT=62.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Mitochondrion / Nucleoplasm | 一致 |
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
1. TRIM24 — Transcription intermediary factor 1-alpha，研究基础较多，新颖性有限。
2. 蛋白大小1050 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 176 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=62.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 176 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O15164
- Protein Atlas: https://www.proteinatlas.org/ENSG00000122779-TRIM24/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TRIM24
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O15164
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000122779-TRIM24/subcellular

![](https://images.proteinatlas.org/43495/504_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/43495/504_C10_2_red_green.jpg)
![](https://images.proteinatlas.org/43495/506_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/43495/506_C10_2_red_green.jpg)
![](https://images.proteinatlas.org/43495/555_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/43495/555_C10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O15164-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

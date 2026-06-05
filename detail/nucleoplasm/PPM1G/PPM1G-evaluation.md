---
type: protein-evaluation
gene: "PPM1G"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PPM1G 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PPM1G / PPM1C |
| 蛋白名称 | Protein phosphatase 1G |
| 蛋白大小 | 546 aa / 59.3 kDa |
| UniProt ID | O15355 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasm; Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 546 aa / 59.3 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=53 篇 (≤60→6) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=73.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR015655, IPR000222, IPR036457, IPR001932; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.5/180** | |
| **归一化总分** | | | **63.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Cytoplasm; Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 53 |
| PubMed broad count | 113 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PPM1C |

**关键文献**:
1. Metal-dependent Ser/Thr protein phosphatase PPM family: Evolution, structures, diseases and inhibitors.. *Pharmacology & therapeutics*. PMID: 32650009
2. PPM1G and its diagnostic, prognostic and therapeutic potential in HCC (Review).. *International journal of oncology*. PMID: 39329206
3. PPM1G Inhibits Epithelial-Mesenchymal Transition in Cholangiocarcinoma by Catalyzing TET1 Dephosphorylation for Destabilization to Impair Its Targeted Demethylation of the CLDN3 Promoter.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 39477806
4. Clinical Value of PPM1G Gene in Survival Prognosis and Immune Infiltration of Hepatocellular Carcinoma.. *Applied bionics and biomechanics*. PMID: 35126665
5. A Macrophage-Derived 7-Gene Signature Predicts Prognosis and Therapeutic Response in Hepatocellular Carcinoma.. *IUBMB life*. PMID: 41355397

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.1 |
| 高置信度残基 (pLDDT>90) 占比 | 51.8% |
| 置信残基 (pLDDT 70-90) 占比 | 7.3% |
| 中等置信 (pLDDT 50-70) 占比 | 6.0% |
| 低置信 (pLDDT<50) 占比 | 34.8% |
| 有序区域 (pLDDT>70) 占比 | 59.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=73.1，有序区 59.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR015655, IPR000222, IPR036457, IPR001932; Pfam: PF00481 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HEXIM1 | 0.918 | 0.292 | — |
| LARP7 | 0.875 | 0.603 | — |
| USP7 | 0.874 | 0.776 | — |
| MEPCE | 0.787 | 0.292 | — |
| PPP1CC | 0.727 | 0.107 | — |
| STMN2 | 0.692 | 0.492 | — |
| PPP1CB | 0.689 | 0.107 | — |
| H2AX | 0.682 | 0.624 | — |
| PPP1R12A | 0.681 | 0.091 | — |
| SNRPA | 0.667 | 0.239 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Btk | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| LRPAP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| TRAF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| FBXO38 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| acpA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| tat | psi-mi:"MI:0096"(pull down) | imex:IM-17346|pubmed:22190034| |
| SLX4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12200|pubmed:19596235 |
| BAP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| USP36 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| USP49 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.1 + PDB: 无 | pLDDT=73.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Membrane / Nucleoplasm | 一致 |
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
1. PPM1G — Protein phosphatase 1G，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小546 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 53 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O15355
- Protein Atlas: https://www.proteinatlas.org/ENSG00000115241-PPM1G/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PPM1G
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O15355
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000115241-PPM1G/subcellular

![](https://images.proteinatlas.org/35530/563_F12_1_red_green.jpg)
![](https://images.proteinatlas.org/35530/563_F12_2_red_green.jpg)
![](https://images.proteinatlas.org/35530/566_F12_1_red_green.jpg)
![](https://images.proteinatlas.org/35530/566_F12_2_red_green.jpg)
![](https://images.proteinatlas.org/35530/569_F12_1_red_green.jpg)
![](https://images.proteinatlas.org/35530/569_F12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O15355-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

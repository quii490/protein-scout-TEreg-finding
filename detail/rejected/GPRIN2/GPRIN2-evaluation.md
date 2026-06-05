---
type: protein-evaluation
gene: "GPRIN2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GPRIN2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPRIN2 / KIAA0514 |
| 蛋白名称 | G protein-regulated inducer of neurite outgrowth 2 |
| 蛋白大小 | 458 aa / 47.5 kDa |
| UniProt ID | O60269 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Plasma membrane, Microtubules; 额外: Cytokinetic bridge, Mitot; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 458 aa / 47.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=50.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026646, IPR032745; Pfam: PF15235 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **110.0/180** | |
| **归一化总分** | | | **61.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Microtubules; 额外: Cytokinetic bridge, Mitotic spindle | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 28 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0514 |

**关键文献**:
1. Identification of molecular biomarkers associated with non-small-cell lung carcinoma (NSCLC) using whole-exome sequencing.. *Cancer biomarkers : section A of Disease markers*. PMID: 37694353
2. Identification of mitophagy-related biomarkers with immune cell infiltration in psoriasis.. *BMC medical genomics*. PMID: 40598168
3. The T2T-CHM13 reference assembly uncovers essential WASH1 and GPRIN2 paralogues.. *Bioinformatics advances*. PMID: 38464973
4. Tumor Suppressive Role of MUC6 in Wilms Tumor via Autophagy-Dependent β-Catenin Degradation.. *Frontiers in oncology*. PMID: 35574418
5. Ferredoxin 1: a gatekeeper in halting lung adenocarcinoma progression through activation of the GPRIN2 signaling pathway.. *Journal of translational medicine*. PMID: 38802900

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 50.5 |
| 高置信度残基 (pLDDT>90) 占比 | 3.5% |
| 置信残基 (pLDDT 70-90) 占比 | 4.6% |
| 中等置信 (pLDDT 50-70) 占比 | 28.6% |
| 低置信 (pLDDT<50) 占比 | 63.3% |
| 有序区域 (pLDDT>70) 占比 | 8.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=50.5），有序残基占 8.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026646, IPR032745; Pfam: PF15235 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HYDIN | 0.914 | 0.000 | — |
| SRGAP2 | 0.858 | 0.000 | — |
| SRGAP3 | 0.850 | 0.000 | — |
| NBPF1 | 0.841 | 0.000 | — |
| DRD5 | 0.836 | 0.000 | — |
| UGT2B17 | 0.832 | 0.000 | — |
| NPEPPS | 0.829 | 0.000 | — |
| GTF2I | 0.780 | 0.000 | — |
| GNAZ | 0.743 | 0.000 | — |
| NPY4R | 0.735 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DYNLL2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| SPRY2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MDFI | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| YWHAE | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| PLSCR1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| KRTAP4-12 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| SFN | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TRIP13 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| Hoxa1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15418|pubmed:23088713 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 9
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=50.5 + PDB: 无 | pLDDT=50.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Plasma membrane, Microtubules; 额外: Cytokinetic bri | 一致 |
| PPI | STRING + IntAct | 15 + 9 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GPRIN2 — G protein-regulated inducer of neurite outgrowth 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小458 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=50.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O60269
- Protein Atlas: https://www.proteinatlas.org/ENSG00000204175-GPRIN2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPRIN2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60269
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000204175-GPRIN2/subcellular

![](https://images.proteinatlas.org/70760/1873_B12_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/70760/1873_B12_9_blue_red_green.jpg)
![](https://images.proteinatlas.org/70760/1901_H11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/70760/1901_H11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/70760/1924_F8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/70760/1924_F8_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O60269-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

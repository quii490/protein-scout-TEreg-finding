---
type: protein-evaluation
gene: "DAP"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DAP — REJECTED (研究热度过高 (PubMed strict=1833，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DAP / DAP1 |
| 蛋白名称 | Death-associated protein 1 |
| 蛋白大小 | 102 aa / 11.2 kDa |
| UniProt ID | P51397 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Vesicles, Mitochondria; 额外: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 102 aa / 11.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1833 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR024130; Pfam: PF15228 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **65.5/180** | |
| **归一化总分** | | | **36.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles, Mitochondria; 额外: Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1833 |
| PubMed broad count | 8924 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DAP1 |

**关键文献**:
1. Dapagliflozin attenuates lipotoxic tenocyte injury via PPARα activation and irisin-driven antioxidant pathways.. *Connective tissue research*. PMID: 40959984
2. Emergence of transferable daptomycin resistance in Gram-positive bacteria.. *npj antimicrobials and resistance*. PMID: 40287593
3. Protective Effects of Deer Antler Peptides on D-Galactose-Induced Brain Injury.. *Nutrients*. PMID: 40732931
4. Detumescence Analgesic Plaster mitigates knee osteoarthritis via active ingredients targeting mitochondrial complex 1/AMPK/MYL3-regulated cartilage homeostasis.. *Chinese medicine*. PMID: 41111150
5. DAP-kinase: from functional gene cloning to establishment of its role in apoptosis and cancer.. *Cell death and differentiation*. PMID: 11313698

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.2 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 63.7% |
| 中等置信 (pLDDT 50-70) 占比 | 22.5% |
| 低置信 (pLDDT<50) 占比 | 13.7% |
| 有序区域 (pLDDT>70) 占比 | 63.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=69.2），有序残基占 63.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR024130; Pfam: PF15228 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DAPK1 | 0.870 | 0.000 | — |
| DAXX | 0.608 | 0.000 | — |
| ATRX | 0.588 | 0.000 | — |
| STK17B | 0.581 | 0.000 | — |
| DAPK3 | 0.580 | 0.000 | — |
| STK17A | 0.571 | 0.000 | — |
| CALM3 | 0.545 | 0.000 | — |
| CALML6 | 0.542 | 0.000 | — |
| CALML4 | 0.542 | 0.000 | — |
| CALML5 | 0.541 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Dmel\CG4194 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| PCNA | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| lysA | psi-mi:"MI:0397"(two hybrid array) | pubmed:17615063 |
| DNPEP | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| lysU | psi-mi:"MI:0096"(pull down) | pubmed:15690043|mint:MINT-5217 |
| tig | psi-mi:"MI:0096"(pull down) | pubmed:15690043|mint:MINT-5217 |
| MOAP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| CEP85 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| moeA2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:17615063 |
| rplF | psi-mi:"MI:0397"(two hybrid array) | pubmed:17615063 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.2 + PDB: 无 | pLDDT=69.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Vesicles, Mitochondria; 额外: Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DAP — Death-associated protein 1，研究基础较多，新颖性有限。
2. 蛋白大小102 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 1833 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=69.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1833 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P51397
- Protein Atlas: https://www.proteinatlas.org/ENSG00000112977-DAP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DAP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P51397
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (approved)。来源: https://www.proteinatlas.org/ENSG00000112977-DAP/subcellular

![](https://images.proteinatlas.org/29456/273_C6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/29456/273_C6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/29456/274_C6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/29456/274_C6_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P51397-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P51397 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR024130; |
| Pfam | PF15228; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000112977-DAP/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| RACK1 | Opencell | false |
| RBM8A | Opencell | false |
| SEC61B | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

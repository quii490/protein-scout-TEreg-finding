---
type: protein-evaluation
gene: "CADPS2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CADPS2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CADPS2 / CAPS2, KIAA1591 |
| 蛋白名称 | Calcium-dependent secretion activator 2 |
| 蛋白大小 | 1296 aa / 147.7 kDa |
| UniProt ID | Q86UW7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Vesicles; UniProt: Cytoplasmic vesicle membrane; Synapse; Cell projection, cili |
| 📏 蛋白大小 | 5/10 | ×1 | 5 | 1296 aa / 147.7 kDa |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=46 篇 (≤60→6) |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=79.0; PDB: 无 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000008, IPR035892, IPR033227, IPR057457, IPR010 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.5/180** | |
| **归一化总分** | | | **60.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles | Approved |
| UniProt | Cytoplasmic vesicle membrane; Synapse; Cell projection, cilium; Cytoplasm, cytos... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- ciliary basal body (GO:0036064)
- cilium (GO:0005929)
- cytoplasmic vesicle membrane (GO:0030659)
- glutamatergic synapse (GO:0098978)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 46 |
| PubMed broad count | 57 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CAPS2, KIAA1591 |

**关键文献**:
1. Single-cell sequencing of human midbrain reveals glial activation and a Parkinson-specific neuronal state.. *Brain : a journal of neurology*. PMID: 34919646
2. CADPS2 gene expression is oppositely regulated by LRRK2 and alpha-synuclein.. *Biochemical and biophysical research communications*. PMID: 28647363
3. Autistic-like phenotypes in Cadps2-knockout mice and aberrant CADPS2 splicing in autistic patients.. *The Journal of clinical investigation*. PMID: 17380209
4. Mouse models of mutations and variations in autism spectrum disorder-associated genes: mice expressing Caps2/Cadps2 copy number and alternative splicing variants.. *International journal of environmental research and public health*. PMID: 24287856
5. Genetic and neural mechanisms of sleep disorders in children with autism spectrum disorder: a review.. *Frontiers in psychiatry*. PMID: 37200906

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.0 |
| 高置信度残基 (pLDDT>90) 占比 | 41.4% |
| 置信残基 (pLDDT 70-90) 占比 | 37.9% |
| 中等置信 (pLDDT 50-70) 占比 | 5.5% |
| 低置信 (pLDDT<50) 占比 | 15.2% |
| 有序区域 (pLDDT>70) 占比 | 79.3% |
| 可用 PDB 条目 | 无 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=79.0，有序区 79.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000008, IPR035892, IPR033227, IPR057457, IPR010439; Pfam: PF25341, PF06292, PF00169 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AUTS2 | 0.871 | 0.000 | — |
| NRG3 | 0.866 | 0.000 | — |
| DYRK1A | 0.811 | 0.000 | — |
| BDNF | 0.644 | 0.000 | — |
| DCTN1 | 0.532 | 0.000 | — |
| TEX45 | 0.527 | 0.527 | — |
| ECPAS | 0.527 | 0.000 | — |
| PCLO | 0.526 | 0.000 | — |
| CNTNAP2 | 0.481 | 0.000 | — |
| RIMS2 | 0.465 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MEGF10 | psi-mi:"MI:0018"(two hybrid) | pubmed:unassigned5 |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| UBE2D1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9597|pubmed:19690564 |
| UBE2D2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9597|pubmed:19690564 |
| UBE2D3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9597|pubmed:19690564 |
| UBE2D4 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9597|pubmed:19690564 |
| UBE2E1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9597|pubmed:19690564 |
| UBE2E3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9597|pubmed:19690564 |
| UBE2N | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9597|pubmed:19690564 |
| UBE2U | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9597|pubmed:19690564 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.0 + PDB: 无 | pLDDT=79.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasmic vesicle membrane; Synapse; Cell projec / Nucleoplasm, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CADPS2 — Calcium-dependent secretion activator 2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小1296 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 46 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86UW7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000081803-CADPS2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CADPS2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86UW7
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 04:29:47

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000081803-CADPS2/subcellular

![](https://images.proteinatlas.org/56398/1334_G11_1_red_green.jpg)
![](https://images.proteinatlas.org/56398/1334_G11_3_red_green.jpg)
![](https://images.proteinatlas.org/56398/957_C12_1_red_green.jpg)
![](https://images.proteinatlas.org/56398/957_C12_2_red_green.jpg)
![](https://images.proteinatlas.org/56398/966_C12_1_red_green.jpg)
![](https://images.proteinatlas.org/56398/966_C12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86UW7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q86UW7 |
| SMART | SM01145;SM00233; |
| UniProt Domain [FT] | DOMAIN 293..400; /note="DM10"; /evidence="ECO:0000305\|PubMed:38538594"; DOMAIN 350..464; /note="C2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00041"; DOMAIN 487..590; /note="PH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00145"; DOMAIN 885..1056; /note="MHD1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00587" |
| InterPro | IPR000008;IPR035892;IPR033227;IPR057457;IPR010439;IPR014770;IPR011993;IPR001849; |
| Pfam | PF25341;PF06292;PF00169; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000081803-CADPS2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CTTN | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

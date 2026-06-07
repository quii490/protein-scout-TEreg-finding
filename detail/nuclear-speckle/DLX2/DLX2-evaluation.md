---
type: protein-evaluation
gene: "DLX2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DLX2 — REJECTED (研究热度过高 (PubMed strict=282，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DLX2 |
| 蛋白名称 | Homeobox protein DLX-2 |
| 蛋白大小 | 328 aa / 34.2 kDa |
| UniProt ID | Q07687 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nuclear speckles; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 328 aa / 34.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=282 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050460, IPR022135, IPR001356, IPR020479, IPR017 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 12 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **84.5/180** | |
| **归一化总分** | | | **46.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 282 |
| PubMed broad count | 452 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Generation of pure GABAergic neurons by transcription factor programming.. *Nature methods*. PMID: 28504679
2. Interneuron-specific dual-AAV SCN1A gene replacement corrects epileptic phenotypes in mouse models of Dravet syndrome.. *Science translational medicine*. PMID: 40106582
3. Decoding gene networks controlling hypothalamic and prethalamic neuron development.. *Cell reports*. PMID: 40512619
4. Expanding GABAergic Neuronal Diversity in iPSC-Derived Disease Models.. *bioRxiv : the preprint server for biology*. PMID: 39677822
5. Mechanisms regulating GABAergic neuron development.. *Cellular and molecular life sciences : CMLS*. PMID: 24196748

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.5 |
| 高置信度残基 (pLDDT>90) 占比 | 16.8% |
| 置信残基 (pLDDT 70-90) 占比 | 2.7% |
| 中等置信 (pLDDT 50-70) 占比 | 35.7% |
| 低置信 (pLDDT<50) 占比 | 44.8% |
| 有序区域 (pLDDT>70) 占比 | 19.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=58.5），有序残基占 19.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050460, IPR022135, IPR001356, IPR020479, IPR017970; Pfam: PF12413, PF00046 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PIK3R1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| BZRAP1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-24135|pubmed:24722188| |
| DGCR6 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-24135|pubmed:24722188| |
| MVP | psi-mi:"MI:0397"(two hybrid array) | imex:IM-24135|pubmed:24722188| |
| PRKN | psi-mi:"MI:0397"(two hybrid array) | imex:IM-24135|pubmed:24722188| |
| AVP | psi-mi:"MI:0397"(two hybrid array) | imex:IM-24135|pubmed:24722188| |
| GRN | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |
| Dlx1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| Alx4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| Sp7 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 12
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 12 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.5 + PDB: 无 | pLDDT=58.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 0 + 12 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DLX2 — Homeobox protein DLX-2，研究基础较多，新颖性有限。
2. 蛋白大小328 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 282 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=58.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 282 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q07687
- Protein Atlas: https://www.proteinatlas.org/ENSG00000115844-DLX2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DLX2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q07687
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000115844-DLX2/subcellular

![](https://images.proteinatlas.org/56965/1001_D5_1_red_green.jpg)
![](https://images.proteinatlas.org/56965/1001_D5_3_red_green.jpg)
![](https://images.proteinatlas.org/56965/1578_A2_1_red_green.jpg)
![](https://images.proteinatlas.org/56965/1578_A2_2_red_green.jpg)
![](https://images.proteinatlas.org/56965/973_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/56965/973_G5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q07687-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q07687 |
| SMART | SM00389; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR050460;IPR022135;IPR001356;IPR020479;IPR017970;IPR009057;IPR000047; |
| Pfam | PF12413;PF00046; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000115844-DLX2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| GRN | Intact | false |
| MSX1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

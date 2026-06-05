---
type: protein-evaluation
gene: "AAMP"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## AAMP — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AAMP |
| 蛋白名称 | Angio-associated migratory cell protein |
| 蛋白大小 | 434 aa / 46.8 kDa |
| UniProt ID | Q13685 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Microtubules; 额外: Plasma membrane, Cytokinetic bridge, Prima; UniProt: Cell membrane; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 434 aa / 46.8 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=36 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=84.6; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR015943, IPR019775, IPR036322, IPR001680, IPR051 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **105.5/180** | |
| **归一化总分** | | | **58.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Microtubules; 额外: Plasma membrane, Cytokinetic bridge, Primary cilium, Primary cilium tip, Cytosol | Approved |
| UniProt | Cell membrane; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell surface (GO:0009986)
- cytosol (GO:0005829)
- intercellular bridge (GO:0045171)
- microtubule cytoskeleton (GO:0015630)
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 36 |
| PubMed broad count | 148 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. A crucial exosome-related gene pair (AAMP and ABAT) is associated with inflammatory cells in intervertebral disc degeneration.. *Frontiers in immunology*. PMID: 37122729
2. AAMP Regulates Endothelial Cell Migration and Angiogenesis Through RhoA/Rho Kinase Signaling.. *Annals of biomedical engineering*. PMID: 26350504
3. AAMP, a conserved protein with immunoglobulin and WD40 domains, regulates endothelial tube formation in vitro.. *Laboratory investigation; a journal of technical methods and pathology*. PMID: 8683944
4. AAMP promotes colorectal cancermetastasis by suppressing SMURF2-mediatedubiquitination and degradation of RhoA.. *Molecular therapy oncolytics*. PMID: 34901393
5. AAMP and MTSS1 Are Novel Negative Regulators of Endothelial Barrier Function Identified in a Proteomics Screen.. *Cells*. PMID: 39404373

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.6 |
| 高置信度残基 (pLDDT>90) 占比 | 74.9% |
| 置信残基 (pLDDT 70-90) 占比 | 2.5% |
| 中等置信 (pLDDT 50-70) 占比 | 2.3% |
| 低置信 (pLDDT<50) 占比 | 20.3% |
| 有序区域 (pLDDT>70) 占比 | 77.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=84.6，有序区 77.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR015943, IPR019775, IPR036322, IPR001680, IPR051179; Pfam: PF00400 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RPL10 | 0.957 | 0.939 | — |
| NOD2 | 0.952 | 0.000 | — |
| EGFR | 0.915 | 0.130 | — |
| TBXA2R | 0.890 | 0.292 | — |
| RPL10L | 0.889 | 0.842 | — |
| GRWD1 | 0.863 | 0.000 | — |
| AEN | 0.783 | 0.782 | — |
| MRTO4 | 0.712 | 0.000 | — |
| NMD3 | 0.710 | 0.000 | — |
| TBL3 | 0.708 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NELFCD | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| GABARAPL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| melB1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| Irak1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |
| BHLHE40 | psi-mi:"MI:0397"(two hybrid array) | pubmed:29892012|doi:10.1038/s4 |
| VPS52 | psi-mi:"MI:0397"(two hybrid array) | pubmed:29892012|doi:10.1038/s4 |
| AEN | psi-mi:"MI:0397"(two hybrid array) | pubmed:29892012|doi:10.1038/s4 |
| MKLN1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| MMADHC | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.6 + PDB: 无 | pLDDT=84.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane; Cytoplasm / Microtubules; 额外: Plasma membrane, Cytokinetic bri | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. AAMP — Angio-associated migratory cell protein，非常新颖，仅有少数基础研究。
2. 蛋白大小434 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 36 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13685
- Protein Atlas: https://www.proteinatlas.org/ENSG00000127837-AAMP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AAMP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13685
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Microtubules (approved)。来源: https://www.proteinatlas.org/ENSG00000127837-AAMP/subcellular

![](https://images.proteinatlas.org/31868/2152_E12_29_blue_red_green.jpg)
![](https://images.proteinatlas.org/31868/2152_E12_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/31868/2177_E11_42_blue_red_green.jpg)
![](https://images.proteinatlas.org/31868/2177_E11_64_blue_red_green.jpg)
![](https://images.proteinatlas.org/31868/2242_C12_49_blue_red_green.jpg)
![](https://images.proteinatlas.org/31868/2242_C12_96_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q13685-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

---
type: protein-evaluation
gene: "CTDSPL2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CTDSPL2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CTDSPL2 / SCP4 |
| 蛋白名称 | CTD small phosphatase-like protein 2 |
| 蛋白大小 | 466 aa / 53.0 kDa |
| UniProt ID | Q05D32 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 466 aa / 53.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011948, IPR004274, IPR036412, IPR023214, IPR050 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.0/180** | |
| **归一化总分** | | | **76.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 18 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SCP4 |

**关键文献**:
1. A Transcriptomic Signature of Depressive Symptoms in Late Life.. *Biological psychiatry global open science*. PMID: 40094036
2. The phosphatase CTDSPL2 promotes proliferation, invasion, metastasis and regorafenib resistance in osteosarcoma.. *Journal of bone oncology*. PMID: 40352265
3. CTD small phosphatase like 2 (CTDSPL2) can increase ε- and γ-globin gene expression in K562 cells and CD34+ cells derived from umbilical cord blood.. *BMC cell biology*. PMID: 20932329
4. SCP4 Promotes Gluconeogenesis Through FoxO1/3a Dephosphorylation.. *Diabetes*. PMID: 28851713
5. C-terminal domain small phosphatase-like 2 promotes epithelial-to-mesenchymal transition via Snail dephosphorylation and stabilization.. *Open biology*. PMID: 29618518

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.6 |
| 高置信度残基 (pLDDT>90) 占比 | 42.3% |
| 置信残基 (pLDDT 70-90) 占比 | 3.6% |
| 中等置信 (pLDDT 50-70) 占比 | 4.5% |
| 低置信 (pLDDT<50) 占比 | 49.6% |
| 有序区域 (pLDDT>70) 占比 | 45.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=65.6），有序残基占 45.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011948, IPR004274, IPR036412, IPR023214, IPR050365; Pfam: PF03031 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PDIK1L | 0.872 | 0.802 | — |
| STK35 | 0.699 | 0.613 | — |
| GTF2F1 | 0.632 | 0.477 | — |
| KPNA4 | 0.614 | 0.459 | — |
| KPNA2 | 0.604 | 0.591 | — |
| KLHDC1 | 0.533 | 0.053 | — |
| UBLCP1 | 0.520 | 0.074 | — |
| KPNA3 | 0.500 | 0.421 | — |
| GAS2L1 | 0.477 | 0.000 | — |
| KPNA1 | 0.476 | 0.397 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PDIK1L | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| STK35 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| nleC | psi-mi:"MI:0018"(two hybrid) | pubmed:25519916|imex:IM-23549 |
| MED15 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| JAK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| CDC42BPA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| MYBL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| FBXL19 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| ELOC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| ATP5F1EP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.6 + PDB: 无 | pLDDT=65.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. CTDSPL2 — CTD small phosphatase-like protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小466 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=65.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q05D32
- Protein Atlas: https://www.proteinatlas.org/ENSG00000137770-CTDSPL2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CTDSPL2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q05D32
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000137770-CTDSPL2/subcellular

![](https://images.proteinatlas.org/40763/475_A11_1_red_green.jpg)
![](https://images.proteinatlas.org/40763/475_A11_2_red_green.jpg)
![](https://images.proteinatlas.org/40763/477_A11_1_red_green.jpg)
![](https://images.proteinatlas.org/40763/477_A11_2_red_green.jpg)
![](https://images.proteinatlas.org/40763/479_A11_2_red_green.jpg)
![](https://images.proteinatlas.org/40763/479_A11_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q05D32-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

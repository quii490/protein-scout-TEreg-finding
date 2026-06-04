---
type: protein-evaluation
gene: "RAB34"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RAB34 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RAB34 / NARR |
| 蛋白名称 | Ras-related protein Rab-34, isoform NARR |
| 蛋白大小 | 198 aa / 21.1 kDa |
| UniProt ID | P0DI83 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm, Primary cilium; 额外: Centrosome, Basal body, Cyt; UniProt: Nucleus; Nucleus, nucleolus |
| 蛋白大小 | 8/10 | ×1 | 8 | 198 aa / 21.1 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=60 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=46.8; PDB: 无 |
| 调控结构域 | 4/10 | ×2 | 8 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **110.0/180** | |
| **归一化总分** | | | **61.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Primary cilium; 额外: Centrosome, Basal body, Cytosol | Approved |
| UniProt | Nucleus; Nucleus, nucleolus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleolus (GO:0005730)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 60 |
| PubMed broad count | 86 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NARR |

**关键文献**:
1. Discovery of Kinetin in inhibiting colorectal cancer progression via enhancing PSMB1-mediated RAB34 degradation.. *Cancer letters*. PMID: 38159835
2. Localization, traffic and function of Rab34 in adipocyte lipid and endocrine functions.. *Journal of biomedical science*. PMID: 38183057
3. Pathogenic RAB34 variants impair primary cilium assembly and cause a novel oral-facial-digital syndrome.. *Human molecular genetics*. PMID: 37384395
4. RAB34 was a progression- and prognosis-associated biomarker in gliomas.. *Tumour biology : the journal of the International Society for Oncodevelopmental Biology and Medicine*. PMID: 25501506
5. DENND6A links Arl8b to a Rab34/RILP/dynein complex, regulating lysosomal positioning and autophagy.. *Nature communications*. PMID: 38296963

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 46.8 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 0.0% |
| 中等置信 (pLDDT 50-70) 占比 | 41.9% |
| 低置信 (pLDDT<50) 占比 | 58.1% |
| 有序区域 (pLDDT>70) 占比 | 0.0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=46.8），有序残基占 0.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释稀疏，属新颖蛋白正常现象。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RILP | 0.933 | 0.184 | — |
| UNC13B | 0.811 | 0.000 | — |
| RABGGTA | 0.672 | 0.000 | — |
| STXBP1 | 0.621 | 0.000 | — |
| GDI1 | 0.615 | 0.543 | — |
| RABGGTB | 0.609 | 0.000 | — |
| WASF2 | 0.604 | 0.000 | — |
| CHM | 0.579 | 0.000 | — |
| RPL23A | 0.567 | 0.000 | — |
| VPS33A | 0.557 | 0.476 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Slc2a4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:16396496|mint:MINT-5218 |
| bgaB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| EPHX1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ETF1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| IL12RB2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| OR4F21 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| CBX6 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| WBP2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ZC3H13 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| MKX | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=46.8 + PDB: 无 | pLDDT=46.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, nucleolus / Nucleoplasm, Primary cilium; 额外: Centrosome, Basal | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. RAB34 — Ras-related protein Rab-34, isoform NARR，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小198 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 60 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=46.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P0DI83
- Protein Atlas: https://www.proteinatlas.org/ENSG00000109113-RAB34/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RAB34
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P0DI83
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

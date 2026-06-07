---
type: protein-evaluation
gene: "SPOPL"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SPOPL 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SPOPL |
| 蛋白名称 | Speckle-type POZ protein-like |
| 蛋白大小 | 392 aa / 44.6 kDa |
| UniProt ID | Q6IQ16 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 392 aa / 44.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=86.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000210, IPR002083, IPR011333, IPR008974; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.5/180** | |
| **归一化总分** | | | **76.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- Cul3-RING ubiquitin ligase complex (GO:0031463)
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 14 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Expression and clinical relevance of SPOPL in medulloblastoma.. *Oncology letters*. PMID: 28928843
2. SPOPL induces tumorigenicity and stemness in glioma stem cells by activating Notch signaling.. *Journal of neuro-oncology*. PMID: 37523046
3. miR-197-3p Promotes Osteosarcoma Stemness and Chemoresistance by Inhibiting SPOPL.. *Journal of clinical medicine*. PMID: 36769824
4. Evolutionary expansion of SPOP and associated TD/POZ gene family: impact of evolutionary route on gene expression pattern.. *Gene*. PMID: 20399258
5. Highlighted role of VEGFA in follow up of celiac disease.. *Gastroenterology and hepatology from bed to bench*. PMID: 31528310

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.2 |
| 高置信度残基 (pLDDT>90) 占比 | 67.3% |
| 置信残基 (pLDDT 70-90) 占比 | 17.9% |
| 中等置信 (pLDDT 50-70) 占比 | 3.6% |
| 低置信 (pLDDT<50) 占比 | 11.2% |
| 有序区域 (pLDDT>70) 占比 | 85.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=86.2，有序区 85.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000210, IPR002083, IPR011333, IPR008974; Pfam: PF00651, PF22486 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL3 | 0.999 | 0.749 | — |
| SPOP | 0.966 | 0.469 | — |
| GLI1 | 0.952 | 0.296 | — |
| GLI3 | 0.951 | 0.296 | — |
| GLI2 | 0.949 | 0.296 | — |
| RBX1 | 0.947 | 0.091 | — |
| SUFU | 0.940 | 0.000 | — |
| KBTBD7 | 0.921 | 0.084 | — |
| KLHL20 | 0.916 | 0.091 | — |
| KBTBD8 | 0.914 | 0.099 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Q81SX2 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| KPNA5 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| MYD88 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ATF2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CREB5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| RXRB | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SPOP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HOMER1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| BBS5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HOMER2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.2 + PDB: 无 | pLDDT=86.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SPOPL — Speckle-type POZ protein-like，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小392 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6IQ16
- Protein Atlas: https://www.proteinatlas.org/ENSG00000144228-SPOPL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SPOPL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6IQ16
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6IQ16-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6IQ16 |
| SMART | SM00225;SM00061; |
| UniProt Domain [FT] | DOMAIN 31..161; /note="MATH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00129"; DOMAIN 200..267; /note="BTB"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00037" |
| InterPro | IPR000210;IPR002083;IPR011333;IPR008974; |
| Pfam | PF00651;PF22486; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000144228-SPOPL/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| KPNA5 | Intact, Biogrid | true |
| ATF2 | Intact | false |
| EPS15 | Biogrid | false |
| MYD88 | Intact | false |
| RXRB | Intact | false |
| SPOP | Intact, Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

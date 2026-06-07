---
type: protein-evaluation
gene: "CEPT1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation, E-batch]
status: scored
---

## CEPT1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CEPT1 / — |
| 蛋白名称 | Choline/ethanolaminephosphotransferase 1 |
| 蛋白大小 | 416 aa / 46.6 kDa |
| UniProt ID | Q9Y6K0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: —; UniProt: Endoplasmic reticulum membrane; Nucleus membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 416 aa / 46.6 kDa |
| 研究新颖性 | 9/10 | ×5 | 45 | PubMed strict=34 篇 |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=89.0; PDB: 暂无 |
| 调控结构域 | 9/10 | ×2 | 18 | InterPro: IPR000462, IPR043130, IPR048254, IPR014472; Pfam: PF01066 |
| PPI 网络 | 9/10 | ×3 | 27 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.2 | AlphaFold 结构预测: +0.25 |
| **原始总分** | | | **160.2/180** | |
| **归一化总分 (÷1.83)** | | | **87.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | — | — |
| UniProt | Endoplasmic reticulum membrane | ECO:0000269
| UniProt | Nucleus membrane | ECO:0000269

**IF 图像说明**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**GO Cellular Component**:
- endoplasmic reticulum membrane (GO:0005789) [IDA:UniProtKB]
- Golgi apparatus (GO:0005794) [IBA:GO_Central]
- membrane (GO:0016020) [TAS:ProtInc]
- nuclear membrane (GO:0031965) [IEA:UniProtKB-SubCell]

**结论**: HPA: —; UniProt: Endoplasmic reticulum membrane; Nucleus membrane

#### 3.2 蛋白大小评估

**评价**: 416 aa / 46.6 kDa，大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 34 |
| PubMed 搜索链接 | [CEPT1 PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=CEPT1) |

**关键文献**:
暂无文献记录。

**评价**: 较新颖，研究关注度低。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.0 |
| 高置信度残基 (pLDDT>90) 占比 | 83.2% |
| 置信残基 (pLDDT 70-90) 占比 | 4.8% |
| 中等置信 (pLDDT 50-70) 占比 | 2.4% |
| 低置信 (pLDDT<50) 占比 | 9.6% |
| 有序区域 (pLDDT>70) 占比 | 88.0% |
| 可用 PDB 条目 | 暂无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000462, IPR043130, IPR048254, IPR014472; Pfam: PF01066 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PCYT2 | 0.991 | 0.000 | — |
| PCYT1A | 0.987 | 0.000 | — |
| PCYT1B | 0.984 | 0.000 | — |
| PEMT | 0.976 | 0.069 | — |
| PISD | 0.972 | 0.000 | — |
| PTDSS2 | 0.966 | 0.000 | — |
| PTDSS1 | 0.956 | 0.000 | — |
| LPCAT2 | 0.952 | 0.000 | — |
| MBOAT2 | 0.943 | 0.000 | — |
| LPCAT3 | 0.943 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:17314511 |
| cutF | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| P/V | psi-mi:"MI:0096"(pull down) | pubmed:21911578|imex:IM-17703 |
| H9A910 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:30177828|imex:IM-26452 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| ELK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| TMEM14B | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| AFDN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| RBM6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |

**PPI 互证分析**:
STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0/15。

**评价**: STRING + IntAct 双源 PPI 数据充分。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold | pLDDT=89.0, v6 | 预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Nucleus membrane / — | 部分一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- AlphaFold 结构预测: +0.25
- 单库核定位证据: +0.25
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5

**总分**: +1.2 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐

**归一化总分**: 87.6/100

**核心优势**:
1. CEPT1 — Choline/ethanolaminephosphotransferase 1，极度新颖，几乎未被系统研究（PubMed 34 篇）。
2. 蛋白大小416 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。
3. AlphaFold pLDDT=89.0，结构预测质量高。

**风险/不确定性**:
1. 功能研究较少，具体调控机制待阐明

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y6K0
- Protein Atlas: https://www.proteinatlas.org/search/CEPT1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CEPT1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y6K0
- STRING: https://string-db.org/network/9606.CEPT1
- Packet data timestamp: 2026-06-03 04:50:34

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y6K0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9Y6K0 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR000462;IPR043130;IPR048254;IPR014472; |
| Pfam | PF01066; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000134255-CEPT1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CAPZB | Opencell | false |
| DCP1B | Opencell | false |
| KLRB1 | Bioplex | false |
| PGRMC1 | Opencell | false |
| RPL5 | Opencell | false |
| SPG21 | Intact | false |
| TMEM14B | Intact | false |
| TMEM263 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

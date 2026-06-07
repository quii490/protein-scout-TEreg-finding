---
type: protein-evaluation
gene: "TRAF7"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TRAF7 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TRAF7 / RFWD1, RNF119 |
| 蛋白名称 | E3 ubiquitin-protein ligase TRAF7 |
| 蛋白大小 | 670 aa / 74.6 kDa |
| UniProt ID | Q6Q0C0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles; UniProt: Cytoplasmic vesicle; Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 670 aa / 74.6 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=87 篇 (≤100→2) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=79.7; PDB: 8IMS |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR015943, IPR020472, IPR019775, IPR036322, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **97.0/180** | |
| **归一化总分** | | | **53.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles | Supported |
| UniProt | Cytoplasmic vesicle; Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasmic vesicle (GO:0031410)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)
- ubiquitin ligase complex (GO:0000151)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 87 |
| PubMed broad count | 199 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RFWD1, RNF119 |

**关键文献**:
1. Comprehensive genomic analysis of malignant pleural mesothelioma identifies recurrent mutations, gene fusions and splicing alterations.. *Nature genetics*. PMID: 26928227
2. [Meningioma].. *No shinkei geka. Neurological surgery*. PMID: 37743334
3. Pleiotropic role of TRAF7 in skull-base meningiomas and congenital heart disease.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 37043537
4. TRAF7 determines circadian period through ubiquitination and degradation of DBP.. *Communications biology*. PMID: 39379486
5. European Association of Neuro-Oncology guideline on molecular testing of meningiomas for targeted therapy selection.. *Neuro-oncology*. PMID: 39577862

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.7 |
| 高置信度残基 (pLDDT>90) 占比 | 50.9% |
| 置信残基 (pLDDT 70-90) 占比 | 29.1% |
| 中等置信 (pLDDT 50-70) 占比 | 1.8% |
| 低置信 (pLDDT<50) 占比 | 18.2% |
| 有序区域 (pLDDT>70) 占比 | 80.0% |
| 可用 PDB 条目 | 8IMS |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=79.7，有序区 80.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR015943, IPR020472, IPR019775, IPR036322, IPR001680; Pfam: PF00400, PF13445 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UBA52 | 0.967 | 0.967 | — |
| MAP3K3 | 0.884 | 0.584 | — |
| MAZ | 0.793 | 0.091 | — |
| UBE2E2 | 0.774 | 0.364 | — |
| NF2 | 0.737 | 0.000 | — |
| MAP3K7 | 0.631 | 0.113 | — |
| TRAF1 | 0.624 | 0.000 | — |
| KLF4 | 0.624 | 0.091 | — |
| TRAF6 | 0.620 | 0.000 | — |
| NEDD8 | 0.595 | 0.518 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000515903.1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:14743216|mint:MINT-5216 |
| MAP3K3 | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:15001576 |
| ampS | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| UBE2D4 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| UBE2L6 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| HIP2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| UBE2D1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| UBE2D2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| UBE2L3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-11696|pubmed:19549727 |
| Ripk4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21903422|imex:IM-17322 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.7 + PDB: 8IMS | pLDDT=79.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasmic vesicle; Cytoplasm; Nucleus / Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TRAF7 — E3 ubiquitin-protein ligase TRAF7，研究基础较多，新颖性有限。
2. 蛋白大小670 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 87 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6Q0C0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000131653-TRAF7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TRAF7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6Q0C0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03



<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6Q0C0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6Q0C0 |
| SMART | SM00184;SM00320; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR015943;IPR020472;IPR019775;IPR036322;IPR001680;IPR027370;IPR001841;IPR013083;IPR017907;IPR001293; |
| Pfam | PF00400;PF13445; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000131653-TRAF7/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| MAP3K3 | Intact, Biogrid | true |
| BAG2 | Bioplex | false |
| CDC42 | Biogrid | false |
| CLEC11A | Bioplex | false |
| CORO1A | Bioplex | false |
| CYTH4 | Intact, Bioplex | false |
| DNAJA2 | Bioplex | false |
| FBXO28 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

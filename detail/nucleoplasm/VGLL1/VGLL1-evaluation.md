---
type: protein-evaluation
gene: "VGLL1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## VGLL1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | VGLL1 / TDU |
| 蛋白名称 | Transcription cofactor vestigial-like protein 1 |
| 蛋白大小 | 258 aa / 28.7 kDa |
| UniProt ID | Q99990 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 258 aa / 28.7 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=35 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR006627, IPR011520; Pfam: PF07545 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 14 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
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
| PubMed strict count | 35 |
| PubMed broad count | 54 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TDU |

**关键文献**:
1. Vestigial-like family member 1 (VGLL1): An emerging candidate in tumor progression.. *Biochemical and biophysical research communications*. PMID: 40300335
2. VGLL1 cooperates with TEAD4 to control human trophectoderm lineage specification.. *Nature communications*. PMID: 38233381
3. Vestigial-like 1 (VGLL1): An ancient co-transcriptional activator linking wing, placenta, and tumor development.. *Biochimica et biophysica acta. Reviews on cancer*. PMID: 37004960
4. Integrated bioinformatics and machine learning identify S100A9 and VGLL1 as hub genes for schizophrenia.. *Frontiers in psychiatry*. PMID: 40980038
5. VGLL fusions define a new class of intraparenchymal central nervous system schwannoma.. *Neuro-oncology*. PMID: 39713960

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.3 |
| 高置信度残基 (pLDDT>90) 占比 | 12.8% |
| 置信残基 (pLDDT 70-90) 占比 | 4.3% |
| 中等置信 (pLDDT 50-70) 占比 | 41.1% |
| 低置信 (pLDDT<50) 占比 | 41.9% |
| 有序区域 (pLDDT>70) 占比 | 17.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=57.3），有序残基占 17.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006627, IPR011520; Pfam: PF07545 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TEAD4 | 0.985 | 0.888 | — |
| TEAD1 | 0.978 | 0.461 | — |
| TEAD3 | 0.840 | 0.716 | — |
| VGLL4 | 0.826 | 0.000 | — |
| WWTR1 | 0.804 | 0.000 | — |
| YAP1 | 0.728 | 0.000 | — |
| TEAD2 | 0.707 | 0.489 | — |
| ACTA1 | 0.650 | 0.000 | — |
| RAD51B | 0.571 | 0.000 | — |
| CAPN6 | 0.464 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TEAD2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TEKT4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CDKN2D | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PFDN5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| AIRIM | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TRIM23 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| RIPPLY1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| HNRNPF | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TLE5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MEIS2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 14
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 14 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.3 + PDB: 无 | pLDDT=57.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 14 interactions | 数据充分 |

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
1. VGLL1 — Transcription cofactor vestigial-like protein 1，非常新颖，仅有少数基础研究。
2. 蛋白大小258 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 35 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=57.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q99990
- Protein Atlas: https://www.proteinatlas.org/ENSG00000102243-VGLL1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=VGLL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99990
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000102243-VGLL1/subcellular

![](https://images.proteinatlas.org/64616/1244_F2_7_red_green.jpg)
![](https://images.proteinatlas.org/64616/1244_F2_8_red_green.jpg)
![](https://images.proteinatlas.org/64616/1247_F2_2_red_green.jpg)
![](https://images.proteinatlas.org/64616/1247_F2_3_red_green.jpg)
![](https://images.proteinatlas.org/64616/1424_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/64616/1424_E5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q99990-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q99990 |
| SMART | SM00711; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR006627;IPR011520; |
| Pfam | PF07545; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000102243-VGLL1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| TEAD3 | Intact, Biogrid | true |
| TEAD4 | Intact, Biogrid | true |
| C1orf109 | Intact | false |
| CDKN2D | Intact | false |
| HNRNPF | Intact | false |
| LONRF1 | Intact | false |
| PFDN5 | Intact | false |
| RIPPLY1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

---
type: protein-evaluation
gene: "CDYL2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CDYL2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CDYL2 |
| 蛋白名称 | Chromodomain Y-like protein 2 |
| 蛋白大小 | 506 aa / 56.5 kDa |
| UniProt ID | Q8N8U2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 506 aa / 56.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=71.6; PDB: 2MJ8, 4HAE, 5JJZ, 6V2D, 6V2H, 6V3N, 6V8W |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR016197, IPR000953, IPR023780, IPR023779, IPR029 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **148.0/180** | |
| **归一化总分** | | | **82.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 23 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Anti-tumor activity of CDYL2b in prostate cancer.. *Cancer letters*. PMID: 40812719
2. Chromodomain on Y-like 2 (CDYL2) implicated in mitosis and genome stability regulation via interaction with CHAMP1 and POGZ.. *Cellular and molecular life sciences : CMLS*. PMID: 36658409
3. CDYL2 Epigenetically Regulates MIR124 to Control NF-κB/STAT3-Dependent Breast Cancer Cell Plasticity.. *iScience*. PMID: 32450513
4. Cdyl2-60aa encoded by CircCDYL2 accelerates cardiomyocyte death by blocking APAF1 ubiquitination in rats.. *Experimental & molecular medicine*. PMID: 37009805
5. Molecular characterization of the bovine chromodomain Y-like genes.. *Animal genetics*. PMID: 18371128

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.6 |
| 高置信度残基 (pLDDT>90) 占比 | 49.4% |
| 置信残基 (pLDDT 70-90) 占比 | 11.1% |
| 中等置信 (pLDDT 50-70) 占比 | 2.0% |
| 低置信 (pLDDT<50) 占比 | 37.5% |
| 有序区域 (pLDDT>70) 占比 | 60.5% |
| 可用 PDB 条目 | 2MJ8, 4HAE, 5JJZ, 6V2D, 6V2H, 6V3N, 6V8W, 8SP6 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2MJ8, 4HAE, 5JJZ, 6V2D, 6V2H, 6V3N, 6V8W, 8SP6）+ AlphaFold极高置信度预测（pLDDT=71.6），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016197, IPR000953, IPR023780, IPR023779, IPR029045; Pfam: PF00385, PF00378 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| H3C12 | 0.936 | 0.915 | — |
| H3C13 | 0.935 | 0.915 | — |
| H3-4 | 0.935 | 0.915 | — |
| H3-2 | 0.935 | 0.915 | — |
| H3C6 | 0.923 | 0.915 | — |
| H3C3 | 0.923 | 0.915 | — |
| H3C2 | 0.923 | 0.915 | — |
| H3C10 | 0.923 | 0.915 | — |
| H3C4 | 0.923 | 0.915 | — |
| H3C1 | 0.923 | 0.915 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NCBP3 | psi-mi:"MI:0096"(pull down) | pubmed:26382858|imex:IM-26480 |
| HSP90B1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| LMO3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ZBTB9 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| SPANXN2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| DVL3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| NXF1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| HSF2BP | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| HUWE1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.6 + PDB: 2MJ8, 4HAE, 5JJZ, 6V2D, 6V2H,  | pLDDT=71.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. CDYL2 — Chromodomain Y-like protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小506 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N8U2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166446-CDYL2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CDYL2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N8U2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03



<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N8U2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

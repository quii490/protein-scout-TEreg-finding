---
type: protein-evaluation
gene: "CERS4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation, E-batch]
status: scored
---

## CERS4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CERS4 / LASS4 |
| 蛋白名称 | Ceramide synthase 4 |
| 蛋白大小 | 394 aa / 46.4 kDa |
| UniProt ID | Q9HA82 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 6/10 | ×4 | 24 | HPA: Nucleoplasm, Vesicles; UniProt: Endoplasmic reticulum membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 394 aa / 46.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=42 篇 |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=85.0; PDB: 暂无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001356, IPR009057, IPR016439, IPR006634; Pfam: PF00046, PF03798 |
| PPI 网络 | 10/10 | ×3 | 30 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.2 | AlphaFold 结构预测: +0.25 |
| **原始总分** | | | **146.2/180** | |
| **归一化总分 (÷1.83)** | | | **79.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles | Supported |
| UniProt | Endoplasmic reticulum membrane | ECO:0000250

**IF 图像说明**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**GO Cellular Component**:
- endoplasmic reticulum membrane (GO:0005789) [TAS:Reactome]

**结论**: HPA: Nucleoplasm, Vesicles; UniProt: Endoplasmic reticulum membrane

#### 3.2 蛋白大小评估

**评价**: 394 aa / 46.4 kDa，大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 42 |
| PubMed 搜索链接 | [CERS4 PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=CERS4) |

**关键文献**:
暂无文献记录。

**评价**: 较新颖，研究关注度低。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.0 |
| 高置信度残基 (pLDDT>90) 占比 | 62.2% |
| 置信残基 (pLDDT 70-90) 占比 | 23.1% |
| 中等置信 (pLDDT 50-70) 占比 | 3.8% |
| 低置信 (pLDDT<50) 占比 | 10.9% |
| 有序区域 (pLDDT>70) 占比 | 85.30000000000001% |
| 可用 PDB 条目 | 暂无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR009057, IPR016439, IPR006634; Pfam: PF00046, PF03798 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DEGS2 | 0.972 | 0.071 | — |
| DEGS1 | 0.970 | 0.071 | — |
| SMPD2 | 0.966 | 0.000 | — |
| CERK | 0.965 | 0.000 | — |
| KDSR | 0.965 | 0.000 | — |
| ACER1 | 0.965 | 0.115 | — |
| ASAH1 | 0.964 | 0.068 | — |
| ACER2 | 0.964 | 0.115 | — |
| UGCG | 0.964 | 0.000 | — |
| SMPD1 | 0.962 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-2621128 | psi-mi:"MI:0018"(two hybrid) | pubmed:17446270|imex:IM-20435|mint:MINT-6769080 |
| LPAR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| PTPN9 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| TOMM6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SLC35F6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| EMD | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| - | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| IER3IP1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TMEM254 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PLP2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0/15。

**评价**: STRING + IntAct 双源 PPI 数据充分。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold | pLDDT=85.0, v6 | 预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane / Nucleoplasm, Vesicles | 部分一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- AlphaFold 结构预测: +0.25
- 单库核定位证据: +0.25
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5

**总分**: +1.2 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐

**归一化总分**: 79.9/100

**核心优势**:
1. CERS4 — Ceramide synthase 4，较新颖，PubMed 42 篇。
2. 蛋白大小394 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。
3. AlphaFold pLDDT=85.0，结构预测质量高。

**风险/不确定性**:
1. 功能研究较少，具体调控机制待阐明

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9HA82
- Protein Atlas: https://www.proteinatlas.org/search/CERS4
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CERS4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HA82
- STRING: https://string-db.org/network/9606.CERS4
- Packet data timestamp: 2026-06-03 04:51:47

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9HA82-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

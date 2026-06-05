---
type: protein-evaluation
gene: "CMIP"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CMIP — REJECTED (研究热度过高 (PubMed strict=188，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CMIP |
| 蛋白名称 | C-Maf-inducing protein |
| 蛋白大小 | 773 aa / 86.3 kDa |
| UniProt ID | Q8IY22 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | x1 | 10 | 773 aa / 86.3 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=188 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=78.8; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 29 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 188 |
| PubMed broad count | 209 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Potential global distribution of Pochazia shantungensis (Chou & Lu, 1977), under current and future climatic scenarios based on an optimised MaxEnt model.. *Bull Entomol Res*. PMID: 42169605
2. Cellugyrin (Synaptogyrin-2) Regulates Macrophage Phagocytosis of Aggregatibacter actinomycetemcomitans (Aa).. *Pathogens*. PMID: 42198631
3. Grade C molar-incisor pattern periodontitis classification and its challenges.. *J Periodontol*. PMID: 41972922
4. Km-scale coupled simulation and model-observation SST trend discrepancy.. *Proc Natl Acad Sci U S A*. PMID: 41712637
5. Localized Periodontitis in Young Individuals: Aggregatibacter JP2 Clone, Immunological Dysfunctions and Other Stories.. *J Periodontal Res*. PMID: 41631366

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.8 |
| 高置信度残基 (pLDDT>90) 占比 | 51.6% |
| 置信残基 (pLDDT 70-90) 占比 | 25.9% |
| 中等置信 (pLDDT 50-70) 占比 | 4.5% |
| 低置信 (pLDDT<50) 占比 | 18.0% |
| 有序区域 (pLDDT>70) 占比 | 77.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=78.8，有序区 77.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ATP2C2 | 0.000 | 0.000 | — |
| FLNA | 0.000 | 0.000 | — |
| RELA | 0.000 | 0.000 | — |
| KIAA0319 | 0.000 | 0.000 | — |
| DCDC2 | 0.000 | 0.000 | — |
| NFXL1 | 0.000 | 0.000 | — |
| CNTNAP2 | 0.000 | 0.000 | — |
| DNAAF4 | 0.000 | 0.000 | — |
| MAF | 0.000 | 0.000 | — |
| GCFC2 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q9BYV2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q969E8 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q8IY22-3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q9NQZ6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:P48039 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q8IY22-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q8IY22 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:O15357 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P07357 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P47900 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 29
- 调控相关比例: 1 / 20 = 5%

**评价**: STRING 25 个预测互作，IntAct 29 个实验互作。调控相关配体占比 5%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.8 + PDB: 无 | pLDDT=78.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 25 + 29 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CMIP -- C-Maf-inducing protein，研究基础较多，新颖性有限。
2. 蛋白大小773 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 188 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 188 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IY22
- Protein Atlas: https://www.proteinatlas.org/ENSG00000153815-CMIP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CMIP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IY22
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IY22-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

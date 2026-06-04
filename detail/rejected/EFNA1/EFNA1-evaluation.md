---
type: protein-evaluation
gene: "EFNA1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EFNA1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=147，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EFNA1 |
| 蛋白名称 | Ephrin-A1 |
| 蛋白大小 | 205 aa / 23.8 kDa |
| UniProt ID | P20827 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane; Secreted |
| 蛋白大小 | 10/10 | ×1 | 10 | 205 aa / 23.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=147 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=79.1; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **61.0/180** | |
| **归一化总分** | | | **33.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | No data |
| UniProt | Cell membrane; Secreted | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 147 |
| PubMed broad count | 535 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Cross-species single-cell and spatial transcriptomic mapping reveals EFNA1-EPHA4-mediated stem-like epithelial-macrophage crosstalk driving colorectal cancer progression.. *Cancer Lett*. PMID: 41966512
2. Investigating trophoblast invasion and angiogenesis expression changes in a caloric deficient mouse model of fetal growth restriction.. *Reprod Biol*. PMID: 41576455
3. Comprehensive multi-omics analysis reveals prognostic, immune, and therapeutic signatures of TNFAIP family genes in breast cancer.. *PLoS One*. PMID: 42213680
4. Distinct genetic variants from the whole-exome sequencing of syndromic anorectal malformations: A cross-sectional study.. *iScience*. PMID: 42058895
5. Identification of EFNA family as new potential prognostic biomarkers correlated with immune cell infiltration in hepatocellular carcinoma.. *Transl Cancer Res*. PMID: 42180949

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.1 |
| 高置信度残基 (pLDDT>90) 占比 | 55.6% |
| 置信残基 (pLDDT 70-90) 占比 | 8.8% |
| 中等置信 (pLDDT 50-70) 占比 | 20.5% |
| 低置信 (pLDDT<50) 占比 | 15.1% |
| 有序区域 (pLDDT>70) 占比 | 64.4% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 中等质量（pLDDT=79.1，有序区 64.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EPHA2 | 0.000 | 0.000 | — |
| EPHA1 | 0.000 | 0.000 | — |
| EPHA4 | 0.000 | 0.000 | — |
| EPHA10 | 0.000 | 0.000 | — |
| EPHA3 | 0.000 | 0.000 | — |
| EPHA5 | 0.000 | 0.000 | — |
| EPHA8 | 0.000 | 0.000 | — |
| EPHA7 | 0.000 | 0.000 | — |
| RASA1 | 0.000 | 0.000 | — |
| EPHB2 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:P26641 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q92993 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:P61956 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:P02775 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:P52793 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:- |
| uniprotkb:Q15375 | psi-mi:"MI:0808"(comigration in sds page) | pubmed:- |
| uniprotkb:P29317 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:- |
| uniprotkb:Q9H706-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:- |
| uniprotkb:P54764 | psi-mi:"MI:0411"(enzyme linked immunosorbent assay | pubmed:- |
| uniprotkb:Q96KA5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 15
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.1 + PDB: 无 | pLDDT=79.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane; Secreted / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 25 + 15 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. EFNA1 — Ephrin-A1，研究基础较多，新颖性有限。
2. 蛋白大小205 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 147 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P20827
- Protein Atlas: https://www.proteinatlas.org/ENSG00000169242-EFNA1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EFNA1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P20827
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

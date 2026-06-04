---
type: protein-evaluation
gene: "CBLL2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CBLL2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CBLL2 |
| 蛋白名称 | E3 ubiquitin-protein ligase CBLL2 |
| 蛋白大小 | 425 aa / 48.8 kDa |
| UniProt ID | Q8N7E2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 425 aa / 48.8 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.0; PDB: 无 |
| 🧬 调控结构域 | 5/10 | ×2 | 10 | 无注释结构域 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 30 interactions |
| ➕ 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **105.5/180** | |
| **归一化总分** | | | **58.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | No data |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 3 |
| 别名(未计入scoring) |  |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.0 |
| 高置信度残基 (pLDDT>90) 占比 | 17.2% |
| 置信残基 (pLDDT 70-90) 占比 | 6.4% |
| 中等置信 (pLDDT 50-70) 占比 | 11.3% |
| 低置信 (pLDDT<50) 占比 | 65.2% |
| 有序区域 (pLDDT>70) 占比 | 23.6% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/CBLL2/CBLL2-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=55.0），有序残基占 23.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SERTAD4 | 0.000 | 0.000 | — |
| WTAP | 0.000 | 0.000 | — |
| VIRMA | 0.000 | 0.000 | — |
| ZC3H13 | 0.000 | 0.000 | — |
| UBE3D | 0.000 | 0.000 | — |
| SMCO3 | 0.000 | 0.000 | — |
| PPP2R2D | 0.000 | 0.000 | — |
| OR1J4 | 0.000 | 0.000 | — |
| TRIM63 | 0.000 | 0.000 | — |
| SATL1 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:A8MQ03 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q99750 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:P59991 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:P45984 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q8WWB5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q8N7E2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q9NZ81 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:O75494-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q15007 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q5T200 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 30
- 调控相关比例: 2 / 15 = 13%

**评价**: STRING 15 个预测互作，IntAct 30 个实验互作。调控相关配体占比 13%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.0 + PDB: 无 | pLDDT=55.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 15 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CBLL2 — E3 ubiquitin-protein ligase CBLL2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小425 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=55.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N7E2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000175809-CBLL2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CBLL2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N7E2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/CBLL2/CBLL2-PAE.png]]

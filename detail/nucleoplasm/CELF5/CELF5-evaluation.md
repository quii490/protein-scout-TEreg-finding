---
type: protein-evaluation
gene: "CELF5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CELF5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CELF5 |
| 蛋白名称 | CUGBP Elav-like family member 5 |
| 蛋白大小 | 485 aa / 52.4 kDa |
| UniProt ID | Q8N6W0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 4/10 | ×4 | 16 | HPA: 暂无HPA定位数据; UniProt: Nucleus; Cytoplasm |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 485 aa / 52.4 kDa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=28 篇 (≤40→8) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.8; PDB: 无 |
| 🧬 调控结构域 | 5/10 | ×2 | 10 | 无注释结构域 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 18 partners; IntAct 30 interactions |
| ➕ 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **103.5/180** | |
| **归一化总分** | | | **57.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | No data |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 28 |
| PubMed broad count | 29 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Comparative language performance in children and adolescents with 22q11.2ds syndrome and down syndrome.. *J Neurodev Disord*. PMID: 42192283
2. Auditory processing and communication in autism: exploring verbal abilities and vocal affective cues.. *Front Psychiatry*. PMID: 42109291
3. Features of Spoken Language Development in Children Who Are Deaf and Hard of Hearing in Kazakhstan.. *J Gen Psychol*. PMID: 41870542
4. Language Skills in Patients With Alexander Disease.. *Am J Speech Lang Pathol*. PMID: 41253129
5. Assessing Language Skills as a Predictor of Children's Listening Difficulties: Validation and Reference Data on a New Auditory Language Task.. *Ear Hear*. PMID: 40887715

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.8 |
| 高置信度残基 (pLDDT>90) 占比 | 36.5% |
| 置信残基 (pLDDT 70-90) 占比 | 16.5% |
| 中等置信 (pLDDT 50-70) 占比 | 7.8% |
| 低置信 (pLDDT<50) 占比 | 39.2% |
| 有序区域 (pLDDT>70) 占比 | 53.0% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CELF5/CELF5-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=67.8），有序残基占 53.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CEBPD | 0.000 | 0.000 | — |
| TNNT2 | 0.000 | 0.000 | — |
| PUM2 | 0.000 | 0.000 | — |
| PAIP2B | 0.000 | 0.000 | — |
| MBNL2 | 0.000 | 0.000 | — |
| MBNL3 | 0.000 | 0.000 | — |
| PUM1 | 0.000 | 0.000 | — |
| CELF3 | 0.000 | 0.000 | — |
| CLCN1 | 0.000 | 0.000 | — |
| RBFOX3 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q8N6W0 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q8IUC3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q9NZ81 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q9BYQ0 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:- |
| uniprotkb:Q15038 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| intact:EBI-22616457 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q6EMK4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q9BYP8 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q9BYR6 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q9BYR5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 18，IntAct interactions: 30
- 调控相关比例: 0 / 18 = 0%

**评价**: STRING 18 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.8 + PDB: 无 | pLDDT=67.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 18 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CELF5 — CUGBP Elav-like family member 5，非常新颖，仅有少数基础研究。
2. 蛋白大小485 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 28 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=67.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N6W0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000161082-CELF5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CELF5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N6W0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CELF5/CELF5-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8N6W0 |
| SMART | SM00360; |
| UniProt Domain [FT] | DOMAIN 45..126; /note="RRM 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00176"; DOMAIN 134..214; /note="RRM 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00176"; DOMAIN 400..478; /note="RRM 3"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00176" |
| InterPro | IPR034648;IPR012677;IPR035979;IPR000504; |
| Pfam | PF00076; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000161082-CELF5/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CYSRT1 | Intact | false |
| DAZAP2 | Intact | false |
| KRTAP1-3 | Intact | false |
| KRTAP12-3 | Intact | false |
| KRTAP17-1 | Intact | false |
| KRTAP19-5 | Intact | false |
| KRTAP26-1 | Intact | false |
| KRTAP3-2 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

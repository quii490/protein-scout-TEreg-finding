---
type: protein-evaluation
gene: "DIEXF"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DIEXF 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DIEXF / UTP25 |
| 蛋白名称 | U3 small nucleolar RNA-associated protein 25 homolog |
| 蛋白大小 | 756 aa / 87.1 kDa |
| UniProt ID | Q68CQ4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 5/10 | ×4 | 20 | HPA: 暂无HPA定位数据; UniProt: Nucleus, nucleolus |
| 蛋白大小 | 10/10 | ×1 | 10 | 756 aa / 87.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=77.8; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.0/180** | |
| **归一化总分** | | | **68.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | No data |
| UniProt | Nucleus, nucleolus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据存在但较为混杂，部分数据源指向非核区室。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 8 |
| 别名(未计入scoring) |  |

**关键文献**:
1. A whole exome sequencing study to identify rare variants in multiplex families with alcohol use disorder.. *Front Psychiatry*. PMID: 37915799
2. Restoring Age-Related Cognitive Decline through Environmental Enrichment: A Transcriptomic Approach.. *Cells*. PMID: 36497123
3. Tissue and cancer-specific expression of DIEXF is epigenetically mediated by an Alu repeat.. *Epigenetics*. PMID: 32041475
4. Loss of digestive organ expansion factor (Diexf) reveals an essential role during murine embryonic development that is independent of p53.. *Oncotarget*. PMID: 29262616
5. Classification and Biomarker Genes Selection for Cancer Gene Expression Data Using Random Forest.. *Iran J Pathol*. PMID: 29563929

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.8 |
| 高置信度残基 (pLDDT>90) 占比 | 52.8% |
| 置信残基 (pLDDT 70-90) 占比 | 17.6% |
| 中等置信 (pLDDT 50-70) 占比 | 11.4% |
| 低置信 (pLDDT<50) 占比 | 18.3% |
| 有序区域 (pLDDT>70) 占比 | 70.4% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/DIEXF/DIEXF-PAE.png]]

**评价**: AlphaFold 中等质量（pLDDT=77.8，有序区 70.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UTP3 | 0.000 | 0.000 | — |
| MPHOSPH10 | 0.000 | 0.000 | — |
| WDR36 | 0.000 | 0.000 | — |
| NOL6 | 0.000 | 0.000 | — |
| RRP36 | 0.000 | 0.000 | — |
| NGDN | 0.000 | 0.000 | — |
| ABT1 | 0.000 | 0.000 | — |
| IMP4 | 0.000 | 0.000 | — |
| NOP14 | 0.000 | 0.000 | — |
| PDCD11 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q68CQ4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q9UJV3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q8NHQ1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q96T51-2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q6FHY5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q96CW1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q9C026 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q96DT7-3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| uniprotkb:Q9BVG3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.8 + PDB: 无 | pLDDT=77.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus, nucleolus / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DIEXF — U3 small nucleolar RNA-associated protein 25 homolog，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小756 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q68CQ4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000117597-DIEXF/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DIEXF
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q68CQ4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/DIEXF/DIEXF-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q68CQ4 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR027417;IPR010678;IPR053939;IPR053940; |
| Pfam | PF06862;PF22916; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000117597-DIEXF/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

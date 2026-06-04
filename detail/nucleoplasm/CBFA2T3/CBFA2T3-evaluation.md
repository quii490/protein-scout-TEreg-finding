---
type: protein-evaluation
gene: "CBFA2T3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CBFA2T3 — REJECTED (研究热度过高 (PubMed strict=157，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CBFA2T3 |
| 蛋白名称 | Transcriptional corepressor CBFA2T3 |
| 蛋白大小 | 653 aa / 71.2 kDa |
| UniProt ID | O75081 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/CBFA2T3/IF_images/SiHa_1.jpg|SiHa]]
![[Projects/TEreg-finding/protein-interested/detail/rejected/CBFA2T3/IF_images/MCF-7_1.jpg|MCF 7]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Nucleus, nucleolus; Nucleus, nucleoplasm; Golgi app |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 653 aa / 71.2 kDa |
| 🆕 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=157 篇 (>100→REJECTED) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.9; PDB: 无 |
| 🧬 调控结构域 | 5/10 | ×2 | 10 | 无注释结构域 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **76.0/180** | |
| **归一化总分** | | | **42.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus; Nucleus, nucleolus; Nucleus, nucleoplasm; Golgi apparatus membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已嵌入

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 157 |
| PubMed broad count | 205 |
| 别名(未计入scoring) |  |

**关键文献**:
1. CBFA2T3 as a Key Prognostic Biomarker in Lung Adenocarcinoma: Insights from Comprehensive Analysis and Validation.. *Biochem Genet*. PMID: 40804206
2. Identification of an NFIA::CBFA2T3 fusion in cerebrospinal fluid confirms the diagnosis of pediatric CNS myeloid sarcoma with erythroid differentiation: a case report and literature review.. *Front Oncol*. PMID: 42205757
3. The NFIA::CBFA2T3 identifies a molecularly defined subgroup of acute erythroid leukemia/erythroid sarcoma.. *Front Oncol*. PMID: 42158426
4. Identification of an Elusive CBFA2T3::GLIS2 Fusion Variant in Acute Megakaryoblastic Leukemia by Whole Genome Sequencing.. *EJHaem*. PMID: 41960216
5. LDB1 represses fetal hemoglobin expression by enhancing BCL11A transcription.. *Redox Biol*. PMID: 41650821

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.9 |
| 高置信度残基 (pLDDT>90) 占比 | 23.9% |
| 置信残基 (pLDDT 70-90) 占比 | 15.8% |
| 中等置信 (pLDDT 50-70) 占比 | 7.4% |
| 低置信 (pLDDT<50) 占比 | 53.0% |
| 有序区域 (pLDDT>70) 占比 | 39.7% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/CBFA2T3/CBFA2T3-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=60.9），有序残基占 39.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LDB1 | 0.000 | 0.000 | — |
| LDB2 | 0.000 | 0.000 | — |
| RUNX1 | 0.000 | 0.000 | — |
| TAL1 | 0.000 | 0.000 | — |
| GATA1 | 0.000 | 0.000 | — |
| CBFA2T2 | 0.000 | 0.000 | — |
| HDAC1 | 0.000 | 0.000 | — |
| TCF3 | 0.000 | 0.000 | — |
| LYL1 | 0.000 | 0.000 | — |
| NCOR1 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:O75081 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:Q9UKD1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:- |
| uniprotkb:A0A6L8P574 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q8D068 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:O75081-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:O43439 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:O75718 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P19174 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P62699 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P82094 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.9 + PDB: 无 | pLDDT=60.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, nucleolus; Nucleus, nucleoplasm; / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CBFA2T3 — Transcriptional corepressor CBFA2T3，研究基础较多，新颖性有限。
2. 蛋白大小653 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 157 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=60.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 157 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75081
- Protein Atlas: https://www.proteinatlas.org/ENSG00000129993-CBFA2T3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CBFA2T3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75081
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/CBFA2T3/CBFA2T3-PAE.png]]





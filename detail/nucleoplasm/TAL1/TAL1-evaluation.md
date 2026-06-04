---
type: protein-evaluation
gene: "TAL1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TAL1 — REJECTED (研究热度过高 (PubMed strict=696，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TAL1 / BHLHA17, SCL, TCL5 |
| 蛋白名称 | T-cell acute lymphocytic leukemia protein 1 |
| 蛋白大小 | 331 aa / 34.3 kDa |
| UniProt ID | P17542 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 331 aa / 34.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=696 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.4; PDB: 2YPA, 2YPB |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011598, IPR036638, IPR040238; Pfam: PF00010 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.5/180** | |
| **归一化总分** | | | **49.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 696 |
| PubMed broad count | 1229 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BHLHA17, SCL, TCL5 |

**关键文献**:
1. A single-cell molecular map of mouse gastrulation and early organogenesis.. *Nature*. PMID: 30787436
2. Rheumatoid arthritis, systemic lupus erythematosus and primary Sjögren's syndrome shared megakaryocyte expansion in peripheral blood.. *Annals of the rheumatic diseases*. PMID: 34462261
3. Direct Phosphorylation and Stabilization of MYC by Aurora B Kinase Promote T-cell Leukemogenesis.. *Cancer cell*. PMID: 32049046
4. Transcription Factor TAL1 in Erythropoiesis.. *Advances in experimental medicine and biology*. PMID: 39017847
5. Integrative dissection of gene regulatory elements at base resolution.. *Cell genomics*. PMID: 37388913

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.4 |
| 高置信度残基 (pLDDT>90) 占比 | 19.0% |
| 置信残基 (pLDDT 70-90) 占比 | 2.7% |
| 中等置信 (pLDDT 50-70) 占比 | 41.4% |
| 低置信 (pLDDT<50) 占比 | 36.9% |
| 有序区域 (pLDDT>70) 占比 | 21.7% |
| 可用 PDB 条目 | 2YPA, 2YPB |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=60.4），有序残基占 21.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR036638, IPR040238; Pfam: PF00010 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TCF12 | 0.999 | 0.983 | — |
| LDB1 | 0.999 | 0.922 | — |
| TCF3 | 0.999 | 0.860 | — |
| LMO2 | 0.999 | 0.977 | — |
| GATA1 | 0.999 | 0.520 | — |
| GATA2 | 0.999 | 0.248 | — |
| RUNX1 | 0.996 | 0.513 | — |
| LDB2 | 0.995 | 0.087 | — |
| GATA3 | 0.993 | 0.521 | — |
| LMO1 | 0.964 | 0.477 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SSA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| SSE1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| GND1 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:16284124 |
| WWM1 | psi-mi:"MI:0089"(protein array) | pubmed:16606443|imex:IM-19627| |
| ESS1 | psi-mi:"MI:0089"(protein array) | pubmed:16606443|imex:IM-19627| |
| URN1 | psi-mi:"MI:0089"(protein array) | pubmed:16606443|imex:IM-19627| |
| PSF2 | psi-mi:"MI:0096"(pull down) | pubmed:14690591 |
| HOXB9 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| CRK | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| DRG1 | psi-mi:"MI:0018"(two hybrid) | pubmed:9824680 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.4 + PDB: 2YPA, 2YPB | pLDDT=60.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. TAL1 — T-cell acute lymphocytic leukemia protein 1，研究基础较多，新颖性有限。
2. 蛋白大小331 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 696 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=60.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 696 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P17542
- Protein Atlas: https://www.proteinatlas.org/ENSG00000162367-TAL1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TAL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P17542
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

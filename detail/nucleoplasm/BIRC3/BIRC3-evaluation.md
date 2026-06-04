---
type: protein-evaluation
gene: "BIRC3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BIRC3 — REJECTED (研究热度过高 (PubMed strict=417，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BIRC3 / API2, MIHC, RNF49 |
| 蛋白名称 | Baculoviral IAP repeat-containing protein 3 |
| 蛋白大小 | 604 aa / 68.4 kDa |
| UniProt ID | Q13489 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 604 aa / 68.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=417 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=74.8; PDB: 2UVL, 3EB5, 3EB6, 3M0A, 3M0D, 7NK0 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001370, IPR048875, IPR001315, IPR011029, IPR050 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 417 |
| PubMed broad count | 831 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: API2, MIHC, RNF49 |

**关键文献**:
1. An Activity-Guided Map of Electrophile-Cysteine Interactions in Primary Human T Cells.. *Cell*. PMID: 32730809
2. Venetoclax Plus Rituximab in Relapsed Chronic Lymphocytic Leukemia: 4-Year Results and Evaluation of Impact of Genomic Complexity and Gene Mutations From the MURANO Phase III Study.. *Journal of clinical oncology : official journal of the American Society of Clinical Oncology*. PMID: 32986498
3. Targeting cIAP2 in a novel senolytic strategy prevents glioblastoma recurrence after radiotherapy.. *EMBO molecular medicine*. PMID: 39972068
4. Identification of osteoarthritis-related genes and potential drugs based on single cell RNA-seq data.. *Molecular medicine (Cambridge, Mass.)*. PMID: 41291434
5. E3 ubiquitin ligase gene BIRC3 modulates TNF-induced cell death pathways and promotes aberrant proliferation in rheumatoid arthritis fibroblast-like synoviocytes.. *Frontiers in immunology*. PMID: 39301019

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.8 |
| 高置信度残基 (pLDDT>90) 占比 | 28.0% |
| 置信残基 (pLDDT 70-90) 占比 | 42.5% |
| 中等置信 (pLDDT 50-70) 占比 | 10.9% |
| 低置信 (pLDDT<50) 占比 | 18.5% |
| 有序区域 (pLDDT>70) 占比 | 70.5% |
| 可用 PDB 条目 | 2UVL, 3EB5, 3EB6, 3M0A, 3M0D, 7NK0 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2UVL, 3EB5, 3EB6, 3M0A, 3M0D, 7NK0）+ AlphaFold极高置信度预测（pLDDT=74.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001370, IPR048875, IPR001315, IPR011029, IPR050784; Pfam: PF00653, PF00619, PF21290 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TNFRSF1A | 0.999 | 0.994 | — |
| TRAF3 | 0.999 | 0.719 | — |
| TRAF2 | 0.999 | 0.991 | — |
| RIPK1 | 0.999 | 0.855 | — |
| TRAF1 | 0.999 | 0.983 | — |
| UBE2D2 | 0.998 | 0.987 | — |
| TRADD | 0.998 | 0.000 | — |
| DIABLO-2 | 0.997 | 0.696 | — |
| CASP3 | 0.997 | 0.643 | — |
| TRAF5 | 0.997 | 0.066 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Pdpk1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Traf2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| DIABLO | psi-mi:"MI:0096"(pull down) | imex:IM-14424|pubmed:16282325 |
| SNX7 | psi-mi:"MI:0663"(confocal microscopy) | imex:IM-15364|pubmed:21988832 |
| SUMO1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| RCHY1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| CYFIP2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| CASP9 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| EBI-1562093 | psi-mi:"MI:0053"(fluorescence polarization spectro | imex:IM-11883|pubmed:18022362 |
| EBI-1562094 | psi-mi:"MI:0053"(fluorescence polarization spectro | imex:IM-11883|pubmed:18022362 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.8 + PDB: 2UVL, 3EB5, 3EB6, 3M0A, 3M0D,  | pLDDT=74.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. BIRC3 — Baculoviral IAP repeat-containing protein 3，研究基础较多，新颖性有限。
2. 蛋白大小604 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 417 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 417 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13489
- Protein Atlas: https://www.proteinatlas.org/ENSG00000023445-BIRC3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BIRC3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13489
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

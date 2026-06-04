---
type: protein-evaluation
gene: "RARG"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## RARG — REJECTED (研究热度过高 (PubMed strict=131，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RARG / NR1B3 |
| 蛋白名称 | Retinoic acid receptor gamma |
| 蛋白大小 | 454 aa / 50.3 kDa |
| UniProt ID | P13631 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 454 aa / 50.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=131 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=78.3; PDB: 1EXA, 1EXX, 1FCX, 1FCY, 1FCZ, 1FD0, 2LBD |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR035500, IPR047159, IPR047158, IPR000536, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- RNA polymerase II transcription regulator complex (GO:0090575)
- transcription regulator complex (GO:0005667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 131 |
| PubMed broad count | 351 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NR1B3 |

**关键文献**:
1. Defining a TFAP2C-centered transcription factor network during murine peri-implantation.. *Developmental cell*. PMID: 38574734
2. Critical role of tripartite fusion and LBD truncation in certain RARA- and all RARG-related atypical APL.. *Blood*. PMID: 39046762
3. Functional Validation of Doxorubicin-Induced Cardiotoxicity-Related Genes.. *JACC. CardioOncology*. PMID: 38510289
4. Pharmacogenetics of Chemotherapy-Induced Cardiotoxicity.. *Current oncology reports*. PMID: 29713898
5. RARG Gene Dysregulation in Acute Myeloid Leukemia.. *Frontiers in molecular biosciences*. PMID: 31709264

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.3 |
| 高置信度残基 (pLDDT>90) 占比 | 60.6% |
| 置信残基 (pLDDT 70-90) 占比 | 8.6% |
| 中等置信 (pLDDT 50-70) 占比 | 6.6% |
| 低置信 (pLDDT<50) 占比 | 24.2% |
| 有序区域 (pLDDT>70) 占比 | 69.2% |
| 可用 PDB 条目 | 1EXA, 1EXX, 1FCX, 1FCY, 1FCZ, 1FD0, 2LBD, 3LBD, 4LBD, 5M24 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1EXA, 1EXX, 1FCX, 1FCY, 1FCZ, 1FD0, 2LBD, 3LBD, 4LBD, 5M24）+ AlphaFold极高置信度预测（pLDDT=78.3），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR035500, IPR047159, IPR047158, IPR000536, IPR001723; Pfam: PF00104, PF00105 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RARS1 | 0.968 | 0.000 | — |
| RXRG | 0.959 | 0.345 | — |
| RARA | 0.958 | 0.780 | — |
| RXRB | 0.946 | 0.786 | — |
| RXRA | 0.945 | 0.208 | — |
| CRABP2 | 0.941 | 0.050 | — |
| RARB | 0.911 | 0.000 | — |
| SRA1 | 0.818 | 0.000 | — |
| NCOR1 | 0.776 | 0.349 | — |
| NCOR2 | 0.754 | 0.231 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MRPL12 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| SPHK1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| MTMR6 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| IL24 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| LSR | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| ZNF576 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| RHPN2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| ACY3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| OIP5 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| ZNF423 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-13591|pubmed:19345331 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.3 + PDB: 1EXA, 1EXX, 1FCX, 1FCY, 1FCZ,  | pLDDT=78.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm | 一致 |
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
1. RARG — Retinoic acid receptor gamma，研究基础较多，新颖性有限。
2. 蛋白大小454 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 131 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 131 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P13631
- Protein Atlas: https://www.proteinatlas.org/ENSG00000172819-RARG/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RARG
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P13631
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

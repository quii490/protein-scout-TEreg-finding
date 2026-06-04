---
type: protein-evaluation
gene: "CMTM5"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CMTM5 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CMTM5 / CKLFSF5 |
| 蛋白名称 | CKLF-like MARVEL transmembrane domain-containing protein 5 |
| 蛋白大小 | 223 aa / 24.7 kDa |
| UniProt ID | Q96DZ9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Golgi apparatus, Vesicles; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 223 aa / 24.7 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=32 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR008253, IPR050578; Pfam: PF01284 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **100.0/180** | |
| **归一化总分** | | | **55.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus, Vesicles | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- extracellular space (GO:0005615)
- membrane (GO:0016020)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 32 |
| PubMed broad count | 49 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CKLFSF5 |

**关键文献**:
1. [Association between CMTM5 gene and coronary artery disease and the relative mechanism].. *Beijing da xue xue bao. Yi xue ban = Journal of Peking University. Health sciences*. PMID: 33331317
2. Loss of the Novel Myelin Protein CMTM5 in Multiple Sclerosis Lesions and Its Involvement in Oligodendroglial Stress Responses.. *Cells*. PMID: 37626895
3. CMTM5 influences Hippo/YAP axis to promote ferroptosis in glioma through regulating WWP2-mediated LATS2 ubiquitination.. *The Kaohsiung journal of medical sciences*. PMID: 39166861
4. Progressive axonopathy when oligodendrocytes lack the myelin protein CMTM5.. *eLife*. PMID: 35274615
5. Bioinformatics-Based Discovery of CKLF-Like MARVEL Transmembrane Member 5 as a Novel Biomarker for Breast Cancer.. *Frontiers in cell and developmental biology*. PMID: 31998718

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.6 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 30.9% |
| 中等置信 (pLDDT 50-70) 占比 | 39.9% |
| 低置信 (pLDDT<50) 占比 | 29.1% |
| 有序区域 (pLDDT>70) 占比 | 30.9% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=59.6），有序残基占 30.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008253, IPR050578; Pfam: PF01284 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CKLF | 0.945 | 0.000 | — |
| CMTM1 | 0.849 | 0.000 | — |
| CMTM2 | 0.848 | 0.000 | — |
| CMTM4 | 0.821 | 0.000 | — |
| TREML1 | 0.798 | 0.000 | — |
| CMTM7 | 0.771 | 0.000 | — |
| CMTM8 | 0.748 | 0.000 | — |
| CMTM6 | 0.735 | 0.000 | — |
| ITGA2B | 0.575 | 0.000 | — |
| CCDC120 | 0.564 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PB2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-13585|pubmed:20064372 |
| SHMT2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:29892012|doi:10.1038/s4 |
| MYG1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| ACSF2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| GLTP | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| TUFM | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| RMDN2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| RBFA | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MRRF | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| GAD1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.6 + PDB: 无 | pLDDT=59.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Golgi apparatus, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CMTM5 — CKLF-like MARVEL transmembrane domain-containing protein 5，非常新颖，仅有少数基础研究。
2. 蛋白大小223 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 32 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=59.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96DZ9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166091-CMTM5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CMTM5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96DZ9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

---
type: protein-evaluation
gene: "EMC7"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EMC7 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EMC7 / C11orf3, C15orf24 |
| 蛋白名称 | Endoplasmic reticulum membrane protein complex subunit 7 |
| 蛋白大小 | 242 aa / 26.5 kDa |
| UniProt ID | Q9NPA0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Endoplasmic reticulum membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 242 aa / 26.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=73.0; PDB: 1B0G, 1LP9, 2J8U, 2JCC, 2UWE, 6WW7, 6Z3W |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR019008, IPR013784, IPR039163; Pfam: PF09430 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **124.0/180** | |
| **归一化总分** | | | **68.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Endoplasmic reticulum membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- EMC complex (GO:0072546)
- endoplasmic reticulum membrane (GO:0005789)
- membrane (GO:0016020)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 9 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C11orf3, C15orf24 |

**关键文献**:
1. Structure of the ER membrane complex, a transmembrane-domain insertase.. *Nature*. PMID: 32494008
2. Selective EMC subunits act as molecular tethers of intracellular organelles exploited during viral entry.. *Nature communications*. PMID: 32111841
3. Identification of genetic variants associated with clinical features of sickle cell disease.. *Scientific reports*. PMID: 39209956
4. The Orthology Clause in the Next Generation Sequencing Era: Novel Reference Genes Identified by RNA-seq in Humans Improve Normalization of Neonatal Equine Ovary RT-qPCR Data.. *PloS one*. PMID: 26536597
5. NUT Is a Specific Immunohistochemical Marker for the Diagnosis of YAP1-NUTM1-rearranged Cutaneous Poroid Neoplasms.. *The American journal of surgical pathology*. PMID: 33739783

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.0 |
| 高置信度残基 (pLDDT>90) 占比 | 40.1% |
| 置信残基 (pLDDT 70-90) 占比 | 19.4% |
| 中等置信 (pLDDT 50-70) 占比 | 15.3% |
| 低置信 (pLDDT<50) 占比 | 25.2% |
| 有序区域 (pLDDT>70) 占比 | 59.5% |
| 可用 PDB 条目 | 1B0G, 1LP9, 2J8U, 2JCC, 2UWE, 6WW7, 6Z3W, 7ADO, 8EOI, 8J0N |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1B0G, 1LP9, 2J8U, 2JCC, 2UWE, 6WW7, 6Z3W, 7ADO, 8EOI, 8J0N）+ AlphaFold极高置信度预测（pLDDT=73.0），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019008, IPR013784, IPR039163; Pfam: PF09430 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MMGT1 | 0.999 | 0.973 | — |
| EMC1 | 0.999 | 0.985 | — |
| EMC10 | 0.999 | 0.988 | — |
| EMC9 | 0.999 | 0.966 | — |
| EMC4 | 0.999 | 0.971 | — |
| EMC8 | 0.999 | 0.965 | — |
| EMC6 | 0.999 | 0.953 | — |
| EMC3 | 0.999 | 0.985 | — |
| EMC2 | 0.999 | 0.976 | — |
| C1orf43 | 0.825 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ATP13A2 | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:22645275|imex:IM-17891 |
| EMC3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PLGRKT | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| CANX | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| LAMP1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| PDIA4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| H2BC9 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| KRTAP5-2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| KLHL22 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TRDN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.0 + PDB: 1B0G, 1LP9, 2J8U, 2JCC, 2UWE,  | pLDDT=73.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. EMC7 — Endoplasmic reticulum membrane protein complex subunit 7，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小242 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NPA0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000134153-EMC7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EMC7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NPA0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

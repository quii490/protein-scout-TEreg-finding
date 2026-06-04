---
type: protein-evaluation
gene: "KCTD20"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KCTD20 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KCTD20 / C6orf69 |
| 蛋白名称 | BTB/POZ domain-containing protein KCTD20 |
| 蛋白大小 | 419 aa / 47.5 kDa |
| UniProt ID | Q7Z5Y7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Endoplasmic reticulum; 额外: Nuclear speckles; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 419 aa / 47.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=70.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000210, IPR039886, IPR039885, IPR011333; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 14 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.5/180** | |
| **归一化总分** | | | **67.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum; 额外: Nuclear speckles | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 11 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C6orf69 |

**关键文献**:
1. Cocaine'omics: Genome-wide and transcriptome-wide analyses provide biological insight into cocaine use and dependence.. *Addiction biology*. PMID: 30734435
2. Long non‑coding RNA NEAT1 regulates glioma cell proliferation and apoptosis by competitively binding to microRNA‑324‑5p and upregulating KCTD20 expression.. *Oncology reports*. PMID: 33982764
3. Kctd20 promotes the development of non-small cell lung cancer through activating Fak/AKT pathway and predicts poor overall survival of patients.. *Molecular carcinogenesis*. PMID: 28398603
4. Genome-wide analyses in Lyme borreliosis: identification of a genetic variant associated with disease susceptibility and its immunological implications.. *BMC infectious diseases*. PMID: 38515037
5. A genome-wide association scan for acute insulin response to glucose in Hispanic-Americans: the Insulin Resistance Atherosclerosis Family Study (IRAS FS).. *Diabetologia*. PMID: 19430760

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.5 |
| 高置信度残基 (pLDDT>90) 占比 | 43.7% |
| 置信残基 (pLDDT 70-90) 占比 | 11.9% |
| 中等置信 (pLDDT 50-70) 占比 | 9.1% |
| 低置信 (pLDDT<50) 占比 | 35.3% |
| 有序区域 (pLDDT>70) 占比 | 55.6% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=70.5，有序区 55.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000210, IPR039886, IPR039885, IPR011333; Pfam: PF16017 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KCTD10 | 0.700 | 0.000 | — |
| KCTD19 | 0.643 | 0.000 | — |
| KCTD18 | 0.608 | 0.000 | — |
| CUL3 | 0.578 | 0.476 | — |
| KCTD5 | 0.575 | 0.000 | — |
| KCTD1 | 0.540 | 0.000 | — |
| KCTD8 | 0.538 | 0.000 | — |
| KCTD12 | 0.538 | 0.000 | — |
| KCTD11 | 0.533 | 0.000 | — |
| KCTD3 | 0.528 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MARK4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:14676191 |
| PPP1CA | psi-mi:"MI:0018"(two hybrid) | imex:IM-16965|pubmed:22321011 |
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| PPP1CC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| BUB3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| COPS7A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |
| SOX13 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| DUSP16 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ENST00000373731 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 14
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 14 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.5 + PDB: 无 | pLDDT=70.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Endoplasmic reticulum; 额外: Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 15 + 14 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. KCTD20 — BTB/POZ domain-containing protein KCTD20，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小419 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z5Y7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000112078-KCTD20/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KCTD20
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7Z5Y7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

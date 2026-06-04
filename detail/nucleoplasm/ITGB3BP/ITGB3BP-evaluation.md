---
type: protein-evaluation
gene: "ITGB3BP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ITGB3BP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ITGB3BP / CENPR, NRIF3 |
| 蛋白名称 | Centromere protein R |
| 蛋白大小 | 177 aa / 20.2 kDa |
| UniProt ID | Q13352 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Chromosome, centromere; Chromosome, centromere, kin |
| 蛋白大小 | 8/10 | ×1 | 8 | 177 aa / 20.2 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=21 篇 (≤40→8) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=72.4; PDB: 7PB8, 7PKN, 7QOO, 7R5S, 7R5V, 7XHN, 7XHO |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR009601; Pfam: PF06729 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **132.0/180** | |
| **归一化总分** | | | **73.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Chromosome, centromere; Chromosome, centromere, kinetochore; Nucleus; Nucleus; Cytoplasm; C... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- inner kinetochore (GO:0000939)
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 21 |
| PubMed broad count | 52 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CENPR, NRIF3 |

**关键文献**:
1. Identification of genes in hepatocellular carcinoma induced by non-alcoholic fatty liver disease.. *Cancer biomarkers : section A of Disease markers*. PMID: 32623384
2. ITGB3BP is a potential biomarker associated with poor prognosis of glioma.. *Journal of cellular and molecular medicine*. PMID: 34953037
3. LncRNA NR_045147 modulates osteogenic differentiation and migration in PDLSCs via ITGB3BP degradation and mitochondrial dysfunction.. *Stem cells translational medicine*. PMID: 39674578
4. Integrated profiling identifies ITGB3BP as prognostic biomarker for hepatocellular carcinoma.. *Bosnian journal of basic medical sciences*. PMID: 33974527
5. Fam208a orchestrates interaction protein network essential for early embryonic development and cell division.. *Experimental cell research*. PMID: 31112734

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.4 |
| 高置信度残基 (pLDDT>90) 占比 | 22.6% |
| 置信残基 (pLDDT 70-90) 占比 | 30.5% |
| 中等置信 (pLDDT 50-70) 占比 | 37.3% |
| 低置信 (pLDDT<50) 占比 | 9.6% |
| 有序区域 (pLDDT>70) 占比 | 53.1% |
| 可用 PDB 条目 | 7PB8, 7PKN, 7QOO, 7R5S, 7R5V, 7XHN, 7XHO, 7YWX, 7YYH |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（7PB8, 7PKN, 7QOO, 7R5S, 7R5V, 7XHN, 7XHO, 7YWX, 7YYH）+ AlphaFold极高置信度预测（pLDDT=72.4），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009601; Pfam: PF06729 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CENPQ | 0.999 | 0.984 | — |
| CENPP | 0.999 | 0.987 | — |
| CENPO | 0.999 | 0.986 | — |
| CENPU | 0.999 | 0.984 | — |
| CENPI | 0.998 | 0.918 | — |
| CENPL | 0.998 | 0.800 | — |
| CENPK | 0.998 | 0.882 | — |
| CENPT | 0.997 | 0.918 | — |
| CENPN | 0.997 | 0.918 | — |
| CENPH | 0.997 | 0.838 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CERT1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ARFIP2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ALDH2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CEP126 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PSME1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ACTG1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ENOX1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| GIT1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| HIP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| POLA2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.4 + PDB: 7PB8, 7PKN, 7QOO, 7R5S, 7R5V,  | pLDDT=72.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome, centromere; Chromosome, centr / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. ITGB3BP — Centromere protein R，非常新颖，仅有少数基础研究。
2. 蛋白大小177 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 21 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13352
- Protein Atlas: https://www.proteinatlas.org/ENSG00000142856-ITGB3BP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ITGB3BP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13352
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

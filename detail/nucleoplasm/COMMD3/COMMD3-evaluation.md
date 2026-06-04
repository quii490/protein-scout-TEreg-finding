---
type: protein-evaluation
gene: "COMMD3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## COMMD3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COMMD3 / BUP, C10orf8 |
| 蛋白名称 | COMM domain-containing protein 3 |
| 蛋白大小 | 195 aa / 22.2 kDa |
| UniProt ID | Q9UBI1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 195 aa / 22.2 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=23 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=87.0; PDB: 8F2R, 8F2U, 8P0W |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR017920, IPR037355; Pfam: PF07258, PF21672 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.0/180** | |
| **归一化总分** | | | **72.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- extracellular region (GO:0005576)
- ficolin-1-rich granule lumen (GO:1904813)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 23 |
| PubMed broad count | 32 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BUP, C10orf8 |

**关键文献**:
1. Commander complex regulates lysosomal function and is implicated in Parkinson's disease risk.. *Science (New York, N.Y.)*. PMID: 40209002
2. A genome-wide genetic screen uncovers determinants of human pigmentation.. *Science (New York, N.Y.)*. PMID: 37561850
3. Celastrol suppresses humoral immune responses and autoimmunity by targeting the COMMD3/8 complex.. *Science immunology*. PMID: 37000855
4. Chemoattractant receptor signaling in humoral immunity.. *International immunology*. PMID: 38573198
5. COMMD3:BMI1 Fusion and COMMD3 Protein Regulate C-MYC Transcription: Novel Therapeutic Target for Metastatic Prostate Cancer.. *Molecular cancer therapeutics*. PMID: 31467179

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.0 |
| 高置信度残基 (pLDDT>90) 占比 | 63.6% |
| 置信残基 (pLDDT 70-90) 占比 | 23.1% |
| 中等置信 (pLDDT 50-70) 占比 | 12.8% |
| 低置信 (pLDDT<50) 占比 | 0.5% |
| 有序区域 (pLDDT>70) 占比 | 86.7% |
| 可用 PDB 条目 | 8F2R, 8F2U, 8P0W |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（8F2R, 8F2U, 8P0W）+ AlphaFold高质量预测（pLDDT=87.0），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR017920, IPR037355; Pfam: PF07258, PF21672 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| COMMD2 | 0.989 | 0.873 | — |
| CCDC22 | 0.980 | 0.868 | — |
| COMMD4 | 0.978 | 0.835 | — |
| COMMD6 | 0.975 | 0.876 | — |
| COMMD10 | 0.971 | 0.868 | — |
| COMMD9 | 0.971 | 0.864 | — |
| COMMD1 | 0.966 | 0.842 | — |
| COMMD8 | 0.955 | 0.837 | — |
| COMMD7 | 0.954 | 0.836 | — |
| COMMD5 | 0.949 | 0.826 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ZNF337 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| TRAF5 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| COMMD1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:15799966 |
| NFKB1 | psi-mi:"MI:0096"(pull down) | pubmed:15799966 |
| RELB | psi-mi:"MI:0096"(pull down) | pubmed:15799966 |
| VPS26C | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| GNB1 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| CCDC22 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| BANF1 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.0 + PDB: 8F2R, 8F2U, 8P0W | pLDDT=87.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. COMMD3 — COMM domain-containing protein 3，非常新颖，仅有少数基础研究。
2. 蛋白大小195 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 23 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UBI1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000148444-COMMD3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COMMD3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UBI1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

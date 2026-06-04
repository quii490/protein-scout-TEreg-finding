---
type: protein-evaluation
gene: "MPHOSPH6"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MPHOSPH6 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MPHOSPH6 / MPP6 |
| 蛋白名称 | M-phase phosphoprotein 6 |
| 蛋白大小 | 160 aa / 19.0 kDa |
| UniProt ID | Q99547 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli; UniProt: Nucleus, nucleolus; Cytoplasm |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 160 aa / 19.0 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=18 篇 (≤20→10) |
| 🏗️ 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=76.4; PDB: 6D6Q, 6D6R, 6H25 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR019324; Pfam: PF10175 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **139.0/180** | |
| **归一化总分** | | | **77.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli | Supported |
| UniProt | Nucleus, nucleolus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**GO Cellular Component**:
- cytosol (GO:0005829)
- exosome (RNase complex) (GO:0000178)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 22 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MPP6 |

**关键文献**:
1. A novel lactylation-related gene signature for effectively distinguishing and predicting the prognosis of ovarian cancer.. *Translational cancer research*. PMID: 38881917
2. Novel ribosome biogenesis-related biomarkers and therapeutic targets identified in psoriasis.. *Scientific reports*. PMID: 40425712
3. Unveiling novel potential drug targets for lung cancer through Mendelian randomization analysis.. *Scientific reports*. PMID: 41436647
4. Association between MPHOSPH6 gene polymorphisms and IgA nephropathy risk in a Chinese Han population.. *Oncotarget*. PMID: 29069794
5. Multi-omics identify ribosome related causal genes methylation, splicing, and expression in prostate cancer.. *Discover oncology*. PMID: 40354008

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.4 |
| 高置信度残基 (pLDDT>90) 占比 | 7.5% |
| 置信残基 (pLDDT 70-90) 占比 | 65.0% |
| 中等置信 (pLDDT 50-70) 占比 | 26.2% |
| 低置信 (pLDDT<50) 占比 | 1.2% |
| 有序区域 (pLDDT>70) 占比 | 72.5% |
| 可用 PDB 条目 | 6D6Q, 6D6R, 6H25 |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: PDB实验结构（6D6Q, 6D6R, 6H25）+ AlphaFold高质量预测（pLDDT=76.4），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019324; Pfam: PF10175 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EXOSC4 | 0.999 | 0.974 | — |
| EXOSC7 | 0.999 | 0.980 | — |
| EXOSC8 | 0.999 | 0.979 | — |
| EXOSC5 | 0.999 | 0.972 | — |
| EXOSC6 | 0.999 | 0.965 | — |
| EXOSC1 | 0.999 | 0.988 | — |
| EXOSC3 | 0.999 | 0.991 | — |
| EXOSC10 | 0.998 | 0.972 | — |
| EXOSC9 | 0.998 | 0.973 | — |
| EXOSC2 | 0.998 | 0.974 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MTREX | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| PARN | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| EXOSC10 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| TLE1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| TP53 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| RIF1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| UNC119 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ZHX1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ERG28 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| HSPB1 | psi-mi:"MI:0097"(reverse ras recruitment system) | imex:IM-20864|pubmed:25277244 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.4 + PDB: 6D6Q, 6D6R, 6H25 | pLDDT=76.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleolus; Cytoplasm / Nucleoplasm, Nucleoli | 一致 |
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
1. MPHOSPH6 — M-phase phosphoprotein 6，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小160 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q99547
- Protein Atlas: https://www.proteinatlas.org/ENSG00000135698-MPHOSPH6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MPHOSPH6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99547
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 21:54:41

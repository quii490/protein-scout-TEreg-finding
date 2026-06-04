---
type: protein-evaluation
gene: "RB1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## RB1 — REJECTED (研究热度过高 (PubMed strict=4117，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RB1 |
| 蛋白名称 | Retinoblastoma-associated protein |
| 蛋白大小 | 928 aa / 106.2 kDa |
| UniProt ID | P06400 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Primary cilium transition zone; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 928 aa / 106.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=4117 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=76.1; PDB: 1AD6, 1GH6, 1GUX, 1H25, 1N4M, 1O9K, 1PJM |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR013763, IPR036915, IPR002720, IPR002719, IPR015 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **92.0/180** | |
| **归一化总分** | | | **51.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Primary cilium transition zone | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- chromatin lock complex (GO:0061793)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- PML body (GO:0016605)
- Rb-E2F complex (GO:0035189)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4117 |
| PubMed broad count | 7972 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Retinoblastoma.. *Nature reviews. Disease primers*. PMID: 27189421
2. RB1-deficient prostate tumor growth and metastasis are vulnerable to ferroptosis induction via the E2F/ACSL4 axis.. *The Journal of clinical investigation*. PMID: 36928314
3. Ginsenoside Rb1 reduces H2O2‑induced HUVEC dysfunction by stimulating the sirtuin‑1/AMP‑activated protein kinase pathway.. *Molecular medicine reports*. PMID: 32377712
4. The Biology of Retinoblastoma.. *Progress in molecular biology and translational science*. PMID: 26310174
5. Novel insights into RB1 mutation.. *Cancer letters*. PMID: 35964818

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.1 |
| 高置信度残基 (pLDDT>90) 占比 | 50.3% |
| 置信残基 (pLDDT 70-90) 占比 | 13.9% |
| 中等置信 (pLDDT 50-70) 占比 | 14.2% |
| 低置信 (pLDDT<50) 占比 | 21.6% |
| 有序区域 (pLDDT>70) 占比 | 64.2% |
| 可用 PDB 条目 | 1AD6, 1GH6, 1GUX, 1H25, 1N4M, 1O9K, 1PJM, 2AZE, 2QDJ, 2R7G |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1AD6, 1GH6, 1GUX, 1H25, 1N4M, 1O9K, 1PJM, 2AZE, 2QDJ, 2R7G）+ AlphaFold极高置信度预测（pLDDT=76.1），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013763, IPR036915, IPR002720, IPR002719, IPR015030; Pfam: PF11934, PF01858, PF01857 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| E2F1 | 0.999 | 0.999 | — |
| E2F2 | 0.999 | 0.990 | — |
| MDM2 | 0.999 | 0.889 | — |
| E2F4 | 0.999 | 0.921 | — |
| CDK2 | 0.999 | 0.991 | — |
| TFDP1 | 0.999 | 0.985 | — |
| HDAC1 | 0.999 | 0.987 | — |
| CDK4 | 0.999 | 0.994 | — |
| CCNA2 | 0.998 | 0.847 | — |
| CCND1 | 0.998 | 0.932 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| A8K5E3 | psi-mi:"MI:0096"(pull down) | pubmed:16360038|imex:IM-20931 |
| TAF1 | psi-mi:"MI:0096"(pull down) | pubmed:9858607 |
| CDK2 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:8756624 |
| E7 | psi-mi:"MI:0096"(pull down) | imex:IM-14542|pubmed:16249186| |
| E2F1 | psi-mi:"MI:0096"(pull down) | imex:IM-14542|pubmed:16249186| |
| E1A | psi-mi:"MI:0096"(pull down) | imex:IM-14542|pubmed:16249186| |
| DGKZ | psi-mi:"MI:0019"(coimmunoprecipitation) | imex:IM-14473|pubmed:16286473 |
| - | psi-mi:"MI:0096"(pull down) | imex:IM-14473|pubmed:16286473 |
| Hmga2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-11861|pubmed:16766265 |
| HDAC1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-11861|pubmed:16766265 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.1 + PDB: 1AD6, 1GH6, 1GUX, 1H25, 1N4M,  | pLDDT=76.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm; 额外: Primary cilium transition zone | 一致 |
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
1. RB1 — Retinoblastoma-associated protein，研究基础较多，新颖性有限。
2. 蛋白大小928 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 4117 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 4117 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P06400
- Protein Atlas: https://www.proteinatlas.org/ENSG00000139687-RB1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RB1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P06400
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

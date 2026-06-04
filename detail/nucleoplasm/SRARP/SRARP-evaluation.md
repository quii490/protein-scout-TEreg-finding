---
type: protein-evaluation
gene: "SRARP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SRARP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SRARP / C1orf64, ERRF, SSPR |
| 蛋白名称 | Steroid receptor-associated and regulated protein |
| 蛋白大小 | 169 aa / 17.7 kDa |
| UniProt ID | Q8NEQ6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 169 aa / 17.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=51.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR027852; Pfam: PF15547 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 2 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **127.5/180** | |
| **归一化总分** | | | **70.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 60 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C1orf64, ERRF, SSPR |

**关键文献**:
1. Role of steroid receptor-associated and regulated protein in tumor progression and progesterone receptor signaling in endometrial cancer.. *Chinese medical journal*. PMID: 37144734
2. Distinct Immune Landscape and Gene Expression Profiles in Breast Cancer: Young versus Non-Young Patients.. *Breast care (Basel, Switzerland)*. PMID: 41063765
3. Genomic and epigenetic aberrations of chromosome 1p36.13 have prognostic implications in malignancies.. *Chromosome research : an international journal on the molecular, supramolecular and evolutionary aspects of chromosome biology*. PMID: 32816122
4. SRARP and HSPB7 are epigenetically regulated gene pairs that function as tumor suppressors and predict clinical outcome in malignancies.. *Molecular oncology*. PMID: 29577611
5. Steroid receptor-associated and regulated protein is a biomarker in predicting the clinical outcome and treatment response in malignancies.. *Cancer reports (Hoboken, N.J.)*. PMID: 32706923

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 51.8 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 9.5% |
| 中等置信 (pLDDT 50-70) 占比 | 43.8% |
| 低置信 (pLDDT<50) 占比 | 46.7% |
| 有序区域 (pLDDT>70) 占比 | 9.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=51.8），有序残基占 9.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027852; Pfam: PF15547 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ABCC11 | 0.500 | 0.000 | — |
| F11R | 0.405 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 2，IntAct interactions: 0
- 调控相关比例: 0 / 2 = 0%

**评价**: STRING 2 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=51.8 + PDB: 无 | pLDDT=51.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 2 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SRARP — Steroid receptor-associated and regulated protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小169 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=51.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NEQ6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000183888-SRARP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SRARP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NEQ6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

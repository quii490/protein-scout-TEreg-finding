---
type: protein-evaluation
gene: "DTNBP1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DTNBP1 — REJECTED (核定位证据不足 (核定位得分 3/10 ≤ 3); 研究热度过高 (PubMed strict=320，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DTNBP1 |
| 蛋白名称 | Dysbindin |
| 蛋白大小 | 351 aa / 39.5 kDa |
| UniProt ID | Q96EV8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 3/10 | ×4 | 12 | HPA: Microtubules; 额外: Midbody; UniProt: Cytoplasm; Cytoplasmic vesicle membrane; Endosome membrane;  |
| 蛋白大小 | 10/10 | ×1 | 10 | 351 aa / 39.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=320 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=74.9; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **65.5/180** | |
| **归一化总分** | | | **36.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Microtubules; 额外: Midbody | Enhanced |
| UniProt | Cytoplasm; Cytoplasmic vesicle membrane; Endosome membrane; Melanosome membrane; Postsynaptic densit... | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据不足，HPA与UniProt存在矛盾或缺乏核注释。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 320 |
| PubMed broad count | 424 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Genetic insights into bovine spastic syndrome (Crampy) in Holstein dairy cattle.. *J Dairy Sci*. PMID: 41076258
2. Characterization of the expression and function of schizophrenia risk gene Dtnbp1 in the suprachiasmatic nucleus.. *Neuroscience*. PMID: 41391739
3. Research on the correlation of nitric oxide-induced neuronal cell pyroptosis with schizophrenia and its cognitive impairment.. *BMC Psychiatry*. PMID: 41029255
4. Beyond vertebrates: Drosophila melanogaster as a model to study negative symptoms of schizophrenia.. *Front Psychiatry*. PMID: 40778327
5. DNA methylation and histone modifications associated with antipsychotic treatment: a systematic review.. *Mol Psychiatry*. PMID: 39227433

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.9 |
| 高置信度残基 (pLDDT>90) 占比 | 42.7% |
| 置信残基 (pLDDT 70-90) 占比 | 14.0% |
| 中等置信 (pLDDT 50-70) 占比 | 19.9% |
| 低置信 (pLDDT<50) 占比 | 23.4% |
| 有序区域 (pLDDT>70) 占比 | 56.7% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 中等质量（pLDDT=74.9，有序区 56.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BLOC1S6 | 0.000 | 0.000 | — |
| BLOC1S1 | 0.000 | 0.000 | — |
| SNAPIN | 0.000 | 0.000 | — |
| BLOC1S2 | 0.000 | 0.000 | — |
| BLOC1S3 | 0.000 | 0.000 | — |
| BLOC1S5 | 0.000 | 0.000 | — |
| BLOC1S4 | 0.000 | 0.000 | — |
| HPS5 | 0.000 | 0.000 | — |
| HPS6 | 0.000 | 0.000 | — |
| HPS3 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q91WZ8-1 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q96EV8 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:O95295 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:P78537 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9UL45 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q6QNY0 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q6QNY1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q8TDH9 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9BY27 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.9 + PDB: 无 | pLDDT=74.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasmic vesicle membrane; Endosome  / Microtubules; 额外: Midbody | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DTNBP1 — Dysbindin，研究基础较多，新颖性有限。
2. 蛋白大小351 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 320 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96EV8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000047579-DTNBP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DTNBP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96EV8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

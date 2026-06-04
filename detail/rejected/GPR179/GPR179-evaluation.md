---
type: protein-evaluation
gene: "GPR179"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GPR179 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPR179 / GPR158L, GPR158L1 |
| 蛋白名称 | Probable G-protein coupled receptor 179 |
| 蛋白大小 | 2367 aa / 257.4 kDa |
| UniProt ID | Q6PRD1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane; Postsynaptic cell membrane; Cell projection,  |
| 蛋白大小 | 2/10 | ×1 | 2 | 2367 aa / 257.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=34 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=42.8; PDB: 8D1B, 8IRJ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR017978, IPR043458, IPR054714; Pfam: PF00003, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **92.5/180** | |
| **归一化总分** | | | **51.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell membrane; Postsynaptic cell membrane; Cell projection, dendrite | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- dendrite (GO:0030425)
- dendrite terminus (GO:0044292)
- postsynaptic membrane (GO:0045211)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 34 |
| PubMed broad count | 55 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GPR158L, GPR158L1 |

**关键文献**:
1. In vitro profiling of orphan G protein coupled receptor (GPCR) constitutive activity.. *British journal of pharmacology*. PMID: 33784795
2. Homodimerization of a proximal region within the C-terminus of the orphan G-protein coupled receptor GPR179.. *Neurochemistry international*. PMID: 34333057
3. Ultrastructural localization of GPR179 and the impact of mutant forms on retinal function in CSNB1 patients and a mouse model.. *Investigative ophthalmology & visual science*. PMID: 24084093
4. GPR179 is required for high sensitivity of the mGluR6 signaling cascade in depolarizing bipolar cells.. *The Journal of neuroscience : the official journal of the Society for Neuroscience*. PMID: 24790204
5. Whole-Exome Sequencing Indicated New Candidate Genes Associated with Unilateral Cryptorchidism in Pigs.. *Sexual development : genetics, molecular biology, evolution, endocrinology, embryology, and pathology of sex determination and differentiation*. PMID: 36758533

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 42.8 |
| 高置信度残基 (pLDDT>90) 占比 | 4.9% |
| 置信残基 (pLDDT 70-90) 占比 | 15.5% |
| 中等置信 (pLDDT 50-70) 占比 | 5.2% |
| 低置信 (pLDDT<50) 占比 | 74.4% |
| 有序区域 (pLDDT>70) 占比 | 20.4% |
| 可用 PDB 条目 | 8D1B, 8IRJ |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=42.8），有序残基占 20.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR017978, IPR043458, IPR054714; Pfam: PF00003, PF22572 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NYX | 0.818 | 0.000 | — |
| LRIT3 | 0.773 | 0.000 | — |
| CABP4 | 0.730 | 0.153 | — |
| EGFLAM | 0.725 | 0.292 | — |
| GRM6 | 0.713 | 0.000 | — |
| TRPM1 | 0.680 | 0.000 | — |
| RGS7 | 0.676 | 0.000 | — |
| RGS11 | 0.668 | 0.000 | — |
| CACNA1F | 0.604 | 0.000 | — |
| WDR90 | 0.577 | 0.577 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HIST2H2BF | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| CTBP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31041561|imex:IM-29110 |
| P | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:unassigned2293|imex:IM- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 3
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=42.8 + PDB: 8D1B, 8IRJ | pLDDT=42.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane; Postsynaptic cell membrane; Cell pr / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 3 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GPR179 — Probable G-protein coupled receptor 179，非常新颖，仅有少数基础研究。
2. 蛋白大小2367 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 34 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=42.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6PRD1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000277399-GPR179/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPR179
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6PRD1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

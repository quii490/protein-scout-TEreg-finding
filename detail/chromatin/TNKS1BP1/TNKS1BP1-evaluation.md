---
type: protein-evaluation
gene: "TNKS1BP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TNKS1BP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TNKS1BP1 / KIAA1741, TAB182 |
| 蛋白名称 | 182 kDa tankyrase-1-binding protein |
| 蛋白大小 | 1729 aa / 181.8 kDa |
| UniProt ID | Q9C0C2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane; UniProt: Nucleus; Cytoplasm, cytoskeleton; Chromosome |
| 蛋白大小 | 5/10 | ×1 | 5 | 1729 aa / 181.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v6 pLDDT=38.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR032764, IPR040006; Pfam: PF15327 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119.0/180** | |
| **归一化总分** | | | **66.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane | Approved |
| UniProt | Nucleus; Cytoplasm, cytoskeleton; Chromosome | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- adherens junction (GO:0005912)
- CCR4-NOT complex (GO:0030014)
- cytoplasm (GO:0005737)
- cytoskeleton (GO:0005856)
- cytosol (GO:0005829)
- heterochromatin (GO:0000792)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 28 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1741, TAB182 |

**关键文献**:
1. TNKS1BP1 facilitates ubiquitination of CNOT4 by TRIM21 to promote hepatocellular carcinoma progression and immune evasion.. *Cell death & disease*. PMID: 39019859
2. Tankyrase-Binding Protein TNKS1BP1 Regulates Actin Cytoskeleton Rearrangement and Cancer Cell Invasion.. *Cancer research*. PMID: 28202517
3. Ocular Mucous Membrane Pemphigoid Demonstrates a Distinct Autoantibody Profile from Those of Other Autoimmune Blistering Diseases: A Preliminary Study.. *Antibodies (Basel, Switzerland)*. PMID: 39584991
4. Rare protein-coding variants implicate genes involved in risk of suicide death.. *American journal of medical genetics. Part B, Neuropsychiatric genetics : the official publication of the International Society of Psychiatric Genetics*. PMID: 34042246
5. Effects of Helicobacter pylori Infection on the Development of Chronic Gastritis.. *The Turkish journal of gastroenterology : the official journal of Turkish Society of Gastroenterology*. PMID: 37249580

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 38.2 |
| 高置信度残基 (pLDDT>90) 占比 | 0.3% |
| 置信残基 (pLDDT 70-90) 占比 | 1.7% |
| 中等置信 (pLDDT 50-70) 占比 | 6.8% |
| 低置信 (pLDDT<50) 占比 | 91.2% |
| 有序区域 (pLDDT>70) 占比 | 2.0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=38.2），有序残基占 2.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR032764, IPR040006; Pfam: PF15327 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CNOT11 | 0.994 | 0.828 | — |
| CNOT7 | 0.994 | 0.873 | — |
| TNKS | 0.991 | 0.512 | — |
| CNOT6L | 0.991 | 0.806 | — |
| CNOT10 | 0.990 | 0.694 | — |
| CNOT3 | 0.989 | 0.690 | — |
| CNOT2 | 0.988 | 0.706 | — |
| CNOT9 | 0.986 | 0.421 | — |
| CNOT1 | 0.985 | 0.620 | — |
| TOB1 | 0.977 | 0.780 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TNKS2 | psi-mi:"MI:0053"(fluorescence polarization spectro | pubmed:22153077|imex:IM-16612 |
| CSNK2A1 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:22113938|imex:IM-16640 |
| Capza1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Cnot3 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Rc3h1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:23663784|imex:IM-21399 |
| Rc3h2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:23663784|imex:IM-21399 |
| NLK | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |
| EZR | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| STK38L | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-26463|pubmed:30108113 |
| ANXA2R | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=38.2 + PDB: 无 | pLDDT=38.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, cytoskeleton; Chromosome / Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TNKS1BP1 — 182 kDa tankyrase-1-binding protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1729 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=38.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9C0C2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000149115-TNKS1BP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TNKS1BP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9C0C2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

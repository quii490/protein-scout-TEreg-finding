---
type: protein-evaluation
gene: "TOGARAM1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TOGARAM1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TOGARAM1 / FAM179B, KIAA0423 |
| 蛋白名称 | TOG array regulator of axonemal microtubules protein 1 |
| 蛋白大小 | 1720 aa / 189.4 kDa |
| UniProt ID | Q9Y4F4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nuclear speckles, Microtubules; 额外: Primary cilium; UniProt: Cell projection, cilium; Cytoplasm, cytoskeleton; Cytoplasm, |
| 蛋白大小 | 5/10 | ×1 | 5 | 1720 aa / 189.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011989, IPR016024, IPR034085; Pfam: PF21040 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.0/180** | |
| **归一化总分** | | | **62.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles, Microtubules; 额外: Primary cilium | Uncertain |
| UniProt | Cell projection, cilium; Cytoplasm, cytoskeleton; Cytoplasm, cytoskeleton, cilium axoneme | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- axoneme (GO:0005930)
- ciliary basal body (GO:0036064)
- cilium (GO:0005929)
- cytoplasmic microtubule (GO:0005881)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 9 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FAM179B, KIAA0423 |

**关键文献**:
1. Dysfunction of the ciliary ARMC9/TOGARAM1 protein module causes Joubert syndrome.. *The Journal of clinical investigation*. PMID: 32453716
2. A network of interacting ciliary tip proteins with opposing activities imparts slow and processive microtubule growth.. *Nature structural & molecular biology*. PMID: 39856351
3. A methylation-driven gene panel predicts survival in patients with colon cancer.. *FEBS open bio*. PMID: 34184409
4. Biallelic mutations in the TOGARAM1 gene cause a novel primary ciliopathy.. *Journal of medical genetics*. PMID: 32747439
5. Microtubule binding protein Togaram1 is required for proper development of mammalian forebrain and neural primary cilia.. *bioRxiv : the preprint server for biology*. PMID: 42039575

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.6 |
| 高置信度残基 (pLDDT>90) 占比 | 29.4% |
| 置信残基 (pLDDT 70-90) 占比 | 19.5% |
| 中等置信 (pLDDT 50-70) 占比 | 6.6% |
| 低置信 (pLDDT<50) 占比 | 44.5% |
| 有序区域 (pLDDT>70) 占比 | 48.9% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=61.6），有序残基占 48.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR034085; Pfam: PF21040 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ARMC9 | 0.662 | 0.000 | — |
| TMEM260 | 0.619 | 0.000 | — |
| PRR35 | 0.611 | 0.000 | — |
| CEP104 | 0.590 | 0.138 | — |
| PRPF39 | 0.587 | 0.000 | — |
| KBTBD12 | 0.557 | 0.000 | — |
| KLHL28 | 0.534 | 0.000 | — |
| RRP36 | 0.526 | 0.000 | — |
| CKAP5 | 0.526 | 0.000 | — |
| GOLGA7 | 0.514 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Tnf | psi-mi:"MI:0096"(pull down) | imex:IM-12051|pubmed:17623297 |
| ESR2 | psi-mi:"MI:0004"(affinity chromatography technolog | imex:IM-13781|pubmed:21182203 |
| H2BC21 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| PRKCSH | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| HTT | psi-mi:"MI:0018"(two hybrid) | pubmed:17500595|imex:IM-21753 |
| CEP104 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| ATG16L1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31015422|imex:IM-29997 |
| ARMC9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:38949024|imex:IM-30084 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 9
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.6 + PDB: 无 | pLDDT=61.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell projection, cilium; Cytoplasm, cytoskeleton;  / Nuclear speckles, Microtubules; 额外: Primary cilium | 一致 |
| PPI | STRING + IntAct | 15 + 9 interactions | 数据充分 |

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
1. TOGARAM1 — TOG array regulator of axonemal microtubules protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1720 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=61.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y4F4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198718-TOGARAM1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TOGARAM1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y4F4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

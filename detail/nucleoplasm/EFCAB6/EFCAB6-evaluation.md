---
type: protein-evaluation
gene: "EFCAB6"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EFCAB6 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EFCAB6 / DJBP, KIAA1672 |
| 蛋白名称 | EF-hand calcium-binding domain-containing protein 6 |
| 蛋白大小 | 1501 aa / 172.9 kDa |
| UniProt ID | Q5THR3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Mid piece, Principal piece; UniProt: Nucleus; Cytoplasm, cytoskeleton, flagellum axoneme |
| 蛋白大小 | 5/10 | ×1 | 5 | 1501 aa / 172.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.9; PDB: 1WLZ, 5D67 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011992, IPR018247, IPR015070, IPR002048, IPR052 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **125.5/180** | |
| **归一化总分** | | | **69.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Mid piece, Principal piece | Supported |
| UniProt | Nucleus; Cytoplasm, cytoskeleton, flagellum axoneme | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- axonemal A tubule inner sheath (GO:0160111)
- nucleoplasm (GO:0005654)
- sperm flagellum (GO:0036126)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 14 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DJBP, KIAA1672 |

**关键文献**:
1. Distinct Mechanisms of Pathogenic DJ-1 Mutations in Mitochondrial Quality Control.. *Frontiers in molecular neuroscience*. PMID: 29599708
2. Identification of a HMGA2-EFCAB6 gene rearrangement following next-generation sequencing in a patient with a t(12;22)(q14.3;q13.2) and JAK2V617F-positive myeloproliferative neoplasm.. *Cancer genetics*. PMID: 22749035
3. Cytogenetic and molecular diagnosis of Fanconi anemia revealed two hidden phenotypes: Disorder of sex development and cerebro-oculo-facio-skeletal syndrome.. *Molecular genetics & genomic medicine*. PMID: 31124294
4. Fetal-adult cardiac transcriptome analysis in rats with contrasting left ventricular mass reveals new candidates for cardiac hypertrophy.. *PloS one*. PMID: 25646840
5. Genome-Wide Association Study of Osteoporosis Risk in Korean Pre-Menopausal Women: The Korean Genome and Epidemiology Study.. *International journal of molecular sciences*. PMID: 40943102

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.9 |
| 高置信度残基 (pLDDT>90) 占比 | 1.5% |
| 置信残基 (pLDDT 70-90) 占比 | 64.3% |
| 中等置信 (pLDDT 50-70) 占比 | 11.0% |
| 低置信 (pLDDT<50) 占比 | 23.2% |
| 有序区域 (pLDDT>70) 占比 | 65.8% |
| 可用 PDB 条目 | 1WLZ, 5D67 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=68.9），有序残基占 65.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011992, IPR018247, IPR015070, IPR002048, IPR052603; Pfam: PF08976, PF13499, PF13833 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PARK7 | 0.934 | 0.294 | — |
| C19orf71 | 0.790 | 0.507 | — |
| DNAI1 | 0.733 | 0.133 | — |
| TEKT2 | 0.723 | 0.507 | — |
| EFHC2 | 0.714 | 0.507 | — |
| AR | 0.712 | 0.294 | — |
| TEKT3 | 0.688 | 0.507 | — |
| RIBC2 | 0.682 | 0.507 | — |
| TEKT1 | 0.680 | 0.507 | — |
| SPAG17 | 0.674 | 0.136 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GOLGA2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 1
- 调控相关比例: 2 / 15 = 13%

**评价**: STRING 15 个预测互作，IntAct 1 个实验互作。调控相关配体占比 13%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.9 + PDB: 1WLZ, 5D67 | pLDDT=68.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, cytoskeleton, flagellum axonem / Nucleoplasm; 额外: Mid piece, Principal piece | 一致 |
| PPI | STRING + IntAct | 15 + 1 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. EFCAB6 — EF-hand calcium-binding domain-containing protein 6，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1501 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=68.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5THR3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000186976-EFCAB6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EFCAB6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5THR3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

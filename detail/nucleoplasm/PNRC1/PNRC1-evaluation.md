---
type: protein-evaluation
gene: "PNRC1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PNRC1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PNRC1 / PROL2 |
| 蛋白名称 | Proline-rich nuclear receptor coactivator 1 |
| 蛋白大小 | 327 aa / 35.2 kDa |
| UniProt ID | Q12796 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm, Nucleoli; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 327 aa / 35.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR028322, IPR026780; Pfam: PF15365 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.0/180** | |
| **归一化总分** | | | **76.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleus (GO:0005634)
- P-body (GO:0000932)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 27 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PROL2 |

**关键文献**:
1. YAP/TAZ enhances P-body formation to promote tumorigenesis.. *eLife*. PMID: 39046443
2. A novel SNP of the PNRC1 gene and its association with reproductive traits in Tsaiya ducks.. *Theriogenology*. PMID: 22494678
3. Integrative Analysis Reveals Genes Causal Relation with Ovarian Cancer and aging.. *Current topics in medicinal chemistry*. PMID: 40353459
4. Patterns of Crystallin Gene Expression in Differentiation State Specific Regions of the Embryonic Chicken Lens.. *Investigative ophthalmology & visual science*. PMID: 35412582
5. Identification of 3 key genes as novel diagnostic and therapeutic targets for OA and COVID-19.. *Frontiers in immunology*. PMID: 37283761

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.2 |
| 高置信度残基 (pLDDT>90) 占比 | 4.3% |
| 置信残基 (pLDDT 70-90) 占比 | 10.4% |
| 中等置信 (pLDDT 50-70) 占比 | 57.8% |
| 低置信 (pLDDT<50) 占比 | 27.5% |
| 有序区域 (pLDDT>70) 占比 | 14.7% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=58.2），有序残基占 14.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR028322, IPR026780; Pfam: PF15365 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DCP1A | 0.867 | 0.786 | — |
| C4BPA | 0.778 | 0.000 | — |
| DDX6 | 0.643 | 0.601 | — |
| PM20D2 | 0.633 | 0.000 | — |
| DCP1B | 0.598 | 0.497 | — |
| ESR1 | 0.508 | 0.000 | — |
| CHD7 | 0.507 | 0.000 | — |
| CRKL | 0.499 | 0.500 | — |
| PRR4 | 0.499 | 0.000 | — |
| STATH | 0.448 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000336931.3 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| NPM1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| EDC4 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| DCP1A | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| DDX6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CRKL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| ENST00000336032 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 8
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 8 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.2 + PDB: 无 | pLDDT=58.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 8 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. PNRC1 — Proline-rich nuclear receptor coactivator 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小327 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=58.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q12796
- Protein Atlas: https://www.proteinatlas.org/ENSG00000146278-PNRC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PNRC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q12796
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

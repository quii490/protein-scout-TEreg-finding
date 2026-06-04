---
type: protein-evaluation
gene: "NOM1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NOM1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NOM1 / C7orf3 |
| 蛋白名称 | Nucleolar MIF4G domain-containing protein 1 |
| 蛋白大小 | 860 aa / 96.3 kDa |
| UniProt ID | Q5C9Z4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoli; UniProt: Nucleus, nucleolus |
| 蛋白大小 | 8/10 | ×1 | 8 | 860 aa / 96.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=20 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR016024, IPR050781, IPR003891, IPR003890; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **136.0/180** | |
| **归一化总分** | | | **75.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli | Enhanced |
| UniProt | Nucleus, nucleolus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（批量模式），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleolus (GO:0005730)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 20 |
| PubMed broad count | 31 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C7orf3 |

**关键文献**:
1. Identification of nucleolar protein NOM1 as a novel nuclear IGF1R-interacting protein.. *Molecular genetics and metabolism*. PMID: 30639046
2. NOM1 targets protein phosphatase I to the nucleolus.. *The Journal of biological chemistry*. PMID: 17965019
3. A new nylon oligomer degradation gene (nylC) on plasmid pOAD2 from a Flavobacterium sp.. *Journal of bacteriology*. PMID: 1459943
4. Role of nucleolar protein NOM1 in pancreatic islet β cell apoptosis in diabetes.. *Experimental and therapeutic medicine*. PMID: 27698723
5. Nom1 mediates pancreas development by regulating ribosome biogenesis in zebrafish.. *PloS one*. PMID: 24967912

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.7 |
| 高置信度残基 (pLDDT>90) 占比 | 29.1% |
| 置信残基 (pLDDT 70-90) 占比 | 30.5% |
| 中等置信 (pLDDT 50-70) 占比 | 10.0% |
| 低置信 (pLDDT<50) 占比 | 30.5% |
| 有序区域 (pLDDT>70) 占比 | 59.6% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（批量模式），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=69.7），有序残基占 59.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016024, IPR050781, IPR003891, IPR003890; Pfam: PF02847, PF02854 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EIF4A3 | 0.996 | 0.981 | — |
| DDX10 | 0.988 | 0.954 | — |
| UTP3 | 0.988 | 0.954 | — |
| WDR3 | 0.986 | 0.954 | — |
| KRR1 | 0.985 | 0.958 | — |
| NGDN | 0.985 | 0.967 | — |
| RRP36 | 0.980 | 0.954 | — |
| NAT10 | 0.979 | 0.954 | — |
| ESF1 | 0.977 | 0.954 | — |
| RRP9 | 0.976 | 0.954 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EEF1D | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| GABARAPL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| TFCP2 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| RRP1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-26310|pubmed:20926688 |
| FBL | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| RPS6 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| NCF1 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| NGDN | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.7 + PDB: 无 | pLDDT=69.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus, nucleolus / Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. NOM1 — Nucleolar MIF4G domain-containing protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小860 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 20 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=69.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5C9Z4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000146909-NOM1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NOM1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5C9Z4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

---
type: protein-evaluation
gene: "DUX1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DUX1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DUX1 |
| 蛋白名称 | Double homeobox protein 1 |
| 蛋白大小 | 170 aa / 19.3 kDa |
| UniProt ID | O43812 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 170 aa / 19.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=77.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001356, IPR017970, IPR051306, IPR009057, IPR000 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **132.0/180** | |
| **归一化总分** | | | **73.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 11 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Homologous Transcription Factors DUX4 and DUX4c Associate with Cytoplasmic Proteins during Muscle Differentiation.. *PloS one*. PMID: 26816005
2. High Content Imaging of Barrett's-Associated High-Grade Dysplasia Cells After siRNA Library Screening Reveals Acid-Responsive Regulators of Cellular Transitions.. *Cellular and molecular gastroenterology and hepatology*. PMID: 32416156
3. Active genes in junk DNA? Characterization of DUX genes embedded within 3.3 kb repeated elements.. *Gene*. PMID: 11245978
4. Characterization of a double homeodomain protein (DUX1) encoded by a cDNA homologous to 3.3 kb dispersed repeated elements.. *Human molecular genetics*. PMID: 9736770
5. Classification and nomenclature of all human homeobox genes.. *BMC biology*. PMID: 17963489

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.5 |
| 高置信度残基 (pLDDT>90) 占比 | 44.7% |
| 置信残基 (pLDDT 70-90) 占比 | 23.5% |
| 中等置信 (pLDDT 50-70) 占比 | 12.4% |
| 低置信 (pLDDT<50) 占比 | 19.4% |
| 有序区域 (pLDDT>70) 占比 | 68.2% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=77.5，有序区 68.2%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR017970, IPR051306, IPR009057, IPR000047; Pfam: PF00046 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ACTN2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-25050|pubmed:26816005 |
| CSNK2B | psi-mi:"MI:0018"(two hybrid) | imex:IM-25050|pubmed:26816005 |
| DES | psi-mi:"MI:0018"(two hybrid) | imex:IM-25050|pubmed:26816005 |
| ACTN3 | psi-mi:"MI:0018"(two hybrid) | imex:IM-25050|pubmed:26816005 |
| CENPE | psi-mi:"MI:0018"(two hybrid) | imex:IM-25050|pubmed:26816005 |
| HADHB | psi-mi:"MI:0018"(two hybrid) | imex:IM-25050|pubmed:26816005 |
| DUX3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 8
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 8 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.5 + PDB: 无 | pLDDT=77.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 0 + 8 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DUX1 — Double homeobox protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小170 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43812
- Protein Atlas: https://www.proteinatlas.org/search/DUX1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DUX1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43812
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

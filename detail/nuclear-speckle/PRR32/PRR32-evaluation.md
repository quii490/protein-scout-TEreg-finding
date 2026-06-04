---
type: protein-evaluation
gene: "PRR32"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PRR32 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PRR32 / CXorf64 |
| 蛋白名称 | Proline-rich protein 32 |
| 蛋白大小 | 298 aa / 31.9 kDa |
| UniProt ID | B1ATL7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Plasma membrane; 额外: Nuclear speckles, Centrosome; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 298 aa / 31.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=49.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR027891; Pfam: PF15488 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117.5/180** | |
| **归一化总分** | | | **65.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Nuclear speckles, Centrosome | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 5 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CXorf64 |

**关键文献**:
1. Identification and characterization of a novel halolysin from Halostella sp. PRR32 with two C-terminal extensions.. *Extremophiles : life under extreme conditions*. PMID: 40591051
2. Genetic parameters and genome-wide association studies including the X chromosome for various reproduction and semen quality traits in Nellore cattle.. *BMC genomics*. PMID: 39794685
3. X-chromosome association study reveals genetic susceptibility loci of hypospadias in southern Chinese population.. *World journal of urology*. PMID: 40335670
4. Generation of an induced pluripotent stem cell line (SSMCi002-A) from a pediatric dilated cardiomyopathy patient carrying heterozygous mutation in the TTN gene.. *Stem cell research*. PMID: 41496282

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 49.3 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 0.7% |
| 中等置信 (pLDDT 50-70) 占比 | 42.3% |
| 低置信 (pLDDT<50) 占比 | 57.0% |
| 有序区域 (pLDDT>70) 占比 | 0.7% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=49.3），有序残基占 0.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027891; Pfam: PF15488 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MCTP1 | 0.526 | 0.000 | — |
| ACTRT1 | 0.523 | 0.000 | — |
| OR10P1 | 0.505 | 0.000 | — |
| GLB1L2 | 0.502 | 0.000 | — |
| SBK3 | 0.479 | 0.000 | — |
| SPANXN4 | 0.478 | 0.000 | — |
| SELENOF | 0.471 | 0.000 | — |
| LRRC23 | 0.464 | 0.000 | — |
| RD3L | 0.447 | 0.000 | — |
| ZNF516 | 0.444 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| YTHDF1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| DTX2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| EFEMP2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| HNRNPF | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 2 / 15 = 13%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 13%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=49.3 + PDB: 无 | pLDDT=49.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Plasma membrane; 额外: Nuclear speckles, Centrosome | 待确认 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PRR32 — Proline-rich protein 32，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小298 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=49.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/B1ATL7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000183631-PRR32/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PRR32
- AlphaFold: https://alphafold.ebi.ac.uk/entry/B1ATL7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

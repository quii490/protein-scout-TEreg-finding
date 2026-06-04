---
type: protein-evaluation
gene: "SPATA17"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SPATA17 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SPATA17 |
| 蛋白名称 | Spermatogenesis-associated protein 17 |
| 蛋白大小 | 361 aa / 43.5 kDa |
| UniProt ID | Q96L03 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Nucleoli, Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 361 aa / 43.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=81.6; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR051185, IPR000048, IPR027417; Pfam: PF00612 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.5/180** | |
| **归一化总分** | | | **68.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli, Cytosol | Uncertain |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 17 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Feature Engineering-Assisted Drug Repurposing on Disease-Drug Transcriptome Profiles in Gastric Cancer.. *Assay and drug development technologies*. PMID: 38572922
2. Expression and identification of a novel apoptosis gene Spata17 (MSRG-11) in mouse spermatogenic cells.. *Acta biochimica et biophysica Sinica*. PMID: 16395525
3. Overexpression of human SPATA17 protein induces germ cell apoptosis in transgenic male mice.. *Molecular biology reports*. PMID: 23079716
4. Genetic analysis of intracapillary glomerular lipoprotein deposits in aging mice.. *PloS one*. PMID: 25353171
5. Overexpression a novel zebra fish spermatogenesis-associated gene 17 (SPATA17) induces apoptosis in GC-1 cells.. *Molecular biology reports*. PMID: 21108043

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.6 |
| 高置信度残基 (pLDDT>90) 占比 | 38.8% |
| 置信残基 (pLDDT 70-90) 占比 | 35.7% |
| 中等置信 (pLDDT 50-70) 占比 | 23.0% |
| 低置信 (pLDDT<50) 占比 | 2.5% |
| 有序区域 (pLDDT>70) 占比 | 74.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=81.6，有序区 74.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051185, IPR000048, IPR027417; Pfam: PF00612 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SPATA4 | 0.738 | 0.000 | — |
| CCDC180 | 0.682 | 0.166 | — |
| KIAA1257 | 0.680 | 0.183 | — |
| SPAG6 | 0.666 | 0.144 | — |
| DPY30 | 0.663 | 0.294 | — |
| GPATCH2 | 0.652 | 0.000 | — |
| SPAG17 | 0.643 | 0.294 | — |
| RRP15 | 0.631 | 0.000 | — |
| DLEC1 | 0.617 | 0.114 | — |
| KDM1B | 0.614 | 0.614 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| KDM1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| - | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TMEM123 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| DLST | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| CALR | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:32814053|imex:IM-28217| |
| NEK7 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32814053|imex:IM-28217| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 6
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.6 + PDB: 无 | pLDDT=81.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm, Nucleoli, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 6 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. SPATA17 — Spermatogenesis-associated protein 17，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小361 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96L03
- Protein Atlas: https://www.proteinatlas.org/ENSG00000162814-SPATA17/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SPATA17
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96L03
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

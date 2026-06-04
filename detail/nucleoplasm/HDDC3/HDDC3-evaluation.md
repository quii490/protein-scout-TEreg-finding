---
type: protein-evaluation
gene: "HDDC3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HDDC3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HDDC3 / MESH1 |
| 蛋白名称 | Guanosine-3',5'-bis(diphosphate) 3'-pyrophosphohydrolase MESH1 |
| 蛋白大小 | 179 aa / 20.3 kDa |
| UniProt ID | Q8N4P3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 179 aa / 20.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=6 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=97.9; PDB: 3NR1, 5VXA |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR003607, IPR006674, IPR052194; Pfam: PF13328 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **127.5/180** | |
| **归一化总分** | | | **70.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6 |
| PubMed broad count | 15 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MESH1 |

**关键文献**:
1. Identification of novel candidate biomarkers and immune infiltration in polycystic ovary syndrome.. *Journal of ovarian research*. PMID: 35794640
2. Exploring Genetic Associations of 3 Types of Risk Factors With Ischemic Stroke: An Integrated Bioinformatics Study.. *Stroke*. PMID: 38591222
3. MicroRNA related polymorphisms and breast cancer risk.. *PloS one*. PMID: 25390939
4. NADPH oxidase 4 is dispensable for skin myofibroblast differentiation and wound healing.. *Redox biology*. PMID: 36708644
5. A metazoan ortholog of SpoT hydrolyzes ppGpp and functions in starvation responses.. *Nature structural & molecular biology*. PMID: 20818390

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 97.9 |
| 高置信度残基 (pLDDT>90) 占比 | 98.3% |
| 置信残基 (pLDDT 70-90) 占比 | 1.1% |
| 中等置信 (pLDDT 50-70) 占比 | 0.6% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 99.4% |
| 可用 PDB 条目 | 3NR1, 5VXA |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（3NR1, 5VXA）+ AlphaFold高质量预测（pLDDT=97.9），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003607, IPR006674, IPR052194; Pfam: PF13328 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MRPS9 | 0.966 | 0.943 | — |
| RPL11 | 0.961 | 0.961 | — |
| RPS11 | 0.961 | 0.961 | — |
| MRPL20 | 0.958 | 0.943 | — |
| MRPS6 | 0.952 | 0.943 | — |
| MRPL36 | 0.952 | 0.935 | — |
| MRPS16 | 0.951 | 0.943 | — |
| NME3 | 0.951 | 0.000 | — |
| MRPL27 | 0.951 | 0.943 | — |
| NME6 | 0.949 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NMI | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CCDC172 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| MSTO1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| STAT5B | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| WRAP73 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CCHCR1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| AKAP9 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MAGEA4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| GOLGA8F | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |
| GOLGA8DP | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=97.9 + PDB: 3NR1, 5VXA | pLDDT=97.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Cytosol | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. HDDC3 — Guanosine-3',5'-bis(diphosphate) 3'-pyrophosphohydrolase MESH1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小179 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 6 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N4P3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000184508-HDDC3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HDDC3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N4P3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

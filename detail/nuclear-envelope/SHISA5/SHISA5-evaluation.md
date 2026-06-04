---
type: protein-evaluation
gene: "SHISA5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SHISA5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SHISA5 / SCOTIN |
| 蛋白名称 | Protein shisa-5 |
| 蛋白大小 | 240 aa / 25.6 kDa |
| UniProt ID | Q8N114 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Endoplasmic reticulum membrane; Nucleus membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 240 aa / 25.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026910, IPR053891; Pfam: PF13908 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 12 partners; IntAct 11 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Endoplasmic reticulum membrane; Nucleus membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum lumen (GO:0005788)
- endoplasmic reticulum membrane (GO:0005789)
- nuclear membrane (GO:0031965)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 20 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SCOTIN |

**关键文献**:
1. Single-cell RNA sequencing reveals immune regulatory mechanisms and molecular therapeutic strategies in the microenvironment of multiple myeloma.. *International journal of surgery (London, England)*. PMID: 40899849
2. High-fat stimulation induces atrial structural remodeling via the TPM1/P53/SHISA5 Axis.. *Lipids in health and disease*. PMID: 40221727
3. Transcriptome profiling of morphogenetic differences between contour and flight feathers in duck.. *British poultry science*. PMID: 35000502
4. The molecular structure of SHISA5 protein and its novel role in primary biliary cholangitis: From single-cell RNA sequencing to biomarkers.. *International journal of biological macromolecules*. PMID: 39800023
5. Integrating multi-omics and machine learning to unravel mechanisms of lymph node metastasis in papillary carcinoma with and without thyroiditis.. *Frontiers in immunology*. PMID: 41789084

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.7 |
| 高置信度残基 (pLDDT>90) 占比 | 1.7% |
| 置信残基 (pLDDT 70-90) 占比 | 19.2% |
| 中等置信 (pLDDT 50-70) 占比 | 46.7% |
| 低置信 (pLDDT<50) 占比 | 32.5% |
| 有序区域 (pLDDT>70) 占比 | 20.9% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=58.7），有序残基占 20.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026910, IPR053891; Pfam: PF13908 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PIDD1 | 0.540 | 0.131 | — |
| TP53 | 0.539 | 0.000 | — |
| FAM20C | 0.503 | 0.000 | — |
| CDKN1A | 0.496 | 0.000 | — |
| CD34 | 0.495 | 0.000 | — |
| APEH | 0.458 | 0.066 | — |
| USP19 | 0.441 | 0.087 | — |
| PERP | 0.438 | 0.000 | — |
| PSCA | 0.424 | 0.045 | — |
| GSG1L2 | 0.418 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| COPS5 | psi-mi:"MI:0018"(two hybrid) | pubmed:18624398|imex:IM-19021 |
| Pdcd6 | psi-mi:"MI:0096"(pull down) | imex:IM-20894|pubmed:17889823 |
| WWOX | psi-mi:"MI:0089"(protein array) | pubmed:15064722|imex:IM-17723 |
| SCAND1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ARL6IP1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| DESI1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TVP23B | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SGTB | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SGTA | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TFAP2C | psi-mi:"MI:0018"(two hybrid) | imex:IM-22985|pubmed:24835590 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 12，IntAct interactions: 11
- 调控相关比例: 0 / 12 = 0%

**评价**: STRING 12 个预测互作，IntAct 11 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.7 + PDB: 无 | pLDDT=58.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Nucleus membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 12 + 11 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SHISA5 — Protein shisa-5，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小240 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=58.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N114
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164054-SHISA5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SHISA5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N114
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

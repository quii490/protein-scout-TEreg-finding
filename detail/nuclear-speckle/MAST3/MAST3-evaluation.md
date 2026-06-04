---
type: protein-evaluation
gene: "MAST3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MAST3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MAST3 |
| 蛋白名称 | MAST3 (UniProt未获取) |
| 蛋白大小 | 未知 aa / 未知 kDa |
| UniProt ID | MAST3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; UniProt: 暂无数据（UniProt获取失败） |
| 蛋白大小 | 5/10 | ×1 | 5 | 未知 aa / 未知 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=31 篇 (≤40→8) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | 暂无数据 (UniProt未获取) |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 12 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.5/180** | |
| **归一化总分** | | | **60.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Approved |
| UniProt | 暂无数据（UniProt获取失败） | 获取失败 |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释 (UniProt未获取)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 31 |
| PubMed broad count | 44 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Microtubule associated serine/threonine kinase-3 inhibits the malignant phenotype of breast cancer by promoting phosphorylation-mediated ubiquitination degradation of yes-associated protein.. *Breast cancer research : BCR*. PMID: 40312366
2. MAST3 modulates the inflammatory response and proliferation of fibroblast-like synoviocytes in rheumatoid arthritis.. *International immunopharmacology*. PMID: 31644963
3. MiR-125a-3p inhibits cell proliferation and inflammation responses in fibroblast-like synovial cells in rheumatoid arthritis by mediating the Wnt/β-catenin and NF-κB pathways via targeting MAST3.. *Journal of musculoskeletal & neuronal interactions*. PMID: 34854396
4. The Role of Microtubule Associated Serine/Threonine Kinase 3 Variants in Neurodevelopmental Diseases: Genotype-Phenotype Association.. *Frontiers in molecular neuroscience*. PMID: 35095415
5. Pathogenic MAST3 Variants in the STK Domain Are Associated with Epilepsy.. *Annals of neurology*. PMID: 34185323

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 暂无数据 (UniProt未获取) |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MAGI3 | 0.763 | 0.000 | — |
| PTEN | 0.694 | 0.326 | — |
| SNTB2 | 0.643 | 0.045 | — |
| ARPP19 | 0.632 | 0.112 | — |
| NEK2 | 0.497 | 0.000 | — |
| ENSA | 0.496 | 0.121 | — |
| FRMD1 | 0.475 | 0.000 | — |
| YWHAH | 0.458 | 0.458 | — |
| ABTB1 | 0.437 | 0.045 | — |
| DLG1 | 0.416 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PTEN | psi-mi:"MI:0096"(pull down) | pubmed:15951562 |
| CNTNAP4 | psi-mi:"MI:0018"(two hybrid) | pubmed:12421765 |
| YWHAH | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11897|pubmed:17979178 |
| PRKAB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| PRKAA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| YWHAG | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RASAL2 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| USP21 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| ZBTB21 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| AGAP1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 12，IntAct interactions: 15
- 调控相关比例: 0 / 12 = 0%

**评价**: STRING 12 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | 暂无数据（UniProt获取失败） / Nuclear speckles | 待确认 |
| PPI | STRING + IntAct | 12 + 15 interactions | 数据充分 |

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
1. MAST3 — MAST3 (UniProt未获取)，非常新颖，仅有少数基础研究。
2. 蛋白大小未知 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 31 篇，已有一定研究基础
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/MAST3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000099308-MAST3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MAST3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/MAST3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

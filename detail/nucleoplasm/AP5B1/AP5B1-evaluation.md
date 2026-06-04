---
type: protein-evaluation
gene: "AP5B1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## AP5B1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AP5B1 |
| 蛋白名称 | AP-5 complex subunit beta-1 |
| 蛋白大小 | 878 aa / 93.9 kDa |
| UniProt ID | Q2VPB7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Vesicles; 额外: Golgi apparatus; UniProt: 无注释 |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 878 aa / 93.9 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 🏗️ 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=79.8; PDB: 8YAB, 8YAH |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR038741, IPR048980, IPR048981, IPR048979, IPR048 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.0/180** | |
| **归一化总分 (÷1.83)** | | | **67.8/100******** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles; 额外: Golgi apparatus | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**GO Cellular Component**:
- AP-5 adaptor complex (GO:0044599)
- AP-type membrane coat adaptor complex (GO:0030119)
- late endosome (GO:0005770)
- lysosomal membrane (GO:0005765)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 22 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Development and validation of a risk prediction model for diabetic kidney disease in patients with diabetic retinopathy.. *Frontiers in endocrinology*. PMID: 40391008
2. Joint transcriptomic and cytometric study of children with peanut allergy reveals molecular and cellular cross talk in reaction thresholds.. *The Journal of allergy and clinical immunology*. PMID: 38272374
3. Bi-allelic variants in three genes encoding distinct subunits of the vesicular AP-5 complex cause hereditary macular dystrophy.. *American journal of human genetics*. PMID: 40081374
4. Whole exome sequencing in three families segregating a pediatric case of sarcoidosis.. *BMC medical genomics*. PMID: 29510755
5. Bi-allelic variants in AP5Z1 and AP5B1 lead to retinal degeneration.. *HGG advances*. PMID: 41830174

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.8 |
| 高置信度残基 (pLDDT>90) 占比 | 15.1% |
| 置信残基 (pLDDT 70-90) 占比 | 68.3% |
| 中等置信 (pLDDT 50-70) 占比 | 10.7% |
| 低置信 (pLDDT<50) 占比 | 5.8% |
| 有序区域 (pLDDT>70) 占比 | 83.4% |
| 可用 PDB 条目 | 8YAB, 8YAH |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: PDB实验结构（8YAB, 8YAH）+ AlphaFold高质量预测（pLDDT=79.8），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR038741, IPR048980, IPR048981, IPR048979, IPR048978; Pfam: PF21589, PF21590, PF21588 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AP5S1 | 0.999 | 0.591 | — |
| AP5Z1 | 0.998 | 0.052 | — |
| AP5M1 | 0.996 | 0.756 | — |
| SPG11 | 0.980 | 0.435 | — |
| AP4E1 | 0.922 | 0.000 | — |
| AP4S1 | 0.922 | 0.000 | — |
| AP3S2 | 0.921 | 0.048 | — |
| AP4B1 | 0.920 | 0.000 | — |
| AP4M1 | 0.918 | 0.000 | — |
| AP1S1 | 0.916 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| AP5M1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CCNJL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ARHGAP25 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| INSYN2A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SKP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GDF9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CAMK2B | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| NIF3L1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| SPG11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PKD1L2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.8 + PDB: 8YAB, 8YAH | pLDDT=79.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Vesicles; 额外: Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ 

**核心优势**:
1. AP5B1 — AP-5 complex subunit beta-1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小878 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q2VPB7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000254470-AP5B1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AP5B1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q2VPB7
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 02:57:19

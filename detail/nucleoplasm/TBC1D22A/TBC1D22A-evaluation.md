---
type: protein-evaluation
gene: "TBC1D22A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TBC1D22A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TBC1D22A / C22orf4 |
| 蛋白名称 | TBC1 domain family member 22A |
| 蛋白大小 | 517 aa / 59.1 kDa |
| UniProt ID | Q8WUA7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Golgi apparatus; 额外: Nucleoplasm, Vesicles; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 517 aa / 59.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=76.1; PDB: 2QFZ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000195, IPR035969; Pfam: PF00566 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **125.0/180** | |
| **归一化总分** | | | **69.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nucleoplasm, Vesicles | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- Golgi apparatus (GO:0005794)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 20 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C22orf4 |

**关键文献**:
1. High Expression of TBC1 Domain Family Member 22A is Related to Poor Prognosis in Ovarian Serous Cystadenocarcinoma.. *International journal of medical sciences*. PMID: 39439452
2. TBC1D22B Regulates ER-to-Golgi Trafficking via RAB1B Inactivation and Promotes Oncogenic Programs in Breast Cancer.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 40878439
3. Identification and validation of genes associated with prognosis of cisplatin-resistant ovarian cancer.. *BMC cancer*. PMID: 39103807
4. Genotype-Phenotype Associations in Phelan-McDermid Syndrome: Insights into Novel Genes Beyond SHANK3.. *International journal of molecular sciences*. PMID: 40429797
5. ACBD3 interaction with TBC1 domain 22 protein is differentially affected by enteroviral and kobuviral 3A protein binding.. *mBio*. PMID: 23572552

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.1 |
| 高置信度残基 (pLDDT>90) 占比 | 59.0% |
| 置信残基 (pLDDT 70-90) 占比 | 4.8% |
| 中等置信 (pLDDT 50-70) 占比 | 6.0% |
| 低置信 (pLDDT<50) 占比 | 30.2% |
| 有序区域 (pLDDT>70) 占比 | 63.8% |
| 可用 PDB 条目 | 2QFZ |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 高质量预测（pLDDT=76.1，有序区 63.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000195, IPR035969; Pfam: PF00566 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ACBD3 | 0.867 | 0.782 | — |
| TBC1D20 | 0.673 | 0.079 | — |
| MICU1 | 0.649 | 0.605 | — |
| GRTP1 | 0.588 | 0.000 | — |
| MRPS6 | 0.583 | 0.580 | — |
| TRABD | 0.564 | 0.000 | — |
| RAB43 | 0.556 | 0.251 | — |
| PPP6R2 | 0.544 | 0.000 | — |
| TBC1D21 | 0.542 | 0.000 | — |
| MICU2 | 0.541 | 0.451 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000336724.4 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| TGOLN2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| STT3B | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| TBC1D22B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ACSL4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DNAJB5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FDXR | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EPHA4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EFNB3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SUPT6H | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.1 + PDB: 2QFZ | pLDDT=76.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Golgi apparatus; 额外: Nucleoplasm, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TBC1D22A — TBC1 domain family member 22A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小517 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WUA7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000054611-TBC1D22A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TBC1D22A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WUA7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

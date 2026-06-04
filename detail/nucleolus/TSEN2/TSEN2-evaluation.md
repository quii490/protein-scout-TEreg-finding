---
type: protein-evaluation
gene: "TSEN2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TSEN2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TSEN2 / SEN2 |
| 蛋白名称 | tRNA-splicing endonuclease subunit Sen2 |
| 蛋白大小 | 465 aa / 53.2 kDa |
| UniProt ID | Q8NCE0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Centrosome, Cytosol; UniProt: Nucleus; Nucleus, nucleolus |
| 蛋白大小 | 10/10 | ×1 | 10 | 465 aa / 53.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=72.1; PDB: 7UXA, 7ZRZ, 8HMY, 8HMZ, 8ISS |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011856, IPR036167, IPR006677, IPR006678, IPR006 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **144.0/180** | |
| **归一化总分** | | | **80.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Centrosome, Cytosol | Supported |
| UniProt | Nucleus; Nucleus, nucleolus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centrosome (GO:0005813)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- tRNA-intron endonuclease complex (GO:0000214)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 20 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SEN2 |

**关键文献**:
1. Pontocerebellar hypoplasia type 2 and TSEN2: review of the literature and two novel mutations.. *European journal of medical genetics*. PMID: 23562994
2. Cotranscription and intergenic splicing of the PPARG and TSEN2 genes in cattle.. *BMC genomics*. PMID: 16595010
3. Gammaherpesvirus infection triggers the formation of tRNA fragments from premature tRNAs.. *mBio*. PMID: 40444975
4. A splice site mutation in the TSEN2 causes a new syndrome with craniofacial and central nervous system malformations, and atypical hemolytic uremic syndrome.. *Clinical genetics*. PMID: 34964109
5. Clinical, neuroradiological and genetic findings in pontocerebellar hypoplasia.. *Brain : a journal of neurology*. PMID: 20952379

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.1 |
| 高置信度残基 (pLDDT>90) 占比 | 53.1% |
| 置信残基 (pLDDT 70-90) 占比 | 12.5% |
| 中等置信 (pLDDT 50-70) 占比 | 5.4% |
| 低置信 (pLDDT<50) 占比 | 29.0% |
| 有序区域 (pLDDT>70) 占比 | 65.6% |
| 可用 PDB 条目 | 7UXA, 7ZRZ, 8HMY, 8HMZ, 8ISS |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（7UXA, 7ZRZ, 8HMY, 8HMZ, 8ISS）+ AlphaFold极高置信度预测（pLDDT=72.1），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011856, IPR036167, IPR006677, IPR006678, IPR006676; Pfam: PF01974, PF02778 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TSEN34 | 0.999 | 0.840 | — |
| TSEN54 | 0.999 | 0.905 | — |
| TSEN15 | 0.999 | 0.782 | — |
| CLP1 | 0.990 | 0.807 | — |
| TRIP10 | 0.822 | 0.822 | — |
| CSTF2 | 0.812 | 0.000 | — |
| CPSF4 | 0.809 | 0.000 | — |
| CPSF6 | 0.807 | 0.000 | — |
| CPSF1 | 0.801 | 0.000 | — |
| FNBP1 | 0.785 | 0.782 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Clp1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| TSEN15 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| XPC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SFSWAP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TMED8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TSEN54 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TSEN34 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GREB1L | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TAX1BP1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TEPSIN | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.1 + PDB: 7UXA, 7ZRZ, 8HMY, 8HMZ, 8ISS | pLDDT=72.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, nucleolus / Nucleoplasm; 额外: Centrosome, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TSEN2 — tRNA-splicing endonuclease subunit Sen2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小465 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NCE0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000154743-TSEN2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TSEN2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NCE0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

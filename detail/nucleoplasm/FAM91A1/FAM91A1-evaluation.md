---
type: protein-evaluation
gene: "FAM91A1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM91A1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM91A1 |
| 蛋白名称 | Protein FAM91A1 |
| 蛋白大小 | 838 aa / 93.9 kDa |
| UniProt ID | Q658Y4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Microtubules; UniProt: Golgi apparatus, trans-Golgi network; Cytoplasmic vesicle |
| 蛋白大小 | 8/10 | ×1 | 8 | 838 aa / 93.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=77.0; PDB: 8JJ9, 8XFB, 8Z9M |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039199, IPR028097, IPR028091; Pfam: PF14648, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **127.0/180** | |
| **归一化总分** | | | **70.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Microtubules | Approved |
| UniProt | Golgi apparatus, trans-Golgi network; Cytoplasmic vesicle | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasmic vesicle (GO:0031410)
- trans-Golgi network (GO:0005802)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 12 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. The WDR11 complex is a receptor for acidic-cluster-containing cargo proteins.. *Cell*. PMID: 39013469
2. NRG1 fusions in breast cancer.. *Breast cancer research : BCR*. PMID: 33413557
3. FAM91A1-TBC1D23 complex structure reveals human genetic variations susceptible for PCH.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 37903274
4. Squalene through Its Post-Squalene Metabolites Is a Modulator of Hepatic Transcriptome in Rabbits.. *International journal of molecular sciences*. PMID: 35456988
5. Dysbindin-associated proteome in the p2 synaptosome fraction of mouse brain.. *Journal of proteome research*. PMID: 25198678

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.0 |
| 高置信度残基 (pLDDT>90) 占比 | 40.1% |
| 置信残基 (pLDDT 70-90) 占比 | 35.8% |
| 中等置信 (pLDDT 50-70) 占比 | 6.1% |
| 低置信 (pLDDT<50) 占比 | 18.0% |
| 有序区域 (pLDDT>70) 占比 | 75.9% |
| 可用 PDB 条目 | 8JJ9, 8XFB, 8Z9M |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（8JJ9, 8XFB, 8Z9M）+ AlphaFold高质量预测（pLDDT=77.0），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039199, IPR028097, IPR028091; Pfam: PF14648, PF14647 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| C17orf75 | 0.965 | 0.830 | — |
| TBC1D23 | 0.819 | 0.000 | — |
| NUDCD1 | 0.652 | 0.619 | — |
| WDR11 | 0.647 | 0.000 | — |
| RALGAPA1 | 0.595 | 0.000 | — |
| CPD | 0.574 | 0.000 | — |
| RHOH | 0.563 | 0.163 | — |
| VCPIP1 | 0.549 | 0.000 | — |
| GOLGA4 | 0.534 | 0.000 | — |
| RALGAPB | 0.533 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MAP1LC3B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| GABARAPL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| LAMP1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| TGOLN2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| RNF19B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FGF8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HLA-B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZNF397 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.0 + PDB: 8JJ9, 8XFB, 8Z9M | pLDDT=77.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Golgi apparatus, trans-Golgi network; Cytoplasmic  / Nucleoplasm, Microtubules | 一致 |
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
1. FAM91A1 — Protein FAM91A1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小838 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q658Y4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000176853-FAM91A1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM91A1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q658Y4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

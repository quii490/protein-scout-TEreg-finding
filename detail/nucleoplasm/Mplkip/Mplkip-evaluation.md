---
type: protein-evaluation
gene: "Mplkip"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## Mplkip 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | Mplkip / C7orf11, TTDN1 |
| 蛋白名称 | M-phase-specific PLK1-interacting protein |
| 蛋白大小 | 179 aa / 19.1 kDa |
| UniProt ID | Q8TAP9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Golgi apparatus, Vesicles; UniProt: Nucleus; Cytoplasm; Cytoplasm, cytoskeleton, microtubule org |
| 蛋白大小 | 8/10 | ×1 | 8 | 179 aa / 19.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026618, IPR028265; Pfam: PF15502 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Golgi apparatus, Vesicles | Supported |
| UniProt | Nucleus; Cytoplasm; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centrosome (GO:0005813)
- cytoplasm (GO:0005737)
- Golgi apparatus (GO:0005794)
- midbody (GO:0030496)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 19 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C7orf11, TTDN1 |

**关键文献**:
1. Trichothiodystrophy-associated MPLKIP maintains DBR1 levels for proper lariat debranching and ectodermal differentiation.. *EMBO molecular medicine*. PMID: 37800682
2. A homozygous G insertion in MPLKIP leads to TTDN1 with the hypergonadotropic hypogonadism symptom.. *BMC medical genetics*. PMID: 30598092
3. A Rare Contiguous Gene Deletion Leading to Trichothiodystrophy Type 4 and Glutaric Aciduria Type 3.. *Molecular syndromology*. PMID: 37064336
4. Bi-allelic TARS Mutations Are Associated with Brittle Hair Phenotype.. *American journal of human genetics*. PMID: 31374204
5. A novel MPLKIP-variant in three Finnish patients with non-photosensitive trichothiodystrophy type 4.. *American journal of medical genetics. Part A*. PMID: 33729667

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.3 |
| 高置信度残基 (pLDDT>90) 占比 | 2.2% |
| 置信残基 (pLDDT 70-90) 占比 | 11.7% |
| 中等置信 (pLDDT 50-70) 占比 | 46.9% |
| 低置信 (pLDDT<50) 占比 | 39.1% |
| 有序区域 (pLDDT>70) 占比 | 13.9% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=56.3），有序残基占 13.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026618, IPR028265; Pfam: PF15502 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SUGCT | 0.986 | 0.000 | — |
| FAM3B | 0.784 | 0.000 | — |
| GTF2H5 | 0.734 | 0.000 | — |
| FAM120C | 0.719 | 0.000 | — |
| DNAJC28 | 0.717 | 0.000 | — |
| RNF113A | 0.712 | 0.000 | — |
| CWC15 | 0.592 | 0.000 | — |
| SGCE | 0.584 | 0.000 | — |
| CTTNBP2 | 0.582 | 0.000 | — |
| RPGR | 0.577 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DBR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GORASP2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| NTAQ1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| AKAP8L | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KCTD17 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |
| NDOR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PLK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ATE1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| IFI30 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.3 + PDB: 无 | pLDDT=56.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cytoplasm, cytoskeleton, micro / Nucleoplasm; 额外: Golgi apparatus, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. Mplkip — M-phase-specific PLK1-interacting protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小179 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=56.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TAP9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000168303-MPLKIP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=Mplkip
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TAP9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

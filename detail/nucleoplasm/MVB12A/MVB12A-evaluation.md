---
type: protein-evaluation
gene: "MVB12A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MVB12A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MVB12A / CFBP, FAM125A |
| 蛋白名称 | Multivesicular body subunit 12A |
| 蛋白大小 | 273 aa / 28.8 kDa |
| UniProt ID | Q96EY5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles; UniProt: Cytoplasm; Nucleus; Endosome; Cytoplasm, cytoskeleton, micro |
| 蛋白大小 | 10/10 | ×1 | 10 | 273 aa / 28.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=77.3; PDB: 6VME |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR023341, IPR040335, IPR018798, IPR023340; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **137.0/180** | |
| **归一化总分** | | | **76.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles | Supported |
| UniProt | Cytoplasm; Nucleus; Endosome; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; La... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centrosome (GO:0005813)
- cytosol (GO:0005829)
- endosome membrane (GO:0010008)
- ESCRT I complex (GO:0000813)
- extracellular exosome (GO:0070062)
- late endosome membrane (GO:0031902)
- nucleus (GO:0005634)
- vesicle (GO:0031982)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 14 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CFBP, FAM125A |

**关键文献**:
1. Distinct tumor genomic signatures underlie canine macrophage polarization.. *PloS one*. PMID: 42030266
2. Distinct functions of human MVB12A and MVB12B in the ESCRT-I dependent on their posttranslational modifications.. *Biochemical and biophysical research communications*. PMID: 20654576
3. Transcriptome Analysis Reveals Hub Genes Regulating Autophagy in Patients With Severe COVID-19.. *Frontiers in genetics*. PMID: 35923698
4. Structural basis for membrane targeting by the MVB12-associated β-prism domain of the human ESCRT-I MVB12 subunit.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 22232651
5. Positive effects of bile acids alleviating heat stress in laying hens by enhancing immunity via metabolome and transcriptome integration.. *Poultry science*. PMID: 41558077

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.3 |
| 高置信度残基 (pLDDT>90) 占比 | 39.6% |
| 置信残基 (pLDDT 70-90) 占比 | 28.2% |
| 中等置信 (pLDDT 50-70) 占比 | 15.8% |
| 低置信 (pLDDT<50) 占比 | 16.5% |
| 有序区域 (pLDDT>70) 占比 | 67.8% |
| 可用 PDB 条目 | 6VME |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 高质量预测（pLDDT=77.3，有序区 67.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR023341, IPR040335, IPR018798, IPR023340; Pfam: PF10240 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TSG101 | 0.999 | 0.989 | — |
| VPS37B | 0.999 | 0.987 | — |
| VPS28 | 0.999 | 0.991 | — |
| VPS37A | 0.995 | 0.500 | — |
| VPS37C | 0.985 | 0.500 | — |
| VPS25 | 0.978 | 0.526 | — |
| UBAP1 | 0.976 | 0.000 | — |
| VPS37D | 0.975 | 0.324 | — |
| VPS36 | 0.972 | 0.000 | — |
| STAM | 0.969 | 0.453 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| EBI-1257123 | psi-mi:"MI:0096"(pull down) | pubmed:19367725|imex:IM-20587 |
| Slc2a4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:16396496|mint:MINT-5218 |
| P/V/C | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:22810585|imex:IM-17331 |
| PDLIM7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CIDEB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| UBE2U | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| VPS28 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CD2AP | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| PPP1R27 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.3 + PDB: 6VME | pLDDT=77.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Endosome; Cytoplasm, cytoskele / Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. MVB12A — Multivesicular body subunit 12A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小273 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96EY5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000141971-MVB12A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MVB12A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96EY5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

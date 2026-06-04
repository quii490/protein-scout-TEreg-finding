---
type: protein-evaluation
gene: "SIMC1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SIMC1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SIMC1 / C5orf25, PLEIAD |
| 蛋白名称 | SUMO-interacting motif-containing protein 1 |
| 蛋白大小 | 872 aa / 96.8 kDa |
| UniProt ID | Q8NDZ2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nucleoli fibrillar center; UniProt: Nucleus, PML body; Cytoplasm; Cytoplasm, myofibril, sarcomer |
| 蛋白大小 | 8/10 | ×1 | 8 | 872 aa / 96.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.3; PDB: 7T5P |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR052119 |
| PPI 网络 | 8/10 | ×3 | 24 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **143.5/180** | |
| **归一化总分** | | | **79.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli fibrillar center | Supported |
| UniProt | Nucleus, PML body; Cytoplasm; Cytoplasm, myofibril, sarcomere | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- PML body (GO:0016605)
- sarcomere (GO:0030017)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 13 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C5orf25, PLEIAD |

**关键文献**:
1. Human gene expression microarray analysis of the HPV 6bE7-HaCaT stable cell line.. *Gene*. PMID: 29501815
2. Integrative Analysis of Differently Expressed Genes Reveals a 17-Gene Prognosis Signature for Endometrial Carcinoma.. *BioMed research international*. PMID: 34337010
3. Characterization of the conserved features of the NSE6 subunit of the Physcomitrium patens SMC5/6 complex.. *The Plant journal : for cell and molecular biology*. PMID: 37191775
4. B chromosome retrotransposed sequences persist through speciation, contributing to genomic and regulatory innovations in the fish genus Psalidodon (Characiformes, Acestrorhamphidae).. *PloS one*. PMID: 41481677
5. PLEIAD/SIMC1/C5orf25, a novel autolysis regulator for a skeletal-muscle-specific calpain, CAPN3, scaffolds a CAPN3 substrate, CTBP1.. *Journal of molecular biology*. PMID: 23707407

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.3 |
| 高置信度残基 (pLDDT>90) 占比 | 27.4% |
| 置信残基 (pLDDT 70-90) 占比 | 13.2% |
| 中等置信 (pLDDT 50-70) 占比 | 2.8% |
| 低置信 (pLDDT<50) 占比 | 56.7% |
| 有序区域 (pLDDT>70) 占比 | 40.6% |
| 可用 PDB 条目 | 7T5P |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=58.3），有序残基占 40.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052119 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CAPN3 | 0.654 | 0.113 | — |
| NSMCE1 | 0.613 | 0.613 | — |
| RNF111 | 0.549 | 0.000 | — |
| SLF2 | 0.542 | 0.533 | — |
| SMC6 | 0.494 | 0.492 | — |
| UBE2I | 0.484 | 0.091 | — |
| FAM153B | 0.479 | 0.000 | — |
| RAB24 | 0.459 | 0.065 | — |
| DNAJB11 | 0.451 | 0.439 | — |
| GNS | 0.442 | 0.099 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TUBA4A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| YWHAG | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| WNK1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| NSMCE1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| C5AR2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| IL17RA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NPY2R | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SDF4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KLHL10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| BBS7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 4 / 15 = 27%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 27%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.3 + PDB: 7T5P | pLDDT=58.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, PML body; Cytoplasm; Cytoplasm, myofibril / Nucleoplasm; 额外: Nucleoli fibrillar center | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SIMC1 — SUMO-interacting motif-containing protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小872 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=58.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NDZ2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000170085-SIMC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SIMC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NDZ2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

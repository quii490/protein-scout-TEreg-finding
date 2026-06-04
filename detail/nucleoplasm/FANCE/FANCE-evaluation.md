---
type: protein-evaluation
gene: "FANCE"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FANCE 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FANCE / FACE |
| 蛋白名称 | Fanconi anemia group E protein |
| 蛋白大小 | 536 aa / 58.7 kDa |
| UniProt ID | Q9HB96 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FANCE/IF_images/HEL_1.jpg|HEL]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FANCE/IF_images/U2OS_1.jpg|U2OS]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Mitotic chromosome, Centrosome; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 536 aa / 58.7 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=78 篇 (≤80→4) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=76.0; PDB: 2ILR, 7KZP, 7KZQ, 7KZR, 7KZS, 7KZT, 7KZV |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039685, IPR021025; Pfam: PF11510 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **114.0/180** | |
| **归一化总分** | | | **63.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Mitotic chromosome, Centrosome | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- centrosome (GO:0005813)
- chromatin (GO:0000785)
- chromosome (GO:0005694)
- cytosol (GO:0005829)
- Fanconi anaemia nuclear complex (GO:0043240)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 78 |
| PubMed broad count | 147 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FACE |

**关键文献**:
1. Fanconi Anemia.. **. PMID: 20301575
2. Molecular Characterization of KRAS Wild-type Tumors in Patients with Pancreatic Adenocarcinoma.. *Clinical cancer research : an official journal of the American Association for Cancer Research*. PMID: 35302596
3. The FANCC-FANCE-FANCF complex is evolutionarily conserved and regulates meiotic recombination.. *Nucleic acids research*. PMID: 36652992
4. Heterozygous Germline Fanconi Anemia-Related Gene Mutations Increase Susceptibility to Germ Cell Tumors.. *JCO precision oncology*. PMID: 40906985
5. Pathogenic variants reveal candidate genes for prostate cancer germline testing for men of African ancestry.. *Nature communications*. PMID: 41038821

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.0 |
| 高置信度残基 (pLDDT>90) 占比 | 45.7% |
| 置信残基 (pLDDT 70-90) 占比 | 25.6% |
| 中等置信 (pLDDT 50-70) 占比 | 6.3% |
| 低置信 (pLDDT<50) 占比 | 22.4% |
| 有序区域 (pLDDT>70) 占比 | 71.3% |
| 可用 PDB 条目 | 2ILR, 7KZP, 7KZQ, 7KZR, 7KZS, 7KZT, 7KZV |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FANCE/FANCE-PAE.png]]

**评价**: PDB实验结构（2ILR, 7KZP, 7KZQ, 7KZR, 7KZS, 7KZT, 7KZV）+ AlphaFold极高置信度预测（pLDDT=76.0），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039685, IPR021025; Pfam: PF11510 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FANCM | 0.999 | 0.994 | — |
| FANCB | 0.999 | 0.998 | — |
| FANCC | 0.999 | 0.998 | — |
| CENPX | 0.999 | 0.994 | — |
| CENPS | 0.999 | 0.994 | — |
| FANCF | 0.999 | 0.998 | — |
| FAAP100 | 0.999 | 0.998 | — |
| FANCG | 0.999 | 0.955 | — |
| FANCD2 | 0.999 | 0.971 | — |
| FANCA | 0.999 | 0.998 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FANCC | psi-mi:"MI:0018"(two hybrid) | pubmed:12649160|imex:IM-19947 |
| FANCD2 | psi-mi:"MI:0018"(two hybrid) | pubmed:12649160|imex:IM-19947 |
| Erh | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| FANCM | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17289582|imex:IM-25488 |
| GPC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GNPAT | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ENPP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GNA13 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PI4K2A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RAB21 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.0 + PDB: 2ILR, 7KZP, 7KZQ, 7KZR, 7KZS,  | pLDDT=76.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Mitotic chromosome, Centrosome | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FANCE — Fanconi anemia group E protein，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小536 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 78 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9HB96
- Protein Atlas: https://www.proteinatlas.org/ENSG00000112039-FANCE/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FANCE
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HB96
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FANCE/FANCE-PAE.png]]





---
type: protein-evaluation
gene: "JRKL"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## JRKL 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | JRKL |
| 蛋白名称 | Jerky protein homolog-like |
| 蛋白大小 | 524 aa / 59.9 kDa |
| UniProt ID | Q9Y4A0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Cytokinetic bridge; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 524 aa / 59.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=79.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050863, IPR004875, IPR009057, IPR006600, IPR007 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 7 partners; IntAct 7 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **141.5/180** | |
| **归一化总分** | | | **78.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytokinetic bridge | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 7 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Anti-inflammatory effect of trans-anethol in a rat model of myocardial ischemia-reperfusion injury.. *Biomedicine & pharmacotherapy = Biomedecine & pharmacotherapie*. PMID: 35658236
2. Reorganization of 3D chromatin architecture in doxorubicin-resistant breast cancer cells.. *Frontiers in cell and developmental biology*. PMID: 36003143
3. Evolution of pogo, a separate superfamily of IS630-Tc1-mariner transposons, revealing recurrent domestication events in vertebrates.. *Mobile DNA*. PMID: 32742312
4. Identification of the Genomic Insertion Site of the Thyroid Peroxidase Promoter-Cre Recombinase Transgene Using a Novel, Efficient, Next-Generation DNA Sequencing Method.. *Thyroid : official journal of the American Thyroid Association*. PMID: 26179797
5. Assessing the Immune Cell Subset and Genetic Mutations in Patients With Palindromic Rheumatism Seronegative for Rheumatoid Factor and Anti-Cyclic Citrullinated Peptide.. *Arthritis & rheumatology (Hoboken, N.J.)*. PMID: 35819819

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.0 |
| 高置信度残基 (pLDDT>90) 占比 | 30.7% |
| 置信残基 (pLDDT 70-90) 占比 | 46.2% |
| 中等置信 (pLDDT 50-70) 占比 | 13.5% |
| 低置信 (pLDDT<50) 占比 | 9.5% |
| 有序区域 (pLDDT>70) 占比 | 76.9% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=79.0，有序区 76.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050863, IPR004875, IPR009057, IPR006600, IPR007889; Pfam: PF04218, PF03184, PF03221 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CNTN5 | 0.691 | 0.000 | — |
| GINM1 | 0.518 | 0.000 | — |
| POGK | 0.500 | 0.000 | — |
| NAIF1 | 0.483 | 0.000 | — |
| ZNF514 | 0.418 | 0.000 | — |
| UBE2I | 0.416 | 0.417 | — |
| ZNF222 | 0.410 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Q81XD7 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| TIGD2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| CEP83 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| FANCD2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| LETMD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| DCAF10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| MKI67 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26949251|imex:IM-26415 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 7，IntAct interactions: 7
- 调控相关比例: 0 / 7 = 0%

**评价**: STRING 7 个预测互作，IntAct 7 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.0 + PDB: 无 | pLDDT=79.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Cytokinetic bridge | 一致 |
| PPI | STRING + IntAct | 7 + 7 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. JRKL — Jerky protein homolog-like，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小524 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y4A0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000183340-JRKL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=JRKL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y4A0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

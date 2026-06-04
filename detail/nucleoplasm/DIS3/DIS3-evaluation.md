---
type: protein-evaluation
gene: "DIS3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DIS3 — REJECTED (研究热度过高 (PubMed strict=235，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DIS3 |
| 蛋白名称 | Exosome complex exonuclease RRP44 |
| 蛋白大小 | 958 aa / 109.0 kDa |
| UniProt ID | Q9Y2L1 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/DIS3/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/rejected/DIS3/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm; Nucleus, nucleolus; Nucleus, nucleoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 958 aa / 109.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=235 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=85.9; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **82.5/180** | |
| **归一化总分** | | | **45.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus, nucleolus; Nucleus, nucleoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 235 |
| PubMed broad count | 286 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Ribonuclease DIS3 delays aging and senescence by generating tRNA halves.. *Nat Commun*. PMID: 42168172
2. RNA exosome component EXOSC10 variants identified in a patient with premature ovarian insufficiency†.. *Biol Reprod*. PMID: 41609100
3. Giardia duodenalis assemblage A: new genotype in non-human primates from the Brazilian Amazon region revealed by high-resolution MLST.. *Mem Inst Oswaldo Cruz*. PMID: 41880478
4. DIS3 mutations enhance AID-driven translocations during B-cell activation, promoting transformation to multiple myeloma.. *Nat Commun*. PMID: 41832173
5. DIS3 ribonuclease regulates Sertoli cell development to support spermatogenesis in mice.. *Development*. PMID: 41645813

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.9 |
| 高置信度残基 (pLDDT>90) 占比 | 52.1% |
| 置信残基 (pLDDT 70-90) 占比 | 35.4% |
| 中等置信 (pLDDT 50-70) 占比 | 9.1% |
| 低置信 (pLDDT<50) 占比 | 3.4% |
| 有序区域 (pLDDT>70) 占比 | 87.5% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/DIS3/DIS3-PAE.png]]

**评价**: AlphaFold 极高置信度预测（pLDDT=85.9，有序区 87.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EXOSC3 | 0.000 | 0.000 | — |
| EXOSC2 | 0.000 | 0.000 | — |
| EXOSC1 | 0.000 | 0.000 | — |
| EXOSC9 | 0.000 | 0.000 | — |
| EXOSC10 | 0.000 | 0.000 | — |
| EXOSC6 | 0.000 | 0.000 | — |
| EXOSC5 | 0.000 | 0.000 | — |
| EXOSC8 | 0.000 | 0.000 | — |
| EXOSC7 | 0.000 | 0.000 | — |
| EXOSC4 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q9VC93 | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9VZR0 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q9Y2L1 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q96B26 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q9WVE0 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q01780 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9NQT5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.9 + PDB: 无 | pLDDT=85.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus, nucleolus; Nucleus, nucleoplas / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DIS3 — Exosome complex exonuclease RRP44，研究基础较多，新颖性有限。
2. 蛋白大小958 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 235 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 235 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y2L1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000083520-DIS3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DIS3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y2L1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/DIS3/DIS3-PAE.png]]





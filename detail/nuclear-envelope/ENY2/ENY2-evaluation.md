---
type: protein-evaluation
gene: "ENY2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ENY2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ENY2 |
| 蛋白名称 | Transcription and mRNA export factor ENY2 |
| 蛋白大小 | 101 aa / 11.5 kDa |
| UniProt ID | Q9NPA8 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/ENY2/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/ENY2/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Mitochondria; UniProt: Nucleus, nucleoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 101 aa / 11.5 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=45 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=93.6; PDB: 4DHX |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR018783, IPR038212; Pfam: PF10163 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117.0/180** | |
| **归一化总分** | | | **65.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Mitochondria | Approved |
| UniProt | Nucleus, nucleoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- DUBm complex (GO:0071819)
- mitochondrion (GO:0005739)
- nuclear pore nuclear basket (GO:0044615)
- nucleoplasm (GO:0005654)
- SAGA complex (GO:0000124)
- transcription export complex 2 (GO:0070390)
- transcription factor TFTC complex (GO:0033276)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 45 |
| PubMed broad count | 69 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Sus1/ENY2: a multitasking protein in eukaryotic gene expression.. *Critical reviews in biochemistry and molecular biology*. PMID: 23057668
2. Highly conserved ENY2/Sus1 protein binds to Drosophila CTCF and is required for barrier activity.. *Epigenetics*. PMID: 25147918
3. Characterization of stem cell landscape and identification of stemness-related gene ENY2 in colorectal cancer by intergrated transcriptomic analysis.. *Global medical genetics*. PMID: 40735504
4. ENY2: couple, triple...more?. *Cell cycle (Georgetown, Tex.)*. PMID: 20090412
5. Zinc Finger Protein CG9890 - New Component of ENY2-Containing Complexes of Drosophila.. *Acta naturae*. PMID: 30713769

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.6 |
| 高置信度残基 (pLDDT>90) 占比 | 87.1% |
| 置信残基 (pLDDT 70-90) 占比 | 9.9% |
| 中等置信 (pLDDT 50-70) 占比 | 3.0% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 97.0% |
| 可用 PDB 条目 | 4DHX |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/ENY2/ENY2-PAE.png]]

**评价**: AlphaFold 极高置信度预测（pLDDT=93.6，有序区 97.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018783, IPR038212; Pfam: PF10163 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| USP22 | 0.999 | 0.942 | — |
| SGF29 | 0.999 | 0.950 | — |
| CETN3 | 0.999 | 0.949 | — |
| CETN2 | 0.999 | 0.636 | — |
| MCM3AP | 0.999 | 0.995 | — |
| ATXN7 | 0.999 | 0.895 | — |
| ATXN7-2 | 0.999 | 0.747 | — |
| PCID2 | 0.999 | 0.795 | — |
| ATXN7L3 | 0.999 | 0.964 | — |
| TRRAP | 0.998 | 0.976 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MCM3AP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| SGF11 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| USP22 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| NS1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:22810585|imex:IM-17331 |
| NS | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:22810585|imex:IM-17331 |
| EPB41L3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-20985|pubmed:24366813 |
| LYG1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| OASL | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| ATXN7L3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CSTPP1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.6 + PDB: 4DHX | pLDDT=93.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleoplasm / Nucleoplasm, Mitochondria | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. ENY2 — Transcription and mRNA export factor ENY2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小101 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 45 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NPA8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000120533-ENY2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ENY2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NPA8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-envelope/ENY2/ENY2-PAE.png]]





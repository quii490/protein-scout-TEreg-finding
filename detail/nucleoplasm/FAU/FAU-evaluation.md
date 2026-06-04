---
type: protein-evaluation
gene: "FAU"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAU 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAU |
| 蛋白名称 | Ubiquitin-like FUBI-ribosomal protein eS30 fusion protein |
| 蛋白大小 | 133 aa / 14.4 kDa |
| UniProt ID | P62861 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAU/IF_images/HEK293_1.jpg|HEK293]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAU/IF_images/PC-3_1.jpg|PC-3]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Endoplasmic reticulum, Cytosol; 额外: Nucleoli; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 133 aa / 14.4 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=90 篇 (≤100→2) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=91.0; PDB: 2L7R, 4UG0, 4V6X, 5A2Q, 5AJ0, 5FLX, 5OA3 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR039415, IPR006846, IPR000626, IPR029071, IPR019 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **104.0/180** | |
| **归一化总分** | | | **57.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum, Cytosol; 额外: Nucleoli | Enhanced |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- cytosolic ribosome (GO:0022626)
- cytosolic small ribosomal subunit (GO:0022627)
- extracellular space (GO:0005615)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- small ribosomal subunit (GO:0015935)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 90 |
| PubMed broad count | 11470 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Exercise Training Modulates Gut Microbiota Profile and Improves Endotoxemia.. *Medicine and science in sports and exercise*. PMID: 31425383
2. Functional and Structural Characterization of FAU Gene/Protein from Marine Sponge Suberites domuncula.. *Marine drugs*. PMID: 26198235
3. RNase W, a conserved ribonuclease family with a novel active site.. *Nucleic acids research*. PMID: 39445822
4. Genomic structure and expression of the human fau gene: encoding the ribosomal protein S30 fused to a ubiquitin-like protein.. *Biochemical and biophysical research communications*. PMID: 1326960
5. Expression cloning and characterization of a novel gene that encodes the RNA-binding protein FAU-1 from Pyrococcus furiosus.. *The Biochemical journal*. PMID: 12614195

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.0 |
| 高置信度残基 (pLDDT>90) 占比 | 76.7% |
| 置信残基 (pLDDT 70-90) 占比 | 18.8% |
| 中等置信 (pLDDT 50-70) 占比 | 4.5% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 95.5% |
| 可用 PDB 条目 | 2L7R, 4UG0, 4V6X, 5A2Q, 5AJ0, 5FLX, 5OA3, 5T2C, 6FEC, 6G18 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAU/FAU-PAE.png]]

**评价**: PDB实验结构（2L7R, 4UG0, 4V6X, 5A2Q, 5AJ0, 5FLX, 5OA3, 5T2C, 6FEC, 6G18）+ AlphaFold极高置信度预测（pLDDT=91.0），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039415, IPR006846, IPR000626, IPR029071, IPR019954; Pfam: PF04758, PF00240 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RPL17 | 0.999 | 0.993 | — |
| RPL23A | 0.999 | 0.994 | — |
| RPL8 | 0.999 | 0.993 | — |
| RPS20 | 0.999 | 0.993 | — |
| RPL10A | 0.999 | 0.993 | — |
| RPS25 | 0.999 | 0.995 | — |
| RPL26 | 0.999 | 0.993 | — |
| UBA52 | 0.999 | 0.993 | — |
| RPS6 | 0.999 | 0.996 | — |
| RPL37A | 0.999 | 0.993 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MAP3K14 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| COPS6 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| EIF1B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PINX1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| LYAR | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| GRB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15417|pubmed:21706016 |
| TAF7 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| GABARAP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| GABARAPL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| US11 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:22810585|imex:IM-17331 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.0 + PDB: 2L7R, 4UG0, 4V6X, 5A2Q, 5AJ0,  | pLDDT=91.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Endoplasmic reticulum, Cytosol; 额外: Nucleoli | 一致 |
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
1. FAU — Ubiquitin-like FUBI-ribosomal protein eS30 fusion protein，研究基础较多，新颖性有限。
2. 蛋白大小133 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 90 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P62861
- Protein Atlas: https://www.proteinatlas.org/ENSG00000149806-FAU/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAU
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P62861
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAU/FAU-PAE.png]]





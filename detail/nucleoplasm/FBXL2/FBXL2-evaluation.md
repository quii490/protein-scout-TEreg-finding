---
type: protein-evaluation
gene: "FBXL2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FBXL2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBXL2 / FBL2, FBL3 |
| 蛋白名称 | F-box/LRR-repeat protein 2 |
| 蛋白大小 | 423 aa / 47.1 kDa |
| UniProt ID | Q9UKC9 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FBXL2/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FBXL2/IF_images/HeLa_1.jpg|HeLa]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Plasma membrane; 额外: Nucleoplasm, Nucleoli; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 423 aa / 47.1 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=46 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=92.3; PDB: 6O60 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001810, IPR050648, IPR057207, IPR006553, IPR032 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 10 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **107.0/180** | |
| **归一化总分** | | | **59.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Nucleoplasm, Nucleoli | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- membrane (GO:0016020)
- SCF ubiquitin ligase complex (GO:0019005)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 46 |
| PubMed broad count | 61 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FBL2, FBL3 |

**关键文献**:
1. Palmitoylation and PDE6δ regulate membrane-compartment-specific substrate ubiquitylation and degradation.. *Cell reports*. PMID: 36662618
2. FBXL2 promotes E47 protein instability to inhibit breast cancer stemness and paclitaxel resistance.. *Oncogene*. PMID: 36460773
3. Role for the F-box proteins in heart diseases.. *Pharmacological research*. PMID: 39577754
4. Cross-Regulation of F-Box Protein FBXL2 with T-bet and TNF-α during Acute and Chronic Lung Allograft Rejection.. *Journal of immunology (Baltimore, Md. : 1950)*. PMID: 36113884
5. GGTase3 is a newly identified geranylgeranyltransferase targeting a ubiquitin ligase.. *Nature structural & molecular biology*. PMID: 31209342

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.3 |
| 高置信度残基 (pLDDT>90) 占比 | 81.6% |
| 置信残基 (pLDDT 70-90) 占比 | 10.9% |
| 中等置信 (pLDDT 50-70) 占比 | 4.0% |
| 低置信 (pLDDT<50) 占比 | 3.5% |
| 有序区域 (pLDDT>70) 占比 | 92.5% |
| 可用 PDB 条目 | 6O60 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FBXL2/FBXL2-PAE.png]]

**评价**: AlphaFold 极高置信度预测（pLDDT=92.3，有序区 92.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001810, IPR050648, IPR057207, IPR006553, IPR032675; Pfam: PF25372, PF12937 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SKP1 | 0.996 | 0.985 | — |
| RABGGTB | 0.970 | 0.926 | — |
| CUL1 | 0.946 | 0.836 | — |
| PTAR1 | 0.934 | 0.900 | — |
| PIK3R2 | 0.873 | 0.292 | — |
| FBXO3 | 0.860 | 0.510 | — |
| ITPR3 | 0.830 | 0.510 | — |
| FOXM1 | 0.681 | 0.625 | — |
| CCND2 | 0.678 | 0.331 | — |
| MARCHF7 | 0.664 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| COL7A1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| SKP1 | psi-mi:"MI:0231"(mammalian protein protein interac | pubmed:19159283|imex:IM-20301 |
| PPP1CC | psi-mi:"MI:0018"(two hybrid) | pubmed:21382349|imex:IM-17664 |
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| YPEL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YPEL3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HSPD1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| SUGT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:25036637|imex:IM-22301 |
| CCT5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| ENST00000484457 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 10
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 10 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.3 + PDB: 6O60 | pLDDT=92.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Membrane / Plasma membrane; 额外: Nucleoplasm, Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 10 interactions | 数据充分 |

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
1. FBXL2 — F-box/LRR-repeat protein 2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小423 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 46 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UKC9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000153558-FBXL2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBXL2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UKC9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FBXL2/FBXL2-PAE.png]]





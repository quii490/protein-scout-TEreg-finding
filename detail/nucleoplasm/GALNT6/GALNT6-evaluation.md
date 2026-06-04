---
type: protein-evaluation
gene: "GALNT6"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GALNT6 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GALNT6 |
| 蛋白名称 | Polypeptide N-acetylgalactosaminyltransferase 6 |
| 蛋白大小 | 622 aa / 71.2 kDa |
| UniProt ID | Q8NCL4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Golgi apparatus; UniProt: Golgi apparatus membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 622 aa / 71.2 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=45 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=88.7; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR045885, IPR001173, IPR029044, IPR035992, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.5/180** | |
| **归一化总分** | | | **65.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Golgi apparatus | Approved |
| UniProt | Golgi apparatus membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- Golgi apparatus (GO:0005794)
- Golgi membrane (GO:0000139)
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 45 |
| PubMed broad count | 68 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Crucial roles of GALNT6-mediated O-glycosylation of GRP78/Bip in proliferation of breast cancer cells.. *Biochemical and biophysical research communications*. PMID: 41197411
2. GALNT6, GALNT14, and Gal-3 in association with GDF-15 promotes drug resistance and stemness of breast cancer via β-catenin axis.. *Growth factors (Chur, Switzerland)*. PMID: 38889447
3. Single-Cell Transcriptomics Identifies Selective Lineage-Specific Regulation of Genes in Aortic Smooth Muscle Cells in Mice.. *Arteriosclerosis, thrombosis, and vascular biology*. PMID: 39744838
4. GALNT6 promotes invasion and metastasis of human lung adenocarcinoma cells through O-glycosylating chaperone protein GRP78.. *Cell death & disease*. PMID: 32393740
5. GALNT6 Promotes Tumorigenicity and Metastasis of Breast Cancer Cell via β-catenin/MUC1-C Signaling Pathway.. *International journal of biological sciences*. PMID: 30662357

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.7 |
| 高置信度残基 (pLDDT>90) 占比 | 77.0% |
| 置信残基 (pLDDT 70-90) 占比 | 10.6% |
| 中等置信 (pLDDT 50-70) 占比 | 4.5% |
| 低置信 (pLDDT<50) 占比 | 7.9% |
| 有序区域 (pLDDT>70) 占比 | 87.6% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=88.7，有序区 87.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045885, IPR001173, IPR029044, IPR035992, IPR000772; Pfam: PF00535, PF00652 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GCNT1 | 0.952 | 0.000 | — |
| ST6GALNAC1 | 0.950 | 0.000 | — |
| B3GNT6 | 0.940 | 0.000 | — |
| C1GALT1 | 0.904 | 0.000 | — |
| B4GALNT1 | 0.847 | 0.000 | — |
| C1GALT1C1 | 0.819 | 0.000 | — |
| MUC1 | 0.698 | 0.043 | — |
| C1GALT1C1L | 0.691 | 0.000 | — |
| FN1 | 0.572 | 0.000 | — |
| MUC4 | 0.547 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ALDOA | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| TMEM9 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| AK6 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| SLC5A6 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| RPL13 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| NDUFS4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NDUFB5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| B4GALT3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PLXNA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FAM20B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.7 + PDB: 无 | pLDDT=88.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus membrane / Nucleoplasm, Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. GALNT6 — Polypeptide N-acetylgalactosaminyltransferase 6，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小622 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 45 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NCL4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000139629-GALNT6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GALNT6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NCL4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

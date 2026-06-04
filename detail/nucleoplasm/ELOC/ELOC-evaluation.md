---
type: protein-evaluation
gene: "ELOC"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ELOC 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ELOC / TCEB1 |
| 蛋白名称 | Elongin-C |
| 蛋白大小 | 112 aa / 12.5 kDa |
| UniProt ID | Q15369 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles; 额外: Nucleoli, Cell Junctions; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 112 aa / 12.5 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=50 篇 (≤60→6) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=89.8; PDB: 1LM8, 1LQB, 1VCB, 2C9W, 2IZV, 2MA9, 3DCG |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR039948, IPR001232, IPR011333, IPR016073; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **124.0/180** | |
| **归一化总分** | | | **68.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nucleoli, Cell Junctions | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- Cul2-RING ubiquitin ligase complex (GO:0031462)
- Cul5-RING ubiquitin ligase complex (GO:0031466)
- cytosol (GO:0005829)
- elongin complex (GO:0070449)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 50 |
| PubMed broad count | 274 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TCEB1 |

**关键文献**:
1. USP51 facilitates colorectal cancer stemness and chemoresistance by forming a positive feed-forward loop with HIF1A.. *Cell death and differentiation*. PMID: 37816999
2. ELOC-Mutated Renal Cell Carcinoma is a Rare Indolent Tumor With Distinctive Genomic Characteristics.. *Modern pathology : an official journal of the United States and Canadian Academy of Pathology, Inc*. PMID: 40246078
3. Comprehensive Analysis of 15 Cases of ELOC -RCC and Identification of Novel Mutation Site.. *The American journal of surgical pathology*. PMID: 40557827
4. Biallelic ELOC-Inactivated Renal Cell Carcinoma: Molecular Features Supporting Classification as a Distinct Entity.. *Modern pathology : an official journal of the United States and Canadian Academy of Pathology, Inc*. PMID: 37088333
5. Elongin C (ELOC/TCEB1)-associated von Hippel-Lindau disease.. *Human molecular genetics*. PMID: 35323939

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.8 |
| 高置信度残基 (pLDDT>90) 占比 | 74.1% |
| 置信残基 (pLDDT 70-90) 占比 | 12.5% |
| 中等置信 (pLDDT 50-70) 占比 | 12.5% |
| 低置信 (pLDDT<50) 占比 | 0.9% |
| 有序区域 (pLDDT>70) 占比 | 86.6% |
| 可用 PDB 条目 | 1LM8, 1LQB, 1VCB, 2C9W, 2IZV, 2MA9, 3DCG, 3ZKJ, 3ZNG, 3ZRC |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1LM8, 1LQB, 1VCB, 2C9W, 2IZV, 2MA9, 3DCG, 3ZKJ, 3ZNG, 3ZRC）+ AlphaFold极高置信度预测（pLDDT=89.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039948, IPR001232, IPR011333, IPR016073; Pfam: PF03931 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL5 | 0.999 | 0.991 | — |
| RBX1 | 0.999 | 0.927 | — |
| CBFB | 0.999 | 0.959 | — |
| HIF1A | 0.999 | 0.969 | — |
| VHL | 0.999 | 0.999 | — |
| ELOB | 0.999 | 0.999 | — |
| ELOA | 0.999 | 0.898 | — |
| CUL2 | 0.999 | 0.997 | — |
| SOCS2 | 0.999 | 0.986 | — |
| RNF7 | 0.999 | 0.562 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ELOB | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:10205047 |
| MED8 | psi-mi:"MI:0018"(two hybrid) | pubmed:12149480 |
| RBX1 | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:12149480 |
| Dmel\CG4286 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Sms | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Grasp65 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| CC9 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| C1GalTA | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Rbp4 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Socs44A | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.8 + PDB: 1LM8, 1LQB, 1VCB, 2C9W, 2IZV,  | pLDDT=89.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Vesicles; 额外: Nucleoli, Cell Junctions | 一致 |
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
1. ELOC — Elongin-C，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小112 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 50 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q15369
- Protein Atlas: https://www.proteinatlas.org/ENSG00000154582-ELOC/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ELOC
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15369
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

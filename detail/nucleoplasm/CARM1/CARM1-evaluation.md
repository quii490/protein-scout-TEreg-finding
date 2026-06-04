---
type: protein-evaluation
gene: "CARM1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CARM1 — REJECTED (研究热度过高 (PubMed strict=402，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CARM1 / PRMT4 |
| 蛋白名称 | Histone-arginine methyltransferase CARM1 |
| 蛋白大小 | 608 aa / 65.9 kDa |
| UniProt ID | Q86X55 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm; Chromosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 608 aa / 65.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=402 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=78.2; PDB: 2Y1W, 2Y1X, 4IKP, 5DWQ, 5DX0, 5DX1, 5DX8 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR025799, IPR011993, IPR055135, IPR029063; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus; Cytoplasm; Chromosome | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nuclear replication fork (GO:0043596)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 402 |
| PubMed broad count | 549 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PRMT4 |

**关键文献**:
1. AMPK-dependent phosphorylation is required for transcriptional activation of TFEB and TFE3.. *Autophagy*. PMID: 33734022
2. CARM1 drives mitophagy and autophagy flux during fasting-induced skeletal muscle atrophy.. *Autophagy*. PMID: 38018843
3. Arginine methylation of PPP1CA by CARM1 regulates glucose metabolism and affects osteogenic differentiation and osteoclastic differentiation.. *Clinical and translational medicine*. PMID: 37649137
4. Identification of Five Hub Genes Based on Single-Cell RNA Sequencing Data and Network Pharmacology in Patients With Acute Myocardial Infarction.. *Frontiers in public health*. PMID: 35757636
5. Cyclic helix B peptide alleviates proinflammatory cell death and improves functional recovery after traumatic spinal cord injury.. *Redox biology*. PMID: 37290302

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.2 |
| 高置信度残基 (pLDDT>90) 占比 | 57.1% |
| 置信残基 (pLDDT 70-90) 占比 | 16.0% |
| 中等置信 (pLDDT 50-70) 占比 | 3.5% |
| 低置信 (pLDDT<50) 占比 | 23.5% |
| 有序区域 (pLDDT>70) 占比 | 73.1% |
| 可用 PDB 条目 | 2Y1W, 2Y1X, 4IKP, 5DWQ, 5DX0, 5DX1, 5DX8, 5DXA, 5DXJ, 5U4X |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2Y1W, 2Y1X, 4IKP, 5DWQ, 5DX0, 5DX1, 5DX8, 5DXA, 5DXJ, 5U4X）+ AlphaFold极高置信度预测（pLDDT=78.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR025799, IPR011993, IPR055135, IPR029063; Pfam: PF11531, PF06325, PF22528 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EP300 | 0.999 | 0.842 | — |
| NCOA3 | 0.997 | 0.826 | — |
| H3C13 | 0.994 | 0.923 | — |
| H3C12 | 0.994 | 0.917 | — |
| NCOA2 | 0.994 | 0.547 | — |
| PRMT1 | 0.982 | 0.225 | — |
| H3C1 | 0.982 | 0.981 | — |
| CREBBP | 0.981 | 0.749 | — |
| H3-2 | 0.978 | 0.923 | — |
| NCOA1 | 0.976 | 0.528 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Creb1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-14479|pubmed:16330542 |
| EP300 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| GABARAPL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| MAP1LC3B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| GABARAPL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| ORF | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-17346|pubmed:22190034| |
| UBE2D4 | psi-mi:"MI:0018"(two hybrid) | imex:IM-11696|pubmed:19549727 |
| TP63 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20085233|imex:IM-20439 |
| IRF4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21903422|imex:IM-17322 |
| CUL5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.2 + PDB: 2Y1W, 2Y1X, 4IKP, 5DWQ, 5DX0,  | pLDDT=78.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Chromosome / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CARM1 — Histone-arginine methyltransferase CARM1，研究基础较多，新颖性有限。
2. 蛋白大小608 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 402 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 402 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86X55
- Protein Atlas: https://www.proteinatlas.org/ENSG00000142453-CARM1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CARM1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86X55
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

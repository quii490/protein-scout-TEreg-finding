---
type: protein-evaluation
gene: "GINS1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GINS1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GINS1 / KIAA0186, PSF1 |
| 蛋白名称 | DNA replication complex GINS protein PSF1 |
| 蛋白大小 | 196 aa / 23.0 kDa |
| UniProt ID | Q14691 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Chromosome |
| 蛋白大小 | 8/10 | ×1 | 8 | 196 aa / 23.0 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=58 篇 (≤60→6) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=93.0; PDB: 2E9X, 2EHO, 2Q9Q, 6XTX, 6XTY, 7PFO, 7PLO |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR021151, IPR036224, IPR005339, IPR056783; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **124.0/180** | |
| **归一化总分** | | | **68.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus; Chromosome | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- CMG complex (GO:0071162)
- cytoplasm (GO:0005737)
- GINS complex (GO:0000811)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 58 |
| PubMed broad count | 96 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0186, PSF1 |

**关键文献**:
1. PAX5 and circ1857 affected DLBCL progression and B-cell proliferation through regulating GINS1.. *Cancer science*. PMID: 37221950
2. OTU deubiquitinase, ubiquitin aldehyde binding 2  (OTUB2) modulates the stemness feature, chemoresistance, and epithelial-mesenchymal transition of colon cancer via regulating GINS complex subunit 1 (GINS1) expression.. *Cell communication and signaling : CCS*. PMID: 39210373
3. FOXP1-GINS1 axis promotes DLBCL proliferation and directs doxorubicin resistance.. *Journal of Cancer*. PMID: 37576391
4. Roles of DSCC1 and GINS1 in gastric cancer.. *Medicine*. PMID: 37904396
5. GINS1 promotes the proliferation and migration of glioma cells through USP15-mediated deubiquitination of TOP2A.. *iScience*. PMID: 36065190

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.0 |
| 高置信度残基 (pLDDT>90) 占比 | 75.5% |
| 置信残基 (pLDDT 70-90) 占比 | 24.0% |
| 中等置信 (pLDDT 50-70) 占比 | 0.5% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 99.5% |
| 可用 PDB 条目 | 2E9X, 2EHO, 2Q9Q, 6XTX, 6XTY, 7PFO, 7PLO, 8B9D, 8OK2, 9E2Z |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2E9X, 2EHO, 2Q9Q, 6XTX, 6XTY, 7PFO, 7PLO, 8B9D, 8OK2, 9E2Z）+ AlphaFold极高置信度预测（pLDDT=93.0），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR021151, IPR036224, IPR005339, IPR056783; Pfam: PF24997, PF05916 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GINS3 | 0.999 | 0.997 | — |
| CDC45 | 0.999 | 0.996 | — |
| MCM3 | 0.999 | 0.991 | — |
| GINS2 | 0.999 | 0.999 | — |
| MCM2 | 0.999 | 0.991 | — |
| MCM7 | 0.999 | 0.995 | — |
| MCM5 | 0.999 | 0.994 | — |
| GINS4 | 0.999 | 0.997 | — |
| MCM4 | 0.999 | 0.991 | — |
| MCM6 | 0.998 | 0.988 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CENATAC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CSNK1G2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GTF2E2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TIPIN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GINS3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MCM7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PTP4A1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MCM5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| GINS4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| DNAJB3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.0 + PDB: 2E9X, 2EHO, 2Q9Q, 6XTX, 6XTY,  | pLDDT=93.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome / Nucleoplasm | 一致 |
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
1. GINS1 — DNA replication complex GINS protein PSF1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小196 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 58 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q14691
- Protein Atlas: https://www.proteinatlas.org/ENSG00000101003-GINS1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GINS1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14691
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

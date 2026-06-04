---
type: protein-evaluation
gene: "CMC2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CMC2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CMC2 / C16orf61 |
| 蛋白名称 | COX assembly mitochondrial protein 2 homolog |
| 蛋白大小 | 79 aa / 9.5 kDa |
| UniProt ID | Q9NRP2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Mitochondria; 额外: Cytosol; UniProt: Mitochondrion |
| 蛋白大小 | 5/10 | ×1 | 5 | 79 aa / 9.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=17 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=91.6; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR013892; Pfam: PF08583 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 14 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.5/180** | |
| **归一化总分** | | | **63.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria; 额外: Cytosol | Supported |
| UniProt | Mitochondrion | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- mitochondrion (GO:0005739)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17 |
| PubMed broad count | 218 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C16orf61 |

**关键文献**:
1. The conserved mitochondrial twin Cx9C protein Cmc2 Is a Cmc1 homologue essential for cytochrome c oxidase biogenesis.. *The Journal of biological chemistry*. PMID: 20220131
2. Dose-response assessment of chemically modified curcumin in experimental periodontitis.. *Journal of periodontology*. PMID: 30394523
3. Chemically modified curcumin (CMC2.24) alleviates osteoarthritis progression by restoring cartilage homeostasis and inhibiting chondrocyte apoptosis via the NF-κB/HIF-2α axis.. *Journal of molecular medicine (Berlin, Germany)*. PMID: 32860098
4. Cloning and transcription analysis of the Aspergillus aculeatus No. F-50 endoglucanase 2 (cmc2) gene.. *Journal of bioscience and bioengineering*. PMID: 16233338
5. Novel Chemically Modified Curcumin (CMC) Analogs Exhibit Anti-Melanogenic Activity in Primary Human Melanocytes.. *International journal of molecular sciences*. PMID: 34205035

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.6 |
| 高置信度残基 (pLDDT>90) 占比 | 86.1% |
| 置信残基 (pLDDT 70-90) 占比 | 5.1% |
| 中等置信 (pLDDT 50-70) 占比 | 7.6% |
| 低置信 (pLDDT<50) 占比 | 1.3% |
| 有序区域 (pLDDT>70) 占比 | 91.2% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=91.6，有序区 91.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013892; Pfam: PF08583 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PROCR | 0.928 | 0.000 | — |
| NSL1 | 0.876 | 0.000 | — |
| CMC4 | 0.831 | 0.000 | — |
| ICAM1 | 0.823 | 0.000 | — |
| COA4 | 0.776 | 0.000 | — |
| CHCHD7 | 0.744 | 0.000 | — |
| COX19 | 0.727 | 0.000 | — |
| COA6 | 0.703 | 0.000 | — |
| COX17 | 0.682 | 0.000 | — |
| AWAT2 | 0.666 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| pcu4 | psi-mi:"MI:0018"(two hybrid) | pubmed:16157682|imex:IM-19856 |
| raf2 | psi-mi:"MI:0096"(pull down) | imex:IM-13771|pubmed:20211136 |
| raf1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-13771|pubmed:20211136 |
| PLGRKT | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| SCO1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| SFXN1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| COQ9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| FAM136A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| COQ5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| C1orf216 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 14
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 14 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.6 + PDB: 无 | pLDDT=91.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Mitochondrion / Mitochondria; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 14 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CMC2 — COX assembly mitochondrial protein 2 homolog，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小79 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 17 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NRP2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000103121-CMC2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CMC2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NRP2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

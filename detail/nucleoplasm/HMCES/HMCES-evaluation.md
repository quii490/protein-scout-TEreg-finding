---
type: protein-evaluation
gene: "HMCES"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HMCES 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HMCES / C3orf37, DC12, SRAPD1 |
| 蛋白名称 | Abasic site processing protein HMCES |
| 蛋白大小 | 354 aa / 40.6 kDa |
| UniProt ID | Q96FZ2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Chromosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 354 aa / 40.6 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=29 篇 (≤40→8) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=82.5; PDB: 5KO9, 6OE7, 6OEA, 6OEB, 6OOV |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR003738, IPR036590; Pfam: PF02586 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **136.0/180** | |
| **归一化总分** | | | **75.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Chromosome | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- replication fork (GO:0005657)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 29 |
| PubMed broad count | 38 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C3orf37, DC12, SRAPD1 |

**关键文献**:
1. Integrating machine learning and multi-omics analysis to reveal nucleotide metabolism-related immune genes and their functional validation in ischemic stroke.. *Frontiers in immunology*. PMID: 40207230
2. HMCES Maintains Genome Integrity by Shielding Abasic Sites in Single-Strand DNA.. *Cell*. PMID: 30554877
3. Self-reversal facilitates the resolution of HMCES DNA-protein crosslinks in cells.. *Cell reports*. PMID: 37950866
4. Celastrol induces DNA damage and cell death in BCR-ABL T315I-mutant CML by targeting YY1 and HMCES.. *Phytomedicine : international journal of phytotherapy and phytopharmacology*. PMID: 39255723
5. HMCES corrupts replication fork stability during base excision repair in homologous recombination-deficient cells.. *Science advances*. PMID: 40138423

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.5 |
| 高置信度残基 (pLDDT>90) 占比 | 68.9% |
| 置信残基 (pLDDT 70-90) 占比 | 4.0% |
| 中等置信 (pLDDT 50-70) 占比 | 7.6% |
| 低置信 (pLDDT<50) 占比 | 19.5% |
| 有序区域 (pLDDT>70) 占比 | 72.9% |
| 可用 PDB 条目 | 5KO9, 6OE7, 6OEA, 6OEB, 6OOV |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（5KO9, 6OE7, 6OEA, 6OEB, 6OOV）+ AlphaFold极高置信度预测（pLDDT=82.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003738, IPR036590; Pfam: PF02586 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SPRTN | 0.680 | 0.000 | — |
| RPA2 | 0.558 | 0.485 | — |
| RNF208 | 0.541 | 0.000 | — |
| RFWD3 | 0.522 | 0.000 | — |
| STPG1 | 0.507 | 0.000 | — |
| RPA4 | 0.504 | 0.492 | — |
| TSR2 | 0.473 | 0.000 | — |
| TRAIP | 0.452 | 0.000 | — |
| IMP3 | 0.450 | 0.000 | — |
| SMARCAL1 | 0.449 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| SRPK2 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:23602568|imex:IM-17935 |
| KLHDC3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HSPA8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HSPBP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RPA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RPA4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EBI-8874509 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:24267889|imex:IM-21754 |
| PLK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Kifc5b | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.5 + PDB: 5KO9, 6OE7, 6OEA, 6OEB, 6OOV | pLDDT=82.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Chromosome / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. HMCES — Abasic site processing protein HMCES，非常新颖，仅有少数基础研究。
2. 蛋白大小354 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 29 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96FZ2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000183624-HMCES/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HMCES
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96FZ2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/HMCES/IF_images/A-431_1.jpg]]
![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/HMCES/IF_images/U-251MG_1.jpg]]


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/HMCES/HMCES-PAE.png]]

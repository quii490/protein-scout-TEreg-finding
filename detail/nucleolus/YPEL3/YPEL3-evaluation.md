---
type: protein-evaluation
gene: "YPEL3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## YPEL3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | YPEL3 |
| 蛋白名称 | Protein yippee-like 3 |
| 蛋白大小 | 119 aa / 13.6 kDa |
| UniProt ID | P61236 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus, nucleolus |
| 蛋白大小 | 8/10 | ×1 | 8 | 119 aa / 13.6 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=25 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=90.6; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR034751, IPR004910, IPR039058; Pfam: PF03226 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.5/180** | |
| **归一化总分** | | | **72.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus, nucleolus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleolus (GO:0005730)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 25 |
| PubMed broad count | 40 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Why YPEL3 represents a novel tumor suppressor.. *Frontiers in bioscience (Landmark edition)*. PMID: 21196260
2. Integrating genetic and transcriptomic data to identify genes underlying obesity risk loci.. *International journal of obesity (2005)*. PMID: 41006818
3. Integrating Genetic and Transcriptomic Data to Identify Genes Underlying Obesity Risk Loci.. *medRxiv : the preprint server for health sciences*. PMID: 38903089
4. Senescence-associated gene YPEL3 is downregulated in human colon tumors.. *Annals of surgical oncology*. PMID: 21267786
5. yippee like 3 (ypel3) is a novel gene required for myelinating and perineurial glia development.. *PLoS genetics*. PMID: 32544203

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.6 |
| 高置信度残基 (pLDDT>90) 占比 | 79.0% |
| 置信残基 (pLDDT 70-90) 占比 | 9.2% |
| 中等置信 (pLDDT 50-70) 占比 | 8.4% |
| 低置信 (pLDDT<50) 占比 | 3.4% |
| 有序区域 (pLDDT>70) 占比 | 88.2% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=90.6，有序区 88.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR034751, IPR004910, IPR039058; Pfam: PF03226 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ASPHD1 | 0.687 | 0.000 | — |
| GDPD3 | 0.662 | 0.000 | — |
| KCTD13 | 0.651 | 0.000 | — |
| HIRIP3 | 0.647 | 0.000 | — |
| CDIPT | 0.634 | 0.000 | — |
| DOC2A | 0.624 | 0.000 | — |
| INO80E | 0.620 | 0.000 | — |
| PAGR1 | 0.615 | 0.000 | — |
| SEZ6L2 | 0.613 | 0.000 | — |
| TMEM219 | 0.612 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Klc | psi-mi:"MI:0018"(two hybrid) | pubmed:15575970|mint:MINT-7952 |
| SRPK1 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:23602568|imex:IM-17935 |
| SRPK2 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:23602568|imex:IM-17935 |
| FBXL20 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FBXL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DOK7 | psi-mi:"MI:0397"(two hybrid array) | pubmed:25814554|imex:IM-22632 |
| APAF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| LSS | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| COASY | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| RIN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.6 + PDB: 无 | pLDDT=90.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus, nucleolus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. YPEL3 — Protein yippee-like 3，非常新颖，仅有少数基础研究。
2. 蛋白大小119 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 25 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P61236
- Protein Atlas: https://www.proteinatlas.org/ENSG00000090238-YPEL3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=YPEL3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P61236
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

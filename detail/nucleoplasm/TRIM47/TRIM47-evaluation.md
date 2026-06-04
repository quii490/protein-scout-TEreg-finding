---
type: protein-evaluation
gene: "TRIM47"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TRIM47 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TRIM47 / GOA, RNF100 |
| 蛋白名称 | E3 ubiquitin-protein ligase TRIM47 |
| 蛋白大小 | 638 aa / 69.5 kDa |
| UniProt ID | Q96LD4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 638 aa / 69.5 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=57 篇 (≤60→6) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=81.0; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001870, IPR043136, IPR013320, IPR051051, IPR042 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **115.5/180** | |
| **归一化总分** | | | **64.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- glutamatergic synapse (GO:0098978)
- nucleus (GO:0005634)
- postsynapse (GO:0098794)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 57 |
| PubMed broad count | 80 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GOA, RNF100 |

**关键文献**:
1. TRIM47 is a novel endothelial activation factor that aggravates lipopolysaccharide-induced acute lung injury in mice via K63-linked ubiquitination of TRAF2.. *Signal transduction and targeted therapy*. PMID: 35513381
2. TRIM47-CDO1 axis dictates hepatocellular carcinoma progression by modulating ferroptotic cell death through the ubiquitin‒proteasome system.. *Free radical biology & medicine*. PMID: 38614226
3. TRIM47 drives gastric cancer cell proliferation and invasion by regulating CYLD protein stability.. *Biology direct*. PMID: 39516831
4. ADAM17 variant causes hair loss via ubiquitin ligase TRIM47-mediated degradation.. *JCI insight*. PMID: 38771644
5. Trim47 prevents hematopoietic stem cell exhaustion during stress by regulating MAVS-mediated innate immune pathway.. *Nature communications*. PMID: 39117713

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.0 |
| 高置信度残基 (pLDDT>90) 占比 | 53.6% |
| 置信残基 (pLDDT 70-90) 占比 | 26.2% |
| 中等置信 (pLDDT 50-70) 占比 | 5.3% |
| 低置信 (pLDDT<50) 占比 | 14.9% |
| 有序区域 (pLDDT>70) 占比 | 79.8% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=81.0，有序区 79.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001870, IPR043136, IPR013320, IPR051051, IPR042780; Pfam: PF25600, PF00643, PF13445 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SATB1 | 0.676 | 0.676 | — |
| MRPL38 | 0.671 | 0.000 | — |
| TRIM59 | 0.667 | 0.000 | — |
| WBP2 | 0.651 | 0.000 | — |
| BBOX1 | 0.625 | 0.000 | — |
| TRIM66 | 0.622 | 0.000 | — |
| NUDCD1 | 0.619 | 0.619 | — |
| FBF1 | 0.597 | 0.000 | — |
| SATB2 | 0.591 | 0.591 | — |
| TRAT1 | 0.576 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-28987808 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| UBE2U | psi-mi:"MI:0397"(two hybrid array) | imex:IM-9597|pubmed:19690564 |
| citT3 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| dinG | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| TRIM8 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15696|pubmed:22493164 |
| ERBB4 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| FGFR4 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| KIT | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| MRFAP1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| KLHL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.0 + PDB: 无 | pLDDT=81.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Cytosol | 一致 |
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
1. TRIM47 — E3 ubiquitin-protein ligase TRIM47，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小638 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 57 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96LD4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000132481-TRIM47/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TRIM47
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96LD4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TRIM47/TRIM47-PAE.png]]

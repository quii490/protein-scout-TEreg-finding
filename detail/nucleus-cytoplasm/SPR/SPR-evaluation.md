---
type: protein-evaluation
gene: "SPR"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SPR — REJECTED (研究热度过高 (PubMed strict=4924，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SPR |
| 蛋白名称 | Sepiapterin reductase |
| 蛋白大小 | 261 aa / 28.0 kDa |
| UniProt ID | P35270 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 261 aa / 28.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=4924 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=96.7; PDB: 1Z6Z, 4HWK, 4J7U, 4J7X, 4XWY, 4Z3K, 6I6C |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR051721, IPR036291, IPR002347, IPR006393; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Supported |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- mitochondrion (GO:0005739)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4924 |
| PubMed broad count | 16544 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Protein-Protein Interactions: Surface Plasmon Resonance.. *Methods in molecular biology (Clifton, N.J.)*. PMID: 28667619
2. Characterization of Small Molecule-Protein Interactions Using SPR Method.. *Methods in molecular biology (Clifton, N.J.)*. PMID: 37450146
3. Developments in SPR Fragment Screening.. *Expert opinion on drug discovery*. PMID: 26948323
4. Bio-sensing of organophosphorus pesticides: A review.. *Biosensors & bioelectronics*. PMID: 31153016
5. Fragment screening by SPR and advanced application to GPCRs.. *Progress in biophysics and molecular biology*. PMID: 25301577

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 96.7 |
| 高置信度残基 (pLDDT>90) 占比 | 95.8% |
| 置信残基 (pLDDT 70-90) 占比 | 3.4% |
| 中等置信 (pLDDT 50-70) 占比 | 0.0% |
| 低置信 (pLDDT<50) 占比 | 0.8% |
| 有序区域 (pLDDT>70) 占比 | 99.2% |
| 可用 PDB 条目 | 1Z6Z, 4HWK, 4J7U, 4J7X, 4XWY, 4Z3K, 6I6C, 6I6F, 6I6P, 6I6T |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1Z6Z, 4HWK, 4J7U, 4J7X, 4XWY, 4Z3K, 6I6C, 6I6F, 6I6P, 6I6T）+ AlphaFold极高置信度预测（pLDDT=96.7），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051721, IPR036291, IPR002347, IPR006393; Pfam: PF00106 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| QDPR | 0.989 | 0.226 | — |
| DHFR2 | 0.985 | 0.000 | — |
| PTS | 0.985 | 0.000 | — |
| DHFR | 0.982 | 0.000 | — |
| PAH | 0.981 | 0.000 | — |
| CBR1 | 0.974 | 0.000 | — |
| AKR1B1 | 0.974 | 0.045 | — |
| TH | 0.969 | 0.000 | — |
| TPH1 | 0.948 | 0.000 | — |
| TPH2 | 0.947 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| mepS | psi-mi:"MI:0096"(pull down) | pubmed:16606699 |
| lexA | psi-mi:"MI:0397"(two hybrid array) | pubmed:24561554|imex:IM-22059 |
| Kcnma1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-9475|pubmed:19423573 |
| GSTM1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| RNF31 | psi-mi:"MI:2289"(virotrap) | pubmed:30561431|imex:IM-26500 |
| BCAP31 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| 708601" | psi-mi:"MI:0096"(pull down) | pubmed:24189400|imex:IM-21413 |
| FGB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| quuQ | psi-mi:"MI:0397"(two hybrid array) | pubmed:24561554|imex:IM-22059 |
| chbR | psi-mi:"MI:0397"(two hybrid array) | pubmed:24561554|imex:IM-22059 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=96.7 + PDB: 1Z6Z, 4HWK, 4J7U, 4J7X, 4XWY,  | pLDDT=96.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm, Cytosol | 一致 |
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
1. SPR — Sepiapterin reductase，研究基础较多，新颖性有限。
2. 蛋白大小261 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4924 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 4924 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P35270
- Protein Atlas: https://www.proteinatlas.org/ENSG00000116096-SPR/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SPR
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P35270
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

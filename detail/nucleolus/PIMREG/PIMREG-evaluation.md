---
type: protein-evaluation
gene: "PIMREG"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PIMREG 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PIMREG / CATS, FAM64A, RCS1 |
| 蛋白名称 | Protein PIMREG |
| 蛋白大小 | 248 aa / 27.5 kDa |
| UniProt ID | Q9BSJ6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus; Nucleus, nucleolus |
| 蛋白大小 | 10/10 | ×1 | 10 | 248 aa / 27.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR009932; Pfam: PF07326 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.0/180** | |
| **归一化总分** | | | **76.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus; Nucleus, nucleolus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 39 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CATS, FAM64A, RCS1 |

**关键文献**:
1. SOD1-high fibroblasts derived exosomal miR-3960 promotes cisplatin resistance in triple-negative breast cancer by suppressing BRSK2-mediated phosphorylation of PIMREG.. *Cancer letters*. PMID: 38582395
2. PIMREG modulation of PI3K/Akt pathway enhances sorafenib resistance in Huh7 cells.. *Arab journal of gastroenterology : the official publication of the Pan-Arab Association of Gastroenterology*. PMID: 40582902
3. PIMREG, a Marker of Proliferation, Facilitates Aggressive Development of Cholangiocarcinoma Cells Partly Through Regulating Cell Cycle-Related Markers.. *Technology in cancer research & treatment*. PMID: 33356974
4. Sex-specific alteration in human muscle transcriptome with age.. *GeroScience*. PMID: 37106281
5. Identification of PIMREG as a novel prognostic signature in breast cancer via integrated bioinformatics analysis and experimental validation.. *PeerJ*. PMID: 37483962

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.5 |
| 高置信度残基 (pLDDT>90) 占比 | 8.1% |
| 置信残基 (pLDDT 70-90) 占比 | 12.9% |
| 中等置信 (pLDDT 50-70) 占比 | 51.6% |
| 低置信 (pLDDT<50) 占比 | 27.4% |
| 有序区域 (pLDDT>70) 占比 | 21.0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=60.5），有序残基占 21.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009932; Pfam: PF07326 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CENPA | 0.863 | 0.000 | — |
| CDCA3 | 0.834 | 0.000 | — |
| KIF20A | 0.829 | 0.000 | — |
| BUB1 | 0.790 | 0.000 | — |
| CCNB2 | 0.754 | 0.000 | — |
| CDK1 | 0.748 | 0.000 | — |
| AURKB | 0.737 | 0.000 | — |
| CDC20 | 0.734 | 0.091 | — |
| DLGAP5 | 0.726 | 0.000 | — |
| TDRD7 | 0.721 | 0.721 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PRNP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:18482256|imex:IM-19010 |
| TDRD7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZYG11B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CSNK2B | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| EMD | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ARMC7 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CCNDBP1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| TRIM27 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| TFCP2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| KRT40 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.5 + PDB: 无 | pLDDT=60.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, nucleolus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. PIMREG — Protein PIMREG，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小248 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=60.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BSJ6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000129195-PIMREG/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PIMREG
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BSJ6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

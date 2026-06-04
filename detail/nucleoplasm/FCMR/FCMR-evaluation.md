---
type: protein-evaluation
gene: "FCMR"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FCMR 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FCMR / FAIM3, TOSO |
| 蛋白名称 | Immunoglobulin mu Fc receptor |
| 蛋白大小 | 390 aa / 43.1 kDa |
| UniProt ID | O60667 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Plasma membrane; 额外: Golgi apparatus, Centrosom; UniProt: Cell membrane; Early endosome membrane; Golgi apparatus, tra |
| 蛋白大小 | 10/10 | ×1 | 10 | 390 aa / 43.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.9; PDB: 7YSG, 7YTC, 7YTD, 7YTE, 8BPE, 8BPF, 8BPG |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050671, IPR036179, IPR013783, IPR003599, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.5/180** | |
| **归一化总分** | | | **73.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Plasma membrane; 额外: Golgi apparatus, Centrosome | Approved |
| UniProt | Cell membrane; Early endosome membrane; Golgi apparatus, trans-Golgi network membrane; Lysosome memb... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centrosome (GO:0005813)
- early endosome membrane (GO:0031901)
- extracellular region (GO:0005576)
- Golgi apparatus (GO:0005794)
- lysosomal membrane (GO:0005765)
- nucleoplasm (GO:0005654)
- plasma membrane (GO:0005886)
- trans-Golgi network membrane (GO:0032588)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 91 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FAIM3, TOSO |

**关键文献**:
1. TGIF2 promotes cervical cancer metastasis by negatively regulating FCMR.. *European review for medical and pharmacological sciences*. PMID: 32572908
2. Enhanced Mott cell formation linked with IgM Fc receptor (FcμR) deficiency.. *European journal of immunology*. PMID: 37098762
3. Overexpression of Fc mu receptor (FCMR, TOSO) gene in chronic lymphocytic leukemia patients.. *Medical oncology (Northwood, London, England)*. PMID: 21264533
4. Functional Roles of the IgM Fc Receptor in the Immune System.. *Frontiers in immunology*. PMID: 31130948
5. Fcμ receptor as a Costimulatory Molecule for T Cells.. *Cell reports*. PMID: 30840890

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.9 |
| 高置信度残基 (pLDDT>90) 占比 | 30.8% |
| 置信残基 (pLDDT 70-90) 占比 | 8.5% |
| 中等置信 (pLDDT 50-70) 占比 | 19.0% |
| 低置信 (pLDDT<50) 占比 | 41.8% |
| 有序区域 (pLDDT>70) 占比 | 39.3% |
| 可用 PDB 条目 | 7YSG, 7YTC, 7YTD, 7YTE, 8BPE, 8BPF, 8BPG |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=64.9），有序残基占 39.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050671, IPR036179, IPR013783, IPR003599, IPR013106; Pfam: PF07686 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CD19 | 0.736 | 0.000 | — |
| FCRLA | 0.645 | 0.071 | — |
| VPREB3 | 0.615 | 0.067 | — |
| MS4A1 | 0.582 | 0.000 | — |
| CD22 | 0.581 | 0.071 | — |
| CD79B | 0.566 | 0.000 | — |
| CFLAR | 0.556 | 0.000 | — |
| CD79A | 0.550 | 0.000 | — |
| JCHAIN | 0.529 | 0.124 | — |
| CCR7 | 0.526 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| eno | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ANKRD2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| HOXD9 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| ZNHIT3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.9 + PDB: 7YSG, 7YTC, 7YTD, 7YTE, 8BPE,  | pLDDT=64.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane; Early endosome membrane; Golgi appa / Nucleoplasm, Plasma membrane; 额外: Golgi apparatus, | 一致 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FCMR — Immunoglobulin mu Fc receptor，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小390 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=64.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O60667
- Protein Atlas: https://www.proteinatlas.org/ENSG00000162894-FCMR/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FCMR
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60667
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

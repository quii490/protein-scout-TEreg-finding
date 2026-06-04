---
type: protein-evaluation
gene: "BANP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BANP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BANP / BEND1, SMAR1 |
| 蛋白名称 | Protein BANP |
| 蛋白大小 | 519 aa / 56.5 kDa |
| UniProt ID | Q8N9N5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nuclear bodies; UniProt: Nucleus; Nucleus speckle; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 519 aa / 56.5 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=41 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=53.6; PDB: 7YUG, 7YUK, 8HTX, 8YZT |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR042343, IPR018379; Pfam: PF10523 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.5/180** | |
| **归一化总分** | | | **61.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear bodies | Supported |
| UniProt | Nucleus; Nucleus speckle; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nuclear body (GO:0016604)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 41 |
| PubMed broad count | 119 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BEND1, SMAR1 |

**关键文献**:
1. ZNF471 Interacts with BANP to Reduce Tumour Malignancy by Inactivating PI3K/AKT/mTOR Signalling but is Frequently Silenced by Aberrant Promoter Methylation in Renal Cell Carcinoma.. *International journal of biological sciences*. PMID: 38169650
2. BANP opens chromatin and activates CpG-island-regulated genes.. *Nature*. PMID: 34234345
3. Genome access is transcription factor-specific and defined by nucleosome position.. *Molecular cell*. PMID: 39208807
4. Banp regulates DNA damage response and chromosome segregation during the cell cycle in zebrafish retina.. *eLife*. PMID: 35942692
5. Identification and molecular analysis of BANP.. *Gene*. PMID: 10940556

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 53.6 |
| 高置信度残基 (pLDDT>90) 占比 | 20.6% |
| 置信残基 (pLDDT 70-90) 占比 | 9.8% |
| 中等置信 (pLDDT 50-70) 占比 | 4.2% |
| 低置信 (pLDDT<50) 占比 | 65.3% |
| 有序区域 (pLDDT>70) 占比 | 30.4% |
| 可用 PDB 条目 | 7YUG, 7YUK, 8HTX, 8YZT |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=53.6），有序残基占 30.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR042343, IPR018379; Pfam: PF10523 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HDAC1 | 0.960 | 0.510 | — |
| TP53 | 0.944 | 0.625 | — |
| SETMAR | 0.896 | 0.000 | — |
| MDM2 | 0.813 | 0.510 | — |
| PRPF19 | 0.811 | 0.000 | — |
| CUX1 | 0.741 | 0.000 | — |
| CTNNB1 | 0.737 | 0.000 | — |
| FARS2 | 0.594 | 0.591 | — |
| HDAC6 | 0.578 | 0.510 | — |
| ZNF469 | 0.571 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000347125.4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ENSP00000376902.1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| ENSP00000431812.1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:26871637|imex:IM-25013| |
| ENSP00000444352.1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:26871637|imex:IM-25013| |
| ENSP00000515015.1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:26871637|imex:IM-25013| |
| EBI-16429704 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:26871637|imex:IM-25013| |
| Blnk | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| TRAF2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| FOXM1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| NS | psi-mi:"MI:0018"(two hybrid) | imex:IM-13585|pubmed:20064372 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=53.6 + PDB: 7YUG, 7YUK, 8HTX, 8YZT | pLDDT=53.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus speckle; Cytoplasm / Nucleoplasm; 额外: Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. BANP — Protein BANP，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小519 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 41 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=53.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N9N5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000172530-BANP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BANP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N9N5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

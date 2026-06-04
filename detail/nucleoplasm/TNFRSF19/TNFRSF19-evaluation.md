---
type: protein-evaluation
gene: "TNFRSF19"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TNFRSF19 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TNFRSF19 / TAJ, TROY |
| 蛋白名称 | Tumor necrosis factor receptor superfamily member 19 |
| 蛋白大小 | 423 aa / 46.0 kDa |
| UniProt ID | Q9NS68 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Golgi apparatus; 额外: Nucleoplasm; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 423 aa / 46.0 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=60 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001368, IPR022342, IPR034047, IPR047526 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **98.0/180** | |
| **归一化总分** | | | **54.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nucleoplasm | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- membrane (GO:0016020)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 60 |
| PubMed broad count | 143 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TAJ, TROY |

**关键文献**:
1. Multi‑layered prevention and treatment of chronic inflammation, organ fibrosis and cancer associated with canonical WNT/β‑catenin signaling activation (Review).. *International journal of molecular medicine*. PMID: 29786110
2. Identification of diagnostic biomarkers and therapeutic targets in peripheral immune landscape from coronary artery disease.. *Journal of translational medicine*. PMID: 36064568
3. Downregulation of TNFRSF19 and RAB43 by a novel miRNA, miR-HCC3, promotes proliferation and epithelial-mesenchymal transition in hepatocellular carcinoma cells.. *Biochemical and biophysical research communications*. PMID: 32102752
4. Cancer-associated fibroblasts (CAFs) gene signatures predict outcomes in breast and prostate tumor patients.. *Journal of translational medicine*. PMID: 38937754
5. Circulating proteins and bone mineral density: A Proteome-Wide Mendelian Randomization Study.. *Current medicinal chemistry*. PMID: 40908527

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.3 |
| 高置信度残基 (pLDDT>90) 占比 | 23.9% |
| 置信残基 (pLDDT 70-90) 占比 | 12.8% |
| 中等置信 (pLDDT 50-70) 占比 | 9.7% |
| 低置信 (pLDDT<50) 占比 | 53.7% |
| 有序区域 (pLDDT>70) 占比 | 36.7% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=60.3），有序残基占 36.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001368, IPR022342, IPR034047, IPR047526 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LINGO1 | 0.996 | 0.000 | — |
| RTN4R | 0.994 | 0.000 | — |
| OMG | 0.942 | 0.000 | — |
| MAG | 0.839 | 0.000 | — |
| LGR5 | 0.785 | 0.000 | — |
| RTN4 | 0.750 | 0.000 | — |
| RELT | 0.722 | 0.000 | — |
| RTN4RL2 | 0.721 | 0.000 | — |
| MIPEP | 0.713 | 0.000 | — |
| NKD1 | 0.678 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TRAF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:10809768 |
| TRAF2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:10809768 |
| TRAF5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:10809768 |
| MTURN | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| GIMAP5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SGTB | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| NOP56 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PLD2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KLK10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| THAP12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.3 + PDB: 无 | pLDDT=60.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Golgi apparatus; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TNFRSF19 — Tumor necrosis factor receptor superfamily member 19，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小423 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 60 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=60.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NS68
- Protein Atlas: https://www.proteinatlas.org/ENSG00000127863-TNFRSF19/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TNFRSF19
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NS68
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

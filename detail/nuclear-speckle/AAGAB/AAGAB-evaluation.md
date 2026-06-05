---
type: protein-evaluation
gene: "AAGAB"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## AAGAB 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AAGAB |
| 蛋白名称 | Alpha- and gamma-adaptin-binding protein p34 |
| 蛋白大小 | 315 aa / 34.6 kDa |
| UniProt ID | Q6PD74 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles, Cytosol; UniProt: Cytoplasm, cytosol |
| 蛋白大小 | 10/10 | ×1 | 10 | 315 aa / 34.6 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=32 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=79.7; PDB: 7TWD, 9DDS, 9DDT |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR019341; Pfam: PF10199 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.0/180** | |
| **归一化总分** | | | **72.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles, Cytosol | Supported |
| UniProt | Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nuclear speck (GO:0016607)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 32 |
| PubMed broad count | 52 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Structural basis of pseudoGTPase-mediated protein-protein interactions.. *bioRxiv : the preprint server for biology*. PMID: 39554064
2. Structural basis of pseudoGTPase-mediated protein-protein interactions.. *Structure (London, England : 1993)*. PMID: 40752490
3. The adaptor protein chaperone AAGAB stabilizes AP-4 complex subunits.. *Molecular biology of the cell*. PMID: 35976721
4. CCDC32 collaborates with the membrane to assemble the AP-2 clathrin adaptor complex.. *bioRxiv : the preprint server for biology*. PMID: 40799577
5. AAGAB is an assembly chaperone regulating AP1 and AP2 clathrin adaptors.. *Journal of cell science*. PMID: 34494650

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.7 |
| 高置信度残基 (pLDDT>90) 占比 | 47.3% |
| 置信残基 (pLDDT 70-90) 占比 | 27.9% |
| 中等置信 (pLDDT 50-70) 占比 | 6.7% |
| 低置信 (pLDDT<50) 占比 | 18.1% |
| 有序区域 (pLDDT>70) 占比 | 75.2% |
| 可用 PDB 条目 | 7TWD, 9DDS, 9DDT |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（7TWD, 9DDS, 9DDT）+ AlphaFold高质量预测（pLDDT=79.7），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019341; Pfam: PF10199 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AP2S1 | 0.917 | 0.837 | — |
| AP1S3 | 0.799 | 0.782 | — |
| AP1G1 | 0.789 | 0.785 | — |
| AP2A2 | 0.775 | 0.738 | — |
| CCDC32 | 0.769 | 0.768 | — |
| KRT9 | 0.732 | 0.000 | — |
| AP2A1 | 0.697 | 0.694 | — |
| AMPH | 0.693 | 0.693 | — |
| AP1G2 | 0.636 | 0.635 | — |
| AP1S2 | 0.629 | 0.596 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EIF3C | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| UNC119 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| AP2S1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:29892012|doi:10.1038/s4 |
| AMPH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| AP1S3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PLEKHA7 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-25739|pubmed:28877994 |
| STXBP3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| AP1G1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| AP1G2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| AP2A2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.7 + PDB: 7TWD, 9DDS, 9DDT | pLDDT=79.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol / Nuclear speckles, Cytosol | 一致 |
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
1. AAGAB — Alpha- and gamma-adaptin-binding protein p34，非常新颖，仅有少数基础研究。
2. 蛋白大小315 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 32 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6PD74
- Protein Atlas: https://www.proteinatlas.org/ENSG00000103591-AAGAB/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AAGAB
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6PD74
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000103591-AAGAB/subcellular

![](https://images.proteinatlas.org/40174/418_F7_1_red_green.jpg)
![](https://images.proteinatlas.org/40174/418_F7_2_red_green.jpg)
![](https://images.proteinatlas.org/40174/424_F7_1_red_green.jpg)
![](https://images.proteinatlas.org/40174/424_F7_2_red_green.jpg)
![](https://images.proteinatlas.org/40174/429_F7_4_red_green.jpg)
![](https://images.proteinatlas.org/40174/429_F7_5_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

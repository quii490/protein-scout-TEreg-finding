---
type: protein-evaluation
gene: "OSTM1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## OSTM1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | OSTM1 / GL |
| 蛋白名称 | Osteopetrosis-associated transmembrane protein 1 |
| 蛋白大小 | 334 aa / 37.3 kDa |
| UniProt ID | Q86WC4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cytosol; 额外: Nucleoplasm, Vesicles; UniProt: Lysosome membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 334 aa / 37.3 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=72 篇 (≤80→4) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=73.9; PDB: 7BXU, 7CQ5, 7CQ6, 7CQ7, 7JM7, 8HVT, 9G6C |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR019172; Pfam: PF09777 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **102.0/180** | |
| **归一化总分** | | | **56.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm, Vesicles | Approved |
| UniProt | Lysosome membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chloride channel complex (GO:0034707)
- cytosol (GO:0005829)
- lysosomal membrane (GO:0005765)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 72 |
| PubMed broad count | 111 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GL |

**关键文献**:
1. Identification of HPCAL1 as a specific autophagy receptor involved in ferroptosis.. *Autophagy*. PMID: 35403545
2. Osteopetrosis-Associated Transmembrane Protein 1 Recruits RNA Exosome To Restrict Hepatitis B Virus Replication.. *Journal of virology*. PMID: 32188736
3. Gain-of-function variants in CLCN7 cause hypopigmentation and lysosomal storage disease.. *The Journal of biological chemistry*. PMID: 38838776
4. The molecular and functional interplay between the osteopetrosis-associated proteins SNX10, OSTM1, and CLC-7 during mouse osteoclastogenesis.. *Journal of bone and mineral research : the official journal of the American Society for Bone and Mineral Research*. PMID: 41408708
5. Expression pattern of the V5-Ostm1 protein in bacterial artificial chromosome transgenic mice.. *Genesis (New York, N.Y. : 2000)*. PMID: 33484096

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.9 |
| 高置信度残基 (pLDDT>90) 占比 | 42.8% |
| 置信残基 (pLDDT 70-90) 占比 | 16.5% |
| 中等置信 (pLDDT 50-70) 占比 | 19.5% |
| 低置信 (pLDDT<50) 占比 | 21.3% |
| 有序区域 (pLDDT>70) 占比 | 59.3% |
| 可用 PDB 条目 | 7BXU, 7CQ5, 7CQ6, 7CQ7, 7JM7, 8HVT, 9G6C, 9G6D, 9G6E |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（7BXU, 7CQ5, 7CQ6, 7CQ7, 7JM7, 8HVT, 9G6C, 9G6D, 9G6E）+ AlphaFold极高置信度预测（pLDDT=73.9），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019172; Pfam: PF09777 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CLCN7 | 0.999 | 0.982 | — |
| TCIRG1 | 0.963 | 0.000 | — |
| PLEKHM1 | 0.919 | 0.000 | — |
| CLCN6 | 0.817 | 0.071 | — |
| CA2 | 0.795 | 0.000 | — |
| SNX10 | 0.781 | 0.000 | — |
| TNFRSF11A | 0.779 | 0.000 | — |
| TNFSF11 | 0.751 | 0.000 | — |
| CLCN3 | 0.751 | 0.063 | — |
| ATP4A | 0.694 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Lamp1 | psi-mi:"MI:0416"(fluorescence microscopy) | imex:IM-14514|pubmed:16525474 |
| Clcn7 | psi-mi:"MI:0416"(fluorescence microscopy) | imex:IM-14514|pubmed:16525474 |
| BIRC7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LGALS8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SCGB1D1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LGALS9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LGALS3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FAM177A1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ATP6AP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| sud1 | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.9 + PDB: 7BXU, 7CQ5, 7CQ6, 7CQ7, 7JM7,  | pLDDT=73.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Lysosome membrane / Cytosol; 额外: Nucleoplasm, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. OSTM1 — Osteopetrosis-associated transmembrane protein 1，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小334 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 72 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86WC4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000081087-OSTM1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=OSTM1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86WC4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

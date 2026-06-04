---
type: protein-evaluation
gene: "TECPR2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TECPR2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TECPR2 / KIAA0297, KIAA0329 |
| 蛋白名称 | Tectonin beta-propeller repeat-containing protein 2 |
| 蛋白大小 | 1411 aa / 153.8 kDa |
| UniProt ID | O15040 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Nucleoli, Centrosome; UniProt: 无注释 |
| 蛋白大小 | 5/10 | ×1 | 5 | 1411 aa / 153.8 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=35 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR056499, IPR006624, IPR009091, IPR015943, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **103.0/180** | |
| **归一化总分** | | | **57.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli, Centrosome | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 35 |
| PubMed broad count | 208 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0297, KIAA0329 |

**关键文献**:
1. The spectrum of neurodevelopmental, neuromuscular and neurodegenerative disorders due to defective autophagy.. *Autophagy*. PMID: 34130600
2. TECPR2-Related Hereditary Sensory and Autonomic Neuropathy with Intellectual Disability.. **. PMID: 36137062
3. The neuropathy-linked protein TECPR2 is a Rab5 effector that regulates cargo recycling from early endosomes.. *Nature communications*. PMID: 41298403
4. TECPR2-related hereditary sensory and autonomic neuropathy in two siblings from Palestine.. *American journal of medical genetics. Part A*. PMID: 38436550
5. Spatial proteomics reveals secretory pathway disturbances caused by neuropathy-associated TECPR2.. *Nature communications*. PMID: 36797266

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.5 |
| 高置信度残基 (pLDDT>90) 占比 | 36.3% |
| 置信残基 (pLDDT 70-90) 占比 | 23.7% |
| 中等置信 (pLDDT 50-70) 占比 | 3.5% |
| 低置信 (pLDDT<50) 占比 | 36.5% |
| 有序区域 (pLDDT>70) 占比 | 60.0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=67.5），有序残基占 60.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR056499, IPR006624, IPR009091, IPR015943, IPR036322; Pfam: PF23756, PF06462, PF19193 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GABARAPL2 | 0.863 | 0.183 | — |
| GABARAPL1 | 0.859 | 0.179 | — |
| MAP1LC3C | 0.824 | 0.165 | — |
| VPS41 | 0.789 | 0.782 | — |
| SPG11 | 0.742 | 0.000 | — |
| VPS16 | 0.729 | 0.690 | — |
| AP5Z1 | 0.726 | 0.000 | — |
| MAP1LC3B | 0.707 | 0.164 | — |
| DDHD1 | 0.687 | 0.000 | — |
| EPG5 | 0.683 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GABARAPL1 | psi-mi:"MI:0096"(pull down) | pubmed:20562859|imex:IM-15184 |
| GABARAPL2 | psi-mi:"MI:0096"(pull down) | pubmed:20562859|imex:IM-15184 |
| MAP1LC3B | psi-mi:"MI:0096"(pull down) | pubmed:20562859|imex:IM-15184 |
| MAP1LC3C | psi-mi:"MI:0096"(pull down) | pubmed:20562859|imex:IM-15184 |
| GABARAP | psi-mi:"MI:0096"(pull down) | pubmed:20562859|imex:IM-15184 |
| DNAJB5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PPM1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| VPS41 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NUDCD3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| VPS16 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.5 + PDB: 无 | pLDDT=67.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Nucleoli, Centrosome | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TECPR2 — Tectonin beta-propeller repeat-containing protein 2，非常新颖，仅有少数基础研究。
2. 蛋白大小1411 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 35 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=67.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O15040
- Protein Atlas: https://www.proteinatlas.org/ENSG00000196663-TECPR2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TECPR2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O15040
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

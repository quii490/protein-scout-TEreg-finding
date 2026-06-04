---
type: protein-evaluation
gene: "BCL9L"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BCL9L 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BCL9L / DLNB11 |
| 蛋白名称 | B-cell CLL/lymphoma 9-like protein |
| 蛋白大小 | 1499 aa / 157.1 kDa |
| UniProt ID | Q86UU0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Nucleoli fibrillar center; UniProt: Nucleus |
| 蛋白大小 | 5/10 | ×1 | 5 | 1499 aa / 157.1 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=48 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=42.2; PDB: 2XB1, 4UP0, 4UP5 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR015668, IPR024670, IPR013083; Pfam: PF11502 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **114.5/180** | |
| **归一化总分** | | | **63.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli fibrillar center | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- beta-catenin-TCF complex (GO:1990907)
- fibrillar center (GO:0001650)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 48 |
| PubMed broad count | 90 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DLNB11 |

**关键文献**:
1. Multi‑layered prevention and treatment of chronic inflammation, organ fibrosis and cancer associated with canonical WNT/β‑catenin signaling activation (Review).. *International journal of molecular medicine*. PMID: 29786110
2. NAT10-mediated mRNA N4-acetylcytidine modification promotes bladder cancer progression.. *Clinical and translational medicine*. PMID: 35522942
3. Identification and characterization of rat Bcl9l gene in silico.. *International journal of oncology*. PMID: 15703843
4. β-Catenin Drives Butyrophilin-like Molecule Loss and γδ T-cell Exclusion in Colon Cancer.. *Cancer immunology research*. PMID: 37309673
5. Identification and characterization of human BCL9L gene and mouse Bcl9l gene in silico.. *International journal of molecular medicine*. PMID: 12964048

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 42.2 |
| 高置信度残基 (pLDDT>90) 占比 | 2.1% |
| 置信残基 (pLDDT 70-90) 占比 | 4.3% |
| 中等置信 (pLDDT 50-70) 占比 | 6.7% |
| 低置信 (pLDDT<50) 占比 | 86.9% |
| 有序区域 (pLDDT>70) 占比 | 6.4% |
| 可用 PDB 条目 | 2XB1, 4UP0, 4UP5 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=42.2），有序残基占 6.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR015668, IPR024670, IPR013083; Pfam: PF11502 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PYGO2 | 0.993 | 0.567 | — |
| CTNNB1 | 0.992 | 0.292 | — |
| BCL9 | 0.963 | 0.221 | — |
| TCF4 | 0.935 | 0.000 | — |
| LDB1 | 0.926 | 0.224 | — |
| PYGO1 | 0.920 | 0.278 | — |
| TLE1 | 0.911 | 0.000 | — |
| TLE3 | 0.907 | 0.000 | — |
| TLE4 | 0.902 | 0.000 | — |
| HNF4A | 0.896 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| WWOX | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15968|pubmed:25678599 |
| Dvl2 | psi-mi:"MI:0663"(confocal microscopy) | imex:IM-15968|pubmed:25678599 |
| PYGO2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15968|pubmed:25678599 |
| CTNNB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15968|pubmed:25678599 |
| HDAC3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15968|pubmed:25678599 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| YAP1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:24255178|imex:IM-21541 |
| STAT3 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:30413785|imex:IM-26874 |
| ROCK2 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:30413785|imex:IM-26874 |
| SH3PXD2B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=42.2 + PDB: 2XB1, 4UP0, 4UP5 | pLDDT=42.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Nucleoli fibrillar center | 一致 |
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
1. BCL9L — B-cell CLL/lymphoma 9-like protein，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小1499 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 48 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=42.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86UU0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000186174-BCL9L/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BCL9L
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86UU0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

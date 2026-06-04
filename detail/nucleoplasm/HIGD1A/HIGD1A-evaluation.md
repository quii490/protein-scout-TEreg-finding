---
type: protein-evaluation
gene: "HIGD1A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HIGD1A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HIGD1A / HIG1 |
| 蛋白名称 | HIG1 domain family member 1A, mitochondrial |
| 蛋白大小 | 93 aa / 10.1 kDa |
| UniProt ID | Q9Y241 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Mitochondria; 额外: Nucleoplasm; UniProt: Mitochondrion membrane; Mitochondrion inner membrane |
| 蛋白大小 | 5/10 | ×1 | 5 | 93 aa / 10.1 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=45 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.0; PDB: 2LOM |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR007667, IPR050355; Pfam: PF04588 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **105.5/180** | |
| **归一化总分** | | | **58.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria; 额外: Nucleoplasm | Supported |
| UniProt | Mitochondrion membrane; Mitochondrion inner membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- mitochondrial inner membrane (GO:0005743)
- mitochondrion (GO:0005739)
- nucleoplasm (GO:0005654)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 45 |
| PubMed broad count | 83 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HIG1 |

**关键文献**:
1. Higd1a facilitates exercise-mediated alleviation of fatty liver in diet-induced obese mice.. *Metabolism: clinical and experimental*. PMID: 35750235
2. The functional role of Higd1a in mitochondrial homeostasis and in multiple disease processes.. *Genes & diseases*. PMID: 37492734
3. Distinct Roles of Mitochondrial HIGD1A and HIGD2A in Respiratory Complex and Supercomplex Biogenesis.. *Cell reports*. PMID: 32375044
4. Mitochondrial HIGD1A inhibits hepatitis B virus transcription and replication through the cellular PNKD-NF-κB-NR2F1 nexus.. *Journal of medical virology*. PMID: 37185850
5. HIGD1A links SIRT1 activity to adipose browning by inhibiting the ROS/DNA damage pathway.. *Cell reports*. PMID: 37393616

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.0 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 35.5% |
| 中等置信 (pLDDT 50-70) 占比 | 47.3% |
| 低置信 (pLDDT<50) 占比 | 17.2% |
| 有序区域 (pLDDT>70) 占比 | 35.5% |
| 可用 PDB 条目 | 2LOM |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=64.0），有序残基占 35.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007667, IPR050355; Pfam: PF04588 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| COX5A | 0.906 | 0.000 | — |
| COX4I1 | 0.838 | 0.085 | — |
| NDUFA4 | 0.761 | 0.228 | — |
| MT-CO3 | 0.731 | 0.619 | — |
| COX5B | 0.721 | 0.494 | — |
| MT-CO2 | 0.710 | 0.619 | — |
| COX6A1 | 0.695 | 0.449 | — |
| COX7A2L | 0.670 | 0.000 | — |
| COX6A2 | 0.661 | 0.449 | — |
| HIF1A | 0.650 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SNRPB | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| 40038273 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PAK5 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EPB41 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TSC22D1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| CASP4 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| 5901994 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| 4759056 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:17314511 |
| P/V | psi-mi:"MI:0096"(pull down) | pubmed:21911578|imex:IM-17703 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.0 + PDB: 2LOM | pLDDT=64.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Mitochondrion membrane; Mitochondrion inner membra / Mitochondria; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. HIGD1A — HIG1 domain family member 1A, mitochondrial，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小93 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 45 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=64.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y241
- Protein Atlas: https://www.proteinatlas.org/ENSG00000181061-HIGD1A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HIGD1A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y241
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

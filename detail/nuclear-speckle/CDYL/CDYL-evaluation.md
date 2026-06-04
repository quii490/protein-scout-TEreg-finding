---
type: protein-evaluation
gene: "CDYL"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CDYL 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CDYL / CDYL1 |
| 蛋白名称 | Chromodomain Y-like protein |
| 蛋白大小 | 598 aa / 66.5 kDa |
| UniProt ID | Q9Y232 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; UniProt: Nucleus; Chromosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 598 aa / 66.5 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=66 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.8; PDB: 2DNT, 2GTR, 7N27 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR016197, IPR000953, IPR023780, IPR023779, IPR029 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **101.5/180** | |
| **归一化总分** | | | **56.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Supported |
| UniProt | Nucleus; Chromosome | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromosome (GO:0005694)
- cytoplasm (GO:0005737)
- nuclear speck (GO:0016607)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 66 |
| PubMed broad count | 100 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CDYL1 |

**关键文献**:
1. Novel Truncated Peptide Derived From circCDYL Exacerbates Cardiac Hypertrophy.. *Circulation research*. PMID: 40242872
2. Global crotonylome reveals CDYL-regulated RPA1 crotonylation in homologous recombination-mediated DNA repair.. *Science advances*. PMID: 32201722
3. The chromodomain protein CDYL confers forebrain identity to human cortical organoids by inhibiting neuronatin.. *Cell reports*. PMID: 39378153
4. Nuclear Condensation of CDYL Links Histone Crotonylation and Cystogenesis in Autosomal Dominant Polycystic Kidney Disease.. *Journal of the American Society of Nephrology : JASN*. PMID: 35918147
5. Hypoxia-induced circ-CDYL-EEF1A2 transcriptional complex drives lung metastasis of cancer stem cells from hepatocellular carcinoma.. *Cancer letters*. PMID: 37852428

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.8 |
| 高置信度残基 (pLDDT>90) 占比 | 41.5% |
| 置信残基 (pLDDT 70-90) 占比 | 11.2% |
| 中等置信 (pLDDT 50-70) 占比 | 2.7% |
| 低置信 (pLDDT<50) 占比 | 44.6% |
| 有序区域 (pLDDT>70) 占比 | 52.7% |
| 可用 PDB 条目 | 2DNT, 2GTR, 7N27 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=67.8），有序残基占 52.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016197, IPR000953, IPR023780, IPR023779, IPR029045; Pfam: PF00385, PF00378 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EHMT2 | 0.995 | 0.789 | — |
| MIER1 | 0.933 | 0.808 | — |
| WIZ | 0.914 | 0.630 | — |
| EHMT1 | 0.912 | 0.135 | — |
| EZH2 | 0.900 | 0.361 | — |
| HDAC1 | 0.883 | 0.704 | — |
| SETDB1 | 0.862 | 0.361 | — |
| HDAC2 | 0.847 | 0.759 | — |
| SCP2 | 0.830 | 0.087 | — |
| HSDL2 | 0.808 | 0.097 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000380718.3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| RICTOR | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17461779 |
| MIER2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:21258344|imex:IM-17039 |
| RBBP4 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:21258344|imex:IM-17039 |
| HDAC2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:21258344|imex:IM-17039 |
| MIER1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:21258344|imex:IM-17039 |
| EHMT2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:21258344|imex:IM-17039 |
| HDAC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-18733|pubmed:23752268 |
| CYBRD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.8 + PDB: 2DNT, 2GTR, 7N27 | pLDDT=67.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome / Nuclear speckles | 一致 |
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
1. CDYL — Chromodomain Y-like protein，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小598 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 66 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=67.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y232
- Protein Atlas: https://www.proteinatlas.org/ENSG00000153046-CDYL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CDYL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y232
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

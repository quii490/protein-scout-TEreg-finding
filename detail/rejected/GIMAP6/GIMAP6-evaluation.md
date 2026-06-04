---
type: protein-evaluation
gene: "GIMAP6"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GIMAP6 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GIMAP6 / IAN2, IAN6 |
| 蛋白名称 | GTPase IMAP family member 6 |
| 蛋白大小 | 292 aa / 32.9 kDa |
| UniProt ID | Q6P9H5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm, cytosol |
| 蛋白大小 | 10/10 | ×1 | 10 | 292 aa / 32.9 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=31 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=86.3; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR006703, IPR045058, IPR027417; Pfam: PF04548 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.5/180** | |
| **归一化总分** | | | **60.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 31 |
| PubMed broad count | 34 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: IAN2, IAN6 |

**关键文献**:
1. GIMAP6 regulates autophagy, immune competence, and inflammation in mice and humans.. *The Journal of experimental medicine*. PMID: 35551368
2. Decoding IBD progression: a dynamic biomarker atlas for personalized disease stratification.. *Journal of translational medicine*. PMID: 41074150
3. Uncovering Hippo pathway-related biomarkers in acute myocardial infarction via scRNA-seq binding transcriptomics.. *Scientific reports*. PMID: 40133574
4. Functional and biochemical characterization of a T cell-associated anti-apoptotic protein, GIMAP6.. *The Journal of biological chemistry*. PMID: 28381553
5. Dysregulation of GTPase IMAP family members in hepatocellular cancer.. *Molecular medicine reports*. PMID: 27667392

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.3 |
| 高置信度残基 (pLDDT>90) 占比 | 71.6% |
| 置信残基 (pLDDT 70-90) 占比 | 12.3% |
| 中等置信 (pLDDT 50-70) 占比 | 4.1% |
| 低置信 (pLDDT<50) 占比 | 12.0% |
| 有序区域 (pLDDT>70) 占比 | 83.9% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=86.3，有序区 83.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006703, IPR045058, IPR027417; Pfam: PF04548 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GIMAP8 | 0.913 | 0.000 | — |
| GIMAP4 | 0.907 | 0.000 | — |
| GIMAP7 | 0.888 | 0.000 | — |
| GIMAP5 | 0.829 | 0.000 | — |
| GIMAP1 | 0.827 | 0.000 | — |
| GABARAPL2 | 0.750 | 0.329 | — |
| GIMAP1-GIMAP5 | 0.749 | 0.000 | — |
| SH2D3C | 0.549 | 0.099 | — |
| KIAA1211L | 0.510 | 0.099 | — |
| TMEM176B | 0.509 | 0.049 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MICAL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SOD1 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:32814053|imex:IM-28217| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.3 + PDB: 无 | pLDDT=86.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GIMAP6 — GTPase IMAP family member 6，非常新颖，仅有少数基础研究。
2. 蛋白大小292 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 31 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6P9H5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000133561-GIMAP6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GIMAP6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6P9H5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

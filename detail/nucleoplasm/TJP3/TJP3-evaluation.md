---
type: protein-evaluation
gene: "TJP3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TJP3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TJP3 / ZO3 |
| 蛋白名称 | Tight junction protein ZO-3 |
| 蛋白大小 | 919 aa / 101.4 kDa |
| UniProt ID | O95049 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cell Junctions; 额外: Plasma membrane; UniProt: Cell membrane; Cell junction, tight junction; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 919 aa / 101.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=32 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.8; PDB: 3KFV |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR008145, IPR008144, IPR027417, IPR001478, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.5/180** | |
| **归一化总分** | | | **65.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cell Junctions; 额外: Plasma membrane | Enhanced |
| UniProt | Cell membrane; Cell junction, tight junction; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- bicellular tight junction (GO:0005923)
- cell junction (GO:0030054)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 32 |
| PubMed broad count | 74 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ZO3 |

**关键文献**:
1. Alterations of the gut commensal Akkermansia muciniphila in patients with COVID-19.. *Virulence*. PMID: 40360188
2. TJP3 promotes T cell immunity escape and chemoresistance in breast cancer: a comprehensive analysis of anoikis-based prognosis prediction and drug sensitivity stratification.. *Aging*. PMID: 37950731
3. Identification, tissue distribution and developmental expression of tjp1/zo-1, tjp2/zo-2 and tjp3/zo-3 in the zebrafish, Danio rerio.. *Gene expression patterns : GEP*. PMID: 17632043
4. Exploring the effects of dietary inulin in rainbow trout fed a high-starch, 100% plant-based diet.. *Journal of animal science and biotechnology*. PMID: 38247008
5. Genomic analysis identifies TJP3 as a prognostic marker for radiotherapy and chemoradiotherapy in oral squamous cell carcinoma.. *Scientific reports*. PMID: 40841384

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.8 |
| 高置信度残基 (pLDDT>90) 占比 | 30.3% |
| 置信残基 (pLDDT 70-90) 占比 | 26.2% |
| 中等置信 (pLDDT 50-70) 占比 | 7.2% |
| 低置信 (pLDDT<50) 占比 | 36.3% |
| 有序区域 (pLDDT>70) 占比 | 56.5% |
| 可用 PDB 条目 | 3KFV |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=66.8），有序残基占 56.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008145, IPR008144, IPR027417, IPR001478, IPR036034; Pfam: PF00625, PF00595, PF07653 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| OCLN | 0.998 | 0.082 | — |
| CGN | 0.997 | 0.000 | — |
| CLDN1 | 0.996 | 0.330 | — |
| PATJ | 0.996 | 0.292 | — |
| MARVELD2 | 0.995 | 0.000 | — |
| CLDN7 | 0.990 | 0.071 | — |
| TJP1 | 0.988 | 0.292 | — |
| CLDN3 | 0.988 | 0.085 | — |
| TJP2 | 0.988 | 0.000 | — |
| CLDN8 | 0.970 | 0.051 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-10970160 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| CFTR | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12000|pubmed:17110338 |
| FASLG | psi-mi:"MI:0084"(phage display) | pubmed:19807924|imex:IM-20398 |
| PLEKHA7 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-25739|pubmed:28877994 |
| Rpl35 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |
| KCNE3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| E | psi-mi:"MI:0096"(pull down) | imex:IM-28944|pubmed:33864728 |
| CSNK2B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MAGIX | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.8 + PDB: 3KFV | pLDDT=66.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane; Cell junction, tight junction; Nucl / Nucleoplasm, Cell Junctions; 额外: Plasma membrane | 一致 |
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
1. TJP3 — Tight junction protein ZO-3，非常新颖，仅有少数基础研究。
2. 蛋白大小919 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 32 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=66.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O95049
- Protein Atlas: https://www.proteinatlas.org/ENSG00000105289-TJP3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TJP3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95049
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

---
type: protein-evaluation
gene: "KLF5"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## KLF5 — REJECTED (研究热度过高 (PubMed strict=668，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KLF5 / BTEB2, CKLF, IKLF |
| 蛋白名称 | Krueppel-like factor 5 |
| 蛋白大小 | 457 aa / 50.8 kDa |
| UniProt ID | Q13887 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Golgi apparatus, Vesicles; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 457 aa / 50.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=668 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=46.9; PDB: 2EBT |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036236, IPR013087; Pfam: PF00096 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.5/180** | |
| **归一化总分** | | | **44.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Golgi apparatus, Vesicles | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- Golgi apparatus (GO:0005794)
- nucleoplasm (GO:0005654)
- transcription regulator complex (GO:0005667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 668 |
| PubMed broad count | 1153 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BTEB2, CKLF, IKLF |

**关键文献**:
1. PPIA dictates NRF2 stability to promote lung cancer progression.. *Nature communications*. PMID: 38830868
2. KLF5 Is Induced by FOXO1 and Causes Oxidative Stress and Diabetic Cardiomyopathy.. *Circulation research*. PMID: 33539225
3. Defining a TFAP2C-centered transcription factor network during murine peri-implantation.. *Developmental cell*. PMID: 38574734
4. Targeting PRMT5 through PROTAC for the treatment of triple-negative breast cancer.. *Journal of experimental & clinical cancer research : CR*. PMID: 39614393
5. Deoxycholic acid induces gastric intestinal metaplasia by activating STAT3 signaling and disturbing gastric bile acids metabolism and microbiota.. *Gut microbes*. PMID: 36067404

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 46.9 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 18.6% |
| 中等置信 (pLDDT 50-70) 占比 | 4.4% |
| 低置信 (pLDDT<50) 占比 | 77.0% |
| 有序区域 (pLDDT>70) 占比 | 18.6% |
| 可用 PDB 条目 | 2EBT |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=46.9），有序残基占 18.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036236, IPR013087; Pfam: PF00096 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CEBPB | 0.967 | 0.328 | — |
| CEBPD | 0.950 | 0.091 | — |
| CEBPA | 0.941 | 0.328 | — |
| FBXW7 | 0.940 | 0.826 | — |
| RARA | 0.938 | 0.742 | — |
| EP300 | 0.931 | 0.749 | — |
| WWP1 | 0.914 | 0.842 | — |
| PPARG | 0.901 | 0.311 | — |
| ESR2 | 0.881 | 0.311 | — |
| JUN | 0.860 | 0.328 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SMAD2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:18729074|imex:IM-19222 |
| Sall4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20362541|imex:IM-16928 |
| Tfcp2l1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20362541|imex:IM-16928 |
| Pou5f1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20362541|imex:IM-16928 |
| Lyn | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| MAGI1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Naa10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |
| ACTR5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| TRIM63 | psi-mi:"MI:0096"(pull down) | pubmed:31391242|imex:IM-25805| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=46.9 + PDB: 2EBT | pLDDT=46.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Golgi apparatus, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. KLF5 — Krueppel-like factor 5，研究基础较多，新颖性有限。
2. 蛋白大小457 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 668 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=46.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 668 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13887
- Protein Atlas: https://www.proteinatlas.org/ENSG00000102554-KLF5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KLF5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13887
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

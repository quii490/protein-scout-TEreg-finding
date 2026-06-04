---
type: protein-evaluation
gene: "KCTD11"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KCTD11 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KCTD11 / C17orf36, REN |
| 蛋白名称 | BTB/POZ domain-containing protein KCTD11 |
| 蛋白大小 | 232 aa / 25.9 kDa |
| UniProt ID | Q693B1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 232 aa / 25.9 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=24 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=84.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR045763, IPR011333, IPR003131; Pfam: PF02214, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.5/180** | |
| **归一化总分** | | | **63.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 24 |
| PubMed broad count | 44 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C17orf36, REN |

**关键文献**:
1. A novel deacetylase inhibitor KLX suppresses liver fibrosis by deacetylating PPARγ through promoting ubiquitination-mediated HDAC1 degradation.. *Science China. Life sciences*. PMID: 40059271
2. KCTD: A new gene family involved in neurodevelopmental and neuropsychiatric disorders.. *CNS neuroscience & therapeutics*. PMID: 31197948
3. KCTD11 tumor suppressor gene expression is reduced in prostate adenocarcinoma.. *BioMed research international*. PMID: 25045667
4. Cullin 3 Recognition Is Not a Universal Property among KCTD Proteins.. *PloS one*. PMID: 25974686
5. The tumor suppressor gene KCTD11REN is regulated by Sp1 and methylation and its expression is reduced in tumors.. *Molecular cancer*. PMID: 20591193

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.2 |
| 高置信度残基 (pLDDT>90) 占比 | 53.0% |
| 置信残基 (pLDDT 70-90) 占比 | 30.6% |
| 中等置信 (pLDDT 50-70) 占比 | 15.5% |
| 低置信 (pLDDT<50) 占比 | 0.9% |
| 有序区域 (pLDDT>70) 占比 | 83.6% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=84.2，有序区 83.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045763, IPR011333, IPR003131; Pfam: PF02214, PF19329 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL3 | 0.978 | 0.625 | — |
| KCTD5 | 0.768 | 0.000 | — |
| KCTD2 | 0.701 | 0.304 | — |
| KCTD17 | 0.697 | 0.000 | — |
| KCTD8 | 0.680 | 0.000 | — |
| GLI1 | 0.668 | 0.000 | — |
| KCTD12 | 0.666 | 0.000 | — |
| KCTD9 | 0.646 | 0.000 | — |
| NEUROG1 | 0.637 | 0.000 | — |
| KCTD3 | 0.624 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| KCTD6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| EBI-16419122 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21472142|imex:IM-26155 |
| KCTD21 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21472142|imex:IM-26155 |
| ENST00000333751 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.2 + PDB: 无 | pLDDT=84.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. KCTD11 — BTB/POZ domain-containing protein KCTD11，非常新颖，仅有少数基础研究。
2. 蛋白大小232 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 24 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q693B1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000213859-KCTD11/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KCTD11
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q693B1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

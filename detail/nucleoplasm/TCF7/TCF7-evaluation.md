---
type: protein-evaluation
gene: "TCF7"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TCF7 — REJECTED (研究热度过高 (PubMed strict=327，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TCF7 / TCF1 |
| 蛋白名称 | Transcription factor 7 |
| 蛋白大小 | 384 aa / 41.6 kDa |
| UniProt ID | P36402 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 384 aa / 41.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=327 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR027397, IPR013558, IPR009071, IPR036910, IPR024 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 12 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.0/180** | |
| **归一化总分** | | | **48.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- beta-catenin-TCF complex (GO:1990907)
- chromatin (GO:0000785)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 327 |
| PubMed broad count | 684 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TCF1 |

**关键文献**:
1. A single-cell map of intratumoral changes during anti-PD1 treatment of patients with breast cancer.. *Nature medicine*. PMID: 33958794
2. Tertiary lymphoid structures improve immunotherapy and survival in melanoma.. *Nature*. PMID: 31942071
3. Lactate increases stemness of CD8 + T cells to augment anti-tumor immunity.. *Nature communications*. PMID: 36068198
4. Regulation of Proliferation, Differentiation and Functions of Osteoblasts by Runx2.. *International journal of molecular sciences*. PMID: 30987410
5. FOXO1 is a master regulator of memory programming in CAR T cells.. *Nature*. PMID: 38600391

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.1 |
| 高置信度残基 (pLDDT>90) 占比 | 15.6% |
| 置信残基 (pLDDT 70-90) 占比 | 6.0% |
| 中等置信 (pLDDT 50-70) 占比 | 26.0% |
| 低置信 (pLDDT<50) 占比 | 52.3% |
| 有序区域 (pLDDT>70) 占比 | 21.6% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=57.1），有序残基占 21.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027397, IPR013558, IPR009071, IPR036910, IPR024940; Pfam: PF08347, PF00505 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CTNNB1 | 0.999 | 0.886 | — |
| AXIN2 | 0.983 | 0.106 | — |
| JUP | 0.975 | 0.511 | — |
| AXIN1 | 0.974 | 0.106 | — |
| CTBP2 | 0.965 | 0.131 | — |
| CTBP1 | 0.965 | 0.000 | — |
| APC | 0.956 | 0.071 | — |
| NLK | 0.955 | 0.307 | — |
| APC2 | 0.954 | 0.071 | — |
| TCF7L1 | 0.944 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CTNNB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15968|pubmed:25678599 |
| RUNX3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12146|pubmed:18772112 |
| MLLT11 | psi-mi:"MI:0018"(two hybrid) | pubmed:26079538|imex:IM-26244 |
| SS18L1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| BCL11B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| RBFOX3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| FN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TOP2A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MAN2B2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| VSX1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:35140242|imex:IM-28767 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 12
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 12 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.1 + PDB: 无 | pLDDT=57.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 12 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. TCF7 — Transcription factor 7，研究基础较多，新颖性有限。
2. 蛋白大小384 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 327 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=57.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 327 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P36402
- Protein Atlas: https://www.proteinatlas.org/ENSG00000081059-TCF7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TCF7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P36402
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

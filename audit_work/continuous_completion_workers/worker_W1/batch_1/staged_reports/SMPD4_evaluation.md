---
type: protein-evaluation
gene: "SMPD4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SMPD4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SMPD4 / KIAA1418, SKNY |
| 蛋白名称 | Sphingomyelin phosphodiesterase 4 |
| 蛋白大小 | 866 aa / 97.8 kDa |
| UniProt ID | Q9NXE4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear membrane; 额外: Cytosol; UniProt: Endoplasmic reticulum membrane; Golgi apparatus membrane; Nu |
| 蛋白大小 | 8/10 | ×1 | 8 | 866 aa / 97.8 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=24 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=71.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR024129; Pfam: PF14724 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.5/180** | |
| **归一化总分** | | | **67.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear membrane; 额外: Cytosol | Approved |
| UniProt | Endoplasmic reticulum membrane; Golgi apparatus membrane; Nucleus envelope; Cell membrane, sarcolemm... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（批量模式），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)
- Golgi apparatus (GO:0005794)
- Golgi membrane (GO:0000139)
- nuclear envelope (GO:0005635)
- nuclear outer membrane (GO:0005640)
- sarcolemma (GO:0042383)
- trans-Golgi network (GO:0005802)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 24 |
| PubMed broad count | 39 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1418, SKNY |

**关键文献**:
1. Neurogenetic fetal akinesia and arthrogryposis: genetics, expanding genotype-phenotypes and functional genomics.. *Journal of medical genetics*. PMID: 33060286
2. SMPD4 mediated sphingolipid metabolism regulates brain and primary cilia development.. *bioRxiv : the preprint server for biology*. PMID: 38168190
3. SMPD4-mediated sphingolipid metabolism regulates brain and primary cilia development.. *Development (Cambridge, England)*. PMID: 39470011
4. High expression of SMPD4 promotes liver cancer and is associated with poor prognosis.. *BMC research notes*. PMID: 40211349
5. Growth and neurodevelopmental disorder with arthrogryposis, microcephaly and structural brain anomalies caused by Bi-allelic partial deletion of SMPD4 gene.. *Journal of human genetics*. PMID: 34621002

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.2 |
| 高置信度残基 (pLDDT>90) 占比 | 28.4% |
| 置信残基 (pLDDT 70-90) 占比 | 33.1% |
| 中等置信 (pLDDT 50-70) 占比 | 13.7% |
| 低置信 (pLDDT<50) 占比 | 24.7% |
| 有序区域 (pLDDT>70) 占比 | 61.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（批量模式），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=71.2，有序区 61.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR024129; Pfam: PF14724 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SMPD3 | 0.996 | 0.000 | — |
| SMPD2 | 0.994 | 0.000 | — |
| SMPD1 | 0.969 | 0.000 | — |
| SGMS1 | 0.968 | 0.000 | — |
| SGMS2 | 0.959 | 0.000 | — |
| ENPP7 | 0.959 | 0.000 | — |
| DEGS1 | 0.952 | 0.000 | — |
| CERS6 | 0.952 | 0.000 | — |
| CERS2 | 0.952 | 0.000 | — |
| DEGS2 | 0.951 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EXOSC4 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| BRF2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| CUL2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| ISG15 | psi-mi:"MI:0096"(pull down) | pubmed:26259872|imex:IM-26283 |
| CANX | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| LMNA | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| CLN6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:30177828|imex:IM-26452 |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |
| SRFBP1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H9A910 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:30177828|imex:IM-26452 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.2 + PDB: 无 | pLDDT=71.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Golgi apparatus me / Nuclear membrane; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. SMPD4 — Sphingomyelin phosphodiesterase 4，非常新颖，仅有少数基础研究。
2. 蛋白大小866 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 24 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NXE4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000136699-SMPD4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SMPD4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NXE4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

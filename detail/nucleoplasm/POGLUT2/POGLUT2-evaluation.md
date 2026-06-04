---
type: protein-evaluation
gene: "POGLUT2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## POGLUT2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | POGLUT2 / EP58, KDELC1 |
| 蛋白名称 | Protein O-glucosyltransferase 2 |
| 蛋白大小 | 502 aa / 58.0 kDa |
| UniProt ID | Q6UW63 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Endoplasmic reticulum lumen |
| 蛋白大小 | 10/10 | ×1 | 10 | 502 aa / 58.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=92.5; PDB: 2DI7 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR006598, IPR017868, IPR001298, IPR013783, IPR014 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 10 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **139.0/180** | |
| **归一化总分** | | | **77.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Endoplasmic reticulum lumen | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- endomembrane system (GO:0012505)
- endoplasmic reticulum lumen (GO:0005788)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 12 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: EP58, KDELC1 |

**关键文献**:
1. Identification, function, and biological relevance of POGLUT2 and POGLUT3.. *Biochemical Society transactions*. PMID: 35411374
2. POGLUT2 and POGLUT3: Two essential protein O-glucosyltransferases modifying EGF repeats in extracellular matrix proteins.. *Biochimica et biophysica acta. General subjects*. PMID: 41955902
3. POGLUT2 and POGLUT3 O-glucosylate multiple EGF repeats in fibrillin-1, -2, and LTBP1 and promote secretion of fibrillin-1.. *The Journal of biological chemistry*. PMID: 34411563
4. A comprehensive role evaluation and mechanism exploration of POGLUT2 in pan-cancer.. *Frontiers in oncology*. PMID: 36158688
5. POGLUT2/3 mediated EGF O-glucosylation promotes separation of digits 2 and 3 by influencing fibrillin network reorganization, signaling, and cell dynamics.. *Developmental biology*. PMID: 40784523

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.5 |
| 高置信度残基 (pLDDT>90) 占比 | 87.5% |
| 置信残基 (pLDDT 70-90) 占比 | 5.0% |
| 中等置信 (pLDDT 50-70) 占比 | 1.6% |
| 低置信 (pLDDT<50) 占比 | 6.0% |
| 有序区域 (pLDDT>70) 占比 | 92.5% |
| 可用 PDB 条目 | 2DI7 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=92.5，有序区 92.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006598, IPR017868, IPR001298, IPR013783, IPR014756; Pfam: PF00630, PF05686 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FLNA | 0.817 | 0.000 | — |
| POFUT1 | 0.694 | 0.111 | — |
| BIVM | 0.640 | 0.000 | — |
| GXYLT1 | 0.630 | 0.000 | — |
| GXYLT2 | 0.620 | 0.000 | — |
| XXYLT1 | 0.600 | 0.000 | — |
| EOGT | 0.535 | 0.000 | — |
| EGF | 0.472 | 0.000 | — |
| POGLUT3 | 0.460 | 0.000 | — |
| BMP1 | 0.407 | 0.397 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| CUL2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| GOLGA4 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| TAZ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| BMP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LOXL3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Ankrd28 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| ITGB8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| LY86 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| BRICD5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 10，IntAct interactions: 15
- 调控相关比例: 0 / 10 = 0%

**评价**: STRING 10 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.5 + PDB: 2DI7 | pLDDT=92.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Endoplasmic reticulum lumen / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 10 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. POGLUT2 — Protein O-glucosyltransferase 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小502 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6UW63
- Protein Atlas: https://www.proteinatlas.org/ENSG00000134901-POGLUT2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=POGLUT2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6UW63
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

---
type: protein-evaluation
gene: "TESMIN"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TESMIN 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TESMIN / MTL5 |
| 蛋白名称 | Tesmin |
| 蛋白大小 | 508 aa / 55.0 kDa |
| UniProt ID | Q9Y4I5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Vesicles, Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 508 aa / 55.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=25 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=53.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR005172, IPR028307, IPR033467; Pfam: PF03638 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.0/180** | |
| **归一化总分** | | | **66.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles, Cytosol | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- male germ cell nucleus (GO:0001673)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 25 |
| PubMed broad count | 32 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MTL5 |

**关键文献**:
1. TESMIN promotes lung adenocarcinoma proliferation, migration and invasion via PI3K/AKT/mTOR signaling.. *Scientific reports*. PMID: 41276573
2. Identification and characterization of a ligand-selective mineralocorticoid receptor coactivator.. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology*. PMID: 24907116
3. Clinical Significance and Functional Insights of Tesmin in Hepatocellular Carcinoma.. *Genetics research*. PMID: 38283987
4. Tesmin transcription is regulated differently during male and female meiosis.. *Molecular reproduction and development*. PMID: 14648882
5. Comprehensive bioinformatics analysis of prognosis and immunotherapy in lung adenocarcinoma.. *Journal of thoracic disease*. PMID: 39831256

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 53.8 |
| 高置信度残基 (pLDDT>90) 占比 | 25.0% |
| 置信残基 (pLDDT 70-90) 占比 | 5.7% |
| 中等置信 (pLDDT 50-70) 占比 | 6.1% |
| 低置信 (pLDDT<50) 占比 | 63.2% |
| 有序区域 (pLDDT>70) 占比 | 30.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=53.8），有序残基占 30.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR005172, IPR028307, IPR033467; Pfam: PF03638 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MT1E | 0.870 | 0.000 | — |
| LIN9 | 0.746 | 0.354 | — |
| LIN52 | 0.682 | 0.188 | — |
| LIN37 | 0.665 | 0.297 | — |
| NAF1 | 0.583 | 0.000 | — |
| RBBP4 | 0.581 | 0.268 | — |
| TMEM147 | 0.533 | 0.294 | — |
| RBBP7 | 0.493 | 0.268 | — |
| TRAPPC5 | 0.482 | 0.482 | — |
| TRAPPC2L | 0.476 | 0.476 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MYDGF | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| FNDC3B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| NRF1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TRAPPC3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| trappc2_trappc2b_human | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HSPA9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TRAPPC10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TRAPPC6B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TRAPPC5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TRAPPC14 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=53.8 + PDB: 无 | pLDDT=53.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Vesicles, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TESMIN — Tesmin，非常新颖，仅有少数基础研究。
2. 蛋白大小508 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 25 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=53.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y4I5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000132749-TESMIN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TESMIN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y4I5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000132749-TESMIN/subcellular

![](https://images.proteinatlas.org/18539/1199_B3_1_red_green.jpg)
![](https://images.proteinatlas.org/18539/1199_B3_2_red_green.jpg)
![](https://images.proteinatlas.org/18539/1232_B3_1_red_green.jpg)
![](https://images.proteinatlas.org/18539/1232_B3_5_red_green.jpg)
![](https://images.proteinatlas.org/18539/1248_A6_5_red_green.jpg)
![](https://images.proteinatlas.org/18539/1248_A6_6_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y4I5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

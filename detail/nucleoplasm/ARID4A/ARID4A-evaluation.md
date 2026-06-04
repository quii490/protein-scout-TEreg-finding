---
type: protein-evaluation
gene: "ARID4A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ARID4A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ARID4A / RBBP1, RBP1 |
| 蛋白名称 | AT-rich interactive domain-containing protein 4A |
| 蛋白大小 | 1257 aa / 142.8 kDa |
| UniProt ID | P29374 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Plasma membrane; UniProt: Nucleus |
| 📏 蛋白大小 | 5/10 | ×1 | 5 | 1257 aa / 142.8 kDa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=33 篇 (≤40→8) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.3; PDB: 2LCC, 2MAM, 2YRV, 6BPH, 6L87, 7SMC, 7V8N |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051232, IPR012603, IPR001606, IPR036431, IPR047 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.5/180** | |
| **归一化总分 (÷1.83)** | | | **62.3/100******** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Plasma membrane | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**GO Cellular Component**:
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)
- Sin3-type complex (GO:0070822)
- transcription repressor complex (GO:0017053)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 33 |
| PubMed broad count | 378 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RBBP1, RBP1 |

**关键文献**:
1. Structural basis for the DNA-binding activity of human ARID4B Tudor domain.. *The Journal of biological chemistry*. PMID: 33675746
2. ARID4A and ARID4B regulate male fertility, a functional link to the AR and RB pathways.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 23487765
3. Downregulation of ARID4A and ARID4B promote tumor progression and directly regulated by microRNA-30d in patient with prostate cancer.. *Journal of cellular biochemistry*. PMID: 29797600
4. AlphaFold-guided structural analyses of nucleosome binding proteins.. *Nucleic acids research*. PMID: 40794873
5. Identification of chromatin remodeling genes Arid4a and Arid4b as leukemia suppressor genes.. *Journal of the National Cancer Institute*. PMID: 18728284

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.3 |
| 高置信度残基 (pLDDT>90) 占比 | 19.6% |
| 置信残基 (pLDDT 70-90) 占比 | 13.6% |
| 中等置信 (pLDDT 50-70) 占比 | 5.5% |
| 低置信 (pLDDT<50) 占比 | 61.3% |
| 有序区域 (pLDDT>70) 占比 | 33.2% |
| 可用 PDB 条目 | 2LCC, 2MAM, 2YRV, 6BPH, 6L87, 7SMC, 7V8N |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: AlphaFold 预测质量有限（pLDDT=56.3），有序残基占 33.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051232, IPR012603, IPR001606, IPR036431, IPR047473; Pfam: PF01388, PF08169, PF11717 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BRMS1 | 0.999 | 0.811 | — |
| BRMS1L | 0.997 | 0.629 | — |
| SIN3A | 0.995 | 0.944 | — |
| SAP30 | 0.992 | 0.821 | — |
| SIN3B | 0.990 | 0.913 | — |
| SUDS3 | 0.987 | 0.631 | — |
| HDAC1 | 0.986 | 0.845 | — |
| ING2 | 0.986 | 0.853 | — |
| RB1 | 0.984 | 0.952 | — |
| ING1 | 0.981 | 0.675 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000347602.3 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| BRMS1 | psi-mi:"MI:0018"(two hybrid) | pubmed:16919237|imex:IM-19611 |
| DEDD | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| HDAC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-18733|pubmed:23752268 |
| PROCR | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| RBBP7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ING2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZNF704 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MXD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SINHCAF | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.3 + PDB: 2LCC, 2MAM, 2YRV, 6BPH, 6L87,  | pLDDT=56.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Plasma membrane | 一致 |
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
1. ARID4A — AT-rich interactive domain-containing protein 4A，非常新颖，仅有少数基础研究。
2. 蛋白大小1257 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 33 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=56.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P29374
- Protein Atlas: https://www.proteinatlas.org/ENSG00000032219-ARID4A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ARID4A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P29374
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 02:29:35

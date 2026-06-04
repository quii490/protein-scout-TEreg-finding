---
type: protein-evaluation
gene: "DDA1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DDA1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DDA1 / C19orf58, PCIA1 |
| 蛋白名称 | DET1- and DDB1-associated protein 1 |
| 蛋白大小 | 102 aa / 11.8 kDa |
| UniProt ID | Q9BW61 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: Nucleoplasm, Nucleoli; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 102 aa / 11.8 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=33 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.3; PDB: 6DSZ, 6PAI, 6Q0R, 6Q0V, 6Q0W, 6SJ7, 6UD7 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR033575, IPR018276; Pfam: PF10172 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.5/180** | |
| **归一化总分** | | | **68.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- Cul4-RING E3 ubiquitin ligase complex (GO:0080008)
- nucleoplasm (GO:0005654)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 33 |
| PubMed broad count | 63 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C19orf58, PCIA1 |

**关键文献**:
1. The small CRL4(CSA) ubiquitin ligase component DDA1 regulates transcription-coupled repair dynamics.. *Nature communications*. PMID: 39075067
2. Cryo-EM structure of the human COP1-DET1 ubiquitin ligase complex.. *Nature communications*. PMID: 41540009
3. Dihydroartemisinin Affects STAT3/DDA1 Signaling Pathway and Reverses Breast Cancer Resistance to Cisplatin.. *The American journal of Chinese medicine*. PMID: 36891981
4. Misregulation of the LOB domain gene DDA1 suggests possible functions in auxin signalling and photomorphogenesis.. *Journal of experimental botany*. PMID: 20797997
5. LncRNA HOTTIP promotes proliferation and cell cycle progression of acute myeloid leukemia cells.. *European review for medical and pharmacological sciences*. PMID: 31002141

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.3 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 50.0% |
| 中等置信 (pLDDT 50-70) 占比 | 34.3% |
| 低置信 (pLDDT<50) 占比 | 15.7% |
| 有序区域 (pLDDT>70) 占比 | 50.0% |
| 可用 PDB 条目 | 6DSZ, 6PAI, 6Q0R, 6Q0V, 6Q0W, 6SJ7, 6UD7, 6UE5, 8G46, 8QH5 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=66.3），有序残基占 50.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR033575, IPR018276; Pfam: PF10172 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL4A | 0.999 | 0.814 | — |
| DDB1 | 0.999 | 0.992 | — |
| DET1 | 0.999 | 0.613 | — |
| DCAF15 | 0.998 | 0.939 | — |
| CUL4B | 0.996 | 0.810 | — |
| DCAF1 | 0.995 | 0.834 | — |
| AMBRA1 | 0.987 | 0.826 | — |
| DDB2 | 0.971 | 0.680 | — |
| RBM39 | 0.968 | 0.862 | — |
| DCAF11 | 0.967 | 0.627 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000473086.1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| DDB1A | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| vpr | psi-mi:"MI:0096"(pull down) | imex:IM-17346|pubmed:22190034| |
| COPS6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| DCAF17 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| CAND1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| NANS | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| FARSB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| DCAF11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| GMPS | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.3 + PDB: 6DSZ, 6PAI, 6Q0R, 6Q0V, 6Q0W,  | pLDDT=66.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DDA1 — DET1- and DDB1-associated protein 1，非常新颖，仅有少数基础研究。
2. 蛋白大小102 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 33 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=66.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BW61
- Protein Atlas: https://www.proteinatlas.org/ENSG00000130311-DDA1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DDA1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BW61
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

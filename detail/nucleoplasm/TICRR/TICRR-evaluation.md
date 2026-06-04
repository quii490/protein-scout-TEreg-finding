---
type: protein-evaluation
gene: "TICRR"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TICRR 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TICRR / C15orf42 |
| 蛋白名称 | Treslin |
| 蛋白大小 | 1910 aa / 210.9 kDa |
| UniProt ID | Q7Z2Z1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 5/10 | ×1 | 5 | 1910 aa / 210.9 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=28 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=47.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026153, IPR032746, IPR053919, IPR053920; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **115.0/180** | |
| **归一化总分** | | | **63.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 28 |
| PubMed broad count | 58 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C15orf42 |

**关键文献**:
1. A vertebrate gene, ticrr, is an essential checkpoint and replication regulator.. *Genes & development*. PMID: 20080954
2. A Genetic Marker Associated with Shoulder Dislocation.. *International journal of sports medicine*. PMID: 28521375
3. Overexpression of TICRR and PPIF confer poor prognosis in endometrial cancer identified by gene co-expression network analysis.. *Aging*. PMID: 33495413
4. ncRNAs-mediated high expression of TICRR promotes tumor cell proliferation and migration and is correlated with poor prognosis and tumor immune infiltration of hepatocellular carcinoma.. *Molecular therapy. Nucleic acids*. PMID: 36213689
5. A mechanism for epigenetic control of DNA replication.. *Genes & development*. PMID: 29483155

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 47.7 |
| 高置信度残基 (pLDDT>90) 占比 | 0.9% |
| 置信残基 (pLDDT 70-90) 占比 | 24.4% |
| 中等置信 (pLDDT 50-70) 占比 | 11.7% |
| 低置信 (pLDDT<50) 占比 | 63.0% |
| 有序区域 (pLDDT>70) 占比 | 25.3% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=47.7），有序残基占 25.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026153, IPR032746, IPR053919, IPR053920; Pfam: PF15292, PF21854, PF21855 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TOPBP1 | 0.999 | 0.825 | — |
| CDC45 | 0.988 | 0.000 | — |
| MTBP | 0.984 | 0.522 | — |
| DBF4 | 0.982 | 0.000 | — |
| RECQL4 | 0.972 | 0.000 | — |
| MCM10 | 0.972 | 0.000 | — |
| MCM4 | 0.939 | 0.000 | — |
| CDC7 | 0.926 | 0.047 | — |
| GINS4 | 0.898 | 0.000 | — |
| GINS3 | 0.884 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| topbp1-A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-13612|pubmed:20116089 |
| H2BC14 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| CCNA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Ptpn23 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| EGLN3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26972000|imex:IM-22750 |
| MKI67 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26949251|imex:IM-26415 |
| AFG2B | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:38554706|imex:IM-30175 |
| AFG2A | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:38554706|imex:IM-30175 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 8
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 8 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=47.7 + PDB: 无 | pLDDT=47.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 8 interactions | 数据充分 |

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
1. TICRR — Treslin，非常新颖，仅有少数基础研究。
2. 蛋白大小1910 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 28 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=47.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z2Z1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000140534-TICRR/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TICRR
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7Z2Z1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

---
type: protein-evaluation
gene: "CMYA5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CMYA5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CMYA5 / C5orf10, DTNBP2, SPRYD2, TRIM76 |
| 蛋白名称 | Cardiomyopathy-associated protein 5 |
| 蛋白大小 | 4069 aa / 449.2 kDa |
| UniProt ID | Q8N3K9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Endoplasmic reticulum, Plasma membrane; UniProt: Nucleus; Sarcoplasmic reticulum; Cytoplasm; Cytoplasm, perin |
| 蛋白大小 | 0/10 | ×1 | 0 | 4069 aa / 449.2 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=39 篇 (≤40→8) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001870, IPR043136, IPR013320, IPR050617, IPR003 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **104.0/180** | |
| **归一化总分** | | | **57.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum, Plasma membrane | Uncertain |
| UniProt | Nucleus; Sarcoplasmic reticulum; Cytoplasm; Cytoplasm, perinuclear region; Cytoplasm, myofibril, sar... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（批量模式），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- M band (GO:0031430)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)
- sarcoplasmic reticulum (GO:0016529)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 39 |
| PubMed broad count | 57 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C5orf10, DTNBP2, SPRYD2, TRIM76 |

**关键文献**:
1. Association between CMYA5 gene polymorphisms and risk of schizophrenia in Uygur population and a meta-analysis.. *Early intervention in psychiatry*. PMID: 26403435
2. Updated meta-analysis of CMYA5 rs3828611 and rs4704591 with schizophrenia in Asian populations.. *Early intervention in psychiatry*. PMID: 28776924
3. GWA study data mining and independent replication identify cardiomyopathy-associated 5 (CMYA5) as a risk gene for schizophrenia.. *Molecular psychiatry*. PMID: 20838396
4. Virally delivered CMYA5 enhances the assembly of cardiac dyads.. *Nature biomedical engineering*. PMID: 39237710
5. CMYA5 establishes cardiac dyad architecture and positioning.. *Nature communications*. PMID: 35449169

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（批量模式），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001870, IPR043136, IPR013320, IPR050617, IPR003961; Pfam: PF00622 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TTN | 0.844 | 0.000 | — |
| DTNBP1 | 0.840 | 0.000 | — |
| PRKAR2A | 0.835 | 0.000 | — |
| CAPN3 | 0.791 | 0.073 | — |
| ACTN2 | 0.774 | 0.046 | — |
| PRKAR1B | 0.756 | 0.000 | — |
| MYOZ2 | 0.734 | 0.000 | — |
| DTNA | 0.674 | 0.000 | — |
| ALMS1 | 0.629 | 0.066 | — |
| BBOX1 | 0.609 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000394770.2 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| Q9ER96 | psi-mi:"MI:0018"(two hybrid) | pubmed:14688250|imex:IM-19238 |
| PSMC4 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| BZW1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| MYBPC2 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| OPTN | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| SNAPIN | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| DYSF | psi-mi:"MI:0663"(confocal microscopy) | pubmed:23414517|imex:IM-16425 |
| CAPN3 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Sarcoplasmic reticulum; Cytoplasm; Cytopl / Endoplasmic reticulum, Plasma membrane | 一致 |
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
1. CMYA5 — Cardiomyopathy-associated protein 5，非常新颖，仅有少数基础研究。
2. 蛋白大小4069 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 39 篇，已有一定研究基础
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N3K9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164309-CMYA5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CMYA5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N3K9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

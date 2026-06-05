---
type: protein-evaluation
gene: "DDX46"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DDX46 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DDX46 |
| 蛋白名称 | Probable ATP-dependent RNA helicase DDX46 |
| 蛋白大小 | 1032 aa / 117.5 kDa |
| UniProt ID | A0A0C4DG89 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | x4 | 32 | HPA: Nuclear speckles; 额外: Nucleoli fibrillar center; UniProt: Nucleus speckle; Nucleus, Cajal body |
| 蛋白大小 | 8/10 | x1 | 8 | 1032 aa / 117.5 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=32 篇 (<=40->8) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=65.7; PDB: 无 |
| 调控结构域 | 5/10 | x2 | 10 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles; 额外: Nucleoli fibrillar center | Supported |
| UniProt | Nucleus speckle; Nucleus, Cajal body | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 32 |
| PubMed broad count | 38 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Caspase-mediated DDX46 cleavage unchains antiviral immunity.. *mBio*. PMID: 41854249
2. O-GlcNAcylation of DDX46 promotes hepatocellular carcinoma progression by activating the PI3K/Akt signaling pathway.. *Biochim Biophys Acta Mol Cell Res*. PMID: 41176131
3. SUGP1 loss drives SF3B1 hotspot mutant missplicing in cancer.. *Cell Rep*. PMID: 40714635
4. Comprehensive analysis indicates DDX46 as a novel biomarker for the prognosis of lung adenocarcinoma.. *Oncol Lett*. PMID: 40271004
5. m6A eraser ALKBH5/treRNA1/DDX46 axis regulates BCR expression.. *Neoplasia*. PMID: 39987653

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.7 |
| 高置信度残基 (pLDDT>90) 占比 | 27.9% |
| 置信残基 (pLDDT 70-90) 占比 | 23.4% |
| 中等置信 (pLDDT 50-70) 占比 | 11.9% |
| 低置信 (pLDDT<50) 占比 | 36.7% |
| 有序区域 (pLDDT>70) 占比 | 51.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=65.7），有序残基占 51.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SF3B1 | 0.000 | 0.000 | — |
| SF3A3 | 0.000 | 0.000 | — |
| SF3A2 | 0.000 | 0.000 | — |
| SF3A1 | 0.000 | 0.000 | — |
| SF3B5 | 0.000 | 0.000 | — |
| SF3B2 | 0.000 | 0.000 | — |
| SF3B3 | 0.000 | 0.000 | — |
| SNRPD1 | 0.000 | 0.000 | — |
| SNRPA1 | 0.000 | 0.000 | — |
| PHF5A | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q5NF50 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q7L014 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P19838 | psi-mi:"MI:0034"(display technology) | pubmed:- |
| uniprotkb:P60763 | psi-mi:"MI:0034"(display technology) | pubmed:- |
| uniprotkb:Q81VT8 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:A0A0C4DG89 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q62780 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.7 + PDB: 无 | pLDDT=65.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus speckle; Nucleus, Cajal body / Nuclear speckles; 额外: Nucleoli fibrillar center | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ***

**核心优势**:
1. DDX46 -- Probable ATP-dependent RNA helicase DDX46，非常新颖，仅有少数基础研究。
2. 蛋白大小1032 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 32 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=65.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A0A0C4DG89
- Protein Atlas: https://www.proteinatlas.org/ENSG00000145833-DDX46/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DDX46
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A0A0C4DG89
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A0A0C4DG89-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

---
type: protein-evaluation
gene: "CYREN"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CYREN 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CYREN / C7orf49, MRI |
| 蛋白名称 | Cell cycle regulator of non-homologous end joining |
| 蛋白大小 | 157 aa / 16.8 kDa |
| UniProt ID | Q9BWK5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm; Nucleus; Chromosome; Cytoplasm; Cytoplasm; Nucleu |
| 蛋白大小 | 8/10 | ×1 | 8 | 157 aa / 16.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.7; PDB: 6TYU |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR028278; Pfam: PF15325 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.5/180** | |
| **归一化总分** | | | **71.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm; Nucleus; Chromosome; Cytoplasm; Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- DNA repair complex (GO:1990391)
- nucleus (GO:0005634)
- site of double-strand break (GO:0035861)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 48 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C7orf49, MRI |

**关键文献**:
1. Biochemistry and Protein Interactions of the CYREN Microprotein.. *Biochemistry*. PMID: 37813856
2. Nonhomologous end joining: new accessory factors fine tune the machinery.. *Trends in genetics : TIG*. PMID: 33785198
3. Uncovering genetic interactions in the DNA repair network in response to endogenous damage and ionizing radiation.. *Cell reports*. PMID: 41546867
4. MRI Is a DNA Damage Response Adaptor during Classical Non-homologous End Joining.. *Molecular cell*. PMID: 30017584
5. KBM-mediated interactions with KU80 promote cellular resistance to DNA replication stress in CHO cells.. *DNA repair*. PMID: 38901287

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.7 |
| 高置信度残基 (pLDDT>90) 占比 | 17.2% |
| 置信残基 (pLDDT 70-90) 占比 | 15.9% |
| 中等置信 (pLDDT 50-70) 占比 | 49.0% |
| 低置信 (pLDDT<50) 占比 | 17.8% |
| 有序区域 (pLDDT>70) 占比 | 33.1% |
| 可用 PDB 条目 | 6TYU |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=65.7），有序残基占 33.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR028278; Pfam: PF15325 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| XRCC6 | 0.905 | 0.000 | — |
| MRI1 | 0.890 | 0.000 | — |
| XRCC5 | 0.879 | 0.000 | — |
| ERCC6L2 | 0.812 | 0.592 | — |
| AMHR2 | 0.783 | 0.000 | — |
| CTNND2 | 0.760 | 0.000 | — |
| PAXX | 0.691 | 0.000 | — |
| XRCC4 | 0.685 | 0.000 | — |
| ROPN1L | 0.637 | 0.000 | — |
| PRKDC | 0.626 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MFHAS1 | psi-mi:"MI:0089"(protein array) | pubmed:29513927|doi:10.1002/pm |
| MKLN1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ERCC6L2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ACOX1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PRRC2B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| FOCAD | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| LPCAT4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| VIRMA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| DHRS11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| RBMXL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.7 + PDB: 6TYU | pLDDT=65.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Chromosome; Cytoplasm; Cytopla / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. CYREN — Cell cycle regulator of non-homologous end joining，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小157 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=65.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BWK5
- Protein Atlas: https://www.proteinatlas.org/search/CYREN
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CYREN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BWK5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BWK5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

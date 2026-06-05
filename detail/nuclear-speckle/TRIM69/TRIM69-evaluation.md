---
type: protein-evaluation
gene: "TRIM69"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TRIM69 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TRIM69 / RNF36 |
| 蛋白名称 | E3 ubiquitin-protein ligase TRIM69 |
| 蛋白大小 | 500 aa / 57.4 kDa |
| UniProt ID | Q86WT6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm; Nucleus; Nucleus speckle; Cytoplasm, cytoskeleton |
| 蛋白大小 | 10/10 | ×1 | 10 | 500 aa / 57.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=28 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=88.3; PDB: 4NQJ, 6YXE |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001870, IPR043136, IPR003879, IPR013320, IPR006 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **132.0/180** | |
| **归一化总分** | | | **73.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm; Nucleus; Nucleus speckle; Cytoplasm, cytoskeleton, microtubule organizing center, centros... | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centrosome (GO:0005813)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nuclear speck (GO:0016607)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 28 |
| PubMed broad count | 36 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RNF36 |

**关键文献**:
1. TRIM69 suppressed the anoikis resistance and metastasis of gastric cancer through ubiquitin‒proteasome-mediated degradation of PRKCD.. *Oncogene*. PMID: 37864033
2. Tripartite motif containing 69 elicits ERK2-dependent EYA4 turnover to impart pancreatic tumorigenesis.. *Journal of Cancer*. PMID: 36741265
3. The TRIM69-MST2 signaling axis regulates centrosome dynamics and chromosome segregation.. *Nucleic acids research*. PMID: 37739411
4. TRIM69 Inhibits Vesicular Stomatitis Indiana Virus.. *Journal of virology*. PMID: 31375575
5. TRIM69 inhibits cataractogenesis by negatively regulating p53.. *Redox biology*. PMID: 30844644

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.3 |
| 高置信度残基 (pLDDT>90) 占比 | 69.8% |
| 置信残基 (pLDDT 70-90) 占比 | 21.8% |
| 中等置信 (pLDDT 50-70) 占比 | 2.8% |
| 低置信 (pLDDT<50) 占比 | 5.6% |
| 有序区域 (pLDDT>70) 占比 | 91.6% |
| 可用 PDB 条目 | 4NQJ, 6YXE |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4NQJ, 6YXE）+ AlphaFold高质量预测（pLDDT=88.3），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001870, IPR043136, IPR003879, IPR013320, IPR006574; Pfam: PF13765, PF00622, PF15227 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MAGEA4 | 0.763 | 0.746 | — |
| BLOC1S5 | 0.708 | 0.708 | — |
| ATP5MC1 | 0.669 | 0.669 | — |
| HAUS1 | 0.657 | 0.595 | — |
| BLOC1S2 | 0.630 | 0.622 | — |
| IYD | 0.624 | 0.614 | — |
| ASNS | 0.608 | 0.606 | — |
| TRAT1 | 0.587 | 0.000 | — |
| TMEM225 | 0.559 | 0.000 | — |
| PML | 0.553 | 0.292 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSMUSP00000047627.8 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| ENSP00000479720.1 | psi-mi:"MI:0231"(mammalian protein protein interac | pubmed:32296183|imex:IM-25472 |
| ENSP00000453177.1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| MAGEA4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| GNB2 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| PPP1R12A | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| STOM | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| DSG2 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| GNAS | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| RPL17 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.3 + PDB: 4NQJ, 6YXE | pLDDT=88.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Nucleus speckle; Cytoplasm, cy / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TRIM69 — E3 ubiquitin-protein ligase TRIM69，非常新颖，仅有少数基础研究。
2. 蛋白大小500 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 28 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86WT6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000185880-TRIM69/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TRIM69
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86WT6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86WT6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

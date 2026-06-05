---
type: protein-evaluation
gene: "DMWD"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DMWD 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DMWD / DM9 |
| 蛋白名称 | Dystrophia myotonica WD repeat-containing protein |
| 蛋白大小 | 674 aa / 70.4 kDa |
| UniProt ID | Q09019 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane, Actin filaments; UniProt: Cytoplasm; Nucleus; Perikaryon; Cell projection, dendrite |
| 蛋白大小 | 10/10 | ×1 | 10 | 674 aa / 70.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR015943, IPR036322, IPR001680, IPR051362; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Actin filaments | Approved |
| UniProt | Cytoplasm; Nucleus; Perikaryon; Cell projection, dendrite | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- dendrite (GO:0030425)
- nucleus (GO:0005634)
- perikaryon (GO:0043204)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 19 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DM9 |

**关键文献**:
1. The dystrophia myotonica WD repeat-containing protein DMWD and WDR20 differentially regulate USP12 deubiquitinase.. *The FEBS journal*. PMID: 33844468
2. The DMWD protein from the myotonic dystrophy (DM1) gene region is developmentally regulated and is present most prominently in synapse-dense brain areas.. *Brain research*. PMID: 12691844
3. Real-time RT-PCR for CTG repeat-containing genes.. *Methods in molecular biology (Clifton, N.J.)*. PMID: 15201450
4. Computational and functional prioritization identifies genes that rescue behavior and reduce tau protein in fly and human cell models of Alzheimer disease.. *American journal of human genetics*. PMID: 40215969
5. Effect of triplet repeat expansion on chromatin structure and expression of DMPK and neighboring genes, SIX5 and DMWD, in myotonic dystrophy.. *Molecular genetics and metabolism*. PMID: 11592825

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.2 |
| 高置信度残基 (pLDDT>90) 占比 | 43.5% |
| 置信残基 (pLDDT 70-90) 占比 | 10.2% |
| 中等置信 (pLDDT 50-70) 占比 | 3.9% |
| 低置信 (pLDDT<50) 占比 | 42.4% |
| 有序区域 (pLDDT>70) 占比 | 53.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=67.2），有序残基占 53.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR015943, IPR036322, IPR001680, IPR051362; Pfam: PF00400 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| USP46 | 0.927 | 0.798 | — |
| RSPH6A | 0.895 | 0.094 | — |
| USP12 | 0.878 | 0.651 | — |
| SIX5 | 0.860 | 0.000 | — |
| DMPK | 0.811 | 0.067 | — |
| WDR48 | 0.752 | 0.409 | — |
| LARS1 | 0.686 | 0.095 | — |
| C20orf27 | 0.652 | 0.094 | — |
| MBNL1 | 0.644 | 0.000 | — |
| CLCN1 | 0.625 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PPBP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| SLX4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12200|pubmed:19596235 |
| USP12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| WDR48 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| SDF2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| OAT | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| CAPZB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| SARS2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| NDUFS2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| YWHAH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.2 + PDB: 无 | pLDDT=67.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Perikaryon; Cell projection, d / Plasma membrane, Actin filaments | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DMWD — Dystrophia myotonica WD repeat-containing protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小674 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=67.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q09019
- Protein Atlas: https://www.proteinatlas.org/ENSG00000185800-DMWD/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DMWD
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q09019
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000185800-DMWD/subcellular

![](https://images.proteinatlas.org/68172/1250_H11_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/68172/1250_H11_7_blue_red_green.jpg)
![](https://images.proteinatlas.org/68172/1255_H11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/68172/1255_H11_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/68172/1318_A10_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/68172/1318_A10_9_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q09019-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

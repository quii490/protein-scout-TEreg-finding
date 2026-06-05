---
type: protein-evaluation
gene: "NACC2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NACC2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NACC2 / BTBD14A, NAC2, RBB |
| 蛋白名称 | Nucleus accumbens-associated protein 2 |
| 蛋白大小 | 587 aa / 62.8 kDa |
| UniProt ID | Q96BF6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli, Mitochondria; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 587 aa / 62.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR018379, IPR000210, IPR011333, IPR050457; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Mitochondria | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- mitochondrion (GO:0005739)
- nucleolus (GO:0005730)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 15 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BTBD14A, NAC2, RBB |

**关键文献**:
1. Development of small-molecule tropomyosin receptor kinase (TRK) inhibitors for NTRK fusion cancers.. *Acta pharmaceutica Sinica. B*. PMID: 33643817
2. Dynamic BTB-domain filaments promote clustering of ZBTB proteins.. *Molecular cell*. PMID: 38996459
3. Critical domains for NACC2-NTRK2 fusion protein activation.. *PloS one*. PMID: 38935636
4. Integrative global co-expression analysis identifies key microRNA-target gene networks as key blood biomarkers for obesity.. *Minerva medica*. PMID: 35266657
5. Identification of biomarkers associated with ferroptosis in macrophages infected with Mycobacterium abscessus using bioinformatic tools.. *PloS one*. PMID: 39792889

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.7 |
| 高置信度残基 (pLDDT>90) 占比 | 26.2% |
| 置信残基 (pLDDT 70-90) 占比 | 14.3% |
| 中等置信 (pLDDT 50-70) 占比 | 6.0% |
| 低置信 (pLDDT<50) 占比 | 53.5% |
| 有序区域 (pLDDT>70) 占比 | 40.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=60.7），有序残基占 40.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018379, IPR000210, IPR011333, IPR050457; Pfam: PF10523, PF00651 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PPP1R26 | 0.592 | 0.114 | — |
| HINFP | 0.512 | 0.071 | — |
| ETV6 | 0.488 | 0.068 | — |
| SPI1 | 0.468 | 0.000 | — |
| BEND3 | 0.465 | 0.045 | — |
| QKI | 0.457 | 0.000 | — |
| RBL2 | 0.446 | 0.071 | — |
| RB1 | 0.434 | 0.071 | — |
| BEND6 | 0.431 | 0.000 | — |
| RB1CC1 | 0.428 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EPS8 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| HSPB8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| BCAN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| FHL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TRAPPC9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NACC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| FEM1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| OSBPL1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| GOPC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NPAS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.7 + PDB: 无 | pLDDT=60.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoli, Mitochondria | 一致 |
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
1. NACC2 — Nucleus accumbens-associated protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小587 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=60.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96BF6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000148411-NACC2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NACC2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96BF6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000148411-NACC2/subcellular

![](https://images.proteinatlas.org/52962/1050_C5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/52962/1050_C5_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/52962/861_H10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/52962/861_H10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/52962/880_H10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/52962/880_H10_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96BF6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

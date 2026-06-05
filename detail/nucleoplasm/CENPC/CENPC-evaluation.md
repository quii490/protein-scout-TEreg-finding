---
type: protein-evaluation
gene: "CENPC"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CENPC — REJECTED (研究热度过高 (PubMed strict=274，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CENPC / CENPC1, ICEN7 |
| 蛋白名称 | Centromere protein C |
| 蛋白大小 | 943 aa / 106.8 kDa |
| UniProt ID | Q03188 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear bodies, Kinetochore; 额外: Nucleoplasm, Midbody; UniProt: Nucleus; Chromosome, centromere, kinetochore; Chromosome, ce |
| 蛋白大小 | 8/10 | ×1 | 8 | 943 aa / 106.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=274 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=48.0; PDB: 5LSJ, 5LSK, 6MUO, 6MUP, 6SE6, 6SEE, 6SEF |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR028386, IPR028931, IPR028052, IPR025974, IPR014 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.5/180** | |
| **归一化总分** | | | **44.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies, Kinetochore; 额外: Nucleoplasm, Midbody | Supported |
| UniProt | Nucleus; Chromosome, centromere, kinetochore; Chromosome, centromere | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- condensed chromosome, centromeric region (GO:0000779)
- cytosol (GO:0005829)
- inner kinetochore (GO:0000939)
- kinetochore (GO:0000776)
- midbody (GO:0030496)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 274 |
| PubMed broad count | 413 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CENPC1, ICEN7 |

**关键文献**:
1. Protein Phosphatase 1 Regulatory Subunit PNUTS Prevents CENP-A Mislocalization and Chromosomal Instability.. *Molecular and cellular biology*. PMID: 40270285
2. A maize homolog of mammalian CENPC is a constitutive component of the inner kinetochore.. *The Plant cell*. PMID: 10402425
3. Centromere/kinetochore is assembled through CENP-C oligomerization.. *Molecular cell*. PMID: 37295434
4. DNA binding of centromere protein C (CENPC) is stabilized by single-stranded RNA.. *PLoS genetics*. PMID: 20140237
5. Functional roles of the interaction of Moa1 with CENP-C and Rec8 in meiosis of Schizosaccharomyces pombe.. *Yi chuan = Hereditas*. PMID: 39140145

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 48.0 |
| 高置信度残基 (pLDDT>90) 占比 | 7.8% |
| 置信残基 (pLDDT 70-90) 占比 | 11.8% |
| 中等置信 (pLDDT 50-70) 占比 | 7.4% |
| 低置信 (pLDDT<50) 占比 | 73.0% |
| 有序区域 (pLDDT>70) 占比 | 19.6% |
| 可用 PDB 条目 | 5LSJ, 5LSK, 6MUO, 6MUP, 6SE6, 6SEE, 6SEF, 7PII, 7QOO, 7R5R |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=48.0），有序残基占 19.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR028386, IPR028931, IPR028052, IPR025974, IPR014710; Pfam: PF11699, PF15620, PF15622 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CENPS | 0.999 | 0.800 | — |
| CENPN | 0.999 | 0.900 | — |
| CENPT | 0.999 | 0.800 | — |
| CENPA | 0.999 | 0.952 | — |
| CENPM | 0.999 | 0.926 | — |
| CENPH | 0.999 | 0.900 | — |
| CENPU | 0.999 | 0.931 | — |
| CENPL | 0.998 | 0.900 | — |
| CENPI | 0.998 | 0.800 | — |
| CENPK | 0.998 | 0.900 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000273853.6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:19503796|imex:IM-26679 |
| DAXX | psi-mi:"MI:0018"(two hybrid) | pubmed:9645950 |
| ELOC | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| MAPK14 | psi-mi:"MI:0018"(two hybrid) | pubmed:18624398|imex:IM-19021 |
| CENPA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12152|pubmed:19070575 |
| CENPW | psi-mi:"MI:0416"(fluorescence microscopy) | imex:IM-12152|pubmed:19070575 |
| centoromere protein C | psi-mi:"MI:0416"(fluorescence microscopy) | imex:IM-12152|pubmed:19070575 |
| Pten | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-11846|pubmed:17218262 |
| Dmel\CG9986 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Cenp-C | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=48.0 + PDB: 5LSJ, 5LSK, 6MUO, 6MUP, 6SE6,  | pLDDT=48.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome, centromere, kinetochore; Chro / Nuclear bodies, Kinetochore; 额外: Nucleoplasm, Midb | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CENPC — Centromere protein C，研究基础较多，新颖性有限。
2. 蛋白大小943 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 274 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=48.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 274 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q03188
- Protein Atlas: https://www.proteinatlas.org/ENSG00000145241-CENPC/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CENPC
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q03188
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (supported)。来源: https://www.proteinatlas.org/ENSG00000145241-CENPC/subcellular

![](https://images.proteinatlas.org/49740/1773_H8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/49740/1773_H8_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/49740/1914_D6_27_cr5c877788c353a_blue_red_green.jpg)
![](https://images.proteinatlas.org/49740/1914_D6_32_blue_red_green.jpg)
![](https://images.proteinatlas.org/49740/721_F3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/49740/721_F3_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q03188-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

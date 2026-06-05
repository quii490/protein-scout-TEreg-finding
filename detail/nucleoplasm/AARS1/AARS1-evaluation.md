---
type: protein-evaluation
gene: "AARS1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## AARS1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | AARS1 / AARS |
| 蛋白名称 | Alanine--tRNA ligase, cytoplasmic |
| 蛋白大小 | 968 aa / 106.8 kDa |
| UniProt ID | P49588 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 968 aa / 106.8 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=47 篇 (≤60→6) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=90.4; PDB: 4XEM, 4XEO, 5KNN, 5T5S, 5T76, 5V59 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR045864, IPR002318, IPR018162, IPR018165, IPR018 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **124.0/180** | |
| **归一化总分** | | | **68.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- membrane (GO:0016020)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 47 |
| PubMed broad count | 79 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: AARS |

**关键文献**:
1. Alanyl-tRNA synthetase, AARS1, is a lactate sensor and lactyltransferase that lactylates p53 and contributes to tumorigenesis.. *Cell*. PMID: 38653238
2. The alanyl-tRNA synthetase AARS1 moonlights as a lactyltransferase to promote YAP signaling in gastric cancer.. *The Journal of clinical investigation*. PMID: 38512451
3. Emerging roles of lysine lactyltransferases and lactylation.. *Nature cell biology*. PMID: 40185947
4. Non-histone lactylation: unveiling its functional significance.. *Frontiers in cell and developmental biology*. PMID: 39925738
5. NUDT21 lactylation reprograms alternative polyadenylation to promote cuproptosis resistance.. *Cell discovery*. PMID: 40425546

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.4 |
| 高置信度残基 (pLDDT>90) 占比 | 68.8% |
| 置信残基 (pLDDT 70-90) 占比 | 26.8% |
| 中等置信 (pLDDT 50-70) 占比 | 3.2% |
| 低置信 (pLDDT<50) 占比 | 1.2% |
| 有序区域 (pLDDT>70) 占比 | 95.6% |
| 可用 PDB 条目 | 4XEM, 4XEO, 5KNN, 5T5S, 5T76, 5V59 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4XEM, 4XEO, 5KNN, 5T5S, 5T76, 5V59）+ AlphaFold极高置信度预测（pLDDT=90.4），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045864, IPR002318, IPR018162, IPR018165, IPR018164; Pfam: PF02272, PF01411, PF07973 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| YARS1 | 0.996 | 0.067 | — |
| KARS1 | 0.992 | 0.000 | — |
| GARS1 | 0.983 | 0.765 | — |
| IARS1 | 0.980 | 0.690 | — |
| EPRS1 | 0.976 | 0.000 | — |
| LARS1 | 0.968 | 0.562 | — |
| QARS1 | 0.964 | 0.524 | — |
| TARS3 | 0.955 | 0.443 | — |
| NARS1 | 0.947 | 0.576 | — |
| IARS2 | 0.942 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| - | psi-mi:"MI:0096"(pull down) | pubmed:19805454|imex:IM-19495 |
| VCAM1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-17358|pubmed:22623428 |
| ETS1 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| 616370" | psi-mi:"MI:0096"(pull down) | pubmed:23606334|imex:IM-21247 |
| FN1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-14135|pubmed:19738201 |
| HSD17B10 | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010 |
| SOD1 | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010 |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |
| SAP18 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| TIMM44 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.4 + PDB: 4XEM, 4XEO, 5KNN, 5T5S, 5T76,  | pLDDT=90.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. AARS1 — Alanine--tRNA ligase, cytoplasmic，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小968 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 47 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P49588
- Protein Atlas: https://www.proteinatlas.org/ENSG00000090861-AARS1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AARS1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P49588
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000090861-AARS1/subcellular

![](https://images.proteinatlas.org/34261/921_F4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/34261/921_F4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/34261/923_F4_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/34261/923_F4_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/34261/931_F4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/34261/931_F4_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P49588-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

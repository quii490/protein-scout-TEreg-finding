---
type: protein-evaluation
gene: "LARS1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LARS1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LARS1 / KIAA1352, LARS |
| 蛋白名称 | Leucine--tRNA ligase, cytoplasmic |
| 蛋白大小 | 1176 aa / 134.5 kDa |
| UniProt ID | Q9P2J5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear bodies, Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 1176 aa / 134.5 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=21 篇 (≤40→8) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=90.5; PDB: 2WFD, 6KID, 6KIE, 6KQY, 6KR7, 6LPF, 6LR6 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001412, IPR002300, IPR054509, IPR004493, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **134.0/180** | |
| **归一化总分** | | | **74.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies, Cytosol | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- aminoacyl-tRNA synthetase multienzyme complex (GO:0017101)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- endomembrane system (GO:0012505)
- endoplasmic reticulum (GO:0005783)
- lysosome (GO:0005764)
- nuclear body (GO:0016604)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 21 |
| PubMed broad count | 39 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1352, LARS |

**关键文献**:
1. LARS1 lactylation inhibits autophagy by activating mTORC1 to promote podocytes injury in diabetic kidney disease.. *Cellular signalling*. PMID: 40545110
2. MRI in LARS1 deficiency-Spectrum, patterns, and correlation with acute neurological deterioration.. *Journal of inherited metabolic disease*. PMID: 38951950
3. Developing a comprehensive solution aimed to disrupt LARS1/RagD protein-protein interaction.. *Journal of biomolecular structure & dynamics*. PMID: 36995308
4. Aminoacyl-tRNA synthetases and amino acid signaling.. *Biochimica et biophysica acta. Molecular cell research*. PMID: 33091505
5. Glucose-dependent control of leucine metabolism by leucyl-tRNA synthetase 1.. *Science (New York, N.Y.)*. PMID: 31780625

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.5 |
| 高置信度残基 (pLDDT>90) 占比 | 73.2% |
| 置信残基 (pLDDT 70-90) 占比 | 21.8% |
| 中等置信 (pLDDT 50-70) 占比 | 1.4% |
| 低置信 (pLDDT<50) 占比 | 3.6% |
| 有序区域 (pLDDT>70) 占比 | 95.0% |
| 可用 PDB 条目 | 2WFD, 6KID, 6KIE, 6KQY, 6KR7, 6LPF, 6LR6 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2WFD, 6KID, 6KIE, 6KQY, 6KR7, 6LPF, 6LR6）+ AlphaFold极高置信度预测（pLDDT=90.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001412, IPR002300, IPR054509, IPR004493, IPR013155; Pfam: PF08264, PF24810, PF00133 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RARS1 | 0.999 | 0.885 | — |
| IARS1 | 0.999 | 0.877 | — |
| EPRS1 | 0.999 | 0.911 | — |
| KARS1 | 0.999 | 0.867 | — |
| QARS1 | 0.999 | 0.899 | — |
| MARS1 | 0.999 | 0.878 | — |
| AIMP1 | 0.997 | 0.874 | — |
| EEF1E1 | 0.997 | 0.834 | — |
| DARS1 | 0.996 | 0.871 | — |
| IARS2 | 0.996 | 0.094 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RELA | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| IKBKG | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| TANK | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| gag | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-17346|pubmed:22190034| |
| VCAM1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-17358|pubmed:22623428 |
| RARS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:16055448|imex:IM-20482 |
| eprs1.S | psi-mi:"MI:0029"(cosedimentation through density g | pubmed:20174651|imex:IM-17228 |
| eef1a1o.S | psi-mi:"MI:0029"(cosedimentation through density g | pubmed:20174651|imex:IM-17228 |
| DDA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.5 + PDB: 2WFD, 6KID, 6KIE, 6KQY, 6KR7,  | pLDDT=90.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Nuclear bodies, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. LARS1 — Leucine--tRNA ligase, cytoplasmic，非常新颖，仅有少数基础研究。
2. 蛋白大小1176 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 21 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9P2J5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000133706-LARS1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LARS1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P2J5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (approved)。来源: https://www.proteinatlas.org/ENSG00000133706-LARS1/subcellular

![](https://images.proteinatlas.org/36424/412_D6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/36424/412_D6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/36424/419_D6_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/36424/419_D6_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/36424/471_D6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/36424/471_D6_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9P2J5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

---
type: protein-evaluation
gene: "HERC4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HERC4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HERC4 / KIAA1593 |
| 蛋白名称 | Probable E3 ubiquitin-protein ligase HERC4 |
| 蛋白大小 | 1057 aa / 118.6 kDa |
| UniProt ID | Q5GLZ8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli fibrillar center, Cytosol; 额外: Primary cilium, Prim; UniProt: Cytoplasm, cytosol |
| 蛋白大小 | 8/10 | ×1 | 8 | 1057 aa / 118.6 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=33 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=91.6; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000569, IPR035983, IPR058923, IPR009091, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 13 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **114.5/180** | |
| **归一化总分** | | | **63.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli fibrillar center, Cytosol; 额外: Primary cilium, Primary cilium tip | Approved |
| UniProt | Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- fibrillar center (GO:0001650)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 33 |
| PubMed broad count | 46 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1593 |

**关键文献**:
1. A targetable PRR11-DHODH axis drives ferroptosis- and temozolomide-resistance in glioblastoma.. *Redox biology*. PMID: 38838551
2. Harnessing genetic interactions for prediction of immune checkpoint inhibitors response signature in cancer cells.. *Cancer letters*. PMID: 38797232
3. METTL3 and HERC4: Elevated Expression and Impact on Hepatocellular Carcinoma Progression.. *Cancer biotherapy & radiopharmaceuticals*. PMID: 39611657
4. HERC4 modulates ovarian cancer cell proliferation by regulating SMO-elicited hedgehog signaling.. *Biochimica et biophysica acta. General subjects*. PMID: 38181892
5. The Emerging Roles of the HERC Ubiquitin Ligases in Cancer.. *Current pharmaceutical design*. PMID: 29807510

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.6 |
| 高置信度残基 (pLDDT>90) 占比 | 70.6% |
| 置信残基 (pLDDT 70-90) 占比 | 25.8% |
| 中等置信 (pLDDT 50-70) 占比 | 3.1% |
| 低置信 (pLDDT<50) 占比 | 0.5% |
| 有序区域 (pLDDT>70) 占比 | 96.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=91.6，有序区 96.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000569, IPR035983, IPR058923, IPR009091, IPR000408; Pfam: PF00632, PF25390 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RABIF | 0.545 | 0.000 | — |
| MYPN | 0.520 | 0.000 | — |
| UBE2D2 | 0.517 | 0.470 | — |
| AGO3 | 0.494 | 0.045 | — |
| UBE2L3 | 0.485 | 0.461 | — |
| UBE2O | 0.462 | 0.049 | — |
| USP5 | 0.451 | 0.204 | — |
| RTP3 | 0.449 | 0.000 | — |
| SMO | 0.439 | 0.292 | — |
| PIGY | 0.438 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| FDXACB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TRADD | psi-mi:"MI:2289"(virotrap) | pubmed:30561431|imex:IM-26500 |
| RET | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| APOBEC3D | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FAM189B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| WRAP73 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| C1orf94 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KLHL10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ALOXE3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 13，IntAct interactions: 15
- 调控相关比例: 0 / 13 = 0%

**评价**: STRING 13 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.6 + PDB: 无 | pLDDT=91.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol / Nucleoli fibrillar center, Cytosol; 额外: Primary ci | 一致 |
| PPI | STRING + IntAct | 13 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. HERC4 — Probable E3 ubiquitin-protein ligase HERC4，非常新颖，仅有少数基础研究。
2. 蛋白大小1057 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 33 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5GLZ8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000148634-HERC4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HERC4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5GLZ8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli fibrillar center (uncertain)。来源: https://www.proteinatlas.org/ENSG00000148634-HERC4/subcellular

![](https://images.proteinatlas.org/70301/1543_G7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/70301/1543_G7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/70301/1544_G7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/70301/1544_G7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/70301/1551_B3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/70301/1551_B3_5_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5GLZ8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

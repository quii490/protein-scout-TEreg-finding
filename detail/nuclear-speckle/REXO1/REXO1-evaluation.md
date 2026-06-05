---
type: protein-evaluation
gene: "REXO1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## REXO1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | REXO1 / ELOABP1, KIAA1138, TCEB3BP1 |
| 蛋白名称 | RNA exonuclease 1 homolog |
| 蛋白大小 | 1221 aa / 131.5 kDa |
| UniProt ID | Q8N1G1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Nuclear bodies; UniProt: Nucleus |
| 蛋白大小 | 5/10 | ×1 | 5 | 1221 aa / 131.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR034922, IPR031736, IPR047021, IPR013520, IPR012 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 10 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.0/180** | |
| **归一化总分** | | | **73.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear bodies | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 11 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ELOABP1, KIAA1138, TCEB3BP1 |

**关键文献**:
1. Unveiling the prognostic value of ARID3A in breast cancer through bioinformatic analysis.. *Heliyon*. PMID: 40028521
2. Conserved domains and structural motifs that differentiate closely related Rex1 and Rex3 DEDDh exoribonucleases are required for their function in yeast.. *PloS one*. PMID: 40455837
3. Effect of primary culture medium type for culture of canine fibroblasts on production of cloned dogs.. *Theriogenology*. PMID: 26001598
4. Circ-CCDC66 upregulates REXO1 expression to aggravate cervical cancer progression via restraining miR-452-5p.. *Cancer cell international*. PMID: 33407514

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.0 |
| 高置信度残基 (pLDDT>90) 占比 | 18.4% |
| 置信残基 (pLDDT 70-90) 占比 | 17.9% |
| 中等置信 (pLDDT 50-70) 占比 | 8.9% |
| 低置信 (pLDDT<50) 占比 | 54.7% |
| 有序区域 (pLDDT>70) 占比 | 36.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=58.0），有序残基占 36.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR034922, IPR031736, IPR047021, IPR013520, IPR012337; Pfam: PF15870 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ELOA | 0.958 | 0.512 | — |
| REXO2 | 0.946 | 0.106 | — |
| REXO5 | 0.916 | 0.000 | — |
| SCAF1 | 0.815 | 0.000 | — |
| ERF | 0.768 | 0.000 | — |
| TCEA1 | 0.752 | 0.071 | — |
| ELOA2 | 0.694 | 0.045 | — |
| ZNF777 | 0.667 | 0.060 | — |
| PCNA | 0.658 | 0.416 | — |
| SNAPC4 | 0.621 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PAFAH1B2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| Cdk9 | psi-mi:"MI:0096"(pull down) | pubmed:20593818|imex:IM-17619 |
| H3-4 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| UBA52 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| AP2M1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Rprd1b | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| DGCR6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CG17159 | psi-mi:"MI:0397"(two hybrid array) | pubmed:37061542|imex:IM-28761 |
| ENST00000170168 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |
| SMNDC1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-30059|pubmed:39251607 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 10
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 10 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.0 + PDB: 无 | pLDDT=58.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 10 interactions | 数据充分 |

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
1. REXO1 — RNA exonuclease 1 homolog，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1221 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=58.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N1G1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000079313-REXO1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=REXO1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N1G1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000079313-REXO1/subcellular

![](https://images.proteinatlas.org/42552/481_H3_1_red_green.jpg)
![](https://images.proteinatlas.org/42552/481_H3_2_red_green.jpg)
![](https://images.proteinatlas.org/42552/487_H3_1_red_green.jpg)
![](https://images.proteinatlas.org/42552/487_H3_3_red_green.jpg)
![](https://images.proteinatlas.org/42552/491_H3_1_red_green.jpg)
![](https://images.proteinatlas.org/42552/491_H3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N1G1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

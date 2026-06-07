---
type: protein-evaluation
gene: "EPAS1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EPAS1 — REJECTED (研究热度过高 (PubMed strict=548，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EPAS1 / BHLHE73, HIF2A, MOP2, PASD2 |
| 蛋白名称 | Endothelial PAS domain-containing protein 1 |
| 蛋白大小 | 870 aa / 96.5 kDa |
| UniProt ID | Q99814 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Actin filaments, Cytokinetic bridge, Cytoso; UniProt: Nucleus; Nucleus speckle |
| 蛋白大小 | 8/10 | ×1 | 8 | 870 aa / 96.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=548 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.6; PDB: 1P97, 2A24, 3F1N, 3F1O, 3F1P, 3H7W, 3H82 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011598, IPR014887, IPR021537, IPR036638, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.0/180** | |
| **归一化总分** | | | **43.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Actin filaments, Cytokinetic bridge, Cytosol | Supported |
| UniProt | Nucleus; Nucleus speckle | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 548 |
| PubMed broad count | 789 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BHLHE73, HIF2A, MOP2, PASD2 |

**关键文献**:
1. Endothelial FUNDC1 Deficiency Drives Pulmonary Hypertension.. *Circulation research*. PMID: 39655444
2. Microbial Metabolite Signaling Is Required for Systemic Iron Homeostasis.. *Cell metabolism*. PMID: 31708445
3. Comprehensive Molecular Characterization of Pheochromocytoma and Paraganglioma.. *Cancer cell*. PMID: 28162975
4. On-target efficacy of a HIF-2α antagonist in preclinical kidney cancer models.. *Nature*. PMID: 27595393
5. Sequencing of 50 human exomes reveals adaptation to high altitude.. *Science (New York, N.Y.)*. PMID: 20595611

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.6 |
| 高置信度残基 (pLDDT>90) 占比 | 29.1% |
| 置信残基 (pLDDT 70-90) 占比 | 6.1% |
| 中等置信 (pLDDT 50-70) 占比 | 11.7% |
| 低置信 (pLDDT<50) 占比 | 53.1% |
| 有序区域 (pLDDT>70) 占比 | 35.2% |
| 可用 PDB 条目 | 1P97, 2A24, 3F1N, 3F1O, 3F1P, 3H7W, 3H82, 4GHI, 4GS9, 4PKY |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=58.6），有序残基占 35.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR014887, IPR021537, IPR036638, IPR001067; Pfam: PF23171, PF11413, PF08778 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EGLN1 | 0.999 | 0.893 | — |
| VHL | 0.999 | 0.993 | — |
| ARNT | 0.999 | 0.994 | — |
| EGLN3 | 0.999 | 0.743 | — |
| EP300 | 0.998 | 0.690 | — |
| HIF1A | 0.998 | 0.331 | — |
| EGLN2 | 0.998 | 0.622 | — |
| ARNT2 | 0.998 | 0.704 | — |
| HIF3A | 0.997 | 0.301 | — |
| ELOB | 0.995 | 0.853 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.6 + PDB: 1P97, 2A24, 3F1N, 3F1O, 3F1P,  | pLDDT=58.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus speckle / Nucleoplasm; 额外: Actin filaments, Cytokinetic brid | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. EPAS1 — Endothelial PAS domain-containing protein 1，研究基础较多，新颖性有限。
2. 蛋白大小870 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 548 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=58.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 548 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q99814
- Protein Atlas: https://www.proteinatlas.org/ENSG00000116016-EPAS1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EPAS1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99814
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000116016-EPAS1/subcellular

![](https://images.proteinatlas.org/31200/1391_B7_1_red_green.jpg)
![](https://images.proteinatlas.org/31200/1391_B7_2_red_green.jpg)
![](https://images.proteinatlas.org/69697/1382_A10_1_red_green.jpg)
![](https://images.proteinatlas.org/69697/1382_A10_2_red_green.jpg)
![](https://images.proteinatlas.org/69697/1419_A10_1_red_green.jpg)
![](https://images.proteinatlas.org/69697/1419_A10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q99814-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q99814 |
| SMART | SM00353;SM00086;SM00091; |
| UniProt Domain [FT] | DOMAIN 14..67; /note="bHLH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00981"; DOMAIN 84..154; /note="PAS 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00140"; DOMAIN 230..300; /note="PAS 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00140"; DOMAIN 304..347; /note="PAC" |
| InterPro | IPR011598;IPR014887;IPR021537;IPR036638;IPR001067;IPR001610;IPR000014;IPR035965;IPR013767; |
| Pfam | PF23171;PF11413;PF08778;PF00989;PF14598; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000116016-EPAS1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ARNT | Intact, Biogrid | true |
| EGLN1 | Intact, Biogrid | true |
| SMAD3 | Intact, Biogrid | true |
| VHL | Intact, Biogrid | true |
| ARNT2 | Biogrid | false |
| BBS4 | Intact | false |
| CHD4 | Biogrid | false |
| CREBBP | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

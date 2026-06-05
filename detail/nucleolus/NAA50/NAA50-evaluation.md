---
type: protein-evaluation
gene: "NAA50"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NAA50 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NAA50 / MAK3, NAT13, NAT5 |
| 蛋白名称 | N-alpha-acetyltransferase 50 |
| 蛋白大小 | 169 aa / 19.4 kDa |
| UniProt ID | Q9GZZ1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 169 aa / 19.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=32 篇 (≤40→8) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=92.2; PDB: 2OB0, 2PSW, 3TFY, 4X5K, 6PPL, 6PW9, 6WF3 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR016181, IPR000182, IPR051556; Pfam: PF00583 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **134.0/180** | |
| **归一化总分** | | | **74.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- NatA complex (GO:0031415)
- nucleolus (GO:0005730)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 32 |
| PubMed broad count | 49 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MAK3, NAT13, NAT5 |

**关键文献**:
1. Structural and functional characterization of the N-terminal acetyltransferase Naa50.. *Structure (London, England : 1993)*. PMID: 33400917
2. Chemoproteomics Yields a Selective Molecular Host for Acetyl-CoA.. *Journal of the American Chemical Society*. PMID: 37486078
3. Structure and Mechanism of Acetylation by the N-Terminal Dual Enzyme NatA/Naa50 Complex.. *Structure (London, England : 1993)*. PMID: 31155310
4. Molecular basis for N-terminal acetylation by human NatE and its modulation by HYPK.. *Nature communications*. PMID: 32042062
5. Pan-cancer analysis reveals NAA50 as a cancer prognosis and immune infiltration-related biomarker.. *Frontiers in genetics*. PMID: 36568377

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.2 |
| 高置信度残基 (pLDDT>90) 占比 | 88.8% |
| 置信残基 (pLDDT 70-90) 占比 | 1.2% |
| 中等置信 (pLDDT 50-70) 占比 | 2.4% |
| 低置信 (pLDDT<50) 占比 | 7.7% |
| 有序区域 (pLDDT>70) 占比 | 90.0% |
| 可用 PDB 条目 | 2OB0, 2PSW, 3TFY, 4X5K, 6PPL, 6PW9, 6WF3, 6WF5, 6WFG, 6WFK |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2OB0, 2PSW, 3TFY, 4X5K, 6PPL, 6PW9, 6WF3, 6WF5, 6WFG, 6WFK）+ AlphaFold极高置信度预测（pLDDT=92.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016181, IPR000182, IPR051556; Pfam: PF00583 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NAA15 | 0.999 | 0.996 | — |
| NAA10 | 0.999 | 0.994 | — |
| HYPK | 0.998 | 0.937 | — |
| NAA16 | 0.995 | 0.930 | — |
| NAA11 | 0.988 | 0.855 | — |
| NAA20 | 0.934 | 0.000 | — |
| NAA35 | 0.921 | 0.000 | — |
| NAA40 | 0.906 | 0.000 | — |
| NAA25 | 0.882 | 0.000 | — |
| NAA38 | 0.881 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Q3TH79 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| TRAF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EIF1B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| Naa15 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Naa10 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| HSD17B10 | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010 |
| SFXN1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| DLD | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010 |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |
| TANK | psi-mi:"MI:2289"(virotrap) | pubmed:30561431|imex:IM-26500 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.2 + PDB: 2OB0, 2PSW, 3TFY, 4X5K, 6PPL,  | pLDDT=92.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoli | 一致 |
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
1. NAA50 — N-alpha-acetyltransferase 50，非常新颖，仅有少数基础研究。
2. 蛋白大小169 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 32 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9GZZ1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000121579-NAA50/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NAA50
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9GZZ1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (supported)。来源: https://www.proteinatlas.org/ENSG00000121579-NAA50/subcellular

![](https://images.proteinatlas.org/74489/1433_C8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/74489/1433_C8_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/74489/1435_C8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/74489/1435_C8_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/74489/1685_E3_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/74489/1685_E3_5_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9GZZ1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

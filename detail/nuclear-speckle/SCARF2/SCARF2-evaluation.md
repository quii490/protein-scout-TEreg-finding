---
type: protein-evaluation
gene: "SCARF2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SCARF2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SCARF2 / SREC2, SREPCR |
| 蛋白名称 | Scavenger receptor class F member 2 |
| 蛋白大小 | 871 aa / 92.4 kDa |
| UniProt ID | Q96GP6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Nuclear bodies, Cytosol; UniProt: Membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 871 aa / 92.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=32 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000742, IPR009030, IPR002049, IPR042635 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **105.5/180** | |
| **归一化总分** | | | **58.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear bodies, Cytosol | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- focal adhesion (GO:0005925)
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 32 |
| PubMed broad count | 42 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SREC2, SREPCR |

**关键文献**:
1. SCARF2 is a target for chronic obstructive pulmonary disease: Evidence from multi-omics research and cohort validation.. *Aging cell*. PMID: 38958042
2. Structure of scavenger receptor SCARF1 and its interaction with lipoproteins.. *eLife*. PMID: 39541158
3. Results of next-generation sequencing gene panel diagnostics including copy-number variation analysis in 810 patients suspected of heritable thoracic aortic disorders.. *Human mutation*. PMID: 29907982
4. Scavenger receptor class F member 2 is an intracellular receptor for hepatitis B virus.. *Cell*. PMID: 42167249
5. Exploring causal plasma protein level ratios and potential drug targets for depression: A proteomics Mendelian randomization study.. *Journal of affective disorders*. PMID: 40499826

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.5 |
| 高置信度残基 (pLDDT>90) 占比 | 25.4% |
| 置信残基 (pLDDT 70-90) 占比 | 21.7% |
| 中等置信 (pLDDT 50-70) 占比 | 6.3% |
| 低置信 (pLDDT<50) 占比 | 46.6% |
| 有序区域 (pLDDT>70) 占比 | 47.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=64.5），有序残基占 47.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000742, IPR009030, IPR002049, IPR042635 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KLHL22 | 0.617 | 0.217 | — |
| ZNF74 | 0.589 | 0.047 | — |
| EGF | 0.536 | 0.133 | — |
| CALM1 | 0.491 | 0.000 | — |
| TGM3 | 0.489 | 0.000 | — |
| LZTR1 | 0.484 | 0.000 | — |
| SPATA6 | 0.479 | 0.000 | — |
| TANGO2 | 0.468 | 0.000 | — |
| AIFM3 | 0.463 | 0.000 | — |
| SNAP29 | 0.450 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=64.5 + PDB: 无 | pLDDT=64.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm; 额外: Nuclear bodies, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. SCARF2 — Scavenger receptor class F member 2，非常新颖，仅有少数基础研究。
2. 蛋白大小871 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 32 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=64.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96GP6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000244486-SCARF2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SCARF2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96GP6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000244486-SCARF2/subcellular

![](https://images.proteinatlas.org/35079/2013_C8_1_red_green.jpg)
![](https://images.proteinatlas.org/35079/2013_C8_2_red_green.jpg)
![](https://images.proteinatlas.org/35079/378_H5_1_red_green.jpg)
![](https://images.proteinatlas.org/35079/378_H5_3_red_green.jpg)
![](https://images.proteinatlas.org/35079/383_H5_3_red_green.jpg)
![](https://images.proteinatlas.org/35079/383_H5_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96GP6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

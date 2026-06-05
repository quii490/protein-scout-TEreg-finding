---
type: protein-evaluation
gene: "HIKESHI"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HIKESHI 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HIKESHI / C11orf73 |
| 蛋白名称 | Protein Hikeshi |
| 蛋白大小 | 197 aa / 21.6 kDa |
| UniProt ID | Q53FT3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; 额外: Nucleoplasm, Nuclear bodies; UniProt: Cytoplasm; Cytoplasm, cytosol; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 197 aa / 21.6 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=24 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=88.9; PDB: 3WVZ, 3WW0 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR048364, IPR008493, IPR031318; Pfam: PF21057, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles; 额外: Nucleoplasm, Nuclear bodies | Approved |
| UniProt | Cytoplasm; Cytoplasm, cytosol; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nuclear body (GO:0016604)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 24 |
| PubMed broad count | 35 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C11orf73 |

**关键文献**:
1. Thermal Stress and Nuclear Transport.. *Advances in experimental medicine and biology*. PMID: 39289274
2. Functional analysis of the Hikeshi-like protein and its interaction with HSP70 in Arabidopsis.. *Biochemical and biophysical research communications*. PMID: 24942879
3. A novel missense variant in HIKESHI: Clinical phenotype, in vitro functional testing, and potential for gene therapy.. *American journal of medical genetics. Part A*. PMID: 38922739
4. Leukoencephalopathy and early death associated with an Ashkenazi-Jewish founder mutation in the Hikeshi gene.. *Journal of medical genetics*. PMID: 26545878
5. Heat stress-induced nuclear transport mediated by Hikeshi confers nuclear function of Hsp70s.. *Current opinion in cell biology*. PMID: 29490261

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.9 |
| 高置信度残基 (pLDDT>90) 占比 | 66.5% |
| 置信残基 (pLDDT 70-90) 占比 | 23.9% |
| 中等置信 (pLDDT 50-70) 占比 | 9.6% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 90.4% |
| 可用 PDB 条目 | 3WVZ, 3WW0 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3WVZ, 3WW0）+ AlphaFold高质量预测（pLDDT=88.9），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR048364, IPR008493, IPR031318; Pfam: PF21057, PF05603 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HSPA4 | 0.849 | 0.091 | — |
| HSPA8 | 0.750 | 0.328 | — |
| HSPA1B | 0.715 | 0.328 | — |
| DNAJB1 | 0.680 | 0.071 | — |
| NUP62 | 0.627 | 0.292 | — |
| HSPA6 | 0.616 | 0.091 | — |
| RCVRN | 0.610 | 0.610 | — |
| CLPB | 0.602 | 0.000 | — |
| HSPA14 | 0.598 | 0.091 | — |
| HSPA13 | 0.597 | 0.091 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HSPA8 | psi-mi:"MI:0096"(pull down) | pubmed:22541429|imex:IM-17341 |
| HSPA1A | psi-mi:"MI:0096"(pull down) | pubmed:22541429|imex:IM-17341 |
| Nup153 | psi-mi:"MI:0096"(pull down) | pubmed:22541429|imex:IM-17341 |
| NUP62 | psi-mi:"MI:0096"(pull down) | pubmed:22541429|imex:IM-17341 |
| EBI-6095589 | psi-mi:"MI:0096"(pull down) | pubmed:21712045|imex:IM-17900 |
| ZNF581 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SIRPD | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PHB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ABLIM3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| OTX2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.9 + PDB: 3WVZ, 3WW0 | pLDDT=88.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, cytosol; Nucleus / Nuclear speckles; 额外: Nucleoplasm, Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. HIKESHI — Protein Hikeshi，非常新颖，仅有少数基础研究。
2. 蛋白大小197 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 24 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q53FT3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000149196-HIKESHI/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HIKESHI
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q53FT3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000149196-HIKESHI/subcellular

![](https://images.proteinatlas.org/12708/1858_H3_34_red_green.jpg)
![](https://images.proteinatlas.org/12708/1858_H3_35_red_green.jpg)
![](https://images.proteinatlas.org/12708/1907_F7_1_red_green.jpg)
![](https://images.proteinatlas.org/12708/1907_F7_2_red_green.jpg)
![](https://images.proteinatlas.org/12708/1913_G13_1_red_green.jpg)
![](https://images.proteinatlas.org/12708/1913_G13_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q53FT3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

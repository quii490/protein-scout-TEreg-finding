---
type: protein-evaluation
gene: "CTNND2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CTNND2 — REJECTED (研究热度过高 (PubMed strict=101，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CTNND2 / NPRAP |
| 蛋白名称 | Catenin delta-2 |
| 蛋白大小 | 1225 aa / 132.7 kDa |
| UniProt ID | Q9UQB3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cell Junctions; 额外: Cytosol; UniProt: Nucleus; Cell junction, adherens junction; Cell projection,  |
| 蛋白大小 | 5/10 | ×1 | 5 | 1225 aa / 132.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=101 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011989, IPR016024, IPR000225, IPR028435; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **75.0/180** | |
| **归一化总分** | | | **41.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cell Junctions; 额外: Cytosol | Approved |
| UniProt | Nucleus; Cell junction, adherens junction; Cell projection, dendrite; Perikaryon | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- adherens junction (GO:0005912)
- cytoplasm (GO:0005737)
- dendrite (GO:0030425)
- nucleus (GO:0005634)
- perikaryon (GO:0043204)
- plasma membrane (GO:0005886)
- postsynaptic density (GO:0014069)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 101 |
| PubMed broad count | 148 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NPRAP |

**关键文献**:
1. Cri du Chat syndrome.. *Orphanet journal of rare diseases*. PMID: 16953888
2. The integrated landscape of driver genomic alterations in glioblastoma.. *Nature genetics*. PMID: 23917401
3. CTNND2 moderates the pace of synaptic maturation and links human evolution to synaptic neoteny.. *Cell reports*. PMID: 39352808
4. CTNND2 gene expression in melanoma tissues and its effects on the malignant biological functions of melanoma cells.. *Translational cancer research*. PMID: 39697757
5. Characterization of CTNND2-related neurodevelopmental disease, phenotype-genotype spectrum and WNT dynamics in early neurogenesis.. *Research square*. PMID: 41502569

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.5 |
| 高置信度残基 (pLDDT>90) 占比 | 30.8% |
| 置信残基 (pLDDT 70-90) 占比 | 6.4% |
| 中等置信 (pLDDT 50-70) 占比 | 5.2% |
| 低置信 (pLDDT<50) 占比 | 57.6% |
| 有序区域 (pLDDT>70) 占比 | 37.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=58.5），有序残基占 37.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR000225, IPR028435; Pfam: PF00514 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PSEN1 | 0.991 | 0.292 | — |
| CDH17 | 0.991 | 0.134 | — |
| ZBTB33 | 0.945 | 0.328 | — |
| PDZD2 | 0.925 | 0.292 | — |
| LEF1 | 0.919 | 0.000 | — |
| TCF7L1 | 0.915 | 0.000 | — |
| TCF7L2 | 0.912 | 0.000 | — |
| TCF7 | 0.904 | 0.000 | — |
| CDH1 | 0.862 | 0.134 | — |
| LRRC7 | 0.827 | 0.369 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Pex5l | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |
| DLG1 | psi-mi:"MI:0900"(p8 filamentous phage display) | imex:IM-26482|pubmed:30126976 |
| DLG4 | psi-mi:"MI:0900"(p8 filamentous phage display) | imex:IM-26482|pubmed:30126976 |
| SCRIB | psi-mi:"MI:0900"(p8 filamentous phage display) | imex:IM-26482|pubmed:30126976 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| DISC1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| PSEN1 | psi-mi:"MI:0096"(pull down) | pubmed:27036734|imex:IM-25035 |
| ZMYND19 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TRIM47 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NUDT12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.5 + PDB: 无 | pLDDT=58.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cell junction, adherens junction; Cell pr / Nucleoplasm, Cell Junctions; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CTNND2 — Catenin delta-2，研究基础较多，新颖性有限。
2. 蛋白大小1225 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 101 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=58.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 101 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UQB3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000169862-CTNND2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CTNND2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UQB3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000169862-CTNND2/subcellular

![](https://images.proteinatlas.org/71124/1783_H8_1_red_green.jpg)
![](https://images.proteinatlas.org/71124/1783_H8_2_red_green.jpg)
![](https://images.proteinatlas.org/71124/1824_B5_2_red_green.jpg)
![](https://images.proteinatlas.org/71124/1824_B5_5_red_green.jpg)
![](https://images.proteinatlas.org/71124/1893_J18_19_cr5bbf4ea76f952_red_green.jpg)
![](https://images.proteinatlas.org/71124/1893_J18_28_cr5bbf4ea76fbc2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UQB3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

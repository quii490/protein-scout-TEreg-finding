---
type: protein-evaluation
gene: "IDH1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## IDH1 — REJECTED (研究热度过高 (PubMed strict=2348，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | IDH1 / PICD |
| 蛋白名称 | Isocitrate dehydrogenase [NADP] cytoplasmic |
| 蛋白大小 | 414 aa / 46.7 kDa |
| UniProt ID | O75874 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nuclear bodies, Cytosol; UniProt: Cytoplasm, cytosol; Peroxisome |
| 蛋白大小 | 10/10 | ×1 | 10 | 414 aa / 46.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=2348 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=95.9; PDB: 1T09, 1T0L, 3INM, 3MAP, 3MAR, 3MAS, 4I3K |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR019818, IPR004790, IPR024084; Pfam: PF00180 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **84.0/180** | |
| **归一化总分** | | | **46.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies, Cytosol | Approved |
| UniProt | Cytoplasm, cytosol; Peroxisome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- extracellular region (GO:0005576)
- ficolin-1-rich granule lumen (GO:1904813)
- mitochondrion (GO:0005739)
- peroxisomal matrix (GO:0005782)
- peroxisome (GO:0005777)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2348 |
| PubMed broad count | 6452 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PICD |

**关键文献**:
1. IDH1 and IDH2 mutations in gliomas.. *The New England journal of medicine*. PMID: 19228619
2. An integrated genomic analysis of human glioblastoma multiforme.. *Science (New York, N.Y.)*. PMID: 18772396
3. Mutant IDH1 inhibition induces dsDNA sensing to activate tumor immunity.. *Science (New York, N.Y.)*. PMID: 38991060
4. Cancer-associated IDH1 mutations produce 2-hydroxyglutarate.. *Nature*. PMID: 19935646
5. A Phase Ib/II Study of Ivosidenib with Venetoclax ± Azacitidine in IDH1-Mutated Myeloid Malignancies.. *Blood cancer discovery*. PMID: 37102976

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 95.9 |
| 高置信度残基 (pLDDT>90) 占比 | 94.7% |
| 置信残基 (pLDDT 70-90) 占比 | 4.8% |
| 中等置信 (pLDDT 50-70) 占比 | 0.5% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 99.5% |
| 可用 PDB 条目 | 1T09, 1T0L, 3INM, 3MAP, 3MAR, 3MAS, 4I3K, 4I3L, 4KZO, 4L03 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1T09, 1T0L, 3INM, 3MAP, 3MAR, 3MAS, 4I3K, 4I3L, 4KZO, 4L03）+ AlphaFold极高置信度预测（pLDDT=95.9），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019818, IPR004790, IPR024084; Pfam: PF00180 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ACO1 | 0.998 | 0.054 | — |
| ACO2 | 0.998 | 0.067 | — |
| IDH3G | 0.996 | 0.611 | — |
| CS | 0.993 | 0.162 | — |
| OGDH | 0.990 | 0.000 | — |
| IDH3B | 0.988 | 0.611 | — |
| IDH3A | 0.987 | 0.389 | — |
| OGDHL | 0.981 | 0.000 | — |
| GLUD1 | 0.973 | 0.069 | — |
| MDH2 | 0.970 | 0.293 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Vamp7 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| grim | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| IDH2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| Idh | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| ZHX1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| Bet3 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| 14-3-3zeta | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| HMT1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:14690591 |
| SPT7 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-15346|pubmed:21734642 |
| SPT8 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-15346|pubmed:21734642 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=95.9 + PDB: 1T09, 1T0L, 3INM, 3MAP, 3MAR,  | pLDDT=95.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Peroxisome / Nuclear bodies, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. IDH1 — Isocitrate dehydrogenase [NADP] cytoplasmic，研究基础较多，新颖性有限。
2. 蛋白大小414 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2348 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 2348 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75874
- Protein Atlas: https://www.proteinatlas.org/ENSG00000138413-IDH1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=IDH1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75874
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (uncertain)。来源: https://www.proteinatlas.org/ENSG00000138413-IDH1/subcellular

![](https://images.proteinatlas.org/62556/1538_D1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/62556/1538_D1_6_blue_red_green.jpg)
![](https://images.proteinatlas.org/62556/1539_D1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/62556/1539_D1_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/62556/1540_D1_7_blue_red_green.jpg)
![](https://images.proteinatlas.org/62556/1540_D1_9_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O75874-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

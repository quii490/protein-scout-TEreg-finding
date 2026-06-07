---
type: protein-evaluation
gene: "PVALB"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PVALB — REJECTED (研究热度过高 (PubMed strict=159，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PVALB |
| 蛋白名称 | Parvalbumin alpha |
| 蛋白大小 | 110 aa / 12.1 kDa |
| UniProt ID | P20472 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Nucleoli, Cell Junctions; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 110 aa / 12.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=159 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=95.8; PDB: 1RJV, 1RK9, 9BB8 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011992, IPR018247, IPR002048, IPR008080; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.0/180** | |
| **归一化总分** | | | **43.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli, Cell Junctions | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- axon (GO:0030424)
- cytoplasm (GO:0005737)
- synapse (GO:0045202)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 159 |
| PubMed broad count | 270 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. The thalamic reticular nucleus orchestrates social memory.. *Neuron*. PMID: 38701789
2. Identification of epilepsy-associated neuronal subtypes and gene expression underlying epileptogenesis.. *Nature communications*. PMID: 33028830
3. Identification of early Alzheimer's disease subclass and signature genes based on PANoptosis genes.. *Frontiers in immunology*. PMID: 39650656
4. Targeting SARM1 improves autophagic stress-induced axonal neuropathy.. *Autophagy*. PMID: 37561040
5. Phenotypic variation of transcriptomic cell types in mouse motor cortex.. *Nature*. PMID: 33184512

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 95.8 |
| 高置信度残基 (pLDDT>90) 占比 | 97.3% |
| 置信残基 (pLDDT 70-90) 占比 | 2.7% |
| 中等置信 (pLDDT 50-70) 占比 | 0.0% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 100.0% |
| 可用 PDB 条目 | 1RJV, 1RK9, 9BB8 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1RJV, 1RK9, 9BB8）+ AlphaFold高质量预测（pLDDT=95.8），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011992, IPR018247, IPR002048, IPR008080; Pfam: PF13499 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GAD1 | 0.968 | 0.091 | — |
| CALB2 | 0.967 | 0.000 | — |
| CALB1 | 0.964 | 0.000 | — |
| SST | 0.937 | 0.000 | — |
| MECP2 | 0.886 | 0.000 | — |
| S100G | 0.863 | 0.116 | — |
| SDF4 | 0.845 | 0.000 | — |
| GAD2 | 0.835 | 0.091 | — |
| NPY | 0.827 | 0.000 | — |
| CCK | 0.819 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SREBF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ASCC3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=95.8 + PDB: 1RJV, 1RK9, 9BB8 | pLDDT=95.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Nucleoli, Cell Junctions | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. PVALB — Parvalbumin alpha，研究基础较多，新颖性有限。
2. 蛋白大小110 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 159 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 159 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P20472
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100362-PVALB/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PVALB
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P20472
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000100362-PVALB/subcellular

![](https://images.proteinatlas.org/48536/1375_C3_1_red_green.jpg)
![](https://images.proteinatlas.org/48536/1375_C3_2_red_green.jpg)
![](https://images.proteinatlas.org/48536/1384_C3_15_red_green.jpg)
![](https://images.proteinatlas.org/48536/1384_C3_8_red_green.jpg)
![](https://images.proteinatlas.org/48536/1895_F5_1_red_green.jpg)
![](https://images.proteinatlas.org/48536/1895_F5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P20472 |
| SMART | SM00054; |
| UniProt Domain [FT] | DOMAIN 39..74; /note="EF-hand 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00448"; DOMAIN 78..110; /note="EF-hand 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00448" |
| InterPro | IPR011992;IPR018247;IPR002048;IPR008080; |
| Pfam | PF13499; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000100362-PVALB/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

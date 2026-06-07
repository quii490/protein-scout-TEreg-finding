---
type: protein-evaluation
gene: "KIAA1549L"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KIAA1549L 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KIAA1549L / C11orf41, C11orf69 |
| 蛋白名称 | UPF0606 protein KIAA1549L |
| 蛋白大小 | 1849 aa / 199.0 kDa |
| UniProt ID | Q6ZVL6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: Membrane |
| 蛋白大小 | 5/10 | ×1 | 5 | 1849 aa / 199.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=44.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR024606; Pfam: PF12877 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 11 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.0/180** | |
| **归一化总分** | | | **62.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 7 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C11orf41, C11orf69 |

**关键文献**:
1. PAX5-KIAA1549L: a novel fusion gene in a case of pediatric B-cell precursor acute lymphoblastic leukemia.. *Molecular cytogenetics*. PMID: 26157485
2. Genetic Influences on Evening Preference Overlap with Those for Bipolar Disorder in a Sample of Mexican Americans and American Indians.. *Twin research and human genetics : the official journal of the International Society for Twin Studies*. PMID: 29192581
3. Tetanus vaccination is associated with differential DNA-methylation: Reduces the risk of asthma in adolescence.. *Vaccine*. PMID: 27866770

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 44.3 |
| 高置信度残基 (pLDDT>90) 占比 | 5.1% |
| 置信残基 (pLDDT 70-90) 占比 | 16.2% |
| 中等置信 (pLDDT 50-70) 占比 | 3.8% |
| 低置信 (pLDDT<50) 占比 | 75.0% |
| 有序区域 (pLDDT>70) 占比 | 21.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=44.3），有序残基占 21.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR024606; Pfam: PF12877 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CSTF3 | 0.909 | 0.000 | — |
| DEPDC7 | 0.874 | 0.000 | — |
| FBXO3 | 0.872 | 0.000 | — |
| CD59 | 0.668 | 0.000 | — |
| LMO2 | 0.536 | 0.058 | — |
| CSTF1 | 0.495 | 0.000 | — |
| DPRX | 0.476 | 0.058 | — |
| HIPK3 | 0.461 | 0.049 | — |
| C11orf91 | 0.446 | 0.000 | — |
| DNAH14 | 0.439 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ATXN1 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| GRB2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| H2BC21 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ENST00000321505 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 11，IntAct interactions: 4
- 调控相关比例: 1 / 11 = 9%

**评价**: STRING 11 个预测互作，IntAct 4 个实验互作。调控相关配体占比 9%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=44.3 + PDB: 无 | pLDDT=44.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 11 + 4 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. KIAA1549L — UPF0606 protein KIAA1549L，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1849 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=44.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6ZVL6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000110427-KIAA1549L/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KIAA1549L
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ZVL6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000110427-KIAA1549L/subcellular

![](https://images.proteinatlas.org/10132/47_C8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/10132/47_C8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/10132/48_C8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/10132/48_C8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/10132/49_C8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/10132/49_C8_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6ZVL6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6ZVL6 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR024606; |
| Pfam | PF12877; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000110427-KIAA1549L/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

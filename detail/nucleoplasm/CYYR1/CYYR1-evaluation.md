---
type: protein-evaluation
gene: "CYYR1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CYYR1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CYYR1 / C21orf95 |
| 蛋白名称 | Cysteine and tyrosine-rich protein 1 |
| 蛋白大小 | 154 aa / 16.6 kDa |
| UniProt ID | Q96J86 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Nucleoplasm; UniProt: Membrane |
| 蛋白大小 | 8/10 | x1 | 8 | 154 aa / 16.6 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=15 篇 (<=20->10) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=60.1; PDB: 无 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR022640; Pfam: PF10873 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.0/180** | |
| **归一化总分** | | | **64.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Membrane | Swiss-Prot/TremBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 18 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C21orf95 |

**关键文献**:
1. CYYR1 promotes the degradation of the E3 ubiquitin ligase WWP1 and is associated with favorable prognosis in breast cancer.. *The Journal of biological chemistry*. PMID: 39059493
2. Cysteine and tyrosine-rich 1 (CYYR1), a novel unpredicted gene on human chromosome 21 (21q21.2), encodes a cysteine and tyrosine-rich protein and defines a new family of highly conserved vertebrate-specific genes.. *Gene*. PMID: 12062809
3. Unveiling the key genes, environmental toxins, and drug exposures in modulating the severity of ulcerative colitis: a comprehensive analysis.. *Frontiers in immunology*. PMID: 37539055
4. Sequence, "subtle" alternative splicing and expression of the CYYR1 (cysteine/tyrosine-rich 1) mRNA in human neuroendocrine tumors.. *BMC cancer*. PMID: 17442112
5. Advancements in biomarkers and machine learning for predicting of bronchopulmonary dysplasia and neonatal respiratory distress syndrome in preterm infants.. *Frontiers in pediatrics*. PMID: 40352605

**评价**: 极度新颖，几乎未被系统研究（PubMed <=20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.1 |
| 高置信度残基 (pLDDT>90) 占比 | 1.3% |
| 置信残基 (pLDDT 70-90) 占比 | 19.5% |
| 中等置信 (pLDDT 50-70) 占比 | 58.4% |
| 低置信 (pLDDT<50) 占比 | 20.8% |
| 有序区域 (pLDDT>70) 占比 | 20.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=60.1），有序残基占 20.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR022640; Pfam: PF10873 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SLC4A11 | 0.652 | 0.000 | — |
| CLEC14A | 0.615 | 0.000 | — |
| COL8A2 | 0.583 | 0.000 | — |
| MAGI1 | 0.546 | 0.534 | — |
| KDR | 0.536 | 0.000 | — |
| SHISAL1 | 0.502 | 0.000 | — |
| MRPL39 | 0.493 | 0.000 | — |
| YAP1 | 0.493 | 0.485 | — |
| SOX18 | 0.476 | 0.000 | — |
| SPARCL1 | 0.462 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| feoA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| YAP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MAGI1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PTPRF | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NEDD4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NEDD4L | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| GOPC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| WWOX | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 8
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 8 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.1 + PDB: 无 | pLDDT=60.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 8 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ***

**核心优势**:
1. CYYR1 -- Cysteine and tyrosine-rich protein 1，极度新颖，几乎未被系统研究（PubMed <=20篇）。
2. 蛋白大小154 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=60.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96J86
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166265-CYYR1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CYYR1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96J86
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000166265-CYYR1/subcellular

![](https://images.proteinatlas.org/67685/1398_F1_1_red_green.jpg)
![](https://images.proteinatlas.org/67685/1398_F1_2_red_green.jpg)
![](https://images.proteinatlas.org/67685/1403_F1_1_red_green.jpg)
![](https://images.proteinatlas.org/67685/1403_F1_2_red_green.jpg)
![](https://images.proteinatlas.org/67685/1441_E1_1_red_green.jpg)
![](https://images.proteinatlas.org/67685/1441_E1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96J86-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

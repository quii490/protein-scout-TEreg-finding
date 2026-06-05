---
type: protein-evaluation
gene: "PRR9"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PRR9 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PRR9 |
| 蛋白名称 | Proline-rich protein 9 |
| 蛋白大小 | 116 aa / 12.9 kDa |
| UniProt ID | Q5T870 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cytosol; 额外: Nucleoplasm, Vesicles; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 116 aa / 12.9 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=62 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=49.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR052888 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **85/180** | |
| **归一化总分** | | | **47.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm, Vesicles | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 62 |
| PubMed broad count | 94 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Overlapping and distinct roles of PRR7 and PRR9 in the Arabidopsis circadian clock.. *Current biology : CB*. PMID: 15649364
2. Genome-Wide Association Meta-Analysis Reveals Novel Juvenile Idiopathic Arthritis Susceptibility Loci.. *Arthritis & rheumatology (Hoboken, N.J.)*. PMID: 28719732
3. Molecular investigation of organ-autonomous expression of Arabidopsis circadian oscillators.. *Plant, cell & environment*. PMID: 32012302
4. The Arabidopsis JMJ29 Protein Controls Circadian Oscillation through Diurnal Histone Demethylation at the CCA1 and PRR9 Loci.. *Genes*. PMID: 33916408
5. PSEUDO-RESPONSE REGULATORS, PRR9, PRR7 and PRR5, together play essential roles close to the circadian clock of Arabidopsis thaliana.. *Plant & cell physiology*. PMID: 15767265

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 49.2 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 0.0% |
| 中等置信 (pLDDT 50-70) 占比 | 41.4% |
| 低置信 (pLDDT<50) 占比 | 58.6% |
| 有序区域 (pLDDT>70) 占比 | 0.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=49.2），有序残基占 0.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052888 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PRR7 | 0.871 | 0.000 | — |
| TRNT1 | 0.795 | 0.000 | — |
| PRR5 | 0.665 | 0.000 | — |
| ELF4 | 0.642 | 0.000 | — |
| LELP1 | 0.573 | 0.000 | — |
| RNF215 | 0.544 | 0.000 | — |
| ELF3 | 0.511 | 0.000 | — |
| VSIG8 | 0.505 | 0.000 | — |
| C1orf68 | 0.496 | 0.000 | — |
| KRT27 | 0.496 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=49.2 + PDB: 无 | pLDDT=49.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Cytosol; 额外: Nucleoplasm, Vesicles | 待确认 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. PRR9 — Proline-rich protein 9，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小116 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 62 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=49.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5T870
- Protein Atlas: https://www.proteinatlas.org/ENSG00000203783-PRR9/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PRR9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5T870
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000203783-PRR9/subcellular

![](https://images.proteinatlas.org/27714/1573_B2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/27714/1573_B2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/27714/1969_C1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/27714/1969_C1_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/27714/232_E10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/27714/232_E10_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5T870-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

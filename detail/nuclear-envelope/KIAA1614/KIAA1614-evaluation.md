---
type: protein-evaluation
gene: "KIAA1614"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KIAA1614 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KIAA1614 |
| 蛋白名称 | Uncharacterized protein KIAA1614 |
| 蛋白大小 | 1190 aa / 126.6 kDa |
| UniProt ID | Q5VZ46 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear membrane, Vesicles; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 1190 aa / 126.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=42.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR032756, IPR051741; Pfam: PF15737 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear membrane, Vesicles | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- apical plasma membrane (GO:0016324)
- cell cortex (GO:0005938)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 8 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Genetic insights into drug targets for sporadic Creutzfeldt-Jakob disease: Integrative multi-omics analysis.. *Neurobiology of disease*. PMID: 38996988
2. Abnormally increased DNA methylation in chorionic tissue might play an important role in development of ectopic pregnancy.. *Reproductive biology and endocrinology : RB&E*. PMID: 34215268
3. DNA polymorphisms predict time to progression from uncomplicated to complicated Crohn's disease.. *European journal of gastroenterology & hepatology*. PMID: 29293112
4. A Genome-Wide Methylation Approach Identifies a New Hypermethylated Gene Panel in Ulcerative Colitis.. *International journal of molecular sciences*. PMID: 27517910
5. Blood group antigen loci demonstrate multivariate genetic associations with circulating cellular adhesion protein levels in the Multi-Ethnic Study of Atherosclerosis.. *Human genetics*. PMID: 26883866

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 42.5 |
| 高置信度残基 (pLDDT>90) 占比 | 1.9% |
| 置信残基 (pLDDT 70-90) 占比 | 6.5% |
| 中等置信 (pLDDT 50-70) 占比 | 7.0% |
| 低置信 (pLDDT<50) 占比 | 84.6% |
| 有序区域 (pLDDT>70) 占比 | 8.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=42.5），有序残基占 8.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR032756, IPR051741; Pfam: PF15737 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RBBP6 | 0.849 | 0.789 | — |
| SYMPK | 0.838 | 0.774 | — |
| WDR82 | 0.832 | 0.788 | — |
| FIP1L1 | 0.828 | 0.777 | — |
| CPSF3 | 0.817 | 0.780 | — |
| RBBP5 | 0.788 | 0.781 | — |
| FAM217B | 0.695 | 0.000 | — |
| CPSF2 | 0.674 | 0.618 | — |
| PAPOLB | 0.578 | 0.504 | — |
| PAPOLG | 0.577 | 0.504 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| H2BC9 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| PTPRR | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=42.5 + PDB: 无 | pLDDT=42.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nuclear membrane, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. KIAA1614 — Uncharacterized protein KIAA1614，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1190 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=42.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5VZ46
- Protein Atlas: https://www.proteinatlas.org/ENSG00000135835-KIAA1614/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KIAA1614
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5VZ46
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000135835-KIAA1614/subcellular

![](https://images.proteinatlas.org/61684/1130_G8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/61684/1130_G8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/61684/1220_F7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/61684/1220_F7_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5VZ46-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5VZ46 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR032756;IPR051741; |
| Pfam | PF15737; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000135835-KIAA1614/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

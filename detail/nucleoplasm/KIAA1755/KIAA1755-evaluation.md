---
type: protein-evaluation
gene: "KIAA1755"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KIAA1755 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KIAA1755 |
| 蛋白名称 | Uncharacterized protein KIAA1755 |
| 蛋白大小 | 1200 aa / 130.8 kDa |
| UniProt ID | Q5JYT7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli; 额外: Golgi apparatus, Vesicles; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 1200 aa / 130.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR052231 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.0/180** | |
| **归一化总分** | | | **64.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Golgi apparatus, Vesicles | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- extrinsic component of membrane (GO:0019898)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 14 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Translating GWAS-identified loci for cardiac rhythm and rate using an in vivo image- and CRISPR/Cas9-based approach.. *Scientific reports*. PMID: 32678143
2. Genetic loci associated with heart rate variability and their effects on cardiac disease risk.. *Nature communications*. PMID: 28613276
3. High-throughput assessment of the antibody profile in ovarian cancer ascitic fluids.. *Oncoimmunology*. PMID: 31428516
4. High Expression Levels of the Long Non-Coding RNAs Lnc-IRF2-3 and Lnc-KIAA1755-4 Are Markers of Poor Prognosis in Chronic Lymphocytic Leukemia.. *International journal of molecular sciences*. PMID: 39940921
5. Discovery of novel heart rate-associated loci using the Exome Chip.. *Human molecular genetics*. PMID: 28379579

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.1 |
| 高置信度残基 (pLDDT>90) 占比 | 34.7% |
| 置信残基 (pLDDT 70-90) 占比 | 18.8% |
| 中等置信 (pLDDT 50-70) 占比 | 2.8% |
| 低置信 (pLDDT<50) 占比 | 43.7% |
| 有序区域 (pLDDT>70) 占比 | 53.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=64.1），有序残基占 53.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052231 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SYT10 | 0.542 | 0.000 | — |
| C11orf71 | 0.496 | 0.000 | — |
| RANBP3L | 0.492 | 0.000 | — |
| SLC35F1 | 0.489 | 0.000 | — |
| RWDD2A | 0.484 | 0.000 | — |
| SLC6A7 | 0.480 | 0.000 | — |
| ZBTB47 | 0.460 | 0.000 | — |
| EPB41L4A | 0.460 | 0.000 | — |
| VSTM2L | 0.456 | 0.000 | — |
| ITM2C | 0.454 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EPHA4 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| Insr | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:30300385|imex:IM-26942| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.1 + PDB: 无 | pLDDT=64.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoli; 额外: Golgi apparatus, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. KIAA1755 — Uncharacterized protein KIAA1755，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1200 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=64.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5JYT7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000149633-KIAA1755/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KIAA1755
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5JYT7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000149633-KIAA1755/subcellular

![](https://images.proteinatlas.org/51064/1331_C4_7_red_green.jpg)
![](https://images.proteinatlas.org/51064/1331_C4_9_red_green.jpg)
![](https://images.proteinatlas.org/51064/1345_C4_2_red_green.jpg)
![](https://images.proteinatlas.org/51064/1345_C4_4_red_green.jpg)
![](https://images.proteinatlas.org/51064/1364_B11_1_red_green.jpg)
![](https://images.proteinatlas.org/51064/1364_B11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5JYT7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5JYT7 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR052231; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000149633-KIAA1755/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

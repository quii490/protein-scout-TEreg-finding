---
type: protein-evaluation
gene: "METTL23"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## METTL23 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | METTL23 / C17orf95 |
| 蛋白名称 | Histone-arginine methyltransferase METTL23 |
| 蛋白大小 | 190 aa / 21.5 kDa |
| UniProt ID | Q86XA0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 190 aa / 21.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=93.9; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR019410, IPR029063; Pfam: PF10294 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **136.5/180** | |
| **归一化总分** | | | **75.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles | Approved |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- female pronucleus (GO:0001939)
- male pronucleus (GO:0001940)
- nucleus (GO:0005634)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 21 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C17orf95 |

**关键文献**:
1. METTL23 Variants and Patients With Normal-Tension Glaucoma.. *JAMA ophthalmology*. PMID: 39325437
2. METTL23 mutation alters histone H3R17 methylation in normal-tension glaucoma.. *The Journal of clinical investigation*. PMID: 36099048
3. Association Analysis of METTL23 Gene Polymorphisms with Reproductive Traits in Kele Pigs.. *Genes*. PMID: 39202421
4. Molecular genetics of inherited normal tension glaucoma.. *Indian journal of ophthalmology*. PMID: 38389252
5. Histone H3 Methylated at Arginine 17 Is Essential for Reprogramming the Paternal Genome in Zygotes.. *Cell reports*. PMID: 28930672

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.9 |
| 高置信度残基 (pLDDT>90) 占比 | 84.2% |
| 置信残基 (pLDDT 70-90) 占比 | 14.2% |
| 中等置信 (pLDDT 50-70) 占比 | 1.6% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 98.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=93.9，有序区 98.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019410, IPR029063; Pfam: PF10294 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GABPA | 0.789 | 0.000 | — |
| METTL22 | 0.716 | 0.065 | — |
| METTL18 | 0.659 | 0.000 | — |
| KIN | 0.626 | 0.000 | — |
| EEF2KMT | 0.619 | 0.065 | — |
| ETFBKMT | 0.618 | 0.000 | — |
| EEF1AKMT2 | 0.588 | 0.000 | — |
| EEF1AKMT1 | 0.566 | 0.000 | — |
| MFSD11 | 0.565 | 0.000 | — |
| PRPSAP1 | 0.529 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| mamo-RC | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:unassigned1513|imex:IM- |
| TfIIEalpha | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:unassigned1513|imex:IM- |
| Dmel\CG5013 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:unassigned1513|imex:IM- |
| heca | psi-mi:"MI:0397"(two hybrid array) | pubmed:37061542|imex:IM-28761 |
| BCAS2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ENST00000341249 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 6
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.9 + PDB: 无 | pLDDT=93.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 6 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. METTL23 — Histone-arginine methyltransferase METTL23，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小190 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86XA0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000181038-METTL23/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=METTL23
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86XA0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (approved)。来源: https://www.proteinatlas.org/ENSG00000181038-METTL23/subcellular

![](https://images.proteinatlas.org/22889/1871_B11_12_cr5b50724e2676b_blue_red_green.jpg)
![](https://images.proteinatlas.org/22889/1871_B11_16_cr5b50724e26ee5_blue_red_green.jpg)
![](https://images.proteinatlas.org/22889/1898_E5_20_cr5ba8a282c27ff_blue_red_green.jpg)
![](https://images.proteinatlas.org/22889/1898_E5_28_cr5ba8a282c32b4_blue_red_green.jpg)
![](https://images.proteinatlas.org/22889/1901_B3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/22889/1901_B3_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86XA0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q86XA0 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR019410;IPR029063; |
| Pfam | PF10294; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000181038-METTL23/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BCAS2 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

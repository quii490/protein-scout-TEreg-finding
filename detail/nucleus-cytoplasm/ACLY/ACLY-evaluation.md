---
type: protein-evaluation
gene: "ACLY"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ACLY — REJECTED (研究热度过高 (PubMed strict=505，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ACLY |
| 蛋白名称 | ATP-citrate synthase |
| 蛋白大小 | 1101 aa / 120.8 kDa |
| UniProt ID | P53396 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nucleoplasm, Primary cilium transition zone, Ba; UniProt: Cytoplasm, cytosol |
| 蛋白大小 | 8/10 | ×1 | 8 | 1101 aa / 120.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=505 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=92.3; PDB: 3MWD, 3MWE, 3PFF, 5TDE, 5TDF, 5TDM, 5TDZ |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR014608, IPR017440, IPR032263, IPR016143, IPR056 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **93.5/180** | |
| **归一化总分** | | | **51.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm, Primary cilium transition zone, Basal body, Principal piece | Supported |
| UniProt | Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- azurophil granule lumen (GO:0035578)
- ciliary basal body (GO:0036064)
- ciliary transition zone (GO:0035869)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- extracellular region (GO:0005576)
- ficolin-1-rich granule lumen (GO:1904813)
- membrane (GO:0016020)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 505 |
| PubMed broad count | 844 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. ACLY inhibition promotes tumour immunity and suppresses liver cancer.. *Nature*. PMID: 40739358
2. Lipid alterations in chronic liver disease and liver cancer.. *JHEP reports : innovation in hepatology*. PMID: 35469167
3. Cancer-associated fibroblast-derived acetate promotes pancreatic cancer development by altering polyamine metabolism via the ACSS2-SP1-SAT1 axis.. *Nature cell biology*. PMID: 38429478
4. Lactate supports a metabolic-epigenetic link in macrophage polarization.. *Science advances*. PMID: 34767443
5. Cancer-derived exosomal HSPC111 promotes colorectal cancer liver metastasis by reprogramming lipid metabolism in cancer-associated fibroblasts.. *Cell death & disease*. PMID: 35027547

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.3 |
| 高置信度残基 (pLDDT>90) 占比 | 88.0% |
| 置信残基 (pLDDT 70-90) 占比 | 5.9% |
| 中等置信 (pLDDT 50-70) 占比 | 0.8% |
| 低置信 (pLDDT<50) 占比 | 5.3% |
| 有序区域 (pLDDT>70) 占比 | 93.9% |
| 可用 PDB 条目 | 3MWD, 3MWE, 3PFF, 5TDE, 5TDF, 5TDM, 5TDZ, 5TE1, 5TEQ, 5TES |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3MWD, 3MWE, 3PFF, 5TDE, 5TDF, 5TDM, 5TDZ, 5TE1, 5TEQ, 5TES）+ AlphaFold极高置信度预测（pLDDT=92.3），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR014608, IPR017440, IPR032263, IPR016143, IPR056749; Pfam: PF16114, PF00285, PF24948 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CS | 0.998 | 0.737 | — |
| FASN | 0.994 | 0.087 | — |
| SUCLG1 | 0.991 | 0.779 | — |
| DLAT | 0.988 | 0.099 | — |
| ACACA | 0.986 | 0.000 | — |
| ACO2 | 0.985 | 0.095 | — |
| ACO1 | 0.981 | 0.095 | — |
| MDH2 | 0.981 | 0.071 | — |
| PC | 0.974 | 0.000 | — |
| ACACB | 0.970 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=92.3 + PDB: 3MWD, 3MWE, 3PFF, 5TDE, 5TDF,  | pLDDT=92.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol / Cytosol; 额外: Nucleoplasm, Primary cilium transitio | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. ACLY — ATP-citrate synthase，研究基础较多，新颖性有限。
2. 蛋白大小1101 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 505 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 505 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P53396
- Protein Atlas: https://www.proteinatlas.org/ENSG00000131473-ACLY/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ACLY
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P53396
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000131473-ACLY/subcellular

![](https://images.proteinatlas.org/22434/2120_F11_18_blue_red_green.jpg)
![](https://images.proteinatlas.org/22434/2120_F11_42_blue_red_green.jpg)
![](https://images.proteinatlas.org/22434/2133_F9_18_blue_red_green.jpg)
![](https://images.proteinatlas.org/22434/2133_F9_55_blue_red_green.jpg)
![](https://images.proteinatlas.org/22434/2167_G12_37_blue_red_green.jpg)
![](https://images.proteinatlas.org/22434/2167_G12_52_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P53396-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P53396 |
| SMART | SM00881; |
| UniProt Domain [FT] | DOMAIN 4..265; /note="ATP-grasp" |
| InterPro | IPR014608;IPR017440;IPR032263;IPR016143;IPR056749;IPR002020;IPR036969;IPR033847;IPR003781;IPR036291;IPR017866;IPR005811;IPR016102; |
| Pfam | PF16114;PF00285;PF24948;PF02629;PF00549; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000131473-ACLY/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| KLHL25 | Biogrid, Bioplex | true |
| ACE2 | Biogrid | false |
| ATXN3 | Biogrid | false |
| CCNF | Biogrid | false |
| CUL2 | Biogrid | false |
| CUL3 | Biogrid | false |
| EP300 | Biogrid | false |
| FBXO43 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

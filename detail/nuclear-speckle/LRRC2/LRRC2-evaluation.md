---
type: protein-evaluation
gene: "LRRC2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LRRC2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LRRC2 |
| 蛋白名称 | Leucine-rich repeat-containing protein 2 |
| 蛋白大小 | 371 aa / 42.9 kDa |
| UniProt ID | Q9BYS8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nuclear bodies, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 371 aa / 42.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=77.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001611, IPR025875, IPR003591, IPR032675, IPR050 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.0/180** | |
| **归一化总分** | | | **73.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear bodies, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 19 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Safety and efficacy of AAV8-aflibercept in treating choroidal neovascularization via single-cell RNA sequencing.. *Molecular therapy. Methods & clinical development*. PMID: 41399432
2. Altered expression of LINC03091 and LINC03090 LncRNAs in bipolar disorder: a case-control study.. *Scientific reports*. PMID: 41298728
3. Construction and Analysis of the lncRNA-miRNA-mRNA Network Based on Competing Endogenous RNA in Atrial Fibrillation.. *Frontiers in cardiovascular medicine*. PMID: 35141302
4. An Integrated Multi-Omics Study of Mammalian Skeletal, Cardiac, and Smooth Muscles.. *International journal of molecular sciences*. PMID: 41516119
5. The transcriptional map of the common eliminated region 1 (C3CER1) in 3p21.3.. *European journal of human genetics : EJHG*. PMID: 11896456

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.6 |
| 高置信度残基 (pLDDT>90) 占比 | 43.7% |
| 置信残基 (pLDDT 70-90) 占比 | 25.6% |
| 中等置信 (pLDDT 50-70) 占比 | 16.7% |
| 低置信 (pLDDT<50) 占比 | 14.0% |
| 有序区域 (pLDDT>70) 占比 | 69.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=77.6，有序区 69.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001611, IPR025875, IPR003591, IPR032675, IPR050216; Pfam: PF12799, PF13855 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| IGFALS | 0.632 | 0.000 | — |
| LRRC20 | 0.619 | 0.000 | — |
| FASN | 0.614 | 0.049 | — |
| GPALPP1 | 0.546 | 0.000 | — |
| PRELP | 0.541 | 0.000 | — |
| ZNF770 | 0.532 | 0.091 | — |
| LRG1 | 0.530 | 0.000 | — |
| LGR5 | 0.523 | 0.046 | — |
| LUM | 0.519 | 0.000 | — |
| KERA | 0.516 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Rpgrip1l | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21565611|imex:IM-16529 |
| TP53RK | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| CETN2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| EBI-9357028 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.6 + PDB: 无 | pLDDT=77.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Nuclear bodies, Cytosol | 待确认 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. LRRC2 — Leucine-rich repeat-containing protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小371 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BYS8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163827-LRRC2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LRRC2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BYS8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000163827-LRRC2/subcellular

![](https://images.proteinatlas.org/39138/1925_A12_24_cr5cd5546812320_red_green.jpg)
![](https://images.proteinatlas.org/39138/1925_A12_6_cr5cd55468112e3_red_green.jpg)
![](https://images.proteinatlas.org/39138/442_D10_1_red_green.jpg)
![](https://images.proteinatlas.org/39138/442_D10_3_red_green.jpg)
![](https://images.proteinatlas.org/39138/521_D10_1_red_green.jpg)
![](https://images.proteinatlas.org/39138/521_D10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BYS8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BYS8 |
| SMART | SM00364;SM00369; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001611;IPR025875;IPR003591;IPR032675;IPR050216; |
| Pfam | PF12799;PF13855; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000163827-LRRC2/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

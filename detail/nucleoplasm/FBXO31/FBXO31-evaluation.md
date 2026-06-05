---
type: protein-evaluation
gene: "FBXO31"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FBXO31 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBXO31 / FBX14, FBX31 |
| 蛋白名称 | F-box only protein 31 |
| 蛋白大小 | 539 aa / 60.7 kDa |
| UniProt ID | Q5XUX0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Golgi apparatus, Cytosol; UniProt: Cytoplasm; Cytoplasm, cytoskeleton, microtubule organizing c |
| 蛋白大小 | 10/10 | ×1 | 10 | 539 aa / 60.7 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=62 篇 (≤80→4) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=83.1; PDB: 5VZT, 5VZU |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR036047, IPR001810, IPR045048; Pfam: PF12014, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **100.0/180** | |
| **归一化总分** | | | **55.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Golgi apparatus, Cytosol | Approved |
| UniProt | Cytoplasm; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- neuronal cell body (GO:0043025)
- SCF ubiquitin ligase complex (GO:0019005)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 62 |
| PubMed broad count | 78 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FBX14, FBX31 |

**关键文献**:
1. FBXO31-mediated ubiquitination of OGT maintains O-GlcNAcylation homeostasis to restrain endometrial malignancy.. *Nature communications*. PMID: 39894887
2. C-terminal amides mark proteins for degradation via SCF-FBXO31.. *Nature*. PMID: 39880951
3. FBXO31 is upregulated by METTL3 to promote pancreatic cancer progression via regulating SIRT2 ubiquitination and degradation.. *Cell death & disease*. PMID: 38216561
4. Nevus senescence.. *ISRN dermatology*. PMID: 22363855
5. Phosphorylation-Mediated Regulation of FBXO31 Stability Under Cellular Homeostasis.. *Advanced biology*. PMID: 40847744

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.1 |
| 高置信度残基 (pLDDT>90) 占比 | 72.7% |
| 置信残基 (pLDDT 70-90) 占比 | 4.6% |
| 中等置信 (pLDDT 50-70) 占比 | 2.0% |
| 低置信 (pLDDT<50) 占比 | 20.6% |
| 有序区域 (pLDDT>70) 占比 | 77.3% |
| 可用 PDB 条目 | 5VZT, 5VZU |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（5VZT, 5VZU）+ AlphaFold高质量预测（pLDDT=83.1），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036047, IPR001810, IPR045048; Pfam: PF12014, PF12937 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SKP1 | 0.996 | 0.983 | — |
| CCND1 | 0.985 | 0.972 | — |
| CUL1 | 0.969 | 0.873 | — |
| RBX1 | 0.853 | 0.725 | — |
| ATM | 0.571 | 0.292 | — |
| NEDD8 | 0.543 | 0.000 | — |
| UBE2M | 0.509 | 0.000 | — |
| CAND1 | 0.504 | 0.000 | — |
| DCUN1D3 | 0.503 | 0.000 | — |
| NAE1 | 0.501 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| COPS5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| CUL1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| SKP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:22632967|imex:IM-17368 |
| FAM98A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MYH6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| PRPS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| CEP170P1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Kctd5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| PDLIM1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| DNAJC19 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.1 + PDB: 5VZT, 5VZU | pLDDT=83.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, cytoskeleton, microtubule or / Nucleoplasm; 额外: Golgi apparatus, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FBXO31 — F-box only protein 31，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小539 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 62 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5XUX0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000103264-FBXO31/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBXO31
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5XUX0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000103264-FBXO31/subcellular

![](https://images.proteinatlas.org/30150/1399_A3_2_red_green.jpg)
![](https://images.proteinatlas.org/30150/1399_A3_3_red_green.jpg)
![](https://images.proteinatlas.org/30150/342_A1_1_red_green.jpg)
![](https://images.proteinatlas.org/30150/342_A1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5XUX0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

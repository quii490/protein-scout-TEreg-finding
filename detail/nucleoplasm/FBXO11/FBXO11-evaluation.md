---
type: protein-evaluation
gene: "FBXO11"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FBXO11 — REJECTED (研究热度过高 (PubMed strict=106，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBXO11 / FBX11, PRMT9, VIT1 |
| 蛋白名称 | F-box only protein 11 |
| 蛋白大小 | 927 aa / 103.6 kDa |
| UniProt ID | Q86XK2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli; UniProt: Nucleus; Chromosome |
| 蛋白大小 | 8/10 | ×1 | 8 | 927 aa / 103.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=106 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=82.5; PDB: 5VMD |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR039448, IPR006633, IPR036047, IPR001810, IPR047 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **87.0/180** | |
| **归一化总分** | | | **48.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli | Supported |
| UniProt | Nucleus; Chromosome | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- chromosome (GO:0005694)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- ubiquitin ligase complex (GO:0000151)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 106 |
| PubMed broad count | 160 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FBX11, PRMT9, VIT1 |

**关键文献**:
1. De novo variants in FBXO11 cause a syndromic form of intellectual disability with behavioral problems and dysmorphisms.. *European journal of human genetics : EJHG*. PMID: 30679813
2. FBXO11 regulates bone development.. *Bone*. PMID: 36863499
3. NDR1/FBXO11 promotes phosphorylation-mediated ubiquitination of β-catenin to suppress metastasis in prostate cancer.. *International journal of biological sciences*. PMID: 39309441
4. FBXO11 variants are associated with intellectual disability and variable clinical manifestation in Chinese affected individuals.. *Journal of human genetics*. PMID: 38740982
5. DRAIC mediates hnRNPA2B1 stability and m(6)A-modified IGF1R instability to inhibit tumor progression.. *Oncogene*. PMID: 38811846

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.5 |
| 高置信度残基 (pLDDT>90) 占比 | 69.3% |
| 置信残基 (pLDDT 70-90) 占比 | 9.7% |
| 中等置信 (pLDDT 50-70) 占比 | 2.5% |
| 低置信 (pLDDT<50) 占比 | 18.6% |
| 有序区域 (pLDDT>70) 占比 | 79.0% |
| 可用 PDB 条目 | 5VMD |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=82.5，有序区 79.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039448, IPR006633, IPR036047, IPR001810, IPR047505; Pfam: PF13229, PF12937, PF02207 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SKP1 | 0.991 | 0.903 | — |
| CUL1 | 0.980 | 0.819 | — |
| RBX1 | 0.872 | 0.689 | — |
| DTL | 0.860 | 0.510 | — |
| BCL6 | 0.805 | 0.626 | — |
| MSH6 | 0.791 | 0.000 | — |
| FBXL14 | 0.772 | 0.000 | — |
| NEDD8 | 0.768 | 0.292 | — |
| TP53 | 0.736 | 0.397 | — |
| UBA3 | 0.729 | 0.292 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Hrs | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| SkpA | psi-mi:"MI:0018"(two hybrid) | pubmed:15575970|mint:MINT-7952 |
| PpD3 | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| TP53 | psi-mi:"MI:0096"(pull down) | pubmed:17098746|imex:IM-19684 |
| RBX1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:17098746|imex:IM-19684 |
| CUL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:17098746|imex:IM-19684 |
| SKP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:17098746|imex:IM-19684 |
| NEDD8 | psi-mi:"MI:0415"(enzymatic study) | pubmed:17098746|imex:IM-19684 |
| UBA3 | psi-mi:"MI:0415"(enzymatic study) | pubmed:17098746|imex:IM-19684 |
| UBE2M | psi-mi:"MI:0415"(enzymatic study) | pubmed:17098746|imex:IM-19684 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.5 + PDB: 5VMD | pLDDT=82.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome / Nucleoplasm, Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. FBXO11 — F-box only protein 11，研究基础较多，新颖性有限。
2. 蛋白大小927 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 106 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 106 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86XK2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000138081-FBXO11/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBXO11
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86XK2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86XK2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

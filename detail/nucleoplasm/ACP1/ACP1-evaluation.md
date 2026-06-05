---
type: protein-evaluation
gene: "ACP1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ACP1 — REJECTED (研究热度过高 (PubMed strict=277，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ACP1 |
| 蛋白名称 | Low molecular weight phosphotyrosine protein phosphatase |
| 蛋白大小 | 158 aa / 18.0 kDa |
| UniProt ID | P24666 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 158 aa / 18.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=277 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=96.1; PDB: 1XWW, 3N8I, 4Z99, 4Z9A, 4Z9B, 5JNR, 5JNS |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR050438, IPR023485, IPR036196, IPR002115, IPR017 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **82.0/180** | |
| **归一化总分** | | | **45.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytoplasmic side of plasma membrane (GO:0009898)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- sarcolemma (GO:0042383)
- synapse (GO:0045202)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 277 |
| PubMed broad count | 522 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Two-stage binding of mitochondrial ferredoxin-2 to the core iron-sulfur cluster assembly complex.. *Nature communications*. PMID: 39632806
2. SOS2 and ACP1 Loci Identified through Large-Scale Exome Chip Analysis Regulate Kidney Development and Function.. *Journal of the American Society of Nephrology : JASN*. PMID: 27920155
3. Pinpointing Novel Plasma and Brain Proteins for Common Ocular Diseases: A Comprehensive Cross-Omics Integration Analysis.. *International journal of molecular sciences*. PMID: 39408566
4. New Molecular Targets in Prostate Cancer-The Emerging Role of ACP1 and Low Molecular Weight Protein Tyrosine Phosphatase.. *JCO precision oncology*. PMID: 39565976
5. Mitochondrial acyl carrier protein, Acp1, required for iron-sulfur cluster assembly in mitochondria and cytoplasm in Saccharomyces cerevisiae.. *Mitochondrion*. PMID: 39251117

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 96.1 |
| 高置信度残基 (pLDDT>90) 占比 | 95.6% |
| 置信残基 (pLDDT 70-90) 占比 | 1.3% |
| 中等置信 (pLDDT 50-70) 占比 | 1.9% |
| 低置信 (pLDDT<50) 占比 | 1.3% |
| 有序区域 (pLDDT>70) 占比 | 96.9% |
| 可用 PDB 条目 | 1XWW, 3N8I, 4Z99, 4Z9A, 4Z9B, 5JNR, 5JNS, 5JNT, 5KQG, 5KQL |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1XWW, 3N8I, 4Z99, 4Z9A, 4Z9B, 5JNR, 5JNS, 5JNT, 5KQG, 5KQL）+ AlphaFold极高置信度预测（pLDDT=96.1），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050438, IPR023485, IPR036196, IPR002115, IPR017867; Pfam: PF01451 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| OCA2 | 0.899 | 0.000 | — |
| GET3 | 0.897 | 0.000 | — |
| FLAD1 | 0.854 | 0.000 | — |
| GLRX | 0.851 | 0.000 | — |
| OSGEPL1 | 0.824 | 0.000 | — |
| TKTL2 | 0.810 | 0.361 | — |
| GLRX2 | 0.805 | 0.000 | — |
| OSGEP | 0.802 | 0.000 | — |
| G6PD | 0.783 | 0.000 | — |
| PTS | 0.772 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000272065.5 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| per | psi-mi:"MI:0018"(two hybrid) | pubmed:15710747|imex:IM-16519| |
| ERV25 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| SFMBT1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MRPL20 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| FNBP1L | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| IKBKE | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EIF1B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TNIK | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EIF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=96.1 + PDB: 1XWW, 3N8I, 4Z99, 4Z9A, 4Z9B,  | pLDDT=96.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. ACP1 — Low molecular weight phosphotyrosine protein phosphatase，研究基础较多，新颖性有限。
2. 蛋白大小158 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 277 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 277 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P24666
- Protein Atlas: https://www.proteinatlas.org/ENSG00000143727-ACP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ACP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P24666
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000143727-ACP1/subcellular

![](https://images.proteinatlas.org/16754/131_E6_1_red_green.jpg)
![](https://images.proteinatlas.org/16754/131_E6_2_red_green.jpg)
![](https://images.proteinatlas.org/16754/132_E6_1_red_green.jpg)
![](https://images.proteinatlas.org/16754/132_E6_2_red_green.jpg)
![](https://images.proteinatlas.org/16754/164_E6_1_red_green.jpg)
![](https://images.proteinatlas.org/16754/164_E6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P24666-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

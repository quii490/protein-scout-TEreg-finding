---
type: protein-evaluation
gene: "PHYHIP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PHYHIP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PHYHIP / DYRK1AP3, KIAA0273 |
| 蛋白名称 | Phytanoyl-CoA hydroxylase-interacting protein |
| 蛋白大小 | 330 aa / 37.6 kDa |
| UniProt ID | Q92561 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Mitochondria; 额外: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 330 aa / 37.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=90.1; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR003961, IPR036116, IPR013783, IPR042868, IPR045 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria; 额外: Nucleoplasm | Supported |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 21 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DYRK1AP3, KIAA0273 |

**关键文献**:
1. Construction of a Genetic Prognostic Model in the Glioblastoma Tumor Microenvironment.. *Genes*. PMID: 40869909
2. Towards a transcriptomic biomarker for the classification of melanocytic neoplasms.. *PLoS genetics*. PMID: 41042798
3. Transcriptomic profiling of Parkinson's disease brains reveals disease stage specific gene expression changes.. *Acta neuropathologica*. PMID: 37347276
4. Phyhip-Targeted Delivery of bFGF Platform with Dual Modulation for Enhancing Neurovascular Repair in Traumatic Brain Injury.. *Advanced healthcare materials*. PMID: 40785555
5. Bioinformatics identification of characteristic genes of cervical cancer via an artificial neural network.. *Chinese clinical oncology*. PMID: 38453655

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.1 |
| 高置信度残基 (pLDDT>90) 占比 | 72.4% |
| 置信残基 (pLDDT 70-90) 占比 | 20.0% |
| 中等置信 (pLDDT 50-70) 占比 | 3.3% |
| 低置信 (pLDDT<50) 占比 | 4.2% |
| 有序区域 (pLDDT>70) 占比 | 92.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=90.1，有序区 92.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003961, IPR036116, IPR013783, IPR042868, IPR045545; Pfam: PF19281 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PHYH | 0.986 | 0.087 | — |
| LGI3 | 0.661 | 0.000 | — |
| LIMD1 | 0.627 | 0.627 | — |
| PAQR5 | 0.620 | 0.620 | — |
| ADGRB1 | 0.560 | 0.095 | — |
| KIF15 | 0.539 | 0.539 | — |
| CA10 | 0.536 | 0.335 | — |
| CPNE6 | 0.521 | 0.000 | — |
| MSI2 | 0.469 | 0.469 | — |
| BRINP2 | 0.452 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000415491.2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| SUPT5H | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| HNRNPA1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| NFE2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| HDAC11 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| WDR89 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| MAGED4B | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| FAM131A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| METTL18 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| NDUFV3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.1 + PDB: 无 | pLDDT=90.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Mitochondria; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. PHYHIP — Phytanoyl-CoA hydroxylase-interacting protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小330 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92561
- Protein Atlas: https://www.proteinatlas.org/ENSG00000168490-PHYHIP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PHYHIP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92561
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Mitochondria (supported)。来源: https://www.proteinatlas.org/ENSG00000168490-PHYHIP/subcellular

![](https://images.proteinatlas.org/68030/1361_C11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/68030/1361_C11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/68030/1366_C11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/68030/1366_C11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/68030/1927_C2_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/68030/1927_C2_5_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q92561-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

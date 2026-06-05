---
type: protein-evaluation
gene: "JKAMP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## JKAMP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | JKAMP / C14orf100, JAMP |
| 蛋白名称 | JNK1/MAPK8-associated membrane protein |
| 蛋白大小 | 311 aa / 35.2 kDa |
| UniProt ID | Q9P055 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Vesicles; 额外: Nucleoplasm; UniProt: Endoplasmic reticulum membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 311 aa / 35.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=86.4; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR008485; Pfam: PF05571 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 11 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nucleoplasm | Approved |
| UniProt | Endoplasmic reticulum membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- endoplasmic reticulum membrane (GO:0005789)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 11 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C14orf100, JAMP |

**关键文献**:
1. JKAMP inhibits the osteogenic capacity of adipose-derived stem cells in diabetic osteoporosis by modulating the Wnt signaling pathway through intragenic DNA methylation.. *Stem cell research & therapy*. PMID: 33579371
2. Identification and validation of endoplasmic reticulum stress-related diagnostic biomarkers for type 1 diabetic cardiomyopathy based on bioinformatics and machine learning.. *Frontiers in endocrinology*. PMID: 40171194
3. Bi-allelic loss-of-function variants in JKAMP cause a neurodevelopmental syndrome associated with dysregulation of GPR37 trafficking.. *American journal of human genetics*. PMID: 41643666
4. Cytotoxicity in vitro assay in 3D vs. 2D L929 cell cultures - comparative analysis of the response to the latex extracts.. *PloS one*. PMID: 42048322
5. TTC7B Activates the AKT-JKAMP Signaling Axis to Promote Tumor Progression in Head and Neck Cancer.. *Journal of cellular physiology*. PMID: 41392613

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.4 |
| 高置信度残基 (pLDDT>90) 占比 | 53.7% |
| 置信残基 (pLDDT 70-90) 占比 | 33.4% |
| 中等置信 (pLDDT 50-70) 占比 | 10.3% |
| 低置信 (pLDDT<50) 占比 | 2.6% |
| 有序区域 (pLDDT>70) 占比 | 87.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=86.4，有序区 87.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008485; Pfam: PF05571 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DUSP10 | 0.870 | 0.000 | — |
| RNF5 | 0.791 | 0.292 | — |
| CCDC175 | 0.643 | 0.000 | — |
| MAPK8 | 0.631 | 0.292 | — |
| L3HYPDH | 0.587 | 0.000 | — |
| ACTR10 | 0.535 | 0.000 | — |
| RBM25 | 0.497 | 0.000 | — |
| RTN1 | 0.440 | 0.000 | — |
| LAMTOR2 | 0.425 | 0.000 | — |
| AP3S1 | 0.423 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MYH9 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| YIPF6 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 11，IntAct interactions: 2
- 调控相关比例: 0 / 11 = 0%

**评价**: STRING 11 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.4 + PDB: 无 | pLDDT=86.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane / Vesicles; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 11 + 2 interactions | 数据充分 |

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
1. JKAMP — JNK1/MAPK8-associated membrane protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小311 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9P055
- Protein Atlas: https://www.proteinatlas.org/ENSG00000050130-JKAMP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=JKAMP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P055
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (approved)。来源: https://www.proteinatlas.org/ENSG00000050130-JKAMP/subcellular

![](https://images.proteinatlas.org/71650/1398_F4_2_red_green.jpg)
![](https://images.proteinatlas.org/71650/1398_F4_3_red_green.jpg)
![](https://images.proteinatlas.org/71650/1403_F4_1_red_green.jpg)
![](https://images.proteinatlas.org/71650/1403_F4_2_red_green.jpg)
![](https://images.proteinatlas.org/71650/1441_H3_2_red_green.jpg)
![](https://images.proteinatlas.org/71650/1441_H3_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9P055-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

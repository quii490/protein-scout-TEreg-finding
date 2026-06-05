---
type: protein-evaluation
gene: "KLHDC7A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KLHDC7A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KLHDC7A |
| 蛋白名称 | Kelch domain-containing protein 7A |
| 蛋白大小 | 777 aa / 84.5 kDa |
| UniProt ID | Q5VTJ3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nuclear speckles; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 777 aa / 84.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR015915, IPR052310, IPR006652; Pfam: PF01344 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 5 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 4 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Comprehensive mass spectrometry for development of proteomic biomarkers of intracranial aneurysms.. *Talanta*. PMID: 34973552
2. Identification of key genes modules linking diabetic retinopathy and circadian rhythm.. *Frontiers in immunology*. PMID: 38124748
3. Association between LEKR1-CCNL1 and IGSF21-KLHDC7A gene polymorphisms and diabetic retinopathy of type 2 diabetes mellitus in the Chinese Han population.. *The journal of gene medicine*. PMID: 27607899
4. Screening of candidate genes in fibroblasts derived from patients with Dupuytren's contracture using bioinformatics analysis.. *Rheumatology international*. PMID: 25963801

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.9 |
| 高置信度残基 (pLDDT>90) 占比 | 31.4% |
| 置信残基 (pLDDT 70-90) 占比 | 10.8% |
| 中等置信 (pLDDT 50-70) 占比 | 10.3% |
| 低置信 (pLDDT<50) 占比 | 47.5% |
| 有序区域 (pLDDT>70) 占比 | 42.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=60.9），有序残基占 42.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR015915, IPR052310, IPR006652; Pfam: PF01344 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KLHDC10 | 0.486 | 0.000 | — |
| IGSF21 | 0.473 | 0.000 | — |
| PPM1J | 0.433 | 0.000 | — |
| SLC25A45 | 0.417 | 0.000 | — |
| KIAA1549 | 0.411 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GRIP2 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| FRMPD1 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| DLG3 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| GRID2IP | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| TJP1 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| FRMPD2 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| PTPN13 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| MAGI1 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| SNTA1 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| SYNJ2BP | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 5，IntAct interactions: 15
- 调控相关比例: 0 / 5 = 0%

**评价**: STRING 5 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.9 + PDB: 无 | pLDDT=60.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 5 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. KLHDC7A — Kelch domain-containing protein 7A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小777 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=60.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5VTJ3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000179023-KLHDC7A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KLHDC7A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5VTJ3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000179023-KLHDC7A/subcellular

![](https://images.proteinatlas.org/56616/1057_B12_7_red_green.jpg)
![](https://images.proteinatlas.org/56616/1057_B12_9_red_green.jpg)
![](https://images.proteinatlas.org/56616/1125_E5_3_red_green.jpg)
![](https://images.proteinatlas.org/56616/1125_E5_4_red_green.jpg)
![](https://images.proteinatlas.org/56616/1421_F4_3_red_green.jpg)
![](https://images.proteinatlas.org/56616/1421_F4_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5VTJ3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

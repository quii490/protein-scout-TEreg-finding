---
type: protein-evaluation
gene: "PDZD9"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PDZD9 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PDZD9 / C16orf65 |
| 蛋白名称 | PDZ domain-containing protein 9 |
| 蛋白大小 | 264 aa / 29.9 kDa |
| UniProt ID | Q8IXQ8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Plasma membrane, Cytosol; 额外: Nuclear speckles, Primary cili; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 264 aa / 29.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001478, IPR036034, IPR039179; Pfam: PF00595 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117.5/180** | |
| **归一化总分** | | | **65.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cytosol; 额外: Nuclear speckles, Primary cilium | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 3 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C16orf65 |

**关键文献**:
1. 16p12.2 Recurrent Deletion.. **. PMID: 25719193
2. Transcriptome analyses indicate that heat stress-induced inflammation in white adipose tissue and oxidative stress in skeletal muscle is partially moderated by zilpaterol supplementation in beef cattle.. *Journal of animal science*. PMID: 35079800

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.8 |
| 高置信度残基 (pLDDT>90) 占比 | 31.1% |
| 置信残基 (pLDDT 70-90) 占比 | 11.0% |
| 中等置信 (pLDDT 50-70) 占比 | 20.5% |
| 低置信 (pLDDT<50) 占比 | 37.5% |
| 有序区域 (pLDDT>70) 占比 | 42.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=64.8），有序残基占 42.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001478, IPR036034, IPR039179; Pfam: PF00595 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| VWA3A | 0.758 | 0.000 | — |
| FAM222B | 0.641 | 0.000 | — |
| MISP3 | 0.623 | 0.000 | — |
| CCDC189 | 0.597 | 0.000 | — |
| OR2K2 | 0.558 | 0.000 | — |
| OR51D1 | 0.533 | 0.000 | — |
| TMCO6 | 0.513 | 0.000 | — |
| MPP4 | 0.511 | 0.000 | — |
| POLR3E | 0.511 | 0.000 | — |
| C16orf54 | 0.491 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ABCC4 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| ARHGEF16 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| ASIC3 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| ATP2B4 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| CYSLTR2 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| DGKK | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| DGKZ | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| DOCK4 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| FRMPD4 | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |
| E | psi-mi:"MI:2437"(holdup assay) | doi:10.1038/s41467-022-33018-0 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 14，IntAct interactions: 15
- 调控相关比例: 0 / 14 = 0%

**评价**: STRING 14 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.8 + PDB: 无 | pLDDT=64.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Plasma membrane, Cytosol; 额外: Nuclear speckles, Pr | 待确认 |
| PPI | STRING + IntAct | 14 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PDZD9 — PDZ domain-containing protein 9，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小264 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=64.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IXQ8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000155714-PDZD9/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PDZD9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IXQ8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000155714-PDZD9/subcellular

![](https://images.proteinatlas.org/42457/2275_H7_10_blue_red_green.jpg)
![](https://images.proteinatlas.org/42457/2275_H7_96_blue_red_green.jpg)
![](https://images.proteinatlas.org/42457/616_D6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/42457/616_D6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/42457/619_D6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/42457/619_D6_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IXQ8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

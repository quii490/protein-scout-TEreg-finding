---
type: protein-evaluation
gene: "TGDS"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TGDS 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TGDS |
| 蛋白名称 | UDP-D-glucose 4,6-dehydratase |
| 蛋白大小 | 350 aa / 40.2 kDa |
| UniProt ID | O95455 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Nucleoli, Cytosol; UniProt: Endoplasmic reticulum; Golgi apparatus |
| 蛋白大小 | 10/10 | ×1 | 10 | 350 aa / 40.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=94.3; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR005888, IPR016040, IPR036291; Pfam: PF16363 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli, Cytosol | Approved |
| UniProt | Endoplasmic reticulum; Golgi apparatus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- endoplasmic reticulum (GO:0005783)
- Golgi apparatus (GO:0005794)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 76 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. When rare meets common: Treatable genetic diseases are enriched in the general psychiatric population.. *American journal of medical genetics. Part A*. PMID: 38532509
2. Homozygous and compound-heterozygous mutations in TGDS cause Catel-Manzke syndrome.. *American journal of human genetics*. PMID: 25480037
3. Genetic Landscape of Robin Sequence: A Systematic Review.. *Clinical genetics*. PMID: 41077824
4. Single-cell and multi-omics analysis identifies mitophagy-related biomarkers and therapeutic targets in ischemic stroke.. *Scientific reports*. PMID: 41792398
5. Submicroscopic deletions at 13q32.1 cause congenital microcoria.. *American journal of human genetics*. PMID: 25772937

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.3 |
| 高置信度残基 (pLDDT>90) 占比 | 91.7% |
| 置信残基 (pLDDT 70-90) 占比 | 3.7% |
| 中等置信 (pLDDT 50-70) 占比 | 0.9% |
| 低置信 (pLDDT<50) 占比 | 3.7% |
| 有序区域 (pLDDT>70) 占比 | 95.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=94.3，有序区 95.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR005888, IPR016040, IPR036291; Pfam: PF16363 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UGDH | 0.967 | 0.000 | — |
| GMPPB | 0.845 | 0.000 | — |
| COQ3 | 0.845 | 0.000 | — |
| GMPPA | 0.818 | 0.000 | — |
| EIF2B3 | 0.818 | 0.000 | — |
| EIF2B5 | 0.816 | 0.000 | — |
| GALT | 0.780 | 0.000 | — |
| IL11RA | 0.778 | 0.000 | — |
| G3V4G9_HUMAN | 0.778 | 0.000 | — |
| GPR180 | 0.752 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NCK1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| PIK3R1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| GABARAP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| POTEE | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MTF2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TCAF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HTT | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| GPD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| LCMT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 9
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.3 + PDB: 无 | pLDDT=94.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum; Golgi apparatus / Nucleoplasm; 额外: Nucleoli, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 9 interactions | 数据充分 |

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
1. TGDS — UDP-D-glucose 4,6-dehydratase，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小350 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O95455
- Protein Atlas: https://www.proteinatlas.org/ENSG00000088451-TGDS/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TGDS
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95455
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000088451-TGDS/subcellular

![](https://images.proteinatlas.org/40857/542_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/40857/542_G1_2_red_green.jpg)
![](https://images.proteinatlas.org/40857/544_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/40857/544_G1_2_red_green.jpg)
![](https://images.proteinatlas.org/40857/571_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/40857/571_G1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O95455-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

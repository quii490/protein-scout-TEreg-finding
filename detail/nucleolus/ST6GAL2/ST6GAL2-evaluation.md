---
type: protein-evaluation
gene: "ST6GAL2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ST6GAL2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ST6GAL2 / KIAA1877, SIAT2 |
| 蛋白名称 | Beta-galactoside alpha-2,6-sialyltransferase 2 |
| 蛋白大小 | 529 aa / 60.2 kDa |
| UniProt ID | Q96JF0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli fibrillar center; 额外: Nucleoplasm; UniProt: Golgi apparatus, Golgi stack membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 529 aa / 60.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=17 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=75.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011330, IPR001675, IPR038578; Pfam: PF00777 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.5/180** | |
| **归一化总分** | | | **67.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli fibrillar center; 额外: Nucleoplasm | Approved |
| UniProt | Golgi apparatus, Golgi stack membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Golgi apparatus (GO:0005794)
- Golgi cisterna membrane (GO:0032580)
- Golgi membrane (GO:0000139)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17 |
| PubMed broad count | 28 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1877, SIAT2 |

**关键文献**:
1. Functional study of the ST6GAL2 gene regulating skeletal muscle growth and development.. *Heliyon*. PMID: 39296044
2. High-Throughput Analysis Reveals miRNA Upregulating α-2,6-Sialic Acid through Direct miRNA-mRNA Interactions.. *ACS central science*. PMID: 36439307
3. Bioinformatic Analysis of Gene Expression Related to Sialic Acid Biosynthesis in Patients With Medulloblastoma.. *Cureus*. PMID: 38854216
4. Integrated aqueous humor ceRNA and miRNA-TF-mRNA network analysis reveals potential molecular mechanisms governing primary open-angle glaucoma pathogenesis.. *Indian journal of ophthalmology*. PMID: 36727359
5. Majority of alpha2,6-sialylated glycans in the adult mouse brain exist in O-glycans: SALSA-MS analysis for knockout mice of alpha2,6-sialyltransferase genes.. *Glycobiology*. PMID: 33242079

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.0 |
| 高置信度残基 (pLDDT>90) 占比 | 60.5% |
| 置信残基 (pLDDT 70-90) 占比 | 5.5% |
| 中等置信 (pLDDT 50-70) 占比 | 2.6% |
| 低置信 (pLDDT<50) 占比 | 31.4% |
| 有序区域 (pLDDT>70) 占比 | 66.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=75.0，有序区 66.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011330, IPR001675, IPR038578; Pfam: PF00777 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| B4GALT2 | 0.958 | 0.000 | — |
| B4GALT1 | 0.950 | 0.000 | — |
| B4GALT3 | 0.925 | 0.000 | — |
| ST6GAL1 | 0.913 | 0.000 | — |
| ST8SIA1 | 0.548 | 0.000 | — |
| NEU2 | 0.516 | 0.000 | — |
| ZNF614 | 0.507 | 0.000 | — |
| NEU4 | 0.495 | 0.000 | — |
| SLC5A7 | 0.489 | 0.000 | — |
| WDR64 | 0.480 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MCM7 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:23764002|imex:IM-20916 |
| CD53 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| PGRMC2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| GPX8 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TIMMDC1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| AQP6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SLC26A1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ENSP00000387332.3 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| SLC39A2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| FNDC9 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.0 + PDB: 无 | pLDDT=75.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus, Golgi stack membrane / Nucleoli fibrillar center; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. ST6GAL2 — Beta-galactoside alpha-2,6-sialyltransferase 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小529 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 17 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96JF0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000144057-ST6GAL2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ST6GAL2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96JF0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli fibrillar center (approved)。来源: https://www.proteinatlas.org/ENSG00000144057-ST6GAL2/subcellular

![](https://images.proteinatlas.org/14459/120_G4_1_red_green.jpg)
![](https://images.proteinatlas.org/14459/120_G4_2_red_green.jpg)
![](https://images.proteinatlas.org/14459/1442_D1_1_red_green.jpg)
![](https://images.proteinatlas.org/14459/1442_D1_3_red_green.jpg)
![](https://images.proteinatlas.org/14459/1669_D2_1_red_green.jpg)
![](https://images.proteinatlas.org/14459/1669_D2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96JF0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

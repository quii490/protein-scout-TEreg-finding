---
type: protein-evaluation
gene: "GAL3ST4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GAL3ST4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GAL3ST4 |
| 蛋白名称 | Galactose-3-O-sulfotransferase 4 |
| 蛋白大小 | 486 aa / 54.2 kDa |
| UniProt ID | Q96RP7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Golgi apparatus, Golgi stack membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 486 aa / 54.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=79.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR009729, IPR027417; Pfam: PF06990 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.5/180** | |
| **归一化总分** | | | **67.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Golgi apparatus, Golgi stack membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- extracellular exosome (GO:0070062)
- Golgi cisterna membrane (GO:0032580)
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 17 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Prognostic models of immune-related cell death and stress unveil mechanisms driving macrophage phenotypic evolution in colorectal cancer.. *Journal of translational medicine*. PMID: 39875913
2. Sulfation of O-glycans on Mucin-type Proteins From Serous Ovarian Epithelial Tumors.. *Molecular & cellular proteomics : MCP*. PMID: 34555499
3. Interrogation of macrophage-related prognostic signatures reveals a potential immune-mediated therapy strategy by histone deacetylase inhibition in glioma.. *Frontiers in oncology*. PMID: 40548122
4. Identification of novel genetic loci GAL3ST4 and CHGB involved in susceptibility to leprosy.. *Scientific reports*. PMID: 29180661
5. Gene expression changes in male and female rhesus macaque 60 days after irradiation.. *PloS one*. PMID: 34288924

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.3 |
| 高置信度残基 (pLDDT>90) 占比 | 63.0% |
| 置信残基 (pLDDT 70-90) 占比 | 7.8% |
| 中等置信 (pLDDT 50-70) 占比 | 6.2% |
| 低置信 (pLDDT<50) 占比 | 23.0% |
| 有序区域 (pLDDT>70) 占比 | 70.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=79.3，有序区 70.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009729, IPR027417; Pfam: PF06990 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ABI3 | 0.514 | 0.000 | — |
| SBNO2 | 0.504 | 0.000 | — |
| TINAG | 0.484 | 0.000 | — |
| SRPX2 | 0.477 | 0.000 | — |
| SYT14 | 0.465 | 0.000 | — |
| H3C7 | 0.461 | 0.000 | — |
| INPP5D | 0.461 | 0.000 | — |
| LRRC25 | 0.459 | 0.000 | — |
| GCNT4 | 0.456 | 0.000 | — |
| LRRN1 | 0.451 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ESR2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:25604459|imex:IM-23333 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 14，IntAct interactions: 1
- 调控相关比例: 0 / 14 = 0%

**评价**: STRING 14 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.3 + PDB: 无 | pLDDT=79.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus, Golgi stack membrane / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 14 + 1 interactions | 数据充分 |

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
1. GAL3ST4 — Galactose-3-O-sulfotransferase 4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小486 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96RP7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000197093-GAL3ST4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GAL3ST4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96RP7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000197093-GAL3ST4/subcellular

![](https://images.proteinatlas.org/38138/1453_B6_1_red_green.jpg)
![](https://images.proteinatlas.org/38138/1453_B6_2_red_green.jpg)
![](https://images.proteinatlas.org/38138/1484_B6_2_red_green.jpg)
![](https://images.proteinatlas.org/38138/1484_B6_3_red_green.jpg)
![](https://images.proteinatlas.org/38138/1576_H8_1_red_green.jpg)
![](https://images.proteinatlas.org/38138/1576_H8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96RP7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96RP7 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR009729;IPR027417; |
| Pfam | PF06990; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000197093-GAL3ST4/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

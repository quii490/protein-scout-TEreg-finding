---
type: protein-evaluation
gene: "VPS9D1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## VPS9D1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | VPS9D1 / ATPBL, C16orf7 |
| 蛋白名称 | VPS9 domain-containing protein 1 |
| 蛋白大小 | 631 aa / 69.0 kDa |
| UniProt ID | Q9Y2B5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cytosol; 额外: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 631 aa / 69.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=27 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=75.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003123, IPR045046, IPR037191; Pfam: PF02204 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.5/180** | |
| **归一化总分** | | | **61.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- endocytic vesicle (GO:0030139)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 27 |
| PubMed broad count | 49 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ATPBL, C16orf7 |

**关键文献**:
1. Vps9d1 regulates tubular endosome formation through specific activation of Rab22A.. *Journal of cell science*. PMID: 36762583
2. VPS9D1-AS1 gene rs7206570 polymorphism associated with the clinical stage of colorectal cancer and binding with hsa-miR-361-3p.. *Human cell*. PMID: 35022999
3. LncRNA VPS9D1-AS1 Promotes Malignant Progression of Lung Adenocarcinoma by Targeting miRNA-30a-5p/KIF11 Axis.. *Frontiers in genetics*. PMID: 35140744
4. LncRNA VPS9D1-AS1 Sponging miR-520a-5p Contributes to the Development of Uterine Corpus Endometrial Carcinoma by Enhancing BIRC5 Expression.. *Molecular biotechnology*. PMID: 35619019
5. Long non-coding RNA VPS9D1-AS1 enhances proliferation, invasion, and epithelial-mesenchymal transition in endometrial cancer via miR-377-3p/SGK1.. *The Kaohsiung journal of medical sciences*. PMID: 36245426

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.2 |
| 高置信度残基 (pLDDT>90) 占比 | 47.2% |
| 置信残基 (pLDDT 70-90) 占比 | 22.2% |
| 中等置信 (pLDDT 50-70) 占比 | 7.8% |
| 低置信 (pLDDT<50) 占比 | 22.8% |
| 有序区域 (pLDDT>70) 占比 | 69.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=75.2，有序区 69.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003123, IPR045046, IPR037191; Pfam: PF02204 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SPATA2L | 0.797 | 0.000 | — |
| ZNF276 | 0.694 | 0.000 | — |
| PDX1 | 0.610 | 0.610 | — |
| NAV3 | 0.610 | 0.610 | — |
| DDX39A | 0.569 | 0.292 | — |
| DBNDD1 | 0.512 | 0.000 | — |
| DTX2 | 0.503 | 0.000 | — |
| CHMP1A | 0.495 | 0.000 | — |
| ASB3 | 0.467 | 0.000 | — |
| ZNF213 | 0.455 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000374037.3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CLU | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| DISC1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| UBXN11 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TRIM27 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TTC23L | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| RSPH14 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| AAMDC | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MAP1LC3A | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| RAD51D | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.2 + PDB: 无 | pLDDT=75.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Cytosol; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. VPS9D1 — VPS9 domain-containing protein 1，非常新颖，仅有少数基础研究。
2. 蛋白大小631 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 27 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y2B5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000075399-VPS9D1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=VPS9D1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y2B5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000075399-VPS9D1/subcellular

![](https://images.proteinatlas.org/23620/192_F10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23620/192_F10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/23620/193_F10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23620/193_F10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/23620/194_F10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23620/194_F10_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y2B5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9Y2B5 |
| SMART | SM00167; |
| UniProt Domain [FT] | DOMAIN 467..630; /note="VPS9"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00550" |
| InterPro | IPR003123;IPR045046;IPR037191; |
| Pfam | PF02204; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000075399-VPS9D1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| IST1 | Intact, Biogrid, Opencell | true |
| AAMDC | Intact | false |
| AHSP | Intact | false |
| ATOSB | Intact | false |
| CCDC172 | Intact | false |
| CSNK2A2 | Opencell | false |
| DYDC1 | Intact | false |
| KRT31 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

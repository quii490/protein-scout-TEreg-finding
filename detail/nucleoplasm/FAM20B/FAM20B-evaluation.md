---
type: protein-evaluation
gene: "FAM20B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM20B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM20B / KIAA0475 |
| 蛋白名称 | Glycosaminoglycan xylosylkinase |
| 蛋白大小 | 409 aa / 46.4 kDa |
| UniProt ID | O75063 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Golgi apparatus; 额外: Nucleoplasm; UniProt: Golgi apparatus membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 409 aa / 46.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=28 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=93.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR024869, IPR009581; Pfam: PF06702 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.5/180** | |
| **归一化总分** | | | **71.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nucleoplasm | Supported |
| UniProt | Golgi apparatus membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Golgi apparatus (GO:0005794)
- Golgi membrane (GO:0000139)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 28 |
| PubMed broad count | 43 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0475 |

**关键文献**:
1. Lack of association between PAX6/SOSTDC1/FAM20B gene polymorphisms and mesiodens.. *BMC oral health*. PMID: 31133012
2. The ABCs of the atypical Fam20 secretory pathway kinases.. *The Journal of biological chemistry*. PMID: 33759783
3. FAM20B is a kinase that phosphorylates xylose in the glycosaminoglycan-protein linkage region.. *The Biochemical journal*. PMID: 19473117
4. Xylose phosphorylation functions as a molecular switch to regulate proteoglycan biosynthesis.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 25331875
5. EXTL2 controls liver regeneration and aortic calcification through xylose kinase-dependent regulation of glycosaminoglycan biosynthesis.. *Matrix biology : journal of the International Society for Matrix Biology*. PMID: 24176719

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.2 |
| 高置信度残基 (pLDDT>90) 占比 | 83.4% |
| 置信残基 (pLDDT 70-90) 占比 | 11.5% |
| 中等置信 (pLDDT 50-70) 占比 | 3.7% |
| 低置信 (pLDDT<50) 占比 | 1.5% |
| 有序区域 (pLDDT>70) 占比 | 94.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=93.2，有序区 94.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR024869, IPR009581; Pfam: PF06702 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| XYLT1 | 0.751 | 0.000 | — |
| GASK1A | 0.714 | 0.000 | — |
| EXTL2 | 0.702 | 0.000 | — |
| B3GALT6 | 0.701 | 0.000 | — |
| NAT9 | 0.699 | 0.000 | — |
| B3GAT3 | 0.687 | 0.000 | — |
| B4GALT7 | 0.671 | 0.000 | — |
| POR | 0.669 | 0.000 | — |
| PXYLP1 | 0.668 | 0.000 | — |
| XYLT2 | 0.659 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ASPHD2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LPAR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| IPPK | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PVR | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CD79B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SLC7A14 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| TMEM80 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| FFAR2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| FAM209A | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| DCN | psi-mi:"MI:0841"(phosphotransferase assay) | pubmed:25331875|imex:IM-25585 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.2 + PDB: 无 | pLDDT=93.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus membrane / Golgi apparatus; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. FAM20B — Glycosaminoglycan xylosylkinase，非常新颖，仅有少数基础研究。
2. 蛋白大小409 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 28 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75063
- Protein Atlas: https://www.proteinatlas.org/ENSG00000116199-FAM20B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM20B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75063
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (supported)。来源: https://www.proteinatlas.org/ENSG00000116199-FAM20B/subcellular

![](https://images.proteinatlas.org/7409/1189_F8_3_red_green.jpg)
![](https://images.proteinatlas.org/7409/1189_F8_6_red_green.jpg)
![](https://images.proteinatlas.org/7409/1219_F8_3_red_green.jpg)
![](https://images.proteinatlas.org/7409/1219_F8_4_red_green.jpg)
![](https://images.proteinatlas.org/7409/1252_C6_1_red_green.jpg)
![](https://images.proteinatlas.org/7409/1252_C6_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O75063-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O75063 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR024869;IPR009581; |
| Pfam | PF06702; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000116199-FAM20B/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ASPHD2 | Intact | false |
| B3GAT2 | Bioplex | false |
| BSCL2 | Biogrid | false |
| CD27 | Bioplex | false |
| DCN | Intact | false |
| FAM174A | Bioplex | false |
| FAM209A | Intact | false |
| FFAR2 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

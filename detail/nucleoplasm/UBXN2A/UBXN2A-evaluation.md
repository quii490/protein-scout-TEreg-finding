---
type: protein-evaluation
gene: "UBXN2A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## UBXN2A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | UBXN2A / UBXD4 |
| 蛋白名称 | UBX domain-containing protein 2A |
| 蛋白大小 | 259 aa / 29.3 kDa |
| UniProt ID | P68543 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Centrosome; UniProt: Golgi apparatus; Endoplasmic reticulum; Perikaryon; Cell pro |
| 蛋白大小 | 10/10 | ×1 | 10 | 259 aa / 29.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=73.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036241, IPR012989, IPR029071, IPR001012; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Centrosome | Approved |
| UniProt | Golgi apparatus; Endoplasmic reticulum; Perikaryon; Cell projection, dendrite; Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cis-Golgi network (GO:0005801)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- dendrite (GO:0030425)
- endoplasmic reticulum (GO:0005783)
- Golgi apparatus (GO:0005794)
- nucleus (GO:0005634)
- perikaryon (GO:0043204)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 19 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: UBXD4 |

**关键文献**:
1. UBXN2A suppresses the Rictor-mTORC2 signaling pathway, an established tumorigenic pathway in human colorectal cancer.. *Oncogene*. PMID: 37037900
2. Pre-clinical safety and therapeutic efficacy of a plant-based alkaloid in a human colon cancer xenograft model.. *Cell death discovery*. PMID: 35347121
3. UBXN2A enhances CHIP-mediated proteasomal degradation of oncoprotein mortalin-2 in cancer cells.. *Molecular oncology*. PMID: 30107089
4. Structural studies of UBXN2A and mortalin interaction and the putative role of silenced UBXN2A in preventing response to chemotherapy.. *Cell stress & chaperones*. PMID: 26634371
5. UBXN2A, a Ubiquitin-Like Protein, Alters Proteins in mTORC2 Pathway.. *South Dakota medicine : the journal of the South Dakota State Medical Association*. PMID: 36889268

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.4 |
| 高置信度残基 (pLDDT>90) 占比 | 33.2% |
| 置信残基 (pLDDT 70-90) 占比 | 25.9% |
| 中等置信 (pLDDT 50-70) 占比 | 21.2% |
| 低置信 (pLDDT<50) 占比 | 19.7% |
| 有序区域 (pLDDT>70) 占比 | 59.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=73.4，有序区 59.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036241, IPR012989, IPR029071, IPR001012; Pfam: PF08059, PF00789 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| VCP | 0.999 | 0.995 | — |
| NSFL1C | 0.999 | 0.994 | — |
| ASPSCR1 | 0.997 | 0.994 | — |
| UBXN10 | 0.997 | 0.994 | — |
| VCPIP1 | 0.995 | 0.994 | — |
| LACTB | 0.994 | 0.994 | — |
| UBXN6 | 0.993 | 0.786 | — |
| UBXN8 | 0.965 | 0.094 | — |
| UBXN1 | 0.963 | 0.095 | — |
| SVIP | 0.957 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Vcp | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12121|pubmed:18775313 |
| VCPIP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| DYDC2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| UBXN6 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| PPP1R11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PPP1R7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ASPSCR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ENSP00000385525.1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-21138|pubmed:21911577 |
| MYH11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Uso1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.4 + PDB: 无 | pLDDT=73.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus; Endoplasmic reticulum; Perikaryon / Centrosome | 一致 |
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
1. UBXN2A — UBX domain-containing protein 2A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小259 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P68543
- Protein Atlas: https://www.proteinatlas.org/ENSG00000173960-UBXN2A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=UBXN2A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P68543
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Centrosome (approved)。来源: https://www.proteinatlas.org/ENSG00000173960-UBXN2A/subcellular

![](https://images.proteinatlas.org/65482/1263_C3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/65482/1263_C3_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/65482/1270_C3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/65482/1270_C3_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/65482/1417_A1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/65482/1417_A1_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P68543-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P68543 |
| SMART | SM00553;SM00166; |
| UniProt Domain [FT] | DOMAIN 60..124; /note="SEP"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00732"; DOMAIN 169..246; /note="UBX"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00215" |
| InterPro | IPR036241;IPR012989;IPR029071;IPR001012; |
| Pfam | PF08059;PF00789; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000173960-UBXN2A/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| UBXN6 | Intact, Biogrid | true |
| VCP | Intact, Biogrid, Opencell, Bioplex | true |
| ASPSCR1 | Biogrid | false |
| DYDC2 | Intact | false |
| HSPA9 | Biogrid | false |
| NSFL1C | Biogrid | false |
| PPP1CB | Biogrid | false |
| PPP1R11 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

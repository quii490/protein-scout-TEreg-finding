---
type: protein-evaluation
gene: "FOXJ2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FOXJ2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FOXJ2 / FHX |
| 蛋白名称 | Forkhead box protein J2 |
| 蛋白大小 | 574 aa / 62.4 kDa |
| UniProt ID | Q9P0K8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Nucleoli fibrillar center; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 574 aa / 62.4 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=46 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR047393, IPR001766, IPR045912, IPR030456, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 7 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli fibrillar center | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- fibrillar center (GO:0001650)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 46 |
| PubMed broad count | 70 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FHX |

**关键文献**:
1. Genomic analyses identify recurrent MEF2D fusions in acute lymphoblastic leukaemia.. *Nature communications*. PMID: 27824051
2. Foxj2 Attenuates LPS-Induced Inflammatory Response in Macrophages.. *Mediators of inflammation*. PMID: 41498035
3. Human FOX gene family (Review).. *International journal of oncology*. PMID: 15492844
4. Granulosa cell-specific FOXJ2 overexpression induces premature ovarian insufficiency by triggering apoptosis via mitochondrial calcium overload.. *Journal of ovarian research*. PMID: 40205506
5. Germline FOXJ2 overexpression causes male infertility via aberrant autophagy activation by LAMP2A upregulation.. *Cell death & disease*. PMID: 35908066

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.3 |
| 高置信度残基 (pLDDT>90) 占比 | 11.0% |
| 置信残基 (pLDDT 70-90) 占比 | 16.7% |
| 中等置信 (pLDDT 50-70) 占比 | 20.2% |
| 低置信 (pLDDT<50) 占比 | 52.1% |
| 有序区域 (pLDDT>70) 占比 | 27.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=57.3），有序残基占 27.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR047393, IPR001766, IPR045912, IPR030456, IPR036388; Pfam: PF00250 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| POU3F2 | 0.707 | 0.000 | — |
| MAGEA10 | 0.638 | 0.624 | — |
| RFX1 | 0.596 | 0.185 | — |
| PAX2 | 0.564 | 0.000 | — |
| CRTC3 | 0.560 | 0.000 | — |
| EGLN3 | 0.543 | 0.543 | — |
| GATAD2B | 0.530 | 0.164 | — |
| PAX4 | 0.511 | 0.053 | — |
| PAX6 | 0.495 | 0.053 | — |
| SREBF2 | 0.479 | 0.061 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| rcsC | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| CSTF2T | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| EGLN3 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |
| MAGEA10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| XCL2 | psi-mi:"MI:0432"(one hybrid) | doi:10.1093/nar/gkaa1055|pubme |
| Cers2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| ENST00000162391 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 7
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 7 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.3 + PDB: 无 | pLDDT=57.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Nucleoli fibrillar center | 一致 |
| PPI | STRING + IntAct | 15 + 7 interactions | 数据充分 |

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
1. FOXJ2 — Forkhead box protein J2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小574 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 46 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=57.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9P0K8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000065970-FOXJ2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FOXJ2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P0K8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000065970-FOXJ2/subcellular

![](https://images.proteinatlas.org/8723/41_E10_1_red_green.jpg)
![](https://images.proteinatlas.org/8723/41_E10_2_red_green.jpg)
![](https://images.proteinatlas.org/8723/42_E10_1_red_green.jpg)
![](https://images.proteinatlas.org/8723/42_E10_2_red_green.jpg)
![](https://images.proteinatlas.org/8723/43_E10_1_red_green.jpg)
![](https://images.proteinatlas.org/8723/43_E10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9P0K8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9P0K8 |
| SMART | SM00339; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR047393;IPR001766;IPR045912;IPR030456;IPR036388;IPR036390; |
| Pfam | PF00250; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000065970-FOXJ2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CSTF2T | Intact | false |
| EGLN3 | Intact | false |
| MAGEA10 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

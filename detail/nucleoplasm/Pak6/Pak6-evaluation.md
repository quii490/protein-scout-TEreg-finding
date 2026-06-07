---
type: protein-evaluation
gene: "Pak6"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## Pak6 — REJECTED (研究热度过高 (PubMed strict=110，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | Pak6 / PAK5 |
| 蛋白名称 | Serine/threonine-protein kinase PAK 6 |
| 蛋白大小 | 681 aa / 74.9 kDa |
| UniProt ID | Q9NQU5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli fibrillar center; 额外: Cell Junctions; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 681 aa / 74.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=110 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.0; PDB: 2C30, 2ODB, 4KS7, 4KS8, 6QDR, 6QDS |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000095, IPR036936, IPR011009, IPR051931, IPR033 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli fibrillar center; 额外: Cell Junctions | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell junction (GO:0030054)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- fibrillar center (GO:0001650)
- nucleoplasm (GO:0005654)
- postsynaptic density (GO:0014069)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 110 |
| PubMed broad count | 151 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PAK5 |

**关键文献**:
1. PAK6 rescues pathogenic LRRK2-mediated ciliogenesis and centrosomal cohesion defects in a mutation-specific manner.. *Cell death & disease*. PMID: 39419978
2. Dual STAT3/STAT5 inhibition as a novel treatment strategy in T-prolymphocytic leukemia.. *Leukemia*. PMID: 40234614
3. Prospective Role of PAK6 and 14-3-3γ as Biomarkers for Parkinson's Disease.. *Journal of Parkinson's disease*. PMID: 38640169
4. Differential roles and regulation of the protein kinases PAK4, PAK5 and PAK6 in melanoma cells.. *The Biochemical journal*. PMID: 35969127
5. Direct interaction between AR and PAK6 in androgen-stimulated PAK6 activation.. *PloS one*. PMID: 24130878

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.0 |
| 高置信度残基 (pLDDT>90) 占比 | 38.8% |
| 置信残基 (pLDDT 70-90) 占比 | 8.2% |
| 中等置信 (pLDDT 50-70) 占比 | 8.7% |
| 低置信 (pLDDT<50) 占比 | 44.3% |
| 有序区域 (pLDDT>70) 占比 | 47.0% |
| 可用 PDB 条目 | 2C30, 2ODB, 4KS7, 4KS8, 6QDR, 6QDS |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=66.0），有序残基占 47.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000095, IPR036936, IPR011009, IPR051931, IPR033923; Pfam: PF00786, PF00069 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDC42 | 0.999 | 0.958 | — |
| AR | 0.962 | 0.625 | — |
| ARHGEF7 | 0.962 | 0.113 | — |
| NCK1 | 0.952 | 0.171 | — |
| RAC2 | 0.944 | 0.303 | — |
| LIMK1 | 0.942 | 0.317 | — |
| PAK4 | 0.938 | 0.820 | — |
| ARHGEF6 | 0.935 | 0.113 | — |
| RAC3 | 0.934 | 0.303 | — |
| RAC1 | 0.934 | 0.755 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| YWHAQ | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| CDK1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| NEK6 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| SNX2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| TPD52L1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| SEMA3B | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| CDC42 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| RHOJ | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| HSF2BP | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.0 + PDB: 2C30, 2ODB, 4KS7, 4KS8, 6QDR,  | pLDDT=66.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm, Nucleoli fibrillar center; 额外: Cell J | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. Pak6 — Serine/threonine-protein kinase PAK 6，研究基础较多，新颖性有限。
2. 蛋白大小681 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 110 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=66.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 110 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NQU5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000137843-PAK6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=Pak6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NQU5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000137843-PAK6/subcellular

![](https://images.proteinatlas.org/31124/1240_A7_3_red_green.jpg)
![](https://images.proteinatlas.org/31124/1240_A7_4_red_green.jpg)
![](https://images.proteinatlas.org/31124/331_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/31124/331_G5_3_red_green.jpg)
![](https://images.proteinatlas.org/31124/333_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/31124/333_G5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NQU5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NQU5 |
| SMART | SM00285; |
| UniProt Domain [FT] | DOMAIN 12..25; /note="CRIB"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00057"; DOMAIN 407..658; /note="Protein kinase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00159" |
| InterPro | IPR000095;IPR036936;IPR011009;IPR051931;IPR033923;IPR000719;IPR017441;IPR035066; |
| Pfam | PF00786;PF00069; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000137843-PAK6/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CDC42 | Intact, Biogrid | true |
| LRRK2 | Intact, Biogrid | true |
| YWHAE | Intact, Biogrid | true |
| YWHAQ | Intact, Biogrid | true |
| AR | Biogrid | false |
| HSF2BP | Intact | false |
| MAK16 | Bioplex | false |
| MDM2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

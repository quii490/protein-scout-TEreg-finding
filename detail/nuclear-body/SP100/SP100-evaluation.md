---
type: protein-evaluation
gene: "Sp100"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## Sp100 — REJECTED (研究热度过高 (PubMed strict=324，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | Sp100 |
| 蛋白名称 | Nuclear autoantigen Sp-100 |
| 蛋白大小 | 879 aa / 100.4 kDa |
| UniProt ID | P23497 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear bodies; 额外: Nucleoplasm; UniProt: Nucleus; Nucleus, PML body; Nucleus, nuclear body; Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 879 aa / 100.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=324 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.9; PDB: 1H5P, 4PTB, 5FB0, 5FB1, 5PWE, 5PWF, 5PWG |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR009071, IPR036910, IPR004865, IPR010919, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.5/180** | |
| **归一化总分** | | | **44.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies; 额外: Nucleoplasm | Supported |
| UniProt | Nucleus; Nucleus, PML body; Nucleus, nuclear body; Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromosome, telomeric region (GO:0000781)
- cytoplasm (GO:0005737)
- nuclear body (GO:0016604)
- nuclear periphery (GO:0034399)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- PML body (GO:0016605)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 324 |
| PubMed broad count | 560 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. The Fate of Speckled Protein 100 (Sp100) During Herpesviruses Infection.. *Frontiers in cellular and infection microbiology*. PMID: 33598438
2. Expression, prognostic value and mechanism of SP100 family in pancreatic adenocarcinoma.. *Aging*. PMID: 37354211
3. Early Nuclear Events after Herpesviral Infection.. *Journal of clinical medicine*. PMID: 31500286
4. Identification of major linear epitopes on the sp100 nuclear PBC autoantigen by the gene-fragment phage-display technology.. *Autoimmunity*. PMID: 10052683
5. The Speckled Protein (SP) Family: Immunity's Chromatin Readers.. *Trends in immunology*. PMID: 32386862

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.9 |
| 高置信度残基 (pLDDT>90) 占比 | 13.5% |
| 置信残基 (pLDDT 70-90) 占比 | 21.2% |
| 中等置信 (pLDDT 50-70) 占比 | 9.6% |
| 低置信 (pLDDT<50) 占比 | 55.7% |
| 有序区域 (pLDDT>70) 占比 | 34.7% |
| 可用 PDB 条目 | 1H5P, 4PTB, 5FB0, 5FB1, 5PWE, 5PWF, 5PWG, 5PWH, 5PWI, 5PWJ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=56.9），有序残基占 34.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009071, IPR036910, IPR004865, IPR010919, IPR000770; Pfam: PF00505, PF09011, PF03172 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SUMO1 | 0.997 | 0.778 | — |
| DAXX | 0.996 | 0.071 | — |
| ATRX | 0.991 | 0.058 | — |
| HSPA4 | 0.987 | 0.047 | — |
| PML | 0.981 | 0.757 | — |
| UBE2I | 0.952 | 0.839 | — |
| H3-3B | 0.934 | 0.906 | — |
| SUMO2 | 0.933 | 0.599 | — |
| H3C12 | 0.929 | 0.906 | — |
| H3C13 | 0.928 | 0.906 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000386404.1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ENSP00000264052.5 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| SUMO1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| SUMO2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| CREM | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| SUMO3 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:17000644|imex:IM-19940 |
| NS | psi-mi:"MI:0018"(two hybrid) | imex:IM-13585|pubmed:20064372 |
| UBE2I | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| FOXL2 | psi-mi:"MI:0018"(two hybrid) | pubmed:22022399|imex:IM-26668 |
| H1-10 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.9 + PDB: 1H5P, 4PTB, 5FB0, 5FB1, 5PWE,  | pLDDT=56.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, PML body; Nucleus, nuclear body; / Nuclear bodies; 额外: Nucleoplasm | 一致 |
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
1. Sp100 — Nuclear autoantigen Sp-100，研究基础较多，新颖性有限。
2. 蛋白大小879 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 324 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=56.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 324 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P23497
- Protein Atlas: https://www.proteinatlas.org/ENSG00000067066-SP100/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=Sp100
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P23497
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (supported)。来源: https://www.proteinatlas.org/ENSG00000067066-SP100/subcellular

![](https://images.proteinatlas.org/17384/140_F8_1_red_green.jpg)
![](https://images.proteinatlas.org/17384/140_F8_2_red_green.jpg)
![](https://images.proteinatlas.org/17384/168_F8_1_red_green.jpg)
![](https://images.proteinatlas.org/17384/168_F8_2_red_green.jpg)
![](https://images.proteinatlas.org/17384/173_F8_1_red_green.jpg)
![](https://images.proteinatlas.org/17384/173_F8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P23497-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P23497 |
| SMART | SM00398;SM00258; |
| UniProt Domain [FT] | DOMAIN 33..149; /note="HSR"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00747"; DOMAIN 595..676; /note="SAND"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00185" |
| InterPro | IPR009071;IPR036910;IPR004865;IPR010919;IPR000770;IPR043563; |
| Pfam | PF00505;PF09011;PF03172;PF01342; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000067066-SP100/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| SUMO1 | Intact, Biogrid | true |
| ACTN2 | Intact | false |
| ARID3A | Biogrid | false |
| CBX1 | Biogrid | false |
| CBX3 | Biogrid | false |
| CBX5 | Biogrid | false |
| CREM | Intact | false |
| DNMT3A | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

---
type: protein-evaluation
gene: "SMAD1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SMAD1 — REJECTED (研究热度过高 (PubMed strict=2534，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SMAD1 / BSP1, MADH1, MADR1 |
| 蛋白名称 | SMAD family member 1 |
| 蛋白大小 | 465 aa / 52.3 kDa |
| UniProt ID | Q15797 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 465 aa / 52.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=2534 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=81.2; PDB: 1KHU, 2LAW, 2LAX, 2LAY, 2LAZ, 2LB0, 2LB1 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR013790, IPR003619, IPR013019, IPR017855, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- heteromeric SMAD protein complex (GO:0071144)
- homomeric SMAD protein complex (GO:0071142)
- membrane (GO:0016020)
- nuclear inner membrane (GO:0005637)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2534 |
| PubMed broad count | 3597 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BSP1, MADH1, MADR1 |

**关键文献**:
1. A KLF2-BMPER-Smad1/5 checkpoint regulates high fluid shear stress-mediated artery remodeling.. *Nature cardiovascular research*. PMID: 39196179
2. ActRII or BMPR ligands inhibit skeletal myoblast differentiation, and BMPs promote heterotopic ossification in skeletal muscles in mice.. *Skeletal muscle*. PMID: 39994804
3. GSK3β Inhibition Ameliorates Atherosclerotic Calcification.. *International journal of molecular sciences*. PMID: 37511396
4. BMP-SMAD1/5 Signaling Regulates Retinal Vascular Development.. *Biomolecules*. PMID: 32210087
5. AHNAK inhibits osteoporosis progression by stabilizing Smad1 protein.. *Experimental cell research*. PMID: 41554467

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.2 |
| 高置信度残基 (pLDDT>90) 占比 | 62.8% |
| 置信残基 (pLDDT 70-90) 占比 | 12.9% |
| 中等置信 (pLDDT 50-70) 占比 | 4.9% |
| 低置信 (pLDDT<50) 占比 | 19.4% |
| 有序区域 (pLDDT>70) 占比 | 75.7% |
| 可用 PDB 条目 | 1KHU, 2LAW, 2LAX, 2LAY, 2LAZ, 2LB0, 2LB1, 3Q47, 3Q4A, 5ZOK |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1KHU, 2LAW, 2LAX, 2LAY, 2LAZ, 2LB0, 2LB1, 3Q47, 3Q4A, 5ZOK）+ AlphaFold极高置信度预测（pLDDT=81.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013790, IPR003619, IPR013019, IPR017855, IPR001132; Pfam: PF03165, PF03166 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SMURF1 | 0.998 | 0.992 | — |
| SMAD4 | 0.997 | 0.939 | — |
| SMAD6 | 0.985 | 0.748 | — |
| LEMD3 | 0.982 | 0.980 | — |
| SMAD2 | 0.979 | 0.624 | — |
| ACVR1 | 0.978 | 0.655 | — |
| BMPR1A | 0.967 | 0.400 | — |
| MAPK1 | 0.965 | 0.625 | — |
| YAP1 | 0.962 | 0.760 | — |
| SMAD3 | 0.954 | 0.474 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000426568.1 | psi-mi:"MI:0071"(molecular sieving) | imex:IM-23817|pubmed:11779505 |
| YWHAQ | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| SMAD2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:18729074|imex:IM-19222 |
| SMAD3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:18729074|imex:IM-19222 |
| CSNK1A1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-17578|pubmed:23455922 |
| YWHAH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| VAPA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| VAPB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAG | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.2 + PDB: 1KHU, 2LAW, 2LAX, 2LAY, 2LAZ,  | pLDDT=81.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. SMAD1 — SMAD family member 1，研究基础较多，新颖性有限。
2. 蛋白大小465 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2534 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 2534 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q15797
- Protein Atlas: https://www.proteinatlas.org/ENSG00000170365-SMAD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SMAD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15797
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000170365-SMAD1/subcellular

![](https://images.proteinatlas.org/5389/963_E12_3_red_green.jpg)
![](https://images.proteinatlas.org/5389/963_E12_4_red_green.jpg)
![](https://images.proteinatlas.org/5389/968_E12_1_red_green.jpg)
![](https://images.proteinatlas.org/5389/968_E12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q15797-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q15797 |
| SMART | SM00523;SM00524; |
| UniProt Domain [FT] | DOMAIN 12..136; /note="MH1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00438"; DOMAIN 271..465; /note="MH2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00439" |
| InterPro | IPR013790;IPR003619;IPR013019;IPR017855;IPR001132;IPR008984;IPR036578; |
| Pfam | PF03165;PF03166; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000170365-SMAD1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AR | Intact, Biogrid | true |
| GSK3B | Intact, Biogrid | true |
| LEMD3 | Intact, Biogrid | true |
| PSMB4 | Intact, Biogrid | true |
| SMAD4 | Intact, Biogrid | true |
| SMAD6 | Intact, Biogrid | true |
| SMURF1 | Intact, Biogrid | true |
| SMURF2 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

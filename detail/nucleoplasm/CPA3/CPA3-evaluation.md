---
type: protein-evaluation
gene: "CPA3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CPA3 — REJECTED (研究热度过高 (PubMed strict=115，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CPA3 / CPA3 |
| 蛋白名称 | Carboxypeptidase A4 |
| 蛋白大小 | 421 aa / 47.4 kDa |
| UniProt ID | Q9UI42 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Golgi apparatus; 额外: Nucleoplasm; UniProt: Secreted |
| 蛋白大小 | 10/10 | ×1 | 10 | 421 aa / 47.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=115 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=93.7; PDB: 2BO9, 2BOA, 2PCU, 4A94, 4BD9 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR057246, IPR057247, IPR034248, IPR036990, IPR003 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **84.0/180** | |
| **归一化总分** | | | **46.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nucleoplasm | Approved |
| UniProt | Secreted | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- extracellular space (GO:0005615)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 115 |
| PubMed broad count | 228 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CPA3 |

**关键文献**:
1. Identification of novel gene signature for lung adenocarcinoma by machine learning to predict immunotherapy and prognosis.. *Frontiers in immunology*. PMID: 37583701
2. Identifying potential active ingredients from pomegranate in treating anemia: CPA3 and SOX4 are key proteins.. *International journal of biological macromolecules*. PMID: 39608521
3. Integrative eQTL and Mendelian randomization analysis reveals key genetic markers in mesothelioma.. *Respiratory research*. PMID: 40223054
4. The effects of inhaled corticosteroids on healthy airways.. *Allergy*. PMID: 38686450
5. Neuroplasticity and neuroimmune interactions in fatal asthma.. *Allergy*. PMID: 39484998

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.7 |
| 高置信度残基 (pLDDT>90) 占比 | 87.4% |
| 置信残基 (pLDDT 70-90) 占比 | 8.8% |
| 中等置信 (pLDDT 50-70) 占比 | 0.0% |
| 低置信 (pLDDT<50) 占比 | 3.8% |
| 有序区域 (pLDDT>70) 占比 | 96.2% |
| 可用 PDB 条目 | 2BO9, 2BOA, 2PCU, 4A94, 4BD9 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2BO9, 2BOA, 2PCU, 4A94, 4BD9）+ AlphaFold极高置信度预测（pLDDT=93.7），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR057246, IPR057247, IPR034248, IPR036990, IPR003146; Pfam: PF00246, PF02244 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CMA1 | 0.966 | 0.126 | — |
| TPSAB1 | 0.945 | 0.126 | — |
| MS4A2 | 0.938 | 0.000 | — |
| CPA1 | 0.922 | 0.000 | — |
| FCER1A | 0.921 | 0.000 | — |
| CPA2 | 0.918 | 0.000 | — |
| NDST2 | 0.897 | 0.000 | — |
| HDC | 0.883 | 0.000 | — |
| TPSB2 | 0.875 | 0.126 | — |
| CTSG | 0.812 | 0.126 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| H1-10 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| SLCO6A1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZIC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CFAP298 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CDK15 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TBC1D22B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZSCAN12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| AIRE | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ASCC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CCDC51 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.7 + PDB: 2BO9, 2BOA, 2PCU, 4A94, 4BD9 | pLDDT=93.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Secreted / Golgi apparatus; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CPA3 — Carboxypeptidase A4，研究基础较多，新颖性有限。
2. 蛋白大小421 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 115 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 115 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UI42
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163751-CPA3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CPA3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UI42
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (approved)。来源: https://www.proteinatlas.org/ENSG00000163751-CPA3/subcellular

![](https://images.proteinatlas.org/6479/10_B5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/6479/10_B5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/6479/11_B5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/6479/11_B5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/6479/1825_G10_22_cr5ac32dec149d6_blue_red_green.jpg)
![](https://images.proteinatlas.org/6479/1825_G10_5_cr5ac32dec139e3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UI42-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UI42 |
| SMART | SM00631; |
| UniProt Domain [FT] | DOMAIN 122..416; /note="Peptidase M14"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01379" |
| InterPro | IPR057246;IPR057247;IPR034248;IPR036990;IPR003146;IPR000834; |
| Pfam | PF00246;PF02244; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000163751-CPA3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DMTN | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

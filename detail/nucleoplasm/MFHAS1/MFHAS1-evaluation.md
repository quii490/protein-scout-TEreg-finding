---
type: protein-evaluation
gene: "MFHAS1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MFHAS1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MFHAS1 / MASL1 |
| 蛋白名称 | Malignant fibrous histiocytoma-amplified sequence 1 |
| 蛋白大小 | 1052 aa / 117.0 kDa |
| UniProt ID | Q9Y4C4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 1052 aa / 117.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=21 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=83.9; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001611, IPR003591, IPR032675, IPR050216, IPR027 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.5/180** | |
| **归一化总分** | | | **61.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 21 |
| PubMed broad count | 46 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MASL1 |

**关键文献**:
1. Genetic Loci Associated With Periodontitis: The FinnGen Study Based on National Health Registers.. *Journal of clinical periodontology*. PMID: 40682483
2. Ferroptosis-related prognostic model of mantle cell lymphoma.. *Open medicine (Warsaw, Poland)*. PMID: 39588389
3. Rare sequence variants associated with the risk of non-syndromic biliary atresia.. *Hepatology research : the official journal of the Japan Society of Hepatology*. PMID: 37491771
4. MFHAS1 suppresses TLR4 signaling pathway via induction of PP2A C subunit cytoplasm translocation and inhibition of c-Jun dephosphorylation at Thr239.. *Molecular immunology*. PMID: 28609714
5. Homozygous microdeletion of the ERI1 and MFHAS1 genes in a patient with intellectual disability, limb abnormalities, and cardiac malformation.. *American journal of medical genetics. Part A*. PMID: 28488351

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.9 |
| 高置信度残基 (pLDDT>90) 占比 | 58.0% |
| 置信残基 (pLDDT 70-90) 占比 | 26.7% |
| 中等置信 (pLDDT 50-70) 占比 | 5.0% |
| 低置信 (pLDDT<50) 占比 | 10.3% |
| 有序区域 (pLDDT>70) 占比 | 84.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=83.9，有序区 84.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001611, IPR003591, IPR032675, IPR050216, IPR027417; Pfam: PF13855 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CLDN23 | 0.970 | 0.000 | — |
| PPP1R3B | 0.929 | 0.000 | — |
| PJA2 | 0.738 | 0.292 | — |
| CAMSAP1 | 0.622 | 0.610 | — |
| STK25 | 0.524 | 0.163 | — |
| ADGRL2 | 0.522 | 0.514 | — |
| ADGRL3 | 0.522 | 0.514 | — |
| ADGRL1 | 0.522 | 0.514 | — |
| FAM90A7P | 0.506 | 0.000 | — |
| DAPK1 | 0.499 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| yscP | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| CEBPZ | psi-mi:"MI:0089"(protein array) | pubmed:29513927|doi:10.1002/pm |
| ANKS4B | psi-mi:"MI:0089"(protein array) | pubmed:29513927|doi:10.1002/pm |
| E2F4 | psi-mi:"MI:0089"(protein array) | pubmed:29513927|doi:10.1002/pm |
| PMM1 | psi-mi:"MI:0089"(protein array) | pubmed:29513927|doi:10.1002/pm |
| CCDC43 | psi-mi:"MI:0089"(protein array) | pubmed:29513927|doi:10.1002/pm |
| ANKRD13A | psi-mi:"MI:0089"(protein array) | pubmed:29513927|doi:10.1002/pm |
| ZMYM5 | psi-mi:"MI:0089"(protein array) | pubmed:29513927|doi:10.1002/pm |
| GAS2L3 | psi-mi:"MI:0089"(protein array) | pubmed:29513927|doi:10.1002/pm |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.9 + PDB: 无 | pLDDT=83.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm; 额外: Cytosol | 一致 |
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
1. MFHAS1 — Malignant fibrous histiocytoma-amplified sequence 1，非常新颖，仅有少数基础研究。
2. 蛋白大小1052 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 21 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y4C4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000147324-MFHAS1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MFHAS1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y4C4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000147324-MFHAS1/subcellular

![](https://images.proteinatlas.org/51213/704_D10_1_red_green.jpg)
![](https://images.proteinatlas.org/51213/704_D10_2_red_green.jpg)
![](https://images.proteinatlas.org/51213/762_B12_1_red_green.jpg)
![](https://images.proteinatlas.org/51213/762_B12_2_red_green.jpg)
![](https://images.proteinatlas.org/51213/858_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/51213/858_B1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y4C4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9Y4C4 |
| SMART | SM00364;SM00365;SM00369; |
| UniProt Domain [FT] | DOMAIN 403..649; /note="Roc"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00758" |
| InterPro | IPR001611;IPR003591;IPR032675;IPR050216;IPR027417;IPR020859; |
| Pfam | PF13855; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000147324-MFHAS1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PGRMC2 | Intact, Biogrid | true |
| HSPD1 | Intact | false |
| KIF3A | Bioplex | false |
| KIFAP3 | Bioplex | false |
| PJA2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

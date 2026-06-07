---
type: protein-evaluation
gene: "CUL5"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CUL5 — REJECTED (研究热度过高 (PubMed strict=193，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CUL5 / VACM1 |
| 蛋白名称 | Cullin-5 |
| 蛋白大小 | 780 aa / 91.0 kDa |
| UniProt ID | Q93034 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Golgi apparatus, Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 780 aa / 91.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=193 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=89.3; PDB: 3DPL, 3DQV, 4JGH, 4N9F, 6V9I, 7ONI, 8EI2 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR045093, IPR059120, IPR016157, IPR016158, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus, Cytosol | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Cul5-RING ubiquitin ligase complex (GO:0031466)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleus (GO:0005634)
- SCF ubiquitin ligase complex (GO:0019005)
- site of DNA damage (GO:0090734)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 193 |
| PubMed broad count | 322 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: VACM1 |

**关键文献**:
1. ASB7 is a negative regulator of H3K9me3 homeostasis.. *Science (New York, N.Y.)*. PMID: 40440427
2. Cullin5 drives experimental asthma exacerbations by modulating alveolar macrophage antiviral immunity.. *Nature communications*. PMID: 38177117
3. PAICS ubiquitination recruits UBAP2 to trigger phase separation for purinosome assembly.. *Molecular cell*. PMID: 37848033
4. CRISPR screens in iPSC-derived neurons reveal principles of tau proteostasis.. *bioRxiv : the preprint server for biology*. PMID: 37398204
5. Cullin-5 deficiency promotes chimeric antigen receptor T cell effector functions potentially via the modulation of JAK/STAT signaling pathway.. *Nature communications*. PMID: 39658572

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.3 |
| 高置信度残基 (pLDDT>90) 占比 | 69.1% |
| 置信残基 (pLDDT 70-90) 占比 | 24.6% |
| 中等置信 (pLDDT 50-70) 占比 | 3.3% |
| 低置信 (pLDDT<50) 占比 | 2.9% |
| 有序区域 (pLDDT>70) 占比 | 93.7% |
| 可用 PDB 条目 | 3DPL, 3DQV, 4JGH, 4N9F, 6V9I, 7ONI, 8EI2, 8FVI, 8FVJ, 9OMA |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3DPL, 3DQV, 4JGH, 4N9F, 6V9I, 7ONI, 8EI2, 8FVI, 8FVJ, 9OMA）+ AlphaFold极高置信度预测（pLDDT=89.3），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045093, IPR059120, IPR016157, IPR016158, IPR036317; Pfam: PF00888, PF26557, PF10557 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CISH | 0.999 | 0.789 | — |
| RBX1 | 0.999 | 0.988 | — |
| ELOC | 0.999 | 0.991 | — |
| CBFB | 0.999 | 0.964 | — |
| ELOB | 0.999 | 0.983 | — |
| NEDD8 | 0.999 | 0.979 | — |
| RNF7 | 0.999 | 0.994 | — |
| SOCS2 | 0.998 | 0.987 | — |
| ARIH2 | 0.997 | 0.977 | — |
| APOBEC3G | 0.984 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SCCRO | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| gus | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20123973|imex:IM-21388 |
| 40031146 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| SOX30 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| PTPN5 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| - | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:15601820|imex:IM-19076 |
| vif | psi-mi:"MI:0096"(pull down) | imex:IM-17346|pubmed:22190034| |
| RBX1 | psi-mi:"MI:0114"(x-ray crystallography) | imex:IM-12127|pubmed:18805092 |
| NEDD8 | psi-mi:"MI:0114"(x-ray crystallography) | imex:IM-12127|pubmed:18805092 |
| UBA3 | psi-mi:"MI:0415"(enzymatic study) | imex:IM-12127|pubmed:18805092 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.3 + PDB: 3DPL, 3DQV, 4JGH, 4N9F, 6V9I,  | pLDDT=89.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Golgi apparatus, Cytosol | 一致 |
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
1. CUL5 — Cullin-5，研究基础较多，新颖性有限。
2. 蛋白大小780 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 193 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 193 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q93034
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166266-CUL5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CUL5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q93034
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (approved)。来源: https://www.proteinatlas.org/ENSG00000166266-CUL5/subcellular

![](https://images.proteinatlas.org/2185/62_H5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/2185/62_H5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/2185/63_H5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/2185/63_H5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/2185/93_H5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/2185/93_H5_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q93034-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q93034 |
| SMART | SM00182;SM00884; |
| UniProt Domain [FT] | DOMAIN 711..772; /note="Cullin neddylation"; /evidence="ECO:0000255" |
| InterPro | IPR045093;IPR059120;IPR016157;IPR016158;IPR036317;IPR001373;IPR019559;IPR016159;IPR036388;IPR036390; |
| Pfam | PF00888;PF26557;PF10557; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000166266-CUL5/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ARIH2 | Intact, Biogrid, Bioplex | true |
| ASB1 | Intact, Biogrid, Bioplex | true |
| ASB6 | Intact, Biogrid, Bioplex | true |
| ASB7 | Intact, Biogrid, Bioplex | true |
| ASB8 | Biogrid, Bioplex | true |
| ASB9 | Biogrid, Bioplex | true |
| CBFB | Intact, Biogrid | true |
| COPS6 | Biogrid, Bioplex | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

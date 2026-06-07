---
type: protein-evaluation
gene: "GARRE1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GARRE1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GARRE1 / KIAA0355 |
| 蛋白名称 | Granule associated Rac and RHOG effector protein 1 |
| 蛋白大小 | 1070 aa / 116.0 kDa |
| UniProt ID | O15063 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; UniProt: Cytoplasm, P-body |
| 蛋白大小 | 8/10 | ×1 | 8 | 1070 aa / 116.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=54.4; PDB: 8BUX, 8BUY |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR031813, IPR043385; Pfam: PF15923 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.5/180** | |
| **归一化总分** | | | **64.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Cytoplasm, P-body | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- P-body (GO:0000932)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 3 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0355 |

**关键文献**:
1. MiniBAR/GARRE1 is a dual Rac and Rab effector required for ciliogenesis.. *Developmental cell*. PMID: 37875118
2. Expression and function of new candidate regulators of placodal neurogenesis in Xenopus laevis.. *Developmental biology*. PMID: 40930482

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 54.4 |
| 高置信度残基 (pLDDT>90) 占比 | 17.1% |
| 置信残基 (pLDDT 70-90) 占比 | 21.1% |
| 中等置信 (pLDDT 50-70) 占比 | 5.5% |
| 低置信 (pLDDT<50) 占比 | 56.3% |
| 有序区域 (pLDDT>70) 占比 | 38.2% |
| 可用 PDB 条目 | 8BUX, 8BUY |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=54.4），有序残基占 38.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR031813, IPR043385; Pfam: PF15923 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NCKAP1 | 0.702 | 0.524 | — |
| RHOG | 0.629 | 0.163 | — |
| RAC3 | 0.587 | 0.161 | — |
| RAC1 | 0.587 | 0.162 | — |
| RAC2 | 0.584 | 0.161 | — |
| ABI2 | 0.579 | 0.328 | — |
| PLEKHG3 | 0.573 | 0.000 | — |
| RESF1 | 0.549 | 0.000 | — |
| CAV1 | 0.533 | 0.225 | — |
| CDC42 | 0.501 | 0.164 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| APOD | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CLU | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CAMKK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MUCL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ABI2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NCKAP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Wdr5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| KRBOX4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| MYH13 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=54.4 + PDB: 8BUX, 8BUY | pLDDT=54.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, P-body / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. GARRE1 — Granule associated Rac and RHOG effector protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1070 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=54.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O15063
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166398-GARRE1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GARRE1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O15063
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000166398-GARRE1/subcellular

![](https://images.proteinatlas.org/14570/118_F11_1_red_green.jpg)
![](https://images.proteinatlas.org/14570/118_F11_2_red_green.jpg)
![](https://images.proteinatlas.org/14570/119_F11_1_red_green.jpg)
![](https://images.proteinatlas.org/14570/119_F11_2_red_green.jpg)
![](https://images.proteinatlas.org/14570/120_F11_1_red_green.jpg)
![](https://images.proteinatlas.org/14570/120_F11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O15063-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O15063 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR031813;IPR043385; |
| Pfam | PF15923; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000166398-GARRE1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| YWHAB | Biogrid, Opencell | true |
| YWHAG | Biogrid, Opencell | true |
| YWHAZ | Biogrid, Opencell | true |
| CAMKK1 | Intact | false |
| STIL | Biogrid | false |
| YWHAH | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

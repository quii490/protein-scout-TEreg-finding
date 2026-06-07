---
type: protein-evaluation
gene: "TTC13"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TTC13 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TTC13 |
| 蛋白名称 | Tetratricopeptide repeat protein 13 |
| 蛋白大小 | 860 aa / 96.8 kDa |
| UniProt ID | Q8NBP0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 860 aa / 96.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=83.4; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011990, IPR019734; Pfam: PF00515, PF13432, PF13 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.0/180** | |
| **归一化总分** | | | **73.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 4 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Quantitative proteomics analysis reveals possible anticancer mechanisms of 5'-deoxy-5'-methylthioadenosine in cholangiocarcinoma cells.. *PloS one*. PMID: 38923999
2. TTC13 expression and STAT3 activation may form a positive feedback loop to promote ccRCC progression.. *PeerJ*. PMID: 37927783
3. Panomics Integration via Machine Learning Prioritizes TAF1D as a Therapeutic Vulnerability in Lung Adenocarcinoma.. *Human mutation*. PMID: 41969615

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.4 |
| 高置信度残基 (pLDDT>90) 占比 | 66.2% |
| 置信残基 (pLDDT 70-90) 占比 | 19.1% |
| 中等置信 (pLDDT 50-70) 占比 | 1.2% |
| 低置信 (pLDDT<50) 占比 | 13.6% |
| 有序区域 (pLDDT>70) 占比 | 85.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=83.4，有序区 85.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011990, IPR019734; Pfam: PF00515, PF13432, PF13181 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| OR4K15 | 0.620 | 0.000 | — |
| TPGS1 | 0.574 | 0.000 | — |
| CDC42EP5 | 0.518 | 0.000 | — |
| FAM122B | 0.496 | 0.000 | — |
| BTBD17 | 0.491 | 0.107 | — |
| LEO1 | 0.475 | 0.398 | — |
| MT-ND4 | 0.472 | 0.398 | — |
| NXPH1 | 0.470 | 0.000 | — |
| RNF217 | 0.461 | 0.000 | — |
| TTC31 | 0.442 | 0.045 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| M2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28169297|imex:IM-25584 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28169297|imex:IM-25584 |
| Hmga2 | psi-mi:"MI:0096"(pull down) | imex:IM-23312|pubmed:26045162 |
| EGLN3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26972000|imex:IM-22750 |
| TCTN1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| BRICD5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| LY86 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| FBXO2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SFTPC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TMEM106A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.4 + PDB: 无 | pLDDT=83.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TTC13 — Tetratricopeptide repeat protein 13，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小860 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NBP0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000143643-TTC13/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TTC13
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NBP0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000143643-TTC13/subcellular

![](https://images.proteinatlas.org/51558/792_G4_1_red_green.jpg)
![](https://images.proteinatlas.org/51558/792_G4_2_red_green.jpg)
![](https://images.proteinatlas.org/51558/795_G4_1_red_green.jpg)
![](https://images.proteinatlas.org/51558/795_G4_2_red_green.jpg)
![](https://images.proteinatlas.org/51558/799_G4_1_red_green.jpg)
![](https://images.proteinatlas.org/51558/799_G4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NBP0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8NBP0 |
| SMART | SM00028; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR011990;IPR019734; |
| Pfam | PF00515;PF13432;PF13181; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000143643-TTC13/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CANX | Opencell | false |
| CCDC47 | Opencell | false |
| TMPRSS2 | Biogrid | false |
| TMPRSS4 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

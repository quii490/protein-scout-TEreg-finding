---
type: protein-evaluation
gene: "CYRIA"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CYRIA 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CYRIA / FAM49A |
| 蛋白名称 | CYFIP-related Rac1 interactor A |
| 蛋白大小 | 323 aa / 37.3 kDa |
| UniProt ID | Q9H0Q0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Nucleoplasm; UniProt: Membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 323 aa / 37.3 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=5 篇 (<=20->10) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=92.8; PDB: 无 |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR039789, IPR009828; Pfam: PF07159 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 11 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Membrane | Swiss-Prot/TremBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 11 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FAM49A |

**关键文献**:
1. A non-syndromic orofacial cleft risk locus links tRNA splicing defects to neural crest cell pathologies.. *American journal of human genetics*. PMID: 40250422
2. Association of selected gene variants with nonsyndromic orofacial clefts in Kuwait.. *Gene*. PMID: 39442823
3. Phenome risk classification enables phenotypic imputation and gene discovery in developmental stuttering.. *American journal of human genetics*. PMID: 34861174
4. Transcription-based identification of uncharacterized genes in the human immune response.. *European journal of human genetics : EJHG*. PMID: 42120540
5. Structural Basis of CYRI-B Direct Competition with Scar/WAVE Complex for Rac1.. *Structure (London, England : 1993)*. PMID: 33217330

**评价**: 极度新颖，几乎未被系统研究（PubMed <=20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.8 |
| 高置信度残基 (pLDDT>90) 占比 | 87.3% |
| 置信残基 (pLDDT 70-90) 占比 | 7.7% |
| 中等置信 (pLDDT 50-70) 占比 | 0.9% |
| 低置信 (pLDDT<50) 占比 | 4.0% |
| 有序区域 (pLDDT>70) 占比 | 95.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=92.8，有序区 95.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039789, IPR009828; Pfam: PF07159 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FAM49B | 0.698 | 0.680 | — |
| LRATD1 | 0.559 | 0.000 | — |
| RHPN2 | 0.539 | 0.000 | — |
| MYCN | 0.506 | 0.000 | — |
| FAM227B | 0.496 | 0.000 | — |
| DDX1 | 0.473 | 0.000 | — |
| SPATS2L | 0.420 | 0.000 | — |
| DCAF4L2 | 0.418 | 0.000 | — |
| PIK3C2G | 0.411 | 0.000 | — |
| PPP1R1A | 0.402 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| 616370" | psi-mi:"MI:0096"(pull down) | pubmed:23606334|imex:IM-21247 |
| CYRIB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GPM6A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| LCOR | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:35914814|imex:IM-27626 |
| MAPT | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:35063084|imex:IM-29773 |
| CDH5 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:39232006|imex:IM-30239 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 11，IntAct interactions: 6
- 调控相关比例: 0 / 11 = 0%

**评价**: STRING 11 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.8 + PDB: 无 | pLDDT=92.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 11 + 6 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ****

**核心优势**:
1. CYRIA -- CYFIP-related Rac1 interactor A，极度新颖，几乎未被系统研究（PubMed <=20篇）。
2. 蛋白大小323 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H0Q0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000197872-CYRIA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CYRIA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H0Q0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000197872-CYRIA/subcellular

![](https://images.proteinatlas.org/60398/1170_C2_2_red_green.jpg)
![](https://images.proteinatlas.org/60398/1170_C2_3_red_green.jpg)
![](https://images.proteinatlas.org/60398/1596_E1_1_red_green.jpg)
![](https://images.proteinatlas.org/60398/1596_E1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H0Q0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H0Q0 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR039789;IPR009828; |
| Pfam | PF07159; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000197872-CYRIA/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CYRIB | Intact, Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

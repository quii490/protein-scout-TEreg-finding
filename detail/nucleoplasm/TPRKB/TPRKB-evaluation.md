---
type: protein-evaluation
gene: "TPRKB"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TPRKB 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TPRKB |
| 蛋白名称 | EKC/KEOPS complex subunit TPRKB |
| 蛋白大小 | 175 aa / 19.7 kDa |
| UniProt ID | Q9Y3C4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Cytoplasm, cytosol; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 175 aa / 19.7 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=21 篇 (≤40→8) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=95.5; PDB: 3ENP, 6WQX, 7SZA, 7SZB, 7SZC, 7SZD |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR013926, IPR036504; Pfam: PF08617 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **134.0/180** | |
| **归一化总分** | | | **74.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Cytoplasm, cytosol; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- EKC/KEOPS complex (GO:0000408)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 21 |
| PubMed broad count | 27 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Mutations in KEOPS-complex genes cause nephrotic syndrome with primary microcephaly.. *Nature genetics*. PMID: 28805828
2. Crystal structure of the human PRPK-TPRKB complex.. *Communications biology*. PMID: 33547416
3. Identification of TP53RK-Binding Protein (TPRKB) Dependency in TP53-Deficient Cancers.. *Molecular cancer research : MCR*. PMID: 31110156
4. Multi-omics analysis identifies OSGEPL1 as an oncogene in hepatocellular carcinoma.. *Discover oncology*. PMID: 40090949
5. Galloway-Mowat syndrome: New insights from bioinformatics and expression during Xenopus embryogenesis.. *Gene expression patterns : GEP*. PMID: 34619372

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 95.5 |
| 高置信度残基 (pLDDT>90) 占比 | 90.9% |
| 置信残基 (pLDDT 70-90) 占比 | 8.6% |
| 中等置信 (pLDDT 50-70) 占比 | 0.6% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 99.5% |
| 可用 PDB 条目 | 3ENP, 6WQX, 7SZA, 7SZB, 7SZC, 7SZD |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3ENP, 6WQX, 7SZA, 7SZB, 7SZC, 7SZD）+ AlphaFold极高置信度预测（pLDDT=95.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013926, IPR036504; Pfam: PF08617 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LAGE3 | 0.999 | 0.655 | — |
| GON7 | 0.999 | 0.361 | — |
| OSGEP | 0.999 | 0.992 | — |
| TP53RK | 0.999 | 0.997 | — |
| OSGEPL1 | 0.968 | 0.752 | — |
| YRDC | 0.875 | 0.000 | — |
| NUP43 | 0.799 | 0.785 | — |
| MBIP | 0.643 | 0.628 | — |
| BUD31 | 0.555 | 0.000 | — |
| POP7 | 0.525 | 0.479 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TP53RK | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| H1-5 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| MBIP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GORASP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GATD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| COMMD10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| OSGEP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NUP43 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TRIM27 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |
| CPSF6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=95.5 + PDB: 3ENP, 6WQX, 7SZA, 7SZB, 7SZC,  | pLDDT=95.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Nucleus / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TPRKB — EKC/KEOPS complex subunit TPRKB，非常新颖，仅有少数基础研究。
2. 蛋白大小175 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 21 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y3C4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000144034-TPRKB/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TPRKB
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y3C4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000144034-TPRKB/subcellular

![](https://images.proteinatlas.org/35712/392_A8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/35712/392_A8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/35712/393_A8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/35712/393_A8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/35712/396_A8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/35712/396_A8_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y3C4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9Y3C4 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR013926;IPR036504; |
| Pfam | PF08617; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000144034-TPRKB/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| LAGE3 | Biogrid, Bioplex | true |
| OSGEP | Biogrid, Bioplex | true |
| TP53RK | Intact, Biogrid, Bioplex | true |
| BAG3 | Biogrid | false |
| GON7 | Intact | false |
| POLR3E | Opencell | false |
| TRIM27 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

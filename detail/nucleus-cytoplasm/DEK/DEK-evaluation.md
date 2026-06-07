---
type: protein-evaluation
gene: "DEK"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DEK — REJECTED (研究热度过高 (PubMed strict=383，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DEK |
| 蛋白名称 | Protein DEK |
| 蛋白大小 | 375 aa / 42.7 kDa |
| UniProt ID | P35659 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 375 aa / 42.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=383 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.6; PDB: 1Q1V, 2JX3, 8KCY, 8KD1, 9L1X, 9L22 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR044198, IPR014876, IPR003034; Pfam: PF08766, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.5/180** | |
| **归一化总分** | | | **49.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- B-WICH complex (GO:0110016)
- contractile muscle fiber (GO:0043292)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 383 |
| PubMed broad count | 844 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Engineered Enucleated Mesenchymal Stem Cells Regulating Immune Microenvironment and Promoting Wound Healing.. *Advanced materials (Deerfield Beach, Fla.)*. PMID: 39295480
2. [Translocated sinonasal tumors].. *Annales de pathologie*. PMID: 38355380
3. DEK-nucleosome structure shows DEK modulates H3K27me3 and stem cell fate.. *Nature structural & molecular biology*. PMID: 40379883
4. XPO1-dependency of DEK::NUP214 leukemia.. *Leukemia*. PMID: 40148556
5. DEK::NUP214 acts as an XPO1-dependent transcriptional activator of essential leukemia genes.. *Leukemia*. PMID: 40204893

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.6 |
| 高置信度残基 (pLDDT>90) 占比 | 5.3% |
| 置信残基 (pLDDT 70-90) 占比 | 38.9% |
| 中等置信 (pLDDT 50-70) 占比 | 25.6% |
| 低置信 (pLDDT<50) 占比 | 30.1% |
| 有序区域 (pLDDT>70) 占比 | 44.2% |
| 可用 PDB 条目 | 1Q1V, 2JX3, 8KCY, 8KD1, 9L1X, 9L22 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=65.6），有序残基占 44.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR044198, IPR014876, IPR003034; Pfam: PF08766, PF02037 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UPF1 | 0.996 | 0.994 | — |
| SRRM1 | 0.978 | 0.292 | — |
| RNPS1 | 0.973 | 0.000 | — |
| BAZ1B | 0.934 | 0.292 | — |
| NUP214 | 0.932 | 0.000 | — |
| MYBBP1A | 0.932 | 0.000 | — |
| SF3B1 | 0.928 | 0.000 | — |
| SMARCA5 | 0.922 | 0.050 | — |
| DDX21 | 0.913 | 0.000 | — |
| U2AF1 | 0.907 | 0.074 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RecQ4 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| Rad23 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG4712 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG15545 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG15141 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Rtnl1 | psi-mi:"MI:0963"(interactome parallel affinity cap | pubmed:21447707|imex:IM-17304 |
| Ugt36F1 | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| Eip63E | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |
| PAPLA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |
| BNIP3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.6 + PDB: 1Q1V, 2JX3, 8KCY, 8KD1, 9L1X,  | pLDDT=65.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
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
1. DEK — Protein DEK，研究基础较多，新颖性有限。
2. 蛋白大小375 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 383 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=65.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 383 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P35659
- Protein Atlas: https://www.proteinatlas.org/ENSG00000124795-DEK/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DEK
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P35659
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000124795-DEK/subcellular

![](https://images.proteinatlas.org/15226/620_H3_1_red_green.jpg)
![](https://images.proteinatlas.org/15226/620_H3_2_red_green.jpg)
![](https://images.proteinatlas.org/15226/623_H3_1_red_green.jpg)
![](https://images.proteinatlas.org/15226/623_H3_2_red_green.jpg)
![](https://images.proteinatlas.org/15226/627_H3_1_red_green.jpg)
![](https://images.proteinatlas.org/15226/627_H3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P35659-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P35659 |
| SMART | SM00513; |
| UniProt Domain [FT] | DOMAIN 149..183; /note="SAP"; DOMAIN 319..375; /note="DEK-C"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01342" |
| InterPro | IPR044198;IPR014876;IPR003034; |
| Pfam | PF08766;PF02037; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000124795-DEK/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CSNK2A1 | Intact, Biogrid, Opencell | true |
| CSNK2A2 | Biogrid, Opencell | true |
| DAXX | Intact, Biogrid | true |
| ACE2 | Biogrid | false |
| BAZ1B | Biogrid | false |
| BMI1 | Biogrid | false |
| BRD2 | Biogrid | false |
| BRD4 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

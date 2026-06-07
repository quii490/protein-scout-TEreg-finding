---
type: protein-evaluation
gene: "NKIRAS2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation, recovery, re-evaluation]
status: scored
---

## NKIRAS2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NKIRAS2 / KBRAS2 |
| 蛋白名称 | NF-kappa-B inhibitor-interacting Ras-like protein 2 |
| 蛋白大小 | 191 aa / 21.5 kDa |
| UniProt ID | Q9NYR9 |
| 数据采集时间 | 2026-06-03 23:46:57 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Nucleoplasm, Nucleoli; UniProt: Cytoplasm |
| 蛋白大小 | 8/10 | x1 | 8 | 191 aa / 21.5 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=22 篇 (21-40 -> 8) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=89.3; PDB: 无 |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR042227, IPR027417, IPR005225, IPR001806; P |
| PPI 网络 | 2/10 | x3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.0/180** | |
| **归一化总分** | | | **61.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 图像状态: if_display_images_available。

**GO Cellular Component**:
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 22 |
| PubMed broad count | 31 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KBRAS2 |

**关键文献**:
1. LDHB inhibition induces mitophagy and facilitates the progression of CSFV infection.. *Autophagy*. PMID: 32924761
2. MIR4726(EccDNA) drives bortezomib resistance in multiple myeloma by enhancing MIR4726-5p/NXF1/NKIRAS2 axis dependent autophagy.. *Cell communication and signaling : CCS*. PMID: 40682103
3. miR-125b controls apoptosis and temozolomide resistance by targeting TNFAIP3 and NKIRAS2 in glioblastomas.. *Cell death & disease*. PMID: 24901050
4. MicroRNA-1908-5p contributes to the oncogenic function of the splicing factor SRSF3.. *Oncotarget*. PMID: 28039456
5. Systems and Computational Screening identifies SRC and NKIRAS2 as Baseline Correlates of Risk (CoR) for Live Attenuated Oral Typhoid Vaccine (TY21a) associated Protection.. *Molecular immunology*. PMID: 38552286

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.3 |
| 高置信度残基 (pLDDT>90) 占比 | 76.4% |
| 置信残基 (pLDDT 70-90) 占比 | 9.9% |
| 中等置信 (pLDDT 50-70) 占比 | 9.9% |
| 低置信 (pLDDT<50) 占比 | 3.7% |
| 有序区域 (pLDDT>70) 占比 | 86.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=89.3，有序区 86.3%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR042227, IPR027417, IPR005225, IPR001806; Pfam: PF00071 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| PAX6 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| CBLN4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RAP1GDS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RALGAPA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GFOD2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DCAF10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RALGAPA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RALGAPB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.3 + PDB: 无 | pLDDT=89.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm, Nucleoli | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ 

**核心优势**:
1. NKIRAS2 -- NF-kappa-B inhibitor-interacting Ras-like protein 2，非常新颖，仅有少数基础研究。
2. 蛋白大小191 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 22 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NYR9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000168256-NKIRAS2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NKIRAS2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NYR9
- STRING: https://string-db.org/network/9606.NKIRAS2
- Packet data timestamp: 2026-06-03 23:46:57

---
*本报告为全量重评估 (Full Re-evaluation) -- Recovery from false-rejection。所有评分基于最新harvest packet数据，使用标准/180评分体系计算。*

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NYR9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NYR9 |
| SMART | SM00175;SM00173; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR042227;IPR027417;IPR005225;IPR001806; |
| Pfam | PF00071; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000168256-NKIRAS2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DNAJC11 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

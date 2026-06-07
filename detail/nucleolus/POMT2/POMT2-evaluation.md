---
type: protein-evaluation
gene: "POMT2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## POMT2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | POMT2 |
| 蛋白名称 | Protein O-mannosyl-transferase 2 |
| 蛋白大小 | 750 aa / 84.2 kDa |
| UniProt ID | Q9UKY4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nucleoli, Cytosol; UniProt: Endoplasmic reticulum membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 750 aa / 84.2 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=90 篇 (≤100→2) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=87.5; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR003342, IPR036300, IPR016093, IPR027005, IPR032 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **98.5/180** | |
| **归一化总分** | | | **54.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli, Cytosol | Approved |
| UniProt | Endoplasmic reticulum membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 90 |
| PubMed broad count | 129 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Genetic variations and clinical spectrum of dystroglycanopathy in a large cohort of Chinese patients.. *Clinical genetics*. PMID: 33200426
2. Walker-Warburg syndrome.. *Orphanet journal of rare diseases*. PMID: 16887026
3. Global View of Domain-Specific O-Linked Mannose Glycosylation in Glycoengineered Cells.. *Molecular & cellular proteomics : MCP*. PMID: 38851451
4. Molecular Diagnosis of Limb-Girdle Muscular Dystrophy Using Next-Generation Sequencing Panels.. *Molecular syndromology*. PMID: 38357257
5. Novel POMT2 variants associated with limb-girdle muscular dystrophy R14: genetic, histological and functional studies.. *Orphanet journal of rare diseases*. PMID: 40102912

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.5 |
| 高置信度残基 (pLDDT>90) 占比 | 66.8% |
| 置信残基 (pLDDT 70-90) 占比 | 24.0% |
| 中等置信 (pLDDT 50-70) 占比 | 2.5% |
| 低置信 (pLDDT<50) 占比 | 6.7% |
| 有序区域 (pLDDT>70) 占比 | 90.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=87.5，有序区 90.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003342, IPR036300, IPR016093, IPR027005, IPR032421; Pfam: PF02815, PF02366, PF16192 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| POMGNT1 | 0.998 | 0.000 | — |
| POMT1 | 0.997 | 0.126 | — |
| DAG1 | 0.992 | 0.088 | — |
| FKRP | 0.987 | 0.072 | — |
| FKTN | 0.986 | 0.000 | — |
| POMGNT2 | 0.986 | 0.000 | — |
| RXYLT1 | 0.862 | 0.000 | — |
| LARGE1 | 0.855 | 0.000 | — |
| GMPPB | 0.854 | 0.139 | — |
| B3GALNT2 | 0.851 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| UPK1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| VWCE | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FDFT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TMED6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ASIC4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PCDHB16 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TCTN2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PON2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CD244 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CHRND | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.5 + PDB: 无 | pLDDT=87.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane / Nucleoplasm; 额外: Nucleoli, Cytosol | 一致 |
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
1. POMT2 — Protein O-mannosyl-transferase 2，研究基础较多，新颖性有限。
2. 蛋白大小750 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 90 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UKY4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000009830-POMT2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=POMT2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UKY4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UKY4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000009830-POMT2/subcellular

![](https://images.proteinatlas.org/3663/17_A6_1_red_green.jpg)
![](https://images.proteinatlas.org/3663/17_A6_2_red_green.jpg)
![](https://images.proteinatlas.org/3663/18_A6_1_red_green.jpg)
![](https://images.proteinatlas.org/3663/18_A6_2_red_green.jpg)
![](https://images.proteinatlas.org/3663/19_A6_1_red_green.jpg)
![](https://images.proteinatlas.org/3663/19_A6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UKY4 |
| SMART | SM00472; |
| UniProt Domain [FT] | DOMAIN 334..390; /note="MIR 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00131"; DOMAIN 403..459; /note="MIR 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00131"; DOMAIN 464..521; /note="MIR 3"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00131" |
| InterPro | IPR003342;IPR036300;IPR016093;IPR027005;IPR032421; |
| Pfam | PF02815;PF02366;PF16192; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000009830-POMT2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CANX | Opencell | false |
| CCDC106 | Bioplex | false |
| POMT1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

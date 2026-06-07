---
type: protein-evaluation
gene: "PRKX"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PRKX 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PRKX / PKX1 |
| 蛋白名称 | cAMP-dependent protein kinase catalytic subunit PRKX |
| 蛋白大小 | 358 aa / 40.9 kDa |
| UniProt ID | P51817 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 358 aa / 40.9 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=61 篇 (≤80→4) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=88.6; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000961, IPR011009, IPR000719, IPR017441, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.5/180** | |
| **归一化总分** | | | **60.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cAMP-dependent protein kinase complex (GO:0005952)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 61 |
| PubMed broad count | 78 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PKX1 |

**关键文献**:
1. PRKX, a Novel cAMP-Dependent Protein Kinase Member, Plays an Important Role in Development.. *Journal of cellular biochemistry*. PMID: 26252946
2. Integrating single-cell transcriptomics, molecular docking, and dynamics simulations to characterize protein kinase X-linked mechanisms in osteosarcoma.. *International journal of biological macromolecules*. PMID: 40907924
3. Abnormal XY interchange between a novel isolated protein kinase gene, PRKY, and its homologue, PRKX, accounts for one third of all (Y+)XX males and (Y-)XY females.. *Human molecular genetics*. PMID: 9302280
4. PRKX, TTBK2 and RSK4 expression causes Sunitinib resistance in kidney carcinoma- and melanoma-cell lines.. *International journal of cancer*. PMID: 22020623
5. Protein kinase X (PRKX) can rescue the effects of polycystic kidney disease-1 gene (PKD1) deficiency.. *Biochimica et biophysica acta*. PMID: 17980165

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.6 |
| 高置信度残基 (pLDDT>90) 占比 | 81.0% |
| 置信残基 (pLDDT 70-90) 占比 | 7.3% |
| 中等置信 (pLDDT 50-70) 占比 | 1.1% |
| 低置信 (pLDDT<50) 占比 | 10.6% |
| 有序区域 (pLDDT>70) 占比 | 88.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=88.6，有序区 88.3%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000961, IPR011009, IPR000719, IPR017441, IPR008271; Pfam: PF00069 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PRKAR2B | 0.977 | 0.648 | — |
| PRKAR1A | 0.940 | 0.702 | — |
| PRKAR1B | 0.885 | 0.418 | — |
| PRKAR2A | 0.860 | 0.418 | — |
| AMELX | 0.847 | 0.000 | — |
| OSTC | 0.841 | 0.000 | — |
| AMELY | 0.819 | 0.000 | — |
| VCX3A | 0.776 | 0.000 | — |
| PCDH11Y | 0.756 | 0.000 | — |
| ARSF | 0.710 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HSP90AB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-17906|pubmed:22939624| |
| PRKAR2B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |
| Prkacb | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| FKBP5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TUBB8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HSP90AB4P | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| RAD54L2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| AIP | psi-mi:"MI:0096"(pull down) | pubmed:32707033|imex:IM-29257| |
| PRH1 | psi-mi:"MI:0096"(pull down) | pubmed:32707033|imex:IM-29257| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.6 + PDB: 无 | pLDDT=88.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm | 一致 |
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
1. PRKX — cAMP-dependent protein kinase catalytic subunit PRKX，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小358 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 61 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P51817
- Protein Atlas: https://www.proteinatlas.org/ENSG00000183943-PRKX/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PRKX
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P51817
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000183943-PRKX/subcellular

![](https://images.proteinatlas.org/15324/2217_C8_14_blue_red_green.jpg)
![](https://images.proteinatlas.org/15324/2217_C8_44_blue_red_green.jpg)
![](https://images.proteinatlas.org/15324/125_A5_1_red_green.jpg)
![](https://images.proteinatlas.org/15324/125_A5_2_red_green.jpg)
![](https://images.proteinatlas.org/15324/126_A5_1_red_green.jpg)
![](https://images.proteinatlas.org/15324/126_A5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P51817-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P51817 |
| SMART | SM00133;SM00220; |
| UniProt Domain [FT] | DOMAIN 49..303; /note="Protein kinase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00159"; DOMAIN 304..358; /note="AGC-kinase C-terminal"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00618" |
| InterPro | IPR000961;IPR011009;IPR000719;IPR017441;IPR008271; |
| Pfam | PF00069; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000183943-PRKX/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ALB | Bioplex | false |
| ALOX12B | Bioplex | false |
| APOD | Bioplex | false |
| AZGP1 | Bioplex | false |
| C3 | Bioplex | false |
| CASP14 | Bioplex | false |
| CTSG | Bioplex | false |
| FKBP5 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

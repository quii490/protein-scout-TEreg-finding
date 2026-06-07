---
type: protein-evaluation
gene: "NXN"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NXN 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NXN / NRX |
| 蛋白名称 | Nucleoredoxin |
| 蛋白大小 | 435 aa / 48.4 kDa |
| UniProt ID | Q6DKJ4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Cytoplasm, cytosol; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 435 aa / 48.4 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=41 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=89.6; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR041861, IPR012336, IPR036249, IPR013766, IPR045 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.5/180** | |
| **归一化总分** | | | **65.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | Cytoplasm, cytosol; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 41 |
| PubMed broad count | 446 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NRX |

**关键文献**:
1. Molecules That Have Rarely Been Studied in Lymphatic Endothelial Cells.. *International journal of molecular sciences*. PMID: 39596293
2. A model of alcoholic liver disease based on different hepatotoxics leading to liver cancer.. *Biochemical pharmacology*. PMID: 38621424
3. NXN Gene Epigenetic Changes in an Adult Neurogenesis Model of Alzheimer's Disease.. *Cells*. PMID: 35406633
4. NXN suppresses metastasis of hepatocellular carcinoma by promoting degradation of Snail through binding to DUB3.. *Cell death & disease*. PMID: 35927236
5. Is Nucleoredoxin a Master Regulator of Cellular Redox Homeostasis? Its Implication in Different Pathologies.. *Antioxidants (Basel, Switzerland)*. PMID: 35453355

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.6 |
| 高置信度残基 (pLDDT>90) 占比 | 66.9% |
| 置信残基 (pLDDT 70-90) 占比 | 26.9% |
| 中等置信 (pLDDT 50-70) 占比 | 2.1% |
| 低置信 (pLDDT<50) 占比 | 4.1% |
| 有序区域 (pLDDT>70) 占比 | 93.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=89.6，有序区 93.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR041861, IPR012336, IPR036249, IPR013766, IPR045870; Pfam: PF13848, PF13905 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DVL1 | 0.966 | 0.615 | — |
| NLGN1 | 0.949 | 0.000 | — |
| EPB41L5 | 0.854 | 0.000 | — |
| TXN | 0.836 | 0.072 | — |
| NRXN1 | 0.836 | 0.000 | — |
| CNTNAP1 | 0.809 | 0.000 | — |
| LRRTM2 | 0.801 | 0.000 | — |
| NRXN2 | 0.787 | 0.000 | — |
| DVL2 | 0.762 | 0.480 | — |
| CRB3 | 0.760 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| 13375783 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| USP3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |
| CDH23 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| WASF1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| NCKAP1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| ABI1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| GORASP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CGB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ARRDC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.6 + PDB: 无 | pLDDT=89.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Nucleus / Cytosol | 一致 |
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
1. NXN — Nucleoredoxin，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小435 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 41 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6DKJ4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000167693-NXN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NXN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6DKJ4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000167693-NXN/subcellular

![](https://images.proteinatlas.org/23566/180_F10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23566/180_F10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/23566/181_F10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23566/181_F10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/23566/182_F10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23566/182_F10_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6DKJ4-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6DKJ4 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 167..321; /note="Thioredoxin"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00691" |
| InterPro | IPR041861;IPR012336;IPR036249;IPR013766;IPR045870; |
| Pfam | PF13848;PF13905; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000167693-NXN/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DVL2 | Biogrid | false |
| DVL3 | Bioplex | false |
| PRKN | Biogrid | false |
| ZBTB24 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

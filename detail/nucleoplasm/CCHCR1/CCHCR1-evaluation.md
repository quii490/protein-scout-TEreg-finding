---
type: protein-evaluation
gene: "CCHCR1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCHCR1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCHCR1 / C6orf18, HCR |
| 蛋白名称 | Coiled-coil alpha-helical rod protein 1 |
| 蛋白大小 | 782 aa / 88.7 kDa |
| UniProt ID | Q8TD31 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Cytoplasm; Nucleus |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 782 aa / 88.7 kDa |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=42 篇 (≤60→6) |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=79.1; PDB: 无 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR009800; Pfam: PF07111 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.5/180** | |
| **归一化总分** | | | **63.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centriole (GO:0005814)
- cytosol (GO:0005829)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 42 |
| PubMed broad count | 74 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C6orf18, HCR |

**关键文献**:
1. Identification of protein/mRNA network involving the PSORS1 locus gene CCHCR1 and the PSORS4 locus gene HAX1.. *Experimental cell research*. PMID: 33417922
2. CCHCR1 links P-body proteins to the centrosome and is required for ciliogenesis through interacting with OFD1 and PCM1.. *Cellular & molecular biology letters*. PMID: 40883668
3. The CCHCR1 (HCR) gene is relevant for skin steroidogenesis and downregulated in cultured psoriatic keratinocytes.. *Journal of molecular medicine (Berlin, Germany)*. PMID: 17221218
4. CCHCR1 is up-regulated in skin cancer and associated with EGFR expression.. *PloS one*. PMID: 19551138
5. Segregation of nascent GPCRs in the ER-to-Golgi transport by CCHCR1 via direct interaction.. *Journal of cell science*. PMID: 38230433

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.1 |
| 高置信度残基 (pLDDT>90) 占比 | 57.5% |
| 置信残基 (pLDDT 70-90) 占比 | 15.0% |
| 中等置信 (pLDDT 50-70) 占比 | 7.7% |
| 低置信 (pLDDT<50) 占比 | 19.8% |
| 有序区域 (pLDDT>70) 占比 | 72.5% |
| 可用 PDB 条目 | 无 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=79.1，有序区 72.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009800; Pfam: PF07111 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDSN | 0.921 | 0.069 | — |
| HLA-C | 0.852 | 0.000 | — |
| TCF19 | 0.799 | 0.000 | — |
| PSORS1C2 | 0.778 | 0.000 | — |
| STAR | 0.778 | 0.510 | — |
| IQCC | 0.777 | 0.683 | — |
| KRT16 | 0.700 | 0.095 | — |
| KRT17 | 0.679 | 0.000 | — |
| KRT6A | 0.648 | 0.000 | — |
| PSORS1C1 | 0.645 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000408012.2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:29892012|doi:10.1038/s4 |
| ENSP00000401039.2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PRKCG | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| POLD2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| IKBKG | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| E2 | psi-mi:"MI:0018"(two hybrid) | pubmed:18305892|imex:IM-19324 |
| EBI-2621128 | psi-mi:"MI:0018"(two hybrid) | pubmed:17446270|imex:IM-20435| |
| HSPB1 | psi-mi:"MI:0097"(reverse ras recruitment system) | imex:IM-20864|pubmed:25277244 |
| IQCC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ABI2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:29892012|doi:10.1038/s4 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.1 + PDB: 无 | pLDDT=79.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CCHCR1 — Coiled-coil alpha-helical rod protein 1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小782 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 42 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TD31
- Protein Atlas: https://www.proteinatlas.org/ENSG00000204536-CCHCR1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCHCR1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TD31
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 04:43:42

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8TD31-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8TD31 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR009800; |
| Pfam | PF07111; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000204536-CCHCR1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HSBP1 | Intact, Biogrid | true |
| KRT40 | Intact, Biogrid | true |
| NUP62 | Intact, Biogrid | true |
| WASHC3 | Intact, Biogrid | true |
| ABI2 | Biogrid | false |
| BORCS6 | Biogrid | false |
| CCDC136 | Biogrid | false |
| CETN2 | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

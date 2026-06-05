---
type: protein-evaluation
gene: "TLK1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TLK1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TLK1 / KIAA0137 |
| 蛋白名称 | Serine/threonine-protein kinase tousled-like 1 |
| 蛋白大小 | 766 aa / 86.7 kDa |
| UniProt ID | Q9UKI8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 766 aa / 86.7 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=55 篇 (≤60→6) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=72.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011009, IPR000719, IPR017441, IPR008271; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.5/180** | |
| **归一化总分** | | | **67.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 55 |
| PubMed broad count | 122 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0137 |

**关键文献**:
1. De novo TLK1 and MDM1 mutations in a patient with a neurodevelopmental disorder and immunodeficiency.. *iScience*. PMID: 38868186
2. Tousled-like kinase 1 promotes gastric cancer progression by regulating the tumor growth factor-beta signaling pathway.. *World journal of gastroenterology*. PMID: 38111505
3. Autophosphorylation of the Tousled-like kinases TLK1 and TLK2 regulates recruitment to damaged chromatin via PCNA interaction.. *Nucleic acids research*. PMID: 39727191
4. The TLK-ASF1 histone chaperone pathway plays a critical role in IL-1β-mediated AML progression.. *Blood*. PMID: 38498025
5. TLK1-mediated MK5-S354 phosphorylation drives prostate cancer cell motility and may signify distinct pathologies.. *Molecular oncology*. PMID: 35064619

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.8 |
| 高置信度残基 (pLDDT>90) 占比 | 50.8% |
| 置信残基 (pLDDT 70-90) 占比 | 12.4% |
| 中等置信 (pLDDT 50-70) 占比 | 2.5% |
| 低置信 (pLDDT<50) 占比 | 34.3% |
| 有序区域 (pLDDT>70) 占比 | 63.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=72.8，有序区 63.2%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011009, IPR000719, IPR017441, IPR008271; Pfam: PF00069 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TLK2 | 0.995 | 0.994 | — |
| ASF1A | 0.981 | 0.878 | — |
| ASF1B | 0.962 | 0.731 | — |
| RAD9A | 0.873 | 0.292 | — |
| SRSF1 | 0.822 | 0.000 | — |
| H3C12 | 0.751 | 0.128 | — |
| H3-3B | 0.729 | 0.000 | — |
| H3C13 | 0.726 | 0.000 | — |
| H3-4 | 0.722 | 0.000 | — |
| H3-2 | 0.722 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000411099.2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ASF1A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ASF1B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| UBE3C | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| A0A0F7RLC1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| YWHAE | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| Dynll1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| uup | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| pykA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| HLF | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.8 + PDB: 无 | pLDDT=72.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
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
1. TLK1 — Serine/threonine-protein kinase tousled-like 1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小766 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 55 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UKI8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198586-TLK1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TLK1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UKI8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/TLK1/IF_images/TLK1_IF_red_green.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000198586-TLK1/subcellular

![](https://images.proteinatlas.org/16043/133_E10_1_red_green.jpg)
![](https://images.proteinatlas.org/16043/133_E10_2_red_green.jpg)
![](https://images.proteinatlas.org/16043/134_E10_1_red_green.jpg)
![](https://images.proteinatlas.org/16043/134_E10_2_red_green.jpg)
![](https://images.proteinatlas.org/16043/135_E10_1_red_green.jpg)
![](https://images.proteinatlas.org/16043/135_E10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UKI8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

---
type: protein-evaluation
gene: "PLCD4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PLCD4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PLCD4 |
| 蛋白名称 | 1-phosphatidylinositol 4,5-bisphosphate phosphodiesterase delta-4 |
| 蛋白大小 | 762 aa / 87.6 kDa |
| UniProt ID | Q9BRC7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Endoplasmic reticulum, Plasma membrane; UniProt: Membrane; Nucleus; Cytoplasm; Endoplasmic reticulum |
| 蛋白大小 | 10/10 | ×1 | 10 | 762 aa / 87.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=18 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=88.9; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000008, IPR035892, IPR011992, IPR018247, IPR002 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.5/180** | |
| **归一化总分** | | | **76.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Endoplasmic reticulum, Plasma membrane | Supported |
| UniProt | Membrane; Nucleus; Cytoplasm; Endoplasmic reticulum | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 34 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Integrative multi-omics analysis reveals the LncRNA 60967.1-PLCD4-ATRA axis as a key regulator of colorectal cancer progression and immune response.. *Molecular cancer*. PMID: 40481569
2. p53-driven lipidome influences non-cell-autonomous lysophospholipids in pancreatic cancer.. *Biology direct*. PMID: 35255936
3. Identification of Multiple Hub Genes in Acute Kidney Injury after Kidney Transplantation by Bioinformatics Analysis.. *Medicina (Kaunas, Lithuania)*. PMID: 35630098
4. Heterotrimeric G protein signaling without GPCRs: The Gα-binding-and-activating (GBA) motif.. *The Journal of biological chemistry*. PMID: 38364891
5. Ezrin silencing remodulates the expression of Phosphoinositide-specific Phospholipase C enzymes in human osteosarcoma cell lines.. *Journal of cell communication and signaling*. PMID: 25073508

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.9 |
| 高置信度残基 (pLDDT>90) 占比 | 70.5% |
| 置信残基 (pLDDT 70-90) 占比 | 20.3% |
| 中等置信 (pLDDT 50-70) 占比 | 2.4% |
| 低置信 (pLDDT<50) 占比 | 6.8% |
| 有序区域 (pLDDT>70) 占比 | 90.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=88.9，有序区 90.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000008, IPR035892, IPR011992, IPR018247, IPR002048; Pfam: PF00168, PF13202, PF09279 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PLCD1 | 0.936 | 0.000 | — |
| ITPR3 | 0.921 | 0.000 | — |
| PRKCB | 0.921 | 0.000 | — |
| ITPR1 | 0.920 | 0.000 | — |
| PRKCA | 0.917 | 0.000 | — |
| IPMK | 0.916 | 0.093 | — |
| INPP5A | 0.914 | 0.000 | — |
| PRKCG | 0.911 | 0.000 | — |
| PLCD3 | 0.910 | 0.000 | — |
| ITPR2 | 0.909 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| IPO11 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TRIM39 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MEOX1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MEOX2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| hspa1a_hspa1b_human-1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MLLT3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| BRPF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MLLT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TCOF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CBX2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.9 + PDB: 无 | pLDDT=88.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane; Nucleus; Cytoplasm; Endoplasmic reticulu / Cytosol; 额外: Endoplasmic reticulum, Plasma membran | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. PLCD4 — 1-phosphatidylinositol 4,5-bisphosphate phosphodiesterase delta-4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小762 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BRC7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000115556-PLCD4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PLCD4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BRC7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000115556-PLCD4/subcellular

![](https://images.proteinatlas.org/38140/1054_E7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/38140/1054_E7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/38140/2265_A9_11_blue_red_green.jpg)
![](https://images.proteinatlas.org/38140/2265_A9_63_blue_red_green.jpg)
![](https://images.proteinatlas.org/38140/847_B8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/38140/847_B8_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BRC7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BRC7 |
| SMART | SM00239;SM00054;SM00233;SM00148;SM00149; |
| UniProt Domain [FT] | DOMAIN 16..124; /note="PH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00145"; DOMAIN 134..169; /note="EF-hand 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00448"; DOMAIN 170..205; /note="EF-hand 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00448"; DOMAIN 206..237; /note="EF-hand 3"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00448"; DOMAIN 290..435; /note="PI-PLC X-box"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00270"; DOMAIN 493..609; /note="PI-PLC Y-box"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00271"; DOMAIN 609..736; /note="C2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00041" |
| InterPro | IPR000008;IPR035892;IPR011992;IPR018247;IPR002048;IPR011993;IPR001849;IPR001192;IPR017946;IPR015359;IPR000909;IPR001711; |
| Pfam | PF00168;PF13202;PF09279;PF00169;PF00388;PF00387; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000115556-PLCD4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| MEOX1 | Intact | false |
| TRIM39 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

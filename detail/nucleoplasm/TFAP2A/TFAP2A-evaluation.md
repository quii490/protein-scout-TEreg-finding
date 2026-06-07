---
type: protein-evaluation
gene: "TFAP2A"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TFAP2A — REJECTED (研究热度过高 (PubMed strict=364，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TFAP2A / AP2TF, TFAP2 |
| 蛋白名称 | Transcription factor AP-2-alpha |
| 蛋白大小 | 437 aa / 48.1 kDa |
| UniProt ID | P05549 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 437 aa / 48.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=364 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.9; PDB: 8J0K, 8J0L, 8J0R |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR004979, IPR008121, IPR013854; Pfam: PF03299 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.5/180** | |
| **归一化总分** | | | **49.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 364 |
| PubMed broad count | 638 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: AP2TF, TFAP2 |

**关键文献**:
1. HINT1 aggravates aortic aneurysm by targeting ITGA6/FAK axis in vascular smooth muscle cells.. *The Journal of clinical investigation*. PMID: 40198125
2. PRMT3 Drives IDO1-Dependent Radioresistance and Immunosuppression by Promoting Kynurenine Metabolism in Non-Small Cell Lung Cancer.. *Cancer research*. PMID: 41129671
3. TFAP2 paralogs regulate midfacial development in part through a conserved ALX genetic pathway.. *Development (Cambridge, England)*. PMID: 38063857
4. TFAP2A enhances tumor stemness and promotes metastasis in pancreatic ductal adenocarcinoma.. *iScience*. PMID: 40727938
5. TFAP2A orchestrates gene regulatory networks and tubular architecture in kidney outer medullary collecting ducts.. *JCI insight*. PMID: 40875514

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.9 |
| 高置信度残基 (pLDDT>90) 占比 | 38.9% |
| 置信残基 (pLDDT 70-90) 占比 | 10.8% |
| 中等置信 (pLDDT 50-70) 占比 | 5.5% |
| 低置信 (pLDDT<50) 占比 | 44.9% |
| 有序区域 (pLDDT>70) 占比 | 49.7% |
| 可用 PDB 条目 | 8J0K, 8J0L, 8J0R |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=67.9），有序残基占 49.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004979, IPR008121, IPR013854; Pfam: PF03299 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CITED2 | 0.989 | 0.482 | — |
| KCTD1 | 0.971 | 0.559 | — |
| TFAP2B | 0.968 | 0.695 | — |
| MYC | 0.938 | 0.292 | — |
| TFAP2C | 0.931 | 0.292 | — |
| TP53 | 0.913 | 0.510 | — |
| CITED4 | 0.905 | 0.295 | — |
| ESR1 | 0.879 | 0.294 | — |
| SP1 | 0.876 | 0.625 | — |
| KCTD15 | 0.863 | 0.559 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GRB2 | psi-mi:"MI:0096"(pull down) | pubmed:12577067|mint:MINT-5216 |
| UBE2I | psi-mi:"MI:0018"(two hybrid) | pubmed:12072434|imex:IM-19634 |
| EP300 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:12586840|imex:IM-19636 |
| CITED2 | psi-mi:"MI:0047"(far western blotting) | pubmed:12586840|imex:IM-19636 |
| ACOT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GSTO2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| INCA1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| RERE | psi-mi:"MI:0018"(two hybrid) | imex:IM-22985|pubmed:24835590 |
| DNAJC19 | psi-mi:"MI:0018"(two hybrid) | imex:IM-22985|pubmed:24835590 |
| KLF10 | psi-mi:"MI:0018"(two hybrid) | imex:IM-22985|pubmed:24835590 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.9 + PDB: 8J0K, 8J0L, 8J0R | pLDDT=67.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
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
1. TFAP2A — Transcription factor AP-2-alpha，研究基础较多，新颖性有限。
2. 蛋白大小437 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 364 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=67.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 364 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P05549
- Protein Atlas: https://www.proteinatlas.org/ENSG00000137203-TFAP2A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TFAP2A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P05549
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000137203-TFAP2A/subcellular

![](https://images.proteinatlas.org/326/943_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/326/943_A3_2_red_green.jpg)
![](https://images.proteinatlas.org/326/948_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/326/948_A3_2_red_green.jpg)
![](https://images.proteinatlas.org/326/951_A3_1_red_green.jpg)
![](https://images.proteinatlas.org/326/951_A3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P05549-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P05549 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR004979;IPR008121;IPR013854; |
| Pfam | PF03299; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000137203-TFAP2A/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| EP300 | Intact, Biogrid | true |
| EWSR1 | Biogrid, Opencell | true |
| NPM1 | Intact, Biogrid | true |
| ACOT1 | Intact | false |
| AP2B1 | Biogrid | false |
| APC | Biogrid | false |
| CITED2 | Biogrid | false |
| CSNK2B | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

---
type: protein-evaluation
gene: "EPM2A"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EPM2A — REJECTED (研究热度过高 (PubMed strict=182，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EPM2A |
| 蛋白名称 | Laforin |
| 蛋白大小 | 331 aa / 37.2 kDa |
| UniProt ID | O95278 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasm; Cytoplasm; Endoplasmic reticulum membrane; Cell m |
| 蛋白大小 | 10/10 | ×1 | 10 | 331 aa / 37.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=182 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=95.6; PDB: 4R30, 4RKK |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR013784, IPR002044, IPR034831, IPR045204, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **92.0/180** | |
| **归一化总分** | | | **51.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Cytoplasm; Cytoplasm; Endoplasmic reticulum membrane; Cell membrane; Cytoplasm; Endoplasmic reticulu... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytoplasmic side of rough endoplasmic reticulum membrane (GO:0098556)
- cytosol (GO:0005829)
- dendrite (GO:0030425)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- perikaryon (GO:0043204)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 182 |
| PubMed broad count | 327 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Gene therapy for Lafora disease in the Epm2a(-/-) mouse model.. *Molecular therapy : the journal of the American Society of Gene Therapy*. PMID: 38796707
2. Lafora Disease.. **. PMID: 29489177
3. Polyglucosan storage myopathies.. *Molecular aspects of medicine*. PMID: 26278982
4. Epm2a(R240X) knock-in mice present earlier cognitive decline and more epileptic activity than Epm2a(-/-) mice.. *Neurobiology of disease*. PMID: 37059210
5. Lafora Disease: A Ubiquitination-Related Pathology.. *Cells*. PMID: 30050012

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 95.6 |
| 高置信度残基 (pLDDT>90) 占比 | 93.1% |
| 置信残基 (pLDDT 70-90) 占比 | 2.7% |
| 中等置信 (pLDDT 50-70) 占比 | 3.0% |
| 低置信 (pLDDT<50) 占比 | 1.2% |
| 有序区域 (pLDDT>70) 占比 | 95.8% |
| 可用 PDB 条目 | 4R30, 4RKK |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4R30, 4RKK）+ AlphaFold高质量预测（pLDDT=95.6），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013784, IPR002044, IPR034831, IPR045204, IPR000340; Pfam: PF00686, PF00782 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NHLRC1 | 0.999 | 0.879 | — |
| PPP1R3C | 0.987 | 0.719 | — |
| GYS1 | 0.965 | 0.324 | — |
| EPM2AIP1 | 0.932 | 0.067 | — |
| NFU1 | 0.916 | 0.292 | — |
| STBD1 | 0.912 | 0.788 | — |
| AGL | 0.876 | 0.000 | — |
| GSK3B | 0.805 | 0.329 | — |
| GYG1 | 0.773 | 0.000 | — |
| PYGB | 0.758 | 0.484 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000356489.3 | psi-mi:"MI:0018"(two hybrid) | pubmed:14532330|imex:IM-20410 |
| Gsk3b | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12037|pubmed:16959610 |
| ENSMUSP00000066050.5 | psi-mi:"MI:0434"(phosphatase assay) | imex:IM-12037|pubmed:16959610 |
| PPP1R3C | psi-mi:"MI:0018"(two hybrid) | pubmed:14532330|imex:IM-20410 |
| GYS1 | psi-mi:"MI:0051"(fluorescence technology) | pubmed:14532330|imex:IM-20410 |
| EBI-2507162 | psi-mi:"MI:0071"(molecular sieving) | pubmed:14532330|imex:IM-20410 |
| STBD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PRKAB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| OTUB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-23897|pubmed:26752685 |
| RPL10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=95.6 + PDB: 4R30, 4RKK | pLDDT=95.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm; Endoplasmic reticulum membra / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. EPM2A — Laforin，研究基础较多，新颖性有限。
2. 蛋白大小331 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 182 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 182 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O95278
- Protein Atlas: https://www.proteinatlas.org/ENSG00000112425-EPM2A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EPM2A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95278
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000112425-EPM2A/subcellular

![](https://images.proteinatlas.org/53643/1189_F3_1_red_green.jpg)
![](https://images.proteinatlas.org/53643/1189_F3_3_red_green.jpg)
![](https://images.proteinatlas.org/53643/1219_F3_1_red_green.jpg)
![](https://images.proteinatlas.org/53643/1219_F3_2_red_green.jpg)
![](https://images.proteinatlas.org/55468/1189_F1_1_red_green.jpg)
![](https://images.proteinatlas.org/55468/1189_F1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O95278-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O95278 |
| SMART | SM01065;SM00195; |
| UniProt Domain [FT] | DOMAIN 1..124; /note="CBM20"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00594"; DOMAIN 156..323; /note="Tyrosine-protein phosphatase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00160" |
| InterPro | IPR013784;IPR002044;IPR034831;IPR045204;IPR000340;IPR013783;IPR042942;IPR029021;IPR016130;IPR000387;IPR020422; |
| Pfam | PF00686;PF00782; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000112425-EPM2A/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| NHLRC1 | Intact, Biogrid, Bioplex | true |
| PPP1R3C | Intact, Biogrid | true |
| BECN1 | Biogrid | false |
| GSK3B | Biogrid | false |
| NFU1 | Biogrid | false |
| PIK3C3 | Biogrid | false |
| PIK3R4 | Biogrid | false |
| PKM | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

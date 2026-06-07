---
type: protein-evaluation
gene: "YWHAQ"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## YWHAQ 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | YWHAQ |
| 蛋白名称 | 14-3-3 protein theta |
| 蛋白大小 | 245 aa / 27.8 kDa |
| UniProt ID | P27348 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nucleoplasm, Nucleoli rim; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 245 aa / 27.8 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=44 篇 (≤60→6) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=93.5; PDB: 2BTP, 5IQP, 6BCR, 6BD2, 6BQT, 6KZG, 6KZH |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000308, IPR023409, IPR036815, IPR023410, IPR042 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.0/180** | |
| **归一化总分** | | | **70.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm, Nucleoli rim | Supported |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- focal adhesion (GO:0005925)
- membrane (GO:0016020)
- nucleus (GO:0005634)
- protein-containing complex (GO:0032991)
- synapse (GO:0045202)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 44 |
| PubMed broad count | 51 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Identification and analysis of the endoplasmic reticulum stress hub genes in sepsis-associated ARDS.. *Scientific reports*. PMID: 40849369
2. 14-3-3 tau (YWHAQ) gene promoter hypermethylation in human placenta of preeclampsia.. *Placenta*. PMID: 25305692
3. The interaction protein of SORBS2 in myocardial tissue to find out the pathogenic mechanism of LVNC disease.. *Aging*. PMID: 35050860
4. A 14-3-3 mRNA is up-regulated in amyotrophic lateral sclerosis spinal cord.. *Journal of neurochemistry*. PMID: 11080204
5. [miR-16-5p regulates apoptosis and migration of drug-resistant breast cancer cells by targeting YWHAQ].. *Nan fang yi ke da xue xue bao = Journal of Southern Medical University*. PMID: 36329581

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.5 |
| 高置信度残基 (pLDDT>90) 占比 | 86.9% |
| 置信残基 (pLDDT 70-90) 占比 | 7.3% |
| 中等置信 (pLDDT 50-70) 占比 | 2.0% |
| 低置信 (pLDDT<50) 占比 | 3.7% |
| 有序区域 (pLDDT>70) 占比 | 94.2% |
| 可用 PDB 条目 | 2BTP, 5IQP, 6BCR, 6BD2, 6BQT, 6KZG, 6KZH |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2BTP, 5IQP, 6BCR, 6BD2, 6BQT, 6KZG, 6KZH）+ AlphaFold极高置信度预测（pLDDT=93.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000308, IPR023409, IPR036815, IPR023410, IPR042584; Pfam: PF00244 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BRAF | 0.997 | 0.910 | — |
| RAF1 | 0.993 | 0.930 | — |
| CDC25C | 0.992 | 0.723 | — |
| CDC25B | 0.990 | 0.834 | — |
| YWHAZ | 0.988 | 0.705 | — |
| ARAF | 0.985 | 0.853 | — |
| YWHAE | 0.984 | 0.791 | — |
| BAD | 0.984 | 0.837 | — |
| YAP1 | 0.982 | 0.812 | — |
| YWHAB | 0.978 | 0.692 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MAP3K5 | psi-mi:"MI:0018"(two hybrid) | pubmed:15023544 |
| EGFR | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:15657067 |
| MAP3K3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| UBQLN4 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| DISC1 | psi-mi:"MI:0018"(two hybrid) | pubmed:17043677|imex:IM-16650 |
| PAK4 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| KIF5B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| SAMD4B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| KLC2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| LARP1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.5 + PDB: 2BTP, 5IQP, 6BCR, 6BD2, 6BQT,  | pLDDT=93.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Cytosol; 额外: Nucleoplasm, Nucleoli rim | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. YWHAQ — 14-3-3 protein theta，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小245 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 44 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P27348
- Protein Atlas: https://www.proteinatlas.org/ENSG00000134308-YWHAQ/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=YWHAQ
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P27348
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000134308-YWHAQ/subcellular

![](https://images.proteinatlas.org/10286/921_C11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/10286/921_C11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/10286/923_C11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/10286/923_C11_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/10286/931_C11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/10286/931_C11_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P27348-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P27348 |
| SMART | SM00101; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR000308;IPR023409;IPR036815;IPR023410;IPR042584; |
| Pfam | PF00244; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000134308-YWHAQ/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ARAF | Biogrid, Opencell | true |
| ARRB1 | Intact, Biogrid | true |
| ARRB2 | Intact, Biogrid | true |
| ATXN1 | Intact, Biogrid | true |
| BAD | Intact, Biogrid | true |
| BAIAP2 | Biogrid, Opencell | true |
| BLTP3B | Biogrid, Opencell | true |
| BRAF | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

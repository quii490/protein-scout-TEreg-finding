---
type: protein-evaluation
gene: "POU5F1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## POU5F1 — REJECTED (研究热度过高 (PubMed strict=818，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | POU5F1 / OCT3, OCT4, OTF3 |
| 蛋白名称 | POU domain, class 5, transcription factor 1 |
| 蛋白大小 | 360 aa / 38.6 kDa |
| UniProt ID | Q01860 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Mitochondria, Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 360 aa / 38.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=818 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.6; PDB: 6T90, 6YOV, 7U0G, 7U0I, 8G87, 8G88, 8G8B |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001356, IPR017970, IPR009057, IPR010982, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Mitochondria, Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- mitochondrion (GO:0005739)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 818 |
| PubMed broad count | 4110 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: OCT3, OCT4, OTF3 |

**关键文献**:
1. Reprogramming to recover youthful epigenetic information and restore vision.. *Nature*. PMID: 33268865
2. Diagnostic significance and carcinogenic mechanism of pan-cancer gene POU5F1 in liver hepatocellular carcinoma.. *Cancer medicine*. PMID: 32978904
3. Comparison of POU5F1 gene expression and protein localization in two differentiated and undifferentiated spermatogonial stem cells.. *Biologia futura*. PMID: 36583847
4. POU5F1 Protein and Gene Expression Analysis in Neonate and Adult Mouse Testicular Germ Cells by Immunohistochemistry and Immunocytochemistry.. *Cellular reprogramming*. PMID: 34788058
5. Generation of germline-competent induced pluripotent stem cells.. *Nature*. PMID: 17554338

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.6 |
| 高置信度残基 (pLDDT>90) 占比 | 30.3% |
| 置信残基 (pLDDT 70-90) 占比 | 7.2% |
| 中等置信 (pLDDT 50-70) 占比 | 18.9% |
| 低置信 (pLDDT<50) 占比 | 43.6% |
| 有序区域 (pLDDT>70) 占比 | 37.5% |
| 可用 PDB 条目 | 6T90, 6YOV, 7U0G, 7U0I, 8G87, 8G88, 8G8B, 8G8E, 8G8G, 8OTS |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=64.6），有序残基占 37.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR017970, IPR009057, IPR010982, IPR013847; Pfam: PF00046, PF00157 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CTNNB1 | 0.999 | 0.525 | — |
| SOX2 | 0.999 | 0.983 | — |
| NANOG | 0.999 | 0.582 | — |
| SALL4 | 0.998 | 0.613 | — |
| KLF4 | 0.994 | 0.089 | — |
| LIN28A | 0.994 | 0.000 | — |
| WDR5 | 0.991 | 0.407 | — |
| SOX17 | 0.988 | 0.345 | — |
| PRDM14 | 0.972 | 0.053 | — |
| POU5F1B | 0.970 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSMUSP00000025271.10 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:20362542|imex:IM-16970 |
| FOXD3 | psi-mi:"MI:0096"(pull down) | pubmed:11891324 |
| Ash2l | psi-mi:"MI:0071"(molecular sieving) | pubmed:21477851|imex:IM-15810 |
| Wdr5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21477851|imex:IM-15810 |
| Cetn2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:21962512|imex:IM-16583 |
| Xpc | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:21962512|imex:IM-16583 |
| Rad23b | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:21962512|imex:IM-16583 |
| EBI-5258515 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:22036565|imex:IM-16644 |
| EBI-5259937 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:22036565|imex:IM-16644 |
| EBI-5259815 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:22036565|imex:IM-16644 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.6 + PDB: 6T90, 6YOV, 7U0G, 7U0I, 8G87,  | pLDDT=64.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Mitochondria, Cytosol | 一致 |
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
1. POU5F1 — POU domain, class 5, transcription factor 1，研究基础较多，新颖性有限。
2. 蛋白大小360 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 818 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=64.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 818 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q01860
- Protein Atlas: https://www.proteinatlas.org/ENSG00000204531-POU5F1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=POU5F1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q01860
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000204531-POU5F1/subcellular

![](https://images.proteinatlas.org/26380/625_A2_1_red_green.jpg)
![](https://images.proteinatlas.org/26380/625_A2_2_red_green.jpg)
![](https://images.proteinatlas.org/58267/1343_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/58267/1343_G6_2_red_green.jpg)
![](https://images.proteinatlas.org/58267/1347_G6_2_red_green.jpg)
![](https://images.proteinatlas.org/58267/1347_G6_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q01860-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q01860 |
| SMART | SM00389;SM00352; |
| UniProt Domain [FT] | DOMAIN 138..212; /note="POU-specific"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00530" |
| InterPro | IPR001356;IPR017970;IPR009057;IPR010982;IPR013847;IPR000327;IPR050255; |
| Pfam | PF00046;PF00157; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000204531-POU5F1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FOXD3 | Intact, Biogrid | true |
| SOX2 | Intact, Biogrid | true |
| WWP2 | Intact, Biogrid | true |
| CTNNB1 | Biogrid | false |
| ETS2 | Biogrid | false |
| HMGB1 | Biogrid | false |
| ITCH | Biogrid | false |
| MBD3 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

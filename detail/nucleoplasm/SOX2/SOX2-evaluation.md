---
type: protein-evaluation
gene: "SOX2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SOX2 — REJECTED (研究热度过高 (PubMed strict=6256，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SOX2 |
| 蛋白名称 | Transcription factor SOX-2 |
| 蛋白大小 | 317 aa / 34.3 kDa |
| UniProt ID | P48431 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus speckle; Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 317 aa / 34.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=6256 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.8; PDB: 1O4X, 2LE4, 6T7B, 6T90, 6WX7, 6WX8, 6WX9 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR009071, IPR036910, IPR022097, IPR050140; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus speckle; Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6256 |
| PubMed broad count | 12743 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. SOX9 suppresses colon cancer via inhibiting epithelial-mesenchymal transition and SOX2 induction.. *The Journal of clinical investigation*. PMID: 40179020
2. Functional maps of a genomic locus reveal confinement of an enhancer by its target gene.. *Science (New York, N.Y.)*. PMID: 40966339
3. Histone Lactylation-Driven Upregulation of VRK1 Expression Promotes Stemness and Proliferation of Glioma Stem Cells.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 40990975
4. CHD7 and SOX2 act in a common gene regulatory network during mammalian semicircular canal and cochlear development.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 38408234
5. DUSP1 and SOX2 expression determine squamous cell carcinoma of the salivary gland progression.. *Scientific reports*. PMID: 38951654

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.8 |
| 高置信度残基 (pLDDT>90) 占比 | 23.3% |
| 置信残基 (pLDDT 70-90) 占比 | 4.1% |
| 中等置信 (pLDDT 50-70) 占比 | 24.3% |
| 低置信 (pLDDT<50) 占比 | 48.3% |
| 有序区域 (pLDDT>70) 占比 | 27.4% |
| 可用 PDB 条目 | 1O4X, 2LE4, 6T7B, 6T90, 6WX7, 6WX8, 6WX9, 6YOV |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=59.8），有序残基占 27.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009071, IPR036910, IPR022097, IPR050140; Pfam: PF00505, PF12336 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| POU5F1 | 0.999 | 0.983 | — |
| NANOG | 0.999 | 0.402 | — |
| KLF4 | 0.998 | 0.095 | — |
| CTNNB1 | 0.991 | 0.627 | — |
| SALL4 | 0.983 | 0.141 | — |
| LIN28A | 0.983 | 0.088 | — |
| PAX6 | 0.977 | 0.309 | — |
| POU2F1 | 0.973 | 0.921 | — |
| HDAC1 | 0.966 | 0.658 | — |
| PRDM14 | 0.965 | 0.094 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-2313612 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:21962512|imex:IM-16583 |
| Rad23b | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:21962512|imex:IM-16583 |
| EBI-5258515 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:22036565|imex:IM-16644 |
| Chd4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21532573|imex:IM-17312 |
| Mta2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21532573|imex:IM-17312 |
| Gatad2b | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21532573|imex:IM-17312 |
| Hdac2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21532573|imex:IM-17312 |
| Hdac1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21532573|imex:IM-17312 |
| Dock7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21532573|imex:IM-17312 |
| Ctbp2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21532573|imex:IM-17312 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.8 + PDB: 1O4X, 2LE4, 6T7B, 6T90, 6WX7,  | pLDDT=59.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus speckle; Cytoplasm; Nucleus / Nucleoplasm | 一致 |
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
1. SOX2 — Transcription factor SOX-2，研究基础较多，新颖性有限。
2. 蛋白大小317 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6256 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=59.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 6256 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P48431
- Protein Atlas: https://www.proteinatlas.org/ENSG00000181449-SOX2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SOX2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P48431
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000181449-SOX2/subcellular

![](https://images.proteinatlas.org/45725/2266_B9_14_red_green.jpg)
![](https://images.proteinatlas.org/45725/2266_B9_34_red_green.jpg)
![](https://images.proteinatlas.org/45725/806_G12_1_red_green.jpg)
![](https://images.proteinatlas.org/45725/806_G12_2_red_green.jpg)
![](https://images.proteinatlas.org/45725/810_G12_1_red_green.jpg)
![](https://images.proteinatlas.org/45725/810_G12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P48431-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P48431 |
| SMART | SM00398; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR009071;IPR036910;IPR022097;IPR050140; |
| Pfam | PF00505;PF12336; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000181449-SOX2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| KDM6A | Intact, Biogrid | true |
| NFIA | Intact, Biogrid | true |
| NFIB | Intact, Biogrid | true |
| NFIC | Intact, Biogrid | true |
| POU5F1 | Intact, Biogrid | true |
| AHCYL1 | Biogrid | false |
| AKT1 | Biogrid | false |
| ANXA1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

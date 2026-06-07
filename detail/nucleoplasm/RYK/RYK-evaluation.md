---
type: protein-evaluation
gene: "RYK"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## RYK — REJECTED (研究热度过高 (PubMed strict=130，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RYK / JTK5A |
| 蛋白名称 | Tyrosine-protein kinase RYK |
| 蛋白大小 | 607 aa / 67.8 kDa |
| UniProt ID | P34925 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Golgi apparatus; 额外: Cytosol; UniProt: Membrane; Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 607 aa / 67.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=130 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=79.7; PDB: 6TUA |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011009, IPR000719, IPR050122, IPR001245, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **87.0/180** | |
| **归一化总分** | | | **48.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Cytosol | Approved |
| UniProt | Membrane; Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- glutamatergic synapse (GO:0098978)
- membrane (GO:0016020)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)
- postsynaptic density membrane (GO:0098839)
- presynaptic active zone membrane (GO:0048787)
- receptor complex (GO:0043235)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 130 |
| PubMed broad count | 495 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: JTK5A |

**关键文献**:
1. RYK is a GPNMB receptor that drives MASH.. *Nature*. PMID: 41708863
2. Vulval development.. *WormBook : the online review of C. elegans biology*. PMID: 18050418
3. The biochemistry, signalling and disease relevance of RYK and other WNT-binding receptor tyrosine kinases.. *Growth factors (Chur, Switzerland)*. PMID: 29806777
4. Revelations of the RYK receptor.. *BioEssays : news and reviews in molecular, cellular and developmental biology*. PMID: 11135307
5. RYK Gene Expression Associated with Drug Response Variation of Temozolomide and Clinical Outcomes in Glioma Patients.. *Pharmaceuticals (Basel, Switzerland)*. PMID: 37242509

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.7 |
| 高置信度残基 (pLDDT>90) 占比 | 58.5% |
| 置信残基 (pLDDT 70-90) 占比 | 16.8% |
| 中等置信 (pLDDT 50-70) 占比 | 3.5% |
| 低置信 (pLDDT<50) 占比 | 21.3% |
| 有序区域 (pLDDT>70) 占比 | 75.3% |
| 可用 PDB 条目 | 6TUA |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=79.7，有序区 75.3%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011009, IPR000719, IPR050122, IPR001245, IPR008266; Pfam: PF07714, PF02019 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| WNT5A | 0.999 | 0.226 | — |
| WNT11 | 0.994 | 0.226 | — |
| WNT5B | 0.982 | 0.226 | — |
| FZD1 | 0.976 | 0.091 | — |
| FZD4 | 0.975 | 0.091 | — |
| WNT3A | 0.968 | 0.226 | — |
| WNT7A | 0.966 | 0.226 | — |
| FZD5 | 0.963 | 0.091 | — |
| FZD2 | 0.963 | 0.091 | — |
| FZD8 | 0.962 | 0.091 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CFTR | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12000|pubmed:17110338 |
| PVR | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SLC39A5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MICA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RAET1E | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NCR3LG1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SIGLECL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CDH5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TNFSF8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MILR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.7 + PDB: 6TUA | pLDDT=79.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Membrane; Nucleus; Cytoplasm / Golgi apparatus; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. RYK — Tyrosine-protein kinase RYK，研究基础较多，新颖性有限。
2. 蛋白大小607 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 130 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 130 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P34925
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163785-RYK/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RYK
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P34925
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/RYK/IF_images/RYK_IF_blue_red_green.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (approved)。来源: https://www.proteinatlas.org/ENSG00000163785-RYK/subcellular

![](https://images.proteinatlas.org/75430/1606_E12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/75430/1606_E12_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/75430/1614_E12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/75430/1614_E12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/75430/1715_H3_13_cr57fd134c6f86e_blue_red_green.jpg)
![](https://images.proteinatlas.org/75430/1715_H3_18_cr57fd1355d3eb4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P34925-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P34925 |
| SMART | SM00469; |
| UniProt Domain [FT] | DOMAIN 66..194; /note="WIF"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00222"; DOMAIN 330..603; /note="Protein kinase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00159" |
| InterPro | IPR011009;IPR000719;IPR050122;IPR001245;IPR008266;IPR003306;IPR038677; |
| Pfam | PF07714;PF02019; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000163785-RYK/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ADGRA2 | Biogrid | false |
| ADGRA3 | Biogrid | false |
| CALM3 | Biogrid | false |
| CD276 | Biogrid | false |
| CDC37 | Biogrid | false |
| CDHR1 | Biogrid | false |
| CELSR1 | Biogrid | false |
| CELSR2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

---
type: protein-evaluation
gene: "BBX"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BBX — REJECTED (研究热度过高 (PubMed strict=200，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BBX / HBP2 |
| 蛋白名称 | HMG box transcription factor BBX |
| 蛋白大小 | 941 aa / 105.1 kDa |
| UniProt ID | Q8WY36 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 941 aa / 105.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=200 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=50.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR049523, IPR052412, IPR009071, IPR036910, IPR019 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **86.0/180** | |
| **归一化总分** | | | **47.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 200 |
| PubMed broad count | 318 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HBP2 |

**关键文献**:
1. COP1 and BBXs-HY5-mediated light signal transduction in plants.. *The New phytologist*. PMID: 31664720
2. SlMPK1- and SlMPK2-mediated SlBBX17 phosphorylation positively regulates CBF-dependent cold tolerance in tomato.. *The New phytologist*. PMID: 37322592
3. The BBX family of plant transcription factors.. *Trends in plant science*. PMID: 24582145
4. Light and ripening-regulated BBX protein-encoding genes in Solanum lycopersicum.. *Scientific reports*. PMID: 33159121
5. Identification of BBX gene family and its function in the regulation of microtuber formation in yam.. *BMC genomics*. PMID: 37365511

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 50.5 |
| 高置信度残基 (pLDDT>90) 占比 | 7.1% |
| 置信残基 (pLDDT 70-90) 占比 | 8.0% |
| 中等置信 (pLDDT 50-70) 占比 | 18.1% |
| 低置信 (pLDDT<50) 占比 | 66.8% |
| 有序区域 (pLDDT>70) 占比 | 15.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=50.5），有序残基占 15.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR049523, IPR052412, IPR009071, IPR036910, IPR019102; Pfam: PF09667, PF00505 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BBOX1 | 0.895 | 0.000 | — |
| TMLHE | 0.651 | 0.000 | — |
| PRH1 | 0.623 | 0.000 | — |
| DHX15 | 0.622 | 0.619 | — |
| CLOCK | 0.622 | 0.000 | — |
| PRH2 | 0.620 | 0.000 | — |
| HDAC1 | 0.551 | 0.239 | — |
| SIN3B | 0.538 | 0.162 | — |
| FOXK1 | 0.497 | 0.000 | — |
| SIN3A | 0.489 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Vha26 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| HPS4 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| cact | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| cv-c | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG15545 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| HDAC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-18733|pubmed:23752268 |
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| ZSCAN31 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| H3C1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=50.5 + PDB: 无 | pLDDT=50.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. BBX — HMG box transcription factor BBX，研究基础较多，新颖性有限。
2. 蛋白大小941 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 200 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=50.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 200 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WY36
- Protein Atlas: https://www.proteinatlas.org/ENSG00000114439-BBX/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BBX
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WY36
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03





<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000114439-BBX/subcellular

![](https://images.proteinatlas.org/50646/757_G10_1_red_green.jpg)
![](https://images.proteinatlas.org/50646/757_G10_3_red_green.jpg)
![](https://images.proteinatlas.org/50646/761_G10_1_red_green.jpg)
![](https://images.proteinatlas.org/50646/761_G10_2_red_green.jpg)
![](https://images.proteinatlas.org/50646/769_G10_1_red_green.jpg)
![](https://images.proteinatlas.org/50646/769_G10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8WY36-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8WY36 |
| SMART | SM00398; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR049523;IPR052412;IPR009071;IPR036910;IPR019102; |
| Pfam | PF09667;PF00505; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000114439-BBX/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HDAC1 | Biogrid, Opencell | true |
| H2BC8 | Biogrid | false |
| MECP2 | Biogrid | false |
| RPA3 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

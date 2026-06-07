---
type: protein-evaluation
gene: "FOXA3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FOXA3 — REJECTED (研究热度过高 (PubMed strict=120，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FOXA3 / HNF3G, TCF3G |
| 蛋白名称 | Hepatocyte nuclear factor 3-gamma |
| 蛋白大小 | 350 aa / 37.1 kDa |
| UniProt ID | P55318 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 350 aa / 37.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=120 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.2; PDB: 1VTN |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR047366, IPR013638, IPR001766, IPR050211, IPR018 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.5/180** | |
| **归一化总分** | | | **44.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629)
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 120 |
| PubMed broad count | 290 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HNF3G, TCF3G |

**关键文献**:
1. FOXA3 induction under endoplasmic reticulum stress contributes to non-alcoholic fatty liver disease.. *Journal of hepatology*. PMID: 33548387
2. scLiverDB: a Database of Human and Mouse Liver Transcriptome Landscapes at Single-Cell Resolution.. *Small methods*. PMID: 37259264
3. Single-Cell Chromatin Accessibility Analysis Reveals the Epigenetic Basis and Signature Transcription Factors for the Molecular Subtypes of Colorectal Cancers.. *Cancer discovery*. PMID: 38445965
4. Different diabetes types and pancreatic ductal adenocarcinoma: a Mendelian randomization and pathway/gene-set analysis.. *Journal of the National Cancer Institute*. PMID: 41206949
5. FOXA3 regulates cholesterol metabolism to compensate for low uptake during the progression of lung adenocarcinoma.. *PLoS biology*. PMID: 38805565

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.2 |
| 高置信度残基 (pLDDT>90) 占比 | 21.1% |
| 置信残基 (pLDDT 70-90) 占比 | 7.1% |
| 中等置信 (pLDDT 50-70) 占比 | 34.3% |
| 低置信 (pLDDT<50) 占比 | 37.4% |
| 有序区域 (pLDDT>70) 占比 | 28.2% |
| 可用 PDB 条目 | 1VTN |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=62.2），有序残基占 28.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR047366, IPR013638, IPR001766, IPR050211, IPR018122; Pfam: PF00250, PF08430 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HNF1A | 0.930 | 0.000 | — |
| FOXA1 | 0.802 | 0.164 | — |
| GATA4 | 0.785 | 0.086 | — |
| TTR | 0.708 | 0.000 | — |
| ALB | 0.693 | 0.183 | — |
| HHEX | 0.684 | 0.000 | — |
| HNF4A | 0.667 | 0.070 | — |
| SPDEF | 0.642 | 0.000 | — |
| AFP | 0.635 | 0.000 | — |
| CEBPA | 0.618 | 0.059 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PPARA | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| CORO1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ST3GAL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KHDRBS2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FGFR3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| CHAT | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| ALX4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| TLE1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| TLE2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 9
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.2 + PDB: 1VTN | pLDDT=62.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 9 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. FOXA3 — Hepatocyte nuclear factor 3-gamma，研究基础较多，新颖性有限。
2. 蛋白大小350 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 120 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=62.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 120 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P55318
- Protein Atlas: https://www.proteinatlas.org/search/FOXA3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FOXA3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P55318
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000170608-FOXA3/subcellular

![](https://images.proteinatlas.org/54034/2265_C8_187_blue_red_green.jpg)
![](https://images.proteinatlas.org/54034/2265_C8_59_blue_red_green.jpg)
![](https://images.proteinatlas.org/54034/1016_D4_1_red_green.jpg)
![](https://images.proteinatlas.org/54034/1016_D4_2_red_green.jpg)
![](https://images.proteinatlas.org/54034/1239_D4_1_red_green.jpg)
![](https://images.proteinatlas.org/54034/1239_D4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P55318-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P55318 |
| SMART | SM00339; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR047366;IPR013638;IPR001766;IPR050211;IPR018122;IPR030456;IPR036388;IPR036390; |
| Pfam | PF00250;PF08430; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000170608-FOXA3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FGFR3 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

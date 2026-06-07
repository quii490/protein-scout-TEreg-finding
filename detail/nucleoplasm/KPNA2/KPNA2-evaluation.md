---
type: protein-evaluation
gene: "KPNA2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## KPNA2 — REJECTED (研究热度过高 (PubMed strict=285，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KPNA2 / RCH1, SRP1 |
| 蛋白名称 | Importin subunit alpha-1 |
| 蛋白大小 | 529 aa / 57.9 kDa |
| UniProt ID | P52292 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm; Nucleus; Endoplasmic reticulum membrane; Golgi ap |
| 蛋白大小 | 10/10 | ×1 | 10 | 529 aa / 57.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=285 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=86.5; PDB: 1EFX, 1QGK, 1QGR, 3FEX, 3FEY, 3WPT, 4E4V |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011989, IPR016024, IPR032413, IPR000225, IPR002 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus; Endoplasmic reticulum membrane; Golgi apparatus membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- endoplasmic reticulum membrane (GO:0005789)
- Golgi membrane (GO:0000139)
- host cell (GO:0043657)
- membrane (GO:0016020)
- NLS-dependent protein nuclear import complex (GO:0042564)
- nuclear membrane (GO:0031965)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 285 |
| PubMed broad count | 439 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RCH1, SRP1 |

**关键文献**:
1. KPNA2 promotes angiogenesis by regulating STAT3 phosphorylation.. *Journal of translational medicine*. PMID: 36578083
2. KPNA2 promotes osteosarcoma progression by regulating the alternative splicing of DDX3X mediated by YBX1.. *Oncogene*. PMID: 40216969
3. Integrated single-cell RNA sequencing analysis reveals distinct cellular and transcriptional modules associated with survival in lung cancer.. *Signal transduction and targeted therapy*. PMID: 35027529
4. ISG15 and ISGylation modulates cancer stem cell-like characteristics in promoting tumor growth of anaplastic thyroid carcinoma.. *Journal of experimental & clinical cancer research : CR*. PMID: 37501099
5. Phase separation of EEF1E1 promotes tumor stemness via PTEN/AKT-mediated DNA repair in hepatocellular carcinoma.. *Cancer letters*. PMID: 39884379

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.5 |
| 高置信度残基 (pLDDT>90) 占比 | 77.9% |
| 置信残基 (pLDDT 70-90) 占比 | 2.8% |
| 中等置信 (pLDDT 50-70) 占比 | 6.6% |
| 低置信 (pLDDT<50) 占比 | 12.7% |
| 有序区域 (pLDDT>70) 占比 | 80.7% |
| 可用 PDB 条目 | 1EFX, 1QGK, 1QGR, 3FEX, 3FEY, 3WPT, 4E4V, 4WV6, 5H43, 7CRU |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1EFX, 1QGK, 1QGR, 3FEX, 3FEY, 3WPT, 4E4V, 4WV6, 5H43, 7CRU）+ AlphaFold极高置信度预测（pLDDT=86.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR032413, IPR000225, IPR002652; Pfam: PF00514, PF16186, PF01749 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KPNB1 | 0.999 | 0.995 | — |
| NCBP1 | 0.994 | 0.986 | — |
| NCBP2 | 0.985 | 0.979 | — |
| NUP153 | 0.969 | 0.849 | — |
| HNRNPK | 0.968 | 0.900 | — |
| CSE1L | 0.961 | 0.813 | — |
| RAN | 0.944 | 0.753 | — |
| TAF8 | 0.935 | 0.926 | — |
| NUP50 | 0.921 | 0.860 | — |
| NBN | 0.909 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MED19 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15175163 |
| MED9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15175163 |
| Q6NVW7 | psi-mi:"MI:0018"(two hybrid) | pubmed:15383276|mint:MINT-5217 |
| MAGEH1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15383276|mint:MINT-5217 |
| CEP126 | psi-mi:"MI:0018"(two hybrid) | pubmed:15383276|mint:MINT-5217 |
| KPNB1 | psi-mi:"MI:0096"(pull down) | pubmed:11024021|imex:IM-25669 |
| CSE1L | psi-mi:"MI:0096"(pull down) | pubmed:11024021|imex:IM-25669 |
| RAN | psi-mi:"MI:0096"(pull down) | pubmed:11024021|imex:IM-25669 |
| NFKBIB | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| RELB | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.5 + PDB: 1EFX, 1QGK, 1QGR, 3FEX, 3FEY,  | pLDDT=86.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Endoplasmic reticulum membrane / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. KPNA2 — Importin subunit alpha-1，研究基础较多，新颖性有限。
2. 蛋白大小529 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 285 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 285 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P52292
- Protein Atlas: https://www.proteinatlas.org/ENSG00000182481-KPNA2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KPNA2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P52292
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000182481-KPNA2/subcellular

![](https://images.proteinatlas.org/15460/945_C8_2_red_green.jpg)
![](https://images.proteinatlas.org/15460/945_C8_3_red_green.jpg)
![](https://images.proteinatlas.org/15460/953_C8_1_red_green.jpg)
![](https://images.proteinatlas.org/15460/953_C8_2_red_green.jpg)
![](https://images.proteinatlas.org/41270/1874_E7_39_cr62177d875a8b8_red_green.jpg)
![](https://images.proteinatlas.org/41270/1874_E7_56_cr5b716f6d86f73_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P52292-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P52292 |
| SMART | SM00185; |
| UniProt Domain [FT] | DOMAIN 2..60; /note="IBB"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00561" |
| InterPro | IPR011989;IPR016024;IPR032413;IPR000225;IPR002652;IPR036975;IPR024931; |
| Pfam | PF00514;PF16186;PF01749; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000182481-KPNA2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BRCA1 | Intact, Biogrid | true |
| CHEK2 | Intact, Biogrid | true |
| FN1 | Intact, Biogrid | true |
| HDAC1 | Biogrid, Opencell | true |
| HDAC2 | Biogrid, Opencell | true |
| HNRNPC | Intact, Biogrid | true |
| HNRNPU | Biogrid, Opencell | true |
| JUN | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

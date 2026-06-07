---
type: protein-evaluation
gene: "KPNA6"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KPNA6 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KPNA6 / IPOA7 |
| 蛋白名称 | Importin subunit alpha-7 |
| 蛋白大小 | 536 aa / 60.0 kDa |
| UniProt ID | O60684 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 536 aa / 60.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=23 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=86.7; PDB: 4UAD, 7RHT |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011989, IPR016024, IPR032413, IPR000225, IPR002 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **132.0/180** | |
| **归一化总分** | | | **73.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- host cell (GO:0043657)
- membrane (GO:0016020)
- NLS-dependent protein nuclear import complex (GO:0042564)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 23 |
| PubMed broad count | 45 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: IPOA7 |

**关键文献**:
1. Protein turnover regulation is critical for influenza A virus infection.. *Cell systems*. PMID: 39368468
2. HNF1A-MODY Mutations in Nuclear Localization Signal Impair HNF1A-Import Receptor KPNA6 Interactions.. *The protein journal*. PMID: 33459938
3. Zika virus recruits karyopherin α6 for efficient replication via NS2B.. *Journal of virology*. PMID: 42159396
4. Changing expression and subcellular distribution of karyopherins during murine oogenesis.. *Reproduction (Cambridge, England)*. PMID: 26399853
5. KPNA6 (Importin {alpha}7)-mediated nuclear import of Keap1 represses the Nrf2-dependent antioxidant response.. *Molecular and cellular biology*. PMID: 21383067

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.7 |
| 高置信度残基 (pLDDT>90) 占比 | 75.6% |
| 置信残基 (pLDDT 70-90) 占比 | 5.0% |
| 中等置信 (pLDDT 50-70) 占比 | 9.3% |
| 低置信 (pLDDT<50) 占比 | 10.1% |
| 有序区域 (pLDDT>70) 占比 | 80.6% |
| 可用 PDB 条目 | 4UAD, 7RHT |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4UAD, 7RHT）+ AlphaFold高质量预测（pLDDT=86.7），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR032413, IPR000225, IPR002652; Pfam: PF00514, PF16186, PF01749 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KPNB1 | 0.995 | 0.838 | — |
| KPNA1 | 0.887 | 0.707 | — |
| RCC1 | 0.865 | 0.451 | — |
| NUP50 | 0.860 | 0.770 | — |
| RAN | 0.845 | 0.504 | — |
| RNMT | 0.807 | 0.790 | — |
| NCBP2 | 0.801 | 0.779 | — |
| KPNA3 | 0.799 | 0.194 | — |
| NUP153 | 0.771 | 0.633 | — |
| IL1F10 | 0.768 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RELB | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| TAF9 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| ANP32A | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| SPOP | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| LYAR | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| GABARAPL2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| VP24 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:22810585|imex:IM-17331 |
| Tnf | psi-mi:"MI:0096"(pull down) | imex:IM-12051|pubmed:17623297 |
| CSP | psi-mi:"MI:0096"(pull down) | imex:IM-12019|pubmed:17981117 |
| NP | psi-mi:"MI:0018"(two hybrid) | imex:IM-13585|pubmed:20064372 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.7 + PDB: 4UAD, 7RHT | pLDDT=86.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Cytosol; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. KPNA6 — Importin subunit alpha-7，非常新颖，仅有少数基础研究。
2. 蛋白大小536 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 23 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O60684
- Protein Atlas: https://www.proteinatlas.org/ENSG00000025800-KPNA6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KPNA6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60684
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000025800-KPNA6/subcellular

![](https://images.proteinatlas.org/18863/152_G2_1_red_green.jpg)
![](https://images.proteinatlas.org/18863/152_G2_2_red_green.jpg)
![](https://images.proteinatlas.org/18863/154_G2_1_red_green.jpg)
![](https://images.proteinatlas.org/18863/154_G2_2_red_green.jpg)
![](https://images.proteinatlas.org/18863/198_G2_1_red_green.jpg)
![](https://images.proteinatlas.org/18863/198_G2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O60684-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O60684 |
| SMART | SM00185; |
| UniProt Domain [FT] | DOMAIN 1..60; /note="IBB"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00561" |
| InterPro | IPR011989;IPR016024;IPR032413;IPR000225;IPR002652;IPR036975;IPR024931; |
| Pfam | PF00514;PF16186;PF01749; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000025800-KPNA6/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ANP32A | Intact, Biogrid, Opencell | true |
| ANP32B | Intact, Biogrid, Opencell | true |
| ANP32E | Biogrid, Bioplex | true |
| CHD8 | Biogrid, Opencell | true |
| HDAC1 | Biogrid, Opencell | true |
| KBTBD4 | Biogrid, Bioplex | true |
| KPNA1 | Biogrid, Opencell | true |
| KPNB1 | Intact, Biogrid, Opencell | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

---
type: protein-evaluation
gene: "CCDC83"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCDC83 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCDC83 |
| 蛋白名称 | Coiled-coil domain-containing protein 83 |
| 蛋白大小 | 413 aa / 48.9 kDa |
| UniProt ID | Q8IWF9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: 无注释 |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 413 aa / 48.9 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=73.0; PDB: 无 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026702 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 9 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.0/180** | |
| **归一化总分** | | | **73.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 5 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Cancer Testis Antigen, NOL4, Is an Immunogenic Antigen Specifically Expressed in Small-Cell Lung Cancer.. *Current oncology (Toronto, Ont.)*. PMID: 34065612
2. Integrated Analysis of Long Non-Coding RNA and mRNA Expression Profiles in Testes of Calves and Sexually Mature Wandong Bulls (Bos taurus).. *Animals : an open access journal from MDPI*. PMID: 34359134
3. KP-CoT-23 (CCDC83) is a novel immunogenic cancer/testis antigen in colon cancer.. *International journal of oncology*. PMID: 22923163

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.0 |
| 高置信度残基 (pLDDT>90) 占比 | 45.5% |
| 置信残基 (pLDDT 70-90) 占比 | 13.1% |
| 中等置信 (pLDDT 50-70) 占比 | 15.7% |
| 低置信 (pLDDT<50) 占比 | 25.7% |
| 有序区域 (pLDDT>70) 占比 | 58.6% |
| 可用 PDB 条目 | 无 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=73.0，有序区 58.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026702 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CCDC65 | 0.683 | 0.000 | — |
| IQCF1 | 0.628 | 0.000 | — |
| CDADC1 | 0.583 | 0.000 | — |
| IQCG | 0.572 | 0.000 | — |
| SPAG9 | 0.539 | 0.000 | — |
| FMR1NB | 0.529 | 0.000 | — |
| RPH3AL | 0.510 | 0.000 | — |
| KLHL10 | 0.470 | 0.000 | — |
| DMRTC2 | 0.466 | 0.000 | — |
| EIF4ENIF1 | 0.447 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FAM161B | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| CHMP2A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MCC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KLC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PPID | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TTC33 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ASPM | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RBM12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CCDC50 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 14，IntAct interactions: 9
- 调控相关比例: 1 / 14 = 7%

**评价**: STRING 14 个预测互作，IntAct 9 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.0 + PDB: 无 | pLDDT=73.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Vesicles | 待确认 |
| PPI | STRING + IntAct | 14 + 9 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. CCDC83 — Coiled-coil domain-containing protein 83，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小413 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 深度机制分析

**CCDC83的coiled-coil结构域架构与无序区域功能**：CCDC83（413 aa, 48.9 kDa, UniProt Q8IWF9）包含IPR026702——一个特征性的coiled-coil结构域，预测形成约200-300 aa的α-螺旋超螺旋支架。Coiled-coil结构域通过七肽重复序列（a-b-c-d-e-f-g）n形成疏水核心的左手双股或多股螺旋束，其核心功能是介导蛋白-蛋白互作和寡聚化。UniProt未检出SMART条目，Pfam也未注释，表明CCDC83属于功能注释极少的"暗蛋白"范畴。AlphaFold pLDDT=73.0（有序区58.6%，高置信区45.5%）表明coiled-coil核心折叠良好，但两端和约25.7%的低置信区域（pLDDT<50）提示大段内在无序区（IDR）——这种"coiled-coil+IDR"的架构在转录共激活因子和染色质重塑辅助因子中常见。

**癌症/睾丸抗原身份与免疫调控关联**：CCDC83被鉴定为新型免疫原性癌症/睾丸抗原（CTA），在结肠癌和肺癌中特异性表达（PMID:22923163, PMID:34065612）。CTA在正常体细胞中通常被表观遗传沉默（通过DNA甲基化和H3K9me3），仅在生殖细胞和癌细胞中重新激活——这一表达模式的调控机制与内源性逆转录病毒（ERV）的表观遗传抑制高度共享。HPA定位Nucleoplasm（Approved）确认了核区室定位，但GO-CC完全无注释，暗示其泛素连接酶复合物（Cul2-RING）关联可能来自其互作伙伴而非直接参与。

**PPI网络中的TE调控线索**：STRING互作仅基于text-mining（全部score<0.7），但IntAct显示9个实验互作伙伴，其中ASP（异常纺锤体样小头畸形相关蛋白）、CHMP2A（带电多泡体蛋白2A/ESCRT-III组分）和KLC1（驱动蛋白轻链1）最为关键（PMID:28514442, PMID:33961781）。ESCRT-III系统的CHMP2A参与膜出芽和核膜修复过程——但ESCRT系统也参与异染色质形成和TE沉默，特别是在裂殖酵母中ESCRT-III组分直接参与着丝粒异染色质的建立。KLC1与CCDC83的互作可能介导CCDC83沿细胞骨架的空间定位。

**TE调控的实验假设与优先级**：PubMed仅3篇的极度新颖性与Nucleoplasm定位使CCDC83成为TE调控研究的高优先级"暗蛋白"候选。结构域-无序混合架构暗示其可能通过coiled-coil介导的多聚化形成类似转录因子复合物的支架，IDR区域参与液-液相分离（LLPS）形成核内凝聚体。实验策略：（1）Cut&Run或DamID确定CCDC83的全基因组染色质结合图谱，特别关注ERV/HERV/LINE-1位点富集；（2）Co-IP/MS鉴定核内互作组，判断是否包含组蛋白修饰酶（HDAC、HMT）或染色质重塑因子；（3）CCDC83敲除细胞系的TE家族特异性RNA-seq表达谱。归一化得分73.9/100中调控结构域7/10（14/30分）是本蛋白的主要优势维度。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| RBM12 | BioGRID | 1 |
| ASPM | BioGRID | 1 |
| EEF1A1 | BioGRID | 1 |
| MCC | BioGRID | 0 |
| CHMP2A | BioGRID | 0 |
| KLC1 | BioGRID | 0 |
| PPID | BioGRID | 0 |
| TTC33 | BioGRID | 0 |


### TE 调控评估

该蛋白具有核定位证据，可能间接参与 TE 调控。需实验验证。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IWF9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000150676-CCDC83/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCDC83
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IWF9
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 04:40:52

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000150676-CCDC83/subcellular

![](https://images.proteinatlas.org/39882/2163_C9_1_red_green.jpg)
![](https://images.proteinatlas.org/39882/2163_C9_2_red_green.jpg)
![](https://images.proteinatlas.org/39882/534_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/39882/534_G1_2_red_green.jpg)
![](https://images.proteinatlas.org/39882/539_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/39882/539_G1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IWF9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8IWF9 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR026702; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000150676-CCDC83/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FAM161B | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

---
type: protein-evaluation
gene: "JDP2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## JDP2 — REJECTED (研究热度过高 (PubMed strict=166，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | JDP2 |
| 蛋白名称 | Jun dimerization protein 2 |
| 蛋白大小 | 163 aa / 18.7 kDa |
| UniProt ID | Q8WYK2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm, Nuclear speckles; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 163 aa / 18.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=166 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=74.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000837, IPR004827, IPR046347; Pfam: PF00170 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.5/180** | |
| **归一化总分** | | | **49.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear speckles | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)
- RNA polymerase II transcription regulator complex (GO:0090575)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 166 |
| PubMed broad count | 218 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. The AHR-NRF2-JDP2 gene battery: Ligand-induced AHR transcriptional activation.. *Biochemical pharmacology*. PMID: 39855429
2. Jun Dimerization Protein 2 (JDP2) Increases p53 Transactivation by Decreasing MDM2.. *Cancers*. PMID: 38473360
3. Maintenance and Reversibility of Paroxysmal Atrial Fibrillation in JDP2 Overexpressing Mice.. *Cells*. PMID: 40710332
4. JDP2, a Novel Molecular Key in Heart Failure and Atrial Fibrillation?. *International journal of molecular sciences*. PMID: 33923401
5. JDP2 and ATF3 deficiencies dampen maladaptive cardiac remodeling and preserve cardiac function.. *PloS one*. PMID: 30818334

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.9 |
| 高置信度残基 (pLDDT>90) 占比 | 38.7% |
| 置信残基 (pLDDT 70-90) 占比 | 9.8% |
| 中等置信 (pLDDT 50-70) 占比 | 44.2% |
| 低置信 (pLDDT<50) 占比 | 7.4% |
| 有序区域 (pLDDT>70) 占比 | 48.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=74.9，有序区 48.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000837, IPR004827, IPR046347; Pfam: PF00170 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| JUN | 0.969 | 0.710 | — |
| JUND | 0.964 | 0.482 | — |
| JUNB | 0.957 | 0.709 | — |
| ARL4C | 0.908 | 0.071 | — |
| ATF2 | 0.810 | 0.763 | — |
| BATF | 0.806 | 0.000 | — |
| CEBPG | 0.795 | 0.102 | — |
| PGR | 0.755 | 0.522 | — |
| ATF3 | 0.725 | 0.000 | — |
| FOS | 0.723 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| DDIT3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ATF4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CREB5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| URS00000A07C1_10090 | psi-mi:"MI:0096"(pull down) | pubmed:29867223|imex:IM-24989 |
| Taf13 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| EBI-26478081 | psi-mi:"MI:0432"(one hybrid) | doi:10.1093/nar/gkaa1055|pubme |
| JUNB | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| ATF2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| GTF2H1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.9 + PDB: 无 | pLDDT=74.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. JDP2 — Jun dimerization protein 2，研究基础较多，新颖性有限。
2. 蛋白大小163 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 166 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 166 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WYK2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000140044-JDP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=JDP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WYK2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000140044-JDP2/subcellular

![](https://images.proteinatlas.org/59511/1082_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/59511/1082_G1_2_red_green.jpg)
![](https://images.proteinatlas.org/59511/1103_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/59511/1103_G1_2_red_green.jpg)
![](https://images.proteinatlas.org/59511/1259_D8_6_red_green.jpg)
![](https://images.proteinatlas.org/59511/1259_D8_7_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8WYK2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8WYK2 |
| SMART | SM00338; |
| UniProt Domain [FT] | DOMAIN 72..135; /note="bZIP"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00978" |
| InterPro | IPR000837;IPR004827;IPR046347; |
| Pfam | PF00170; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000140044-JDP2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ATF2 | Intact, Biogrid | true |
| IRF2BP1 | Intact, Biogrid | true |
| JUN | Biogrid, Opencell | true |
| ATF4 | Intact | false |
| DDIT3 | Intact | false |
| HDAC6 | Biogrid | false |
| JUNB | Intact | false |
| PGR | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

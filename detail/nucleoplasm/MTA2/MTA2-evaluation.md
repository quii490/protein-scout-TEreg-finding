---
type: protein-evaluation
gene: "MTA2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MTA2 — REJECTED (研究热度过高 (PubMed strict=139，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MTA2 / MTA1L1, PID |
| 蛋白名称 | Metastasis-associated protein MTA2 |
| 蛋白大小 | 668 aa / 75.0 kDa |
| UniProt ID | O94776 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 668 aa / 75.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=139 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=75.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001025, IPR043151, IPR000949, IPR009057, IPR040 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **83.5/180** | |
| **归一化总分** | | | **46.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- chromosome, telomeric region (GO:0000781)
- histone deacetylase complex (GO:0000118)
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- NuRD complex (GO:0016581)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 139 |
| PubMed broad count | 205 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MTA1L1, PID |

**关键文献**:
1. Prognostic, Immunological, and Mutational Analysis of MTA2 in Pan-Cancer and Drug Screening for Hepatocellular Carcinoma.. *Biomolecules*. PMID: 37371463
2. Expression of MTA2 gene in ovarian epithelial cancer and its clinical implication.. *Journal of Huazhong University of Science and Technology. Medical sciences = Hua zhong ke ji da xue xue bao. Yi xue Ying De wen ban = Huazhong keji daxue xuebao. Yixue Yingdewen ban*. PMID: 16961294
3. Expression and Significance of MTA2 and CPNE1 in Cervical Squamous Cell Carcinoma.. *Applied immunohistochemistry & molecular morphology : AIMM*. PMID: 37399268
4. HMGB2 Promotes Cardiomyocyte Proliferation and Heart Regeneration Through MTA2-Driven Metabolic Reprogramming.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 41092376
5. MTA2 knockdown suppresses human osteosarcoma metastasis by inhibiting uPA expression.. *Aging*. PMID: 39248711

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.2 |
| 高置信度残基 (pLDDT>90) 占比 | 42.4% |
| 置信残基 (pLDDT 70-90) 占比 | 26.8% |
| 中等置信 (pLDDT 50-70) 占比 | 7.0% |
| 低置信 (pLDDT<50) 占比 | 23.8% |
| 有序区域 (pLDDT>70) 占比 | 69.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=75.2，有序区 69.2%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001025, IPR043151, IPR000949, IPR009057, IPR040138; Pfam: PF01426, PF01448, PF00320 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HDAC2 | 0.999 | 0.941 | — |
| GATAD2A | 0.999 | 0.860 | — |
| HDAC1 | 0.999 | 0.972 | — |
| RBBP7 | 0.999 | 0.953 | — |
| RBBP4 | 0.999 | 0.957 | — |
| CHD3 | 0.999 | 0.874 | — |
| CHD4 | 0.999 | 0.909 | — |
| MTA1 | 0.998 | 0.838 | — |
| GATAD2B | 0.998 | 0.881 | — |
| MBD3 | 0.996 | 0.915 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HDAC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:14645126|imex:IM-19850 |
| RBBP4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:14645126|imex:IM-19850 |
| RBBP7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:14645126|imex:IM-19850 |
| UBE3C | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| TSC22D3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| Sall4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20362541|imex:IM-16928 |
| Esrrb | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20362541|imex:IM-16928 |
| Tfcp2l1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20362541|imex:IM-16928 |
| Sox2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21532573|imex:IM-17312 |
| - | psi-mi:"MI:0096"(pull down) | imex:IM-12128|pubmed:18485871 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.2 + PDB: 无 | pLDDT=75.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
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
1. MTA2 — Metastasis-associated protein MTA2，研究基础较多，新颖性有限。
2. 蛋白大小668 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 139 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 139 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O94776
- Protein Atlas: https://www.proteinatlas.org/ENSG00000149480-MTA2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MTA2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O94776
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000149480-MTA2/subcellular

![](https://images.proteinatlas.org/17522/943_G7_3_red_green.jpg)
![](https://images.proteinatlas.org/17522/943_G7_4_red_green.jpg)
![](https://images.proteinatlas.org/17522/948_G7_1_red_green.jpg)
![](https://images.proteinatlas.org/17522/948_G7_2_red_green.jpg)
![](https://images.proteinatlas.org/17522/951_G7_1_red_green.jpg)
![](https://images.proteinatlas.org/17522/951_G7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O94776-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O94776 |
| SMART | SM00439;SM01189;SM00717;SM00401; |
| UniProt Domain [FT] | DOMAIN 1..144; /note="BAH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00370"; DOMAIN 145..256; /note="ELM2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00512"; DOMAIN 263..315; /note="SANT"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00624" |
| InterPro | IPR001025;IPR043151;IPR000949;IPR009057;IPR040138;IPR035170;IPR001005;IPR017884;IPR000679; |
| Pfam | PF01426;PF01448;PF00320;PF17226;PF00249; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000149480-MTA2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CDK2AP1 | Biogrid, Bioplex | true |
| CSNK2A1 | Biogrid, Opencell | true |
| CSNK2A2 | Biogrid, Opencell | true |
| GATAD2B | Biogrid, Bioplex | true |
| HDAC1 | Intact, Biogrid, Opencell, Bioplex | true |
| HDAC2 | Biogrid, Opencell | true |
| MBD3L1 | Biogrid, Bioplex | true |
| PARK7 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

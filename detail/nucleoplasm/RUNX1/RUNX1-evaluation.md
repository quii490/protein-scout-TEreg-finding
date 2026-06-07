---
type: protein-evaluation
gene: "RUNX1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## RUNX1 — REJECTED (研究热度过高 (PubMed strict=2974，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RUNX1 / AML1, CBFA2 |
| 蛋白名称 | Runt-related transcription factor 1 |
| 蛋白大小 | 453 aa / 48.7 kDa |
| UniProt ID | Q01196 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 453 aa / 48.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=2974 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.0; PDB: 1CMO, 1CO1, 1E50, 1H9D, 1LJM |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000040, IPR008967, IPR012346, IPR013524, IPR027 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.5/180** | |
| **归一化总分** | | | **49.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- core-binding factor complex (GO:0016513)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2974 |
| PubMed broad count | 6283 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: AML1, CBFA2 |

**关键文献**:
1. Erythropoietin regulates energy metabolism through EPO-EpoR-RUNX1 axis.. *Nature communications*. PMID: 39284834
2. Runt-related transcription factor 1 (RUNX1) is a mediator of acute kidney injury.. *The Journal of pathology*. PMID: 39472111
3. RUNX1-PDIA5 Axis Promotes Malignant Progression of Glioblastoma by Regulating CCAR1 Protein Expression.. *International journal of biological sciences*. PMID: 39247813
4. Molecular and pharmacological heterogeneity of ETV6::RUNX1 acute lymphoblastic leukemia.. *Nature communications*. PMID: 39880832
5. CBFβ-SMMHC-driven leukemogenesis requires enhanced RUNX1-DNA binding affinity in mice.. *The Journal of clinical investigation*. PMID: 40763310

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.0 |
| 高置信度残基 (pLDDT>90) 占比 | 25.8% |
| 置信残基 (pLDDT 70-90) 占比 | 7.9% |
| 中等置信 (pLDDT 50-70) 占比 | 11.5% |
| 低置信 (pLDDT<50) 占比 | 54.7% |
| 有序区域 (pLDDT>70) 占比 | 33.7% |
| 可用 PDB 条目 | 1CMO, 1CO1, 1E50, 1H9D, 1LJM |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=61.0），有序残基占 33.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000040, IPR008967, IPR012346, IPR013524, IPR027384; Pfam: PF00853, PF08504 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RUNX1T1 | 0.999 | 0.512 | — |
| ETS1 | 0.999 | 0.928 | — |
| FOXP3 | 0.999 | 0.332 | — |
| CBFB | 0.999 | 0.995 | — |
| HDAC1 | 0.998 | 0.743 | — |
| TAL1 | 0.996 | 0.513 | — |
| GATA2 | 0.996 | 0.125 | — |
| CEBPA | 0.994 | 0.328 | — |
| SPI1 | 0.993 | 0.292 | — |
| EP300 | 0.989 | 0.513 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| gro | psi-mi:"MI:0018"(two hybrid) | pubmed:9751710 |
| TLE1 | psi-mi:"MI:0010"(beta galactosidase complementatio | pubmed:9751710 |
| CBFB | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:2845103|imex:IM-30308 |
| PHLDA3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| IGHM | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:15174051|imex:IM-19123 |
| TRIM33 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-14704|pubmed:20603019 |
| HDAC11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-18733|pubmed:23752268 |
| CDK6 | psi-mi:"MI:0813"(proximity ligation assay) | pubmed:25241761|imex:IM-18707 |
| Cdk9 | psi-mi:"MI:0096"(pull down) | pubmed:20593818|imex:IM-17619 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.0 + PDB: 1CMO, 1CO1, 1E50, 1H9D, 1LJM | pLDDT=61.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Vesicles | 一致 |
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
1. RUNX1 — Runt-related transcription factor 1，研究基础较多，新颖性有限。
2. 蛋白大小453 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2974 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=61.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 2974 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q01196
- Protein Atlas: https://www.proteinatlas.org/ENSG00000159216-RUNX1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RUNX1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q01196
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000159216-RUNX1/subcellular

![](https://images.proteinatlas.org/37912/683_B8_1_red_green.jpg)
![](https://images.proteinatlas.org/37912/683_B8_2_red_green.jpg)
![](https://images.proteinatlas.org/37912/776_H2_2_red_green.jpg)
![](https://images.proteinatlas.org/37912/776_H2_3_red_green.jpg)
![](https://images.proteinatlas.org/37912/899_H2_1_red_green.jpg)
![](https://images.proteinatlas.org/37912/899_H2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q01196-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q01196 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 50..178; /note="Runt"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00399" |
| InterPro | IPR000040;IPR008967;IPR012346;IPR013524;IPR027384;IPR013711;IPR016554; |
| Pfam | PF00853;PF08504; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000159216-RUNX1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CBFB | Intact, Biogrid | true |
| CDK6 | Intact, Biogrid | true |
| HIPK2 | Intact, Biogrid | true |
| AKT1 | Intact | false |
| CBFA2T2 | Biogrid | false |
| CBFA2T3 | Biogrid | false |
| CCNK | Biogrid | false |
| CDK1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

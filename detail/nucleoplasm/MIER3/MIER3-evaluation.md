---
type: protein-evaluation
gene: "MIER3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MIER3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MIER3 |
| 蛋白名称 | Mesoderm induction early response protein 3 |
| 蛋白大小 | 550 aa / 61.4 kDa |
| UniProt ID | Q7Z3K6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 550 aa / 61.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000949, IPR009057, IPR040138, IPR045787, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 9 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.0/180** | |
| **归一化总分** | | | **76.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- protein-containing complex (GO:0032991)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 14 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Preliminary Study on Expression and Function of the Chicken W Chromosome Gene MIER3 in Embryonic Gonads.. *International journal of molecular sciences*. PMID: 37240242
2. [Expression of MIER3 in colorectal cancer and bioinformatic analysis of MIER3- interacting proteins].. *Nan fang yi ke da xue xue bao = Journal of Southern Medical University*. PMID: 28801283
3. Identification and functional analysis of Rattus norvegicus Mammary carcinoma susceptibility 1b (Mcs1b) nominated variants.. *Mammalian genome : official journal of the International Mammalian Genome Society*. PMID: 40973823
4. Rat Mcs1b is concordant to the genome-wide association-identified breast cancer risk locus at human 5q11.2 and MIER3 is a candidate cancer susceptibility gene.. *Cancer research*. PMID: 22993404
5. MIER3 suppresses the progression of non-small cell lung cancer by inhibiting Wnt/β-Catenin pathway and histone acetyltransferase activity.. *Translational cancer research*. PMID: 35117188

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.9 |
| 高置信度残基 (pLDDT>90) 占比 | 16.0% |
| 置信残基 (pLDDT 70-90) 占比 | 13.5% |
| 中等置信 (pLDDT 50-70) 占比 | 19.1% |
| 低置信 (pLDDT<50) 占比 | 51.5% |
| 有序区域 (pLDDT>70) 占比 | 29.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=57.9），有序残基占 29.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000949, IPR009057, IPR040138, IPR045787, IPR001005; Pfam: PF01448, PF19426, PF00249 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HDAC2 | 0.832 | 0.689 | — |
| HDAC1 | 0.802 | 0.625 | — |
| BAHD1 | 0.796 | 0.610 | — |
| C16orf87 | 0.790 | 0.785 | — |
| H2AZ1 | 0.634 | 0.623 | — |
| SETD9 | 0.617 | 0.000 | — |
| H2BC1 | 0.605 | 0.605 | — |
| MIER1 | 0.449 | 0.000 | — |
| DYTN | 0.441 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HDAC2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:21258344|imex:IM-17039 |
| HDAC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-18733|pubmed:23752268 |
| STK16 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MCRS1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| H2AX | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| H2BC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| C16orf87 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| WIZ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| BAHD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MICAL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 9，IntAct interactions: 15
- 调控相关比例: 0 / 9 = 0%

**评价**: STRING 9 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.9 + PDB: 无 | pLDDT=57.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 9 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. MIER3 — Mesoderm induction early response protein 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小550 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=57.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z3K6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000155545-MIER3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MIER3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7Z3K6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000155545-MIER3/subcellular

![](https://images.proteinatlas.org/58349/1242_G7_1_red_green.jpg)
![](https://images.proteinatlas.org/58349/1242_G7_3_red_green.jpg)
![](https://images.proteinatlas.org/58349/983_C7_1_red_green.jpg)
![](https://images.proteinatlas.org/58349/983_C7_2_red_green.jpg)
![](https://images.proteinatlas.org/58349/991_C7_1_red_green.jpg)
![](https://images.proteinatlas.org/58349/991_C7_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7Z3K6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q7Z3K6 |
| SMART | SM01189;SM00717; |
| UniProt Domain [FT] | DOMAIN 174..272; /note="ELM2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00512"; DOMAIN 277..329; /note="SANT"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00624" |
| InterPro | IPR000949;IPR009057;IPR040138;IPR045787;IPR001005;IPR017884; |
| Pfam | PF01448;PF19426;PF00249; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000155545-MIER3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HDAC1 | Biogrid, Opencell | true |
| HDAC2 | Biogrid, Opencell | true |
| H2AZ1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

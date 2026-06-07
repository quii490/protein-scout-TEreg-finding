---
type: protein-evaluation
gene: "PCNP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PCNP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PCNP |
| 蛋白名称 | PEST proteolytic signal-containing nuclear protein |
| 蛋白大小 | 178 aa / 18.9 kDa |
| UniProt ID | Q8WW12 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Nuclear bodies; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 178 aa / 18.9 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=31 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029169; Pfam: PF15473 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.0/180** | |
| **归一化总分** | | | **70.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear bodies | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 31 |
| PubMed broad count | 111 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Taking a holistic view of PEST-containing nuclear protein (PCNP) in cancer biology.. *Cancer medicine*. PMID: 31487123
2. PCNP is a novel regulator of proliferation, migration, and invasion in human thyroid cancer.. *International journal of biological sciences*. PMID: 35813472
3. Biology of PEST-Containing Nuclear Protein: A Potential Molecular Target for Cancer Research.. *Frontiers in oncology*. PMID: 35186732
4. TIPE2 and PCNP expression abnormalities in peripheral blood mononuclear cells associated with disease activity in rheumatoid arthritis: a meta-analysis.. *European review for medical and pharmacological sciences*. PMID: 33629294
5. PEST-containing nuclear protein in eye health and disease: A review.. *Experimental eye research*. PMID: 40414338

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.8 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 25.8% |
| 中等置信 (pLDDT 50-70) 占比 | 60.1% |
| 低置信 (pLDDT<50) 占比 | 14.0% |
| 有序区域 (pLDDT>70) 占比 | 25.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=62.8），有序残基占 25.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029169; Pfam: PF15473 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UHRF2 | 0.898 | 0.625 | — |
| OSTN | 0.610 | 0.610 | — |
| PTGES3 | 0.557 | 0.000 | — |
| HYPK | 0.531 | 0.000 | — |
| ZRANB2 | 0.519 | 0.000 | — |
| NAA50 | 0.513 | 0.000 | — |
| POLI | 0.504 | 0.000 | — |
| SF3B6 | 0.496 | 0.431 | — |
| FAM107B | 0.490 | 0.484 | — |
| DNPH1 | 0.488 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CAND1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |
| HNRNPDL | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| SF1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:26420826|imex:IM-23671 |
| Kifc5b | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| MYO1C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Mis12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| USP11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| EMC2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.8 + PDB: 无 | pLDDT=62.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. PCNP — PEST proteolytic signal-containing nuclear protein，非常新颖，仅有少数基础研究。
2. 蛋白大小178 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 31 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=62.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WW12
- Protein Atlas: https://www.proteinatlas.org/ENSG00000081154-PCNP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PCNP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WW12
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000081154-PCNP/subcellular

![](https://images.proteinatlas.org/35011/370_D12_1_red_green.jpg)
![](https://images.proteinatlas.org/35011/370_D12_2_red_green.jpg)
![](https://images.proteinatlas.org/35011/373_D12_1_red_green.jpg)
![](https://images.proteinatlas.org/35011/373_D12_2_red_green.jpg)
![](https://images.proteinatlas.org/35011/860_B5_1_red_green.jpg)
![](https://images.proteinatlas.org/35011/860_B5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8WW12-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8WW12 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029169; |
| Pfam | PF15473; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000081154-PCNP/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BPNT1 | Opencell | false |
| KLK6 | Intact | false |
| MYC | Biogrid | false |
| RBM17 | Opencell | false |
| RBM39 | Opencell | false |
| SF3A1 | Opencell | false |
| SF3A2 | Opencell | false |
| SF3B1 | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

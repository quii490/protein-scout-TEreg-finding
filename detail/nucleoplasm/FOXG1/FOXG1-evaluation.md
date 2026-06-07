---
type: protein-evaluation
gene: "FOXG1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FOXG1 — REJECTED (研究热度过高 (PubMed strict=385，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FOXG1 / FKH2, FKHL1, FKHL2, FKHL3, FKHL4 |
| 蛋白名称 | Forkhead box protein G1 |
| 蛋白大小 | 489 aa / 52.4 kDa |
| UniProt ID | P55316 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 489 aa / 52.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=385 篇 (>100→REJECTED) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v6 pLDDT=0; PDB: 7CBY |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001766, IPR047208, IPR018122, IPR030456, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 11 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **78.0/180** | |
| **归一化总分** | | | **43.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 385 |
| PubMed broad count | 714 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FKH2, FKHL1, FKHL2, FKHL3, FKHL4, FOXG1A |

**关键文献**:
1. Massively parallel in vivo Perturb-seq reveals cell-type-specific transcriptional networks in cortical development.. *Cell*. PMID: 38772369
2. FOXG1-Dependent Dysregulation of GABA/Glutamate Neuron Differentiation in Autism Spectrum Disorders.. *Cell*. PMID: 26186191
3. Diagnostic outcomes for genetic testing of 70 genes in 8565 patients with epilepsy and neurodevelopmental disorders.. *Epilepsia*. PMID: 29655203
4. De novo mutations in moderate or severe intellectual disability.. *PLoS genetics*. PMID: 25356899
5. FOXG1 Syndrome.. **. PMID: 38843374

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 7CBY |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001766, IPR047208, IPR018122, IPR030456, IPR036388; Pfam: PF00250 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SRF | 0.991 | 0.377 | — |
| MECP2 | 0.947 | 0.095 | — |
| TLE1 | 0.903 | 0.758 | — |
| KDM5B | 0.884 | 0.512 | — |
| CDKL5 | 0.866 | 0.000 | — |
| PAX6 | 0.865 | 0.084 | — |
| TBR1 | 0.836 | 0.045 | — |
| SMAD3 | 0.816 | 0.071 | — |
| EMX1 | 0.802 | 0.046 | — |
| OTX2 | 0.781 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EEF1G | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| GDF9 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| RBM33 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| PROZ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FOXO3 | psi-mi:"MI:0096"(pull down) | pubmed:15084259|imex:IM-24476 |
| Zbtb17 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | imex:IM-25039|pubmed:26766587 |
| FOXO4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15084259|imex:IM-24476 |
| Foxo1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15084259|imex:IM-24476 |
| THSD4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Tsc1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 11
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 11 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 7CBY | pLDDT=0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 11 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. FOXG1 — Forkhead box protein G1，研究基础较多，新颖性有限。
2. 蛋白大小489 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 385 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 385 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P55316
- Protein Atlas: https://www.proteinatlas.org/ENSG00000176165-FOXG1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FOXG1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P55316
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P55316-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P55316 |
| SMART | SM00339; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001766;IPR047208;IPR018122;IPR030456;IPR036388;IPR036390; |
| Pfam | PF00250; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000176165-FOXG1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AR | Biogrid | false |
| FOXH1 | Biogrid | false |
| KDM5B | Biogrid | false |
| LNPK | Opencell | false |
| TLE1 | Biogrid | false |
| TLE6 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

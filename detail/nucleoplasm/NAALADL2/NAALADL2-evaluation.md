---
type: protein-evaluation
gene: "NAALADL2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NAALADL2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NAALADL2 |
| 蛋白名称 | Inactive N-acetylated-alpha-linked acidic dipeptidase-like protein 2 |
| 蛋白大小 | 795 aa / 88.7 kDa |
| UniProt ID | Q58DX5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 795 aa / 88.7 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=78.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR046450, IPR007484, IPR039373, IPR036757; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 14 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 32 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Genetic alterations in the 3q26.31-32 locus confer an aggressive prostate cancer phenotype.. *Communications biology*. PMID: 32796921
2. Identification of genetic susceptibility loci for intestinal Behçet's disease.. *Scientific reports*. PMID: 28045058
3. Optical genome mapping unveils hidden structural variants in neurodevelopmental disorders.. *Scientific reports*. PMID: 38755281
4. N-acetyl-L-aspartyl-L-glutamate peptidase-like 2 is overexpressed in cancer and promotes a pro-migratory and pro-metastatic phenotype.. *Oncogene*. PMID: 24240687
5. Balanced Translocation t(3;12) Disrupting HMGA2 and NAALADL2 Genes in Twins With Silver-Russell Syndrome and Intellectual Disability.. *Clinical genetics*. PMID: 39846526

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.7 |
| 高置信度残基 (pLDDT>90) 占比 | 50.9% |
| 置信残基 (pLDDT 70-90) 占比 | 22.1% |
| 中等置信 (pLDDT 50-70) 占比 | 10.8% |
| 低置信 (pLDDT<50) 占比 | 16.1% |
| 有序区域 (pLDDT>70) 占比 | 73.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=78.7，有序区 73.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR046450, IPR007484, IPR039373, IPR036757; Pfam: PF04389 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NIPBL | 0.726 | 0.000 | — |
| NAALAD2 | 0.649 | 0.601 | — |
| SMC1A | 0.649 | 0.000 | — |
| PAPPA | 0.588 | 0.000 | — |
| SMC3 | 0.587 | 0.000 | — |
| CDH13 | 0.568 | 0.000 | — |
| LNX1 | 0.568 | 0.000 | — |
| TCP1 | 0.541 | 0.000 | — |
| ZFHX3 | 0.528 | 0.000 | — |
| TAFA2 | 0.525 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| LAPTM4B | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| IGSF3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ERBB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KCNJ8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KLC2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CELSR2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NAALAD2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GPR25 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |
| GRM2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 14
- 调控相关比例: 2 / 15 = 13%

**评价**: STRING 15 个预测互作，IntAct 14 个实验互作。调控相关配体占比 13%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.7 + PDB: 无 | pLDDT=78.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 14 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. NAALADL2 — Inactive N-acetylated-alpha-linked acidic dipeptidase-like protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小795 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q58DX5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000177694-NAALADL2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NAALADL2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q58DX5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000177694-NAALADL2/subcellular

![](https://images.proteinatlas.org/12413/1658_G2_1_red_green.jpg)
![](https://images.proteinatlas.org/12413/1658_G2_2_red_green.jpg)
![](https://images.proteinatlas.org/12413/1682_C11_2_red_green.jpg)
![](https://images.proteinatlas.org/12413/1682_C11_3_red_green.jpg)
![](https://images.proteinatlas.org/12413/1774_A8_24_cr5950f7703119e_red_green.jpg)
![](https://images.proteinatlas.org/12413/1774_A8_3_cr5950f77030918_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q58DX5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

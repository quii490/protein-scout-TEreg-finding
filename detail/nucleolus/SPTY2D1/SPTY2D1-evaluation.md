---
type: protein-evaluation
gene: "SPTY2D1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SPTY2D1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SPTY2D1 |
| 蛋白名称 | Protein SPT2 homolog |
| 蛋白大小 | 685 aa / 75.6 kDa |
| UniProt ID | Q68D10 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm, Nucleoli; UniProt: Nucleus, nucleolus |
| 蛋白大小 | 10/10 | ×1 | 10 | 685 aa / 75.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.9; PDB: 5BS7, 5BSA |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR013256, IPR054552; Pfam: PF08243, PF22878 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.5/180** | |
| **归一化总分** | | | **76.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli | Enhanced |
| UniProt | Nucleus, nucleolus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 11 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Association of protein function-altering variants with cardiometabolic traits: the strong heart study.. *Scientific reports*. PMID: 35665752
2. Sex-specific association of the SPTY2D1 rs7934205 polymorphism and serum lipid levels.. *International journal of clinical and experimental pathology*. PMID: 25755761
3. Large-scale gene-centric meta-analysis across 32 studies identifies multiple lipid loci.. *American journal of human genetics*. PMID: 23063622
4. Association of the SPT2 chromatin protein domain containing 1 gene rs17579600 polymorphism and serum lipid traits.. *International journal of clinical and experimental pathology*. PMID: 26722495
5. Identification of an interactome network between lncRNAs and miRNAs in thyroid cancer reveals SPTY2D1-AS1 as a new tumor suppressor.. *Scientific reports*. PMID: 35562181

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.9 |
| 高置信度残基 (pLDDT>90) 占比 | 5.7% |
| 置信残基 (pLDDT 70-90) 占比 | 19.0% |
| 中等置信 (pLDDT 50-70) 占比 | 19.1% |
| 低置信 (pLDDT<50) 占比 | 56.2% |
| 有序区域 (pLDDT>70) 占比 | 24.7% |
| 可用 PDB 条目 | 5BS7, 5BSA |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=55.9），有序残基占 24.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013256, IPR054552; Pfam: PF08243, PF22878 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| H4C6 | 0.935 | 0.932 | — |
| H4C12 | 0.914 | 0.913 | — |
| H4C9 | 0.913 | 0.912 | — |
| H3C13 | 0.911 | 0.905 | — |
| H3C15 | 0.909 | 0.905 | — |
| H3C14 | 0.909 | 0.905 | — |
| H4C8 | 0.905 | 0.903 | — |
| H4C5 | 0.904 | 0.903 | — |
| H4C11 | 0.904 | 0.903 | — |
| H4C2 | 0.904 | 0.903 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MKI67 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26949251|imex:IM-26415 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| RRP8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RPL18 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PLEKHO1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KBTBD7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MAGEB10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RPS14 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NIFK | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SART3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.9 + PDB: 5BS7, 5BSA | pLDDT=55.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleolus / Nucleoplasm, Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SPTY2D1 — Protein SPT2 homolog，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小685 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=55.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q68D10
- Protein Atlas: https://www.proteinatlas.org/ENSG00000179119-SPTY2D1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SPTY2D1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q68D10
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000179119-SPTY2D1/subcellular

![](https://images.proteinatlas.org/40177/1807_E9_31_red_green.jpg)
![](https://images.proteinatlas.org/40177/1807_E9_32_red_green.jpg)
![](https://images.proteinatlas.org/40177/1891_I12_25_cr5bbde013a97c1_red_green.jpg)
![](https://images.proteinatlas.org/40177/1891_I12_9_cr5bbde013a94a2_red_green.jpg)
![](https://images.proteinatlas.org/40177/1901_I19_2_red_green.jpg)
![](https://images.proteinatlas.org/40177/1901_I19_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q68D10-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q68D10 |
| SMART | SM00784; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR013256;IPR054552; |
| Pfam | PF08243;PF22878; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000179119-SPTY2D1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| MYC | Biogrid | false |
| NIFK | Biogrid | false |
| SSRP1 | Opencell | false |
| TOP1 | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

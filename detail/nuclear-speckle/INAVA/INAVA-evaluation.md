---
type: protein-evaluation
gene: "INAVA"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## INAVA 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | INAVA / C1orf106 |
| 蛋白名称 | Innate immunity activator protein |
| 蛋白大小 | 663 aa / 72.9 kDa |
| UniProt ID | Q3KP66 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nuclear bodies; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 663 aa / 72.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=17 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR043447, IPR021774; Pfam: PF11819 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear bodies | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17 |
| PubMed broad count | 26 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C1orf106 |

**关键文献**:
1. Role of the Gut-Brain Axis in the Shared Genetic Etiology Between Gastrointestinal Tract Diseases and Psychiatric Disorders: A Genome-Wide Pleiotropic Analysis.. *JAMA psychiatry*. PMID: 36753304
2. An international genome-wide meta-analysis of primary biliary cholangitis: Novel risk loci and candidate drugs.. *Journal of hepatology*. PMID: 34033851
3. The INAVA mRNA in Extracellular Vesicles Activates Normal Ovarian Fibroblasts by Phosphorylation-Ubiquitylation Crosstalk of HMGA2.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 40265981
4. Small-molecule modulators of INAVA cytosolic condensate and cell-cell junction assemblies.. *The Journal of cell biology*. PMID: 34251416
5. Genetic overlap between inflammatory bowel disease and iridocyclitis: insights from a genome-wide association study in a European population.. *BMC genomic data*. PMID: 39472800

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.2 |
| 高置信度残基 (pLDDT>90) 占比 | 11.9% |
| 置信残基 (pLDDT 70-90) 占比 | 10.1% |
| 中等置信 (pLDDT 50-70) 占比 | 24.4% |
| 低置信 (pLDDT<50) 占比 | 53.5% |
| 有序区域 (pLDDT>70) 占比 | 22.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=56.2），有序残基占 22.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR043447, IPR021774; Pfam: PF11819 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CYTH2 | 0.847 | 0.776 | — |
| CYTH1 | 0.827 | 0.726 | — |
| CYTH3 | 0.747 | 0.644 | — |
| DCTN1 | 0.595 | 0.595 | — |
| TRIM27 | 0.559 | 0.231 | — |
| CEP170 | 0.525 | 0.480 | — |
| DCTN5 | 0.454 | 0.454 | — |
| ACTR1A | 0.451 | 0.430 | — |
| DCTN2 | 0.446 | 0.422 | — |
| SGF29 | 0.444 | 0.444 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CYTH1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DCTN6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TAX1BP3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CYTH3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CRTAP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DCTN3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TRIM27 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SMARCA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GRN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ACTR1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.2 + PDB: 无 | pLDDT=56.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm; 额外: Nuclear bodies | 一致 |
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
1. INAVA — Innate immunity activator protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小663 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 17 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=56.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q3KP66
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163362-INAVA/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=INAVA
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q3KP66
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000163362-INAVA/subcellular

![](https://images.proteinatlas.org/79622/2030_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/79622/2030_E5_2_red_green.jpg)
![](https://images.proteinatlas.org/79622/2042_E2_1_red_green.jpg)
![](https://images.proteinatlas.org/79622/2042_E2_2_red_green.jpg)
![](https://images.proteinatlas.org/79622/2047_C4_2_red_green.jpg)
![](https://images.proteinatlas.org/79622/2047_C4_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q3KP66-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q3KP66 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR043447;IPR021774; |
| Pfam | PF11819; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000163362-INAVA/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BTRC | Intact, Biogrid | true |
| CYTH1 | Intact, Biogrid | true |
| CYTH2 | Intact, Biogrid | true |
| FBXW11 | Intact, Biogrid | true |
| SGF29 | Biogrid, Bioplex | true |
| CEP170 | Biogrid | false |
| CYTH3 | Biogrid | false |
| IQGAP3 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

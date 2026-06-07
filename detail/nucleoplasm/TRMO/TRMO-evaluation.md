---
type: protein-evaluation
gene: "TRMO"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TRMO 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TRMO / C9orf156 |
| 蛋白名称 | tRNA (adenine(37)-N6)-methyltransferase |
| 蛋白大小 | 441 aa / 48.6 kDa |
| UniProt ID | Q9BU70 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 441 aa / 48.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR023370, IPR023368, IPR040372, IPR036413, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.5/180** | |
| **归一化总分** | | | **71.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
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
| PubMed strict count | 7 |
| PubMed broad count | 44 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C9orf156 |

**关键文献**:
1. Gene network and biological pathways associated with susceptibility to differentiated thyroid carcinoma.. *Scientific reports*. PMID: 33903625
2. Applications for Circulating Cell-Free DNA in Oral Squamous Cell Carcinoma: A Non-Invasive Approach for Detecting Structural Variants, Fusions, and Oncoviruses.. *Cancers*. PMID: 40563552
3. Identification and validation of prognostic models and tumor microenvironment infiltration characteristics for tRNA modification regulators in clear cell renal cell carcinoma.. *Oncology letters*. PMID: 40469919
4. In Silico Functional Characterization of a Hypothetical Protein From Pasteurella Multocida Reveals a Novel S-Adenosylmethionine-Dependent Methyltransferase Activity.. *Bioinformatics and biology insights*. PMID: 37424709
5. Tissue-specific role of dTrmO in threonine decoding during Drosophila melanogaster development.. *Biological research*. PMID: 41654963

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.5 |
| 高置信度残基 (pLDDT>90) 占比 | 40.6% |
| 置信残基 (pLDDT 70-90) 占比 | 12.2% |
| 中等置信 (pLDDT 50-70) 占比 | 7.0% |
| 低置信 (pLDDT<50) 占比 | 40.1% |
| 有序区域 (pLDDT>70) 占比 | 52.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=67.5），有序残基占 52.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR023370, IPR023368, IPR040372, IPR036413, IPR036414; Pfam: PF01980 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HEMGN | 0.821 | 0.000 | — |
| FOXE1 | 0.753 | 0.000 | — |
| ASTE1 | 0.537 | 0.000 | — |
| TMEM253 | 0.532 | 0.000 | — |
| ZNF202 | 0.529 | 0.000 | — |
| STX18 | 0.519 | 0.000 | — |
| ADTRP | 0.495 | 0.000 | — |
| STK32B | 0.495 | 0.000 | — |
| SEC22A | 0.494 | 0.000 | — |
| TBX10 | 0.491 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| def | psi-mi:"MI:0096"(pull down) | pubmed:16606699 |
| thrS | psi-mi:"MI:0096"(pull down) | pubmed:16606699 |
| groEL | psi-mi:"MI:0096"(pull down) | pubmed:16606699 |
| carA | psi-mi:"MI:0096"(pull down) | pubmed:16606699 |
| rplW | psi-mi:"MI:0096"(pull down) | pubmed:16606699 |
| STAC | psi-mi:"MI:0018"(two hybrid) | imex:IM-13772|pubmed:18654987 |
| SPATC1L | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MYH9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PSMC3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| STAT5B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.5 + PDB: 无 | pLDDT=67.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TRMO — tRNA (adenine(37)-N6)-methyltransferase，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小441 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=67.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BU70
- Protein Atlas: https://www.proteinatlas.org/ENSG00000136932-TRMO/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TRMO
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BU70
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000136932-TRMO/subcellular

![](https://images.proteinatlas.org/52197/766_H5_1_red_green.jpg)
![](https://images.proteinatlas.org/52197/766_H5_2_red_green.jpg)
![](https://images.proteinatlas.org/52197/778_H5_2_red_green.jpg)
![](https://images.proteinatlas.org/52197/778_H5_3_red_green.jpg)
![](https://images.proteinatlas.org/52197/863_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/52197/863_B1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BU70-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BU70 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 30..168; /note="TsaA-like"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01003" |
| InterPro | IPR023370;IPR023368;IPR040372;IPR036413;IPR036414; |
| Pfam | PF01980; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000136932-TRMO/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| SRC | Intact, Biogrid | true |
| GNA13 | Bioplex | false |
| NDUFA2 | Bioplex | false |
| RHPN2 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

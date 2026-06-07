---
type: protein-evaluation
gene: "SHPK"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SHPK 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SHPK / CARKL |
| 蛋白名称 | Sedoheptulokinase |
| 蛋白大小 | 478 aa / 51.5 kDa |
| UniProt ID | Q9UHJ6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Nuclear speckles; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 478 aa / 51.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=94.1; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR043129, IPR018484; Pfam: PF00370 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear speckles | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 19 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CARKL |

**关键文献**:
1. Deficiency of the sedoheptulose kinase (Shpk) does not alter the ability of hematopoietic stem cells to rescue cystinosis in the mouse model.. *Molecular genetics and metabolism*. PMID: 34823997
2. The 57 kb deletion in cystinosis patients extends into TRPV1 causing dysregulation of transcription in peripheral blood mononuclear cells.. *Journal of medical genetics*. PMID: 21546516
3. Genomic dissection of methane emission traits in cattle: A meta-GWAS and heritability analysis across populations.. *PloS one*. PMID: 41961873
4. Elevated concentrations of sedoheptulose in bloodspots of patients with cystinosis caused by the 57-kb deletion: implications for diagnostics and neonatal screening.. *Molecular genetics and metabolism*. PMID: 21195649

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.1 |
| 高置信度残基 (pLDDT>90) 占比 | 87.7% |
| 置信残基 (pLDDT 70-90) 占比 | 10.0% |
| 中等置信 (pLDDT 50-70) 占比 | 2.1% |
| 低置信 (pLDDT<50) 占比 | 0.2% |
| 有序区域 (pLDDT>70) 占比 | 97.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=94.1，有序区 97.7%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR043129, IPR018484; Pfam: PF00370 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CTNS | 0.978 | 0.000 | — |
| KCNA3 | 0.952 | 0.048 | — |
| FGGY | 0.879 | 0.000 | — |
| GPD2 | 0.796 | 0.097 | — |
| KCNA1 | 0.793 | 0.048 | — |
| KCNN4 | 0.731 | 0.000 | — |
| KCNA6 | 0.717 | 0.048 | — |
| LARS2 | 0.648 | 0.106 | — |
| EARS2 | 0.640 | 0.000 | — |
| FAM126A | 0.621 | 0.621 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MDM2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| TRAF3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| THYN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GATD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NR2F2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HYCC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TCF25 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FAM219A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| LRP4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| LRRC8E | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.1 + PDB: 无 | pLDDT=94.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm, Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. SHPK — Sedoheptulokinase，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小478 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UHJ6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000197417-SHPK/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SHPK
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UHJ6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000197417-SHPK/subcellular

![](https://images.proteinatlas.org/64939/1164_F7_4_red_green.jpg)
![](https://images.proteinatlas.org/64939/1164_F7_5_red_green.jpg)
![](https://images.proteinatlas.org/64939/1174_F7_3_red_green.jpg)
![](https://images.proteinatlas.org/64939/1174_F7_4_red_green.jpg)
![](https://images.proteinatlas.org/64939/1254_H2_1_red_green.jpg)
![](https://images.proteinatlas.org/64939/1254_H2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UHJ6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UHJ6 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR043129;IPR018484; |
| Pfam | PF00370; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000197417-SHPK/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| C10orf88 | Bioplex | false |
| PSMF1 | Bioplex | false |
| RAB6B | Bioplex | false |
| TCF25 | Bioplex | false |
| THYN1 | Intact | false |
| TRAF3 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

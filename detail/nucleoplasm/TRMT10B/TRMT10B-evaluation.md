---
type: protein-evaluation
gene: "TRMT10B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TRMT10B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TRMT10B / RG9MTD3 |
| 蛋白名称 | tRNA methyltransferase 10 homolog B |
| 蛋白大小 | 316 aa / 36.1 kDa |
| UniProt ID | Q6PF06 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Plasma membrane; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 316 aa / 36.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=80.1; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR028564, IPR038459, IPR047911, IPR007356 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **135.5/180** | |
| **归一化总分** | | | **75.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Plasma membrane | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- mitochondrial inner membrane (GO:0005743)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- TIM22 mitochondrial import inner membrane insertion complex (GO:0042721)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 3 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RG9MTD3 |

**关键文献**:
1. Functional characterization of the human tRNA methyltransferases TRMT10A and TRMT10B.. *Nucleic acids research*. PMID: 32392304
2. Distinct substrate specificities of the human tRNA methyltransferases TRMT10A and TRMT10B.. *RNA (New York, N.Y.)*. PMID: 31292261

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.1 |
| 高置信度残基 (pLDDT>90) 占比 | 57.6% |
| 置信残基 (pLDDT 70-90) 占比 | 18.7% |
| 中等置信 (pLDDT 50-70) 占比 | 5.1% |
| 低置信 (pLDDT<50) 占比 | 18.7% |
| 有序区域 (pLDDT>70) 占比 | 76.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=80.1，有序区 76.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR028564, IPR038459, IPR047911, IPR007356 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MRPS15 | 0.833 | 0.814 | — |
| MRPS31 | 0.830 | 0.782 | — |
| MRPS28 | 0.819 | 0.818 | — |
| MRPS18B | 0.807 | 0.799 | — |
| MRPS25 | 0.798 | 0.794 | — |
| MRPS27 | 0.795 | 0.783 | — |
| MRPS11 | 0.793 | 0.783 | — |
| MRPS14 | 0.785 | 0.782 | — |
| MRPS2 | 0.785 | 0.785 | — |
| MRPS16 | 0.783 | 0.779 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MEIS1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| NPM1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| OTX2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MRPS14 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PTX3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DAP3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MRPS25 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MRPS10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MRPS35 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MRPS5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.1 + PDB: 无 | pLDDT=80.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TRMT10B — tRNA methyltransferase 10 homolog B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小316 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6PF06
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165275-TRMT10B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TRMT10B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6PF06
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000165275-TRMT10B/subcellular

![](https://images.proteinatlas.org/21800/146_H7_1_red_green.jpg)
![](https://images.proteinatlas.org/21800/146_H7_2_red_green.jpg)
![](https://images.proteinatlas.org/21800/147_H7_1_red_green.jpg)
![](https://images.proteinatlas.org/21800/147_H7_2_red_green.jpg)
![](https://images.proteinatlas.org/21800/148_H7_1_red_green.jpg)
![](https://images.proteinatlas.org/21800/148_H7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6PF06-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6PF06 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 113..310; /note="SAM-dependent MTase TRM10-type"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01012" |
| InterPro | IPR028564;IPR038459;IPR047911;IPR007356; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000165275-TRMT10B/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

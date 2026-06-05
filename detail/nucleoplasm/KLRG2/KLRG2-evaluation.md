---
type: protein-evaluation
gene: "KLRG2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KLRG2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KLRG2 / CLEC15B |
| 蛋白名称 | Killer cell lectin-like receptor subfamily G member 2 |
| 蛋白大小 | 409 aa / 42.9 kDa |
| UniProt ID | A4D1S0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 409 aa / 42.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001304, IPR016186, IPR016187, IPR043318, IPR033 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Uncertain |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 12 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CLEC15B |

**关键文献**:
1. Genome-wide DNA methylation analysis in schizophrenia with tardive dyskinesia: a preliminary study.. *Genes & genomics*. PMID: 37414911
2. C6 and KLRG2 are pyroptosis subtype-related prognostic biomarkers and correlated with tumor-infiltrating lymphocytes in lung adenocarcinoma.. *Scientific reports*. PMID: 39438534
3. Expression Characteristics and Prognostic Value of KLRG2 in Endometrial Cancer: A Comprehensive Analysis Based on Multi-Omics Data.. *Biomedicines*. PMID: 40722666
4. Fine-mapping of prostate cancer aggressiveness loci on chromosome 7q22-35.. *The Prostate*. PMID: 20945404
5. Killer cell lectin-like receptor G2 facilitates aggressive phenotypes of gastric cancer cells via dual activation of the ERK1/2 and JAK/STAT pathways.. *Gastric cancer : official journal of the International Gastric Cancer Association and the Japanese Gastric Cancer Association*. PMID: 38386237

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.2 |
| 高置信度残基 (pLDDT>90) 占比 | 13.9% |
| 置信残基 (pLDDT 70-90) 占比 | 17.6% |
| 中等置信 (pLDDT 50-70) 占比 | 16.4% |
| 低置信 (pLDDT<50) 占比 | 52.1% |
| 有序区域 (pLDDT>70) 占比 | 31.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=58.2），有序残基占 31.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001304, IPR016186, IPR016187, IPR043318, IPR033992; Pfam: PF00059 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UBN2 | 0.659 | 0.000 | — |
| TNFRSF4 | 0.565 | 0.000 | — |
| FCGRT | 0.560 | 0.071 | — |
| TNFRSF8 | 0.548 | 0.000 | — |
| IL1RN | 0.525 | 0.000 | — |
| PRAMEF18 | 0.510 | 0.000 | — |
| SPATA31A6 | 0.474 | 0.000 | — |
| RWDD2B | 0.463 | 0.000 | — |
| WNT5B | 0.453 | 0.452 | — |
| GLRX3 | 0.447 | 0.447 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GXYLT2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FAM171A2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| APBA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TOR1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| AURKA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GLRX3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PRSS23 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| STBD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TNKS | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| WNT11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.2 + PDB: 无 | pLDDT=58.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. KLRG2 — Killer cell lectin-like receptor subfamily G member 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小409 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=58.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A4D1S0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000188883-KLRG2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KLRG2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A4D1S0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000188883-KLRG2/subcellular

![](https://images.proteinatlas.org/18199/1661_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/18199/1661_G1_2_red_green.jpg)
![](https://images.proteinatlas.org/18199/1729_H1_1_red_green.jpg)
![](https://images.proteinatlas.org/18199/1729_H1_2_red_green.jpg)
![](https://images.proteinatlas.org/18199/1918_G7_15_cr5cb48dae34cd4_red_green.jpg)
![](https://images.proteinatlas.org/18199/1918_G7_26_cr5cb48dae35154_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A4D1S0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

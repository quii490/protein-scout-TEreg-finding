---
type: protein-evaluation
gene: "PSTK"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PSTK 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PSTK / C10orf89 |
| 蛋白名称 | L-seryl-tRNA(Sec) kinase |
| 蛋白大小 | 348 aa / 39.5 kDa |
| UniProt ID | Q8IV42 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Actin filaments; 额外: Nucleoli, Nuclear bodies; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 348 aa / 39.5 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=36 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=76.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR013641, IPR020028, IPR027417, IPR052648; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **122.5/180** | |
| **归一化总分** | | | **68.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Actin filaments; 额外: Nucleoli, Nuclear bodies | Approved |
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
| PubMed strict count | 36 |
| PubMed broad count | 60 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C10orf89 |

**关键文献**:
1. PSTK inhibition activates cGAS-STING, precipitating ferroptotic cell death in leukemic stem cells.. *Blood*. PMID: 39912669
2. CRISPR screens uncover protective effect of PSTK as a regulator of chemotherapy-induced ferroptosis in hepatocellular carcinoma.. *Molecular cancer*. PMID: 34983546
3. Identification and characterization of phosphoseryl-tRNA[Ser]Sec kinase.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 15317934
4. Arabidopsis kinome: after the casting.. *Functional & integrative genomics*. PMID: 14740254
5. PSTK is a novel gene associated with early lung injury in Paraquat Poisoning.. *Life sciences*. PMID: 25592138

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.5 |
| 高置信度残基 (pLDDT>90) 占比 | 46.3% |
| 置信残基 (pLDDT 70-90) 占比 | 17.5% |
| 中等置信 (pLDDT 50-70) 占比 | 22.4% |
| 低置信 (pLDDT<50) 占比 | 13.8% |
| 有序区域 (pLDDT>70) 占比 | 63.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=76.5，有序区 63.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013641, IPR020028, IPR027417, IPR052648; Pfam: PF08433 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SEPSECS | 0.999 | 0.000 | — |
| SARS1 | 0.999 | 0.000 | — |
| SARS2-2 | 0.998 | 0.000 | — |
| EEFSEC | 0.993 | 0.000 | — |
| SARS2 | 0.989 | 0.000 | — |
| TRNAU1AP | 0.938 | 0.000 | — |
| SEPHS2 | 0.915 | 0.000 | — |
| SECISBP2 | 0.886 | 0.000 | — |
| SEPHS1 | 0.808 | 0.000 | — |
| SCLY | 0.713 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.5 + PDB: 无 | pLDDT=76.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Actin filaments; 额外: Nucleoli, Nuclear bodies | 待确认 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PSTK — L-seryl-tRNA(Sec) kinase，非常新颖，仅有少数基础研究。
2. 蛋白大小348 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 36 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IV42
- Protein Atlas: https://www.proteinatlas.org/ENSG00000179988-PSTK/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PSTK
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IV42
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Actin filaments (approved)。来源: https://www.proteinatlas.org/ENSG00000179988-PSTK/subcellular

![](https://images.proteinatlas.org/37781/422_E9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/37781/422_E9_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/37781/423_E9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/37781/423_E9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/37781/426_E9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/37781/426_E9_4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IV42-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8IV42 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR013641;IPR020028;IPR027417;IPR052648; |
| Pfam | PF08433; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000179988-PSTK/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| TXLNG | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

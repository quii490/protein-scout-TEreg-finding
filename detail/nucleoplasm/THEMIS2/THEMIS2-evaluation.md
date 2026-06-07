---
type: protein-evaluation
gene: "THEMIS2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## THEMIS2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | THEMIS2 / C1orf38, ICB1 |
| 蛋白名称 | Protein THEMIS2 |
| 蛋白大小 | 643 aa / 72.0 kDa |
| UniProt ID | Q5TEJ8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 643 aa / 72.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=23 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=74.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR025946, IPR039671; Pfam: PF12736 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.5/180** | |
| **归一化总分** | | | **68.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 23 |
| PubMed broad count | 44 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C1orf38, ICB1 |

**关键文献**:
1. Themis2 regulates natural killer cell memory function and formation.. *Nature communications*. PMID: 37938555
2. Themis2 is not required for B cell development, activation, and antibody responses.. *Journal of immunology (Baltimore, Md. : 1950)*. PMID: 24907343
3. The TNFRSF1B Connection: Implications for Androgenetic Alopecia Pathogenesis and Treatment.. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology*. PMID: 40343723
4. Themis2 lowers the threshold for B cell activation during positive selection.. *Nature immunology*. PMID: 27992403
5. Stemness-Relevant Gene Signature for Chemotherapeutic Response and Prognosis Prediction in Ovarian Cancer.. *Stem cells international*. PMID: 40182754

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.8 |
| 高置信度残基 (pLDDT>90) 占比 | 23.8% |
| 置信残基 (pLDDT 70-90) 占比 | 46.0% |
| 中等置信 (pLDDT 50-70) 占比 | 13.8% |
| 低置信 (pLDDT<50) 占比 | 16.3% |
| 有序区域 (pLDDT>70) 占比 | 69.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=74.8，有序区 69.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR025946, IPR039671; Pfam: PF12736 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LYN | 0.655 | 0.000 | — |
| EIF4E3 | 0.639 | 0.629 | — |
| SRGN | 0.623 | 0.000 | — |
| TYROBP | 0.621 | 0.000 | — |
| CD53 | 0.620 | 0.000 | — |
| MNDA | 0.580 | 0.000 | — |
| GRB2 | 0.573 | 0.071 | — |
| IL10RA | 0.565 | 0.000 | — |
| SASH3 | 0.539 | 0.000 | — |
| FGR | 0.520 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ddl | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| glnF | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| NOTCH2NLA | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| EIF4E3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DDX55 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-30059|pubmed:39251607 |
| LIN28B | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-30059|pubmed:39251607 |
| YWHAG | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-30059|pubmed:39251607 |
| SMNDC1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-30059|pubmed:39251607 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 8
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 8 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.8 + PDB: 无 | pLDDT=74.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 8 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. THEMIS2 — Protein THEMIS2，非常新颖，仅有少数基础研究。
2. 蛋白大小643 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 23 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5TEJ8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000130775-THEMIS2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=THEMIS2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5TEJ8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000130775-THEMIS2/subcellular

![](https://images.proteinatlas.org/27513/1798_F5_2_red_green.jpg)
![](https://images.proteinatlas.org/27513/1798_F5_3_red_green.jpg)
![](https://images.proteinatlas.org/27513/1893_N6_31_red_green.jpg)
![](https://images.proteinatlas.org/27513/1893_N6_32_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5TEJ8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5TEJ8 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR025946;IPR039671; |
| Pfam | PF12736; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000130775-THEMIS2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| NOTCH2NLA | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

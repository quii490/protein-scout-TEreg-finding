---
type: protein-evaluation
gene: "ELMOD2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ELMOD2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ELMOD2 |
| 蛋白名称 | ELMO domain-containing protein 2 |
| 蛋白大小 | 293 aa / 35.0 kDa |
| UniProt ID | Q8IZ81 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nuclear bodies, Actin filaments; 额外: Nucleoplasm, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 293 aa / 35.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=17 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=94.6; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR006816, IPR050868; Pfam: PF04727 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.0/180** | |
| **归一化总分** | | | **70.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies, Actin filaments; 额外: Nucleoplasm, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17 |
| PubMed broad count | 22 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Roles for ELMOD2 and Rootletin in ciliogenesis.. *Molecular biology of the cell*. PMID: 33596093
2. ELMOD2 Overexpression Predicts Adverse Outcomes and Regulates Tumor Progression in Gliomas.. *Current medical science*. PMID: 40397299
3. ELMOD2, a candidate gene for idiopathic pulmonary fibrosis, regulates antiviral responses.. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology*. PMID: 19966137
4. GTPase-activating protein Elmod2 is essential for meiotic progression in mouse oocytes.. *Cell cycle (Georgetown, Tex.)*. PMID: 28324667
5. ELMOD2 regulates mitochondrial fusion in a mitofusin-dependent manner, downstream of ARL2.. *Molecular biology of the cell*. PMID: 30865555

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.6 |
| 高置信度残基 (pLDDT>90) 占比 | 89.1% |
| 置信残基 (pLDDT 70-90) 占比 | 7.2% |
| 中等置信 (pLDDT 50-70) 占比 | 3.8% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 96.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=94.6，有序区 96.3%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006816, IPR050868; Pfam: PF04727 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SFTPA2 | 0.793 | 0.000 | — |
| ARL2 | 0.655 | 0.000 | — |
| SFTPA1 | 0.651 | 0.000 | — |
| ARL3 | 0.647 | 0.000 | — |
| SFTPC | 0.616 | 0.000 | — |
| TERT | 0.575 | 0.000 | — |
| TBC1D9 | 0.568 | 0.000 | — |
| RASA1 | 0.567 | 0.000 | — |
| MTUS1 | 0.554 | 0.000 | — |
| PMFBP1 | 0.538 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.6 + PDB: 无 | pLDDT=94.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nuclear bodies, Actin filaments; 额外: Nucleoplasm,  | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. ELMOD2 — ELMO domain-containing protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小293 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 17 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IZ81
- Protein Atlas: https://www.proteinatlas.org/ENSG00000179387-ELMOD2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ELMOD2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IZ81
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (approved)。来源: https://www.proteinatlas.org/ENSG00000179387-ELMOD2/subcellular

![](https://images.proteinatlas.org/41468/1819_B10_18_cr59f333d13211d_red_green.jpg)
![](https://images.proteinatlas.org/41468/1819_B10_3_cr59f333d130f2a_red_green.jpg)
![](https://images.proteinatlas.org/41468/1951_C12_3_red_green.jpg)
![](https://images.proteinatlas.org/41468/1951_C12_6_red_green.jpg)
![](https://images.proteinatlas.org/41468/2091_B9_1_red_green.jpg)
![](https://images.proteinatlas.org/41468/2091_B9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IZ81-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8IZ81 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 126..282; /note="ELMO"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00664" |
| InterPro | IPR006816;IPR050868; |
| Pfam | PF04727; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000179387-ELMOD2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| RHOG | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

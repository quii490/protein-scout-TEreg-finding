---
type: protein-evaluation
gene: "HMG20B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HMG20B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HMG20B / BRAF35, HMGX2, HMGXB2, SMARCE1R |
| 蛋白名称 | SWI/SNF-related matrix-associated actin-dependent regulator of chromatin subfamily E member 1-related |
| 蛋白大小 | 317 aa / 35.8 kDa |
| UniProt ID | Q9P0W2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus; Chromosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 317 aa / 35.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=77.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051965, IPR009071, IPR036910; Pfam: PF00505 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **141.5/180** | |
| **归一化总分** | | | **78.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus; Chromosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromosome (GO:0005694)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 39 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BRAF35, HMGX2, HMGXB2, SMARCE1R |

**关键文献**:
1. HMG20A is required for SNAI1-mediated epithelial to mesenchymal transition.. *Oncogene*. PMID: 25639869
2. HMG20B stabilizes association of LSD1 with GFI1 on chromatin to confer transcription repression and leukemia cell differentiation block.. *Oncogene*. PMID: 36171271
3. A mitotic function for the high-mobility group protein HMG20b regulated by its interaction with the BRC repeats of the BRCA2 tumor suppressor.. *Oncogene*. PMID: 21399666
4. The DNA binding factor Hmg20b is a repressor of erythroid differentiation.. *Haematologica*. PMID: 21606163
5. A cancer-associated mutation inactivates a region of the high-mobility group protein HMG20b essential for cytokinesis.. *Cell cycle (Georgetown, Tex.)*. PMID: 25486196

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.9 |
| 高置信度残基 (pLDDT>90) 占比 | 49.2% |
| 置信残基 (pLDDT 70-90) 占比 | 20.8% |
| 中等置信 (pLDDT 50-70) 占比 | 7.9% |
| 低置信 (pLDDT<50) 占比 | 22.1% |
| 有序区域 (pLDDT>70) 占比 | 70.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=77.9，有序区 70.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051965, IPR009071, IPR036910; Pfam: PF00505 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RCOR1 | 0.999 | 0.833 | — |
| KDM1A | 0.999 | 0.875 | — |
| PHF21A | 0.999 | 0.849 | — |
| HDAC1 | 0.998 | 0.827 | — |
| HDAC2 | 0.996 | 0.844 | — |
| GSE1 | 0.975 | 0.838 | — |
| ZNF217 | 0.965 | 0.091 | — |
| BRCA2 | 0.942 | 0.735 | — |
| HMG20A | 0.932 | 0.872 | — |
| RCOR3 | 0.903 | 0.796 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Traf1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| CCDC85B | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| VIM | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| HNRNPL | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| TACC2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| HDAC1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:21258344|imex:IM-17039 |
| HDAC2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:21258344|imex:IM-17039 |
| KDM1A | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:21258344|imex:IM-17039 |
| glpC | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.9 + PDB: 无 | pLDDT=77.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Chromosome / Nucleoplasm | 一致 |
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
1. HMG20B — SWI/SNF-related matrix-associated actin-dependent regulator of chromatin subfamily E member 1-related，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小317 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9P0W2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000064961-HMG20B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HMG20B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P0W2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000064961-HMG20B/subcellular

![](https://images.proteinatlas.org/50220/735_F10_1_red_green.jpg)
![](https://images.proteinatlas.org/50220/735_F10_2_red_green.jpg)
![](https://images.proteinatlas.org/50220/749_F10_1_red_green.jpg)
![](https://images.proteinatlas.org/50220/749_F10_2_red_green.jpg)
![](https://images.proteinatlas.org/50220/871_H10_1_red_green.jpg)
![](https://images.proteinatlas.org/50220/871_H10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9P0W2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

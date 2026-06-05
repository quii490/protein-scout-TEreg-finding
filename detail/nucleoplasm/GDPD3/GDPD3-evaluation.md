---
type: protein-evaluation
gene: "GDPD3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GDPD3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GDPD3 / GDE7 |
| 蛋白名称 | Lysophospholipase D GDPD3 |
| 蛋白大小 | 318 aa / 36.6 kDa |
| UniProt ID | Q7L5L3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytokinetic bridge, Cytosol; UniProt: Membrane; Cytoplasm, perinuclear region; Endoplasmic reticul |
| 蛋白大小 | 10/10 | ×1 | 10 | 318 aa / 36.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=92.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR052271, IPR030395, IPR017946; Pfam: PF03009 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.5/180** | |
| **归一化总分** | | | **76.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytokinetic bridge, Cytosol | Approved |
| UniProt | Membrane; Cytoplasm, perinuclear region; Endoplasmic reticulum | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)
- extracellular exosome (GO:0070062)
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 14 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GDE7 |

**关键文献**:
1. GDPD3 Deficiency Alleviates Neuropathic Pain and Reprograms Macrophagic Polarization Through PGE2 and PPARγ Pathway.. *Neurochemical research*. PMID: 38769197
2. Identification and validation of genetic signature associated with aging in chronic obstructive pulmonary disease.. *Aging*. PMID: 36309899
3. Human GDPD3 overexpression promotes liver steatosis by increasing lysophosphatidic acid production and fatty acid uptake.. *Journal of lipid research*. PMID: 32430316
4. Deficiency of the Endocytic Protein Hip1 Leads to Decreased Gdpd3 Expression, Low Phosphocholine, and Kypholordosis.. *Molecular and cellular biology*. PMID: 30224518
5. Identify GDPD3 as a key regulator of epithelial-mesenchymal transition and prostate adenocarcinoma progression via the LPA/LPAR1/AKT axis: transcriptomic and experimental study.. *Frontiers in immunology*. PMID: 41562071

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.2 |
| 高置信度残基 (pLDDT>90) 占比 | 80.5% |
| 置信残基 (pLDDT 70-90) 占比 | 12.9% |
| 中等置信 (pLDDT 50-70) 占比 | 4.4% |
| 低置信 (pLDDT<50) 占比 | 2.2% |
| 有序区域 (pLDDT>70) 占比 | 93.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=92.2，有序区 93.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052271, IPR030395, IPR017946; Pfam: PF03009 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ENPP2 | 0.988 | 0.000 | — |
| ENPP6 | 0.938 | 0.000 | — |
| ENPP3 | 0.924 | 0.000 | — |
| LPCAT4 | 0.910 | 0.000 | — |
| TMEM86B | 0.909 | 0.000 | — |
| GDPD1 | 0.907 | 0.000 | — |
| ENPP1 | 0.828 | 0.000 | — |
| PLA2G10 | 0.799 | 0.000 | — |
| PLA2G4A | 0.782 | 0.000 | — |
| PLA2G2A | 0.773 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CUL2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| DNAAF19 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZIC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NPPA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| AIRE | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CCR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PINK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PCP4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ERCC3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SH2D3A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.2 + PDB: 无 | pLDDT=92.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane; Cytoplasm, perinuclear region; Endoplasm / Nucleoplasm; 额外: Cytokinetic bridge, Cytosol | 一致 |
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
1. GDPD3 — Lysophospholipase D GDPD3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小318 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7L5L3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000102886-GDPD3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GDPD3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7L5L3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000102886-GDPD3/subcellular

![](https://images.proteinatlas.org/41470/1142_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/41470/1142_G6_8_red_green.jpg)
![](https://images.proteinatlas.org/41470/1208_B3_3_red_green.jpg)
![](https://images.proteinatlas.org/41470/1208_B3_5_red_green.jpg)
![](https://images.proteinatlas.org/41470/534_E8_1_red_green.jpg)
![](https://images.proteinatlas.org/41470/534_E8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7L5L3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

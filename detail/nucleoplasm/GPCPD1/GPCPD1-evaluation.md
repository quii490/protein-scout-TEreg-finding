---
type: protein-evaluation
gene: "GPCPD1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GPCPD1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPCPD1 / GDE5, KIAA1434 |
| 蛋白名称 | Glycerophosphocholine phosphodiesterase GPCPD1 |
| 蛋白大小 | 672 aa / 76.0 kDa |
| UniProt ID | Q9NPB8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; UniProt: Cytoplasm, cytosol |
| 蛋白大小 | 10/10 | ×1 | 10 | 672 aa / 76.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=17 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=87.1; PDB: 2Z0B |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR057506, IPR013784, IPR002044, IPR034839, IPR051 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **127.0/180** | |
| **归一化总分** | | | **70.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Uncertain |
| UniProt | Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17 |
| PubMed broad count | 40 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GDE5, KIAA1434 |

**关键文献**:
1. Hypoxia-induced GPCPD1 depalmitoylation triggers mitophagy via regulating PRKN-mediated ubiquitination of VDAC1.. *Autophagy*. PMID: 36803235
2. Role of Gpcpd1 in intestinal alpha-glycerophosphocholine metabolism and trimethylamine N-oxide production.. *The Journal of biological chemistry*. PMID: 39510189
3. A defective lysophosphatidic acid-autophagy axis increases miscarriage risk by restricting decidual macrophage residence.. *Autophagy*. PMID: 35220880
4. Chronic mild stress-induced protein dysregulations correlated with susceptibility and resiliency to depression or anxiety revealed by quantitative proteomics of the rat prefrontal cortex.. *Translational psychiatry*. PMID: 33627638
5. ACSL1, CH25H, GPCPD1, and PLA2G12A as the potential lipid-related diagnostic biomarkers of acute myocardial infarction.. *Aging*. PMID: 36863716

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.1 |
| 高置信度残基 (pLDDT>90) 占比 | 69.5% |
| 置信残基 (pLDDT 70-90) 占比 | 17.7% |
| 中等置信 (pLDDT 50-70) 占比 | 5.5% |
| 低置信 (pLDDT<50) 占比 | 7.3% |
| 有序区域 (pLDDT>70) 占比 | 87.2% |
| 可用 PDB 条目 | 2Z0B |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=87.1，有序区 87.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR057506, IPR013784, IPR002044, IPR034839, IPR051578; Pfam: PF25329, PF00686, PF03009 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CHKA | 0.953 | 0.000 | — |
| LYPLA1 | 0.951 | 0.000 | — |
| LYPLA2 | 0.943 | 0.000 | — |
| CHKB | 0.932 | 0.000 | — |
| PNPLA6 | 0.926 | 0.000 | — |
| PNPLA7 | 0.926 | 0.000 | — |
| CHAT | 0.924 | 0.000 | — |
| ETNK1 | 0.919 | 0.000 | — |
| PLB1 | 0.917 | 0.000 | — |
| ACHE | 0.916 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SLC35D3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZNF418 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PCBD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ENST00000379019 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.1 + PDB: 2Z0B | pLDDT=87.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. GPCPD1 — Glycerophosphocholine phosphodiesterase GPCPD1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小672 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 17 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NPB8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000125772-GPCPD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPCPD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NPB8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/GPCPD1/IF_images/A-549_1.jpg]]
![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/GPCPD1/IF_images/A-431_1.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000125772-GPCPD1/subcellular

![](https://images.proteinatlas.org/42987/918_F11_2_red_green.jpg)
![](https://images.proteinatlas.org/42987/918_F11_3_red_green.jpg)
![](https://images.proteinatlas.org/42987/981_D12_1_red_green.jpg)
![](https://images.proteinatlas.org/42987/981_D12_2_red_green.jpg)
![](https://images.proteinatlas.org/42987/984_D12_1_red_green.jpg)
![](https://images.proteinatlas.org/42987/984_D12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NPB8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

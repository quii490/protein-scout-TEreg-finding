---
type: protein-evaluation
gene: "DUSP19"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DUSP19 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DUSP19 / DUSP17, LMWDSP3, SKRP1 |
| 蛋白名称 | Dual specificity protein phosphatase 19 |
| 蛋白大小 | 217 aa / 24.2 kDa |
| UniProt ID | Q8WTR2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 217 aa / 24.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=88.2; PDB: 3S4E, 4D3P, 4D3Q, 4D3R |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000340, IPR029021, IPR000387, IPR020422; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.5/180** | |
| **归一化总分** | | | **72.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 12 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DUSP17, LMWDSP3, SKRP1 |

**关键文献**:
1. Collar occupancy: A new quantitative imaging tool for morphometric analysis of oligodendrocytes.. *Journal of neuroscience methods*. PMID: 29174019
2. DUSP19, a downstream effector of leptin, inhibits chondrocyte apoptosis via dephosphorylating JNK during osteoarthritis pathogenesis.. *Molecular bioSystems*. PMID: 26751999
3. PTEN regulates invasiveness in pancreatic neuroendocrine tumors through DUSP19-mediated VEGFR3 dephosphorylation.. *Journal of biomedical science*. PMID: 36336681
4. Circ_HIPK3 alleviates CoCl(2)-induced apoptotic injury in neuronal cells by depending on the regulation of the miR-222-3p/DUSP19 axis.. *Biochemical and biophysical research communications*. PMID: 33770577

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.2 |
| 高置信度残基 (pLDDT>90) 占比 | 64.1% |
| 置信残基 (pLDDT 70-90) 占比 | 22.6% |
| 中等置信 (pLDDT 50-70) 占比 | 11.5% |
| 低置信 (pLDDT<50) 占比 | 1.8% |
| 有序区域 (pLDDT>70) 占比 | 86.7% |
| 可用 PDB 条目 | 3S4E, 4D3P, 4D3Q, 4D3R |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3S4E, 4D3P, 4D3Q, 4D3R）+ AlphaFold高质量预测（pLDDT=88.2），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000340, IPR029021, IPR000387, IPR020422; Pfam: PF00782 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MAP2K7 | 0.948 | 0.563 | — |
| MAP3K5 | 0.767 | 0.292 | — |
| MAPK9 | 0.723 | 0.357 | — |
| ALAS1 | 0.712 | 0.712 | — |
| FEN1 | 0.560 | 0.512 | — |
| LRRFIP1 | 0.533 | 0.000 | — |
| MAP2K4 | 0.517 | 0.000 | — |
| NOL9 | 0.491 | 0.000 | — |
| LMOD3 | 0.455 | 0.000 | — |
| PAQR3 | 0.450 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=88.2 + PDB: 3S4E, 4D3P, 4D3Q, 4D3R | pLDDT=88.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DUSP19 — Dual specificity protein phosphatase 19，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小217 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WTR2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000162999-DUSP19/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DUSP19
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WTR2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000162999-DUSP19/subcellular

![](https://images.proteinatlas.org/21501/1364_D8_1_red_green.jpg)
![](https://images.proteinatlas.org/21501/1364_D8_2_red_green.jpg)
![](https://images.proteinatlas.org/21501/146_F6_1_red_green.jpg)
![](https://images.proteinatlas.org/21501/146_F6_2_red_green.jpg)
![](https://images.proteinatlas.org/21501/148_F6_1_red_green.jpg)
![](https://images.proteinatlas.org/21501/148_F6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8WTR2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8WTR2 |
| SMART | SM00195; |
| UniProt Domain [FT] | DOMAIN 65..206; /note="Tyrosine-protein phosphatase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00160" |
| InterPro | IPR000340;IPR029021;IPR000387;IPR020422; |
| Pfam | PF00782; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000162999-DUSP19/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ALAS1 | Intact, Biogrid | true |
| ACTB | Intact | false |
| ACTBL2 | Biogrid | false |
| GTPBP1 | Bioplex | false |
| MAP2K7 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

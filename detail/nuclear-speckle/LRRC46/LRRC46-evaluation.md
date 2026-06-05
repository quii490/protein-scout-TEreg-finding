---
type: protein-evaluation
gene: "LRRC46"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LRRC46 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LRRC46 |
| 蛋白名称 | Leucine-rich repeat-containing protein 46 |
| 蛋白大小 | 321 aa / 35.3 kDa |
| UniProt ID | Q96FV0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Plasma membrane; 额外: Nuclear bodies, Primary cilium, Basal b; UniProt: Cell projection, cilium, flagellum |
| 蛋白大小 | 10/10 | ×1 | 10 | 321 aa / 35.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050576, IPR001611, IPR003591, IPR032675; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117.5/180** | |
| **归一化总分** | | | **65.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Nuclear bodies, Primary cilium, Basal body | Approved |
| UniProt | Cell projection, cilium, flagellum | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- sperm flagellum (GO:0036126)
- sperm midpiece (GO:0097225)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 13 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Identification of Potential Therapeutic Gene Markers in Nasopharyngeal Carcinoma Based on Bioinformatics Analysis.. *Clinical and translational science*. PMID: 31863646
2. Identification of LRRC46 as a novel candidate gene for high myopia.. *Science China. Life sciences*. PMID: 38874710
3. LRRC46 Accumulates at the Midpiece of Sperm Flagella and Is Essential for Spermiogenesis and Male Fertility in Mouse.. *International journal of molecular sciences*. PMID: 35955660
4. CCDC181 is required for sperm flagellum biogenesis and male fertility in mice.. *Zoological research*. PMID: 39245650
5. Clinical effects of novel susceptibility genes for beta-amyloid: a gene-based association study in the Korean population.. *Frontiers in aging neuroscience*. PMID: 37901794

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.9 |
| 高置信度残基 (pLDDT>90) 占比 | 6.2% |
| 置信残基 (pLDDT 70-90) 占比 | 42.7% |
| 中等置信 (pLDDT 50-70) 占比 | 11.8% |
| 低置信 (pLDDT<50) 占比 | 39.3% |
| 有序区域 (pLDDT>70) 占比 | 48.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=63.9），有序残基占 48.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050576, IPR001611, IPR003591, IPR032675; Pfam: PF13855 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PACS2 | 0.742 | 0.736 | — |
| CFAP161 | 0.674 | 0.000 | — |
| ZMYND10 | 0.663 | 0.041 | — |
| TSNAXIP1 | 0.621 | 0.100 | — |
| POLE | 0.614 | 0.612 | — |
| CFAP57 | 0.611 | 0.099 | — |
| PPP1CC | 0.575 | 0.303 | — |
| PPP1CA | 0.572 | 0.303 | — |
| PPP1R3D | 0.567 | 0.000 | — |
| RIBC1 | 0.566 | 0.104 | — |

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
| 三维结构 | AlphaFold pLDDT=63.9 + PDB: 无 | pLDDT=63.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell projection, cilium, flagellum / Plasma membrane; 额外: Nuclear bodies, Primary ciliu | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. LRRC46 — Leucine-rich repeat-containing protein 46，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小321 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=63.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96FV0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000141294-LRRC46/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LRRC46
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96FV0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000141294-LRRC46/subcellular

![](https://images.proteinatlas.org/74893/1872_D7_34_blue_red_green.jpg)
![](https://images.proteinatlas.org/74893/1872_D7_36_blue_red_green.jpg)
![](https://images.proteinatlas.org/74893/1901_N20_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/74893/1901_N20_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/74893/1919_B8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/74893/1919_B8_4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96FV0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

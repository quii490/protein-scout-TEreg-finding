---
type: protein-evaluation
gene: "GLE1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GLE1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GLE1 / GLE1L |
| 蛋白名称 | mRNA export factor GLE1 |
| 蛋白大小 | 698 aa / 79.8 kDa |
| UniProt ID | Q53GS7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear membrane; 额外: Nucleoli, Cytosol; UniProt: Nucleus; Cytoplasm; Cytoplasm; Nucleus, nuclear pore complex |
| 蛋白大小 | 10/10 | ×1 | 10 | 698 aa / 79.8 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=80 篇 (≤80→4) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v6 pLDDT=0; PDB: 6B4F, 6B4I, 6B4J |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR012476, IPR038506; Pfam: PF07817 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **95.0/180** | |
| **归一化总分** | | | **52.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear membrane; 额外: Nucleoli, Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm; Cytoplasm; Nucleus, nuclear pore complex | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centriole (GO:0005814)
- centrosome (GO:0005813)
- ciliary basal body (GO:0036064)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular space (GO:0005615)
- membrane (GO:0016020)
- nuclear envelope (GO:0005635)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 80 |
| PubMed broad count | 120 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GLE1L |

**关键文献**:
1. Phosphorylation impacts GLE1 nuclear localization and association with DDX1.. *Advances in biological regulation*. PMID: 37801910
2. Inositol hexakisphosphate and Gle1 activate the DEAD-box protein Dbp5 for nuclear mRNA export.. *Nature cell biology*. PMID: 16783363
3. In vivo modeling of lethal congenital contracture syndrome 1 suggests pathomechanisms in cellular stress responses.. *The FEBS journal*. PMID: 40674274
4. Insights into mRNA export-linked molecular mechanisms of human disease through a Gle1 structure-function analysis.. *Advances in biological regulation*. PMID: 24275432
5. Chemically Induced Nuclear Pore Complex Protein Degradation via TRIM21.. *ACS chemical biology*. PMID: 40247740

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 6B4F, 6B4I, 6B4J |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR012476, IPR038506; Pfam: PF07817 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NUP42 | 0.998 | 0.981 | — |
| NUP214 | 0.998 | 0.965 | — |
| RAE1 | 0.992 | 0.847 | — |
| NUP155 | 0.988 | 0.772 | — |
| DDX19B | 0.950 | 0.918 | — |
| NUP88 | 0.945 | 0.412 | — |
| NUP107 | 0.942 | 0.686 | — |
| NUP133 | 0.933 | 0.642 | — |
| NXF1 | 0.933 | 0.503 | — |
| SON | 0.932 | 0.052 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| D6VRE7 | psi-mi:"MI:0040"(electron microscopy) | imex:IM-21748|pubmed:24243016 |
| ENSP00000308622.5 | psi-mi:"MI:0028"(cosedimentation in solution) | imex:IM-21748|pubmed:24243016 |
| AIM4 | psi-mi:"MI:0091"(chromatography technology) | pubmed:10684247 |
| GLE2 | psi-mi:"MI:0040"(electron microscopy) | pubmed:10684247 |
| NIC96 | psi-mi:"MI:0040"(electron microscopy) | pubmed:10684247 |
| NSP1 | psi-mi:"MI:0040"(electron microscopy) | pubmed:10684247 |
| NUP100 | psi-mi:"MI:0040"(electron microscopy) | pubmed:10684247 |
| NUP116 | psi-mi:"MI:0040"(electron microscopy) | pubmed:10684247 |
| NUP120 | psi-mi:"MI:0040"(electron microscopy) | pubmed:10684247 |
| NUP133 | psi-mi:"MI:0040"(electron microscopy) | pubmed:10684247 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 6B4F, 6B4I, 6B4J | pLDDT=0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cytoplasm; Nucleus, nuclear po / Nuclear membrane; 额外: Nucleoli, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. GLE1 — mRNA export factor GLE1，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小698 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 80 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q53GS7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000119392-GLE1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GLE1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q53GS7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear membrane (supported)。来源: https://www.proteinatlas.org/ENSG00000119392-GLE1/subcellular

![](https://images.proteinatlas.org/61560/1080_E3_1_red_green.jpg)
![](https://images.proteinatlas.org/61560/1080_E3_2_red_green.jpg)
![](https://images.proteinatlas.org/61560/1102_E3_2_red_green.jpg)
![](https://images.proteinatlas.org/61560/1102_E3_3_red_green.jpg)
![](https://images.proteinatlas.org/61560/1319_B11_1_red_green.jpg)
![](https://images.proteinatlas.org/61560/1319_B11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q53GS7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

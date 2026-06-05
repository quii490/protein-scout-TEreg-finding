---
type: protein-evaluation
gene: "DDN"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DDN 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DDN / KIAA0749 |
| 蛋白名称 | Dendrin |
| 蛋白大小 | 711 aa / 76.0 kDa |
| UniProt ID | O94850 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cell projection, dendritic spine membrane; Cytoplasm; Endopl |
| 蛋白大小 | 10/10 | ×1 | 10 | 711 aa / 76.0 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=73 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=45.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026500; Pfam: PF15498 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 10 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **100.0/180** | |
| **归一化总分** | | | **55.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Cell projection, dendritic spine membrane; Cytoplasm; Endoplasmic reticulum membrane; Perikaryon; Nu... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell projection (GO:0042995)
- cytoplasm (GO:0005737)
- dendritic spine membrane (GO:0032591)
- endoplasmic reticulum membrane (GO:0005789)
- nucleus (GO:0005634)
- perikaryon (GO:0043204)
- presynapse (GO:0098793)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 73 |
| PubMed broad count | 662 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0749 |

**关键文献**:
1. Comprehensive Genetic Analysis Reveals Complexity of Monogenic Urinary Stone Disease.. *Kidney international reports*. PMID: 34805638
2. Osteoporosis and osteoarthritis: a bi-directional Mendelian randomization study.. *Arthritis research & therapy*. PMID: 38093316
3. Whole-genome sequencing identifies novel genes for autism in Chinese trios.. *Science China. Life sciences*. PMID: 39126614
4. Activation and regulation of the dynein-dynactin-NuMA complex.. *Nature chemical biology*. PMID: 41840068
5. Molecular dynamic assisted investigation on impact of mutations in deazaflavin dependent nitroreductase against pretomanid: a computational study.. *Journal of biomolecular structure & dynamics*. PMID: 35574601

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 45.8 |
| 高置信度残基 (pLDDT>90) 占比 | 0.4% |
| 置信残基 (pLDDT 70-90) 占比 | 9.0% |
| 中等置信 (pLDDT 50-70) 占比 | 13.8% |
| 低置信 (pLDDT<50) 占比 | 76.8% |
| 有序区域 (pLDDT>70) 占比 | 9.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=45.8），有序残基占 9.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026500; Pfam: PF15498 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| WWC1 | 0.998 | 0.000 | — |
| MAGI2 | 0.904 | 0.850 | — |
| MAGI1 | 0.839 | 0.813 | — |
| NPHS1 | 0.762 | 0.000 | — |
| SYNPO | 0.734 | 0.000 | — |
| CD2AP | 0.712 | 0.089 | — |
| MAGI3 | 0.673 | 0.515 | — |
| CCDC192 | 0.648 | 0.000 | — |
| CTXN3 | 0.648 | 0.000 | — |
| KIRREL1 | 0.551 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SH3KBP1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16751601|imex:IM-17254| |
| Magi1 | psi-mi:"MI:0018"(two hybrid) | pubmed:16751601|imex:IM-17254| |
| Magi2 | psi-mi:"MI:0096"(pull down) | pubmed:16751601|imex:IM-17254| |
| Syngap1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |
| RALA | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| CD2AP | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| Dlgap1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |
| NEDD4 | psi-mi:"MI:0084"(phage display) | imex:IM-29361|pubmed:35044719 |
| YAP1 | psi-mi:"MI:0084"(phage display) | imex:IM-29361|pubmed:35044719 |
| ENST00000421952 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 10
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 10 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=45.8 + PDB: 无 | pLDDT=45.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell projection, dendritic spine membrane; Cytopla / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 10 interactions | 数据充分 |

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
1. DDN — Dendrin，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小711 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 73 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=45.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O94850
- Protein Atlas: https://www.proteinatlas.org/ENSG00000181418-DDN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DDN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O94850
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000181418-DDN/subcellular

![](https://images.proteinatlas.org/60952/1504_H7_2_red_green.jpg)
![](https://images.proteinatlas.org/60952/1504_H7_3_red_green.jpg)
![](https://images.proteinatlas.org/60952/1512_H7_1_red_green.jpg)
![](https://images.proteinatlas.org/60952/1512_H7_2_red_green.jpg)
![](https://images.proteinatlas.org/60952/1520_F10_1_red_green.jpg)
![](https://images.proteinatlas.org/60952/1520_F10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O94850-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

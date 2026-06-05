---
type: protein-evaluation
gene: "SHCBP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SHCBP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SHCBP1 |
| 蛋白名称 | SHC SH2 domain-binding protein 1 |
| 蛋白大小 | 672 aa / 75.7 kDa |
| UniProt ID | Q8NEM2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nuclear bodies; 额外: Microtubules, Midbody, Mitotic spindle; UniProt: Midbody; Cytoplasm, cytoskeleton, spindle |
| 蛋白大小 | 10/10 | ×1 | 10 | 672 aa / 75.7 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=86 篇 (≤100→2) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=73.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039448, IPR006626, IPR012334, IPR011050, IPR057 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies; 额外: Microtubules, Midbody, Mitotic spindle | Approved |
| UniProt | Midbody; Cytoplasm, cytoskeleton, spindle | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- midbody (GO:0030496)
- spindle (GO:0005819)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 86 |
| PubMed broad count | 102 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Hyperactivation of HER2-SHCBP1-PLK1 axis promotes tumor cell mitosis and impairs trastuzumab sensitivity to gastric cancer.. *Nature communications*. PMID: 33990570
2. EGF-induced nuclear translocation of SHCBP1 promotes bladder cancer progression through inhibiting RACGAP1-mediated RAC1 inactivation.. *Cell death & disease*. PMID: 35013128
3. The Role of Shcbp1 in Signaling and Disease.. *Current cancer drug targets*. PMID: 31250756
4. Targeting SHCBP1 Inhibits Tumor Progression by Restoring Ciliogenesis in Ductal Carcinoma.. *Cancer research*. PMID: 39312205
5. Comprehensive analysis of anoikis-related genes in diagnosis osteoarthritis: based on machine learning and single-cell RNA sequencing data.. *Artificial cells, nanomedicine, and biotechnology*. PMID: 38423139

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.5 |
| 高置信度残基 (pLDDT>90) 占比 | 37.1% |
| 置信残基 (pLDDT 70-90) 占比 | 31.5% |
| 中等置信 (pLDDT 50-70) 占比 | 9.2% |
| 低置信 (pLDDT<50) 占比 | 22.2% |
| 有序区域 (pLDDT>70) 占比 | 68.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=73.5，有序区 68.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039448, IPR006626, IPR012334, IPR011050, IPR057508; Pfam: PF13229, PF23762 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RACGAP1 | 0.965 | 0.844 | — |
| KIF23 | 0.965 | 0.829 | — |
| SHC1 | 0.941 | 0.294 | — |
| KIF11 | 0.863 | 0.000 | — |
| NCAPG2 | 0.854 | 0.000 | — |
| BIRC5 | 0.853 | 0.000 | — |
| RRM2 | 0.834 | 0.000 | — |
| PBK | 0.834 | 0.000 | — |
| NCAPG | 0.830 | 0.000 | — |
| POLDIP3 | 0.827 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Q3UMD9 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Shc1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| ZUP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| YWHAG | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| USP49 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| PDIA4 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| GPC5 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| ALDH3B1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| ACOT9 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| RACGAP1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.5 + PDB: 无 | pLDDT=73.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Midbody; Cytoplasm, cytoskeleton, spindle / Nuclear bodies; 额外: Microtubules, Midbody, Mitotic | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. SHCBP1 — SHC SH2 domain-binding protein 1，研究基础较多，新颖性有限。
2. 蛋白大小672 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 86 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NEM2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000171241-SHCBP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SHCBP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NEM2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (approved)。来源: https://www.proteinatlas.org/ENSG00000171241-SHCBP1/subcellular

![](https://images.proteinatlas.org/48876/1773_D8_13_blue_red_green.jpg)
![](https://images.proteinatlas.org/48876/1773_D8_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/48876/827_E9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/48876/827_E9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/48876/977_E9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/48876/977_E9_5_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NEM2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

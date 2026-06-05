---
type: protein-evaluation
gene: "PCED1A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PCED1A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PCED1A / C20orf81, FAM113A |
| 蛋白名称 | PC-esterase domain-containing protein 1A |
| 蛋白大小 | 454 aa / 51.8 kDa |
| UniProt ID | Q9H1Q7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 454 aa / 51.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=70.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR059235 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 11 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.0/180** | |
| **归一化总分** | | | **67.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 6 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C20orf81, FAM113A |

**关键文献**:
1. Succinylation-related molecular activities in cancer: metabolic adaptations, immune landscape, and prognostic significance in colorectal cancer.. *Frontiers in immunology*. PMID: 40463370
2. Whole genome sequencing of mouse lines divergently selected for fatness (FLI) and leanness (FHI) revealed several genetic variants as candidates for novel obesity genes.. *Genes & genomics*. PMID: 38483771
3. Expression of PCED1A in Hepatocellular Carcinoma and Colorectal Cancer and Its Relationship with Immune Infiltration: Potential as a Diagnostic Marker.. *Journal of gastroenterology and hepatology*. PMID: 39865523
4. PCED1A serves as a potential biomarker for diagnosis and prognosis in colorectal cancer.. *Discover oncology*. PMID: 40775410

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.3 |
| 高置信度残基 (pLDDT>90) 占比 | 49.8% |
| 置信残基 (pLDDT 70-90) 占比 | 5.7% |
| 中等置信 (pLDDT 50-70) 占比 | 6.2% |
| 低置信 (pLDDT<50) 占比 | 38.3% |
| 有序区域 (pLDDT>70) 占比 | 55.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=70.3，有序区 55.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR059235 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SLX4IP | 0.598 | 0.000 | — |
| RBM26 | 0.548 | 0.000 | — |
| VPS16 | 0.522 | 0.000 | — |
| VPS50 | 0.507 | 0.000 | — |
| RNF24 | 0.499 | 0.000 | — |
| POF1B | 0.470 | 0.000 | — |
| ATRN | 0.460 | 0.000 | — |
| ESF1 | 0.459 | 0.000 | — |
| TRERF1 | 0.418 | 0.000 | — |
| ZNF711 | 0.417 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CDK2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| CAV1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| 6319953 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EBI-1049959 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EBI-1052818 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TNFRSF14 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| UBE2M | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PLSCR1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| Q81P31 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ENSP00000353868.2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 11，IntAct interactions: 15
- 调控相关比例: 0 / 11 = 0%

**评价**: STRING 11 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.3 + PDB: 无 | pLDDT=70.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Cytosol | 待确认 |
| PPI | STRING + IntAct | 11 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PCED1A — PC-esterase domain-containing protein 1A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小454 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H1Q7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000132635-PCED1A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PCED1A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H1Q7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000132635-PCED1A/subcellular

![](https://images.proteinatlas.org/50816/740_A2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/50816/740_A2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/50816/784_A2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/50816/784_A2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/50816/837_A9_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/50816/837_A9_6_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H1Q7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

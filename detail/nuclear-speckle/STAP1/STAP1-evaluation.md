---
type: protein-evaluation
gene: "STAP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## STAP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | STAP1 / BRDG1 |
| 蛋白名称 | Signal-transducing adaptor protein 1 |
| 蛋白大小 | 295 aa / 34.3 kDa |
| UniProt ID | Q9ULZ2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear bodies, Cytosol; UniProt: Nucleus; Cytoplasm; Mitochondrion |
| 蛋白大小 | 10/10 | ×1 | 10 | 295 aa / 34.3 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=50 篇 (≤60→6) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=78.5; PDB: 1X1F, 3MAZ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011993, IPR001849, IPR000980, IPR036860, IPR039 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.0/180** | |
| **归一化总分** | | | **66.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies, Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm; Mitochondrion | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- mitochondrion (GO:0005739)
- nuclear body (GO:0016604)
- nucleus (GO:0005634)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 50 |
| PubMed broad count | 71 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BRDG1 |

**关键文献**:
1. Delisting STAP1: The Rise and Fall of a Putative Hypercholesterolemia Gene.. *Arteriosclerosis, thrombosis, and vascular biology*. PMID: 32208993
2. Signal-transducing adaptor protein-1 and protein-2 in hematopoiesis and diseases.. *Experimental hematology*. PMID: 34780812
3. FH4=STAP1. Another gene for familial hypercholesterolemia? Relevance to cascade testing and drug development?. *Circulation research*. PMID: 25170087
4. Signal-transducing adaptor protein 1 (STAP1) in microglia promotes the malignant progression of glioma.. *Journal of neuro-oncology*. PMID: 37462801
5. Evaluation of the role of STAP1 in Familial Hypercholesterolemia.. *Scientific reports*. PMID: 31427613

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.5 |
| 高置信度残基 (pLDDT>90) 占比 | 36.6% |
| 置信残基 (pLDDT 70-90) 占比 | 42.4% |
| 中等置信 (pLDDT 50-70) 占比 | 5.1% |
| 低置信 (pLDDT<50) 占比 | 15.9% |
| 有序区域 (pLDDT>70) 占比 | 79.0% |
| 可用 PDB 条目 | 1X1F, 3MAZ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1X1F, 3MAZ）+ AlphaFold高质量预测（pLDDT=78.5），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011993, IPR001849, IPR000980, IPR036860, IPR039111; Pfam: PF00169, PF00017 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SH3KBP1 | 0.861 | 0.837 | — |
| CD2AP | 0.836 | 0.834 | — |
| BMX | 0.773 | 0.054 | — |
| BTK | 0.659 | 0.054 | — |
| ITK | 0.654 | 0.054 | — |
| TXK | 0.620 | 0.054 | — |
| CAPZA2 | 0.612 | 0.612 | — |
| CAPZB | 0.595 | 0.595 | — |
| LDLRAP1 | 0.580 | 0.000 | — |
| PLEK | 0.560 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EGFR | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| EHD4 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| PTPRC | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| PEAK1 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| RETREG3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| Relch | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| Sh2b1 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| Eif2b4 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| Cyp3a23-3a1 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| Haus8 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.5 + PDB: 1X1F, 3MAZ | pLDDT=78.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Mitochondrion / Nuclear bodies, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. STAP1 — Signal-transducing adaptor protein 1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小295 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 50 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9ULZ2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000035720-STAP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=STAP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9ULZ2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (supported)。来源: https://www.proteinatlas.org/ENSG00000035720-STAP1/subcellular

![](https://images.proteinatlas.org/38094/1849_G6_10_cr5afc4626562f9_blue_red_green.jpg)
![](https://images.proteinatlas.org/38094/1849_G6_30_cr5afc4626567d8_blue_red_green.jpg)
![](https://images.proteinatlas.org/38094/2059_E11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/38094/2059_E11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/38094/2181_E9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/38094/2181_E9_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9ULZ2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9ULZ2 |
| SMART | SM00233;SM00252; |
| UniProt Domain [FT] | DOMAIN 25..121; /note="PH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00145"; DOMAIN 177..280; /note="SH2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00191" |
| InterPro | IPR011993;IPR001849;IPR000980;IPR036860;IPR039111;IPR035877; |
| Pfam | PF00169;PF00017; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000035720-STAP1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| SH3KBP1 | Intact, Biogrid | true |
| CAPZA1 | Bioplex | false |
| CAPZA2 | Bioplex | false |
| CD2AP | Bioplex | false |
| GRIPAP1 | Intact | false |
| RETREG3 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

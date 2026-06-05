---
type: protein-evaluation
gene: "CEP57"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation, E-batch]
status: scored
---

## CEP57 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CEP57 / KIAA0092 / TSP57 |
| 蛋白名称 | Centrosomal protein of 57 kDa |
| 蛋白大小 | 500 aa / 57.1 kDa |
| UniProt ID | Q86XR8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Centrosome; 额外: Centriolar satellite, Cytosol; UniProt: Nucleus; Cytoplasm; Cytoplasm, cytoskel |
| 蛋白大小 | 10/10 | ×1 | 10 | 500 aa / 57.1 kDa |
| 研究新颖性 | 9/10 | ×5 | 45 | PubMed strict=33 篇 |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=75.3; PDB: 暂无 |
| 调控结构域 | 9/10 | ×2 | 18 | InterPro: IPR051756, IPR025913, IPR024957; Pfam: PF14073, PF06657 |
| PPI 网络 | 10/10 | ×3 | 30 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.2 | AlphaFold 结构预测: +0.25 |
| **原始总分** | | | **141.2/180** | |
| **归一化总分 (÷1.83)** | | | **77.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Centrosome | Supported |
| UniProt | Nucleus | ECO:0000250
| UniProt | Cytoplasm | —
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome | ECO:0000269

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- centriolar satellite (GO:0034451) [IDA:HPA]
- centrosome (GO:0005813) [IDA:HPA]
- cytosol (GO:0005829) [IDA:HPA]
- Golgi apparatus (GO:0005794) [IDA:UniProtKB]
- microtubule (GO:0005874) [IDA:UniProtKB]
- nucleus (GO:0005634) [ISS:HGNC-UCL]

**结论**: HPA: Centrosome; 额外: Centriolar satellite, Cytosol; UniProt: Nucleus; Cytoplasm; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome

#### 3.2 蛋白大小评估

**评价**: 500 aa / 57.1 kDa，大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 33 |
| PubMed 搜索链接 | [CEP57 PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=CEP57) |

**关键文献**:
暂无文献记录。

**评价**: 较新颖，研究关注度低。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.3 |
| 高置信度残基 (pLDDT>90) 占比 | 47.2% |
| 置信残基 (pLDDT 70-90) 占比 | 13.0% |
| 中等置信 (pLDDT 50-70) 占比 | 17.4% |
| 低置信 (pLDDT<50) 占比 | 22.4% |
| 有序区域 (pLDDT>70) 占比 | 60.2% |
| 可用 PDB 条目 | 暂无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量中等。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051756, IPR025913, IPR024957; Pfam: PF14073, PF06657 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CEP63 | 0.956 | 0.701 | — |
| PLK1 | 0.834 | 0.000 | — |
| CEP152 | 0.784 | 0.428 | — |
| TRIP13 | 0.681 | 0.000 | — |
| BUB1B | 0.677 | 0.000 | — |
| MYH11 | 0.647 | 0.000 | — |
| PLK4 | 0.637 | 0.000 | — |
| FGF1 | 0.631 | 0.000 | — |
| CEP290 | 0.612 | 0.161 | — |
| HAUS2 | 0.600 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MEGF10 | psi-mi:"MI:0018"(two hybrid) | pubmed:unassigned5 |
| tktA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| vpu | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-17346|pubmed:22190034|psi-mi:"MI:0007" |
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:20195357|imex:IM-20475 |
| HDAC6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-18733|pubmed:23752268 |
| EBI-20625841 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:30177828|imex:IM-26452 |
| GCC1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s41467-019-11959-3|pubmed:31515488 |
| TFIP11 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s41467-019-11959-3|pubmed:31515488 |
| RABEP1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MAGEA2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0/15。

**评价**: STRING + IntAct 双源 PPI 数据充分。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold | pLDDT=75.3, v6 | 预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome / Centrosome | 部分一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- AlphaFold 结构预测: +0.25
- 单库核定位证据: +0.25
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5

**总分**: +1.2 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐

**归一化总分**: 77.2/100

**核心优势**:
1. CEP57 — Centrosomal protein of 57 kDa，极度新颖，几乎未被系统研究（PubMed 33 篇）。
2. 蛋白大小500 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. 核定位信号较弱，多源数据支持有限。

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86XR8
- Protein Atlas: https://www.proteinatlas.org/search/CEP57
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CEP57
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86XR8
- STRING: https://string-db.org/network/9606.CEP57
- Packet data timestamp: 2026-06-03 04:49:41

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Centrosome (supported)。来源: https://www.proteinatlas.org/ENSG00000166037-CEP57/subcellular

![](https://images.proteinatlas.org/66403/1827_G2_17_cr5ac377d830d0c_blue_red_green.jpg)
![](https://images.proteinatlas.org/66403/1827_G2_1_cr5ac377d83031d_blue_red_green.jpg)
![](https://images.proteinatlas.org/66403/2034_E1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/66403/2034_E1_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/66403/2086_B11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/66403/2086_B11_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86XR8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

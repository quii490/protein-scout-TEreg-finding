---
type: protein-evaluation
gene: "CGNL1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation, E-batch]
status: scored
---

## CGNL1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CGNL1 / JACOP / KIAA1749 |
| 蛋白名称 | Cingulin-like protein 1 |
| 蛋白大小 | 1302 aa / 149.1 kDa |
| UniProt ID | Q0VF96 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cell Junctions; 额外: Nuclear bodies; UniProt: Cell junction, tight junction |
| 蛋白大小 | 6/10 | ×1 | 6 | 1302 aa / 149.1 kDa |
| 研究新颖性 | 9/10 | ×5 | 45 | PubMed strict=31 篇 |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.1; PDB: 暂无 |
| 调控结构域 | 5/10 | ×2 | 10 | InterPro: IPR002928; Pfam: PF01576 |
| PPI 网络 | 10/10 | ×3 | 30 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | AlphaFold 结构预测: +0.25 |
| **原始总分** | | | **126.0/180** | |
| **归一化总分 (÷1.83)** | | | **68.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cell Junctions | Supported |
| UniProt | Cell junction, tight junction | ECO:0000250

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- bicellular tight junction (GO:0005923) [IBA:GO_Central]
- myosin complex (GO:0016459) [IEA:InterPro]
- protein-containing complex (GO:0032991) [IDA:ARUK-UCL]

**结论**: HPA: Cell Junctions; 额外: Nuclear bodies; UniProt: Cell junction, tight junction

#### 3.2 蛋白大小评估

**评价**: 1302 aa / 149.1 kDa，蛋白大小稍偏，但可进行常规生化分析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 31 |
| PubMed 搜索链接 | [CGNL1 PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=CGNL1) |

**关键文献**:
暂无文献记录。

**评价**: 较新颖，研究关注度低。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.1 |
| 高置信度残基 (pLDDT>90) 占比 | 30.0% |
| 置信残基 (pLDDT 70-90) 占比 | 18.8% |
| 中等置信 (pLDDT 50-70) 占比 | 8.7% |
| 低置信 (pLDDT<50) 占比 | 42.5% |
| 有序区域 (pLDDT>70) 占比 | 48.8% |
| 可用 PDB 条目 | 暂无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量中等。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002928; Pfam: PF01576 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ARHGEF2 | 0.992 | 0.000 | — |
| TJP1 | 0.975 | 0.303 | — |
| TMOD3 | 0.906 | 0.000 | — |
| ARHGEF18 | 0.872 | 0.000 | — |
| ARHGEF18-2 | 0.872 | 0.000 | — |
| RACGAP1 | 0.840 | 0.000 | — |
| PLEKHA7 | 0.830 | 0.000 | — |
| CYP19A1 | 0.774 | 0.000 | — |
| TMOD2 | 0.760 | 0.000 | — |
| OCLN | 0.748 | 0.071 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| YWHAE | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| YWHAG | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| WNK1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| APC | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| YWHAH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| YWHAB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| RCN2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653|doi:10.1074/mcp.ra118.000924 |
| EEF1G | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653|doi:10.1074/mcp.ra118.000924 |
| HSPA5 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653|doi:10.1074/mcp.ra118.000924 |
| PDIA5 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653|doi:10.1074/mcp.ra118.000924 |

**PPI 互证分析**:
STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0/15。

**评价**: STRING + IntAct 双源 PPI 数据充分。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold | pLDDT=63.1, v6 | 预测 |
| 定位 | UniProt + HPA | Cell junction, tight junction / Cell Junctions | 部分一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- AlphaFold 结构预测: +0.25
- 单库核定位证据: +0.25
- STRING + IntAct 双源验证: +0.5
- 结构域注释 + AlphaFold 预测: +0.25

**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**归一化总分**: 68.9/100

**核心优势**:
1. CGNL1 — Cingulin-like protein 1，极度新颖，几乎未被系统研究（PubMed 31 篇）。

**风险/不确定性**:
1. 核定位信号较弱，多源数据支持有限。

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q0VF96
- Protein Atlas: https://www.proteinatlas.org/search/CGNL1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CGNL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q0VF96
- STRING: https://string-db.org/network/9606.CGNL1
- Packet data timestamp: 2026-06-03 04:53:51

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cell Junctions (supported)。来源: https://www.proteinatlas.org/ENSG00000128849-CGNL1/subcellular

![](https://images.proteinatlas.org/69214/1635_H1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/69214/1635_H1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/69214/1647_D10_34_blue_red_green.jpg)
![](https://images.proteinatlas.org/69214/1647_D10_40_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q0VF96-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

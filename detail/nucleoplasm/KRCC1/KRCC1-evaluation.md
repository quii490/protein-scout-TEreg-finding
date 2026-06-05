---
type: protein-evaluation
gene: "KRCC1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KRCC1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KRCC1 / CHBP2 |
| 蛋白名称 | Lysine-rich coiled-coil protein 1 |
| 蛋白大小 | 259 aa / 31.0 kDa |
| UniProt ID | Q9NPI7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nucleoli; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 259 aa / 31.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.4; PDB: 无 |
| 调控结构域 | 5/10 | ×2 | 10 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 11 partners; IntAct 7 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.0/180** | |
| **归一化总分** | | | **70.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoli | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 4 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CHBP2 |

**关键文献**:
1. Increased expression of MERTK is associated with a unique form of canine retinopathy.. *PloS one*. PMID: 25517981
2. KRCC1, a modulator of the DNA damage response.. *Nucleic acids research*. PMID: 36243983

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.4 |
| 高置信度残基 (pLDDT>90) 占比 | 5.8% |
| 置信残基 (pLDDT 70-90) 占比 | 9.3% |
| 中等置信 (pLDDT 50-70) 占比 | 55.2% |
| 低置信 (pLDDT<50) 占比 | 29.7% |
| 有序区域 (pLDDT>70) 占比 | 15.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=58.4），有序残基占 15.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ARL6IP4 | 0.547 | 0.547 | — |
| CPSF4L | 0.493 | 0.000 | — |
| HEBP1 | 0.452 | 0.000 | — |
| CCNL1 | 0.445 | 0.000 | — |
| ZNF644 | 0.431 | 0.000 | — |
| TMEM101 | 0.423 | 0.000 | — |
| THNSL2 | 0.420 | 0.000 | — |
| ANGEL2 | 0.408 | 0.000 | — |
| KIAA1841 | 0.406 | 0.000 | — |
| TEX37 | 0.404 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| bipA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| PPP1CC | psi-mi:"MI:0018"(two hybrid) | pubmed:21382349|imex:IM-17664 |
| ARL6IP4 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| SPANXN2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| NKAPD1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SPRED1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| GTF2IRD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 11，IntAct interactions: 7
- 调控相关比例: 0 / 11 = 0%

**评价**: STRING 11 个预测互作，IntAct 7 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.4 + PDB: 无 | pLDDT=58.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Cytosol; 额外: Nucleoli | 一致 |
| PPI | STRING + IntAct | 11 + 7 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. KRCC1 — Lysine-rich coiled-coil protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小259 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=58.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NPI7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000172086-KRCC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KRCC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NPI7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000172086-KRCC1/subcellular

![](https://images.proteinatlas.org/52666/1137_F8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/52666/1137_F8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/52666/833_E10_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/52666/833_E10_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/52666/864_E8_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/52666/864_E8_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NPI7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

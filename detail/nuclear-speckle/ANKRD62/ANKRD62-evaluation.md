---
type: protein-evaluation
gene: "ANKRD62"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ANKRD62 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ANKRD62 |
| 蛋白名称 | Ankyrin repeat domain-containing protein 62 |
| 蛋白大小 | 917 aa / 106.4 kDa |
| UniProt ID | A6NC57 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 5/10 | ×4 | 20 | HPA: Nucleoplasm, Nuclear bodies; 额外: Actin filaments; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 917 aa / 106.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=75.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050657, IPR002110, IPR036770, IPR039497; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.0/180** | |
| **归一化总分** | | | **68.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear bodies; 额外: Actin filaments | Uncertain |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据存在但较为混杂，部分数据源指向非核区室。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 2 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Prognostic factors of 87 ovarian yolk sac tumor (OYST) patients and molecular characteristics of persistent and recurrent OYST.. *Gynecologic oncology*. PMID: 38733954
2. ANKRD62 Modulates NF-κB Signaling to Promote Proliferation and Migration in UCEC.. *Cancer medicine*. PMID: 41987392

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.3 |
| 高置信度残基 (pLDDT>90) 占比 | 27.3% |
| 置信残基 (pLDDT 70-90) 占比 | 45.5% |
| 中等置信 (pLDDT 50-70) 占比 | 8.2% |
| 低置信 (pLDDT<50) 占比 | 19.1% |
| 有序区域 (pLDDT>70) 占比 | 72.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=75.3，有序区 72.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050657, IPR002110, IPR036770, IPR039497; Pfam: PF12796, PF14915 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MTMR12 | 0.598 | 0.098 | — |
| C3orf22 | 0.589 | 0.000 | — |
| C1orf167 | 0.565 | 0.000 | — |
| EEF2KMT | 0.563 | 0.000 | — |
| RNASE12 | 0.544 | 0.000 | — |
| C12orf56 | 0.543 | 0.000 | — |
| WDR97 | 0.534 | 0.051 | — |
| SMIM17 | 0.527 | 0.000 | — |
| CC2D2B | 0.509 | 0.000 | — |
| SH2D7 | 0.507 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MAP1LC3A | psi-mi:"MI:0084"(phage display) | imex:IM-29361|pubmed:35044719 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 1
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 1 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.3 + PDB: 无 | pLDDT=75.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Nuclear bodies; 额外: Actin filaments | 待确认 |
| PPI | STRING + IntAct | 15 + 1 interactions | 数据充分 |

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
1. ANKRD62 — Ankyrin repeat domain-containing protein 62，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小917 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A6NC57
- Protein Atlas: https://www.proteinatlas.org/ENSG00000181626-ANKRD62/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ANKRD62
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A6NC57
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000181626-ANKRD62/subcellular

![](https://images.proteinatlas.org/59835/1942_E4_17_cr5d289f022c15f_red_green.jpg)
![](https://images.proteinatlas.org/59835/1942_E4_21_cr5db2e78d84683_red_green.jpg)
![](https://images.proteinatlas.org/59835/2019_B11_1_red_green.jpg)
![](https://images.proteinatlas.org/59835/2019_B11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A6NC57-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

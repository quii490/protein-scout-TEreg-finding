---
type: protein-evaluation
gene: "PLSCR2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PLSCR2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PLSCR2 |
| 蛋白名称 | Phospholipid scramblase 2 |
| 蛋白大小 | 297 aa / 33.5 kDa |
| UniProt ID | Q9NRY7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Endoplasmic reticulum, Vesicles; UniProt: Membrane; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 297 aa / 33.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR005552; Pfam: PF03803 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 1 partners; IntAct 14 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Endoplasmic reticulum, Vesicles | Supported |
| UniProt | Membrane; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- endoplasmic reticulum (GO:0005783)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 13 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. STAT3 Cooperates With Phospholipid Scramblase 2 to Suppress Type I Interferon Response.. *Frontiers in immunology*. PMID: 30158934
2. Comparative and integrative analysis of transcriptomic and epigenomic-wide DNA methylation changes in African American prostate cancer.. *Epigenetics*. PMID: 37279148
3. Epigenetic Study of Cohort of Monozygotic Twins With Hypertrophic Cardiomyopathy Due to MYBPC3 (Cardiac Myosin-Binding Protein C).. *Journal of the American Heart Association*. PMID: 39470061
4. Global gene expression analysis of the mouse colonic mucosa treated with azoxymethane and dextran sodium sulfate.. *BMC cancer*. PMID: 17506908
5. Effect of PP2A on p34SEI-1 expression in response to ionizing radiation in MCF-7 human breast cancer cells.. *International journal of oncology*. PMID: 21344158

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.9 |
| 高置信度残基 (pLDDT>90) 占比 | 36.7% |
| 置信残基 (pLDDT 70-90) 占比 | 18.9% |
| 中等置信 (pLDDT 50-70) 占比 | 13.1% |
| 低置信 (pLDDT<50) 占比 | 31.3% |
| 有序区域 (pLDDT>70) 占比 | 55.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=69.9），有序残基占 55.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR005552; Pfam: PF03803 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DEPDC4 | 0.400 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EP300 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| FAM221B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| LCE5A | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| LCE3A | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| AQP1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| POU4F2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| LCE3E | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| BSND | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| OTX1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| GNG13 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 1，IntAct interactions: 14
- 调控相关比例: 0 / 1 = 0%

**评价**: STRING 1 个预测互作，IntAct 14 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.9 + PDB: 无 | pLDDT=69.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane; Nucleus / Nucleoplasm; 额外: Endoplasmic reticulum, Vesicles | 一致 |
| PPI | STRING + IntAct | 1 + 14 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. PLSCR2 — Phospholipid scramblase 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小297 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=69.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NRY7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163746-PLSCR2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PLSCR2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NRY7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000163746-PLSCR2/subcellular

![](https://images.proteinatlas.org/51352/1937_F1_2_red_green.jpg)
![](https://images.proteinatlas.org/51352/1937_F1_3_red_green.jpg)
![](https://images.proteinatlas.org/51352/1954_G1_52_cr5df8f9ee87a48_red_green.jpg)
![](https://images.proteinatlas.org/51352/1954_G1_57_cr5df8f9ee8882e_red_green.jpg)
![](https://images.proteinatlas.org/51352/1976_E7_1_red_green.jpg)
![](https://images.proteinatlas.org/51352/1976_E7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NRY7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

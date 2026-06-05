---
type: protein-evaluation
gene: "CYP20A1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CYP20A1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CYP20A1 |
| 蛋白名称 | Cytochrome P450 family 20 subfamily A member 1 |
| 蛋白大小 | 470 aa / 53.4 kDa |
| UniProt ID | E9PHG5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Plasma membrane, Cell Junctions, Actin filaments; 额外: Nucleo; UniProt: 无注释 |
| 蛋白大小 | 10/10 | x1 | 10 | 470 aa / 53.4 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=29 篇 (≤40→8) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=79.4; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 11 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **109.0/180** | |
| **归一化总分** | | | **60.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cell Junctions, Actin filaments; 额外: Nucleoplasm | Uncertain |
| UniProt | 无注释 | Swiss-Prot/TremBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 29 |
| PubMed broad count | 31 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Unveiling Hepatic Protein Alterations in Neonatal and Infant Biliary Atresia.. *Clin Pharmacol Ther*. PMID: 41781340
2. An Episomal Clustered Regularly Interspaced Short Palindromic Repeats/Cas9 System for Transgene-Free Multiplex Gene Editing in Pig Cells.. *Biology (Basel)*. PMID: 42187704
3. Macula densa-specific NOS1 knockout determines susceptibility to ischemic acute kidney injury.. *Clin Sci (Lond)*. PMID: 41837645
4. MicroRNA-592 suppresses breast cancer progression by targeting CYP20A1 to modulate the CHOP pathway.. *J Physiol Biochem*. PMID: 41087653
5. Paracetamol metabolism by endothelial cells - Potential mechanism underlying intravenous paracetamol-induced hypotension.. *Pharmacol Res*. PMID: 39653302

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.4 |
| 高置信度残基 (pLDDT>90) 占比 | 35.3% |
| 置信残基 (pLDDT 70-90) 占比 | 40.0% |
| 中等置信 (pLDDT 50-70) 占比 | 13.2% |
| 低置信 (pLDDT<50) 占比 | 11.5% |
| 有序区域 (pLDDT>70) 占比 | 75.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=79.4，有序区 75.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CYP39A1 | 0.000 | 0.000 | — |
| CYP7A1 | 0.000 | 0.000 | — |
| HSD3B7 | 0.000 | 0.000 | — |
| GK5 | 0.000 | 0.000 | — |
| ICA1L | 0.000 | 0.000 | — |
| CYP7B1 | 0.000 | 0.000 | — |
| C17orf75 | 0.000 | 0.000 | — |
| OPA3 | 0.000 | 0.000 | — |
| AASDH | 0.000 | 0.000 | — |
| DCAF10 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q92508 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:- |
| uniprotkb:Q6UW02 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 11
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 11 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.4 + PDB: 无 | pLDDT=79.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Plasma membrane, Cell Junctions, Actin filaments;  | 待确认 |
| PPI | STRING + IntAct | 25 + 11 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CYP20A1 -- Cytochrome P450 family 20 subfamily A member 1，非常新颖，仅有少数基础研究。
2. 蛋白大小470 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 29 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/E9PHG5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000119004-CYP20A1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CYP20A1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/E9PHG5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (uncertain)。来源: https://www.proteinatlas.org/ENSG00000119004-CYP20A1/subcellular

![](https://images.proteinatlas.org/55872/1027_B1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/55872/1027_B1_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/55872/875_F11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/55872/875_F11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/55872/883_F11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/55872/883_F11_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-E9PHG5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

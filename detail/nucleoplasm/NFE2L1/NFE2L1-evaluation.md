---
type: protein-evaluation
gene: "NFE2L1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NFE2L1 — REJECTED (研究热度过高 (PubMed strict=142，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NFE2L1 / HBZ17, NRF1, TCF11 |
| 蛋白名称 | Endoplasmic reticulum membrane sensor NFE2L1 |
| 蛋白大小 | 772 aa / 84.7 kDa |
| UniProt ID | Q14494 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Endoplasmic reticulum membrane; Endoplasmic reticulum membra |
| 蛋白大小 | 10/10 | ×1 | 10 | 772 aa / 84.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=142 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=54.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR004827, IPR004826, IPR047167, IPR008917; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Endoplasmic reticulum membrane; Endoplasmic reticulum membrane; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- endoplasmic reticulum membrane (GO:0005789)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 142 |
| PubMed broad count | 272 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HBZ17, NRF1, TCF11 |

**关键文献**:
1. Cross-disorder and disease-specific pathways in dementia revealed by single-cell genomics.. *Cell*. PMID: 39265576
2. Sugar-mediated non-canonical ubiquitination impairs Nrf1/NFE2L1 activation.. *Molecular cell*. PMID: 39116872
3. Activating the NFE2L1-ubiquitin-proteasome system by DDI2 protects from ferroptosis.. *Cell death and differentiation*. PMID: 39384955
4. Nrf1 promotes heart regeneration and repair by regulating proteostasis and redox balance.. *Nature communications*. PMID: 34489413
5. Serum taurine affects lung cancer progression by regulating tumor immune escape mediated by the immune microenvironment.. *Journal of advanced research*. PMID: 39243941

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 54.8 |
| 高置信度残基 (pLDDT>90) 占比 | 13.9% |
| 置信残基 (pLDDT 70-90) 占比 | 13.7% |
| 中等置信 (pLDDT 50-70) 占比 | 15.3% |
| 低置信 (pLDDT<50) 占比 | 57.1% |
| 有序区域 (pLDDT>70) 占比 | 27.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=54.8），有序残基占 27.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004827, IPR004826, IPR047167, IPR008917; Pfam: PF03131 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MAFG | 0.998 | 0.842 | — |
| MAFF | 0.977 | 0.807 | — |
| MAF | 0.970 | 0.184 | — |
| MAFK | 0.955 | 0.319 | — |
| KEAP1 | 0.937 | 0.837 | — |
| PPARGC1A | 0.727 | 0.000 | — |
| DDI2 | 0.724 | 0.000 | — |
| HHAT | 0.697 | 0.000 | — |
| GCLC | 0.685 | 0.000 | — |
| NRF1 | 0.684 | 0.300 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| KEAP1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| TULP3 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| CD6 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| lysU | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| recC | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ENSP00000354855.3 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| A0A5P8YHX0 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| fadL | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| Cdk9 | psi-mi:"MI:0096"(pull down) | pubmed:20593818|imex:IM-17619 |
| FMR1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=54.8 + PDB: 无 | pLDDT=54.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Endoplasmic reticu / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. NFE2L1 — Endoplasmic reticulum membrane sensor NFE2L1，研究基础较多，新颖性有限。
2. 蛋白大小772 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 142 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=54.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 142 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q14494
- Protein Atlas: https://www.proteinatlas.org/ENSG00000082641-NFE2L1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NFE2L1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14494
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000082641-NFE2L1/subcellular

![](https://images.proteinatlas.org/63384/1151_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/63384/1151_C10_2_red_green.jpg)
![](https://images.proteinatlas.org/63384/1154_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/63384/1154_C10_2_red_green.jpg)
![](https://images.proteinatlas.org/63384/1238_A8_4_red_green.jpg)
![](https://images.proteinatlas.org/63384/1238_A8_5_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q14494-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

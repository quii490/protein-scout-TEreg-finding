---
type: protein-evaluation
gene: "GLRX2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GLRX2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GLRX2 / GRX2 |
| 蛋白名称 | Glutaredoxin-2, mitochondrial |
| 蛋白大小 | 164 aa / 18.1 kDa |
| UniProt ID | Q9NS18 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: Mitochondrion; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 164 aa / 18.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=31 篇 (≤40→8) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=82.1; PDB: 2CQ9, 2FLS, 2HT9 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR002109, IPR011899, IPR014025, IPR036249; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.0/180** | |
| **归一化总分** | | | **72.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Supported |
| UniProt | Mitochondrion; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- mitochondrion (GO:0005739)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 31 |
| PubMed broad count | 125 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GRX2 |

**关键文献**:
1. Uncovering novel protein pathways regulating bioavailable testosterone through sex hormone-binding globulin.. *Computational biology and chemistry*. PMID: 41161126
2. Glutaredoxin 2 is essential for AML survival through mitochondrial permeability transition pore regulation.. *Blood*. PMID: 41237364
3. From proteome to pathogenesis: investigating polycystic ovary syndrome with Mendelian randomization analysis.. *Frontiers in endocrinology*. PMID: 39314522
4. Mitochondrial Glrx2 Knockout Augments Acetaminophen-Induced Hepatotoxicity in Mice.. *Antioxidants (Basel, Switzerland)*. PMID: 36139718
5. Ablating the glutaredoxin-2 (Glrx2) gene protects male mice against non-alcoholic fatty liver disease (NAFLD) by limiting oxidative distress.. *Free radical biology & medicine*. PMID: 39278573

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.1 |
| 高置信度残基 (pLDDT>90) 占比 | 62.8% |
| 置信残基 (pLDDT 70-90) 占比 | 4.9% |
| 中等置信 (pLDDT 50-70) 占比 | 21.3% |
| 低置信 (pLDDT<50) 占比 | 11.0% |
| 有序区域 (pLDDT>70) 占比 | 67.7% |
| 可用 PDB 条目 | 2CQ9, 2FLS, 2HT9 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2CQ9, 2FLS, 2HT9）+ AlphaFold高质量预测（pLDDT=82.1），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002109, IPR011899, IPR014025, IPR036249; Pfam: PF00462 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GLRX3 | 0.879 | 0.100 | — |
| RRM1 | 0.842 | 0.412 | — |
| TXNRD2 | 0.820 | 0.077 | — |
| TXN | 0.808 | 0.065 | — |
| ACP1 | 0.805 | 0.000 | — |
| GSR | 0.798 | 0.070 | — |
| MSRA | 0.794 | 0.602 | — |
| GLRX5 | 0.768 | 0.000 | — |
| TXN2 | 0.763 | 0.050 | — |
| ITPA | 0.743 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SFXN1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| ELF5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| DCXR | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 3
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.1 + PDB: 2CQ9, 2FLS, 2HT9 | pLDDT=82.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Mitochondrion; Nucleus / Nucleoplasm; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 3 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. GLRX2 — Glutaredoxin-2, mitochondrial，非常新颖，仅有少数基础研究。
2. 蛋白大小164 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 31 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NS18
- Protein Atlas: https://www.proteinatlas.org/ENSG00000023572-GLRX2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GLRX2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NS18
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000023572-GLRX2/subcellular

![](https://images.proteinatlas.org/23087/215_C1_1_red_green.jpg)
![](https://images.proteinatlas.org/23087/215_C1_2_red_green.jpg)
![](https://images.proteinatlas.org/23087/216_C1_1_red_green.jpg)
![](https://images.proteinatlas.org/23087/216_C1_2_red_green.jpg)
![](https://images.proteinatlas.org/23087/217_C1_1_red_green.jpg)
![](https://images.proteinatlas.org/23087/217_C1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NS18-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NS18 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 57..157; /note="Glutaredoxin"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00686" |
| InterPro | IPR002109;IPR011899;IPR014025;IPR036249; |
| Pfam | PF00462; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000023572-GLRX2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DCXR | Intact | false |
| ELF5 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

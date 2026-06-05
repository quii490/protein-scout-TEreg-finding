---
type: protein-evaluation
gene: "MDC1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MDC1 — REJECTED (研究热度过高 (PubMed strict=339，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MDC1 / KIAA0170, NFBD1 |
| 蛋白名称 | Mediator of DNA damage checkpoint protein 1 |
| 蛋白大小 | 2089 aa / 226.7 kDa |
| UniProt ID | Q14676 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm, Nuclear bodies; UniProt: Nucleus; Chromosome |
| 蛋白大小 | 2/10 | ×1 | 2 | 2089 aa / 226.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=339 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=40.2; PDB: 2ADO, 2AZM, 2ETX, 3K05, 3UEO, 3UMZ, 3UN0 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001357, IPR036420, IPR051579, IPR000253, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear bodies | Supported |
| UniProt | Nucleus; Chromosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromosome (GO:0005694)
- focal adhesion (GO:0005925)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- site of double-strand break (GO:0035861)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 339 |
| PubMed broad count | 662 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0170, NFBD1 |

**关键文献**:
1. DNA damage response signaling pathways and targets for radiotherapy sensitization in cancer.. *Signal transduction and targeted therapy*. PMID: 32355263
2. MDC1 maintains active elongation complexes of RNA polymerase II.. *Cell reports*. PMID: 36640322
3. METTL16 is Required for Meiotic Sex Chromosome Inactivation and DSB Formation and Recombination during Male Meiosis.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 39607422
4. Mitotic tethering enables inheritance of shattered micronuclear chromosomes.. *Nature*. PMID: 37316668
5. The CIP2A-TOPBP1 complex safeguards chromosomal stability during mitosis.. *Nature communications*. PMID: 35842428

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 40.2 |
| 高置信度残基 (pLDDT>90) 占比 | 12.8% |
| 置信残基 (pLDDT 70-90) 占比 | 1.4% |
| 中等置信 (pLDDT 50-70) 占比 | 0.4% |
| 低置信 (pLDDT<50) 占比 | 85.3% |
| 有序区域 (pLDDT>70) 占比 | 14.2% |
| 可用 PDB 条目 | 2ADO, 2AZM, 2ETX, 3K05, 3UEO, 3UMZ, 3UN0, 3UNM, 3UNN, 3UOT |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=40.2），有序残基占 14.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001357, IPR036420, IPR051579, IPR000253, IPR008984; Pfam: PF16589, PF00498, PF16770 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ATM | 0.999 | 0.876 | — |
| H2AX | 0.999 | 0.933 | — |
| BRCA1 | 0.999 | 0.833 | — |
| RNF8 | 0.999 | 0.835 | — |
| TP53BP1 | 0.999 | 0.892 | — |
| RNF168 | 0.997 | 0.091 | — |
| UIMC1 | 0.997 | 0.778 | — |
| TOPBP1 | 0.995 | 0.891 | — |
| NBN | 0.994 | 0.928 | — |
| CHEK2 | 0.990 | 0.469 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Fer2LCH | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| Ten-m | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| TERF2IP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15383534 |
| NBN | psi-mi:"MI:0663"(confocal microscopy) | imex:IM-11889|pubmed:18001824 |
| H2AX | psi-mi:"MI:0663"(confocal microscopy) | imex:IM-11889|pubmed:18001824 |
| RNF8 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-11889|pubmed:18001824 |
| BRCA1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17525332|imex:IM-19727 |
| nbs1 | psi-mi:"MI:0065"(isothermal titration calorimetry) | imex:IM-12090|pubmed:19804756 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:19505873|imex:IM-20483 |
| CDK8 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=40.2 + PDB: 2ADO, 2AZM, 2ETX, 3K05, 3UEO,  | pLDDT=40.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome / Nucleoplasm, Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. MDC1 — Mediator of DNA damage checkpoint protein 1，研究基础较多，新颖性有限。
2. 蛋白大小2089 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 339 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=40.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 339 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q14676
- Protein Atlas: https://www.proteinatlas.org/ENSG00000137337-MDC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MDC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14676
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000137337-MDC1/subcellular

![](https://images.proteinatlas.org/6915/17_D12_1_red_green.jpg)
![](https://images.proteinatlas.org/6915/17_D12_2_red_green.jpg)
![](https://images.proteinatlas.org/6915/18_D12_1_red_green.jpg)
![](https://images.proteinatlas.org/6915/18_D12_2_red_green.jpg)
![](https://images.proteinatlas.org/6915/19_D12_1_red_green.jpg)
![](https://images.proteinatlas.org/6915/19_D12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q14676-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

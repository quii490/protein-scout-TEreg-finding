---
type: protein-evaluation
gene: "CLPTM1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CLPTM1 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CLPTM1 |
| 蛋白名称 | Putative lipid scramblase CLPTM1 |
| 蛋白大小 | 669 aa / 76.1 kDa |
| UniProt ID | O96005 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Endoplasmic reticulum; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 669 aa / 76.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=32 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR008429; Pfam: PF05602 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **100.0/180** | |
| **归一化总分** | | | **55.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- endomembrane system (GO:0012505)
- external side of plasma membrane (GO:0009897)
- membrane (GO:0016020)
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 32 |
| PubMed broad count | 49 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Haploinsufficiency of GABA(A) Receptor-Associated Clptm1 Enhances Phasic and Tonic Inhibitory Neurotransmission, Suppresses Excitatory Synaptic Plasticity, and Impairs Memory.. *The Journal of neuroscience : the official journal of the Society for Neuroscience*. PMID: 38942471
2. De novo CLPTM1 variants with reduced GABA(A) R current response in patients with epilepsy.. *Epilepsia*. PMID: 37577761
3. Comprehensive characterization of the RNA editing landscape in the human aging brains with Alzheimer's disease.. *Alzheimer's & dementia : the journal of the Alzheimer's Association*. PMID: 40631452
4. Long telomere length and a TERT-CLPTM1 locus polymorphism association with melanoma risk.. *European journal of cancer (Oxford, England : 1990)*. PMID: 25457634
5. Pathobiological role of cleft palate transmembrane protein 1 family proteins in oral squamous cell carcinoma.. *Journal of cancer research and clinical oncology*. PMID: 30635792

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.4 |
| 高置信度残基 (pLDDT>90) 占比 | 10.9% |
| 置信残基 (pLDDT 70-90) 占比 | 48.3% |
| 中等置信 (pLDDT 50-70) 占比 | 18.4% |
| 低置信 (pLDDT<50) 占比 | 22.4% |
| 有序区域 (pLDDT>70) 占比 | 59.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=69.4），有序残基占 59.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008429; Pfam: PF05602 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ITM2C | 0.620 | 0.000 | — |
| MTSS1 | 0.553 | 0.051 | — |
| HTRA1 | 0.549 | 0.000 | — |
| HM13 | 0.546 | 0.164 | — |
| UBAC2 | 0.528 | 0.163 | — |
| MAD1L1 | 0.526 | 0.477 | — |
| GLG1 | 0.524 | 0.000 | — |
| CEACAM19 | 0.510 | 0.000 | — |
| MAD2L1 | 0.488 | 0.487 | — |
| VAC14 | 0.446 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Q947H0 | psi-mi:"MI:0096"(pull down) | imex:IM-14965|pubmed:20217867 |
| pps | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| Unc93b1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21903422|imex:IM-17322 |
| 1C | psi-mi:"MI:0096"(pull down) | imex:IM-15828|pubmed:22593156 |
| STT3B | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| TCTN2 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| LMAN1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| HSCB | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28380382|imex:IM-25655 |
| ERGIC3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ASIC4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.4 + PDB: 无 | pLDDT=69.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Endoplasmic reticulum | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CLPTM1 — Putative lipid scramblase CLPTM1，非常新颖，仅有少数基础研究。
2. 蛋白大小669 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 32 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=69.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O96005
- Protein Atlas: https://www.proteinatlas.org/ENSG00000104853-CLPTM1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CLPTM1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O96005
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Endoplasmic reticulum (approved)。来源: https://www.proteinatlas.org/ENSG00000104853-CLPTM1/subcellular

![](https://images.proteinatlas.org/68767/1310_C11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/68767/1310_C11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/68767/1312_C11_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/68767/1312_C11_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/68767/1482_B11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/68767/1482_B11_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O96005-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

---
type: protein-evaluation
gene: "ERO1A"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ERO1A — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ERO1A / ERO1L |
| 蛋白名称 | ERO1-like protein alpha |
| 蛋白大小 | 468 aa / 54.4 kDa |
| UniProt ID | Q96HE7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Endoplasmic reticulum membrane; Golgi apparatus lumen; Secre |
| 蛋白大小 | 10/10 | ×1 | 10 | 468 aa / 54.4 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=47 篇 (≤60→6) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=75.7; PDB: 3AHQ, 3AHR |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR007266, IPR037192; Pfam: PF04137 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **100.0/180** | |
| **归一化总分** | | | **55.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Endoplasmic reticulum membrane; Golgi apparatus lumen; Secreted; Cell projection, dendrite | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- dendrite (GO:0030425)
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum lumen (GO:0005788)
- endoplasmic reticulum membrane (GO:0005789)
- extracellular space (GO:0005615)
- Golgi lumen (GO:0005796)
- intracellular membrane-bounded organelle (GO:0043231)
- membrane (GO:0016020)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 47 |
| PubMed broad count | 193 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ERO1L |

**关键文献**:
1. Ablation of ERO1A induces lethal endoplasmic reticulum stress responses and immunogenic cell death to activate anti-tumor immunity.. *Cell reports. Medicine*. PMID: 37769655
2. SEPN1-related myopathy depends on the oxidoreductase ERO1A and is druggable with the chemical chaperone TUDCA.. *Cell reports. Medicine*. PMID: 38402623
3. Ero1a, the most strongly hypoxia-induced protein in PASMCs, promotes the development of hypoxia- and monocrotaline-induced pulmonary hypertension in rats.. *Life sciences*. PMID: 40414553
4. Inhibition of ERO1a and IDO1 improves dendritic cell infiltration into pancreatic ductal adenocarcinoma.. *Frontiers in immunology*. PMID: 38187398
5. Paraoxonase-like APMAP maintains endoplasmic-reticulum-associated lipid and lipoprotein homeostasis.. *Developmental cell*. PMID: 40318637

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.7 |
| 高置信度残基 (pLDDT>90) 占比 | 35.0% |
| 置信残基 (pLDDT 70-90) 占比 | 32.9% |
| 中等置信 (pLDDT 50-70) 占比 | 14.1% |
| 低置信 (pLDDT<50) 占比 | 17.9% |
| 有序区域 (pLDDT>70) 占比 | 67.9% |
| 可用 PDB 条目 | 3AHQ, 3AHR |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3AHQ, 3AHR）+ AlphaFold高质量预测（pLDDT=75.7），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007266, IPR037192; Pfam: PF04137 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ERP44 | 0.997 | 0.475 | — |
| P4HB | 0.996 | 0.839 | — |
| PDIA4 | 0.984 | 0.584 | — |
| TXNDC5 | 0.976 | 0.130 | — |
| PDIA6 | 0.961 | 0.130 | — |
| ERO1B | 0.961 | 0.606 | — |
| ERP29 | 0.956 | 0.000 | — |
| HSPA5 | 0.875 | 0.263 | — |
| PDIA2 | 0.847 | 0.722 | — |
| GPX8 | 0.846 | 0.230 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Hnrnpk | psi-mi:"MI:0096"(pull down) | pubmed:16518874|imex:IM-11840 |
| PELI2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| Q947H0 | psi-mi:"MI:0096"(pull down) | imex:IM-14965|pubmed:20217867 |
| ATF2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:22304920|imex:IM-17307 |
| Slc2a4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:16396496|mint:MINT-5218 |
| H2AX | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20000738|imex:IM-19572 |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |
| FBXO6 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| TANK | psi-mi:"MI:2289"(virotrap) | pubmed:30561431|imex:IM-26500 |
| TNIK | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.7 + PDB: 3AHQ, 3AHR | pLDDT=75.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Golgi apparatus lu / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. ERO1A — ERO1-like protein alpha，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小468 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 47 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96HE7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000197930-ERO1A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ERO1A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96HE7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96HE7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

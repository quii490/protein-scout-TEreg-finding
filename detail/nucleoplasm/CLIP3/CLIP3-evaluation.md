---
type: protein-evaluation
gene: "CLIP3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CLIP3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CLIP3 / CLIPR59 |
| 蛋白名称 | CAP-Gly domain-containing linker protein 3 |
| 蛋白大小 | 547 aa / 59.6 kDa |
| UniProt ID | Q96DZ5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: 暂无HPA定位数据; UniProt: Cell membrane; Cytoplasm; Golgi apparatus, Golgi stack |
| 蛋白大小 | 10/10 | ×1 | 10 | 547 aa / 59.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=74.9; PDB: 2CP0 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR002110, IPR036770, IPR036859, IPR000938; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 10 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **125.0/180** | |
| **归一化总分** | | | **69.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell membrane; Cytoplasm; Golgi apparatus, Golgi stack | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cell cortex (GO:0005938)
- cytosol (GO:0005829)
- early endosome membrane (GO:0031901)
- Golgi stack (GO:0005795)
- membrane raft (GO:0045121)
- microtubule plus-end (GO:0035371)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 19 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CLIPR59 |

**关键文献**:
1. miRNA-mediated loss of m6A increases nascent translation in glioblastoma.. *PLoS genetics*. PMID: 33684100
2. Changes in CLIP3 expression after sciatic nerve injury in adult rats.. *Journal of molecular histology*. PMID: 23014974
3. Quercetin through miR-147-5p/Clip3 axis reducing Th17 cell differentiation to alleviate periodontitis.. *Regenerative therapy*. PMID: 38756701
4. Effect of CLIP3 Upregulation on Astrocyte Proliferation and Subsequent Glial Scar Formation in the Rat Spinal Cord via STAT3 Pathway After Injury.. *Journal of molecular neuroscience : MN*. PMID: 29218499
5. Carbon Dots from Lycium barbarum Attenuate Radiation-Induced Bone Injury by Inhibiting Senescence via METTL3/Clip3 in an m(6)A-Dependent Manner.. *ACS applied materials & interfaces*. PMID: 37088945

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.9 |
| 高置信度残基 (pLDDT>90) 占比 | 42.8% |
| 置信残基 (pLDDT 70-90) 占比 | 24.7% |
| 中等置信 (pLDDT 50-70) 占比 | 9.0% |
| 低置信 (pLDDT<50) 占比 | 23.6% |
| 有序区域 (pLDDT>70) 占比 | 67.5% |
| 可用 PDB 条目 | 2CP0 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=74.9，有序区 67.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002110, IPR036770, IPR036859, IPR000938; Pfam: PF12796, PF01302 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CYLD | 0.920 | 0.510 | — |
| RIPK1 | 0.676 | 0.294 | — |
| TNFRSF1A | 0.650 | 0.292 | — |
| ANK2 | 0.566 | 0.000 | — |
| ANK1 | 0.533 | 0.000 | — |
| BIRC2 | 0.532 | 0.059 | — |
| ANK3 | 0.528 | 0.000 | — |
| BIRC3 | 0.516 | 0.059 | — |
| XIAP | 0.516 | 0.059 | — |
| TNF | 0.514 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FMR1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| PB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28611246|imex:IM-25425 |
| CEP83 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TLE5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| GOLGA2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| WFS1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| KIF1B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| RNF11 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| HSPB1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| GRN | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:32814053|imex:IM-28217| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 10
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 10 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.9 + PDB: 2CP0 | pLDDT=74.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane; Cytoplasm; Golgi apparatus, Golgi s / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 10 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CLIP3 — CAP-Gly domain-containing linker protein 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小547 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96DZ5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000105270-CLIP3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CLIP3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96DZ5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96DZ5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

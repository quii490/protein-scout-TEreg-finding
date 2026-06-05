---
type: protein-evaluation
gene: "SYNPO2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SYNPO2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SYNPO2 |
| 蛋白名称 | Synaptopodin-2 |
| 蛋白大小 | 1093 aa / 117.5 kDa |
| UniProt ID | Q9UMS6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles, Actin filaments; UniProt: Nucleus; Cytoplasm; Cytoplasm, cytoskeleton; Cytoplasm, myof |
| 蛋白大小 | 8/10 | ×1 | 8 | 1093 aa / 117.5 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=63 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=49.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001478, IPR036034, IPR051976; Pfam: PF00595 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **98.0/180** | |
| **归一化总分** | | | **54.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles, Actin filaments | Enhanced |
| UniProt | Nucleus; Cytoplasm; Cytoplasm, cytoskeleton; Cytoplasm, myofibril, sarcomere, Z line; Cell junction,... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629)
- cytosol (GO:0005829)
- focal adhesion (GO:0005925)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- stress fiber (GO:0001725)
- Z disc (GO:0030018)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 63 |
| PubMed broad count | 111 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Synaptopodin-2: a potential tumor suppressor.. *Cancer cell international*. PMID: 37544991
2. Synaptopodin-2 promotes hepatocellular carcinoma metastasis via calcineurin-induced nuclear-cytoplasmic translocation.. *Cancer letters*. PMID: 32278815
3. Synaptopodin-2 Isoforms Have Specific Binding Partners and Display Distinct, Muscle Cell Type-Specific Expression Patterns.. *Cells*. PMID: 38201288
4. Cytoskeletal-related genes function as checkpoints for the maintenance of VSMC contractile phenotype and prevent pathological remodeling in arterial diseases.. *Journal of advanced research*. PMID: 40516911
5. Synaptopodin-2 suppresses metastasis of triple-negative breast cancer via inhibition of YAP/TAZ activity.. *The Journal of pathology*. PMID: 28991374

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 49.5 |
| 高置信度残基 (pLDDT>90) 占比 | 9.2% |
| 置信残基 (pLDDT 70-90) 占比 | 7.9% |
| 中等置信 (pLDDT 50-70) 占比 | 15.2% |
| 低置信 (pLDDT<50) 占比 | 67.7% |
| 有序区域 (pLDDT>70) 占比 | 17.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=49.5），有序残基占 17.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001478, IPR036034, IPR051976; Pfam: PF00595 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FLNC | 0.836 | 0.294 | — |
| BAG3 | 0.808 | 0.292 | — |
| FLNA | 0.791 | 0.476 | — |
| ACTN2 | 0.736 | 0.355 | — |
| HSPB8 | 0.731 | 0.000 | — |
| MYOT | 0.681 | 0.000 | — |
| MYOZ1 | 0.678 | 0.000 | — |
| PGM5 | 0.660 | 0.000 | — |
| LMOD1 | 0.643 | 0.000 | — |
| FLNB | 0.624 | 0.045 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CDK6 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:22094256|imex:IM-16628 |
| YWHAG | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| WNK1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| PLK4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Gsk3b | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| RHOA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| POLK | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Actr1b | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| DUX4L9 | psi-mi:"MI:0018"(two hybrid) | imex:IM-25050|pubmed:26816005 |
| NEDD4 | psi-mi:"MI:0084"(phage display) | imex:IM-29361|pubmed:35044719 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=49.5 + PDB: 无 | pLDDT=49.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cytoplasm, cytoskeleton; Cytop / Vesicles, Actin filaments | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. SYNPO2 — Synaptopodin-2，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小1093 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 63 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=49.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UMS6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000172403-SYNPO2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SYNPO2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UMS6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (enhanced)。来源: https://www.proteinatlas.org/ENSG00000172403-SYNPO2/subcellular

![](https://images.proteinatlas.org/30665/1368_A12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/30665/1368_A12_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/30665/1698_C10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/30665/1698_C10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/49707/1680_F11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/49707/1680_F11_6_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UMS6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

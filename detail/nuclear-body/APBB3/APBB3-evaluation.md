---
type: protein-evaluation
gene: "APBB3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## APBB3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | APBB3 / FE65L2 |
| 蛋白名称 | Amyloid-beta A4 precursor protein-binding family B member 3 |
| 蛋白大小 | 486 aa / 52.6 kDa |
| UniProt ID | O95704 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear bodies, Actin filaments; 额外: Cytosol; UniProt: Cytoplasm; Nucleus; Nucleus; Nucleus |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 486 aa / 52.6 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.5; PDB: 2DYQ, 2YSC |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039576, IPR011993, IPR006020, IPR001202, IPR036 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.5/180** | |
| **归一化总分** | | | **72.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies, Actin filaments; 额外: Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus; Nucleus; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 图像状态: if_display_images_available。

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- membrane (GO:0016020)
- nuclear body (GO:0016604)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 13 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FE65L2 |

**关键文献**:
1. Selection in Australian Thoroughbred horses acts on a locus associated with early two-year old speed.. *PloS one*. PMID: 32049967
2. Integration of Alzheimer's disease genetics and myeloid genomics identifies disease risk regulatory elements and genes.. *Nature communications*. PMID: 33712570
3. Fe65 is the sole member of its family that mediates transcription regulated by the amyloid precursor protein.. *Journal of cell science*. PMID: 32843577
4. Convergence of genes implicated in Alzheimer's disease on the cerebral cholesterol shuttle: APP, cholesterol, lipoproteins, and atherosclerosis.. *Neurochemistry international*. PMID: 16973241
5. Inflammation and neurological disease-related genes are differentially expressed in depressed patients with mood disorders and correlate with morphometric and functional imaging abnormalities.. *Brain, behavior, and immunity*. PMID: 23064081

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.5 |
| 高置信度残基 (pLDDT>90) 占比 | 20.6% |
| 置信残基 (pLDDT 70-90) 占比 | 31.7% |
| 中等置信 (pLDDT 50-70) 占比 | 8.8% |
| 低置信 (pLDDT<50) 占比 | 38.9% |
| 有序区域 (pLDDT>70) 占比 | 52.3% |
| 可用 PDB 条目 | 2DYQ, 2YSC |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=64.5），有序残基占 52.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039576, IPR011993, IPR006020, IPR001202, IPR036020; Pfam: PF00640, PF00397 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| APP | 0.984 | 0.802 | — |
| APLP2 | 0.803 | 0.650 | — |
| APLP1 | 0.796 | 0.640 | — |
| RHOBTB1 | 0.716 | 0.715 | — |
| COPS4 | 0.702 | 0.702 | — |
| COPS5 | 0.694 | 0.694 | — |
| COPS2 | 0.680 | 0.680 | — |
| COPS7A | 0.677 | 0.670 | — |
| COPS7B | 0.676 | 0.670 | — |
| COPS6 | 0.665 | 0.665 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| App | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:9461550 |
| APLP2 | psi-mi:"MI:0018"(two hybrid) | pubmed:9461550 |
| RAB4A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| RBM14 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RHOBTB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| UBB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| BLK | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| APLP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| COPS2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HGFAC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.5 + PDB: 2DYQ, 2YSC | pLDDT=64.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Nucleus; Nucleus / Nuclear bodies, Actin filaments; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ 

**核心优势**:
1. APBB3 — Amyloid-beta A4 precursor protein-binding family B member 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小486 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=64.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O95704
- Protein Atlas: https://www.proteinatlas.org/ENSG00000113108-APBB3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=APBB3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95704
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 02:58:37

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (supported)。来源: https://www.proteinatlas.org/ENSG00000113108-APBB3/subcellular

![](https://images.proteinatlas.org/5571/2144_A3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/5571/2144_A3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/5571/2189_D2_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/5571/2189_D2_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/5571/73_B9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/5571/73_B9_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O95704-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

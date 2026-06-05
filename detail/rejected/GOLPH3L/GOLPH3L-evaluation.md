---
type: protein-evaluation
gene: "GOLPH3L"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GOLPH3L — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GOLPH3L / GPP34R |
| 蛋白名称 | Golgi phosphoprotein 3-like |
| 蛋白大小 | 285 aa / 32.8 kDa |
| UniProt ID | Q9H4A5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Golgi apparatus; 额外: Cytosol; UniProt: Golgi apparatus, Golgi stack membrane; Golgi apparatus, tran |
| 蛋白大小 | 10/10 | ×1 | 10 | 285 aa / 32.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=84.9; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR008628, IPR038261; Pfam: PF05719 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **115.5/180** | |
| **归一化总分** | | | **64.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Cytosol | Supported |
| UniProt | Golgi apparatus, Golgi stack membrane; Golgi apparatus, trans-Golgi network membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- Golgi apparatus (GO:0005794)
- Golgi cisterna (GO:0031985)
- Golgi cisterna membrane (GO:0032580)
- Golgi membrane (GO:0000139)
- trans-Golgi network (GO:0005802)
- trans-Golgi network membrane (GO:0032588)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 20 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GPP34R |

**关键文献**:
1. GOLPH3 and GOLPH3L maintain Golgi localization of LYSET and a functional mannose 6-phosphate transport pathway.. *The EMBO journal*. PMID: 39587297
2. Independent duplications of the Golgi phosphoprotein 3 oncogene in birds.. *Scientific reports*. PMID: 34127736
3. The Role of GOLPH3L in the Prognosis and NACT response in Cervical Cancer.. *Journal of Cancer*. PMID: 28261346
4. GOLPH3L is a Novel Prognostic Biomarker for Epithelial Ovarian Cancer.. *Journal of Cancer*. PMID: 26284141
5. The miR-1185-2-3p-GOLPH3L pathway promotes glucose metabolism in breast cancer by stabilizing p53-induced SERPINE1.. *Journal of experimental & clinical cancer research : CR*. PMID: 33509226

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.9 |
| 高置信度残基 (pLDDT>90) 占比 | 71.2% |
| 置信残基 (pLDDT 70-90) 占比 | 11.9% |
| 中等置信 (pLDDT 50-70) 占比 | 2.5% |
| 低置信 (pLDDT<50) 占比 | 14.4% |
| 有序区域 (pLDDT>70) 占比 | 83.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=84.9，有序区 83.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008628, IPR038261; Pfam: PF05719 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PCSK9 | 0.864 | 0.818 | — |
| MYO18A | 0.778 | 0.073 | — |
| ARCN1 | 0.672 | 0.411 | — |
| HORMAD1 | 0.629 | 0.000 | — |
| PI4KB | 0.555 | 0.000 | — |
| GALNT2 | 0.554 | 0.000 | — |
| RAB1A | 0.539 | 0.152 | — |
| COPA | 0.478 | 0.432 | — |
| DNAJB5 | 0.470 | 0.078 | — |
| ST6GAL1 | 0.469 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| HTT | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-17394|pubmed:23275563 |
| LNX1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | imex:IM-23318|pubmed:25416956 |
| SLC39A5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| C5AR2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PNKD | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RWDD2B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GPRC5C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TNFRSF8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GLB1L2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.9 + PDB: 无 | pLDDT=84.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus, Golgi stack membrane; Golgi appar / Golgi apparatus; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GOLPH3L — Golgi phosphoprotein 3-like，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小285 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H4A5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000143457-GOLPH3L/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GOLPH3L
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H4A5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (supported)。来源: https://www.proteinatlas.org/ENSG00000143457-GOLPH3L/subcellular

![](https://images.proteinatlas.org/72016/1872_E3_27_cr5b50524d86a86_blue_red_green.jpg)
![](https://images.proteinatlas.org/72016/1872_E3_7_cr5b50524d8657a_blue_red_green.jpg)
![](https://images.proteinatlas.org/72016/1925_E9_1_cr5cd561ee955f5_blue_red_green.jpg)
![](https://images.proteinatlas.org/72016/1925_E9_7_cr5cd561ee95db1_blue_red_green.jpg)
![](https://images.proteinatlas.org/72016/1935_D7_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/72016/1935_D7_5_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H4A5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

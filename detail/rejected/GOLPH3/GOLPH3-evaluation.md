---
type: protein-evaluation
gene: "GOLPH3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GOLPH3 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GOLPH3 / GPP34 |
| 蛋白名称 | Golgi phosphoprotein 3 |
| 蛋白大小 | 298 aa / 33.8 kDa |
| UniProt ID | Q9H4A6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Golgi apparatus, Vesicles; UniProt: Golgi apparatus, Golgi stack membrane; Golgi apparatus, tran |
| 蛋白大小 | 10/10 | ×1 | 10 | 298 aa / 33.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=83.4; PDB: 3KN1 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR008628, IPR038261; Pfam: PF05719 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119.0/180** | |
| **归一化总分** | | | **66.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus, Vesicles | Supported |
| UniProt | Golgi apparatus, Golgi stack membrane; Golgi apparatus, trans-Golgi network membrane; Mitochondrion ... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- endosome (GO:0005768)
- Golgi apparatus (GO:0005794)
- Golgi cisterna (GO:0031985)
- Golgi cisterna membrane (GO:0032580)
- Golgi membrane (GO:0000139)
- mitochondrial intermembrane space (GO:0005758)
- mitochondrion (GO:0005739)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) | 无 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.4 |
| 高置信度残基 (pLDDT>90) 占比 | 68.5% |
| 置信残基 (pLDDT 70-90) 占比 | 11.4% |
| 中等置信 (pLDDT 50-70) 占比 | 3.0% |
| 低置信 (pLDDT<50) 占比 | 17.1% |
| 有序区域 (pLDDT>70) 占比 | 79.9% |
| 可用 PDB 条目 | 3KN1 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=83.4，有序区 79.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008628, IPR038261; Pfam: PF05719 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MYO18A | 0.971 | 0.526 | — |
| SEC24B | 0.949 | 0.000 | — |
| ARF1 | 0.944 | 0.138 | — |
| COPB1 | 0.922 | 0.254 | — |
| PPEF1 | 0.920 | 0.000 | — |
| CD4 | 0.905 | 0.000 | — |
| GOLGA2 | 0.902 | 0.000 | — |
| PCSK9 | 0.889 | 0.818 | — |
| ARCN1 | 0.887 | 0.411 | — |
| SEC13 | 0.862 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| sau | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| vpr | psi-mi:"MI:0096"(pull down) | imex:IM-17346|pubmed:22190034| |
| Ywhaz | psi-mi:"MI:0028"(cosedimentation in solution) | imex:IM-11648|pubmed:19562802 |
| EBI-2465282 | psi-mi:"MI:0049"(filter binding) | imex:IM-12096|pubmed:19837035 |
| MYO18A | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12096|pubmed:19837035 |
| TGOLN2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| RCC1L | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GMPPA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TSR3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.4 + PDB: 3KN1 | pLDDT=83.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Golgi apparatus, Golgi stack membrane; Golgi appar / Golgi apparatus, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GOLPH3 — Golgi phosphoprotein 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小298 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H4A6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000113384-GOLPH3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GOLPH3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H4A6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (supported)。来源: https://www.proteinatlas.org/ENSG00000113384-GOLPH3/subcellular

![](https://images.proteinatlas.org/55841/879_D11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/55841/879_D11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/55841/893_E10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/55841/893_E10_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/55841/895_E10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/55841/895_E10_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H4A6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

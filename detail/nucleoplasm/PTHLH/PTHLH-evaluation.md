---
type: protein-evaluation
gene: "PTHLH"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PTHLH — REJECTED (研究热度过高 (PubMed strict=207，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PTHLH / PTHRP |
| 蛋白名称 | Parathyroid hormone-related protein |
| 蛋白大小 | 177 aa / 20.2 kDa |
| UniProt ID | P12272 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; 额外: Golgi apparatus; UniProt: Secreted; Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 177 aa / 20.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=207 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.9; PDB: 1BZG, 1M5N, 3FFD, 3H3G, 7UZO, 7UZP, 7VVJ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003626, IPR001415; Pfam: PF01279 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.5/180** | |
| **归一化总分** | | | **44.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Golgi apparatus | Supported |
| UniProt | Secreted; Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular region (GO:0005576)
- extracellular space (GO:0005615)
- Golgi apparatus (GO:0005794)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 207 |
| PubMed broad count | 1490 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PTHRP |

**关键文献**:
1. Regulation of Proliferation, Differentiation and Functions of Osteoblasts by Runx2.. *International journal of molecular sciences*. PMID: 30987410
2. Targeting of HIF2-driven cachexia in kidney cancer.. *Nature medicine*. PMID: 41315757
3. Functional and molecular characterisation of EO771.LMB tumours, a new C57BL/6-mouse-derived model of spontaneously metastatic mammary cancer.. *Disease models & mechanisms*. PMID: 25633981
4. HIF-2-Dependent Regulation of PTHrP and Paraneoplastic Hypercalcemia in Aggressive Clear-Cell Renal Cell Carcinoma.. *Cancer discovery*. PMID: 41065553
5. Proliferative behaviours of CD90-expressing chondrocytes under the control of the TSC1-mTOR/PTHrP-nuclear localisation segment pathway.. *Osteoarthritis and cartilage*. PMID: 39730094

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.9 |
| 高置信度残基 (pLDDT>90) 占比 | 15.8% |
| 置信残基 (pLDDT 70-90) 占比 | 12.4% |
| 中等置信 (pLDDT 50-70) 占比 | 50.3% |
| 低置信 (pLDDT<50) 占比 | 21.5% |
| 有序区域 (pLDDT>70) 占比 | 28.2% |
| 可用 PDB 条目 | 1BZG, 1M5N, 3FFD, 3H3G, 7UZO, 7UZP, 7VVJ, 8D51, 8D52, 8FLR |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=62.9），有序残基占 28.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003626, IPR001415; Pfam: PF01279 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PTH1R | 0.999 | 0.967 | — |
| PTH | 0.999 | 0.000 | — |
| KPNB1 | 0.978 | 0.960 | — |
| PTH2R | 0.975 | 0.218 | — |
| IHH | 0.956 | 0.000 | — |
| GNAS | 0.928 | 0.800 | — |
| IGHV3-16 | 0.800 | 0.800 | — |
| GNB1 | 0.800 | 0.800 | — |
| GNG2 | 0.800 | 0.800 | — |
| FGF2 | 0.784 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PLK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12200|pubmed:19596235 |
| PTH1R | psi-mi:"MI:0905"(amplified luminescent proximity h | pubmed:19674967|imex:IM-26820 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.9 + PDB: 1BZG, 1M5N, 3FFD, 3H3G, 7UZO,  | pLDDT=62.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Secreted; Cytoplasm; Nucleus / Nucleoplasm, Cytosol; 额外: Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

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
1. PTHLH — Parathyroid hormone-related protein，研究基础较多，新颖性有限。
2. 蛋白大小177 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 207 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=62.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 207 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P12272
- Protein Atlas: https://www.proteinatlas.org/ENSG00000087494-PTHLH/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PTHLH
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P12272
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000087494-PTHLH/subcellular

![](https://images.proteinatlas.org/35982/469_A1_2_red_green.jpg)
![](https://images.proteinatlas.org/35982/469_A1_3_red_green.jpg)
![](https://images.proteinatlas.org/35982/472_A1_1_red_green.jpg)
![](https://images.proteinatlas.org/35982/472_A1_2_red_green.jpg)
![](https://images.proteinatlas.org/35982/476_A1_1_red_green.jpg)
![](https://images.proteinatlas.org/35982/476_A1_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P12272-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P12272 |
| SMART | SM00087; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR003626;IPR001415; |
| Pfam | PF01279; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000087494-PTHLH/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PTH1R | Intact, Biogrid | true |
| ARRB1 | Biogrid | false |
| KPNB1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

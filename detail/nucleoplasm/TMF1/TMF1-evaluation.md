---
type: protein-evaluation
gene: "TMF1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TMF1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TMF1 / ARA160 |
| 蛋白名称 | TATA element modulatory factor |
| 蛋白大小 | 1093 aa / 122.8 kDa |
| UniProt ID | P82094 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Golgi apparatus; UniProt: Cytoplasm; Nucleus; Golgi apparatus membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 1093 aa / 122.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR052602, IPR022092, IPR022091; Pfam: PF12329, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus | Supported |
| UniProt | Cytoplasm; Nucleus; Golgi apparatus membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- endoplasmic reticulum (GO:0005783)
- Golgi apparatus (GO:0005794)
- Golgi membrane (GO:0000139)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 44 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ARA160 |

**关键文献**:
1. TMF1 is upregulated by insulin and is required for a sustained glucose homeostasis.. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology*. PMID: 33475194
2. The plasma peptides of sepsis.. *Clinical proteomics*. PMID: 32636717
3. Sodium acetate promotes fat synthesis by suppressing TATA element modulatory factor 1 in bovine mammary epithelial cells.. *Animal nutrition (Zhongguo xu mu shou yi xue hui)*. PMID: 37123620
4. The Warburg micro syndrome protein RAB3GAP1 modulates neuronal morphogenesis and interacts with axon elongation end ER-Golgi trafficking factors.. *Neurobiology of disease*. PMID: 37385458
5. Acute COG complex inactivation unveiled its immediate impact on Golgi and illuminated the nature of intra-Golgi recycling vesicles.. *Traffic (Copenhagen, Denmark)*. PMID: 36468177

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.9 |
| 高置信度残基 (pLDDT>90) 占比 | 36.1% |
| 置信残基 (pLDDT 70-90) 占比 | 14.7% |
| 中等置信 (pLDDT 50-70) 占比 | 5.9% |
| 低置信 (pLDDT<50) 占比 | 43.3% |
| 有序区域 (pLDDT>70) 占比 | 50.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=64.9），有序残基占 50.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052602, IPR022092, IPR022091; Pfam: PF12329, PF12325 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RAB6A | 0.928 | 0.136 | — |
| RAB6B | 0.839 | 0.136 | — |
| ANKAR | 0.820 | 0.000 | — |
| GOLGA4 | 0.795 | 0.000 | — |
| GCC2 | 0.782 | 0.088 | — |
| GCC1 | 0.729 | 0.000 | — |
| VPS54 | 0.725 | 0.000 | — |
| GOLGA1 | 0.720 | 0.095 | — |
| OSGEPL1 | 0.671 | 0.000 | — |
| TGOLN2 | 0.656 | 0.120 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GFI1B | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| PLK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12200|pubmed:19596235 |
| E2 | psi-mi:"MI:0018"(two hybrid) | pubmed:18305892|imex:IM-19324 |
| NR3C1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:20195357|imex:IM-20475 |
| A0A380PNP6 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| PDHA1 | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010 |
| TCP10L2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TGOLN2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| CEBPZ | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.9 + PDB: 无 | pLDDT=64.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Golgi apparatus membrane / Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TMF1 — TATA element modulatory factor，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1093 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=64.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P82094
- Protein Atlas: https://www.proteinatlas.org/ENSG00000144747-TMF1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TMF1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P82094
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (supported)。来源: https://www.proteinatlas.org/ENSG00000144747-TMF1/subcellular

![](https://images.proteinatlas.org/8729/41_G10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/8729/41_G10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/8729/42_G10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/8729/42_G10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/8729/43_G10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/8729/43_G10_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P82094-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P82094 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR052602;IPR022092;IPR022091; |
| Pfam | PF12329;PF12325; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000144747-TMF1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AR | Biogrid | false |
| FER | Biogrid | false |
| NR3C1 | Intact | false |
| PLK1 | Biogrid | false |
| RAB11A | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

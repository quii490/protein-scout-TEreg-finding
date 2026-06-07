---
type: protein-evaluation
gene: "CSTB"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CSTB — REJECTED (研究热度过高 (PubMed strict=183，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CSTB / CST6, STFB |
| 蛋白名称 | Cystatin-B |
| 蛋白大小 | 98 aa / 11.1 kDa |
| UniProt ID | P04080 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli, Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 5/10 | ×1 | 5 | 98 aa / 11.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=183 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=95.5; PDB: 1STF, 2OCT, 4N6V |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000010, IPR046350, IPR018073, IPR001713; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.0/180** | |
| **归一化总分** | | | **48.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- extracellular matrix (GO:0031012)
- extracellular region (GO:0005576)
- extracellular space (GO:0005615)
- ficolin-1-rich granule lumen (GO:1904813)
- nucleolus (GO:0005730)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 183 |
| PubMed broad count | 640 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CST6, STFB |

**关键文献**:
1. Identification of the shared gene signatures and pathways between sarcopenia and type 2 diabetes mellitus.. *PloS one*. PMID: 35271662
2. Unverricht-Lundborg disease.. *Epileptic disorders : international epilepsy journal with videotape*. PMID: 27582036
3. Cystatin B increases autophagic flux by sustaining proteolytic activity of cathepsin B and fuels glycolysis in pancreatic cancer: CSTB orchestrates autophagy and glycolysis in PDAC.. *Clinical and translational medicine*. PMID: 36495123
4. Progressive Myoclonus Epilepsy: Unverricht-Lundborg Disease.. **. PMID: 39637163
5. CSTB gene replacement improves neuroinflammation, neurodegeneration and ataxia in murine type 1 progressive myoclonus epilepsy.. *Gene therapy*. PMID: 38135787

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 95.5 |
| 高置信度残基 (pLDDT>90) 占比 | 94.9% |
| 置信残基 (pLDDT 70-90) 占比 | 2.0% |
| 中等置信 (pLDDT 50-70) 占比 | 2.0% |
| 低置信 (pLDDT<50) 占比 | 1.0% |
| 有序区域 (pLDDT>70) 占比 | 96.9% |
| 可用 PDB 条目 | 1STF, 2OCT, 4N6V |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1STF, 2OCT, 4N6V）+ AlphaFold高质量预测（pLDDT=95.5），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000010, IPR046350, IPR018073, IPR001713; Pfam: PF00031 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CTSL | 0.954 | 0.576 | — |
| CTSB | 0.948 | 0.626 | — |
| CTSS | 0.904 | 0.044 | — |
| RRP1B | 0.880 | 0.000 | — |
| CST3 | 0.855 | 0.292 | — |
| NHLRC1 | 0.825 | 0.000 | — |
| RRP1 | 0.811 | 0.000 | — |
| PRICKLE1 | 0.807 | 0.000 | — |
| TRAPPC10 | 0.793 | 0.000 | — |
| APOD | 0.781 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CFTR | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12000|pubmed:17110338 |
| PINX1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| VHL | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EPB41 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| HLA-B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| GABARAP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| MAP1LC3A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| GABARAPL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| LIN54 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17531812 |
| A0A0F7RG01 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=95.5 + PDB: 1STF, 2OCT, 4N6V | pLDDT=95.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoli, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CSTB — Cystatin-B，研究基础较多，新颖性有限。
2. 蛋白大小98 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 183 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 183 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P04080
- Protein Atlas: https://www.proteinatlas.org/ENSG00000160213-CSTB/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CSTB
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P04080
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (supported)。来源: https://www.proteinatlas.org/ENSG00000160213-CSTB/subcellular

![](https://images.proteinatlas.org/17380/140_A1_1_red_green.jpg)
![](https://images.proteinatlas.org/17380/140_A1_2_red_green.jpg)
![](https://images.proteinatlas.org/17380/173_A1_1_red_green.jpg)
![](https://images.proteinatlas.org/17380/173_A1_2_red_green.jpg)
![](https://images.proteinatlas.org/17380/2268_A2_112_red_green.jpg)
![](https://images.proteinatlas.org/17380/2268_A2_8_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P04080-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P04080 |
| SMART | SM00043; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR000010;IPR046350;IPR018073;IPR001713; |
| Pfam | PF00031; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000160213-CSTB/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CCNF | Biogrid | false |
| CTSB | Biogrid | false |
| CTSH | Biogrid | false |
| TNFSF13B | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

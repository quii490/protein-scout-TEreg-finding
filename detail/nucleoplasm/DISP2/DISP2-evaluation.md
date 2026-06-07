---
type: protein-evaluation
gene: "DISP2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DISP2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DISP2 / C15orf36, DISPB, KIAA1742, LINC00594 |
| 蛋白名称 | Protein dispatched homolog 2 |
| 蛋白大小 | 1401 aa / 152.0 kDa |
| UniProt ID | A7MBM2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Vesicles; UniProt: Membrane |
| 蛋白大小 | 5/10 | ×1 | 5 | 1401 aa / 152.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=8 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR052081, IPR000731 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.0/180** | |
| **归一化总分** | | | **62.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- membrane (GO:0016020)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 14 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C15orf36, DISPB, KIAA1742, LINC00594 |

**关键文献**:
1. The ataxia-telangiectasia disease protein ATM controls vesicular protein secretion via CHGA and microtubule dynamics via CRMP5.. *Neurobiology of disease*. PMID: 39615799
2. Genetic Determinants of Colonic Diverticulosis-A Systematic Review.. *Genes*. PMID: 40428403
3. Pancreatic islet and progenitor cell surface markers with cell sorting potential.. *Diabetologia*. PMID: 21947380
4. A Hypermutable Region in the DISP2 Gene Links to Natural Selection and Late-Onset Neurocognitive Disorders in Humans.. *Molecular neurobiology*. PMID: 38565786
5. Hedgehog signaling pathway and gastric cancer.. *Cancer biology & therapy*. PMID: 16258256

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.5 |
| 高置信度残基 (pLDDT>90) 占比 | 26.7% |
| 置信残基 (pLDDT 70-90) 占比 | 32.9% |
| 中等置信 (pLDDT 50-70) 占比 | 5.9% |
| 低置信 (pLDDT<50) 占比 | 34.5% |
| 有序区域 (pLDDT>70) 占比 | 59.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=67.5），有序残基占 59.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052081, IPR000731 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SHH | 0.916 | 0.563 | — |
| DHH | 0.858 | 0.563 | — |
| IHH | 0.850 | 0.563 | — |
| PTCH1 | 0.592 | 0.000 | — |
| SCUBE2 | 0.569 | 0.000 | — |
| FAM185A | 0.506 | 0.000 | — |
| MAP6D1 | 0.493 | 0.000 | — |
| COMTD1 | 0.482 | 0.000 | — |
| PAXBP1 | 0.479 | 0.000 | — |
| DUS2 | 0.466 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CACNA1C | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:37207277|imex:IM-29810 |
| HCN1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:37207277|imex:IM-29810 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.5 + PDB: 无 | pLDDT=67.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

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
1. DISP2 — Protein dispatched homolog 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1401 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 8 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=67.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A7MBM2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000140323-DISP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DISP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A7MBM2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000140323-DISP2/subcellular

![](https://images.proteinatlas.org/59903/1314_F8_1_red_green.jpg)
![](https://images.proteinatlas.org/59903/1314_F8_2_red_green.jpg)
![](https://images.proteinatlas.org/59903/1326_F8_1_red_green.jpg)
![](https://images.proteinatlas.org/59903/1326_F8_2_red_green.jpg)
![](https://images.proteinatlas.org/59903/1519_D6_1_red_green.jpg)
![](https://images.proteinatlas.org/59903/1519_D6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A7MBM2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | A7MBM2 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 471..643; /note="SSD"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00199" |
| InterPro | IPR052081;IPR000731; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000140323-DISP2/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

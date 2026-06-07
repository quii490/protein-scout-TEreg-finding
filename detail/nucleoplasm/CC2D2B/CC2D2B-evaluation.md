---
type: protein-evaluation
gene: "CC2D2B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CC2D2B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CC2D2B / C10orf130, C10orf131 |
| 蛋白名称 | Protein CC2D2B |
| 蛋白大小 | 1437 aa / 166.8 kDa |
| UniProt ID | Q6DHV5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Vesicles, Basal body, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 5/10 | ×1 | 5 | 1437 aa / 166.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000008, IPR035892, IPR028928, IPR056288, IPR056 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **112.5/180** | |
| **归一化总分** | | | **62.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles, Basal body, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- ciliary transition zone (GO:0035869)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 4 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C10orf130, C10orf131 |

**关键文献**:
1. The CC2D2B is a novel genetic modifier of the clinical phenotype in patients with hereditary angioedema due to C1 inhibitor deficiency.. *Gene*. PMID: 38679185
2. Novel transglutaminase-like peptidase and C2 domains elucidate the structure, biogenesis and evolution of the ciliary compartment.. *Cell cycle (Georgetown, Tex.)*. PMID: 22983010

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.1 |
| 高置信度残基 (pLDDT>90) 占比 | 13.4% |
| 置信残基 (pLDDT 70-90) 占比 | 44.0% |
| 中等置信 (pLDDT 50-70) 占比 | 16.9% |
| 低置信 (pLDDT<50) 占比 | 25.7% |
| 有序区域 (pLDDT>70) 占比 | 57.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=68.1），有序残基占 57.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000008, IPR035892, IPR028928, IPR056288, IPR056290; Pfam: PF15625, PF24652, PF24656 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| C3orf22 | 0.591 | 0.000 | — |
| RNASE12 | 0.570 | 0.000 | — |
| C12orf56 | 0.544 | 0.000 | — |
| SMIM17 | 0.541 | 0.000 | — |
| CCNJ | 0.522 | 0.000 | — |
| ANKRD62 | 0.509 | 0.000 | — |
| SH2D7 | 0.508 | 0.000 | — |
| C22orf42 | 0.507 | 0.000 | — |
| C1orf167 | 0.507 | 0.000 | — |
| SPDYE4 | 0.505 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.1 + PDB: 无 | pLDDT=68.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Vesicles, Basal body, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CC2D2B — Protein CC2D2B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1437 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=68.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6DHV5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000188649-CC2D2B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CC2D2B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6DHV5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000188649-CC2D2B/subcellular

![](https://images.proteinatlas.org/44091/2243_H10_21_blue_red_green.jpg)
![](https://images.proteinatlas.org/44091/2243_H10_38_blue_red_green.jpg)
![](https://images.proteinatlas.org/44091/2244_H11_21_blue_red_green.jpg)
![](https://images.proteinatlas.org/44091/2244_H11_8_blue_red_green.jpg)
![](https://images.proteinatlas.org/44091/2248_E12_14_blue_red_green.jpg)
![](https://images.proteinatlas.org/44091/2248_E12_77_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6DHV5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6DHV5 |
| SMART | SM00239; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR000008;IPR035892;IPR028928;IPR056288;IPR056290;IPR041510;IPR052434; |
| Pfam | PF15625;PF24652;PF24656;PF17661; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000188649-CC2D2B/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

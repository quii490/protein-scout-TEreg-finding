---
type: protein-evaluation
gene: "TBC1D9B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TBC1D9B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TBC1D9B / KIAA0676 |
| 蛋白名称 | TBC1 domain family member 9B |
| 蛋白大小 | 1250 aa / 140.5 kDa |
| UniProt ID | Q66K14 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Plasma membrane; 额外: Nucleoplasm, Nucleoli fibrillar center,; UniProt: Membrane |
| 蛋白大小 | 5/10 | ×1 | 5 | 1250 aa / 140.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=74.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011992, IPR002048, IPR004182, IPR011993, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.5/180** | |
| **归一化总分** | | | **64.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Nucleoplasm, Nucleoli fibrillar center, Actin filaments | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 12 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0676 |

**关键文献**:
1. Angiogenesis-related genes and immune microenvironment in moyamoya disease: a transcriptomic and functional analysis.. *Orphanet journal of rare diseases*. PMID: 40722175
2. The LMTK1-TBC1D9B-Rab11A Cascade Regulates Dendritic Spine Formation via Endosome Trafficking.. *The Journal of neuroscience : the official journal of the Society for Neuroscience*. PMID: 31628178
3. Control of lysosome function by the GTPase-activating protein TBC1D9B and its binding partner TMEM55B.. *Nature communications*. PMID: 41832156
4. TBC1D9B functions as a GTPase-activating protein for Rab11a in polarized MDCK cells.. *Molecular biology of the cell*. PMID: 25232007
5. Comparative Proteomics Analysis of Human Macrophages Infected with Virulent Mycobacterium bovis.. *Frontiers in cellular and infection microbiology*. PMID: 28337427

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.3 |
| 高置信度残基 (pLDDT>90) 占比 | 38.8% |
| 置信残基 (pLDDT 70-90) 占比 | 29.8% |
| 中等置信 (pLDDT 50-70) 占比 | 9.4% |
| 低置信 (pLDDT<50) 占比 | 22.0% |
| 有序区域 (pLDDT>70) 占比 | 68.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=74.3，有序区 68.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011992, IPR002048, IPR004182, IPR011993, IPR000195; Pfam: PF02893, PF00566 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RAB11A | 0.673 | 0.071 | — |
| GABARAPL2 | 0.653 | 0.591 | — |
| RAB8A | 0.628 | 0.540 | — |
| TBC1D9 | 0.628 | 0.610 | — |
| TBC1D20 | 0.593 | 0.000 | — |
| LANCL1 | 0.576 | 0.574 | — |
| TBC1D5 | 0.558 | 0.000 | — |
| MAP1LC3B | 0.549 | 0.230 | — |
| RNF130 | 0.532 | 0.000 | — |
| TBC1D25 | 0.531 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| mntH | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| MAX | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| LANCL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PIP4P1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| UBAC1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| SH2D3C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| Stat3 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| Memo1 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |
| Txndc12 | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.3 + PDB: 无 | pLDDT=74.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Plasma membrane; 额外: Nucleoplasm, Nucleoli fibrill | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TBC1D9B — TBC1 domain family member 9B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1250 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q66K14
- Protein Atlas: https://www.proteinatlas.org/ENSG00000197226-TBC1D9B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TBC1D9B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q66K14
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000197226-TBC1D9B/subcellular

![](https://images.proteinatlas.org/38350/435_A4_1_red_green.jpg)
![](https://images.proteinatlas.org/38350/435_A4_2_red_green.jpg)
![](https://images.proteinatlas.org/38350/445_A4_1_red_green.jpg)
![](https://images.proteinatlas.org/38350/445_A4_2_red_green.jpg)
![](https://images.proteinatlas.org/38350/448_A4_3_red_green.jpg)
![](https://images.proteinatlas.org/38350/448_A4_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q66K14-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

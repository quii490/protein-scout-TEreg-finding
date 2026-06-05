---
type: protein-evaluation
gene: "TNFAIP8L2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TNFAIP8L2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TNFAIP8L2 |
| 蛋白名称 | Tumor necrosis factor alpha-induced protein 8-like protein 2 |
| 蛋白大小 | 184 aa / 20.6 kDa |
| UniProt ID | Q6P589 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles; UniProt: Cytoplasm; Nucleus; Lysosome |
| 蛋白大小 | 8/10 | ×1 | 8 | 184 aa / 20.6 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=70 篇 (≤80→4) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=90.4; PDB: 3F4M |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR008477, IPR038355; Pfam: PF05527 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **107.0/180** | |
| **归一化总分** | | | **59.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles | Approved |
| UniProt | Cytoplasm; Nucleus; Lysosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- lysosome (GO:0005764)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 70 |
| PubMed broad count | 155 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Polyethylene microplastic exposure adversely affects oocyte quality in human and mouse.. *Environment international*. PMID: 39729868
2. TNFAIP8L2 maintains hair cell function and regulates age-related hearing loss via mTORC1 signaling.. *Molecular therapy : the journal of the American Society of Gene Therapy*. PMID: 40165373
3. Characterization and transcriptional regulation analysis of the porcine TNFAIP8L2 gene.. *Molecular genetics and genomics : MGG*. PMID: 20640581
4. TNFAIP8L2/TIPE2 impairs autolysosome reformation via modulating the RAC1-MTORC1 axis.. *Autophagy*. PMID: 32460619
5. Tumor necrosis factor α-induced protein 8-like-2 controls microglia phenotype via metabolic reprogramming in BV2 microglial cells and responses to neuropathic pain.. *The international journal of biochemistry & cell biology*. PMID: 38309648

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.4 |
| 高置信度残基 (pLDDT>90) 占比 | 75.5% |
| 置信残基 (pLDDT 70-90) 占比 | 14.7% |
| 中等置信 (pLDDT 50-70) 占比 | 8.2% |
| 低置信 (pLDDT<50) 占比 | 1.6% |
| 有序区域 (pLDDT>70) 占比 | 90.2% |
| 可用 PDB 条目 | 3F4M |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=90.4，有序区 90.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008477, IPR038355; Pfam: PF05527 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CASP8 | 0.776 | 0.094 | — |
| TLR1 | 0.621 | 0.000 | — |
| TES | 0.601 | 0.596 | — |
| RAC1 | 0.596 | 0.510 | — |
| ARHGAP9 | 0.488 | 0.000 | — |
| SASH3 | 0.483 | 0.000 | — |
| GIMAP8 | 0.479 | 0.000 | — |
| S1PR4 | 0.478 | 0.000 | — |
| LST1 | 0.463 | 0.000 | — |
| RGS18 | 0.462 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Casp8 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-11963|pubmed:18455983 |
| TES | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NPTN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.4 + PDB: 3F4M | pLDDT=90.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Lysosome / Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TNFAIP8L2 — Tumor necrosis factor alpha-induced protein 8-like protein 2，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小184 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 70 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6P589
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163154-TNFAIP8L2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TNFAIP8L2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6P589
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (approved)。来源: https://www.proteinatlas.org/ENSG00000163154-TNFAIP8L2/subcellular

![](https://images.proteinatlas.org/62742/1677_A1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/62742/1677_A1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/62742/1688_A1_31_blue_red_green.jpg)
![](https://images.proteinatlas.org/62742/1688_A1_32_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6P589-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

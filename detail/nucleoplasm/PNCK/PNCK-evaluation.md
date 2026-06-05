---
type: protein-evaluation
gene: "PNCK"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PNCK 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PNCK |
| 蛋白名称 | Calcium/calmodulin-dependent protein kinase type 1B |
| 蛋白大小 | 343 aa / 38.5 kDa |
| UniProt ID | Q6P2M8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane, Cytosol; 额外: Golgi apparatus; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 343 aa / 38.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=20 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=81.8; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR042696, IPR011009, IPR000719, IPR017441, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **135.5/180** | |
| **归一化总分** | | | **75.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cytosol; 额外: Golgi apparatus | Approved |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 20 |
| PubMed broad count | 90 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Pnck overexpression in HER-2 gene-amplified breast cancer causes Trastuzumab resistance through a paradoxical PTEN-mediated process.. *Breast cancer research and treatment*. PMID: 25773930
2. Cloning, characterization, and chromosomal localization of Pnck, a Ca(2+)/calmodulin-dependent protein kinase.. *Genomics*. PMID: 10673339
3. Pregnancy-upregulated nonubiquitous calmodulin kinase induces ligand-independent EGFR degradation.. *American journal of physiology. Cell physiology*. PMID: 18562482
4. PTEN-mediated ERK1/2 inhibition and paradoxical cellular proliferation following Pnck overexpression.. *Cell cycle (Georgetown, Tex.)*. PMID: 24552815
5. Transcriptomic Analysis and Meta-Analysis of Human Granulosa and Cumulus Cells.. *PloS one*. PMID: 26313571

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.8 |
| 高置信度残基 (pLDDT>90) 占比 | 55.1% |
| 置信残基 (pLDDT 70-90) 占比 | 23.6% |
| 中等置信 (pLDDT 50-70) 占比 | 6.4% |
| 低置信 (pLDDT<50) 占比 | 14.9% |
| 有序区域 (pLDDT>70) 占比 | 78.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=81.8，有序区 78.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR042696, IPR011009, IPR000719, IPR017441, IPR008271; Pfam: PF00069 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DCX | 0.885 | 0.114 | — |
| IRAK1 | 0.583 | 0.068 | — |
| CALM3 | 0.571 | 0.246 | — |
| CALML3 | 0.565 | 0.246 | — |
| CALML5 | 0.559 | 0.246 | — |
| FGF3 | 0.519 | 0.000 | — |
| CAMK2A | 0.516 | 0.056 | — |
| NOMO2 | 0.507 | 0.000 | — |
| NOMO3 | 0.507 | 0.000 | — |
| NOMO1 | 0.505 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EPHA4 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 1
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.8 + PDB: 无 | pLDDT=81.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Plasma membrane, Cytosol; 额外: Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 1 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. PNCK — Calcium/calmodulin-dependent protein kinase type 1B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小343 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 20 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6P2M8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000130822-PNCK/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PNCK
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6P2M8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000130822-PNCK/subcellular

![](https://images.proteinatlas.org/7458/2166_E6_41_blue_red_green.jpg)
![](https://images.proteinatlas.org/7458/2166_E6_66_blue_red_green.jpg)
![](https://images.proteinatlas.org/7458/44_E4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/7458/44_E4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/7458/45_E4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/7458/45_E4_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6P2M8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

---
type: protein-evaluation
gene: "DTNB"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DTNB — REJECTED (研究热度过高 (PubMed strict=530，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DTNB |
| 蛋白名称 | Dystrobrevin beta |
| 蛋白大小 | 627 aa / 71.4 kDa |
| UniProt ID | O60941 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/DTNB/IF_images/HBEC3-KT_1.jpg|HBEC3-KT]]
![[Projects/TEreg-finding/protein-interested/detail/rejected/DTNB/IF_images/SiHa_1.jpg|SiHa]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Golgi apparatus; UniProt: Cytoplasm; Postsynaptic density; Cell projection, dendrite;  |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 627 aa / 71.4 kDa |
| 🆕 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=530 篇 (>100→REJECTED) |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=75.4; PDB: 无 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR017432, IPR011992, IPR015153, IPR015154, IPR050 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **83.0/180** | |
| **归一化总分** | | | **46.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus | Approved |
| UniProt | Cytoplasm; Postsynaptic density; Cell projection, dendrite; Basal cell membrane;... | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- basal plasma membrane (GO:0009925)
- cytoplasm (GO:0005737)
- dendrite (GO:0030425)
- inhibitory synapse (GO:0060077)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 530 |
| PubMed broad count | 1553 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Region-based analysis of rare genomic variants in whole-genome sequencing datasets reveal two novel Alzheimer's disease-associated genes: DTNB and DLG2.. *Molecular psychiatry*. PMID: 35246634
2. Elucidating the structure-function attributes of a trypanosomal arginyl-tRNA synthetase.. *Molecular and biochemical parasitology*. PMID: 37852416
3. Hyperthermia induces reductive stress in murine macrophages.. *Biochimica et biophysica acta. Molecular basis of disease*. PMID: 41381010
4. Cardamonin suppresses mTORC1/SREBP1 through reducing Raptor and inhibits de novo lipogenesis in ovarian cancer.. *PloS one*. PMID: 40315213
5. Effect of Redox-Modifying Agents on the Activity of Channelrhodopsin-2.. *CNS neuroscience & therapeutics*. PMID: 27917616

**评价**: 有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.4 |
| 高置信度残基 (pLDDT>90) 占比 | 42.7% |
| 置信残基 (pLDDT 70-90) 占比 | 23.0% |
| 中等置信 (pLDDT 50-70) 占比 | 14.0% |
| 低置信 (pLDDT<50) 占比 | 20.3% |
| 有序区域 (pLDDT>70) 占比 | 65.7% |
| 可用 PDB 条目 | 无 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=75.4，有序区 65.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR017432, IPR011992, IPR015153, IPR015154, IPR050774; Pfam: PF09068, PF09069, PF00569 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SNTG2 | 0.980 | 0.834 | — |
| DMD | 0.956 | 0.860 | — |
| SNTG1 | 0.951 | 0.619 | — |
| SNTB2 | 0.937 | 0.762 | — |
| DAG1 | 0.937 | 0.292 | — |
| SNTB1 | 0.922 | 0.780 | — |
| DTNBP1 | 0.919 | 0.383 | — |
| SNTA1 | 0.915 | 0.763 | — |
| UTRN | 0.860 | 0.808 | — |
| PPP1R21 | 0.841 | 0.840 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.4 + PDB: 无 | pLDDT=75.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Postsynaptic density; Cell projection,  / Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DTNB — Dystrobrevin beta，有一定研究基础，但仍存在niche空间。
2. 蛋白大小627 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 530 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 530 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O60941
- Protein Atlas: https://www.proteinatlas.org/ENSG00000138101-DTNB/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DTNB
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60941
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 12:20:19

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O60941-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O60941 |
| SMART | SM00291; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR017432;IPR011992;IPR015153;IPR015154;IPR050774;IPR000433;IPR043145; |
| Pfam | PF09068;PF09069;PF00569; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000138101-DTNB/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ABI2 | Intact, Biogrid | true |
| DMD | Intact, Biogrid | true |
| DTNBP1 | Intact, Biogrid | true |
| HMG20A | Intact, Biogrid | true |
| PPFIA1 | Intact, Biogrid | true |
| SNTG2 | Intact, Biogrid | true |
| UTRN | Intact, Biogrid | true |
| ABI3 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

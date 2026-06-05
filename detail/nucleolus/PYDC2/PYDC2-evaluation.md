---
type: protein-evaluation
gene: "PYDC2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PYDC2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PYDC2 / POP2 |
| 蛋白名称 | Pyrin domain-containing protein 2 |
| 蛋白大小 | 97 aa / 10.8 kDa |
| UniProt ID | Q56P42 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli; 额外: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 5/10 | ×1 | 5 | 97 aa / 10.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=74.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR004020, IPR011029; Pfam: PF02758 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 12 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli; 额外: Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 30 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: POP2 |

**关键文献**:
1. Association of NOD1, NOD2, PYDC1 and PYDC2 genes with Behcet's disease susceptibility and clinical manifestations.. *Ophthalmic genetics*. PMID: 34294014
2. The CLRX.1/NOD24 (NLRP2P) pseudogene codes a functional negative regulator of NF-κB, pyrin-only protein 4.. *Genes and immunity*. PMID: 24871464
3. Exploratory genetic analysis in children with autism spectrum disorder and other developmental disorders using whole exome sequencing.. *Biomolecules & biomedicine*. PMID: 38421723
4. Inflammatory Gene Signature Identified by Machine Algorithms Reveals Novel Biomarkers of Coronary Artery Disease.. *Journal of inflammation research*. PMID: 39959641
5. NOD1, NOD2, PYDC1, and PYDC2 gene polymorphisms in ovarian endometriosis.. *Frontiers in medicine*. PMID: 40034240

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.3 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 70.1% |
| 中等置信 (pLDDT 50-70) 占比 | 21.6% |
| 低置信 (pLDDT<50) 占比 | 8.2% |
| 有序区域 (pLDDT>70) 占比 | 70.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=74.3，有序区 70.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004020, IPR011029; Pfam: PF02758 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PYCARD | 0.956 | 0.409 | — |
| MEFV | 0.646 | 0.067 | — |
| PYDC1 | 0.606 | 0.000 | — |
| CARD17 | 0.539 | 0.000 | — |
| CARD8 | 0.479 | 0.000 | — |
| NAIP | 0.477 | 0.000 | — |
| CASP5 | 0.476 | 0.000 | — |
| CNOT1 | 0.445 | 0.000 | — |
| NLRP12 | 0.444 | 0.230 | — |
| DAPK1 | 0.434 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 12，IntAct interactions: 0
- 调控相关比例: 0 / 12 = 0%

**评价**: STRING 12 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.3 + PDB: 无 | pLDDT=74.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm, Nucleoli; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 12 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. PYDC2 — Pyrin domain-containing protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小97 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q56P42
- Protein Atlas: https://www.proteinatlas.org/ENSG00000253548-PYDC2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PYDC2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q56P42
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000253548-PYDC2/subcellular

![](https://images.proteinatlas.org/35819/2064_E1_1_red_green.jpg)
![](https://images.proteinatlas.org/35819/2064_E1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q56P42-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

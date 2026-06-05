---
type: protein-evaluation
gene: "CLEC18C"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CLEC18C — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CLEC18C / MRLP3 |
| 蛋白名称 | C-type lectin domain family 18 member C |
| 蛋白大小 | 446 aa / 49.6 kDa |
| UniProt ID | Q8NCF0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Secreted; Endoplasmic reticulum; Golgi apparatus; Endosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 446 aa / 49.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=82.1; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR001304, IPR016186, IPR018378, IPR014044, IPR035 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 2 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **115.5/180** | |
| **归一化总分** | | | **64.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Secreted; Endoplasmic reticulum; Golgi apparatus; Endosome | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- endoplasmic reticulum (GO:0005783)
- endosome (GO:0005768)
- extracellular space (GO:0005615)
- Golgi apparatus (GO:0005794)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 5 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MRLP3 |

**关键文献**:
1. Definition of a Novel Immunogenic Cell Death-Relevant Gene Signature Associated with Immune Landscape in Gastric Cancer.. *Biochemical genetics*. PMID: 36943521
2. [Establishment and gene expression analysis of drug-resistant cell lines in hepatocellular carcinoma induced by sorafenib].. *Beijing da xue xue bao. Yi xue ban = Journal of Peking University. Health sciences*. PMID: 32306000
3. A novel golgi related genes based correlation prognostic index can better predict the prognosis of glioma and responses to immunotherapy.. *Discover oncology*. PMID: 39976877
4. Human CLEC18 Gene Cluster Contains C-type Lectins with Differential Glycan-binding Specificity.. *The Journal of biological chemistry*. PMID: 26170455

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.1 |
| 高置信度残基 (pLDDT>90) 占比 | 54.0% |
| 置信残基 (pLDDT 70-90) 占比 | 27.6% |
| 中等置信 (pLDDT 50-70) 占比 | 6.3% |
| 低置信 (pLDDT<50) 占比 | 12.1% |
| 有序区域 (pLDDT>70) 占比 | 81.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=82.1，有序区 81.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001304, IPR016186, IPR018378, IPR014044, IPR035940; Pfam: PF00188, PF00059 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GART | 0.831 | 0.000 | — |
| C1QTNF9B | 0.505 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NFKBIL1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 2，IntAct interactions: 1
- 调控相关比例: 0 / 2 = 0%

**评价**: STRING 2 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.1 + PDB: 无 | pLDDT=82.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Secreted; Endoplasmic reticulum; Golgi apparatus;  / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 2 + 1 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CLEC18C — C-type lectin domain family 18 member C，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小446 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NCF0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000157335-CLEC18C/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CLEC18C
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NCF0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NCF0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

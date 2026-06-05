---
type: protein-evaluation
gene: "COX7A2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## COX7A2 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COX7A2 / COX7AL |
| 蛋白名称 | Cytochrome c oxidase subunit 7A2, mitochondrial |
| 蛋白大小 | 83 aa / 9.4 kDa |
| UniProt ID | P14406 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: 暂无HPA定位数据; UniProt: Mitochondrion inner membrane |
| 蛋白大小 | 5/10 | x1 | 5 | 83 aa / 9.4 kDa |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed strict=45 篇 (≤60→6) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=88.4; PDB: 5Z62 |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR039297, IPR036539, IPR003177; Pfam: PF02238 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **93.5/180** | |
| **归一化总分** | | | **51.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Mitochondrion inner membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- mitochondrial inner membrane (GO:0005743)
- mitochondrial membrane (GO:0031966)
- mitochondrion (GO:0005739)
- respiratory chain complex (GO:0098803)
- respiratory chain complex IV (GO:0045277)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 45 |
| PubMed broad count | 66 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: COX7AL |

**关键文献**:
1. A novel palmitoylation-based molecular signature reveals COX6A1 as a key regulator in metabolic dysfunction-associated steatotic liver disease.. *Journal of translational medicine*. PMID: 41185013
2. Differential gene expression in obese pregnancy.. *Pregnancy hypertension*. PMID: 26104615
3. Proteomic signatures of Alzheimer's disease and Lewy body dementias: A comparative analysis.. *Alzheimer's & dementia : the journal of the Alzheimer's Association*. PMID: 39711511
4. [Construction of pGEX4T-1-Cox7a2 and expression, purification and identification of the recombinant protein].. *Zhonghua nan ke xue = National journal of andrology*. PMID: 17009529
5. Cox7a2 mediates steroidogenesis in TM3 mouse Leydig cells.. *Asian journal of andrology*. PMID: 16752004

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.4 |
| 高置信度残基 (pLDDT>90) 占比 | 65.1% |
| 置信残基 (pLDDT 70-90) 占比 | 22.9% |
| 中等置信 (pLDDT 50-70) 占比 | 12.0% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 88.0% |
| 可用 PDB 条目 | 5Z62 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度（pLDDT=88.4，有序区 88.0%）。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039297, IPR036539, IPR003177; Pfam: PF02238 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MT-CO2 | 0.999 | 0.998 | — |
| COX6B1 | 0.998 | 0.934 | — |
| COX6A1 | 0.998 | 0.906 | — |
| COX7C | 0.997 | 0.902 | — |
| COX5B | 0.997 | 0.900 | — |
| COX6C | 0.997 | 0.804 | — |
| NDUFA4 | 0.997 | 0.839 | — |
| COX4I1 | 0.993 | 0.893 | — |
| COX7B | 0.991 | 0.800 | — |
| COX5A | 0.991 | 0.802 | — |

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
| 三维结构 | AlphaFold pLDDT=88.4 + PDB: 5Z62 | pLDDT=88.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Mitochondrion inner membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. COX7A2 -- Cytochrome c oxidase subunit 7A2, mitochondrial，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小83 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 45 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P14406
- Protein Atlas: https://www.proteinatlas.org/ENSG00000112695-COX7A2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COX7A2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P14406
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P14406-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

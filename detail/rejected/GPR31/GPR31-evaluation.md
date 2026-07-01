---
type: protein-evaluation
gene: "GPR31"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GPR31 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPR31 |
| 蛋白名称 | 12-(S)-hydroxy-5,8,10,14-eicosatetraenoic acid receptor |
| 蛋白大小 | 319 aa / 35.1 kDa |
| UniProt ID | O00270 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 319 aa / 35.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=83.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000276, IPR017452, IPR051893; Pfam: PF00001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **115.5/180** | |
| **归一化总分** | | | **64.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) | 无 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.2 |
| 高置信度残基 (pLDDT>90) 占比 | 41.4% |
| 置信残基 (pLDDT 70-90) 占比 | 43.9% |
| 中等置信 (pLDDT 50-70) 占比 | 8.8% |
| 低置信 (pLDDT<50) 占比 | 6.0% |
| 有序区域 (pLDDT>70) 占比 | 85.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=83.2，有序区 85.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000276, IPR017452, IPR051893; Pfam: PF00001 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ZIC3 | 0.841 | 0.000 | — |
| NODAL | 0.767 | 0.069 | — |
| CFC1 | 0.721 | 0.049 | — |
| ACVR2B | 0.588 | 0.000 | — |
| DENR | 0.549 | 0.000 | — |
| TCP10L2 | 0.527 | 0.000 | — |
| SRC | 0.517 | 0.000 | — |
| AGT | 0.507 | 0.000 | — |
| AGTR2 | 0.499 | 0.000 | — |
| GPR3 | 0.496 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RAMP2 | psi-mi:"MI:0947"(bead aggregation assay) | pubmed:39083597|imex:IM-30383 |
| RAMP3 | psi-mi:"MI:0947"(bead aggregation assay) | pubmed:39083597|imex:IM-30383 |
| RAMP1 | psi-mi:"MI:0947"(bead aggregation assay) | pubmed:39083597|imex:IM-30383 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 3
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.2 + PDB: 无 | pLDDT=83.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 3 interactions | 数据充分 |

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
1. GPR31 — 12-(S)-hydroxy-5,8,10,14-eicosatetraenoic acid receptor，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小319 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 深度机制分析

GPR31（319 aa, pLDDT=83.2）是G蛋白偶联受体31（OXER1），定位于细胞质膜（UniProt）。其结构域包含GPCR视紫红质样7跨膜螺旋束（IPR000276、IPR017452、PF00001），作为12(S)-HETE（羟基二十碳四烯酸）的高亲和力受体行使Gi/Go偶联信号转导功能。GPR31的AlphaFold预测pLDDT=83.2（有序区85.3%），7TM螺旋束折叠的高置信度与GPCR整体折叠特征完全一致。

该蛋白的核心生理功能为花生四烯酸代谢产物的脂质介质感知。12(S)-HETE作为12-脂氧合酶的产物，通过GPR31激活Gi信号抑制cAMP产生并促进钙动员和PI3K/Akt通路。GPR31与RAMP1/2/3的实验验证互作（PMID:39083597, bead aggregation assay）提示其作为RAMP互作GPCR，RAMP蛋白（受体活性修饰蛋白）可调节GPCR的药理学特性和细胞内运输。

从TE调控角度，GPR31的STRING互作网络包含ZIC3（Combined Score=0.841）、NODAL（0.767）、CFC1（0.721）等与发育信号通路密切相关的互作伙伴。ZIC3是锌指转录因子，在胚胎左-右不对称发育中发挥关键作用，NODAL/CFC1是TGFβ超家族信号的核心组分。这些互作提示GPR31可能通过GPCR-TGFβ信号串扰参与发育基因调控网络。然而，GPR31因核定位证据极弱（2/10）已被淘汰，其TE调控意义仅限于作为质膜启动的GPCR信号级联的远端效应器，通过PI3K/Akt→mTOR→TET通路间接影响TE甲基化状态的可能性微乎其微。评分64.2/100，定位决定其不适合作为核蛋白TE调控靶标。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O00270
- Protein Atlas: https://www.proteinatlas.org/ENSG00000120436-GPR31/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPR31
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O00270
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O00270-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

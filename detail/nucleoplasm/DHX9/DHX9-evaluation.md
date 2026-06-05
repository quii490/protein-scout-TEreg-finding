---
type: protein-evaluation
gene: "DHX9"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DHX9 — REJECTED (研究热度过高 (PubMed strict=333，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DHX9 |
| 蛋白名称 | ATP-dependent RNA helicase A |
| 蛋白大小 | 1270 aa / 141.0 kDa |
| UniProt ID | Q08211 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm; 额外: Nucleoli; UniProt: Nucleus; Nucleus, nucleoplasm; Nucleus, nucleolus; Cytoplasm |
| 蛋白大小 | 5/10 | x1 | 5 | 1270 aa / 141.0 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=333 篇 (>100->REJECTED) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=80.9; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **76.5/180** | |
| **归一化总分** | | | **42.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli | Enhanced |
| UniProt | Nucleus; Nucleus, nucleoplasm; Nucleus, nucleolus; Cytoplasm; Cytoplasm, cytoskeleton, microtubule o... | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 333 |
| PubMed broad count | 409 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Pilot study on differential gene expression in relation to vincristine response in canine transmissible venereal tumor.. *Res Vet Sci*. PMID: 42001618
2. Role of RNA helicases in circRNA biogenesis and regulation.. *Biochim Biophys Acta Gene Regul Mech*. PMID: 41862014
3. Accumulated sotorasib-bound KRAS(G12C) reactivates the MAPK pathway and drives sotorasib resistance via the DHX9-RAC1-PAK1 axis.. *Cell Rep*. PMID: 42090290
4. Helicase A determines the transcription program of T(H)17 lineage differentiation and autoimmunity.. *Sci Adv*. PMID: 42139358
5. HlncRNA-1 integrates the hepatic circadian clock with lipid metabolism by targeting Hdlbp.. *Commun Biol*. PMID: 42092182

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.9 |
| 高置信度残基 (pLDDT>90) 占比 | 54.1% |
| 置信残基 (pLDDT 70-90) 占比 | 27.0% |
| 中等置信 (pLDDT 50-70) 占比 | 4.1% |
| 低置信 (pLDDT<50) 占比 | 14.8% |
| 有序区域 (pLDDT>70) 占比 | 81.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=80.9，有序区 81.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HNRNPU | 0.000 | 0.000 | — |
| AGO2 | 0.000 | 0.000 | — |
| EWSR1 | 0.000 | 0.000 | — |
| DDX5 | 0.000 | 0.000 | — |
| SYNCRIP | 0.000 | 0.000 | — |
| YBX1 | 0.000 | 0.000 | — |
| HNRNPC | 0.000 | 0.000 | — |
| DICER1 | 0.000 | 0.000 | — |
| ILF2 | 0.000 | 0.000 | — |
| IGF2BP1 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q08211 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 1 / 20 = 5%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 5%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.9 + PDB: 无 | pLDDT=80.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, nucleoplasm; Nucleus, nucleolus; / Nucleoplasm; 额外: Nucleoli | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ** (REJECTED)

**核心优势**:
1. DHX9 -- ATP-dependent RNA helicase A，研究基础较多，新颖性有限。
2. 蛋白大小1270 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 333 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 333 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q08211
- Protein Atlas: https://www.proteinatlas.org/ENSG00000135829-DHX9/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DHX9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q08211
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q08211-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

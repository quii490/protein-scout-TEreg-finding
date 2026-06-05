---
type: protein-evaluation
gene: "GPR15"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GPR15 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=111，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPR15 |
| 蛋白名称 | G-protein coupled receptor 15 |
| 蛋白大小 | 360 aa / 40.8 kDa |
| UniProt ID | P49685 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 360 aa / 40.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=111 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=81.8; PDB: 8ZQE |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR050119, IPR000276, IPR017452; Pfam: PF00001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **68.5/180** | |
| **归一化总分** | | | **38.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- endosome (GO:0005768)
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 111 |
| PubMed broad count | 199 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Blocking GPR15 Counteracts Integrin-dependent T Cell Gut Homing in Vivo.. *Journal of Crohn's & colitis*. PMID: 38243565
2. The Role of GPR15 Function in Blood and Vasculature.. *International journal of molecular sciences*. PMID: 34639163
3. Emerging roles of a chemoattractant receptor GPR15 and ligands in pathophysiology.. *Frontiers in immunology*. PMID: 37457732
4. GPR15 in colon cancer development and anti-tumor immune responses.. *Frontiers in oncology*. PMID: 38074634
5. GPR15LG binds CXCR4 and synergistically modulates CXCL12-induced cell signaling and migration.. *Cell communication and signaling : CCS*. PMID: 40394646

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.8 |
| 高置信度残基 (pLDDT>90) 占比 | 49.7% |
| 置信残基 (pLDDT 70-90) 占比 | 28.3% |
| 中等置信 (pLDDT 50-70) 占比 | 9.4% |
| 低置信 (pLDDT<50) 占比 | 12.5% |
| 有序区域 (pLDDT>70) 占比 | 78.0% |
| 可用 PDB 条目 | 8ZQE |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=81.8，有序区 78.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050119, IPR000276, IPR017452; Pfam: PF00001 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| C10orf99 | 0.775 | 0.000 | — |
| ITIH4 | 0.638 | 0.000 | — |
| ZNF80 | 0.603 | 0.000 | — |
| GPR150 | 0.578 | 0.000 | — |
| GPR27 | 0.574 | 0.000 | — |
| CLDND1 | 0.573 | 0.000 | — |
| LRRN3 | 0.571 | 0.000 | — |
| GPR32 | 0.561 | 0.000 | — |
| GPR25 | 0.530 | 0.000 | — |
| GPR45 | 0.527 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=81.8 + PDB: 8ZQE | pLDDT=81.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. GPR15 — G-protein coupled receptor 15，研究基础较多，新颖性有限。
2. 蛋白大小360 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 111 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P49685
- Protein Atlas: https://www.proteinatlas.org/ENSG00000154165-GPR15/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPR15
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P49685
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P49685-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

---
type: protein-evaluation
gene: "GPR85"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GPR85 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPR85 / SREB2 |
| 蛋白名称 | Probable G-protein coupled receptor 85 |
| 蛋白大小 | 370 aa / 42.0 kDa |
| UniProt ID | P60893 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane; Endoplasmic reticulum |
| 蛋白大小 | 10/10 | ×1 | 10 | 370 aa / 42.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=36 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=82.6; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR051509, IPR000276, IPR017452; Pfam: PF00001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **105.5/180** | |
| **归一化总分** | | | **58.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell membrane; Endoplasmic reticulum | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- endoplasmic reticulum (GO:0005783)
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 36 |
| PubMed broad count | 42 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SREB2 |

**关键文献**:
1. Synaptic Gpr85 Influences Cerebellar-Granule-Cell Electrical Properties and Light-Induced Behavior in Zebrafish.. *The Journal of neuroscience : the official journal of the Society for Neuroscience*. PMID: 41213803
2. The role of orphan G protein-coupled receptors in pain.. *Heliyon*. PMID: 38590871
3. Orphan G protein-coupled receptors: The role in CNS disorders.. *Biomedicine & pharmacotherapy = Biomedecine & pharmacotherapie*. PMID: 29268243
4. Molecular insights into orphan G protein-coupled receptors relevant to schizophrenia.. *British journal of pharmacology*. PMID: 37605621
5. Super-conserved receptors expressed in the brain: biology and medicinal chemistry efforts.. *Future medicinal chemistry*. PMID: 35535715

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.6 |
| 高置信度残基 (pLDDT>90) 占比 | 56.5% |
| 置信残基 (pLDDT 70-90) 占比 | 18.4% |
| 中等置信 (pLDDT 50-70) 占比 | 15.9% |
| 低置信 (pLDDT<50) 占比 | 9.2% |
| 有序区域 (pLDDT>70) 占比 | 74.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=82.6，有序区 74.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051509, IPR000276, IPR017452; Pfam: PF00001 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CXCL14 | 0.836 | 0.292 | — |
| INSIG2 | 0.775 | 0.000 | — |
| INSIG1 | 0.683 | 0.000 | — |
| SREBF2 | 0.640 | 0.000 | — |
| ALDH18A1 | 0.640 | 0.000 | — |
| SREBF1 | 0.586 | 0.000 | — |
| SCARF1 | 0.557 | 0.000 | — |
| SNX33 | 0.515 | 0.000 | — |
| PLAGL2 | 0.489 | 0.000 | — |
| ENC1 | 0.482 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| yopM | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ACP2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.6 + PDB: 无 | pLDDT=82.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane; Endoplasmic reticulum / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

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
1. GPR85 — Probable G-protein coupled receptor 85，非常新颖，仅有少数基础研究。
2. 蛋白大小370 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 36 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P60893
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164604-GPR85/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPR85
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P60893
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P60893-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

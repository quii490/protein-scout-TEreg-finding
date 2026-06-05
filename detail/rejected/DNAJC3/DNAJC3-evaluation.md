---
type: protein-evaluation
gene: "DNAJC3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DNAJC3 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNAJC3 / P58IPK, PRKRI |
| 蛋白名称 | DnaJ homolog subfamily C member 3 |
| 蛋白大小 | 504 aa / 57.6 kDa |
| UniProt ID | Q13217 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 2/10 | ×4 | 8 | HPA: Endoplasmic reticulum; UniProt: Endoplasmic reticulum |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 504 aa / 57.6 kDa |
| 🆕 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=77 篇 (≤80→4) |
| 🏗️ 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=86.5; PDB: 2Y4T, 2Y4U |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR051727, IPR001623, IPR036869, IPR011990, IPR019 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **91.5/180** | |
| **归一化总分** | | | **50.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum | Approved |
| UniProt | Endoplasmic reticulum | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- azurophil granule lumen (GO:0035578)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum lumen (GO:0005788)
- extracellular exosome (GO:0070062)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 77 |
| PubMed broad count | 148 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: P58IPK, PRKRI |

**关键文献**:
1. Long noncoding RNA DNAJC3-AS1 promotes osteosarcoma progression via its sense-cognate gene DNAJC3.. *Cancer medicine*. PMID: 30652414
2. Reduced DNAJC3 Expression Affects Protein Translocation across the ER Membrane and Attenuates the Down-Modulating Effect of the Translocation Inhibitor Cyclotriazadisulfonamide.. *International journal of molecular sciences*. PMID: 35054769
3. Progranulin inhibits fibrosis by interacting with and up-regulating DNAJC3 during mouse skin wound healing.. *Cellular signalling*. PMID: 37329998
4. Absence of BiP co-chaperone DNAJC3 causes diabetes mellitus and multisystemic neurodegeneration.. *American journal of human genetics*. PMID: 25466870
5. Down-regulation of lncRNA DNAJC3-AS1 inhibits colon cancer via regulating miR-214-3p/LIVIN axis.. *Bioengineered*. PMID: 32352854

**评价**: 有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.5 |
| 高置信度残基 (pLDDT>90) 占比 | 74.2% |
| 置信残基 (pLDDT 70-90) 占比 | 11.7% |
| 中等置信 (pLDDT 50-70) 占比 | 1.4% |
| 低置信 (pLDDT<50) 占比 | 12.7% |
| 有序区域 (pLDDT>70) 占比 | 85.9% |
| 可用 PDB 条目 | 2Y4T, 2Y4U |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2Y4T, 2Y4U）+ AlphaFold高质量预测（pLDDT=86.5），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051727, IPR001623, IPR036869, IPR011990, IPR019734; Pfam: PF00226, PF00515, PF13432 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EIF2AK2 | 0.995 | 0.510 | — |
| HSPA5 | 0.978 | 0.663 | — |
| DNAJB1 | 0.976 | 0.096 | — |
| XBP1 | 0.951 | 0.000 | — |
| PDIA6 | 0.944 | 0.472 | — |
| HYOU1 | 0.928 | 0.410 | — |
| HSP90B1 | 0.927 | 0.245 | — |
| HSPA4 | 0.916 | 0.661 | — |
| THAP12 | 0.907 | 0.294 | — |
| DNAJB11 | 0.831 | 0.469 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 2 / 15 = 13%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 13%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.5 + PDB: 2Y4T, 2Y4U | pLDDT=86.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Endoplasmic reticulum / Endoplasmic reticulum | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. DNAJC3 — DnaJ homolog subfamily C member 3，有一定研究基础，但仍存在niche空间。
2. 蛋白大小504 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 77 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13217
- Protein Atlas: https://www.proteinatlas.org/ENSG00000102580-DNAJC3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNAJC3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13217
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 12:17:32

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q13217-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

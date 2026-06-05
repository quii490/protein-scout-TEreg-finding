---
type: protein-evaluation
gene: "MAFG"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MAFG — REJECTED (研究热度过高 (PubMed strict=194，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MAFG |
| 蛋白名称 | Transcription factor MafG |
| 蛋白大小 | 162 aa / 17.9 kDa |
| UniProt ID | O15525 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 162 aa / 17.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=194 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=79.5; PDB: 7X5E, 7X5F, 7X5G |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR004827, IPR004826, IPR046347, IPR008917, IPR024 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **92.5/180** | |
| **归一化总分** | | | **51.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- RNA polymerase II transcription regulator complex (GO:0090575)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 194 |
| PubMed broad count | 296 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Activation of the p62-Keap1-NRF2 pathway protects against ferroptosis in hepatocellular carcinoma cells.. *Hepatology (Baltimore, Md.)*. PMID: 26403645
2. Cross-disorder and disease-specific pathways in dementia revealed by single-cell genomics.. *Cell*. PMID: 39265576
3. Small Molecule Inhibitor of NRF2 Selectively Intervenes Therapeutic Resistance in KEAP1-Deficient NSCLC Tumors.. *ACS chemical biology*. PMID: 27552339
4. Farnesoid X receptor protects against cisplatin-induced acute kidney injury by regulating the transcription of ferroptosis-related genes.. *Redox biology*. PMID: 35767918
5. Mechanical signaling via β2 integrin decouples T cell proliferation and differentiation for generating stem cell-like CAR T cells.. *Immunity*. PMID: 40782798

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.5 |
| 高置信度残基 (pLDDT>90) 占比 | 59.3% |
| 置信残基 (pLDDT 70-90) 占比 | 3.1% |
| 中等置信 (pLDDT 50-70) 占比 | 21.0% |
| 低置信 (pLDDT<50) 占比 | 16.7% |
| 有序区域 (pLDDT>70) 占比 | 62.4% |
| 可用 PDB 条目 | 7X5E, 7X5F, 7X5G |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（7X5E, 7X5F, 7X5G）+ AlphaFold高质量预测（pLDDT=79.5），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004827, IPR004826, IPR046347, IPR008917, IPR024874; Pfam: PF03131 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NFE2L2 | 0.999 | 0.899 | — |
| NFE2L1 | 0.998 | 0.842 | — |
| NFE2 | 0.998 | 0.623 | — |
| BACH2 | 0.981 | 0.683 | — |
| MAFK | 0.975 | 0.610 | — |
| DNMT3B | 0.952 | 0.292 | — |
| NFE2L3 | 0.937 | 0.842 | — |
| MAFF | 0.910 | 0.237 | — |
| BACH1 | 0.894 | 0.860 | — |
| CHD8 | 0.877 | 0.309 | — |

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
| 三维结构 | AlphaFold pLDDT=79.5 + PDB: 7X5E, 7X5F, 7X5G | pLDDT=79.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. MAFG — Transcription factor MafG，研究基础较多，新颖性有限。
2. 蛋白大小162 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 194 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 194 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O15525
- Protein Atlas: https://www.proteinatlas.org/ENSG00000197063-MAFG/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MAFG
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O15525
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O15525-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

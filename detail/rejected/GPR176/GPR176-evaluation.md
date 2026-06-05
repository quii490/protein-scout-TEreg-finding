---
type: protein-evaluation
gene: "GPR176"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GPR176 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPR176 |
| 蛋白名称 | G-protein coupled receptor 176 |
| 蛋白大小 | 515 aa / 57.0 kDa |
| UniProt ID | Q14439 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 515 aa / 57.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=30 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR043523, IPR000276, IPR017452; Pfam: PF00001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **99.5/180** | |
| **归一化总分** | | | **55.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- plasma membrane (GO:0005886)
- synapse (GO:0045202)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 30 |
| PubMed broad count | 36 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. GPR176 Promotes Cancer Progression by Interacting with G Protein GNAS to Restrain Cell Mitophagy in Colorectal Cancer.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 36905238
2. GPR176 promotes fibroblast-to-myofibroblast transition in organ fibrosis progression.. *Biochimica et biophysica acta. Molecular cell research*. PMID: 39047914
3. Orphan Class A GPCRs Signature Predicts Prognosis and Immune Microenvironment in Gastric Cancer: GPR176 Drives Tumor Progression Through Wnt Signaling and Macrophage Polarization.. *Mediators of inflammation*. PMID: 40689396
4. Time-Restricted G-Protein Signaling Pathways via GPR176, G(z), and RGS16 Set the Pace of the Master Circadian Clock in the Suprachiasmatic Nucleus.. *International journal of molecular sciences*. PMID: 32709014
5. G-protein-coupled receptor signaling through Gpr176, Gz, and RGS16 tunes time in the center of the circadian clock [Review].. *Endocrine journal*. PMID: 28502923

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.5 |
| 高置信度残基 (pLDDT>90) 占比 | 19.4% |
| 置信残基 (pLDDT 70-90) 占比 | 33.8% |
| 中等置信 (pLDDT 50-70) 占比 | 14.0% |
| 低置信 (pLDDT<50) 占比 | 32.8% |
| 有序区域 (pLDDT>70) 占比 | 53.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=66.5），有序残基占 53.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR043523, IPR000276, IPR017452; Pfam: PF00001 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GPR150 | 0.697 | 0.000 | — |
| GPR27 | 0.649 | 0.000 | — |
| GPR17 | 0.631 | 0.050 | — |
| GPR25 | 0.630 | 0.000 | — |
| GPR45 | 0.618 | 0.000 | — |
| GNAS | 0.618 | 0.142 | — |
| FSIP1 | 0.610 | 0.000 | — |
| GPR20 | 0.584 | 0.000 | — |
| GNAZ | 0.580 | 0.125 | — |
| GPR153 | 0.570 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=66.5 + PDB: 无 | pLDDT=66.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GPR176 — G-protein coupled receptor 176，非常新颖，仅有少数基础研究。
2. 蛋白大小515 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 30 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=66.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q14439
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166073-GPR176/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPR176
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14439
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q14439-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

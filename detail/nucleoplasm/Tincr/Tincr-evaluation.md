---
type: protein-evaluation
gene: "Tincr"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## Tincr 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | Tincr / LINC00036, NCRNA00036, PLAC2 |
| 蛋白名称 | Ubiquitin domain-containing protein TINCR |
| 蛋白大小 | 87 aa / 10.1 kDa |
| UniProt ID | A0A2R8Y7D0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: 暂无HPA定位数据; UniProt: Nucleus; Cell junction; Cytoplasm |
| 蛋白大小 | 5/10 | ×1 | 5 | 87 aa / 10.1 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=79 篇 (≤80→4) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=76.9; PDB: 7MRJ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000626, IPR029071; Pfam: PF00240 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 10 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.5/180** | |
| **归一化总分** | | | **49.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus; Cell junction; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 79 |
| PubMed broad count | 140 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: LINC00036, NCRNA00036, PLAC2 |

**关键文献**:
1. The TINCR ubiquitin-like microprotein is a tumor suppressor in squamous cell carcinoma.. *Nature communications*. PMID: 36899004
2. TINCR inhibits the proliferation and invasion of laryngeal squamous cell carcinoma by regulating miR-210/BTG2.. *BMC cancer*. PMID: 34187411
3. METTL14 suppresses pyroptosis and diabetic cardiomyopathy by downregulating TINCR lncRNA.. *Cell death & disease*. PMID: 35013106
4. lncRNA TINCR knockdown inhibits colon cancer cells via regulation of autophagy.. *Food science & nutrition*. PMID: 37051356
5. TINCR suppresses proliferation and invasion through regulating miR-544a/FBXW7 axis in lung cancer.. *Biomedicine & pharmacotherapy = Biomedecine & pharmacotherapie*. PMID: 29324317

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.9 |
| 高置信度残基 (pLDDT>90) 占比 | 11.7% |
| 置信残基 (pLDDT 70-90) 占比 | 56.7% |
| 中等置信 (pLDDT 50-70) 占比 | 25.0% |
| 低置信 (pLDDT<50) 占比 | 6.7% |
| 有序区域 (pLDDT>70) 占比 | 68.4% |
| 可用 PDB 条目 | 7MRJ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=76.9，有序区 68.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000626, IPR029071; Pfam: PF00240 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| STAU1 | 0.825 | 0.292 | — |
| KRT80 | 0.646 | 0.000 | — |
| ALOX12B | 0.607 | 0.000 | — |
| ALOXE3 | 0.593 | 0.000 | — |
| EZH2 | 0.585 | 0.000 | — |
| ABCA12 | 0.563 | 0.000 | — |
| CASP14 | 0.555 | 0.000 | — |
| ELOVL3 | 0.538 | 0.000 | — |
| UPF1 | 0.505 | 0.000 | — |
| ZNRF4 | 0.418 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 10，IntAct interactions: 0
- 调控相关比例: 1 / 10 = 10%

**评价**: STRING 10 个预测互作，IntAct 0 个实验互作。调控相关配体占比 10%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.9 + PDB: 7MRJ | pLDDT=76.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cell junction; Cytoplasm / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 10 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. Tincr — Ubiquitin domain-containing protein TINCR，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小87 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 79 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A0A2R8Y7D0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000223573-TINCR/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=Tincr
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A0A2R8Y7D0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A0A2R8Y7D0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

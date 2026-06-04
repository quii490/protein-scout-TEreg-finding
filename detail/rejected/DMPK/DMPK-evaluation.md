---
type: protein-evaluation
gene: "DMPK"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DMPK — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=871，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DMPK |
| 蛋白名称 | DMPK (UniProt未获取) |
| 蛋白大小 | 未知 aa / 未知 kDa |
| UniProt ID | DMPK |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/DMPK/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/rejected/DMPK/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 2/10 | ×4 | 8 | HPA: Cytosol; 额外: Vesicles; UniProt: 暂无数据（UniProt获取失败） |
| 📏 蛋白大小 | 5/10 | ×1 | 5 | 未知 aa / 未知 kDa |
| 🆕 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=871 篇 (>100→REJECTED) |
| 🏗️ 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 🧬 调控结构域 | 4/10 | ×2 | 8 | 暂无数据 (UniProt未获取) |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| ➕ 互证加分 | — | max +3 | 0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **42/180** | |
| **归一化总分** | | | **23.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Vesicles | Uncertain |
| UniProt | 暂无数据（UniProt获取失败） | 获取失败 |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- 无 GO-CC 注释 (UniProt未获取)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 871 |
| PubMed broad count | 5025 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Development of an AAV-delivered microRNA gene therapy for myotonic dystrophy type 1.. *Molecular therapy : the journal of the American Society of Gene Therapy*. PMID: 40903903
2. Antisense oligonucleotide targeting DMPK in patients with myotonic dystrophy type 1: a multicentre, randomised, dose-escalation, placebo-controlled, phase 1/2a trial.. *The Lancet. Neurology*. PMID: 36804094
3. Discovery of Risdiplam, a Selective Survival of Motor Neuron-2 ( SMN2) Gene Splicing Modifier for the Treatment of Spinal Muscular Atrophy (SMA).. *Journal of medicinal chemistry*. PMID: 30044619
4. Myotonic disorders.. *Neurology India*. PMID: 18974556
5. AntimiR treatment corrects myotonic dystrophy primary cell defects across several CTG repeat expansions with a dual mechanism of action.. *Science advances*. PMID: 39383229

**评价**: 有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |


**PAE**: AlphaFold 数据未获取，无 PAE 可用。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 暂无数据 (UniProt未获取) |

**染色质调控潜力分析**: 结构域注释稀疏，属新颖蛋白正常现象。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MBNL1 | 0.939 | 0.000 | — |
| CELF1 | 0.925 | 0.046 | — |
| CNBP | 0.916 | 0.049 | — |
| CLCN1 | 0.878 | 0.000 | — |
| MBNL2 | 0.850 | 0.000 | — |
| MBNL3 | 0.845 | 0.000 | — |
| SIX5 | 0.839 | 0.000 | — |
| PLN | 0.835 | 0.299 | — |
| DMWD | 0.811 | 0.067 | — |
| ATP2A1 | 0.754 | 0.071 | — |

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
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | 暂无数据（UniProt获取失败） / Cytosol; 额外: Vesicles | 待确认 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0 / max +3

### 4. 总体评价

**推荐等级**: ⭐ (REJECTED)

**核心优势**:
1. DMPK — DMPK (UniProt未获取)，有一定研究基础，但仍存在niche空间。
2. 蛋白大小未知 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 871 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/DMPK
- Protein Atlas: https://www.proteinatlas.org/ENSG00000104936-DMPK/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DMPK
- AlphaFold: https://alphafold.ebi.ac.uk/entry/DMPK
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 12:16:00





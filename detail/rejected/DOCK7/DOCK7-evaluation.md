---
type: protein-evaluation
gene: "DOCK7"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DOCK7 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DOCK7 / KIAA1771 |
| 蛋白名称 | Dedicator of cytokinesis protein 7 |
| 蛋白大小 | 2140 aa / 242.6 kDa |
| UniProt ID | Q96N67 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell projection, axon |
| 📏 蛋白大小 | 2/10 | ×1 | 2 | 2140 aa / 242.6 kDa |
| 🆕 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=63 篇 (≤80→4) |
| 🏗️ 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=73.9; PDB: 6AJ4, 6AJL |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR037808, IPR027007, IPR035892, IPR026791, IPR021 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell projection, axon | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- axon (GO:0030424)
- basal part of cell (GO:0045178)
- focal adhesion (GO:0005925)
- growth cone (GO:0030426)
- neuron projection (GO:0043005)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 63 |
| PubMed broad count | 118 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1771 |

**关键文献**:
1. The Interaction between the DOCK7 Protein and the E2 Protein of Classical Swine Fever Virus Is Not Involved with Viral Replication or Pathogenicity.. *Viruses*. PMID: 38257770
2. Nbeal2 interacts with Dock7, Sec16a, and Vac14.. *Blood*. PMID: 29187380
3. Healthy longevity-associated protein improves cardiac function in murine models of cardiomyopathy with preserved ejection fraction.. *Cardiovascular diabetology*. PMID: 39501278
4. Association between the DOCK7, PCSK9 and GALNT2 Gene Polymorphisms and Serum Lipid levels.. *Scientific reports*. PMID: 26744084
5. Characteristic facial features and cortical blindness distinguish the DOCK7-related epileptic encephalopathy.. *Molecular genetics & genomic medicine*. PMID: 33471954

**评价**: 有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.9 |
| 高置信度残基 (pLDDT>90) 占比 | 26.6% |
| 置信残基 (pLDDT 70-90) 占比 | 45.4% |
| 中等置信 (pLDDT 50-70) 占比 | 7.4% |
| 低置信 (pLDDT<50) 占比 | 20.6% |
| 有序区域 (pLDDT>70) 占比 | 72.0% |
| 可用 PDB 条目 | 6AJ4, 6AJL |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（6AJ4, 6AJL）+ AlphaFold高质量预测（pLDDT=73.9），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037808, IPR027007, IPR035892, IPR026791, IPR021816; Pfam: PF06920, PF20422, PF20421 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDC42 | 0.994 | 0.946 | — |
| LRCH3 | 0.976 | 0.829 | — |
| MYO6 | 0.934 | 0.776 | — |
| DOCK8 | 0.882 | 0.790 | — |
| LRCH1 | 0.835 | 0.781 | — |
| RAC1 | 0.776 | 0.459 | — |
| CRK | 0.753 | 0.000 | — |
| DHX37 | 0.718 | 0.000 | — |
| ANGPTL3 | 0.683 | 0.000 | — |
| USP7 | 0.679 | 0.420 | — |

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
| 三维结构 | AlphaFold pLDDT=73.9 + PDB: 6AJ4, 6AJL | pLDDT=73.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell projection, axon / 暂无HPA定位数据 | 一致 |
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
1. DOCK7 — Dedicator of cytokinesis protein 7，有一定研究基础，但仍存在niche空间。
2. 蛋白大小2140 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 63 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96N67
- Protein Atlas: https://www.proteinatlas.org/ENSG00000116641-DOCK7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DOCK7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96N67
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 12:18:40

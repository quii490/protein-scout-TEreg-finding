---
type: protein-evaluation
gene: "BRI3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BRI3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BRI3 / 无 |
| 蛋白名称 | Membrane protein BRI3 |
| 蛋白大小 | 125 aa / 13.6 kDa |
| UniProt ID | O95415 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 03:44:27 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | UniProt: Lysosome membrane, Cytoplasm... |
| 蛋白大小 | 7/10 | x1 | 7 | 125 aa / 13.6 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=34 篇 (21-40->8) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=65.1 |
| 调控结构域 | 5/10 | x2 | 10 | InterPro: 1; Pfam: 1; IPR019317 |
| PPI 网络 | 6/10 | x3 | 18 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 0.5 | 结构域 + AlphaFold 质量: +0.5 |
| **原始总分** | | | **112.5/180** | |
| **归一化总分 (/1.83)** | | | **61.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 无数据; 额外: 无 | N/A |
| UniProt | Lysosome membrane, Cytoplasm, perinuclear region, Cytoplasm, Nucleus | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**GO Cellular Component**:
- azurophil granule membrane (GO:0035577)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)
- plasma membrane (GO:0005886)

**结论**: 核定位证据一般，存在混合定位或不一致信号，需进一步实验验证。

#### 3.2 蛋白大小评估

**评价**: 125 aa，蛋白较小，但仍在可操作范围。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 34 |
| PubMed broad count | 39 |

**关键文献**:
1. The Bri2 and Bri3 BRICHOS Domains Interact Differently with Aβ(42) and Alzheimer Amyloid Plaques.. *Journal of Alzheimer's disease reports*. PMID: 30480246
2. BRI2 and BRI3 are functionally distinct phosphoproteins.. *Cellular signalling*. PMID: 26515131
3. BRI3 inhibits amyloid precursor protein processing in a mechanistically distinct manner from its homologue dementia gene BRI2.. *The Journal of biological chemistry*. PMID: 19366692
4. Beta-amyloid protein converting enzyme 1 and brain-specific type II membrane protein BRI3: binding partners processed by furin.. *Journal of neurochemistry*. PMID: 15606899
5. Recombinant Bri3 BRICHOS domain is a molecular chaperone with effect against amyloid formation and non-fibrillar protein aggregation.. *Scientific reports*. PMID: 32555390

**评价**: 较高新颖性，研究尚处早期阶段（PubMed 21-40篇）。新颖性评分 8/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.1 |
| 高置信度残基 (pLDDT>90) 占比 | 3.2% |
| 置信残基 (pLDDT 70-90) 占比 | 41.6% |
| 中等置信 (pLDDT 50-70) 占比 | 35.2% |
| 低置信 (pLDDT<50) 占比 | 20.0% |
| 有序区域 (pLDDT>70) 占比 | 44.8% |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: AlphaFold中等质量预测（pLDDT=65.1），存在部分低置信区域。三维结构评分 7/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019317; Pfam: PF10164 |

**染色质调控潜力分析**: 存在 2 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作**: 暂无数据或查询失败。

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RNF7 | two hybrid pooling approach | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 |
| ITM2C | two hybrid pooling approach | pubmed:16169070|imex:IM-16517|mint:MINT-5217955 |
| MTNR1B | tandem affinity purification | pubmed:17215244|imex:IM-19124 |
| M | anti tag coimmunoprecipitation | imex:IM-27674|pubmed:33208464 |
| OLFM4 | validated two hybrid | pubmed:32296183|imex:IM-25472 |
| CCL4L1 | validated two hybrid | pubmed:32296183|imex:IM-25472 |
| FNDC9 | validated two hybrid | pubmed:32296183|imex:IM-25472 |
| UPK2 | two hybrid array | pubmed:32296183|imex:IM-25472 |
| CXCL9 | validated two hybrid | pubmed:32296183|imex:IM-25472 |
| TMEM216 | proximity-dependent biotin identificatio | imex:IM-24512|pubmed:26638075 |

**PPI 互证分析**:
- 仅 IntAct 有数据 (15 interactions)

**评价**: 互作网络中等：STRING 0 预测 + IntAct 15 实验互作。PPI 评分 6/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold v6 | pLDDT=65.1 | 单一来源 |
| 定位 | UniProt | Cytoplasm, perinuclear region, Nucleus | 单一来源 |
| PPI | IntAct | 15 interactions | 单一来源 |

**互证加分明细**:
- 结构域 + AlphaFold 质量: +0.5
**总分**: +0.5 / max +3

### 4. 总体评价

**归一化总分**: 61.5/100

**核心优势**:
1. BRI3 -- Membrane protein BRI3，较高新颖性，研究尚处早期阶段。
2. 存在 2 个已知结构域，有明确的结构-功能切入点。

**风险/不确定性**:
1. 核定位信号较弱或存在矛盾（评分 4/10），需IF实验验证
2. 暂无PDB实验结构，结构证据完全依赖AlphaFold预测

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] 考虑通过AlphaFold预测 + MD模拟获取结构信息

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/O95415
- Protein Atlas: https://www.proteinatlas.org/search/BRI3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BRI3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95415
- STRING: https://string-db.org/network/9606.BRI3
- Packet data timestamp: 2026-06-03 03:44:27

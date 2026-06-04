---
type: protein-evaluation
gene: "BICRAL"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BICRAL 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BICRAL / GLTSCR1L, KIAA0240 |
| 蛋白名称 | BRD4-interacting chromatin-remodeling complex-associated protein-like |
| 蛋白大小 | 1079 aa / 115.1 kDa |
| UniProt ID | Q6AI39 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 03:37:32 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 10/10 | x4 | 40 | HPA: Nucleoplasm |
| 蛋白大小 | 7/10 | x1 | 7 | 1079 aa / 115.1 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=0 篇 (<=20->10) |
| 三维结构 | 3/10 | x3 | 9 | AlphaFold v6 pLDDT=45.7 |
| 调控结构域 | 5/10 | x2 | 10 | InterPro: 2; Pfam: 1; IPR052438, IPR015671 |
| PPI 网络 | 10/10 | x3 | 30 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 0.5 | STRING + IntAct 双源验证: +0.5 |
| **原始总分** | | | **146.5/180** | |
| **归一化总分 (/1.83)** | | | **80.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoplasm, Cytosol | Approved |

**IF 图像说明**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**GO Cellular Component**:
- chromatin (GO:0000785)
- GBAF complex (GO:0140288)
- nucleoplasm (GO:0005654)
- SWI/SNF complex (GO:0016514)

**结论**: 核定位证据充分，多个数据源一致支持核定位，定位特异性高。

#### 3.2 蛋白大小评估

**评价**: 1079 aa，蛋白偏大（> 800 aa），表达纯化有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GLTSCR1L, KIAA0240 |

**评价**: 极度新颖，几乎未被系统研究（PubMed <= 20篇）。新颖性评分 10/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 45.7 |
| 高置信度残基 (pLDDT>90) 占比 | 6.8% |
| 置信残基 (pLDDT 70-90) 占比 | 10.8% |
| 中等置信 (pLDDT 50-70) 占比 | 4.4% |
| 低置信 (pLDDT<50) 占比 | 78.0% |
| 有序区域 (pLDDT>70) 占比 | 17.6% |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: AlphaFold低质量预测（pLDDT=45.7），大部分区域无序。三维结构评分 3/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052438, IPR015671; Pfam: PF15249 |

**染色质调控潜力分析**: 存在 3 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score > 0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BRD9 | 0.999 | 0.606 | -- |
| SMARCD1 | 0.994 | 0.784 | -- |
| BCL7C | 0.988 | 0.669 | -- |
| BCL7A | 0.983 | 0.703 | -- |
| ACTL6A | 0.975 | 0.332 | -- |
| BICRA | 0.974 | 0.000 | -- |
| SMARCC1 | 0.974 | 0.045 | -- |
| SMARCA4 | 0.974 | 0.297 | -- |
| SMARCA2 | 0.967 | 0.425 | -- |
| BCL7B | 0.965 | 0.000 | -- |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CACHD1 | two hybrid | pubmed:12421765 |
| CDC5L | two hybrid | pubmed:17043677|imex:IM-16650 |
| DTNBP1 | two hybrid | pubmed:17043677|imex:IM-16650 |
| ENSP00000377723.1 | two hybrid pooling approach | imex:IM-13779|pubmed:20711500 |
| rpoB | two hybrid pooling approach | imex:IM-13779|pubmed:20711500 |
| dinG | two hybrid pooling approach | imex:IM-13779|pubmed:20711500 |
| A0A0F7RF31 | two hybrid pooling approach | imex:IM-13779|pubmed:20711500 |
| A0A0F7RCF4 | two hybrid pooling approach | imex:IM-13779|pubmed:20711500 |
| NFYC | two hybrid pooling approach | pubmed:20936779|imex:IM-17049 |
| degP | two hybrid pooling approach | imex:IM-13779|pubmed:20711500 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15

**评价**: 互作网络丰富：STRING 15 预测 + IntAct 15 实验互作。PPI 评分 10/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold v6 | pLDDT=45.7 | 单一来源 |
| 定位 | HPA | Nucleoplasm | 单一来源 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- STRING + IntAct 双源验证: +0.5
**总分**: +0.5 / max +3

### 4. 总体评价

**归一化总分**: 80.1/100

**核心优势**:
1. BICRAL -- BRD4-interacting chromatin-remodeling complex-associated protein-like，极度新颖，几乎未被系统研究（PubMed <= 20篇）。
2. 存在 3 个已知结构域，有明确的结构-功能切入点。
3. 核定位信号明确，多个数据源一致支持。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. AlphaFold pLDDT 较低（45.7），存在显著无序区
3. 暂无PDB实验结构，结构证据完全依赖AlphaFold预测

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] 考虑通过AlphaFold预测 + MD模拟获取结构信息

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q6AI39
- Protein Atlas: https://www.proteinatlas.org/search/BICRAL
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BICRAL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6AI39
- STRING: https://string-db.org/network/9606.BICRAL
- Packet data timestamp: 2026-06-03 03:37:32

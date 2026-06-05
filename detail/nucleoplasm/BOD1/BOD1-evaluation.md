---
type: protein-evaluation
gene: "BOD1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BOD1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BOD1 / FAM44B |
| 蛋白名称 | Biorientation of chromosomes in cell division protein 1 |
| 蛋白大小 | 185 aa / 19.2 kDa |
| UniProt ID | Q96IK1 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 03:41:48 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | UniProt: Cytoplasm, cytoskeleton, mic... |
| 蛋白大小 | 7/10 | x1 | 7 | 185 aa / 19.2 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=19 篇 (<=20->10) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=73.6 |
| 调控结构域 | 5/10 | x2 | 10 | InterPro: 2; Pfam: 1; IPR055264, IPR043244 |
| PPI 网络 | 10/10 | x3 | 30 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 1.0 | STRING + IntAct 双源验证: +0.5; 结构域 + AlphaFold 质量: +0.5 |
| **原始总分** | | | **135.0/180** | |
| **归一化总分 (/1.83)** | | | **73.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 无数据; 额外: 无 | N/A |
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome, Chromosome, centromere, kinetochore | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**GO Cellular Component**:
- centrosome (GO:0005813)
- nucleoplasm (GO:0005654)
- outer kinetochore (GO:0000940)
- Set1C/COMPASS complex (GO:0048188)
- spindle microtubule (GO:0005876)
- spindle pole (GO:0000922)

**结论**: 核定位证据一般，存在混合定位或不一致信号，需进一步实验验证。

#### 3.2 蛋白大小评估

**评价**: 185 aa，蛋白较小，但仍在可操作范围。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 19 |
| PubMed broad count | 33 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FAM44B |

**关键文献**:
1. Chromosome orientation.. *The Journal of cell biology*. PMID: 17954603
2. A busy BOD1-y: the diverse functions of an intracellular signaling regulatory protein family.. *Biochemical Society transactions*. PMID: 41417274
3. Bod1 regulates protein phosphatase 2A at mitotic kinetochores.. *Nature communications*. PMID: 24157919
4. BOD1 Is Required for Cognitive Function in Humans and Drosophila.. *PLoS genetics*. PMID: 27166630
5. Bod1, a novel kinetochore protein required for chromosome biorientation.. *The Journal of cell biology*. PMID: 17938248

**评价**: 极度新颖，几乎未被系统研究（PubMed <= 20篇）。新颖性评分 10/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.6 |
| 高置信度残基 (pLDDT>90) 占比 | 40.0% |
| 置信残基 (pLDDT 70-90) 占比 | 24.9% |
| 中等置信 (pLDDT 50-70) 占比 | 7.0% |
| 低置信 (pLDDT<50) 占比 | 28.1% |
| 有序区域 (pLDDT>70) 占比 | 64.9% |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold中等质量预测（pLDDT=73.6），存在部分低置信区域。三维结构评分 7/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR055264, IPR043244; Pfam: PF05205 |

**染色质调控潜力分析**: 存在 3 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score > 0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SKA3 | 0.933 | 0.000 | -- |
| SKA1 | 0.932 | 0.000 | -- |
| SKA2 | 0.927 | 0.000 | -- |
| BUB1B | 0.924 | 0.000 | -- |
| SPDL1 | 0.917 | 0.000 | -- |
| CENPF | 0.915 | 0.000 | -- |
| CXXC1 | 0.908 | 0.612 | -- |
| WDR5 | 0.887 | 0.596 | -- |
| RBBP5 | 0.875 | 0.489 | -- |
| ASH2L | 0.864 | 0.481 | -- |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RpL15 | two hybrid | pubmed:14605208|imex:IM-16524|mint:MINT-5216804 |
| Sf3a2 | two hybrid | pubmed:14605208|imex:IM-16524|mint:MINT-5216804 |
| CCT2 | two hybrid | pubmed:14605208|imex:IM-16524|mint:MINT-5216804 |
| Bin1 | two hybrid | pubmed:14605208|imex:IM-16524|mint:MINT-5216804 |
| PPO2 | two hybrid | pubmed:14605208|imex:IM-16524|mint:MINT-5216804 |
| GILT1 | two hybrid | pubmed:14605208|imex:IM-16524|mint:MINT-5216804 |
| eIF3m | two hybrid | pubmed:14605208|imex:IM-16524|mint:MINT-5216804 |
| EBI-139033 | two hybrid | pubmed:14605208|imex:IM-16524|mint:MINT-5216804 |
| CG32920 | two hybrid | pubmed:14605208|imex:IM-16524|mint:MINT-5216804 |
| PpD3 | anti tag coimmunoprecipitation | imex:IM-16527|pubmed:25294943 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15

**评价**: 互作网络丰富：STRING 15 预测 + IntAct 15 实验互作。PPI 评分 10/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold v6 | pLDDT=73.6 | 单一来源 |
| 定位 | -- | 无明确核定位数据 | -- |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
**总分**: +1.0 / max +3

### 4. 总体评价

**归一化总分**: 73.8/100

**核心优势**:
1. BOD1 -- Biorientation of chromosomes in cell division protein 1，极度新颖，几乎未被系统研究（PubMed <= 20篇）。
2. 存在 3 个已知结构域，有明确的结构-功能切入点。

**风险/不确定性**:
1. 核定位信号较弱或存在矛盾（评分 4/10），需IF实验验证
2. 暂无PDB实验结构，结构证据完全依赖AlphaFold预测

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] 考虑通过AlphaFold预测 + MD模拟获取结构信息

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q96IK1
- Protein Atlas: https://www.proteinatlas.org/search/BOD1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BOD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96IK1
- STRING: https://string-db.org/network/9606.BOD1
- Packet data timestamp: 2026-06-03 03:41:48

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96IK1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

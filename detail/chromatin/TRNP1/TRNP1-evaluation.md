---
type: protein-evaluation
gene: "TRNP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TRNP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TRNP1 / C1orf225, TRNP |
| 蛋白名称 | TMF-regulated nuclear protein 1 |
| 蛋白大小 | 227 aa / 23.5 kDa |
| UniProt ID | Q6NT89 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 227 aa / 23.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR040266 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 9 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **134.0/180** | |
| **归一化总分** | | | **74.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- euchromatin (GO:0000791)
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 22 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C1orf225, TRNP |

**关键文献**:
1. Regulatory and coding sequences of TRNP1 co-evolve with brain size and cortical folding in mammals.. *eLife*. PMID: 36947129
2. Resequencing of the TMF-1 (TATA Element Modulatory Factor) regulated protein (TRNP1) gene in domestic and wild canids.. *Canine medicine and genetics*. PMID: 37968761
3. Trnp1 organizes diverse nuclear membrane-less compartments in neural stem cells.. *The EMBO journal*. PMID: 32627867
4. Gsg1, Trnp1, and Tmem215 Mark Subpopulations of Bipolar Interneurons in the Mouse Retina.. *Investigative ophthalmology & visual science*. PMID: 28199486
5. Identification of fatty acid metabolism-related clusters and immune infiltration features in hepatocellular carcinoma.. *Aging*. PMID: 36881382

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.9 |
| 高置信度残基 (pLDDT>90) 占比 | 28.6% |
| 置信残基 (pLDDT 70-90) 占比 | 11.5% |
| 中等置信 (pLDDT 50-70) 占比 | 38.8% |
| 低置信 (pLDDT<50) 占比 | 21.1% |
| 有序区域 (pLDDT>70) 占比 | 40.1% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=68.9），有序残基占 40.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR040266 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ARHGAP11B | 0.630 | 0.000 | — |
| ARHGAP11B-2 | 0.623 | 0.000 | — |
| TMEM14B | 0.473 | 0.000 | — |
| UBTF | 0.451 | 0.000 | — |
| PLEKHG6 | 0.448 | 0.000 | — |
| C6orf132 | 0.434 | 0.000 | — |
| SEMG1 | 0.414 | 0.000 | — |
| HAPLN1 | 0.407 | 0.000 | — |
| NANOS1 | 0.402 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Tmf1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-24854|pubmed:16792503 |
| P | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:unassigned2293|imex:IM- |
| SNAP29 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 9，IntAct interactions: 3
- 调控相关比例: 0 / 9 = 0%

**评价**: STRING 9 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.9 + PDB: 无 | pLDDT=68.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 9 + 3 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TRNP1 — TMF-regulated nuclear protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小227 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=68.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6NT89
- Protein Atlas: https://www.proteinatlas.org/ENSG00000253368-TRNP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TRNP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6NT89
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

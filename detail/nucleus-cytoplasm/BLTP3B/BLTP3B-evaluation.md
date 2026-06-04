---
type: protein-evaluation
gene: "BLTP3B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BLTP3B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BLTP3B / KIAA0701, SHIP164, UHRF1BP1L |
| 蛋白名称 | Bridge-like lipid transfer protein family member 3B |
| 蛋白大小 | 1464 aa / 164.2 kDa |
| UniProt ID | A0JNW5 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 03:39:18 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 10/10 | x4 | 40 | HPA: Nucleoplasm; UniProt: Cytoplasm,... |
| 蛋白大小 | 4/10 | x1 | 4 | 1464 aa / 164.2 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=1 篇 (<=20->10) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=66.8 |
| 调控结构域 | 5/10 | x2 | 10 | InterPro: 1; Pfam: 1; IPR026728 |
| PPI 网络 | 6/10 | x3 | 18 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 1.0 | 多库定位一致 (3源): +0.5; 结构域 + AlphaFold 质量: +0.5 |
| **原始总分** | | | **144.0/180** | |
| **归一化总分 (/1.83)** | | | **78.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoplasm, Vesicles, Cytosol | Uncertain |
| UniProt | Cytoplasm, cytosol, Early endosome | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**GO Cellular Component**:
- cytosol (GO:0005829)
- early endosome (GO:0005769)

**结论**: 核定位证据充分，多个数据源一致支持核定位，定位特异性高。

#### 3.2 蛋白大小评估

**评价**: 1464 aa，蛋白偏大（> 1200 aa），表达纯化难度增加，但结构域丰富。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1 |
| PubMed broad count | 1 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0701, SHIP164, UHRF1BP1L |

**关键文献**:
1. BLTP3A is associated with membranes of the late endocytic pathway and is an effector of CASM.. *bioRxiv : the preprint server for biology*. PMID: 39386594

**评价**: 极度新颖，几乎未被系统研究（PubMed <= 20篇）。新颖性评分 10/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.8 |
| 高置信度残基 (pLDDT>90) 占比 | 29.2% |
| 置信残基 (pLDDT 70-90) 占比 | 28.8% |
| 中等置信 (pLDDT 50-70) 占比 | 6.5% |
| 低置信 (pLDDT<50) 占比 | 35.5% |
| 有序区域 (pLDDT>70) 占比 | 58.0% |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: AlphaFold中等质量预测（pLDDT=66.8），存在部分低置信区域。三维结构评分 7/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026728; Pfam: PF24917 |

**染色质调控潜力分析**: 存在 2 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作**: 暂无数据或查询失败。

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| wecF | two hybrid pooling approach | imex:IM-13779|pubmed:20711500 |
| ATXN1 | two hybrid prey pooling approach | imex:IM-17394|pubmed:23275563 |
| RAB5A | proximity-dependent biotin identificatio | pubmed:29568061|imex:IM-26301 |
| TGOLN2 | proximity-dependent biotin identificatio | pubmed:29568061|imex:IM-26301 |
| DISC1 | two hybrid fragment pooling approach | pubmed:31413325|imex:IM-26801 |
| PDGFRB | pull down | doi:10.1016/j.cell.2019.09.008|pubmed:31585087|imex:IM-27423 |
| SCML1 | inference by socio-affinity scoring | pubmed:unassigned1312 |
| COBLL1 | inference by socio-affinity scoring | pubmed:unassigned1312 |
| CDADC1 | inference by socio-affinity scoring | pubmed:unassigned1312 |
| AMOTL1 | inference by socio-affinity scoring | pubmed:unassigned1312 |

**PPI 互证分析**:
- 仅 IntAct 有数据 (15 interactions)

**评价**: 互作网络中等：STRING 0 预测 + IntAct 15 实验互作。PPI 评分 6/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold v6 | pLDDT=66.8 | 单一来源 |
| 定位 | HPA | Nucleoplasm | 单一来源 |
| PPI | IntAct | 15 interactions | 单一来源 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- 结构域 + AlphaFold 质量: +0.5
**总分**: +1.0 / max +3

### 4. 总体评价

**归一化总分**: 78.7/100

**核心优势**:
1. BLTP3B -- Bridge-like lipid transfer protein family member 3B，极度新颖，几乎未被系统研究（PubMed <= 20篇）。
2. 存在 2 个已知结构域，有明确的结构-功能切入点。
3. 核定位信号明确，多个数据源一致支持。

**风险/不确定性**:
1. PubMed 1 篇，研究基础极有限，功能注释不完整
2. 暂无PDB实验结构，结构证据完全依赖AlphaFold预测
3. 蛋白偏大（1464 aa），表达纯化难度大

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] 考虑通过AlphaFold预测 + MD模拟获取结构信息

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/A0JNW5
- Protein Atlas: https://www.proteinatlas.org/search/BLTP3B
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BLTP3B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A0JNW5
- STRING: https://string-db.org/network/9606.BLTP3B
- Packet data timestamp: 2026-06-03 03:39:18

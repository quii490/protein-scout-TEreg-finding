---
type: protein-evaluation
gene: "DNAJB8"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DNAJB8 — REJECTED (核定位证据不足 (核定位得分 3/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNAJB8 |
| 蛋白名称 | DnaJ homolog subfamily B member 8 |
| 蛋白大小 | 232 aa / 25.7 kDa |
| UniProt ID | Q8NHS0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 3/10 | x4 | 12 | HPA: 暂无HPA定位数据; UniProt: 无注释 |
| 蛋白大小 | 10/10 | x1 | 10 | 232 aa / 25.7 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=29 篇 (<=40->8) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=64.9; PDB: 无 |
| 调控结构域 | 5/10 | x2 | 10 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **99/180** | |
| **归一化总分** | | | **55.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | No data |
| UniProt | 无注释 | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据不足，HPA与UniProt存在矛盾或缺乏核注释。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 29 |
| PubMed broad count | 29 |
| 别名(未计入scoring) |  |

**关键文献**:
1. The heat shock protein DNAJB8 inhibits pseudorabies virus replication by autophagy.. *Vet Microbiol*. PMID: 38936156
2. Factors affecting protein recovery during Hsp40 affinity profiling.. *Anal Bioanal Chem*. PMID: 38850318
3. DNAJB8 oligomerization is mediated by an aromatic-rich motif that is dispensable for substrate activity.. *Structure*. PMID: 38508190
4. DNAJB8 oligomerization is mediated by an aromatic-rich motif that is dispensable for substrate activity.. *bioRxiv*. PMID: 36945632
5. Cellular Exposure to Chloroacetanilide Herbicides Induces Distinct Protein Destabilization Profiles.. *ACS Chem Biol*. PMID: 37427419

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.9 |
| 高置信度残基 (pLDDT>90) 占比 | 4.3% |
| 置信残基 (pLDDT 70-90) 占比 | 43.1% |
| 中等置信 (pLDDT 50-70) 占比 | 22.0% |
| 低置信 (pLDDT<50) 占比 | 30.6% |
| 有序区域 (pLDDT>70) 占比 | 47.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=64.9），有序残基占 47.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HSPA1B | 0.000 | 0.000 | — |
| HSPA4 | 0.000 | 0.000 | — |
| HSPA8 | 0.000 | 0.000 | — |
| HSPA9 | 0.000 | 0.000 | — |
| HSPA6 | 0.000 | 0.000 | — |
| HSPA2 | 0.000 | 0.000 | — |
| HSPA1L | 0.000 | 0.000 | — |
| HSPA1A | 0.000 | 0.000 | — |
| HSPA5 | 0.000 | 0.000 | — |
| HSPA14 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 25，IntAct interactions: 0
- 调控相关比例: 2 / 20 = 10%

**评价**: STRING 25 个预测互作，IntAct 0 个实验互作。调控相关配体占比 10%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.9 + PDB: 无 | pLDDT=64.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 25 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0 / max +3

### 4. 总体评价

**推荐等级**: *** (REJECTED)

**核心优势**:
1. DNAJB8 -- DnaJ homolog subfamily B member 8，非常新颖，仅有少数基础研究。
2. 蛋白大小232 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 29 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=64.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（<=3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NHS0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000179407-DNAJB8/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNAJB8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NHS0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NHS0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

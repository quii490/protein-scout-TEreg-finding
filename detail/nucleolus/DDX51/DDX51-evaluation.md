---
type: protein-evaluation
gene: "DDX51"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DDX51 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DDX51 |
| 蛋白名称 | ATP-dependent RNA helicase DDX51 |
| 蛋白大小 | 666 aa / 72.5 kDa |
| UniProt ID | Q8N8A6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | x4 | 32 | HPA: Nucleoplasm, Nucleoli; 额外: Cytosol; UniProt: Nucleus, nucleolus |
| 蛋白大小 | 10/10 | x1 | 10 | 666 aa / 72.5 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=10 篇 (<=20->10) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=73.6; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **135.5/180** | |
| **归一化总分** | | | **75.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli; 额外: Cytosol | Approved |
| UniProt | Nucleus, nucleolus | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 10 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Genome-Wide Association Study Reveals the Genetic Architecture of Growth and Meat Production Traits in a Chicken F(2) Resource Population.. *Genes (Basel)*. PMID: 39457370
2. Where all the Roads Meet? A Crossover Perspective on Host Factors Regulating SARS-CoV-2 infection.. *J Mol Biol*. PMID: 34914966
3. Knockdown of DEAD-box 51 inhibits tumor growth of esophageal squamous cell carcinoma via the PI3K/AKT pathway.. *World J Gastroenterol*. PMID: 35125830
4. Phosphorylated protein modification analysis on normal liver and Exo-celiac liver of Glyptosternum maculatum.. *J Fish Biol*. PMID: 34392541
5. DDX51 gene promotes proliferation by activating Wnt/β-catenin signaling in breast cancer.. *Int J Clin Exp Pathol*. PMID: 31966432

**评价**: 极度新颖，几乎未被系统研究（PubMed <=20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.6 |
| 高置信度残基 (pLDDT>90) 占比 | 35.1% |
| 置信残基 (pLDDT 70-90) 占比 | 31.4% |
| 中等置信 (pLDDT 50-70) 占比 | 10.7% |
| 低置信 (pLDDT<50) 占比 | 22.8% |
| 有序区域 (pLDDT>70) 占比 | 66.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=73.6，有序区 66.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NOL8 | 0.000 | 0.000 | — |
| RRP8 | 0.000 | 0.000 | — |
| NOP58 | 0.000 | 0.000 | — |
| RBM34 | 0.000 | 0.000 | — |
| GTPBP4 | 0.000 | 0.000 | — |
| NOL10 | 0.000 | 0.000 | — |
| NOP56 | 0.000 | 0.000 | — |
| BOP1 | 0.000 | 0.000 | — |
| PDCD11 | 0.000 | 0.000 | — |
| WDR12 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q8N8A6 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.6 + PDB: 无 | pLDDT=73.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus, nucleolus / Nucleoplasm, Nucleoli; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ****

**核心优势**:
1. DDX51 -- ATP-dependent RNA helicase DDX51，极度新颖，几乎未被系统研究（PubMed <=20篇）。
2. 蛋白大小666 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N8A6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000185163-DDX51/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DDX51
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N8A6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N8A6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

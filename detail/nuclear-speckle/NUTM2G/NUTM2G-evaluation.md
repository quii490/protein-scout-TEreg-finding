---
type: protein-evaluation
gene: "NUTM2G"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NUTM2G 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NUTM2G / FAM22G |
| 蛋白名称 | NUT family member 2G |
| 蛋白大小 | 741 aa / 79.0 kDa |
| UniProt ID | Q5VZR2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear bodies; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 741 aa / 79.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=50.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR024310, IPR024309; Pfam: PF12881 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129/180** | |
| **归一化总分** | | | **71.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 2 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FAM22G |

**关键文献**:
1. MAD::NUT Fusion Sarcoma: A Sarcoma Class With NUTM1, NUTM2A, and NUTM2G Fusions and Possibly Distinctive Subtypes.. *Modern pathology : an official journal of the United States and Canadian Academy of Pathology, Inc*. PMID: 39921028
2. Genomic profiling of BCOR-rearranged uterine sarcomas reveals novel gene fusion partners, frequent CDK4 amplification and CDKN2A loss.. *Gynecologic oncology*. PMID: 32156473

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 50.9 |
| 高置信度残基 (pLDDT>90) 占比 | 10.1% |
| 置信残基 (pLDDT 70-90) 占比 | 12.6% |
| 中等置信 (pLDDT 50-70) 占比 | 7.3% |
| 低置信 (pLDDT<50) 占比 | 70.0% |
| 有序区域 (pLDDT>70) 占比 | 22.7% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=50.9），有序残基占 22.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR024310, IPR024309; Pfam: PF12881 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RTL9 | 0.669 | 0.058 | — |
| NUGGC | 0.626 | 0.045 | — |
| RALGPS1 | 0.596 | 0.000 | — |
| OR2T27 | 0.595 | 0.000 | — |
| MAP7D2 | 0.590 | 0.000 | — |
| ZC3H7B | 0.556 | 0.092 | — |
| KRTAP9-1 | 0.518 | 0.000 | — |
| MCRIP1 | 0.514 | 0.000 | — |
| MROH8 | 0.507 | 0.000 | — |
| ZNF169 | 0.501 | 0.071 | — |

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
| 三维结构 | AlphaFold pLDDT=50.9 + PDB: 无 | pLDDT=50.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nuclear bodies | 待确认 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. NUTM2G — NUT family member 2G，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小741 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=50.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5VZR2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000188152-NUTM2G/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NUTM2G
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5VZR2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

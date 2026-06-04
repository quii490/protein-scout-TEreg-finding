---
type: protein-evaluation
gene: "INSYN1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## INSYN1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | INSYN1 / C15orf59 |
| 蛋白名称 | Inhibitory synaptic factor 1 |
| 蛋白大小 | 293 aa / 31.9 kDa |
| UniProt ID | Q2T9L4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Cytosol; UniProt: Postsynaptic density |
| 蛋白大小 | 10/10 | ×1 | 10 | 293 aa / 31.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR027997; Pfam: PF15252 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | Postsynaptic density | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- GABA-ergic synapse (GO:0098982)
- postsynaptic density (GO:0014069)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 5 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C15orf59 |

**关键文献**:
1. Essential role for InSyn1 in dystroglycan complex integrity and cognitive behaviors in mice.. *eLife*. PMID: 31829939
2. Identifying Synaptic Proteins by In Vivo BioID from Mouse Brain.. *Methods in molecular biology (Clifton, N.J.)*. PMID: 31124092
3. Investigating the genetic imprint of long body length, high lean meat rate, high fertility and long gestation period in Danish Landrace pigs.. *BMC genomics*. PMID: 41023780

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.5 |
| 高置信度残基 (pLDDT>90) 占比 | 14.7% |
| 置信残基 (pLDDT 70-90) 占比 | 9.6% |
| 中等置信 (pLDDT 50-70) 占比 | 42.0% |
| 低置信 (pLDDT<50) 占比 | 33.8% |
| 有序区域 (pLDDT>70) 占比 | 24.3% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=61.5），有序残基占 24.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027997; Pfam: PF15252 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GPHN | 0.807 | 0.000 | — |
| INSYN2A | 0.715 | 0.000 | — |
| IQSEC3 | 0.662 | 0.000 | — |
| NLGN2 | 0.617 | 0.000 | — |
| FAM187A | 0.600 | 0.000 | — |
| BLOC1S6 | 0.591 | 0.591 | — |
| ARHGEF9 | 0.578 | 0.000 | — |
| LHFPL4 | 0.513 | 0.000 | — |
| DTNB | 0.501 | 0.162 | — |
| SLITRK3 | 0.463 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PPP1CC | psi-mi:"MI:0018"(two hybrid) | pubmed:21382349|imex:IM-17664 |
| H1-4 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| TRAF3IP1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| DTNB | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| BLOC1S6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| WASHC3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| BORCS6 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SNAPIN | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| GABARAPL2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MCRS1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.5 + PDB: 无 | pLDDT=61.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Postsynaptic density / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. INSYN1 — Inhibitory synaptic factor 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小293 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=61.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q2T9L4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000205363-INSYN1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=INSYN1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q2T9L4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

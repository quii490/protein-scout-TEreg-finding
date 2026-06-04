---
type: protein-evaluation
gene: "PRR23A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PRR23A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PRR23A |
| 蛋白名称 | Proline-rich protein 23A |
| 蛋白大小 | 266 aa / 28.2 kDa |
| UniProt ID | A6NEV1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Microtubules; 额外: Nuclear bodies, Cytokinetic b; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 266 aa / 28.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=1 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR018903; Pfam: PF10630 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 12 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **117/180** | |
| **归一化总分** | | | **65.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Microtubules; 额外: Nuclear bodies, Cytokinetic bridge, Mitotic spindle, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1 |
| PubMed broad count | 2 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Rare coding variation and stroke heterogeneity in Saudi Arabia: an exome‑wide association study across severity, etiology, vascular territory, and early‑onset disease.. *BMC neurology*. PMID: 42087103

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.4 |
| 高置信度残基 (pLDDT>90) 占比 | 1.1% |
| 置信残基 (pLDDT 70-90) 占比 | 23.3% |
| 中等置信 (pLDDT 50-70) 占比 | 36.1% |
| 低置信 (pLDDT<50) 占比 | 39.5% |
| 有序区域 (pLDDT>70) 占比 | 24.4% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=58.4），有序残基占 24.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018903; Pfam: PF10630 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FAM90A10P | 0.583 | 0.000 | — |
| IQCJ | 0.583 | 0.000 | — |
| DEFB106A | 0.559 | 0.000 | — |
| SPAG11B | 0.556 | 0.000 | — |
| DEFB107A | 0.554 | 0.000 | — |
| DEFB105A | 0.504 | 0.000 | — |
| DEFB106B | 0.478 | 0.000 | — |
| USP17L4 | 0.476 | 0.000 | — |
| PRSS22 | 0.475 | 0.000 | — |
| USP17L7 | 0.446 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 12，IntAct interactions: 0
- 调控相关比例: 0 / 12 = 0%

**评价**: STRING 12 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.4 + PDB: 无 | pLDDT=58.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm, Microtubules; 额外: Nuclear bodies, Cyt | 待确认 |
| PPI | STRING + IntAct | 12 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PRR23A — Proline-rich protein 23A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小266 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=58.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A6NEV1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000206260-PRR23A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PRR23A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A6NEV1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

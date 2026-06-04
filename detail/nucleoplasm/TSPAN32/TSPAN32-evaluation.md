---
type: protein-evaluation
gene: "TSPAN32"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TSPAN32 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TSPAN32 / PHEMX, TSSC6 |
| 蛋白名称 | Tetraspanin-32 |
| 蛋白大小 | 320 aa / 34.6 kDa |
| UniProt ID | Q96QS1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 320 aa / 34.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=72.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR042782, IPR018499, IPR008952; Pfam: PF00335 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.0/180** | |
| **归一化总分** | | | **67.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cell surface (GO:0009986)
- integrin alphaIIb-beta3 complex (GO:0070442)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 47 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PHEMX, TSSC6 |

**关键文献**:
1. The role of tetraspanins pan-cancer.. *iScience*. PMID: 35992081
2. TCF3 and ID3 Regulate TSPAN32 Expression in Burkitt Lymphoma.. *Scandinavian journal of immunology*. PMID: 40572059
3. TSPAN32 suppresses chronic myeloid leukemia pathogenesis and progression by stabilizing PTEN.. *Signal transduction and targeted therapy*. PMID: 36854750
4. Comprehensive Analysis of TSPAN32 Regulatory Networks and Their Role in Immune Cell Biology.. *Biomolecules*. PMID: 39858501
5. Comprehensive Analysis of a Nine-Gene Signature Related to Tumor Microenvironment in Lung Adenocarcinoma.. *Frontiers in cell and developmental biology*. PMID: 34540825

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.3 |
| 高置信度残基 (pLDDT>90) 占比 | 37.2% |
| 置信残基 (pLDDT 70-90) 占比 | 27.2% |
| 中等置信 (pLDDT 50-70) 占比 | 8.8% |
| 低置信 (pLDDT<50) 占比 | 26.9% |
| 有序区域 (pLDDT>70) 占比 | 64.4% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=72.3，有序区 64.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR042782, IPR018499, IPR008952; Pfam: PF00335 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| C11orf21 | 0.936 | 0.000 | — |
| TSSC4 | 0.929 | 0.000 | — |
| CD151 | 0.805 | 0.000 | — |
| CD63 | 0.799 | 0.000 | — |
| CD9 | 0.790 | 0.000 | — |
| CD81 | 0.768 | 0.000 | — |
| PHLDA2 | 0.739 | 0.000 | — |
| TSPAN9 | 0.715 | 0.000 | — |
| CD37 | 0.694 | 0.000 | — |
| B4E171_HUMAN | 0.676 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=72.3 + PDB: 无 | pLDDT=72.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TSPAN32 — Tetraspanin-32，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小320 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96QS1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000064201-TSPAN32/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TSPAN32
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96QS1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

---
type: protein-evaluation
gene: "DPH7"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DPH7 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DPH7 / C9orf112, WDR85 |
| 蛋白名称 | Diphthine methyltransferase |
| 蛋白大小 | 452 aa / 50.6 kDa |
| UniProt ID | Q9BTV6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nuclear bodies; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 452 aa / 50.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=80.9; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR052415, IPR015943, IPR019775, IPR036322, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.0/180** | |
| **归一化总分** | | | **68.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 24 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C9orf112, WDR85 |

**关键文献**:
1. The diphthamide modification pathway from Saccharomyces cerevisiae--revisited.. *Molecular microbiology*. PMID: 25352115
2. Decoding the biosynthesis and function of diphthamide, an enigmatic modification of translation elongation factor 2 (EF2).. *Microbial cell (Graz, Austria)*. PMID: 28357244
3. Translational fidelity and growth of Arabidopsis require stress-sensitive diphthamide biosynthesis.. *Nature communications*. PMID: 35817801
4. Molecular characterization of diphthamide biosynthesis protein 7 in Marsupenaeus japonicus and its role in white spot syndrome virus infection.. *Fish & shellfish immunology*. PMID: 29407614
5. Yeast gene KTI13 (alias DPH8) operates in the initiation step of diphthamide synthesis on elongation factor 2.. *Microbial cell (Graz, Austria)*. PMID: 37662670

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.9 |
| 高置信度残基 (pLDDT>90) 占比 | 67.0% |
| 置信残基 (pLDDT 70-90) 占比 | 9.5% |
| 中等置信 (pLDDT 50-70) 占比 | 4.6% |
| 低置信 (pLDDT<50) 占比 | 18.8% |
| 有序区域 (pLDDT>70) 占比 | 76.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=80.9，有序区 76.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052415, IPR015943, IPR019775, IPR036322, IPR001680; Pfam: PF00400 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EEF2 | 0.984 | 0.114 | — |
| DPH1 | 0.927 | 0.000 | — |
| DPH2 | 0.902 | 0.000 | — |
| DPH5 | 0.876 | 0.000 | — |
| DPH6 | 0.852 | 0.000 | — |
| DPH3 | 0.845 | 0.000 | — |
| DNAJC24 | 0.809 | 0.000 | — |
| WDR6 | 0.534 | 0.095 | — |
| SERGEF | 0.527 | 0.000 | — |
| TEX29 | 0.519 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.9 + PDB: 无 | pLDDT=80.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DPH7 — Diphthine methyltransferase，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小452 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BTV6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000148399-DPH7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DPH7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BTV6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

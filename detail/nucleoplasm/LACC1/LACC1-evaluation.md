---
type: protein-evaluation
gene: "LACC1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LACC1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LACC1 / C13orf31, FAMIN |
| 蛋白名称 | Purine nucleoside phosphorylase LACC1 |
| 蛋白大小 | 430 aa / 47.8 kDa |
| UniProt ID | Q8IV20 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm; Nucleus; Endoplasmic reticulum; Peroxisome |
| 蛋白大小 | 10/10 | ×1 | 10 | 430 aa / 47.8 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=43 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=88.7; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR003730, IPR038371, IPR011324; Pfam: PF02578 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.5/180** | |
| **归一化总分** | | | **65.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm; Nucleus; Endoplasmic reticulum; Peroxisome | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- endoplasmic reticulum (GO:0005783)
- nucleus (GO:0005634)
- peroxisome (GO:0005777)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 43 |
| PubMed broad count | 87 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C13orf31, FAMIN |

**关键文献**:
1. LACC1 bridges NOS2 and polyamine metabolism in inflammatory macrophages.. *Nature*. PMID: 35978195
2. LACC1: A critical involvement in macrophage immunometabolism.. *Cell biology international*. PMID: 37366569
3. FAMIN Is a Multifunctional Purine Enzyme Enabling the Purine Nucleotide Cycle.. *Cell*. PMID: 31978345
4. Clinical characteristics and genotype analysis of a Chinese patient with juvenile arthritis due to novel LACC1 frameshift mutation and literature review.. *Molecular genetics & genomic medicine*. PMID: 37186377
5. LACC1 contributes to inflammation and cognitive disorder after stroke via the AMPK/NLRP3 pathway.. *Acta neurobiologiae experimentalis*. PMID: 35833820

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.7 |
| 高置信度残基 (pLDDT>90) 占比 | 75.8% |
| 置信残基 (pLDDT 70-90) 占比 | 11.2% |
| 中等置信 (pLDDT 50-70) 占比 | 4.9% |
| 低置信 (pLDDT<50) 占比 | 8.1% |
| 有序区域 (pLDDT>70) 占比 | 87.0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=88.7，有序区 87.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003730, IPR038371, IPR011324; Pfam: PF02578 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CCDC122 | 0.949 | 0.000 | — |
| PLPBP | 0.829 | 0.000 | — |
| TNFSF15 | 0.728 | 0.000 | — |
| RIPK2 | 0.721 | 0.000 | — |
| NOD2 | 0.699 | 0.000 | — |
| SPRYD7 | 0.639 | 0.000 | — |
| LRRK2 | 0.619 | 0.000 | — |
| SIN3A | 0.614 | 0.614 | — |
| FASN | 0.610 | 0.292 | — |
| PXDNL | 0.605 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ORC4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| OSER1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DLC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FASN | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:27478939|imex:IM-26127 |
| ENSP00000391747.1 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:27478939|imex:IM-26127 |
| FCHSD2 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:27478939|imex:IM-26127 |
| SIN3A | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:27478939|imex:IM-26127 |
| RBBP7 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:27478939|imex:IM-26127 |
| DDB1 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:27478939|imex:IM-26127 |
| CLUH | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:27478939|imex:IM-26127 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.7 + PDB: 无 | pLDDT=88.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Endoplasmic reticulum; Peroxis / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. LACC1 — Purine nucleoside phosphorylase LACC1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小430 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 43 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IV20
- Protein Atlas: https://www.proteinatlas.org/ENSG00000179630-LACC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LACC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IV20
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

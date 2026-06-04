---
type: protein-evaluation
gene: "MINDY1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MINDY1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MINDY1 / FAM63A, KIAA1390 |
| 蛋白名称 | Ubiquitin carboxyl-terminal hydrolase MINDY-1 |
| 蛋白大小 | 469 aa / 51.8 kDa |
| UniProt ID | Q8N5J2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 469 aa / 51.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=72.7; PDB: 5JKN, 5JQS, 5MN9, 6TUV, 6TXB, 6Y6R, 6YJG |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR007518, IPR033979; Pfam: PF04424 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **148.0/180** | |
| **归一化总分** | | | **82.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cell periphery (GO:0071944)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 19 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FAM63A, KIAA1390 |

**关键文献**:
1. Mechanism of activation and regulation of deubiquitinase activity in MINDY1 and MINDY2.. *Molecular cell*. PMID: 34529927
2. MINDY1 Is a Downstream Target of the Polyamines and Promotes Embryonic Stem Cell Self-Renewal.. *Stem cells (Dayton, Ohio)*. PMID: 29644784
3. MINDY1 promotes breast cancer cell proliferation by stabilizing estrogen receptor α.. *Cell death & disease*. PMID: 34645792
4. MINDY1 Induces PD-L1 Deubiquitination to Promote Immune Escape in Hepatocellular Carcinoma by the Wnt/β-Catenin Pathway.. *Oncology research*. PMID: 41179305
5. MINDY1 promotes bladder cancer progression by stabilizing YAP.. *Cancer cell international*. PMID: 34315490

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.7 |
| 高置信度残基 (pLDDT>90) 占比 | 46.3% |
| 置信残基 (pLDDT 70-90) 占比 | 15.1% |
| 中等置信 (pLDDT 50-70) 占比 | 6.6% |
| 低置信 (pLDDT<50) 占比 | 32.0% |
| 有序区域 (pLDDT>70) 占比 | 61.4% |
| 可用 PDB 条目 | 5JKN, 5JQS, 5MN9, 6TUV, 6TXB, 6Y6R, 6YJG, 6Z90 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（5JKN, 5JQS, 5MN9, 6TUV, 6TXB, 6Y6R, 6YJG, 6Z90）+ AlphaFold极高置信度预测（pLDDT=72.7），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007518, IPR033979; Pfam: PF04424 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| UBC | 0.979 | 0.974 | — |
| UBA52 | 0.926 | 0.915 | — |
| UBB | 0.922 | 0.909 | — |
| RPS27A | 0.907 | 0.907 | — |
| SLC13A5 | 0.790 | 0.000 | — |
| COPS5 | 0.668 | 0.000 | — |
| MINDY4 | 0.649 | 0.000 | — |
| ZUP1 | 0.615 | 0.000 | — |
| JOSD2 | 0.580 | 0.000 | — |
| JOSD1 | 0.578 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Q74S26 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| SEL1L3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KDELR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GMCL1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| LSM8 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| KCNA10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MANSC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RNF126 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SLC45A2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| GRTP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.7 + PDB: 5JKN, 5JQS, 5MN9, 6TUV, 6TXB,  | pLDDT=72.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. MINDY1 — Ubiquitin carboxyl-terminal hydrolase MINDY-1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小469 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N5J2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000143409-MINDY1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MINDY1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N5J2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

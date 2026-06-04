---
type: protein-evaluation
gene: "EN1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EN1 — REJECTED (研究热度过高 (PubMed strict=331，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EN1 |
| 蛋白名称 | Homeobox protein engrailed-1 |
| 蛋白大小 | 392 aa / 40.1 kDa |
| UniProt ID | Q05925 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoli rim; 额外: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 392 aa / 40.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=331 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050720, IPR001356, IPR000747, IPR020479, IPR019 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **87.5/180** | |
| **归一化总分** | | | **48.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli rim; 额外: Nucleoplasm | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 331 |
| PubMed broad count | 745 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Opposing Functions of BRD4 Isoforms in Breast Cancer.. *Molecular cell*. PMID: 32446320
2. Epigenetic regulation during cancer transitions across 11 tumour types.. *Nature*. PMID: 37914932
3. Cre reporter strains produced by targeted insertion of EYFP and ECFP into the ROSA26 locus.. *BMC developmental biology*. PMID: 11299042
4. Engrailed-1 Promotes Pancreatic Cancer Metastasis.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 38110836
5. Of travelling homeoproteins and medulloblastomas.. *Oncogene*. PMID: 40760093

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.5 |
| 高置信度残基 (pLDDT>90) 占比 | 12.5% |
| 置信残基 (pLDDT 70-90) 占比 | 9.9% |
| 中等置信 (pLDDT 50-70) 占比 | 27.8% |
| 低置信 (pLDDT<50) 占比 | 49.7% |
| 有序区域 (pLDDT>70) 占比 | 22.4% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=56.5），有序残基占 22.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050720, IPR001356, IPR000747, IPR020479, IPR019549; Pfam: PF10525, PF00046 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TLE1 | 0.853 | 0.841 | — |
| PAX2 | 0.841 | 0.000 | — |
| WNT1 | 0.768 | 0.000 | — |
| FGF8 | 0.765 | 0.000 | — |
| FOXA2 | 0.741 | 0.000 | — |
| PAX6 | 0.726 | 0.316 | — |
| TLE5 | 0.700 | 0.682 | — |
| NR4A2 | 0.697 | 0.000 | — |
| LBH | 0.668 | 0.000 | — |
| TLE4 | 0.659 | 0.582 | — |

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
| 三维结构 | AlphaFold pLDDT=56.5 + PDB: 无 | pLDDT=56.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoli rim; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. EN1 — Homeobox protein engrailed-1，研究基础较多，新颖性有限。
2. 蛋白大小392 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 331 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=56.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 331 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q05925
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163064-EN1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EN1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q05925
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

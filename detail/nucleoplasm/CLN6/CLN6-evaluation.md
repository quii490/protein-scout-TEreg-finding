---
type: protein-evaluation
gene: "CLN6"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CLN6 — REJECTED (研究热度过高 (PubMed strict=165，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CLN6 |
| 蛋白名称 | Ceroid-lipofuscinosis neuronal protein 6 |
| 蛋白大小 | 311 aa / 35.9 kDa |
| UniProt ID | Q9NWW5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Endoplasmic reticulum; 额外: Nucleoli, Vesicles; UniProt: Endoplasmic reticulum membrane; Endoplasmic reticulum |
| 蛋白大小 | 10/10 | ×1 | 10 | 311 aa / 35.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=165 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=85.0; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR029255; Pfam: PF15156 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.5/180** | |
| **归一化总分** | | | **49.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum; 额外: Nucleoli, Vesicles | Approved |
| UniProt | Endoplasmic reticulum membrane; Endoplasmic reticulum | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- early endosome (GO:0005769)
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum lumen (GO:0005788)
- endoplasmic reticulum membrane (GO:0005789)
- membrane (GO:0016020)
- membrane raft (GO:0045121)
- nucleolus (GO:0005730)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 165 |
| PubMed broad count | 234 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. The Neuronal Ceroid Lipofuscinoses.. **. PMID: 39637217
2. Adult-onset Kufs disease.. *Practical neurology*. PMID: 37802651
3. The Association Between Lysosomal Storage Disorder Genes and Parkinson's Disease: A Large Cohort Study in Chinese Mainland Population.. *Frontiers in aging neuroscience*. PMID: 34867278
4. Neuronal Ceroid Lipofuscinoses Overview.. **. PMID: 20301601
5. Expanded Phenotype of the Cln6(nclf) Mouse Model.. *Cells*. PMID: 40358187

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.0 |
| 高置信度残基 (pLDDT>90) 占比 | 61.4% |
| 置信残基 (pLDDT 70-90) 占比 | 24.4% |
| 中等置信 (pLDDT 50-70) 占比 | 1.3% |
| 低置信 (pLDDT<50) 占比 | 12.9% |
| 有序区域 (pLDDT>70) 占比 | 85.8% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=85.0，有序区 85.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029255; Pfam: PF15156 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CLN5 | 0.987 | 0.000 | — |
| CLN8 | 0.987 | 0.000 | — |
| CLN3 | 0.979 | 0.000 | — |
| PPT1 | 0.976 | 0.000 | — |
| MFSD8 | 0.947 | 0.000 | — |
| DNAJC5 | 0.863 | 0.000 | — |
| KCTD7 | 0.798 | 0.000 | — |
| TPP1 | 0.774 | 0.045 | — |
| CTSD | 0.771 | 0.000 | — |
| CALML4 | 0.733 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000249806.5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:30177828|imex:IM-26452 |
| env | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-17346|pubmed:22190034| |
| ILK | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-17578|pubmed:23455922 |
| P/V | psi-mi:"MI:0096"(pull down) | pubmed:21911578|imex:IM-17703 |
| SLC16A1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:30177828|imex:IM-26452 |
| ATP2A2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:30177828|imex:IM-26452 |
| GCN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:30177828|imex:IM-26452 |
| ERLIN2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:30177828|imex:IM-26452 |
| XPO1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:30177828|imex:IM-26452 |
| DDOST | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:30177828|imex:IM-26452 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.0 + PDB: 无 | pLDDT=85.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Endoplasmic reticu / Endoplasmic reticulum; 额外: Nucleoli, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CLN6 — Ceroid-lipofuscinosis neuronal protein 6，研究基础较多，新颖性有限。
2. 蛋白大小311 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 165 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 165 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NWW5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000128973-CLN6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CLN6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NWW5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

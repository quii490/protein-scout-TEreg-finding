---
type: protein-evaluation
gene: "GNE"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GNE — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GNE / GLCNE, IBM2 |
| 蛋白名称 | Bifunctional UDP-N-acetylglucosamine 2-epimerase/N-acetylmannosamine kinase |
| 蛋白大小 | 722 aa / 79.3 kDa |
| UniProt ID | Q9Y223 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Cytosol; UniProt: Cytoplasm, cytosol |
| 蛋白大小 | 10/10 | ×1 | 10 | 722 aa / 79.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=93.1; PDB: 2YHW, 2YHY, 2YI1, 3EO3, 4ZHT |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR043129, IPR000600, IPR020004, IPR003331; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.0/180** | |
| **归一化总分** | | | **70.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) | 无 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.1 |
| 高置信度残基 (pLDDT>90) 占比 | 87.4% |
| 置信残基 (pLDDT 70-90) 占比 | 8.4% |
| 中等置信 (pLDDT 50-70) 占比 | 1.2% |
| 低置信 (pLDDT<50) 占比 | 2.9% |
| 有序区域 (pLDDT>70) 占比 | 95.8% |
| 可用 PDB 条目 | 2YHW, 2YHY, 2YI1, 3EO3, 4ZHT |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2YHW, 2YHY, 2YI1, 3EO3, 4ZHT）+ AlphaFold极高置信度预测（pLDDT=93.1），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR043129, IPR000600, IPR020004, IPR003331; Pfam: PF02350, PF00480 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NANS | 0.992 | 0.000 | — |
| UAP1 | 0.967 | 0.000 | — |
| RNF38 | 0.953 | 0.000 | — |
| NPL | 0.950 | 0.000 | — |
| RENBP | 0.944 | 0.000 | — |
| UAP1L1 | 0.922 | 0.000 | — |
| CRMP1 | 0.907 | 0.095 | — |
| GPI | 0.904 | 0.000 | — |
| H6PD | 0.903 | 0.000 | — |
| AMDHD2 | 0.898 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1194896 | psi-mi:"MI:0397"(two hybrid array) | pubmed:17615063 |
| ENSP00000494141.2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| flaG | psi-mi:"MI:0397"(two hybrid array) | pubmed:17615063 |
| EBI-1194794 | psi-mi:"MI:0397"(two hybrid array) | pubmed:17615063 |
| luxS | psi-mi:"MI:0397"(two hybrid array) | pubmed:17615063 |
| EBI-1257123 | psi-mi:"MI:0096"(pull down) | pubmed:19367725|imex:IM-20587 |
| EBI-1329801 | psi-mi:"MI:0397"(two hybrid array) | pubmed:17615063 |
| EBI-1194929 | psi-mi:"MI:0397"(two hybrid array) | pubmed:17615063 |
| Q0P8G6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:17615063 |
| ndk | psi-mi:"MI:0397"(two hybrid array) | pubmed:17615063 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.1 + PDB: 2YHW, 2YHY, 2YI1, 3EO3, 4ZHT | pLDDT=93.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ (REJECTED)

**核心优势**:
1. GNE — Bifunctional UDP-N-acetylglucosamine 2-epimerase/N-acetylmannosamine kinase，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小722 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y223
- Protein Atlas: https://www.proteinatlas.org/ENSG00000159921-GNE/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GNE
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y223
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

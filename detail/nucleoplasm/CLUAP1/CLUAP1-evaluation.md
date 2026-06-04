---
type: protein-evaluation
gene: "CLUAP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CLUAP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CLUAP1 |
| 蛋白名称 | Clusterin associated protein 1 |
| 蛋白大小 | 432 aa / 50.1 kDa |
| UniProt ID | J3KNW5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Nucleoplasm, Primary cilium; 额外: Vesicles, Actin filaments; UniProt: Cell projection, cilium |
| 蛋白大小 | 10/10 | x1 | 10 | 432 aa / 50.1 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=25 篇 (≤40→8) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=73.7; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **109.5/180** | |
| **归一化总分** | | | **60.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Primary cilium; 额外: Vesicles, Actin filaments | Supported |
| UniProt | Cell projection, cilium | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 25 |
| PubMed broad count | 26 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Associations between RetNet gene polymorphisms and the efficacy of orthokeratology for myopia control: a retrospective clinical study.. *Eye Vis (Lond)*. PMID: 40091069
2. Identification of a Risk Allele at SLC41A3 and a Protective Allele HLA-DPB1*02:01 Associated with Sarcopenia in Japanese.. *Gerontology*. PMID: 40552851
3. Region-specific gene expression profile in the epididymis of high- and low-fertile dromedary camels.. *Reprod Domest Anim*. PMID: 39031030
4. Abundance of selected genes implicated in testicular functions in Camelus dromedarius with high and low epididymal semen quality.. *Biol Reprod*. PMID: 38145478
5. COVID-19 progression towards ARDS: a genome wide study reveals host factors underlying critical COVID-19.. *Genomics Inform*. PMID: 37415451

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.7 |
| 高置信度残基 (pLDDT>90) 占比 | 44.9% |
| 置信残基 (pLDDT 70-90) 占比 | 19.0% |
| 中等置信 (pLDDT 50-70) 占比 | 4.2% |
| 低置信 (pLDDT<50) 占比 | 31.9% |
| 有序区域 (pLDDT>70) 占比 | 63.9% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=73.7，有序区 63.9%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| IFT80 | 0.000 | 0.000 | — |
| IFT88 | 0.000 | 0.000 | — |
| IFT57 | 0.000 | 0.000 | — |
| TRAF3IP1 | 0.000 | 0.000 | — |
| IFT52 | 0.000 | 0.000 | — |
| IFT172 | 0.000 | 0.000 | — |
| IFT20 | 0.000 | 0.000 | — |
| IFT46 | 0.000 | 0.000 | — |
| TTC26 | 0.000 | 0.000 | — |
| IFT27 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q9VR64 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q9VQ34 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q8MYW2 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q9W092 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q9W0G6 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:P17704 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q9W3S4 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:P06754 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q9VBP2 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q9W029 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.7 + PDB: 无 | pLDDT=73.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell projection, cilium / Nucleoplasm, Primary cilium; 额外: Vesicles, Actin f | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CLUAP1 -- Clusterin associated protein 1，非常新颖，仅有少数基础研究。
2. 蛋白大小432 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 25 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/J3KNW5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000103351-CLUAP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CLUAP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/J3KNW5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

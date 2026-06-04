---
type: protein-evaluation
gene: "GNPAT"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GNPAT — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GNPAT / DAPAT, DHAPAT |
| 蛋白名称 | Dihydroxyacetone phosphate acyltransferase |
| 蛋白大小 | 680 aa / 77.2 kDa |
| UniProt ID | O15228 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Vesicles, Cell Junctions; UniProt: Peroxisome membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 680 aa / 77.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=88.5; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR028353, IPR022284, IPR045520, IPR041728, IPR002 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.5/180** | |
| **归一化总分** | | | **65.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles, Cell Junctions | Approved |
| UniProt | Peroxisome membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cell junction (GO:0030054)
- cytosol (GO:0005829)
- membrane (GO:0016020)
- peroxisomal matrix (GO:0005782)
- peroxisomal membrane (GO:0005778)
- peroxisome (GO:0005777)

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
| AlphaFold 平均 pLDDT | 88.5 |
| 高置信度残基 (pLDDT>90) 占比 | 73.8% |
| 置信残基 (pLDDT 70-90) 占比 | 17.9% |
| 中等置信 (pLDDT 50-70) 占比 | 2.6% |
| 低置信 (pLDDT<50) 占比 | 5.6% |
| 有序区域 (pLDDT>70) 占比 | 91.7% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=88.5，有序区 91.7%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR028353, IPR022284, IPR045520, IPR041728, IPR002123; Pfam: PF01553, PF19277 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AGPS | 0.997 | 0.447 | — |
| FAR1 | 0.978 | 0.000 | — |
| GPD1 | 0.967 | 0.000 | — |
| GPD1L | 0.956 | 0.000 | — |
| GPD2 | 0.932 | 0.000 | — |
| AGPAT3 | 0.910 | 0.000 | — |
| AGPAT2 | 0.905 | 0.000 | — |
| PEX5 | 0.904 | 0.510 | — |
| AGPAT1 | 0.903 | 0.000 | — |
| AGPAT5 | 0.898 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Arrb1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| RAB35 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| EBI-1257125 | psi-mi:"MI:0096"(pull down) | pubmed:19463016|imex:IM-17246 |
| GPR3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| PEX5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:22002062|imex:IM-17176 |
| PEX14 | psi-mi:"MI:0096"(pull down) | pubmed:21525035|imex:IM-16885 |
| SLX4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12200|pubmed:19596235 |
| 1C | psi-mi:"MI:0096"(pull down) | imex:IM-15828|pubmed:22593156 |
| HSPB1 | psi-mi:"MI:0097"(reverse ras recruitment system) | imex:IM-20864|pubmed:25277244 |
| CAT | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.5 + PDB: 无 | pLDDT=88.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Peroxisome membrane / Vesicles, Cell Junctions | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GNPAT — Dihydroxyacetone phosphate acyltransferase，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小680 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O15228
- Protein Atlas: https://www.proteinatlas.org/ENSG00000116906-GNPAT/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GNPAT
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O15228
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

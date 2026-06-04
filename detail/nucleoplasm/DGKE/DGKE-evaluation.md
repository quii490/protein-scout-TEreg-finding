---
type: protein-evaluation
gene: "DGKE"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DGKE 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DGKE / DAGK5 |
| 蛋白名称 | Diacylglycerol kinase epsilon |
| 蛋白大小 | 567 aa / 63.9 kDa |
| UniProt ID | P52429 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Membrane; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 567 aa / 63.9 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=60 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=86.0; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR017438, IPR046349, IPR037607, IPR000756, IPR001 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **115.0/180** | |
| **归一化总分** | | | **63.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | Membrane; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- glutamatergic synapse (GO:0098978)
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 60 |
| PubMed broad count | 114 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DAGK5 |

**关键文献**:
1. Thrombotic microangiopathy in children.. *Pediatric nephrology (Berlin, Germany)*. PMID: 35041041
2. C3 Glomerulopathy.. **. PMID: 20301598
3. Clinical features and management of atypical hemolytic uremic syndrome patient with DGKE gene variants: a case report.. *Frontiers in pediatrics*. PMID: 37456562
4. Genetic Atypical Hemolytic-Uremic Syndrome.. **. PMID: 20301541
5. DGKE and atypical HUS.. *Nature genetics*. PMID: 23619787

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.0 |
| 高置信度残基 (pLDDT>90) 占比 | 58.4% |
| 置信残基 (pLDDT 70-90) 占比 | 28.6% |
| 中等置信 (pLDDT 50-70) 占比 | 8.1% |
| 低置信 (pLDDT<50) 占比 | 4.9% |
| 有序区域 (pLDDT>70) 占比 | 87.0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=86.0，有序区 87.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR017438, IPR046349, IPR037607, IPR000756, IPR001206; Pfam: PF00130, PF00609, PF00781 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PAICS | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PDHA1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| NUDC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| SET | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| NUF2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MRPL44 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| ARRB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:17620599 |
| CD74 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| P2RY6 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| SLC15A3 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.0 + PDB: 无 | pLDDT=86.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane; Cytoplasm / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

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
1. DGKE — Diacylglycerol kinase epsilon，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小567 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 60 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P52429
- Protein Atlas: https://www.proteinatlas.org/ENSG00000153933-DGKE/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DGKE
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P52429
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

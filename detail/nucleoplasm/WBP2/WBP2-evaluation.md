---
type: protein-evaluation
gene: "WBP2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## WBP2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | WBP2 |
| 蛋白名称 | WW domain-binding protein 2 |
| 蛋白大小 | 261 aa / 28.1 kDa |
| UniProt ID | Q969T9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 261 aa / 28.1 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=59 篇 (≤60→6) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=72.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR004182, IPR044852; Pfam: PF02893 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.5/180** | |
| **归一化总分** | | | **63.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 59 |
| PubMed broad count | 73 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. WBP2 restrains the lysosomal degradation of GPX4 to inhibit ferroptosis in cisplatin-induced acute kidney injury.. *Redox biology*. PMID: 37516014
2. Targeted proteomics addresses selectivity and complexity of protein degradation by autophagy.. *Autophagy*. PMID: 39245437
3. Reciprocal Regulation of Hippo and WBP2 Signalling-Implications in Cancer Therapy.. *Cells*. PMID: 34831354
4. The emerging roles of WBP2 oncogene in human cancers.. *Oncogene*. PMID: 32393834
5. WW domain binding protein 2 (WBP2) as an oncogene in breast cancer: mechanisms and therapeutic prospects-a narrative review.. *Gland surgery*. PMID: 36654949

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.2 |
| 高置信度残基 (pLDDT>90) 占比 | 40.6% |
| 置信残基 (pLDDT 70-90) 占比 | 11.9% |
| 中等置信 (pLDDT 50-70) 占比 | 21.5% |
| 低置信 (pLDDT<50) 占比 | 26.1% |
| 有序区域 (pLDDT>70) 占比 | 52.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=72.2，有序区 52.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004182, IPR044852; Pfam: PF02893 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| YAP1 | 0.970 | 0.824 | — |
| WBP1 | 0.953 | 0.000 | — |
| CYC1 | 0.941 | 0.777 | — |
| UQCRC2 | 0.926 | 0.753 | — |
| UQCRQ | 0.923 | 0.765 | — |
| UQCRB | 0.917 | 0.641 | — |
| WWP2 | 0.917 | 0.814 | — |
| NEDD4 | 0.882 | 0.803 | — |
| NEDD4L | 0.872 | 0.656 | — |
| WWOX | 0.872 | 0.598 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BP1086 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Ubi-p5E | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| DmTOM1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| SEPTIN3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| GABARAP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| GABARAPL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| GABARAPL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| CLEC4G | psi-mi:"MI:0018"(two hybrid) | pubmed:18624398|imex:IM-19021 |
| Pax8 | psi-mi:"MI:0084"(phage display) | pubmed:14531730|mint:MINT-5216 |
| Nedd4 | psi-mi:"MI:0400"(affinity technology) | imex:IM-17722|pubmed:11042109| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.2 + PDB: 无 | pLDDT=72.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. WBP2 — WW domain-binding protein 2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小261 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 59 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q969T9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000132471-WBP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=WBP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q969T9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

---
type: protein-evaluation
gene: "STEEP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## STEEP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | STEEP1 / CXorf56 |
| 蛋白名称 | STING ER exit protein |
| 蛋白大小 | 222 aa / 25.6 kDa |
| UniProt ID | Q9H5V9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Centrosome; UniProt: Cytoplasm; Endoplasmic reticulum membrane; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 222 aa / 25.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=76.1; PDB: 8C6J, 9FMD |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029704, IPR057965; Pfam: PF25809 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **136.5/180** | |
| **归一化总分** | | | **75.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Centrosome | Supported |
| UniProt | Cytoplasm; Endoplasmic reticulum membrane; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cell body (GO:0044297)
- centrosome (GO:0005813)
- cytoplasm (GO:0005737)
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 7 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CXorf56 |

**关键文献**:
1. RETREG1/FAM134B-mediated ERGICphagy regulates GSDME-dependent dendritic cell pyroptosis during sepsis.. *Autophagy*. PMID: 41787734
2. Positively selected genes in the hoary bat (Lasiurus cinereus) lineage: prominence of thymus expression, immune and metabolic function, and regions of ancient synteny.. *PeerJ*. PMID: 35317076
3. A CRISPR-Cas9 screen Reveals STEEP1 as a Key Host Dependency Factor for Epstein-Barr Virus Latent Membrane Protein 1 Trafficking and Signaling.. *bioRxiv : the preprint server for biology*. PMID: 41890102

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.1 |
| 高置信度残基 (pLDDT>90) 占比 | 36.9% |
| 置信残基 (pLDDT 70-90) 占比 | 23.0% |
| 中等置信 (pLDDT 50-70) 占比 | 32.4% |
| 低置信 (pLDDT<50) 占比 | 7.7% |
| 有序区域 (pLDDT>70) 占比 | 59.9% |
| 可用 PDB 条目 | 8C6J, 9FMD |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（8C6J, 9FMD）+ AlphaFold高质量预测（pLDDT=76.1），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029704, IPR057965; Pfam: PF25809 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NFKBIL1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| cactin | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| KLHL36 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CHMP3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LMNA | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| LRRK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31046837|imex:IM-26684 |
| H3C1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| RPRD1B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PIBF1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| HAT1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.1 + PDB: 8C6J, 9FMD | pLDDT=76.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Endoplasmic reticulum membrane; Nucleus / Nucleoplasm; 额外: Centrosome | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. STEEP1 — STING ER exit protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小222 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H5V9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000018610-STEEP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=STEEP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H5V9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

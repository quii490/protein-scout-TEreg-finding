---
type: protein-evaluation
gene: "DMAP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DMAP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DMAP1 / KIAA1425 |
| 蛋白名称 | DNA methyltransferase 1-associated protein 1 |
| 蛋白大小 | 467 aa / 53.0 kDa |
| UniProt ID | Q9NPF5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 467 aa / 53.0 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=56 篇 (≤60→6) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=73.7; PDB: 3HM5, 4IEJ, 8QR1, 8X15, 8X19, 8X1C, 8XVG |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR032563, IPR008468, IPR027109; Pfam: PF05499, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **124.0/180** | |
| **归一化总分** | | | **68.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- NuA4 histone acetyltransferase complex (GO:0035267)
- nucleoplasm (GO:0005654)
- nucleosome (GO:0000786)
- nucleus (GO:0005634)
- replication fork (GO:0005657)
- Swr1 complex (GO:0000812)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 56 |
| PubMed broad count | 168 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1425 |

**关键文献**:
1. De novo variants predicting haploinsufficiency for DIP2C are associated with expressive speech delay.. *American journal of medical genetics. Part A*. PMID: 38421105
2. RGS6 interacts with DMAP1 and DNMT1 and inhibits DMAP1 transcriptional repressor activity.. *The Journal of biological chemistry*. PMID: 14734556
3. The DNA methyltransferase DMAP1 is required for tissue maintenance and planarian regeneration.. *Developmental biology*. PMID: 39179016
4. The DNA Methyltransferase DMAP1 is Required for Tissue Maintenance and Planarian Regeneration.. *bioRxiv : the preprint server for biology*. PMID: 38645093
5. Physical and functional interactions between Daxx and DNA methyltransferase 1-associated protein, DMAP1.. *Journal of immunology (Baltimore, Md. : 1950)*. PMID: 14978102

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.7 |
| 高置信度残基 (pLDDT>90) 占比 | 36.6% |
| 置信残基 (pLDDT 70-90) 占比 | 26.1% |
| 中等置信 (pLDDT 50-70) 占比 | 12.8% |
| 低置信 (pLDDT<50) 占比 | 24.4% |
| 有序区域 (pLDDT>70) 占比 | 62.7% |
| 可用 PDB 条目 | 3HM5, 4IEJ, 8QR1, 8X15, 8X19, 8X1C, 8XVG, 8XVT, 9C57, 9C62 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（3HM5, 4IEJ, 8QR1, 8X15, 8X19, 8X1C, 8XVG, 8XVT, 9C57, 9C62）+ AlphaFold极高置信度预测（pLDDT=73.7），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR032563, IPR008468, IPR027109; Pfam: PF05499, PF16282 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TRRAP | 0.999 | 0.984 | — |
| YEATS4 | 0.999 | 0.979 | — |
| EPC1 | 0.999 | 0.963 | — |
| KAT5 | 0.999 | 0.911 | — |
| VPS72 | 0.999 | 0.940 | — |
| RUVBL2 | 0.999 | 0.929 | — |
| BRD8 | 0.999 | 0.670 | — |
| ACTL6A | 0.999 | 0.963 | — |
| MRGBP | 0.999 | 0.974 | — |
| MEAF6 | 0.999 | 0.974 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TSG101 | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:15033475 |
| MRGBP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:12963728 |
| ACTL6A | psi-mi:"MI:0071"(molecular sieving) | pubmed:12963728 |
| Esrrb | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20362541|imex:IM-16928 |
| ZNHIT1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16230350 |
| VPS72 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15647280 |
| HTZ1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15647280 |
| RUVBL1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16230350 |
| RUVBL2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16230350 |
| PPP2R2D | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-9155|pubmed:19156129 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.7 + PDB: 3HM5, 4IEJ, 8QR1, 8X15, 8X19,  | pLDDT=73.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DMAP1 — DNA methyltransferase 1-associated protein 1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小467 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 56 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NPF5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000178028-DMAP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DMAP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NPF5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

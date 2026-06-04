---
type: protein-evaluation
gene: "DYRK1B"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DYRK1B — REJECTED (研究热度过高 (PubMed strict=128，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DYRK1B / MIRK |
| 蛋白名称 | Dual specificity tyrosine-phosphorylation-regulated kinase 1B |
| 蛋白大小 | 629 aa / 69.2 kDa |
| UniProt ID | Q9Y463 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Mitotic chromosome; UniProt: Nucleus; Nucleus, nucleolus; Chromosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 629 aa / 69.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=128 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=73.0; PDB: 8C2Z |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011009, IPR044131, IPR000719, IPR017441, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **95.0/180** | |
| **归一化总分** | | | **52.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Mitotic chromosome | Supported |
| UniProt | Nucleus; Nucleus, nucleolus; Chromosome | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromosome (GO:0005694)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 128 |
| PubMed broad count | 208 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MIRK |

**关键文献**:
1. Mirk/Dyrk1B in cancer.. *Journal of cellular biochemistry*. PMID: 17583556
2. Discovery and Functional Characterization of a Potent, Selective, and Metabolically Stable PROTAC of the Protein Kinases DYRK1A and DYRK1B.. *Journal of medicinal chemistry*. PMID: 39344427
3. Dyrk1b promotes autophagy during skeletal muscle differentiation by upregulating 4e-bp1.. *Cellular signalling*. PMID: 34752933
4. PHF8 facilitates transcription recovery following DNA double-strand break repair.. *Nucleic acids research*. PMID: 39087553
5. Differential maturation and chaperone dependence of the paralogous protein kinases DYRK1A and DYRK1B.. *Scientific reports*. PMID: 35165364

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.0 |
| 高置信度残基 (pLDDT>90) 占比 | 51.4% |
| 置信残基 (pLDDT 70-90) 占比 | 8.6% |
| 中等置信 (pLDDT 50-70) 占比 | 5.1% |
| 低置信 (pLDDT<50) 占比 | 35.0% |
| 有序区域 (pLDDT>70) 占比 | 60.0% |
| 可用 PDB 条目 | 8C2Z |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 高质量预测（pLDDT=73.0，有序区 60.0%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011009, IPR044131, IPR000719, IPR017441, IPR008271; Pfam: PF00069 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DCAF7 | 0.989 | 0.914 | — |
| PCBD2 | 0.892 | 0.292 | — |
| FAM53C | 0.839 | 0.816 | — |
| HNF1A | 0.823 | 0.510 | — |
| RNF169 | 0.816 | 0.564 | — |
| PCBD1 | 0.782 | 0.292 | — |
| C10orf71 | 0.771 | 0.759 | — |
| EP300 | 0.708 | 0.387 | — |
| RBL2 | 0.707 | 0.394 | — |
| CTBP2 | 0.662 | 0.361 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PCBD2 | psi-mi:"MI:0018"(two hybrid) | pubmed:11980910 |
| MAP2K3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:11980910 |
| HNF1A | psi-mi:"MI:0424"(protein kinase assay) | pubmed:11980910 |
| RANBP9 | psi-mi:"MI:0018"(two hybrid) | pubmed:14500717 |
| PAK1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| MCM7 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:23764002|imex:IM-20916 |
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| ICE1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |
| FAM117B | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |
| ABCD3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.0 + PDB: 8C2Z | pLDDT=73.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, nucleolus; Chromosome / Nucleoplasm; 额外: Mitotic chromosome | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. DYRK1B — Dual specificity tyrosine-phosphorylation-regulated kinase 1B，研究基础较多，新颖性有限。
2. 蛋白大小629 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 128 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 128 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y463
- Protein Atlas: https://www.proteinatlas.org/ENSG00000105204-DYRK1B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DYRK1B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y463
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/DYRK1B/IF_images/DYRK1B_IF_red_green.jpg]]


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/DYRK1B/DYRK1B-PAE.png]]

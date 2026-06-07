---
type: protein-evaluation
gene: "TTBK1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TTBK1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TTBK1 / BDTK, KIAA1855 |
| 蛋白名称 | Tau-tubulin kinase 1 |
| 蛋白大小 | 1321 aa / 142.7 kDa |
| UniProt ID | Q5TCY1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nucleoplasm; UniProt: Cytoplasm |
| 蛋白大小 | 5/10 | ×1 | 5 | 1321 aa / 142.7 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=40 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=51.1; PDB: 4BTJ, 4BTK, 4BTM, 4NFM, 4NFN, 7JXX, 7JXY |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050235, IPR011009, IPR000719, IPR017441, IPR042 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 11 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.5/180** | |
| **归一化总分** | | | **64.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm | Supported |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- microtubule associated complex (GO:0005875)
- neuronal cell body (GO:0043025)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 40 |
| PubMed broad count | 63 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BDTK, KIAA1855 |

**关键文献**:
1. Tau-tubulin kinase.. *Frontiers in molecular neuroscience*. PMID: 24808823
2. Computational Design of Novel Tau-Tubulin Kinase 1 Inhibitors for Neurodegenerative Diseases.. *Pharmaceuticals (Basel, Switzerland)*. PMID: 39065802
3. Pathological phosphorylation of tau and TDP-43 by TTBK1 and TTBK2 drives neurodegeneration.. *Molecular neurodegeneration*. PMID: 29409526
4. Antisense oligonucleotide-based targeting of Tau-tubulin kinase 1 prevents hippocampal accumulation of phosphorylated tau in PS19 tauopathy mice.. *Acta neuropathologica communications*. PMID: 37853497
5. The structural, functional, and dynamic effect of Tau tubulin kinase1 upon a mutation: A neuro-degenerative hotspot.. *Journal of cellular biochemistry*. PMID: 34297427

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 51.1 |
| 高置信度残基 (pLDDT>90) 占比 | 21.1% |
| 置信残基 (pLDDT 70-90) 占比 | 3.5% |
| 中等置信 (pLDDT 50-70) 占比 | 3.4% |
| 低置信 (pLDDT<50) 占比 | 72.0% |
| 有序区域 (pLDDT>70) 占比 | 24.6% |
| 可用 PDB 条目 | 4BTJ, 4BTK, 4BTM, 4NFM, 4NFN, 7JXX, 7JXY, 7Q8V, 7Q8W, 7QHW |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=51.1），有序残基占 24.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050235, IPR011009, IPR000719, IPR017441, IPR042714; Pfam: PF00069 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MAPT | 0.682 | 0.296 | — |
| LTV1 | 0.586 | 0.514 | — |
| MAPRE3 | 0.524 | 0.442 | — |
| GABARAPL2 | 0.514 | 0.476 | — |
| C20orf194 | 0.472 | 0.000 | — |
| RIOK2 | 0.464 | 0.384 | — |
| TARDBP | 0.460 | 0.067 | — |
| CDK5 | 0.440 | 0.000 | — |
| MAPRE1 | 0.424 | 0.422 | — |
| GSK3B | 0.417 | 0.086 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HEATR1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| DLST | psi-mi:"MI:0030"(cross-linking study) | doi:10.1016/j.cels.2017.10.010 |
| YWHAG | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| HNRNPC | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ACSL3 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| GABARAP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| GABARAPL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ANK3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| MAPRE1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ACSF3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 11，IntAct interactions: 15
- 调控相关比例: 1 / 11 = 9%

**评价**: STRING 11 个预测互作，IntAct 15 个实验互作。调控相关配体占比 9%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=51.1 + PDB: 4BTJ, 4BTK, 4BTM, 4NFM, 4NFN,  | pLDDT=51.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Cytosol; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 11 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TTBK1 — Tau-tubulin kinase 1，非常新颖，仅有少数基础研究。
2. 蛋白大小1321 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 40 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=51.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5TCY1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000146216-TTBK1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TTBK1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5TCY1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5TCY1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5TCY1 |
| SMART | SM00220; |
| UniProt Domain [FT] | DOMAIN 34..297; /note="Protein kinase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00159" |
| InterPro | IPR050235;IPR011009;IPR000719;IPR017441;IPR042714; |
| Pfam | PF00069; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000146216-TTBK1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| GABARAPL2 | Biogrid | false |
| TTBK2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

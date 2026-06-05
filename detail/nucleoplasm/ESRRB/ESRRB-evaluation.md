---
type: protein-evaluation
gene: "ESRRB"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ESRRB — REJECTED (研究热度过高 (PubMed strict=174，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ESRRB / ERRB2, ESRL2, NR3B2 |
| 蛋白名称 | Steroid hormone receptor ERR2 |
| 蛋白大小 | 433 aa / 48.1 kDa |
| UniProt ID | O95718 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Cytoplasm; Chromosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 433 aa / 48.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=174 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=78.0; PDB: 1LO1, 6LIT, 6LN4 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR024178, IPR035500, IPR000536, IPR050200, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **91.0/180** | |
| **归一化总分** | | | **50.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm; Chromosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- condensed chromosome (GO:0000793)
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
| PubMed strict count | 174 |
| PubMed broad count | 343 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ERRB2, ESRL2, NR3B2 |

**关键文献**:
1. Genetic Hearing Loss Overview.. **. PMID: 20301607
2. Chromatin accessibility during human first-trimester neurodevelopment.. *Nature*. PMID: 38693260
3. Rewiring of SINE-MIR enhancer topology and Esrrb modulation in expanded and naive pluripotency.. *Genome biology*. PMID: 40296153
4. Loss of H3K9 trimethylation alters chromosome compaction and transcription factor retention during mitosis.. *Nature structural & molecular biology*. PMID: 36941433
5. Genetic architecture of Meniere's disease.. *Hearing research*. PMID: 31874721

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.0 |
| 高置信度残基 (pLDDT>90) 占比 | 60.7% |
| 置信残基 (pLDDT 70-90) 占比 | 8.5% |
| 中等置信 (pLDDT 50-70) 占比 | 3.5% |
| 低置信 (pLDDT<50) 占比 | 27.3% |
| 有序区域 (pLDDT>70) 占比 | 69.2% |
| 可用 PDB 条目 | 1LO1, 6LIT, 6LN4 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1LO1, 6LIT, 6LN4）+ AlphaFold高质量预测（pLDDT=78.0），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR024178, IPR035500, IPR000536, IPR050200, IPR001723; Pfam: PF00104, PF00105 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NANOG | 0.932 | 0.288 | — |
| SALL4 | 0.923 | 0.095 | — |
| POU5F1 | 0.905 | 0.190 | — |
| NR0B1 | 0.861 | 0.288 | — |
| SOX2 | 0.860 | 0.115 | — |
| EGFR | 0.848 | 0.092 | — |
| KLF5 | 0.845 | 0.067 | — |
| SLC7A1 | 0.842 | 0.000 | — |
| TBX3 | 0.827 | 0.071 | — |
| ESRRA | 0.824 | 0.625 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| 7705955 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| Sall4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20362541|imex:IM-16928 |
| Med26 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20362541|imex:IM-16928 |
| Taf10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20362541|imex:IM-16928 |
| Taf9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20362541|imex:IM-16928 |
| Taf4a | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20362541|imex:IM-16928 |
| Med16 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20362541|imex:IM-16928 |
| Tbp | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20362541|imex:IM-16928 |
| Taf6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20362541|imex:IM-16928 |
| Med1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20362541|imex:IM-16928 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.0 + PDB: 1LO1, 6LIT, 6LN4 | pLDDT=78.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Chromosome / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. ESRRB — Steroid hormone receptor ERR2，研究基础较多，新颖性有限。
2. 蛋白大小433 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 174 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 174 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O95718
- Protein Atlas: https://www.proteinatlas.org/ENSG00000119715-ESRRB/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ESRRB
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95718
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000119715-ESRRB/subcellular

![](https://images.proteinatlas.org/74772/1892_C3_1_red_green.jpg)
![](https://images.proteinatlas.org/74772/1892_C3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O95718-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

---
type: protein-evaluation
gene: "CLK2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CLK2 — REJECTED (研究热度过高 (PubMed strict=107，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CLK2 |
| 蛋白名称 | Dual specificity protein kinase CLK2 |
| 蛋白大小 | 499 aa / 60.1 kDa |
| UniProt ID | P49760 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Nuclear bodies; UniProt: Nucleus; Nucleus; Nucleus speckle; Nucleus speckle |
| 蛋白大小 | 10/10 | ×1 | 10 | 499 aa / 60.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=107 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=77.5; PDB: 3NR9, 5UNP, 6FYI, 6FYK, 6FYL, 6KHE |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051175, IPR011009, IPR000719, IPR017441, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **102.0/180** | |
| **归一化总分** | | | **56.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear bodies | Supported |
| UniProt | Nucleus; Nucleus; Nucleus speckle; Nucleus speckle | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nuclear body (GO:0016604)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 107 |
| PubMed broad count | 171 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. CLK2 Regulates the KEAP1/NRF2 and p53 Pathways to Suppress Ferroptosis in Colorectal Cancer.. *Cancer research*. PMID: 40882016
2. Modulation of the Wnt pathway through inhibition of CLK2 and DYRK1A by lorecivivint as a novel, potentially disease-modifying approach for knee osteoarthritis treatment.. *Osteoarthritis and cartilage*. PMID: 31132406
3. Genetic Heterogeneity Underlying Phenotypes with Early-Onset Cerebellar Atrophy.. *International journal of molecular sciences*. PMID: 38003592
4. CLK2 Expression Is Associated with the Progression of Colorectal Cancer and Is a Prognostic Biomarker.. *BioMed research international*. PMID: 35860803
5. CLK2 promotes occurrence and development of non-small cell lung cancer.. *Journal of B.U.ON. : official journal of the Balkan Union of Oncology*. PMID: 33721432

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.5 |
| 高置信度残基 (pLDDT>90) 占比 | 65.5% |
| 置信残基 (pLDDT 70-90) 占比 | 3.2% |
| 中等置信 (pLDDT 50-70) 占比 | 1.4% |
| 低置信 (pLDDT<50) 占比 | 29.9% |
| 有序区域 (pLDDT>70) 占比 | 68.7% |
| 可用 PDB 条目 | 3NR9, 5UNP, 6FYI, 6FYK, 6FYL, 6KHE |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（3NR9, 5UNP, 6FYI, 6FYK, 6FYL, 6KHE）+ AlphaFold极高置信度预测（pLDDT=77.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051175, IPR011009, IPR000719, IPR017441, IPR008271; Pfam: PF00069 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RSRP1 | 0.849 | 0.791 | — |
| CLK3 | 0.846 | 0.836 | — |
| BCLAF1 | 0.801 | 0.781 | — |
| CLK1 | 0.792 | 0.779 | — |
| RBBP6 | 0.788 | 0.782 | — |
| SNIP1 | 0.781 | 0.781 | — |
| PAFAH1B3 | 0.770 | 0.000 | — |
| ACIN1 | 0.748 | 0.702 | — |
| SRSF12 | 0.732 | 0.630 | — |
| SRSF8 | 0.729 | 0.717 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000460443.1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CLK3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| YWHAG | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| SNRNP70 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15364|pubmed:21988832 |
| SNRPN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15364|pubmed:21988832 |
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| WDR33 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |
| CPSF2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |
| HNRNPM | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |
| LUC7L | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.5 + PDB: 3NR9, 5UNP, 6FYI, 6FYK, 6FYL,  | pLDDT=77.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus; Nucleus speckle; Nucleus speckle / Nucleoplasm; 额外: Nuclear bodies | 一致 |
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
1. CLK2 — Dual specificity protein kinase CLK2，研究基础较多，新颖性有限。
2. 蛋白大小499 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 107 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 107 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P49760
- Protein Atlas: https://www.proteinatlas.org/ENSG00000176444-CLK2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CLK2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P49760
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/CLK2/CLK2-PAE.png]]

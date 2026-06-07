---
type: protein-evaluation
gene: "MMS22L"
date: 2026-06-03
tags: [protein-scout, nucleoplasm, re-evaluation, recovery]
status: scored
category: nucleoplasm
normalized_score: 71.3
raw_score: 130.5
nuclear_score: 7
---

## MMS22L 核蛋白评估报告 (Full Re-evaluation)


### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MMS22L / C6orf167 |
| 蛋白名称 | Protein MMS22-like |
| 蛋白大小 | 1243 aa / 142.3 kDa |
| UniProt ID | Q6ZRQ5 |
| PubMed (strict) | 19 |
| PubMed (broad) | 39 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Chromosome |
| 📏 蛋白大小 | 5/10 | ×1 | 5 | 1243 aa / 142.3 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=19 篇 (≤20→10) |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=81.4，PDB: 无 |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR042320, IPR029424, IPR029425; Pfam: PF14911, PF |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners, IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.5/183** | |
| **归一化总分** | | | **71.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Chromosome | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nuclear replication fork (GO:0043596)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- site of DNA damage (GO:0090734)
- site of double-strand break (GO:0035861)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持，部分数据源提示非核定位但核信号主导。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 19 |
| PubMed broad count | 39 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C6orf167 |

**关键文献**:
1. Genes and Athletic Performance: The 2023 Update.. *Genes*. PMID: 37372415
2. FIGNL1 inhibits homologous recombination in BRCA2 deficient cells by dissociating RAD51 filaments.. *Science (New York, N.Y.)*. PMID: 41166468
3. MMS22L is a novel key actor of normal and pathological erythropoiesis.. *HemaSphere*. PMID: 41446536
4. Genes and Weightlifting Performance.. *Genes*. PMID: 35052366
5. Sex-Specific Genetic and Transcriptomic Liability to Neuroticism.. *Biological psychiatry*. PMID: 36244801

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.4 |
| 高置信度残基 (pLDDT>90) 占比 | 30.6% |
| 置信残基 (pLDDT 70-90) 占比 | 51.0% |
| 中等置信 (pLDDT 50-70) 占比 | 13.3% |
| 低置信 (pLDDT<50) 占比 | 5.1% |
| 有序区域 (pLDDT>70) 占比 | 81.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=81.4，有序区 81.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR042320, IPR029424, IPR029425; Pfam: PF14911, PF14910 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TONSL | 0.999 | 0.735 | — |
| ASF1B | 0.874 | 0.733 | — |
| ESCO2 | 0.824 | 0.292 | — |
| SSRP1 | 0.815 | 0.784 | — |
| MCM6 | 0.787 | 0.510 | — |
| BRCA1 | 0.748 | 0.439 | — |
| RAD51 | 0.713 | 0.292 | — |
| ASF1A | 0.712 | 0.447 | — |
| MCM2 | 0.705 | 0.631 | — |
| SUPT16H | 0.689 | 0.622 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FBXW7 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PINX1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ASF1B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| RRP1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-26310|pubmed:20926688 |
| PACC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PVR | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| H4C16 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| OPRM1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| H2AX | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| H2BC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**已知复合体成员** (GO Cellular Component):
- cytosol (GO:0005829)
- nuclear replication fork (GO:0043596)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- site of DNA damage (GO:0090734)
- site of double-strand break (GO:0035861)

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.4 + PDB: 无 | pLDDT=81.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Chromosome / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. MMS22L — Protein MMS22-like，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1243 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 19 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6ZRQ5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000146263-MMS22L
- Protein Atlas Subcellular: https://www.proteinatlas.org/ENSG00000146263-MMS22L/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MMS22L
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ZRQ5
- STRING: https://string-db.org/network
- IntAct: https://www.ebi.ac.uk/intact/search?query=MMS22L
- Packet data timestamp: 2026-06-03 21:47:09

---

*本报告基于最新的 harvest packet 数据（2026-06-03 21:47:09），各数据库实时抓取。评分严格遵循 /180 加权评分体系：核定位×4 + 大小×1 + 新颖性×5 + 结构×3 + 结构域×2 + PPI×3 + 互证加分（max+3）。PubMed>100 或 核定位≤3 为 REJECTED。*

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000146263-MMS22L/subcellular

![](https://images.proteinatlas.org/67042/1237_F6_1_red_green.jpg)
![](https://images.proteinatlas.org/67042/1237_F6_2_red_green.jpg)
![](https://images.proteinatlas.org/67042/1284_C10_4_red_green.jpg)
![](https://images.proteinatlas.org/67042/1284_C10_5_red_green.jpg)
![](https://images.proteinatlas.org/67042/1754_F6_13_cr57f3ed192abcf_red_green.jpg)
![](https://images.proteinatlas.org/67042/1754_F6_18_cr57f3ed2cb7320_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6ZRQ5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6ZRQ5 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR042320;IPR029424;IPR029425; |
| Pfam | PF14911;PF14910; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000146263-MMS22L/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ASF1B | Intact, Biogrid | true |
| H3C6 | Biogrid, Bioplex | true |
| MCM2 | Biogrid, Bioplex | true |
| SSRP1 | Biogrid, Opencell | true |
| SUPT16H | Biogrid, Opencell | true |
| TONSL | Intact, Biogrid | true |
| ASF1A | Biogrid | false |
| ESCO2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

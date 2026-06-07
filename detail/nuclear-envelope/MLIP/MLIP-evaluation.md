---
type: protein-evaluation
gene: "MLIP"
date: 2026-06-03
tags: [protein-scout, nuclear-envelope, re-evaluation, recovery]
status: scored
category: nuclear-envelope
normalized_score: 64.5
raw_score: 118.0
nuclear_score: 7
---

## MLIP 核蛋白评估报告 (Full Re-evaluation)


### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MLIP / C6orf142, Cip |
| 蛋白名称 | Muscular LMNA-interacting protein |
| 蛋白大小 | 993 aa / 105.9 kDa |
| UniProt ID | Q5VWP3 |
| PubMed (strict) | 27 |
| PubMed (broad) | 175 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Plasma membrane; Vesicles; UniProt: Nucleus; Nucleus envelope; Nucleus, PML body; Cytoplasm, cyt |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 993 aa / 105.9 kDa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=27 篇 (21-40→8) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=43.3，PDB: 无 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029331; Pfam: PF15274 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 4 partners, IntAct 1 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/183** | |
| **归一化总分** | | | **64.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Plasma membrane; Vesicles | Approved |
| UniProt | Nucleus; Nucleus envelope; Nucleus, PML body; Cytoplasm, cytosol; Cell membrane,... | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nuclear envelope (GO:0005635)
- nuclear lumen (GO:0031981)
- nucleus (GO:0005634)
- PML body (GO:0016605)
- sarcolemma (GO:0042383)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持，部分数据源提示非核定位但核信号主导。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 27 |
| PubMed broad count | 175 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C6orf142, Cip |

**关键文献**:
1. MLIP and Its Potential Influence on Key Oncogenic Pathways.. *Cells*. PMID: 38994962
2. MLIP-Associated Myopathy: A Case Report and Review of the Literature.. *Journal of neuromuscular diseases*. PMID: 36641683
3. Muscle Enriched Lamin Interacting Protein (Mlip) Binds Chromatin and Is Required for Myoblast Differentiation.. *Cells*. PMID: 33802236
4. Neuromuscular disease: 2022 update.. *Free neuropathology*. PMID: 37284156
5. Biallelic truncating variants in the muscular A-type lamin-interacting protein (MLIP) gene cause myopathy with hyperCKemia.. *European journal of neurology*. PMID: 34935254

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 43.3 |
| 高置信度残基 (pLDDT>90) 占比 | 1.6% |
| 置信残基 (pLDDT 70-90) 占比 | 3.8% |
| 中等置信 (pLDDT 50-70) 占比 | 14.8% |
| 低置信 (pLDDT<50) 占比 | 79.8% |
| 有序区域 (pLDDT>70) 占比 | 5.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=43.3），有序残基占 5.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029331; Pfam: PF15274 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LMNA | 0.612 | 0.230 | — |
| ZACN | 0.474 | 0.000 | — |
| ZNF239 | 0.447 | 0.000 | — |
| C16orf71 | 0.445 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MAPK9 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |

**已知复合体成员** (GO Cellular Component):
- cytosol (GO:0005829)
- nuclear envelope (GO:0005635)
- nuclear lumen (GO:0031981)
- nucleus (GO:0005634)
- PML body (GO:0016605)
- sarcolemma (GO:0042383)

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 4，IntAct interactions: 1
- 调控相关比例: 0 / 4 = 0%

**评价**: STRING 4 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=43.3 + PDB: 无 | pLDDT=43.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Nucleus envelope; Nucleus, PML body; Cyto / Nucleoplasm, Plasma membrane; Vesicles | 一致 |
| PPI | STRING + IntAct | 4 + 1 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. MLIP — Muscular LMNA-interacting protein，非常新颖，仅有少数基础研究。
2. 蛋白大小993 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 27 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=43.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5VWP3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000146147-MLIP
- Protein Atlas Subcellular: https://www.proteinatlas.org/ENSG00000146147-MLIP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MLIP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5VWP3
- STRING: https://string-db.org/network
- IntAct: https://www.ebi.ac.uk/intact/search?query=MLIP
- Packet data timestamp: 2026-06-03 21:45:03

---

*本报告基于最新的 harvest packet 数据（2026-06-03 21:45:03），各数据库实时抓取。评分严格遵循 /180 加权评分体系：核定位×4 + 大小×1 + 新颖性×5 + 结构×3 + 结构域×2 + PPI×3 + 互证加分（max+3）。PubMed>100 或 核定位≤3 为 REJECTED。*

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000146147-MLIP/subcellular

![](https://images.proteinatlas.org/46654/1361_A2_1_red_green.jpg)
![](https://images.proteinatlas.org/46654/1361_A2_2_red_green.jpg)
![](https://images.proteinatlas.org/46654/1366_A2_1_red_green.jpg)
![](https://images.proteinatlas.org/46654/1366_A2_2_red_green.jpg)
![](https://images.proteinatlas.org/46654/1413_D2_1_red_green.jpg)
![](https://images.proteinatlas.org/46654/1413_D2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5VWP3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5VWP3 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029331; |
| Pfam | PF15274; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000146147-MLIP/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| LMNA | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

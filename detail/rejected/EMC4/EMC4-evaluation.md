---
type: protein-evaluation
gene: "EMC4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EMC4 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EMC4 / TMEM85 |
| 蛋白名称 | ER membrane protein complex subunit 4 |
| 蛋白大小 | 183 aa / 20.1 kDa |
| UniProt ID | Q5J8M3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Endoplasmic reticulum membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 183 aa / 20.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.9; PDB: 6Z3W, 7ADO, 7ADP, 8EOI, 8J0N, 8J0O, 8S9S |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR009445; Pfam: PF06417 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **109.5/180** | |
| **归一化总分** | | | **60.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Endoplasmic reticulum membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- EMC complex (GO:0072546)
- endoplasmic reticulum membrane (GO:0005789)
- membrane (GO:0016020)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 17 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TMEM85 |

**关键文献**:
1. Structure of the ER membrane complex, a transmembrane-domain insertase.. *Nature*. PMID: 32494008
2. Analysis of Potential Hub Genes for Neuropathic Pain Based on Differential Expression in Rat Models.. *Pain research & management*. PMID: 35281346
3. Selective EMC subunits act as molecular tethers of intracellular organelles exploited during viral entry.. *Nature communications*. PMID: 32111841
4. Reproductive toxicity of β-diketone antibiotic mixtures to zebrafish (Danio rerio).. *Ecotoxicology and environmental safety*. PMID: 28342328
5. Saccharomyces cerevisiae ER membrane protein complex subunit 4 (EMC4) plays a crucial role in eIF2B-mediated translation regulation and survival under stress conditions.. *Journal, genetic engineering & biotechnology*. PMID: 32476094

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.9 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 42.6% |
| 中等置信 (pLDDT 50-70) 占比 | 47.5% |
| 低置信 (pLDDT<50) 占比 | 9.8% |
| 有序区域 (pLDDT>70) 占比 | 42.6% |
| 可用 PDB 条目 | 6Z3W, 7ADO, 7ADP, 8EOI, 8J0N, 8J0O, 8S9S, 9C7V |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=66.9），有序残基占 42.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009445; Pfam: PF06417 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MMGT1 | 0.999 | 0.965 | — |
| EMC7 | 0.999 | 0.971 | — |
| EMC3 | 0.999 | 0.997 | — |
| EMC6 | 0.999 | 0.980 | — |
| EMC1 | 0.999 | 0.997 | — |
| EMC10 | 0.999 | 0.964 | — |
| EMC9 | 0.999 | 0.962 | — |
| EMC2 | 0.999 | 0.997 | — |
| EMC8 | 0.999 | 0.982 | — |
| VPS28 | 0.960 | 0.954 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GABA-B-R1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:37061542|imex:IM-28761 |
| ENSP00000267750.4 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| SSB1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| SSE1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |
| EMC3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MUCL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CANX | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| LAMP1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| TRDN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SLC18A1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.9 + PDB: 6Z3W, 7ADO, 7ADP, 8EOI, 8J0N,  | pLDDT=66.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. EMC4 — ER membrane protein complex subunit 4，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小183 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=66.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5J8M3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000128463-EMC4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EMC4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5J8M3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

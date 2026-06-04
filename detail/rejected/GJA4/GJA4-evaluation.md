---
type: protein-evaluation
gene: "GJA4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GJA4 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GJA4 |
| 蛋白名称 | Gap junction alpha-4 protein |
| 蛋白大小 | 333 aa / 37.4 kDa |
| UniProt ID | P35212 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cell membrane; Cell junction, gap junction |
| 蛋白大小 | 10/10 | ×1 | 10 | 333 aa / 37.4 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=74 篇 (≤80→4) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=74.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000500, IPR002263, IPR019570, IPR017990, IPR013 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cell membrane; Cell junction, gap junction | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- connexin complex (GO:0005922)
- gap junction (GO:0005921)
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 74 |
| PubMed broad count | 105 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Mannose-Binding Lectin (MBL) and Gap Junction Protein Alpha 4 (GJA4) Gene Heterogeneity in Relation to Severity of Clinical Disease in Cystic Fibrosis.. *Frontiers in bioscience (Landmark edition)*. PMID: 35748244
2. GNA14 and GNAQ somatic mutations cause spinal and intracranial extra-axial cavernous hemangiomas.. *American journal of human genetics*. PMID: 38917801
3. Integrated single-cell sequencing for the development of a GJA4-based precision immuno-prognostic model in melanoma.. *Translational oncology*. PMID: 40639089
4. Homozygous Nonsense Variant in the GJA4 Gene Associated With Increased Fetal Nuchal Fold Thickness and Abnormal Fetal Ductus Venosus Termination: A Case Report.. *Cureus*. PMID: 41416265
5. VEGF-dependent testicular vascularisation involves MEK1/2 signalling and the essential angiogenesis factors, SOX7 and SOX17.. *BMC biology*. PMID: 39354506

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.3 |
| 高置信度残基 (pLDDT>90) 占比 | 31.8% |
| 置信残基 (pLDDT 70-90) 占比 | 31.2% |
| 中等置信 (pLDDT 50-70) 占比 | 15.6% |
| 低置信 (pLDDT<50) 占比 | 21.3% |
| 有序区域 (pLDDT>70) 占比 | 63.0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=74.3，有序区 63.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000500, IPR002263, IPR019570, IPR017990, IPR013092; Pfam: PF00029 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| OPRM1 | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:23840749|imex:IM-21238 |
| OPRK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:23840749|imex:IM-21238 |
| Oprd1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:23840749|imex:IM-21238 |
| CD81 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| EBI-2857623 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TMEM86B | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ENSP00000343676.4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MS4A13 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 8
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 8 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.3 + PDB: 无 | pLDDT=74.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane; Cell junction, gap junction / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 0 + 8 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. GJA4 — Gap junction alpha-4 protein，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小333 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 74 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P35212
- Protein Atlas: https://www.proteinatlas.org/ENSG00000187513-GJA4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GJA4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P35212
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

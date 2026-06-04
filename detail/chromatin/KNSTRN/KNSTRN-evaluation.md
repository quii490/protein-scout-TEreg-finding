---
type: protein-evaluation
gene: "KNSTRN"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KNSTRN 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KNSTRN / C15orf23, SKAP, TRAF4AF1 |
| 蛋白名称 | Small kinetochore-associated protein |
| 蛋白大小 | 316 aa / 35.4 kDa |
| UniProt ID | Q9Y448 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Mitotic spindle, Centriolar satellite; 额外: Plasma membrane; UniProt: Nucleus; Chromosome, centromere, kinetochore; Cytoplasm, cyt |
| 蛋白大小 | 10/10 | ×1 | 10 | 316 aa / 35.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=18 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR033373 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitotic spindle, Centriolar satellite; 额外: Plasma membrane | Enhanced |
| UniProt | Nucleus; Chromosome, centromere, kinetochore; Cytoplasm, cytoskeleton, spindle pole; Cytoplasm, cyto... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centriolar satellite (GO:0034451)
- kinetochore (GO:0000776)
- microtubule organizing center (GO:0005815)
- microtubule plus-end (GO:0035371)
- mitotic spindle (GO:0072686)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)
- ruffle (GO:0001726)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 42 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C15orf23, SKAP, TRAF4AF1 |

**关键文献**:
1. Elevated KNSTRN as a potential indicator for triple-negative breast cancer progression and immune infiltration.. *Frontiers in immunology*. PMID: 41209020
2. KNSTRN, a Poor Prognostic Biomarker, Affects the Tumor Immune Microenvironment and Immunotherapy Outcomes in Pan-Cancer.. *Disease markers*. PMID: 36845017
3. Somatic mutations in kinetochore gene KNSTRN are associated with basal proliferating actinic keratoses and cutaneous squamous cell carcinoma.. *Journal of the European Academy of Dermatology and Venereology : JEADV*. PMID: 30972880
4. KNSTRN Is a Prognostic Biomarker That Is Correlated with Immune Infiltration in Breast Cancer and Promotes Cell Cycle and Proliferation.. *Biochemical genetics*. PMID: 38198023
5. Copy number variations in atypical fibroxanthomas and pleomorphic dermal sarcomas.. *Oncotarget*. PMID: 29312620

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.5 |
| 高置信度残基 (pLDDT>90) 占比 | 36.1% |
| 置信残基 (pLDDT 70-90) 占比 | 5.1% |
| 中等置信 (pLDDT 50-70) 占比 | 23.1% |
| 低置信 (pLDDT<50) 占比 | 35.8% |
| 有序区域 (pLDDT>70) 占比 | 41.2% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=67.5），有序残基占 41.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR033373 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SPAG5 | 0.983 | 0.435 | — |
| CENPE | 0.890 | 0.000 | — |
| NUF2 | 0.847 | 0.000 | — |
| CHMP1B | 0.798 | 0.230 | — |
| BUB1B | 0.758 | 0.000 | — |
| CDCA3 | 0.755 | 0.000 | — |
| PRPF19 | 0.749 | 0.717 | — |
| SKA1 | 0.748 | 0.000 | — |
| KIF20A | 0.727 | 0.000 | — |
| STAMBP | 0.723 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Q8K2D9 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Cep152 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Cep55 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| MYCBP | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| SPAG5 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Mad2l1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Dynll1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Plk1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| HSPB1 | psi-mi:"MI:0097"(reverse ras recruitment system) | imex:IM-20864|pubmed:25277244 |
| UNC93B1 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.5 + PDB: 无 | pLDDT=67.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Chromosome, centromere, kinetochore; Cyto / Mitotic spindle, Centriolar satellite; 额外: Plasma  | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. KNSTRN — Small kinetochore-associated protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小316 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=67.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y448
- Protein Atlas: https://www.proteinatlas.org/ENSG00000128944-KNSTRN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KNSTRN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y448
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

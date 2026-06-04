---
type: protein-evaluation
gene: "RAB6C"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RAB6C 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RAB6C / WTH3 |
| 蛋白名称 | Ras-related protein Rab-6C |
| 蛋白大小 | 254 aa / 28.4 kDa |
| UniProt ID | Q9H0N0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Golgi apparatus; 额外: Basal body; UniProt: Nucleus; Cytoplasm; Cytoplasm, cytoskeleton, microtubule org |
| 蛋白大小 | 10/10 | ×1 | 10 | 254 aa / 28.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=72.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR027417, IPR050227, IPR005225, IPR001806; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Basal body | Approved |
| UniProt | Nucleus; Cytoplasm; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centrosome (GO:0005813)
- ciliary basal body (GO:0036064)
- cytosol (GO:0005829)
- endomembrane system (GO:0012505)
- Golgi apparatus (GO:0005794)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 25 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: WTH3 |

**关键文献**:
1. Genetic and functional analysis of Raynaud's syndrome implicates loci in vasculature and immunity.. *Cell genomics*. PMID: 39142284
2. Aberrant gene-specific DNA methylation signature analysis in cervical cancer.. *Tumour biology : the journal of the International Society for Oncodevelopmental Biology and Medicine*. PMID: 28351298
3. Machine learning and bioinformatics framework integration reveal potential characteristic genes related to immune cell infiltration in preeclampsia.. *Frontiers in physiology*. PMID: 37389124
4. Gene promoter-associated CpG island hypermethylation in squamous cell carcinoma of the tongue.. *Virchows Archiv : an international journal of pathology*. PMID: 28255813
5. RAB6C is a retrogene that encodes a centrosomal protein involved in cell cycle progression.. *Journal of molecular biology*. PMID: 20064528

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.3 |
| 高置信度残基 (pLDDT>90) 占比 | 42.5% |
| 置信残基 (pLDDT 70-90) 占比 | 19.7% |
| 中等置信 (pLDDT 50-70) 占比 | 5.1% |
| 低置信 (pLDDT<50) 占比 | 32.7% |
| 有序区域 (pLDDT>70) 占比 | 62.2% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=72.3，有序区 62.2%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027417, IPR050227, IPR005225, IPR001806; Pfam: PF00071 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| VPS53 | 0.830 | 0.263 | — |
| VPS39 | 0.761 | 0.746 | — |
| GDI1 | 0.665 | 0.545 | — |
| RIC1 | 0.595 | 0.456 | — |
| VPS33A | 0.577 | 0.514 | — |
| VPS33B | 0.577 | 0.514 | — |
| ARL1 | 0.553 | 0.406 | — |
| DAXX | 0.542 | 0.074 | — |
| GCC2 | 0.523 | 0.420 | — |
| GDI2 | 0.519 | 0.430 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| araB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| GDI1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| OCRL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RAB6B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RAB6A | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| RAB10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26824392|imex:IM-25486 |
| RAB12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26824392|imex:IM-25486 |
| RAB8A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26824392|imex:IM-25486 |
| APBA1 | psi-mi:"MI:0018"(two hybrid) | pubmed:23737971|imex:IM-21673 |
| APP | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.3 + PDB: 无 | pLDDT=72.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cytoplasm, cytoskeleton, micro / Golgi apparatus; 额外: Basal body | 一致 |
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
1. RAB6C — Ras-related protein Rab-6C，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小254 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H0N0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000222014-RAB6C/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RAB6C
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H0N0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

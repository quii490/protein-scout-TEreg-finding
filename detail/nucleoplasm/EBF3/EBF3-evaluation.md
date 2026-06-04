---
type: protein-evaluation
gene: "EBF3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EBF3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EBF3 / COE3 |
| 蛋白名称 | Transcription factor COE3 |
| 蛋白大小 | 596 aa / 64.9 kDa |
| UniProt ID | Q9H4W6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 596 aa / 64.9 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=86 篇 (≤100→2) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=70.6; PDB: 3MUJ, 3N50 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR032200, IPR038173, IPR032201, IPR038006, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.0/180** | |
| **归一化总分** | | | **60.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 86 |
| PubMed broad count | 150 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: COE3 |

**关键文献**:
1. Long non-coding RNAs: From disease code to drug role.. *Acta pharmaceutica Sinica. B*. PMID: 33643816
2. Neurologic, Neuropsychologic, and Neuroradiologic Features of EBF3-Related Syndrome.. *Neurology. Genetics*. PMID: 37090941
3. EBF3 Gene-Related Fetal Phenotypes.. *Maternal-fetal medicine (Wolters Kluwer Health, Inc.)*. PMID: 40620266
4. A cell type-aware framework for nominating non-coding variants in Mendelian regulatory disorders.. *Nature communications*. PMID: 39333082
5. Duplication/triplication mosaicism of EBF3 and expansion of the EBF3 neurodevelopmental disorder phenotype.. *European journal of paediatric neurology : EJPN : official journal of the European Paediatric Neurology Society*. PMID: 34999443

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.6 |
| 高置信度残基 (pLDDT>90) 占比 | 43.6% |
| 置信残基 (pLDDT 70-90) 占比 | 14.4% |
| 中等置信 (pLDDT 50-70) 占比 | 4.5% |
| 低置信 (pLDDT<50) 占比 | 37.4% |
| 有序区域 (pLDDT>70) 占比 | 58.0% |
| 可用 PDB 条目 | 3MUJ, 3N50 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（3MUJ, 3N50）+ AlphaFold高质量预测（pLDDT=70.6），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR032200, IPR038173, IPR032201, IPR038006, IPR013783; Pfam: PF16422, PF16423, PF01833 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ZNF423 | 0.708 | 0.309 | — |
| EBF2 | 0.691 | 0.460 | — |
| TMTC1 | 0.681 | 0.000 | — |
| UBE2M | 0.618 | 0.000 | — |
| DCUN1D1 | 0.571 | 0.000 | — |
| PRDM16 | 0.556 | 0.091 | — |
| CPNE4 | 0.550 | 0.545 | — |
| UFD1 | 0.544 | 0.514 | — |
| CPNE7 | 0.538 | 0.533 | — |
| PAX5 | 0.529 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MEN1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| Itk | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| EBF2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MARF1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| SOWAHA | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| HELZ | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| PAN2 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| ATPAF2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CPNE4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CPNE2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.6 + PDB: 3MUJ, 3N50 | pLDDT=70.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. EBF3 — Transcription factor COE3，研究基础较多，新颖性有限。
2. 蛋白大小596 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 86 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H4W6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000108001-EBF3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EBF3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H4W6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

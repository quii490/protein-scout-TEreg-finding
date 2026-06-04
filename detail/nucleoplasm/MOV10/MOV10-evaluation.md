---
type: protein-evaluation
gene: "MOV10"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MOV10 — REJECTED (研究热度过高 (PubMed strict=111，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MOV10 / KIAA1631 |
| 蛋白名称 | Helicase MOV-10 |
| 蛋白大小 | 1003 aa / 113.7 kDa |
| UniProt ID | Q9HCE1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Cytoplasm, P-body; Cytoplasm, Cytoplasmic ribonucleoprotein  |
| 蛋白大小 | 8/10 | ×1 | 8 | 1003 aa / 113.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=111 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=81.1; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR041679, IPR041677, IPR049080, IPR026122, IPR049 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **83.5/180** | |
| **归一化总分** | | | **46.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | Cytoplasm, P-body; Cytoplasm, Cytoplasmic ribonucleoprotein granule; Cytoplasm, Stress granule; Nucl... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasmic ribonucleoprotein granule (GO:0036464)
- cytoplasmic stress granule (GO:0010494)
- cytosol (GO:0005829)
- extracellular space (GO:0005615)
- nucleus (GO:0005634)
- P granule (GO:0043186)
- P-body (GO:0000932)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 111 |
| PubMed broad count | 151 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1631 |

**关键文献**:
1. A diverse range of gene products are effectors of the type I interferon antiviral response.. *Nature*. PMID: 21478870
2. Unwinding the roles of RNA helicase MOV10.. *Wiley interdisciplinary reviews. RNA*. PMID: 34327836
3. MOV10 Helicase Interacts with Coronavirus Nucleocapsid Protein and Has Antiviral Activity.. *mBio*. PMID: 34517762
4. FMRP and MOV10 regulate Dicer1 expression and dendrite development.. *PloS one*. PMID: 34847178
5. Evolutionary and Expression Analysis of MOV10 and MOV10L1 Reveals Their Origin, Duplication and Divergence.. *International journal of molecular sciences*. PMID: 35886872

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.1 |
| 高置信度残基 (pLDDT>90) 占比 | 38.4% |
| 置信残基 (pLDDT 70-90) 占比 | 44.2% |
| 中等置信 (pLDDT 50-70) 占比 | 7.9% |
| 低置信 (pLDDT<50) 占比 | 9.6% |
| 有序区域 (pLDDT>70) 占比 | 82.6% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=81.1，有序区 82.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR041679, IPR041677, IPR049080, IPR026122, IPR049079; Pfam: PF13086, PF13087, PF21634 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AGO2 | 0.997 | 0.608 | — |
| DICER1 | 0.991 | 0.000 | — |
| TNRC6B | 0.988 | 0.163 | — |
| AGO1 | 0.988 | 0.423 | — |
| UPF1 | 0.912 | 0.756 | — |
| FMR1 | 0.892 | 0.166 | — |
| PUM2 | 0.891 | 0.180 | — |
| CBX6 | 0.880 | 0.541 | — |
| TNRC6A | 0.867 | 0.163 | — |
| APOBEC3G | 0.811 | 0.292 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PUF60 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ATG12 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| GABARAPL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| GABARAP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| MAP1LC3A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| GABARAPL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| ORF7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16317|pubmed:22522808 |
| NS1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:22810585|imex:IM-17331 |
| US11 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:22810585|imex:IM-17331 |
| IFIT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15277|pubmed:21642987 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.1 + PDB: 无 | pLDDT=81.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, P-body; Cytoplasm, Cytoplasmic ribonucl / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. MOV10 — Helicase MOV-10，研究基础较多，新颖性有限。
2. 蛋白大小1003 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 111 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 111 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9HCE1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000155363-MOV10/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MOV10
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HCE1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

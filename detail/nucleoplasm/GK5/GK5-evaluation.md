---
type: protein-evaluation
gene: "GK5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GK5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GK5 |
| 蛋白名称 | Glycerol kinase 5 |
| 蛋白大小 | 529 aa / 59.2 kDa |
| UniProt ID | Q6ZS86 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 529 aa / 59.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=93.9; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR043129, IPR000577, IPR018483, IPR018485, IPR018 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- mitochondrion (GO:0005739)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 25 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Glycerol kinase 5 confers gefitinib resistance through SREBP1/SCD1 signaling pathway.. *Journal of experimental & clinical cancer research : CR*. PMID: 30791926
2. Exposure to particulate matter 2.5 and cigarette smoke induces the synthesis of lipid droplets by glycerol kinase 5.. *Clinical and experimental pharmacology & physiology*. PMID: 33462866
3. The Binding Sites of miR-619-5p in the mRNAs of Human and Orthologous Genes.. *BMC genomics*. PMID: 28569192
4. MicroRNA-645 promotes cell metastasis and proliferation of renal clear cell carcinoma by targeting GK5.. *European review for medical and pharmacological sciences*. PMID: 29131260
5. Enhanced insulin secretion and cholesterol metabolism in congenic strains of the spontaneously diabetic (Type 2) Goto Kakizaki rat are controlled by independent genetic loci in rat chromosome 8.. *Diabetologia*. PMID: 15164172

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.9 |
| 高置信度残基 (pLDDT>90) 占比 | 88.3% |
| 置信残基 (pLDDT 70-90) 占比 | 8.1% |
| 中等置信 (pLDDT 50-70) 占比 | 0.6% |
| 低置信 (pLDDT<50) 占比 | 3.0% |
| 有序区域 (pLDDT>70) 占比 | 96.4% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=93.9，有序区 96.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR043129, IPR000577, IPR018483, IPR018485, IPR018484; Pfam: PF02782, PF00370 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GPD2 | 0.807 | 0.097 | — |
| DBT | 0.694 | 0.071 | — |
| PSMD4 | 0.603 | 0.460 | — |
| PSMD6 | 0.598 | 0.451 | — |
| CEACAM4 | 0.596 | 0.095 | — |
| RSPH3 | 0.582 | 0.049 | — |
| PSMD12 | 0.565 | 0.444 | — |
| UNC80 | 0.563 | 0.093 | — |
| PSMD2 | 0.562 | 0.458 | — |
| PSMD11 | 0.560 | 0.453 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HSPA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ROS1 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:35384245|imex:IM-29494 |
| MST1R | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:35384245|imex:IM-29494 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 3
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.9 + PDB: 无 | pLDDT=93.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 3 interactions | 数据充分 |

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
1. GK5 — Glycerol kinase 5，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小529 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6ZS86
- Protein Atlas: https://www.proteinatlas.org/ENSG00000175066-GK5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GK5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ZS86
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

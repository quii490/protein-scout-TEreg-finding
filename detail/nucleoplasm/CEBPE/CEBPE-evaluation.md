---
type: protein-evaluation
gene: "CEBPE"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CEBPE 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CEBPE |
| 蛋白名称 | CCAAT/enhancer-binding protein epsilon |
| 蛋白大小 | 281 aa / 30.6 kDa |
| UniProt ID | Q15744 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Plasma membrane, Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 281 aa / 30.6 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=91 篇 (≤100→2) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.2; PDB: 3T92 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR004827, IPR046347, IPR031106, IPR016468; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **90.5/180** | |
| **归一化总分** | | | **50.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Plasma membrane, Cytosol | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)
- RNA polymerase II transcription regulator complex (GO:0090575)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 91 |
| PubMed broad count | 216 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Emerging molecular subtypes and therapies in acute lymphoblastic leukemia.. *Seminars in diagnostic pathology*. PMID: 37120350
2. Single-cell RNA-sequencing of human eosinophils in allergic inflammation in the esophagus.. *The Journal of allergy and clinical immunology*. PMID: 38871184
3. A new severe congenital neutropenia syndrome associated with autosomal recessive COPZ1 mutations.. *Blood*. PMID: 39642330
4. Integrative single-cell RNA-seq and ATAC-seq identifies transcriptional and epigenetic blueprint guiding osteoclastogenic trajectory.. *Journal of bone and mineral research : the official journal of the American Society for Bone and Mineral Research*. PMID: 40577680
5. Deliver CEBPE via cartilage targeting Lipid nanoparticle to block CEBPE-LTF-STAT3 positive feedback loop for efficient treatment of cartilage endplate degeneration.. *Materials today. Bio*. PMID: 40677394

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.2 |
| 高置信度残基 (pLDDT>90) 占比 | 22.8% |
| 置信残基 (pLDDT 70-90) 占比 | 5.0% |
| 中等置信 (pLDDT 50-70) 占比 | 39.1% |
| 低置信 (pLDDT<50) 占比 | 33.1% |
| 有序区域 (pLDDT>70) 占比 | 27.8% |
| 可用 PDB 条目 | 3T92 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=63.2），有序残基占 27.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004827, IPR046347, IPR031106, IPR016468; Pfam: PF07716 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ARID5B | 0.917 | 0.000 | — |
| CEBPA | 0.893 | 0.496 | — |
| SPI1 | 0.892 | 0.054 | — |
| LTF | 0.876 | 0.045 | — |
| RARA | 0.863 | 0.045 | — |
| GATA1 | 0.832 | 0.328 | — |
| CENPV | 0.785 | 0.000 | — |
| RXRA | 0.779 | 0.045 | — |
| MPO | 0.735 | 0.000 | — |
| GZMH | 0.725 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CCT7 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| PSAT1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| EDA2R | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| EBI-3907063 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| GPR22 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| CSNK1A1L | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| NELFB | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| TAF5L | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| POU2F1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.2 + PDB: 3T92 | pLDDT=63.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Plasma membrane, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CEBPE — CCAAT/enhancer-binding protein epsilon，研究基础较多，新颖性有限。
2. 蛋白大小281 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 91 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=63.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q15744
- Protein Atlas: https://www.proteinatlas.org/ENSG00000092067-CEBPE/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CEBPE
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15744
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

---
type: protein-evaluation
gene: "SGK2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SGK2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SGK2 |
| 蛋白名称 | Serine/threonine-protein kinase Sgk2 |
| 蛋白大小 | 367 aa / 41.2 kDa |
| UniProt ID | Q9HBY8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 367 aa / 41.2 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=70 篇 (≤80→4) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=87.0; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000961, IPR011009, IPR017892, IPR000719, IPR017 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.5/180** | |
| **归一化总分** | | | **60.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 70 |
| PubMed broad count | 97 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Targeting Kindlin-2 in adipocytes increases bone mass through inhibiting FAS/PPARγ/FABP4 signaling in mice.. *Acta pharmaceutica Sinica. B*. PMID: 37969743
2. Kinase requirements in human cells: V. Synthetic lethal interactions between p53 and the protein kinases SGK2 and PAK3.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 20616055
3. Lethality of PAK3 and SGK2 shRNAs to human papillomavirus positive cervical cancer cells is independent of PAK3 and SGK2 knockdown.. *PloS one*. PMID: 25615606
4. SGK2 promotes renal cancer progression via enhancing ERK 1/2 and AKT phosphorylation.. *European review for medical and pharmacological sciences*. PMID: 31002126
5. Regulation and physiological roles of serum- and glucocorticoid-induced protein kinase isoforms.. *Science's STKE : signal transduction knowledge environment*. PMID: 11707620

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.0 |
| 高置信度残基 (pLDDT>90) 占比 | 69.2% |
| 置信残基 (pLDDT 70-90) 占比 | 16.6% |
| 中等置信 (pLDDT 50-70) 占比 | 4.4% |
| 低置信 (pLDDT<50) 占比 | 9.8% |
| 有序区域 (pLDDT>70) 占比 | 85.8% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=87.0，有序区 85.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000961, IPR011009, IPR017892, IPR000719, IPR017441; Pfam: PF00069, PF00433 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PDPK1 | 0.954 | 0.454 | — |
| SGK3 | 0.934 | 0.329 | — |
| FOXO1 | 0.932 | 0.125 | — |
| FOXO3 | 0.930 | 0.125 | — |
| FOXO4 | 0.923 | 0.125 | — |
| SGK1 | 0.904 | 0.000 | — |
| NEDD4L | 0.677 | 0.092 | — |
| HSP90AB1 | 0.672 | 0.621 | — |
| HSP90AA1 | 0.642 | 0.579 | — |
| MTOR | 0.639 | 0.521 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| IL3RA | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| MBD2 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | imex:IM-26348|pubmed:27593931 |
| PMM2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| HIRIP3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ILF3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:25852190|imex:IM-23674 |
| DDX5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:25852190|imex:IM-23674 |
| CCT8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:25852190|imex:IM-23674 |
| CCT4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:25852190|imex:IM-23674 |
| CCT6A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:25852190|imex:IM-23674 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.0 + PDB: 无 | pLDDT=87.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. SGK2 — Serine/threonine-protein kinase Sgk2，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小367 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 70 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9HBY8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000101049-SGK2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SGK2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HBY8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

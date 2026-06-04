---
type: protein-evaluation
gene: "VDR"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## VDR — REJECTED (研究热度过高 (PubMed strict=6110，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | VDR / NR1I1 |
| 蛋白名称 | Vitamin D3 receptor |
| 蛋白大小 | 427 aa / 48.3 kDa |
| UniProt ID | P11473 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Intermediate filaments, Cytosol; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 427 aa / 48.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=6110 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=83.6; PDB: 1DB1, 1IE8, 1IE9, 1KB2, 1KB4, 1KB6, 1S0Z |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR042153, IPR035500, IPR000536, IPR050234, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Intermediate filaments, Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- receptor complex (GO:0043235)
- RNA polymerase II transcription regulator complex (GO:0090575)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 6110 |
| PubMed broad count | 10094 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NR1I1 |

**关键文献**:
1. Discovery of vitexin as a novel VDR agonist that mitigates the transition from chronic intestinal inflammation to colorectal cancer.. *Molecular cancer*. PMID: 39272040
2. Vitamin D Receptor (VDR) Gene Polymorphisms and High-Turnover Renal Osteodystrophy or Secondary Hyperparathyroidism in End-Stage Renal Disease: A Systematic Review.. *Cureus*. PMID: 39156357
3. VDR Gene variation and insulin resistance related diseases.. *Lipids in health and disease*. PMID: 28822353
4. Role of Calcitriol and Vitamin D Receptor (VDR) Gene Polymorphisms in Alzheimer's Disease.. *International journal of molecular sciences*. PMID: 38732025
5. The VDR gene FokI polymorphism and ovarian cancer risk.. *Tumour biology : the journal of the International Society for Oncodevelopmental Biology and Medicine*. PMID: 24078452

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.6 |
| 高置信度残基 (pLDDT>90) 占比 | 72.1% |
| 置信残基 (pLDDT 70-90) 占比 | 7.5% |
| 中等置信 (pLDDT 50-70) 占比 | 3.5% |
| 低置信 (pLDDT<50) 占比 | 16.9% |
| 有序区域 (pLDDT>70) 占比 | 79.6% |
| 可用 PDB 条目 | 1DB1, 1IE8, 1IE9, 1KB2, 1KB4, 1KB6, 1S0Z, 1S19, 1TXI, 1YNW |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1DB1, 1IE8, 1IE9, 1KB2, 1KB4, 1KB6, 1S0Z, 1S19, 1TXI, 1YNW）+ AlphaFold极高置信度预测（pLDDT=83.6），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR042153, IPR035500, IPR000536, IPR050234, IPR001723; Pfam: PF00104, PF00105 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RXRA | 0.981 | 0.968 | — |
| CYP2R1 | 0.964 | 0.265 | — |
| CYP24A1 | 0.947 | 0.306 | — |
| PTH | 0.941 | 0.000 | — |
| NCOA1 | 0.920 | 0.865 | — |
| MED1 | 0.913 | 0.886 | — |
| FGF23 | 0.907 | 0.000 | — |
| GC | 0.858 | 0.000 | — |
| SLC34A1 | 0.848 | 0.000 | — |
| NCOA3 | 0.843 | 0.810 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NCOA6 | psi-mi:"MI:0018"(two hybrid) | pubmed:10866662 |
| Trim24 | psi-mi:"MI:0018"(two hybrid) | pubmed:8978696 |
| PRKCSH | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| RXRA | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| RXRB | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| CXXC5 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| EP300 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| MMRN2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| NKD2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| CCND3 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.6 + PDB: 1DB1, 1IE8, 1IE9, 1KB2, 1KB4,  | pLDDT=83.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm; 额外: Intermediate filaments, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. VDR — Vitamin D3 receptor，研究基础较多，新颖性有限。
2. 蛋白大小427 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 6110 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 6110 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P11473
- Protein Atlas: https://www.proteinatlas.org/ENSG00000111424-VDR/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=VDR
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P11473
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

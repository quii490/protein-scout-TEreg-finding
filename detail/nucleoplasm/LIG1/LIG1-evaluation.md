---
type: protein-evaluation
gene: "LIG1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## LIG1 — REJECTED (研究热度过高 (PubMed strict=175，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LIG1 |
| 蛋白名称 | DNA ligase 1 |
| 蛋白大小 | 919 aa / 101.7 kDa |
| UniProt ID | P18858 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Golgi apparatus, Vesicles; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 919 aa / 101.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=175 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=76.8; PDB: 1X9N, 5YY9, 6P09, 6P0A, 6P0B, 6P0C, 6P0D |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050191, IPR000977, IPR012309, IPR012310, IPR016 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **100.0/180** | |
| **归一化总分** | | | **55.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Golgi apparatus, Vesicles | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 175 |
| PubMed broad count | 454 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Proteogenomic Markers of Chemotherapy Resistance and Response in Triple-Negative Breast Cancer.. *Cancer discovery*. PMID: 36001024
2. CRISPR/Cas9 screens identify LIG1 as a sensitizer of PARP inhibitors in castration-resistant prostate cancer.. *The Journal of clinical investigation*. PMID: 39718835
3. Mammalian DNA ligases.. *BioEssays : news and reviews in molecular, cellular and developmental biology*. PMID: 9363683
4. LIG1 is a novel marker for bladder cancer prognosis: evidence based on experimental studies, machine learning and single-cell sequencing.. *Frontiers in immunology*. PMID: 39234248
5. Therapeutic validation of MMR-associated genetic modifiers in a human ex vivo model of Huntington disease.. *American journal of human genetics*. PMID: 38749429

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.8 |
| 高置信度残基 (pLDDT>90) 占比 | 62.1% |
| 置信残基 (pLDDT 70-90) 占比 | 7.9% |
| 中等置信 (pLDDT 50-70) 占比 | 0.7% |
| 低置信 (pLDDT<50) 占比 | 29.3% |
| 有序区域 (pLDDT>70) 占比 | 70.0% |
| 可用 PDB 条目 | 1X9N, 5YY9, 6P09, 6P0A, 6P0B, 6P0C, 6P0D, 6P0E, 6Q1V, 7KR3 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1X9N, 5YY9, 6P09, 6P0A, 6P0B, 6P0C, 6P0D, 6P0E, 6Q1V, 7KR3）+ AlphaFold极高置信度预测（pLDDT=76.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050191, IPR000977, IPR012309, IPR012310, IPR016059; Pfam: PF04679, PF01068, PF04675 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FEN1 | 0.999 | 0.942 | — |
| PCNA | 0.999 | 0.997 | — |
| XRCC1 | 0.997 | 0.094 | — |
| APEX1 | 0.996 | 0.143 | — |
| POLB | 0.996 | 0.096 | — |
| UHRF1 | 0.987 | 0.971 | — |
| POLD1 | 0.973 | 0.098 | — |
| RFC4 | 0.959 | 0.112 | — |
| UNG | 0.952 | 0.000 | — |
| MCM5 | 0.947 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TUBB4A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| INPP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ptrB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| HSPB1 | psi-mi:"MI:0097"(reverse ras recruitment system) | imex:IM-20864|pubmed:25277244 |
| H1-2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| LRIG1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-27729|pubmed:29317492 |
| ERBB2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-27705|pubmed:23723069 |
| RET | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:29436694|imex:IM-27680 |
| RNF166 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NBL1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.8 + PDB: 1X9N, 5YY9, 6P09, 6P0A, 6P0B,  | pLDDT=76.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Golgi apparatus, Vesicles | 一致 |
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
1. LIG1 — DNA ligase 1，研究基础较多，新颖性有限。
2. 蛋白大小919 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 175 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 175 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P18858
- Protein Atlas: https://www.proteinatlas.org/ENSG00000105486-LIG1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LIG1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P18858
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

---
type: protein-evaluation
gene: "SP4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SP4 — REJECTED (研究热度过高 (PubMed strict=395，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SP4 |
| 蛋白名称 | Transcription factor Sp4 |
| 蛋白大小 | 784 aa / 82.0 kDa |
| UniProt ID | Q02446 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 784 aa / 82.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=395 篇 (>100→REJECTED) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v6 pLDDT=38.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039938, IPR036236, IPR013087; Pfam: PF00096 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **70.5/180** | |
| **归一化总分** | | | **39.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 395 |
| PubMed broad count | 2101 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Mapping genomic loci implicates genes and synaptic biology in schizophrenia.. *Nature*. PMID: 35396580
2. Sp4 Regulates PTTG1IP Gene Transcription and Expression.. *DNA and cell biology*. PMID: 36383136
3. Specificity Proteins (Sp) and Cancer.. *International journal of molecular sciences*. PMID: 36982239
4. Anti-Sp4 and anti-CCAR1 autoantibodies in UK vs US patients with adult and juvenile-onset anti-TIF1γ-positive myositis.. *Rheumatology (Oxford, England)*. PMID: 39514366
5. Over-representation of potential SP4 target genes within schizophrenia-risk genes.. *Molecular psychiatry*. PMID: 34750502

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 38.8 |
| 高置信度残基 (pLDDT>90) 占比 | 0.1% |
| 置信残基 (pLDDT 70-90) 占比 | 10.7% |
| 中等置信 (pLDDT 50-70) 占比 | 2.7% |
| 低置信 (pLDDT<50) 占比 | 86.5% |
| 有序区域 (pLDDT>70) 占比 | 10.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=38.8），有序残基占 10.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039938, IPR036236, IPR013087; Pfam: PF00096 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000222584.3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| dl | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Spn42Da | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| ENSG00000283930 | psi-mi:"MI:0432"(one hybrid) | imex:IM-26689|pubmed:31481462 |
| VEZF1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MCRS1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| EBI-12760345 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ELK3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CIB3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PNKP | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=38.8 + PDB: 无 | pLDDT=38.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. SP4 — Transcription factor Sp4，研究基础较多，新颖性有限。
2. 蛋白大小784 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 395 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=38.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 395 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q02446
- Protein Atlas: https://www.proteinatlas.org/ENSG00000105866-SP4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SP4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q02446
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000105866-SP4/subcellular

![](https://images.proteinatlas.org/10246/921_E10_2_red_green.jpg)
![](https://images.proteinatlas.org/10246/921_E10_3_red_green.jpg)
![](https://images.proteinatlas.org/10246/923_E10_2_red_green.jpg)
![](https://images.proteinatlas.org/10246/923_E10_3_red_green.jpg)
![](https://images.proteinatlas.org/10246/931_E10_1_red_green.jpg)
![](https://images.proteinatlas.org/10246/931_E10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q02446-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

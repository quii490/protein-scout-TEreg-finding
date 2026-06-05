---
type: protein-evaluation
gene: "TNP1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TNP1 — REJECTED (研究热度过高 (PubMed strict=123，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TNP1 |
| 蛋白名称 | Spermatid nuclear transition protein 1 |
| 蛋白大小 | 55 aa / 6.4 kDa |
| UniProt ID | P09430 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus; Chromosome |
| 蛋白大小 | 5/10 | ×1 | 5 | 55 aa / 6.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=123 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001319, IPR020062; Pfam: PF02079 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 2 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.0/180** | |
| **归一化总分** | | | **43.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus; Chromosome | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- male germ cell nucleus (GO:0001673)
- nucleosome (GO:0000786)
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 123 |
| PubMed broad count | 172 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Phase-separated CCER1 coordinates the histone-to-protamine transition and male fertility.. *Nature communications*. PMID: 38081819
2. Evaluation of TNP1 and PRM1 gene expression in male infertility patients with low or high sperm DNA fragmentation.. *Journal of the Turkish German Gynecological Association*. PMID: 40077949
3. Genomic and Computational Analysis of Novel SNPs in TNP1 Gene Promoter Region of Bos indicus Breeding Bulls.. *Genetics research*. PMID: 35356752
4. Gene polymorphisms and male infertility--a meta-analysis and literature review.. *Reproductive biomedicine online*. PMID: 18062861
5. Histone demethylase JHDM2A is critical for Tnp1 and Prm1 transcription and spermatogenesis.. *Nature*. PMID: 17943087

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.1 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 9.1% |
| 中等置信 (pLDDT 50-70) 占比 | 89.1% |
| 低置信 (pLDDT<50) 占比 | 1.8% |
| 有序区域 (pLDDT>70) 占比 | 9.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=62.1），有序残基占 9.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001319, IPR020062; Pfam: PF02079 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TNP2 | 0.980 | 0.000 | — |
| PRM2 | 0.966 | 0.000 | — |
| PRM1 | 0.961 | 0.000 | — |
| KDM3A | 0.855 | 0.000 | — |
| NUPR1 | 0.838 | 0.000 | — |
| TSSK6 | 0.818 | 0.000 | — |
| VIL1 | 0.772 | 0.000 | — |
| SPEM1 | 0.748 | 0.000 | — |
| ACR | 0.727 | 0.000 | — |
| PRM3 | 0.705 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SDCBP2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| DVL3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 2
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.1 + PDB: 无 | pLDDT=62.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Chromosome / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 2 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. TNP1 — Spermatid nuclear transition protein 1，研究基础较多，新颖性有限。
2. 蛋白大小55 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 123 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=62.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 123 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P09430
- Protein Atlas: https://www.proteinatlas.org/ENSG00000118245-TNP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TNP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P09430
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P09430-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

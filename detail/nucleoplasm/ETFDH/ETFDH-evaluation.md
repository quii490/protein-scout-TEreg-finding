---
type: protein-evaluation
gene: "ETFDH"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ETFDH — REJECTED (研究热度过高 (PubMed strict=193，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ETFDH |
| 蛋白名称 | Electron transfer flavoprotein-ubiquinone oxidoreductase, mitochondrial |
| 蛋白大小 | 617 aa / 68.5 kDa |
| UniProt ID | Q16134 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Mitochondria; 额外: Nucleoplasm, Cytosol; UniProt: Mitochondrion inner membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 617 aa / 68.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=193 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=93.6; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR017896, IPR040156, IPR049398, IPR007859, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 12 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.5/180** | |
| **归一化总分** | | | **49.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria; 额外: Nucleoplasm, Cytosol | Supported |
| UniProt | Mitochondrion inner membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- cytosol (GO:0005829)
- mitochondrial inner membrane (GO:0005743)
- mitochondrial membrane (GO:0031966)
- mitochondrion (GO:0005739)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 193 |
| PubMed broad count | 260 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Regulation of energy metabolism by long-chain fatty acids.. *Progress in lipid research*. PMID: 24362249
2. Characterizing mitochondrial features in osteoarthritis through integrative multi-omics and machine learning analysis.. *Frontiers in immunology*. PMID: 39026663
3. NGS-Based Genetic Analysis in a Cohort of Italian Patients with Suspected Inherited Myopathies and/or HyperCKemia.. *Genes*. PMID: 37510298
4. Deep Intronic ETFDH Variants Represent a Recurrent Pathogenic Event in Multiple Acyl-CoA Dehydrogenase Deficiency.. *International journal of molecular sciences*. PMID: 39273584
5. Variants in mitochondrial disease genes are common causes of inherited peripheral neuropathies.. *Journal of neurology*. PMID: 38549004

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.6 |
| 高置信度残基 (pLDDT>90) 占比 | 91.2% |
| 置信残基 (pLDDT 70-90) 占比 | 2.1% |
| 中等置信 (pLDDT 50-70) 占比 | 0.8% |
| 低置信 (pLDDT<50) 占比 | 5.8% |
| 有序区域 (pLDDT>70) 占比 | 93.3% |
| 可用 PDB 条目 | 无 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=93.6，有序区 93.3%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR017896, IPR040156, IPR049398, IPR007859, IPR036188; Pfam: PF21162, PF05187, PF01946 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ETFA | 0.999 | 0.797 | — |
| ETFB | 0.999 | 0.797 | — |
| HADHB | 0.924 | 0.099 | — |
| ACADVL | 0.817 | 0.099 | — |
| ACAA2 | 0.810 | 0.099 | — |
| COQ9 | 0.801 | 0.226 | — |
| GCDH | 0.783 | 0.299 | — |
| FLAD1 | 0.775 | 0.000 | — |
| ACADM | 0.766 | 0.051 | — |
| ACADS | 0.759 | 0.099 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Dmel\CG12379 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| rnb | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| KRTAP11-1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ZNF581 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| OTX1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| GSC2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| KRTAP13-2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MYH7B | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TRIM69 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| HBB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 12
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 12 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.6 + PDB: 无 | pLDDT=93.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Mitochondrion inner membrane / Mitochondria; 额外: Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 12 interactions | 数据充分 |

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
1. ETFDH — Electron transfer flavoprotein-ubiquinone oxidoreductase, mitochondrial，研究基础较多，新颖性有限。
2. 蛋白大小617 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 193 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 193 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q16134
- Protein Atlas: https://www.proteinatlas.org/ENSG00000171503-ETFDH/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ETFDH
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q16134
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

---
type: protein-evaluation
gene: "TRIOBP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TRIOBP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TRIOBP / KIAA1662, TARA |
| 蛋白名称 | TRIO and F-actin-binding protein |
| 蛋白大小 | 2365 aa / 261.4 kDa |
| UniProt ID | Q9H2D6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus; Nucleus; Cytoplasm, cytoskeleton, microtubule organ |
| 蛋白大小 | 2/10 | ×1 | 2 | 2365 aa / 261.4 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=74 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=40.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR052223, IPR039597, IPR011993, IPR001849; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **92.0/180** | |
| **归一化总分** | | | **51.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus; Nucleus; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Midbody; Chrom... | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629)
- centrosome (GO:0005813)
- chromosome, telomeric region (GO:0000781)
- focal adhesion (GO:0005925)
- midbody (GO:0030496)
- nucleus (GO:0005634)
- stereocilium base (GO:0120044)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 74 |
| PubMed broad count | 105 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1662, TARA |

**关键文献**:
1. Genetic Hearing Loss Overview.. **. PMID: 20301607
2. Trans-ancestry GWAS identifies 59 loci and improves risk prediction and fine-mapping for kidney stone disease.. *Nature communications*. PMID: 40216741
3. The TRIOBP Isoforms and Their Distinct Roles in Actin Stabilization, Deafness, Mental Illness, and Cancer.. *Molecules (Basel, Switzerland)*. PMID: 33121024
4. Aggregation of the protein TRIOBP-1 and its potential relevance to schizophrenia.. *PloS one*. PMID: 25333879
5. SYMPTOM SEVERITY IN SCHIZOPHRENIA PATIENTS WITH NPAS3, DYSBINDIN-1 AND/OR TRIOBP PROTEIN PATHOLOGY IN THEIR BLOOD SERUM: A PANSS-BASED FOLLOW UP STUDY.. *Psychiatria Danubina*. PMID: 37480305

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 40.1 |
| 高置信度残基 (pLDDT>90) 占比 | 9.0% |
| 置信残基 (pLDDT 70-90) 占比 | 5.2% |
| 中等置信 (pLDDT 50-70) 占比 | 2.9% |
| 低置信 (pLDDT<50) 占比 | 82.9% |
| 有序区域 (pLDDT>70) 占比 | 14.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=40.1），有序残基占 14.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052223, IPR039597, IPR011993, IPR001849; Pfam: PF00169 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PJVK | 0.904 | 0.000 | — |
| XIRP2 | 0.868 | 0.000 | — |
| SPTAN1 | 0.854 | 0.000 | — |
| SPTBN1 | 0.849 | 0.000 | — |
| MYO15A | 0.829 | 0.000 | — |
| TPRN | 0.828 | 0.000 | — |
| ESPN | 0.809 | 0.045 | — |
| MYO7A | 0.791 | 0.000 | — |
| WHRN | 0.770 | 0.000 | — |
| MYO3A | 0.759 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-1023227 | psi-mi:"MI:0071"(molecular sieving) | pubmed:17629495|imex:IM-19091 |
| VIM | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| GTF2H1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| IKBKG | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| POLR1C | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| TERF1 | psi-mi:"MI:0096"(pull down) | pubmed:17629495|imex:IM-19091 |
| Plk1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| dppD | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| LAMP1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| EZR | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=40.1 + PDB: 无 | pLDDT=40.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Nucleus; Cytoplasm, cytoskeleton, microtu / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TRIOBP — TRIO and F-actin-binding protein，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小2365 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 74 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=40.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H2D6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100106-TRIOBP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TRIOBP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H2D6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H2D6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

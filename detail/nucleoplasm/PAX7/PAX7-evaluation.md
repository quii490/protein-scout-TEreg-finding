---
type: protein-evaluation
gene: "PAX7"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PAX7 — REJECTED (研究热度过高 (PubMed strict=1215，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PAX7 / HUP1 |
| 蛋白名称 | Paired box protein Pax-7 |
| 蛋白大小 | 505 aa / 55.1 kDa |
| UniProt ID | P23759 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 505 aa / 55.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1215 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001356, IPR017970, IPR009057, IPR003654, IPR043 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **84.0/180** | |
| **归一化总分** | | | **46.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1215 |
| PubMed broad count | 2523 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HUP1 |

**关键文献**:
1. CLIC5 promotes myoblast differentiation and skeletal muscle regeneration via the BGN-mediated canonical Wnt/β-catenin signaling pathway.. *Science advances*. PMID: 39999205
2. Acetylation of PAX7 controls muscle stem cell self-renewal and differentiation potential in mice.. *Nature communications*. PMID: 34059674
3. Interplay between Pitx2 and Pax7 temporally governs specification of extraocular muscle stem cells.. *PLoS genetics*. PMID: 38875306
4. Human skeletal muscle organoids model fetal myogenesis and sustain uncommitted PAX7 myogenic progenitors.. *eLife*. PMID: 37963071
5. Understanding the role of NOTCH2 mutation in centronuclear myopathy.. *Molecular therapy : the journal of the American Society of Gene Therapy*. PMID: 40336196

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.0 |
| 高置信度残基 (pLDDT>90) 占比 | 23.4% |
| 置信残基 (pLDDT 70-90) 占比 | 11.9% |
| 中等置信 (pLDDT 50-70) 占比 | 18.8% |
| 低置信 (pLDDT<50) 占比 | 45.9% |
| 有序区域 (pLDDT>70) 占比 | 35.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=62.0），有序残基占 35.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR017970, IPR009057, IPR003654, IPR043182; Pfam: PF00046, PF00292, PF12360 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MYOG | 0.938 | 0.000 | — |
| MYOD1 | 0.932 | 0.292 | — |
| FOXO1 | 0.925 | 0.071 | — |
| PAX3 | 0.907 | 0.000 | — |
| MYF5 | 0.901 | 0.000 | — |
| ASH2L | 0.871 | 0.314 | — |
| MYF6 | 0.850 | 0.000 | — |
| SIX1 | 0.759 | 0.000 | — |
| SOX10 | 0.748 | 0.065 | — |
| SNAI2 | 0.733 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| AKR1B1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| FHL1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| TCAP | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| CRK | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| SRC | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| FYN | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| NCK1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| ENSMUSP00000030508.7 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | imex:IM-13773|pubmed:20178747 |
| HOMER3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| KRTAP19-7 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.0 + PDB: 无 | pLDDT=62.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. PAX7 — Paired box protein Pax-7，研究基础较多，新颖性有限。
2. 蛋白大小505 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1215 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=62.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1215 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P23759
- Protein Atlas: https://www.proteinatlas.org/ENSG00000009709-PAX7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PAX7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P23759
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P23759-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P23759 |
| SMART | SM00389;SM00351; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001356;IPR017970;IPR009057;IPR003654;IPR043182;IPR001523;IPR022106;IPR043565;IPR036388; |
| Pfam | PF00046;PF00292;PF12360; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000009709-PAX7/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| NFIC | Intact, Biogrid | true |
| NEDD4 | Biogrid | false |
| NFIA | Intact | false |
| NFIB | Intact | false |
| WDR5 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

---
type: protein-evaluation
gene: "EYA4"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EYA4 — REJECTED (研究热度过高 (PubMed strict=129，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EYA4 |
| 蛋白名称 | EYA4 (UniProt未获取) |
| 蛋白大小 | 未知 aa / 未知 kDa |
| UniProt ID | EYA4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: 暂无数据（UniProt获取失败） |
| 蛋白大小 | 5/10 | ×1 | 5 | 未知 aa / 未知 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=129 篇 (>100→REJECTED) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | 暂无数据 (UniProt未获取) |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **68.5/180** | |
| **归一化总分** | | | **38.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | 暂无数据（UniProt获取失败） | 获取失败 |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- 无 GO-CC 注释 (UniProt未获取)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 129 |
| PubMed broad count | 175 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Dilated Cardiomyopathy Overview.. **. PMID: 20301486
2. Genetic Hearing Loss Overview.. **. PMID: 20301607
3. Delineating the tumour-regulatory roles of EYA4.. *Biochemical pharmacology*. PMID: 36849065
4. Profiling the proximal proteome of the activated μ-opioid receptor.. *Nature chemical biology*. PMID: 38528119
5. Phosphorylation determines the glucose metabolism reprogramming and tumor-promoting activity of sine oculis homeobox 1.. *Signal transduction and targeted therapy*. PMID: 39617783

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |


**PAE**: AlphaFold 数据未获取，无 PAE 可用。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 暂无数据 (UniProt未获取) |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SIX1 | 0.895 | 0.723 | — |
| TCF21 | 0.805 | 0.000 | — |
| SIX4 | 0.803 | 0.490 | — |
| SIX2 | 0.795 | 0.673 | — |
| NLRX1 | 0.788 | 0.000 | — |
| RBM20 | 0.741 | 0.000 | — |
| ABCC9 | 0.715 | 0.000 | — |
| TMPO | 0.690 | 0.000 | — |
| SIX5 | 0.679 | 0.478 | — |
| NEXN | 0.655 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| URGCP | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| DVL3 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| UBE2D2 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| PLEC | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| QSER1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| AAK1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| CCDC88A | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| LUZP1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| SEC24B | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| PPIP5K2 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | 暂无数据（UniProt获取失败） / Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. EYA4 — EYA4 (UniProt未获取)，研究基础较多，新颖性有限。
2. 蛋白大小未知 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 129 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 129 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/EYA4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000112319-EYA4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EYA4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/EYA4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O95677 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR028472;IPR006545;IPR042577;IPR038102; |
| Pfam | PF00702; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000112319-EYA4/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CIC | Biogrid | false |
| DCTPP1 | Biogrid | false |
| MAPK1 | Biogrid | false |
| PLK1 | Biogrid | false |
| SCO1 | Biogrid | false |
| SCO2 | Biogrid | false |
| SIX1 | Biogrid | false |
| SIX2 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

---
type: protein-evaluation
gene: "CIPC"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CIPC 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CIPC / KIAA1737 |
| 蛋白名称 | CLOCK-interacting pacemaker |
| 蛋白大小 | 399 aa / 42.7 kDa |
| UniProt ID | Q9C0C6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; 额外: Nucleoli; UniProt: Nucleus; Cytoplasm, cytosol |
| 蛋白大小 | 10/10 | ×1 | 10 | 399 aa / 42.7 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=71 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR031602; Pfam: PF15800 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 13 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **100.0/180** | |
| **归一化总分** | | | **55.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Nucleoli | Supported |
| UniProt | Nucleus; Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 71 |
| PubMed broad count | 199 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1737 |

**关键文献**:
1. Satellite cell-specific deletion of Cipc alleviates myopathy in mdx mice.. *Cell reports*. PMID: 35705041
2. Intestinal microbiota by angiotensin receptor blocker therapy exerts protective effects against hypertensive damages.. *iMeta*. PMID: 39135690
3. Versatile function of the circadian protein CIPC as a regulator of Erk activation.. *Biochemical and biophysical research communications*. PMID: 26657846
4. cipC is important for Aspergillus fumigatus virulence.. *APMIS : acta pathologica, microbiologica, et immunologica Scandinavica*. PMID: 28120495
5. CIPC is a mammalian circadian clock protein without invertebrate homologues.. *Nature cell biology*. PMID: 17310242

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.1 |
| 高置信度残基 (pLDDT>90) 占比 | 14.3% |
| 置信残基 (pLDDT 70-90) 占比 | 5.0% |
| 中等置信 (pLDDT 50-70) 占比 | 34.6% |
| 低置信 (pLDDT<50) 占比 | 46.1% |
| 有序区域 (pLDDT>70) 占比 | 19.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=58.1），有序残基占 19.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR031602; Pfam: PF15800 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CLOCK | 0.912 | 0.877 | — |
| ARNTL2 | 0.858 | 0.760 | — |
| NPAS2 | 0.802 | 0.711 | — |
| ARNTL | 0.768 | 0.639 | — |
| ZMYM4 | 0.572 | 0.552 | — |
| CIART | 0.531 | 0.000 | — |
| NR1D2 | 0.515 | 0.000 | — |
| ITGB1BP1 | 0.439 | 0.000 | — |
| HIVEP2 | 0.436 | 0.000 | — |
| LY75 | 0.429 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Exo84 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| Cog6 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| APPL1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| Dmel\CG4853 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| "BcDNA:AT31258" | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| UbcE2M | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| AIMP1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Mabi | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG13838 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG13423 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 13，IntAct interactions: 15
- 调控相关比例: 0 / 13 = 0%

**评价**: STRING 13 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.1 + PDB: 无 | pLDDT=58.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, cytosol / Nucleoplasm, Cytosol; 额外: Nucleoli | 一致 |
| PPI | STRING + IntAct | 13 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CIPC — CLOCK-interacting pacemaker，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小399 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 71 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=58.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9C0C6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198894-CIPC/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CIPC
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9C0C6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000198894-CIPC/subcellular

![](https://images.proteinatlas.org/644/1081_H4_1_red_green.jpg)
![](https://images.proteinatlas.org/644/1081_H4_2_red_green.jpg)
![](https://images.proteinatlas.org/644/1902_F2_1_red_green.jpg)
![](https://images.proteinatlas.org/644/1902_F2_2_red_green.jpg)
![](https://images.proteinatlas.org/644/1918_B2_10_cr5cacab97c26d7_red_green.jpg)
![](https://images.proteinatlas.org/644/1918_B2_18_cr5cacab97c2b9a_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9C0C6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9C0C6 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR031602; |
| Pfam | PF15800; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000198894-CIPC/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CLOCK | Biogrid, Bioplex | true |
| COPS5 | Biogrid | false |
| NCK2 | Intact | false |
| NPAS2 | Bioplex | false |
| RABGEF1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

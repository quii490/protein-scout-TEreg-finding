---
type: protein-evaluation
gene: "EDRF1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EDRF1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EDRF1 / C10orf137 |
| 蛋白名称 | Erythroid differentiation-related factor 1 |
| 蛋白大小 | 1238 aa / 138.5 kDa |
| UniProt ID | Q3B7T1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Centrosome, Cytosol; UniProt: Nucleus |
| 蛋白大小 | 5/10 | ×1 | 5 | 1238 aa / 138.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=75.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR056582, IPR056583; Pfam: PF23788, PF23723 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **136.5/180** | |
| **归一化总分** | | | **75.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Centrosome, Cytosol | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 11 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C10orf137 |

**关键文献**:
1. The diagnostic yield, candidate genes, and pitfalls for a genetic study of intellectual disability in 118 middle eastern families.. *Scientific reports*. PMID: 36344539
2. Analysis of Cleavage Activity of Dengue Virus Protease by Co-transfections.. *Bio-protocol*. PMID: 38464936
3. A novel erythroid differentiation related gene EDRF1 upregulating globin gene expression in HEL cells.. *Chinese medical journal*. PMID: 12609092
4. cDNA cloning and function analysis of two novel erythroid differentiation related genes.. *Science in China. Series C, Life sciences*. PMID: 18763094
5. Antisense EDRF1 gene inhibited GATA-1 transcription factor DNA-binding activity in K562 cells.. *Science in China. Series C, Life sciences*. PMID: 18759052

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.4 |
| 高置信度残基 (pLDDT>90) 占比 | 36.8% |
| 置信残基 (pLDDT 70-90) 占比 | 34.2% |
| 中等置信 (pLDDT 50-70) 占比 | 9.8% |
| 低置信 (pLDDT<50) 占比 | 19.2% |
| 有序区域 (pLDDT>70) 占比 | 71.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=75.4，有序区 71.0%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR056582, IPR056583; Pfam: PF23788, PF23723 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HSPBP1 | 0.775 | 0.563 | — |
| TTC4 | 0.638 | 0.616 | — |
| CHORDC1 | 0.624 | 0.619 | — |
| HSPA8 | 0.567 | 0.564 | — |
| TEX36 | 0.476 | 0.000 | — |
| IGSF5 | 0.473 | 0.000 | — |
| DNAJC7 | 0.460 | 0.237 | — |
| TMEM179 | 0.452 | 0.000 | — |
| EXOC5 | 0.452 | 0.441 | — |
| ZBTB11 | 0.452 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HSP90AA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19875381 |
| tyrS | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| CUL2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| HSPA8 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| DISC1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| DNAJC13 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| NMT1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| MLF1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| TBCE | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.4 + PDB: 无 | pLDDT=75.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Centrosome, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. EDRF1 — Erythroid differentiation-related factor 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1238 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q3B7T1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000107938-EDRF1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EDRF1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q3B7T1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000107938-EDRF1/subcellular

![](https://images.proteinatlas.org/31820/371_F11_2_red_green.jpg)
![](https://images.proteinatlas.org/31820/371_F11_3_red_green.jpg)
![](https://images.proteinatlas.org/31820/372_F11_2_red_green.jpg)
![](https://images.proteinatlas.org/31820/372_F11_4_red_green.jpg)
![](https://images.proteinatlas.org/31820/374_F11_1_red_green.jpg)
![](https://images.proteinatlas.org/31820/374_F11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q3B7T1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q3B7T1 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR056582;IPR056583; |
| Pfam | PF23788;PF23723; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000107938-EDRF1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HSPBP1 | Biogrid, Opencell | true |
| APP | Intact | false |
| ATXN1 | Intact | false |
| ATXN3 | Intact | false |
| CAPZB | Opencell | false |
| EIF3B | Opencell | false |
| EIF4A1 | Opencell | false |
| HSP90AA1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

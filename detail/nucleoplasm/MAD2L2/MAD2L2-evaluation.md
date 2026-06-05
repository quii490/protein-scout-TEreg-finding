---
type: protein-evaluation
gene: "MAD2L2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MAD2L2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MAD2L2 / MAD2B, REV7 |
| 蛋白名称 | Mitotic spindle assembly checkpoint protein MAD2B |
| 蛋白大小 | 211 aa / 24.3 kDa |
| UniProt ID | Q9UI95 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm, cytoskeleton, spindle; Cytoplasm; Chromo |
| 蛋白大小 | 10/10 | ×1 | 10 | 211 aa / 24.3 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=79 篇 (≤80→4) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=90.4; PDB: 3ABD, 3ABE, 3VU7, 4EXT, 4GK0, 4GK5, 5XPT |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR003511, IPR036570, IPR045091; Pfam: PF02301 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.0/180** | |
| **归一化总分** | | | **64.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Cytoplasm, cytoskeleton, spindle; Cytoplasm; Chromosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- chromosome (GO:0005694)
- cytoplasm (GO:0005737)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- site of DNA damage (GO:0090734)
- site of double-strand break (GO:0035861)
- spindle (GO:0005819)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 79 |
| PubMed broad count | 211 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MAD2B, REV7 |

**关键文献**:
1. The shieldin complex mediates 53BP1-dependent DNA repair.. *Nature*. PMID: 30022168
2. Fanconi Anemia.. **. PMID: 20301575
3. AURKB promotes bladder cancer progression by deregulating the p53 DNA damage response pathway via MAD2L2.. *Journal of translational medicine*. PMID: 38515112
4. Mitotic syndicates Aurora Kinase B (AURKB) and mitotic arrest deficient 2 like 2 (MAD2L2) in cohorts of DNA damage response (DDR) and tumorigenesis.. *Mutation research. Reviews in mutation research*. PMID: 34083040
5. The promoting effect and mechanism of MAD2L2 on stemness maintenance and malignant progression in glioma.. *Journal of translational medicine*. PMID: 38017538

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.4 |
| 高置信度残基 (pLDDT>90) 占比 | 73.0% |
| 置信残基 (pLDDT 70-90) 占比 | 18.5% |
| 中等置信 (pLDDT 50-70) 占比 | 4.7% |
| 低置信 (pLDDT<50) 占比 | 3.8% |
| 有序区域 (pLDDT>70) 占比 | 91.5% |
| 可用 PDB 条目 | 3ABD, 3ABE, 3VU7, 4EXT, 4GK0, 4GK5, 5XPT, 5XPU, 6BC8, 6BCD |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3ABD, 3ABE, 3VU7, 4EXT, 4GK0, 4GK5, 5XPT, 5XPU, 6BC8, 6BCD）+ AlphaFold极高置信度预测（pLDDT=90.4），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003511, IPR036570, IPR045091; Pfam: PF02301 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| REV1 | 0.999 | 0.997 | — |
| POLD2 | 0.999 | 0.956 | — |
| REV3L | 0.999 | 0.997 | — |
| SHLD2 | 0.999 | 0.973 | — |
| POLD3 | 0.998 | 0.510 | — |
| SHLD3 | 0.998 | 0.939 | — |
| SHLD1 | 0.997 | 0.301 | — |
| TRIP13 | 0.980 | 0.919 | — |
| POLD1 | 0.978 | 0.529 | — |
| MAD2L1 | 0.975 | 0.474 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSMUSP00000081146.3 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| PRRC2A | psi-mi:"MI:0018"(two hybrid) | pubmed:14667819|mint:MINT-5216 |
| MYBPC2 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| sctE | psi-mi:"MI:0018"(two hybrid) | imex:IM-11936|pubmed:17719540 |
| CDC27 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-11936|pubmed:17719540 |
| CDC20 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-11936|pubmed:17719540 |
| FZR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-11936|pubmed:17719540 |
| RBBP6 | psi-mi:"MI:0018"(two hybrid) | pubmed:18624398|imex:IM-19021 |
| TRIP13 | psi-mi:"MI:0397"(two hybrid array) | pubmed:19060904|imex:IM-20259 |
| RCN1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.4 + PDB: 3ABD, 3ABE, 3VU7, 4EXT, 4GK0,  | pLDDT=90.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, cytoskeleton, spindle; Cytopla / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. MAD2L2 — Mitotic spindle assembly checkpoint protein MAD2B，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小211 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 79 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UI95
- Protein Atlas: https://www.proteinatlas.org/ENSG00000116670-MAD2L2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MAD2L2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UI95
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000116670-MAD2L2/subcellular

![](https://images.proteinatlas.org/3882/1978_E6_1_red_green.jpg)
![](https://images.proteinatlas.org/3882/1978_E6_3_red_green.jpg)
![](https://images.proteinatlas.org/3882/2104_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/3882/2104_C10_2_red_green.jpg)
![](https://images.proteinatlas.org/3882/2142_F10_2_red_green.jpg)
![](https://images.proteinatlas.org/3882/2142_F10_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UI95-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

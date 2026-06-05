---
type: protein-evaluation
gene: "FBRS"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FBRS 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBRS / FBS, FBS1 |
| 蛋白名称 | Probable fibrosin-1 |
| 蛋白大小 | 460 aa / 48.4 kDa |
| UniProt ID | Q9HAH7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 460 aa / 48.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=21 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=52.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR023246; Pfam: PF15336 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119.5/180** | |
| **归一化总分** | | | **66.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 21 |
| PubMed broad count | 156 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FBS, FBS1 |

**关键文献**:
1. De Novo Pathogenic Variant in FBRSL1, Non OMIM Gene Paralogue AUTS2, Causes a Novel Recognizable Syndromic Manifestation with Intellectual Disability; An Additional Patient and Review of the Literature.. *Genes*. PMID: 39062605
2. Implantable bioelectrodes: challenges, strategies, and future directions.. *Biomaterials science*. PMID: 38175154
3. Regulating Blood Clot Fibrin Films to Manipulate Biomaterial-Mediated Foreign Body Responses.. *Research (Washington, D.C.)*. PMID: 37719049
4. Different Molecular Features of Epithelioid and Giant Cells in Foreign Body Reaction Identified by Single-Cell RNA Sequencing.. *The Journal of investigative dermatology*. PMID: 35853485
5. Transcriptional Complexity and Distinct Expression Patterns of auts2 Paralogs in Danio rerio.. *G3 (Bethesda, Md.)*. PMID: 28626003

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 52.3 |
| 高置信度残基 (pLDDT>90) 占比 | 3.0% |
| 置信残基 (pLDDT 70-90) 占比 | 2.6% |
| 中等置信 (pLDDT 50-70) 占比 | 44.8% |
| 低置信 (pLDDT<50) 占比 | 49.6% |
| 有序区域 (pLDDT>70) 占比 | 5.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=52.3），有序残基占 5.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR023246; Pfam: PF15336 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PCGF5 | 0.956 | 0.869 | — |
| RYBP | 0.921 | 0.867 | — |
| RNF2 | 0.900 | 0.624 | — |
| YAF2 | 0.885 | 0.806 | — |
| PCGF3 | 0.879 | 0.628 | — |
| PCGF6 | 0.871 | 0.702 | — |
| CSNK2A2 | 0.861 | 0.843 | — |
| RING1 | 0.827 | 0.375 | — |
| DCAF7 | 0.819 | 0.717 | — |
| CSNK2A1 | 0.793 | 0.764 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| fklB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| CSNK2A2 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-17578|pubmed:23455922 |
| MARF1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| SOWAHA | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| HELZ | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| PCGF3 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| PCGF6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MYCL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| P4HA3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PRPF31 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=52.3 + PDB: 无 | pLDDT=52.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FBRS — Probable fibrosin-1，非常新颖，仅有少数基础研究。
2. 蛋白大小460 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 21 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=52.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9HAH7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000156860-FBRS/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBRS
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HAH7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000156860-FBRS/subcellular

![](https://images.proteinatlas.org/44117/518_C3_1_red_green.jpg)
![](https://images.proteinatlas.org/44117/518_C3_2_red_green.jpg)
![](https://images.proteinatlas.org/44117/530_C3_1_red_green.jpg)
![](https://images.proteinatlas.org/44117/530_C3_2_red_green.jpg)
![](https://images.proteinatlas.org/44117/558_C3_1_red_green.jpg)
![](https://images.proteinatlas.org/44117/558_C3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9HAH7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

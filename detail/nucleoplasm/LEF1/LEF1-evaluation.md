---
type: protein-evaluation
gene: "LEF1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## LEF1 — REJECTED (研究热度过高 (PubMed strict=1484，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LEF1 |
| 蛋白名称 | Lymphoid enhancer-binding factor 1 |
| 蛋白大小 | 399 aa / 44.2 kDa |
| UniProt ID | Q9UJU2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 399 aa / 44.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1484 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR027397, IPR013558, IPR009071, IPR036910, IPR024 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 12 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- beta-catenin-TCF complex (GO:1990907)
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- protein-DNA complex (GO:0032993)
- transcription regulator complex (GO:0005667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1484 |
| PubMed broad count | 2438 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Increased LEF1 protein levels and isoform switching drive cell proliferation in chronic lymphocytic leukemia.. *Blood*. PMID: 40983031
2. Single-cell multiomics identifies Tcf1 and Lef1 as key initiators of early thymic progenitor fate.. *Science immunology*. PMID: 40938954
3. LEF1 intragenic deletion induces a dominant-negative isoform and unveils a Wnt/β-catenin vulnerability in T-ALL.. *Blood*. PMID: 40857670
4. LEF1 haploinsufficiency causes ectodermal dysplasia.. *Clinical genetics*. PMID: 32022899
5. HMGB proteins and arthritis.. *Human cell*. PMID: 28916968

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.0 |
| 高置信度残基 (pLDDT>90) 占比 | 15.8% |
| 置信残基 (pLDDT 70-90) 占比 | 5.3% |
| 中等置信 (pLDDT 50-70) 占比 | 27.8% |
| 低置信 (pLDDT<50) 占比 | 51.1% |
| 有序区域 (pLDDT>70) 占比 | 21.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=57.0），有序残基占 21.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027397, IPR013558, IPR009071, IPR036910, IPR024940; Pfam: PF08347, PF00505 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HNF4A | 0.999 | 0.051 | — |
| SMAD4 | 0.999 | 0.335 | — |
| CTNNB1 | 0.999 | 0.996 | — |
| NLK | 0.993 | 0.796 | — |
| FHL2 | 0.988 | 0.000 | — |
| EP300 | 0.981 | 0.354 | — |
| SMAD2 | 0.978 | 0.540 | — |
| SMAD3 | 0.978 | 0.540 | — |
| JUP | 0.971 | 0.638 | — |
| HDAC1 | 0.966 | 0.333 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TLE1 | psi-mi:"MI:0047"(far western blotting) | pubmed:9751710 |
| Ctnnb1 | psi-mi:"MI:0065"(isothermal titration calorimetry) | imex:IM-14500|pubmed:16293619 |
| 7242199 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| DPYSL2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| RUNX3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12146|pubmed:18772112 |
| MLLT11 | psi-mi:"MI:0018"(two hybrid) | pubmed:26079538|imex:IM-26244 |
| EBI-6620336 | psi-mi:"MI:0412"(electrophoretic mobility supershi | pubmed:26079538|imex:IM-26244 |
| PRMT6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NFE2L2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32911434|imex:IM-27648 |
| TNFSF4 | psi-mi:"MI:0432"(one hybrid) | doi:10.1093/nar/gkaa1055|pubme |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 12
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 12 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.0 + PDB: 无 | pLDDT=57.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 12 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. LEF1 — Lymphoid enhancer-binding factor 1，研究基础较多，新颖性有限。
2. 蛋白大小399 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1484 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=57.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1484 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UJU2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000138795-LEF1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LEF1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UJU2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000138795-LEF1/subcellular

![](https://images.proteinatlas.org/2087/1778_C2_2_red_green.jpg)
![](https://images.proteinatlas.org/2087/1778_C2_6_red_green.jpg)
![](https://images.proteinatlas.org/2087/32_A1_1_red_green.jpg)
![](https://images.proteinatlas.org/2087/32_A1_2_red_green.jpg)
![](https://images.proteinatlas.org/2087/34_A1_1_red_green.jpg)
![](https://images.proteinatlas.org/2087/34_A1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UJU2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

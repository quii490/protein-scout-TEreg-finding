---
type: protein-evaluation
gene: "NRIP1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NRIP1 — REJECTED (研究热度过高 (PubMed strict=151，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NRIP1 |
| 蛋白名称 | Nuclear receptor-interacting protein 1 |
| 蛋白大小 | 1158 aa / 126.9 kDa |
| UniProt ID | P48552 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli; 额外: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 1158 aa / 126.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=151 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=45.9; PDB: 2GPO, 2GPP, 4S14, 4S15, 5NTI, 5NTN, 5NTW |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026649, IPR031405, IPR031406, IPR031407, IPR031 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.5/180** | |
| **归一化总分** | | | **44.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli; 额外: Cytosol | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- fibrillar center (GO:0001650)
- histone deacetylase complex (GO:0000118)
- nuclear speck (GO:0016607)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 151 |
| PubMed broad count | 311 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. NRIP1 aggravates lung injury caused by Pseudomonas aeruginosa in mice by increasing PIAS1 ubiquitination.. *Aging*. PMID: 35460552
2. The Genetic Determinants and Genomic Consequences of Non-Leukemogenic Somatic Point Mutations.. *medRxiv : the preprint server for health sciences*. PMID: 39228737
3. Emerging roles of circ_NRIP1 in tumor development and cancer therapy (Review).. *Oncology letters*. PMID: 37332333
4. RIP140 deficiency enhances cardiac fuel metabolism and protects mice from heart failure.. *The Journal of clinical investigation*. PMID: 36927960
5. NRIP1 regulates cell proliferation in lung adenocarcinoma cells.. *Journal of biochemistry*. PMID: 38102728

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 45.9 |
| 高置信度残基 (pLDDT>90) 占比 | 0.5% |
| 置信残基 (pLDDT 70-90) 占比 | 11.5% |
| 中等置信 (pLDDT 50-70) 占比 | 11.4% |
| 低置信 (pLDDT<50) 占比 | 76.6% |
| 有序区域 (pLDDT>70) 占比 | 12.0% |
| 可用 PDB 条目 | 2GPO, 2GPP, 4S14, 4S15, 5NTI, 5NTN, 5NTW, 5NU1, 6FZU, 6G05 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=45.9），有序残基占 12.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026649, IPR031405, IPR031406, IPR031407, IPR031408; Pfam: PF15687, PF15688, PF15689 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ESR1 | 0.999 | 0.844 | — |
| PPARGC1A | 0.985 | 0.292 | — |
| RORA | 0.982 | 0.900 | — |
| CTBP1 | 0.968 | 0.778 | — |
| NR2C1 | 0.930 | 0.286 | — |
| RORC | 0.910 | 0.900 | — |
| NCOR1 | 0.907 | 0.090 | — |
| FOXA1 | 0.902 | 0.000 | — |
| ESRRG | 0.898 | 0.824 | — |
| RARA | 0.895 | 0.839 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CEP70 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CTBP2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TRAF2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| LDOC1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TEX11 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CCDC85B | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TULP3 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| ilvE1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| Esrrb | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20362541|imex:IM-16928 |
| N | psi-mi:"MI:0018"(two hybrid) | imex:IM-11904|pubmed:18267075 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=45.9 + PDB: 2GPO, 2GPP, 4S14, 4S15, 5NTI,  | pLDDT=45.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Nucleoli; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. NRIP1 — Nuclear receptor-interacting protein 1，研究基础较多，新颖性有限。
2. 蛋白大小1158 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 151 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=45.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 151 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P48552
- Protein Atlas: https://www.proteinatlas.org/ENSG00000180530-NRIP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NRIP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P48552
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000180530-NRIP1/subcellular

![](https://images.proteinatlas.org/29785/1817_G9_2_red_green.jpg)
![](https://images.proteinatlas.org/29785/1817_G9_3_red_green.jpg)
![](https://images.proteinatlas.org/29785/1874_F12_24_cr5b6d38a290174_red_green.jpg)
![](https://images.proteinatlas.org/29785/1874_F12_29_cr5b6d38a29017f_red_green.jpg)
![](https://images.proteinatlas.org/29785/1886_E11_1_red_green.jpg)
![](https://images.proteinatlas.org/29785/1886_E11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P48552-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

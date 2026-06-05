---
type: protein-evaluation
gene: "CKAP2L"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CKAP2L — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CKAP2L |
| 蛋白名称 | Cytoskeleton-associated protein 2-like |
| 蛋白大小 | 745 aa / 83.6 kDa |
| UniProt ID | Q8IYA6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Microtubules; 额外: Mitotic spindle, Primary cilium, Cytosol; UniProt: Cytoplasm, cytoskeleton, spindle pole |
| 蛋白大小 | 10/10 | ×1 | 10 | 745 aa / 83.6 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=42 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=54.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR052855, IPR029197; Pfam: PF15297 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 7 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **90.0/180** | |
| **归一化总分** | | | **50.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Microtubules; 额外: Mitotic spindle, Primary cilium, Cytosol | Supported |
| UniProt | Cytoplasm, cytoskeleton, spindle pole | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- cilium (GO:0005929)
- cytosol (GO:0005829)
- microtubule cytoskeleton (GO:0015630)
- mitotic spindle (GO:0072686)
- spindle pole (GO:0000922)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 42 |
| PubMed broad count | 51 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Smoking promotes the progression of bladder cancer through FOXM1/CKAP2L axis.. *Journal of translational medicine*. PMID: 40646610
2. CKAP2L, transcriptionally inhibited by FOXP3, promotes breast carcinogenesis through the AKT/mTOR pathway.. *Experimental cell research*. PMID: 35065924
3. Human CKAP2L shows a cell cycle-dependent expression pattern and exhibits microtubule-stabilizing properties.. *FEBS open bio*. PMID: 39073037
4. IGF2BP2 promotes ovarian cancer growth and metastasis by upregulating CKAP2L protein expression in an m(6) A-dependent manner.. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology*. PMID: 37665628
5. Pan-cancer analysis reveals the prognostic and immunotherapeutic value of cytoskeleton-associated protein 2-like.. *Scientific reports*. PMID: 37225919

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 54.3 |
| 高置信度残基 (pLDDT>90) 占比 | 8.2% |
| 置信残基 (pLDDT 70-90) 占比 | 19.3% |
| 中等置信 (pLDDT 50-70) 占比 | 9.8% |
| 低置信 (pLDDT<50) 占比 | 62.7% |
| 有序区域 (pLDDT>70) 占比 | 27.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=54.3），有序残基占 27.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052855, IPR029197; Pfam: PF15297 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HJURP | 0.913 | 0.000 | — |
| MELK | 0.912 | 0.000 | — |
| DLGAP5 | 0.897 | 0.000 | — |
| CEP55 | 0.886 | 0.000 | — |
| ASPM | 0.883 | 0.000 | — |
| CDCA2 | 0.871 | 0.000 | — |
| BUB1 | 0.867 | 0.000 | — |
| NCAPG | 0.864 | 0.000 | — |
| KIF14 | 0.852 | 0.000 | — |
| CDCA5 | 0.848 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DCTN1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| PCM1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| SPICE1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| ARL9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| N | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:34232536|imex:IM-29365 |
| ENST00000302450 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |
| EBI-2532316 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-30341|pubmed:40739040 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 7
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 7 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=54.3 + PDB: 无 | pLDDT=54.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, spindle pole / Microtubules; 额外: Mitotic spindle, Primary cilium, | 一致 |
| PPI | STRING + IntAct | 15 + 7 interactions | 数据充分 |

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
1. CKAP2L — Cytoskeleton-associated protein 2-like，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小745 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 42 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=54.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IYA6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000169607-CKAP2L/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CKAP2L
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IYA6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Microtubules (supported)。来源: https://www.proteinatlas.org/ENSG00000169607-CKAP2L/subcellular

![](https://images.proteinatlas.org/70737/1717_G8_32_blue_red_green.jpg)
![](https://images.proteinatlas.org/70737/1717_G8_34_blue_red_green.jpg)
![](https://images.proteinatlas.org/70737/2123_G5_30_blue_red_green.jpg)
![](https://images.proteinatlas.org/70737/2123_G5_42_blue_red_green.jpg)
![](https://images.proteinatlas.org/70737/2127_D10_11_blue_red_green.jpg)
![](https://images.proteinatlas.org/70737/2127_D10_31_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IYA6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

---
type: protein-evaluation
gene: "MASTL"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MASTL 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MASTL / GW, GWL, THC2 |
| 蛋白名称 | Serine/threonine-protein kinase greatwall |
| 蛋白大小 | 879 aa / 97.3 kDa |
| UniProt ID | Q96GX5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, cent |
| 蛋白大小 | 8/10 | ×1 | 8 | 879 aa / 97.3 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=54 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=54.2; PDB: 5LOH, 8V5H |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000961, IPR011009, IPR037638, IPR000719, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.5/180** | |
| **归一化总分** | | | **60.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Nucleus; Cleavage furrow | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- cleavage furrow (GO:0032154)
- microtubule cytoskeleton (GO:0015630)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 54 |
| PubMed broad count | 127 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GW, GWL, THC2 |

**关键文献**:
1. MASTL: A novel therapeutic target for Cancer Malignancy.. *Cancer medicine*. PMID: 32692487
2. IL-22 regulates MASTL expression in intestinal epithelial cells.. *American journal of physiology. Gastrointestinal and liver physiology*. PMID: 38771154
3. The MASTL/YBX1/PAK4 axis regulated by stress-activated STK24 triggers lenvatinib resistance and tumor progression in HCC.. *Hepatology (Baltimore, Md.)*. PMID: 40456026
4. Integrative causal inference illuminates gene-environment interactions linking endocrine disruptors to female infertility.. *Ecotoxicology and environmental safety*. PMID: 40663944
5. The ATM-E6AP-MASTL axis mediates DNA damage checkpoint recovery.. *eLife*. PMID: 37672026

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 54.2 |
| 高置信度残基 (pLDDT>90) 占比 | 20.1% |
| 置信残基 (pLDDT 70-90) 占比 | 13.2% |
| 中等置信 (pLDDT 50-70) 占比 | 6.7% |
| 低置信 (pLDDT<50) 占比 | 60.0% |
| 有序区域 (pLDDT>70) 占比 | 33.3% |
| 可用 PDB 条目 | 5LOH, 8V5H |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=54.2），有序残基占 33.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000961, IPR011009, IPR037638, IPR000719, IPR008271; Pfam: PF00069 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ENSA | 0.995 | 0.154 | — |
| ARPP19 | 0.994 | 0.112 | — |
| PPP2R2D | 0.978 | 0.000 | — |
| CCNB1 | 0.893 | 0.000 | — |
| CDK1 | 0.870 | 0.000 | — |
| PPP2R1A | 0.836 | 0.124 | — |
| PPP2CA | 0.810 | 0.000 | — |
| CCNA2 | 0.791 | 0.000 | — |
| KIF11 | 0.776 | 0.000 | — |
| TTK | 0.773 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Dynll1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| RPS6KA1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-17578|pubmed:23455922 |
| CDK8 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| C16orf70 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28169297|imex:IM-25584 |
| UBN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| CDK18 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| ACBD5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| TAP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| PLEKHA8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=54.2 + PDB: 5LOH, 8V5H | pLDDT=54.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, microtubule organizing ce / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. MASTL — Serine/threonine-protein kinase greatwall，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小879 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 54 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=54.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96GX5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000120539-MASTL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MASTL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96GX5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000120539-MASTL/subcellular

![](https://images.proteinatlas.org/27175/2135_E6_18_blue_red_green.jpg)
![](https://images.proteinatlas.org/27175/2135_E6_80_blue_red_green.jpg)
![](https://images.proteinatlas.org/27175/2165_C6_19_blue_red_green.jpg)
![](https://images.proteinatlas.org/27175/2165_C6_41_blue_red_green.jpg)
![](https://images.proteinatlas.org/27175/212_E11_1_red_green.jpg)
![](https://images.proteinatlas.org/27175/212_E11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96GX5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

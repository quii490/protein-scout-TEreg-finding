---
type: protein-evaluation
gene: "NYNRIN"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NYNRIN 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NYNRIN / CGIN1, KIAA1305 |
| 蛋白名称 | Protein NYNRIN |
| 蛋白大小 | 1898 aa / 208.4 kDa |
| UniProt ID | Q9P2P1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Golgi apparatus; 额外: Nucleoplasm, Vesicles; UniProt: Membrane |
| 蛋白大小 | 5/10 | ×1 | 5 | 1898 aa / 208.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR043502, IPR001584, IPR041588, IPR056629, IPR056 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 11 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **125.0/180** | |
| **归一化总分** | | | **69.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nucleoplasm, Vesicles | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasmic ribonucleoprotein granule (GO:0036464)
- membrane (GO:0016020)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 15 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CGIN1, KIAA1305 |

**关键文献**:
1. Wilms Tumor Predisposition.. **. PMID: 20301471
2. Causal Gene Identification and Biomarker Prioritization in Periodontitis via Integrative Multiomics and Mendelian Randomization.. *Mediators of inflammation*. PMID: 41333919
3. Identification of new Wilms tumour predisposition genes: an exome sequencing study.. *The Lancet. Child & adolescent health*. PMID: 30885698
4. Origination of LTR Retroelement-Derived NYNRIN Coincides with Therian Placental Emergence.. *Molecular biology and evolution*. PMID: 35959649
5. A six-gene prognostic signature for both adult and pediatric acute myeloid leukemia identified with machine learning.. *American journal of translational research*. PMID: 36247279

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.0 |
| 高置信度残基 (pLDDT>90) 占比 | 10.0% |
| 置信残基 (pLDDT 70-90) 占比 | 34.2% |
| 中等置信 (pLDDT 50-70) 占比 | 12.1% |
| 低置信 (pLDDT<50) 占比 | 43.7% |
| 有序区域 (pLDDT>70) 占比 | 44.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=59.0），有序残基占 44.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR043502, IPR001584, IPR041588, IPR056629, IPR056630; Pfam: PF17921, PF23050, PF23052 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SMIM24 | 0.659 | 0.000 | — |
| CPXM1 | 0.632 | 0.000 | — |
| KRBA2 | 0.626 | 0.000 | — |
| SDR39U1 | 0.588 | 0.000 | — |
| CBLN3 | 0.582 | 0.074 | — |
| ARHGAP22 | 0.569 | 0.000 | — |
| STOML1 | 0.545 | 0.000 | — |
| FANCM | 0.532 | 0.528 | — |
| ZBTB46 | 0.525 | 0.065 | — |
| LAPTM4B | 0.524 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| AGTPBP1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| OPG200 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:22810585|imex:IM-17331 |
| FAM167A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CRYAB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CDH8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SAV1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:24255178|imex:IM-21541 |
| PTGES3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TRIM52 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| DUSP16 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CRYAA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 11
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 11 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.0 + PDB: 无 | pLDDT=59.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Golgi apparatus; 额外: Nucleoplasm, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 11 interactions | 数据充分 |

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
1. NYNRIN — Protein NYNRIN，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1898 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=59.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9P2P1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000205978-NYNRIN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NYNRIN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P2P1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (approved)。来源: https://www.proteinatlas.org/ENSG00000205978-NYNRIN/subcellular

![](https://images.proteinatlas.org/18945/117_E1_1_red_green.jpg)
![](https://images.proteinatlas.org/18945/117_E1_2_red_green.jpg)
![](https://images.proteinatlas.org/18945/1383_A6_2_red_green.jpg)
![](https://images.proteinatlas.org/18945/1383_A6_3_red_green.jpg)
![](https://images.proteinatlas.org/18945/1734_E6_2_red_green.jpg)
![](https://images.proteinatlas.org/18945/1734_E6_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9P2P1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

---
type: protein-evaluation
gene: "CAD"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CAD — REJECTED (研究热度过高 (PubMed strict=8737，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CAD |
| 蛋白名称 | Multifunctional protein CAD |
| 蛋白大小 | 2225 aa / 243.0 kDa |
| UniProt ID | P27708 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 2/10 | ×1 | 2 | 2225 aa / 243.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=8737 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=87.0; PDB: 4BY3, 4C6B, 4C6C, 4C6D, 4C6E, 4C6F, 4C6I |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR006680, IPR006132, IPR006130, IPR036901, IPR002 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.0/180** | |
| **归一化总分** | | | **48.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell projection (GO:0042995)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- membrane (GO:0016020)
- neuronal cell body (GO:0043025)
- nuclear matrix (GO:0016363)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8737 |
| PubMed broad count | 76039 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Genetic inhibition of angiopoietin-like protein-3, lipids, and cardiometabolic risk.. *European heart journal*. PMID: 38243829
2. Multi-Omic Insight Into the Molecular Networks in the Pathogenesis of Coronary Artery Disease.. *Journal of the American Heart Association*. PMID: 40135555
3. Enhancer-targeting CRISPR screens at coronary artery disease loci suggest shared mechanisms of disease risk.. *medRxiv : the preprint server for health sciences*. PMID: 40950476
4. Identification and Functional Analysis of CAD Gene Family in Pomegranate (Punica granatum).. *Genes*. PMID: 36672766
5. Transcriptome associated with single-cell analysis reveal the role of S-palmitoylation in coronary artery disease.. *Scientific reports*. PMID: 40307438

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.0 |
| 高置信度残基 (pLDDT>90) 占比 | 61.7% |
| 置信残基 (pLDDT 70-90) 占比 | 29.7% |
| 中等置信 (pLDDT 50-70) 占比 | 3.1% |
| 低置信 (pLDDT<50) 占比 | 5.5% |
| 有序区域 (pLDDT>70) 占比 | 91.4% |
| 可用 PDB 条目 | 4BY3, 4C6B, 4C6C, 4C6D, 4C6E, 4C6F, 4C6I, 4C6J, 4C6K, 4C6L |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4BY3, 4C6B, 4C6C, 4C6D, 4C6E, 4C6F, 4C6I, 4C6J, 4C6K, 4C6L）+ AlphaFold极高置信度预测（pLDDT=87.0），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006680, IPR006132, IPR006130, IPR036901, IPR002082; Pfam: PF01979, PF25596, PF02786 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DHODH | 0.994 | 0.071 | — |
| ASS1 | 0.994 | 0.000 | — |
| PPAT | 0.991 | 0.000 | — |
| OTC | 0.975 | 0.052 | — |
| GLUL | 0.967 | 0.000 | — |
| ADSS2 | 0.963 | 0.000 | — |
| ADSS1 | 0.954 | 0.000 | — |
| GFPT1 | 0.949 | 0.203 | — |
| UMPS | 0.946 | 0.099 | — |
| ASNS | 0.945 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ADH7 | psi-mi:"MI:0111"(dihydrofolate reductase reconstru | pubmed:31454312|imex:IM-26944 |
| ADH6 | psi-mi:"MI:0111"(dihydrofolate reductase reconstru | pubmed:31454312|imex:IM-26944 |
| DFFA | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| DFFB | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TRX3 | psi-mi:"MI:0415"(enzymatic study) | pubmed:15352244 |
| NAF1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:14690591 |
| RBG7 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| CAD5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| GRP9 | psi-mi:"MI:0018"(two hybrid) | pubmed:17287892|imex:IM-19702 |
| SSA2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:19536198 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.0 + PDB: 4BY3, 4C6B, 4C6C, 4C6D, 4C6E,  | pLDDT=87.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CAD — Multifunctional protein CAD，研究基础较多，新颖性有限。
2. 蛋白大小2225 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 8737 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 8737 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P27708
- Protein Atlas: https://www.proteinatlas.org/ENSG00000084774-CAD/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CAD
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P27708
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000084774-CAD/subcellular

![](https://images.proteinatlas.org/65158/1865_A10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/65158/1865_A10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/7781/612_F12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/7781/612_F12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/7781/615_F12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/7781/615_F12_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P27708-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

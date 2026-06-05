---
type: protein-evaluation
gene: "NBN"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NBN — REJECTED (研究热度过高 (PubMed strict=377，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NBN / NBS, NBS1, P95 |
| 蛋白名称 | Nibrin |
| 蛋白大小 | 754 aa / 85.0 kDa |
| UniProt ID | O60934 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Mitotic chromosome, Golgi apparatus; UniProt: Nucleus; Chromosome; Nucleus, PML body; Chromosome, telomere |
| 蛋白大小 | 10/10 | ×1 | 10 | 754 aa / 85.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=377 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.1; PDB: 5WQD, 7SID, 8BAH |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001357, IPR036420, IPR000253, IPR040227, IPR032 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Mitotic chromosome, Golgi apparatus | Supported |
| UniProt | Nucleus; Chromosome; Nucleus, PML body; Chromosome, telomere | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- BRCA1-C complex (GO:0070533)
- chromosomal region (GO:0098687)
- chromosome, telomeric region (GO:0000781)
- cytosol (GO:0005829)
- Golgi apparatus (GO:0005794)
- Mre11 complex (GO:0030870)
- nuclear inclusion body (GO:0042405)
- nucleolus (GO:0005730)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 377 |
| PubMed broad count | 2073 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NBS, NBS1, P95 |

**关键文献**:
1. A Population-Based Study of Genes Previously Implicated in Breast Cancer.. *The New England journal of medicine*. PMID: 33471974
2. Germline Mutations in the BRIP1, BARD1, PALB2, and NBN Genes in Women With Ovarian Cancer.. *Journal of the National Cancer Institute*. PMID: 26315354
3. Frequency of Germline Mutations in 25 Cancer Susceptibility Genes in a Sequential Series of Patients With Breast Cancer.. *Journal of clinical oncology : official journal of the American Society of Clinical Oncology*. PMID: 26976419
4. Gene panel testing of 5589 BRCA1/2-negative index patients with breast cancer in a routine diagnostic setting: results of the German Consortium for Hereditary Breast and Ovarian Cancer.. *Cancer medicine*. PMID: 29522266
5. Nijmegen Breakage Syndrome.. **. PMID: 20301355

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.1 |
| 高置信度残基 (pLDDT>90) 占比 | 29.6% |
| 置信残基 (pLDDT 70-90) 占比 | 15.3% |
| 中等置信 (pLDDT 50-70) 占比 | 10.6% |
| 低置信 (pLDDT<50) 占比 | 44.6% |
| 有序区域 (pLDDT>70) 占比 | 44.9% |
| 可用 PDB 条目 | 5WQD, 7SID, 8BAH |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=63.1），有序残基占 44.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001357, IPR036420, IPR000253, IPR040227, IPR032429; Pfam: PF00533, PF00498, PF08599 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RBBP8 | 0.999 | 0.935 | — |
| ATM | 0.999 | 0.989 | — |
| MRE11 | 0.999 | 0.999 | — |
| RAD50 | 0.999 | 0.994 | — |
| BRIP1 | 0.998 | 0.994 | — |
| BARD1 | 0.998 | 0.994 | — |
| MDC1 | 0.994 | 0.928 | — |
| BRCA1 | 0.993 | 0.868 | — |
| TERF2 | 0.993 | 0.982 | — |
| H2AX | 0.980 | 0.889 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MDC1 | psi-mi:"MI:0663"(confocal microscopy) | imex:IM-11889|pubmed:18001824 |
| H2AX | psi-mi:"MI:0663"(confocal microscopy) | imex:IM-11889|pubmed:18001824 |
| RNF8 | psi-mi:"MI:0416"(fluorescence microscopy) | imex:IM-11890|pubmed:18001825 |
| Mre11 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12131|pubmed:18854157 |
| EBI-6398911 | psi-mi:"MI:0663"(confocal microscopy) | imex:IM-18128|pubmed:23063122 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| INTS3 | psi-mi:"MI:0096"(pull down) | imex:IM-25484|pubmed:19683501 |
| CELA2B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RGS20 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FAM219A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.1 + PDB: 5WQD, 7SID, 8BAH | pLDDT=63.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome; Nucleus, PML body; Chromosome / Nucleoplasm; 额外: Mitotic chromosome, Golgi apparat | 一致 |
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
1. NBN — Nibrin，研究基础较多，新颖性有限。
2. 蛋白大小754 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 377 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=63.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 377 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O60934
- Protein Atlas: https://www.proteinatlas.org/ENSG00000104320-NBN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NBN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60934
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000104320-NBN/subcellular

![](https://images.proteinatlas.org/1429/27_E7_1_red_green.jpg)
![](https://images.proteinatlas.org/1429/27_E7_2_red_green.jpg)
![](https://images.proteinatlas.org/1429/28_E7_1_red_green.jpg)
![](https://images.proteinatlas.org/1429/28_E7_2_red_green.jpg)
![](https://images.proteinatlas.org/80233/2112_F6_1_red_green.jpg)
![](https://images.proteinatlas.org/80233/2112_F6_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O60934-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

---
type: protein-evaluation
gene: "GMNN"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GMNN 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GMNN |
| 蛋白名称 | Geminin |
| 蛋白大小 | 209 aa / 23.6 kDa |
| UniProt ID | O75496 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Basal body, Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 209 aa / 23.6 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=53 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.5; PDB: 1T6F, 1UII, 2LP0, 2WVR, 4BRY, 7KLZ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR022786; Pfam: PF07412 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.5/180** | |
| **归一化总分** | | | **61.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Basal body, Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- transcription repressor complex (GO:0017053)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 53 |
| PubMed broad count | 313 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Integrating single-cell RNA sequencing, WGCNA, and machine learning to identify key biomarkers in hepatocellular carcinoma.. *Scientific reports*. PMID: 40169794
2. Computational analysis for identification of early diagnostic biomarkers and prognostic biomarkers of liver cancer based on GEO and TCGA databases and studies on pathways and biological functions affecting the survival time of liver cancer.. *BMC cancer*. PMID: 34238253
3. GMNN mutations cause female infertility characterized by preimplantation embryo arrest through regulating DNA re-replication.. *Science China. Life sciences*. PMID: 40455380
4. High expression of GMNN predicts malignant progression and poor prognosis in ACC.. *European journal of medical research*. PMID: 36539849
5. Frequent amplification of CENPF, GMNN and CDK13 genes in hepatocellular carcinomas.. *PloS one*. PMID: 22912832

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.5 |
| 高置信度残基 (pLDDT>90) 占比 | 27.8% |
| 置信残基 (pLDDT 70-90) 占比 | 13.9% |
| 中等置信 (pLDDT 50-70) 占比 | 40.2% |
| 低置信 (pLDDT<50) 占比 | 18.2% |
| 有序区域 (pLDDT>70) 占比 | 41.7% |
| 可用 PDB 条目 | 1T6F, 1UII, 2LP0, 2WVR, 4BRY, 7KLZ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=69.5），有序残基占 41.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR022786; Pfam: PF07412 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDT1 | 0.999 | 0.997 | — |
| MCIDAS | 0.956 | 0.949 | — |
| MCM6 | 0.951 | 0.620 | — |
| SPOP | 0.946 | 0.946 | — |
| CDC6 | 0.905 | 0.000 | — |
| ORC6 | 0.894 | 0.000 | — |
| CDC20 | 0.889 | 0.625 | — |
| CCNA2 | 0.882 | 0.680 | — |
| ORC4 | 0.880 | 0.000 | — |
| CDK1 | 0.867 | 0.623 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000477506.1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| CDT1 | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:11125146 |
| Hoxd10 | psi-mi:"MI:0018"(two hybrid) | pubmed:14973489|mint:MINT-5216 |
| Hoxa11 | psi-mi:"MI:0018"(two hybrid) | pubmed:14973489|mint:MINT-5216 |
| Scmh1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14973489|mint:MINT-5216 |
| Hoxa7 | psi-mi:"MI:0096"(pull down) | pubmed:14973489|mint:MINT-5216 |
| Hoxb7 | psi-mi:"MI:0096"(pull down) | pubmed:14973489|mint:MINT-5216 |
| Hoxc8 | psi-mi:"MI:0096"(pull down) | pubmed:14973489|mint:MINT-5216 |
| Hoxc9 | psi-mi:"MI:0096"(pull down) | pubmed:14973489|mint:MINT-5216 |
| Hoxa10 | psi-mi:"MI:0096"(pull down) | pubmed:14973489|mint:MINT-5216 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.5 + PDB: 1T6F, 1UII, 2LP0, 2WVR, 4BRY,  | pLDDT=69.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Basal body, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. GMNN — Geminin，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小209 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 53 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=69.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75496
- Protein Atlas: https://www.proteinatlas.org/ENSG00000112312-GMNN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GMNN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75496
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000112312-GMNN/subcellular

![](https://images.proteinatlas.org/11458/610_B12_4_red_green.jpg)
![](https://images.proteinatlas.org/11458/610_B12_5_red_green.jpg)
![](https://images.proteinatlas.org/11458/613_B12_1_red_green.jpg)
![](https://images.proteinatlas.org/11458/613_B12_2_red_green.jpg)
![](https://images.proteinatlas.org/47327/717_E6_2_red_green.jpg)
![](https://images.proteinatlas.org/47327/717_E6_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O75496-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O75496 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR022786; |
| Pfam | PF07412; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000112312-GMNN/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CCDC146 | Intact, Biogrid | true |
| CCNA2 | Biogrid, Bioplex | true |
| CDKN2A | Intact, Biogrid | true |
| CDT1 | Intact, Biogrid | true |
| MTMR1 | Biogrid, Opencell | true |
| AURKA | Biogrid | false |
| CANX | Opencell | false |
| CDC20 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

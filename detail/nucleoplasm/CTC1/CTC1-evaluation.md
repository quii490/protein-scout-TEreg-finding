---
type: protein-evaluation
gene: "CTC1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CTC1 — REJECTED (研究热度过高 (PubMed strict=129，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CTC1 / C17orf68 |
| 蛋白名称 | CST complex subunit CTC1 |
| 蛋白大小 | 1217 aa / 134.6 kDa |
| UniProt ID | Q2NKJ3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Chromosome, telomere |
| 蛋白大小 | 5/10 | ×1 | 5 | 1217 aa / 134.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=129 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=77.5; PDB: 5W2L, 6W6W, 7U5C, 8D0B, 8D0K, 8SOJ, 8SOK |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029156, IPR042617; Pfam: PF15489 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **89.0/180** | |
| **归一化总分** | | | **49.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus; Chromosome, telomere | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromosome, telomeric region (GO:0000781)
- CST complex (GO:1990879)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 129 |
| PubMed broad count | 241 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C17orf68 |

**关键文献**:
1. Dyskeratosis Congenita and Related Telomere Biology Disorders.. **. PMID: 20301779
2. POT1 recruits and regulates CST-Polα/primase at human telomeres.. *Cell*. PMID: 38838667
3. The evolving genetic landscape of telomere biology disorder dyskeratosis congenita.. *EMBO molecular medicine*. PMID: 39198715
4. Germline variant of CTC1 gene in a patient with pulmonary fibrosis and myelodysplastic syndrome.. *Multidisciplinary respiratory medicine*. PMID: 37404458
5. Associations between ZNF676, CTC1 Gene Polymorphisms and Relative Leukocyte Telomere Length with Myopia and Its Degree.. *Biomedicines*. PMID: 38540151

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.5 |
| 高置信度残基 (pLDDT>90) 占比 | 19.8% |
| 置信残基 (pLDDT 70-90) 占比 | 56.0% |
| 中等置信 (pLDDT 50-70) 占比 | 14.2% |
| 低置信 (pLDDT<50) 占比 | 10.0% |
| 有序区域 (pLDDT>70) 占比 | 75.8% |
| 可用 PDB 条目 | 5W2L, 6W6W, 7U5C, 8D0B, 8D0K, 8SOJ, 8SOK |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（5W2L, 6W6W, 7U5C, 8D0B, 8D0K, 8SOJ, 8SOK）+ AlphaFold极高置信度预测（pLDDT=77.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029156, IPR042617; Pfam: PF15489 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TEN1 | 0.999 | 0.981 | — |
| STN1 | 0.999 | 0.982 | — |
| POLA1 | 0.983 | 0.900 | — |
| TINF2 | 0.972 | 0.045 | — |
| PRIM2 | 0.955 | 0.900 | — |
| TERF1 | 0.946 | 0.000 | — |
| POT1 | 0.939 | 0.249 | — |
| POLA2 | 0.929 | 0.800 | — |
| ACD | 0.906 | 0.000 | — |
| PRIM1 | 0.902 | 0.800 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CYT1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| PET9 | psi-mi:"MI:0096"(pull down) | pubmed:18779372 |
| Stn1 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Pot1b | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:22748632|imex:IM-17623 |
| TEN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RIF1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| NELL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KHDRBS2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DNAJC7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CACNG5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.5 + PDB: 5W2L, 6W6W, 7U5C, 8D0B, 8D0K,  | pLDDT=77.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome, telomere / Nucleoplasm; 额外: Cytosol | 一致 |
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
1. CTC1 — CST complex subunit CTC1，研究基础较多，新颖性有限。
2. 蛋白大小1217 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 129 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 129 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q2NKJ3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000178971-CTC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CTC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q2NKJ3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000178971-CTC1/subcellular

![](https://images.proteinatlas.org/52436/1281_E11_1_red_green.jpg)
![](https://images.proteinatlas.org/52436/1281_E11_6_red_green.jpg)
![](https://images.proteinatlas.org/52436/1313_E11_3_red_green.jpg)
![](https://images.proteinatlas.org/52436/1313_E11_4_red_green.jpg)
![](https://images.proteinatlas.org/52436/2064_C2_1_red_green.jpg)
![](https://images.proteinatlas.org/52436/2064_C2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q2NKJ3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q2NKJ3 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029156;IPR042617; |
| Pfam | PF15489; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000178971-CTC1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| APPBP2 | Intact | false |
| DDOST | Opencell | false |
| FKBP5 | Opencell | false |
| SHLD1 | Biogrid | false |
| STN1 | Intact | false |
| STT3B | Opencell | false |
| TEN1 | Intact | false |
| TPP1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

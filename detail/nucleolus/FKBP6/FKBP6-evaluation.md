---
type: protein-evaluation
gene: "FKBP6"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FKBP6 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FKBP6 / FKBP36 |
| 蛋白名称 | Inactive peptidyl-prolyl cis-trans isomerase FKBP6 |
| 蛋白大小 | 327 aa / 37.2 kDa |
| UniProt ID | O75344 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli fibrillar center, Cytosol; 额外: Microtubules, Cytoki; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 327 aa / 37.2 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=55 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=90.3; PDB: 3B7X |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR042282, IPR046357, IPR001179, IPR011990, IPR019 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119.0/180** | |
| **归一化总分** | | | **66.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli fibrillar center, Cytosol; 额外: Microtubules, Cytokinetic bridge | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- fibrillar center (GO:0001650)
- intercellular bridge (GO:0045171)
- microtubule cytoskeleton (GO:0015630)
- synaptonemal complex (GO:0000795)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 55 |
| PubMed broad count | 68 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FKBP36 |

**关键文献**:
1. Genetics of Equine Reproductive Diseases.. *The Veterinary clinics of North America. Equine practice*. PMID: 32534849
2. In vivo versus in silico assessment of potentially pathogenic missense variants in human reproductive genes.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 37459509
3. Mutation screening of the FKBP6 gene and its association study with spermatogenic impairment in idiopathic infertile men.. *Reproduction (Cambridge, England)*. PMID: 17307919
4. Involvement of FKBP6 in hepatitis C virus replication.. *Scientific reports*. PMID: 26567527
5. Differential DNA methylation of the meiosis-specific gene FKBP6 in testes of yak and cattle-yak hybrids.. *Reproduction in domestic animals = Zuchthygiene*. PMID: 27658575

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.3 |
| 高置信度残基 (pLDDT>90) 占比 | 78.9% |
| 置信残基 (pLDDT 70-90) 占比 | 12.5% |
| 中等置信 (pLDDT 50-70) 占比 | 1.5% |
| 低置信 (pLDDT<50) 占比 | 7.0% |
| 有序区域 (pLDDT>70) 占比 | 91.4% |
| 可用 PDB 条目 | 3B7X |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=90.3，有序区 91.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR042282, IPR046357, IPR001179, IPR011990, IPR019734; Pfam: PF00254 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HSP90AA1 | 0.965 | 0.238 | — |
| PPIL4 | 0.838 | 0.095 | — |
| GTF2IRD1 | 0.836 | 0.000 | — |
| CDK5RAP3 | 0.832 | 0.832 | — |
| HSPA2 | 0.822 | 0.093 | — |
| UBE2I | 0.819 | 0.087 | — |
| DIDO1 | 0.812 | 0.000 | — |
| TBL2 | 0.807 | 0.063 | — |
| FZD9 | 0.798 | 0.000 | — |
| TRIM50 | 0.782 | 0.045 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000252037.4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| NME7 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CCNK | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| IHO1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:29892012|doi:10.1038/s4 |
| CDK5RAP3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| LZTS2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| TMEM9B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| EEF1D | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ENKD1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KANK2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.3 + PDB: 3B7X | pLDDT=90.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoli fibrillar center, Cytosol; 额外: Microtubul | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FKBP6 — Inactive peptidyl-prolyl cis-trans isomerase FKBP6，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小327 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 55 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75344
- Protein Atlas: https://www.proteinatlas.org/ENSG00000077800-FKBP6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FKBP6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75344
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli fibrillar center (supported)。来源: https://www.proteinatlas.org/ENSG00000077800-FKBP6/subcellular

![](https://images.proteinatlas.org/41414/1966_G7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41414/1966_G7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/41414/1978_F11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41414/1978_F11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/41414/2122_H5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/41414/2122_H5_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O75344-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O75344 |
| SMART | SM00028; |
| UniProt Domain [FT] | DOMAIN 54..143; /note="PPIase FKBP-type"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00277" |
| InterPro | IPR042282;IPR046357;IPR001179;IPR011990;IPR019734; |
| Pfam | PF00254; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000077800-FKBP6/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| OSBP | Intact, Biogrid, Bioplex | true |
| ACTA1 | Bioplex | false |
| ALDH3A1 | Intact | false |
| APOD | Bioplex | false |
| CBS | Intact | false |
| CCND1 | Bioplex | false |
| CDC37 | Biogrid | false |
| CDC37L1 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

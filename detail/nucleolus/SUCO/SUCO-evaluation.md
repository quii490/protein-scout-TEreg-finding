---
type: protein-evaluation
gene: "SUCO"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SUCO 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SUCO / C1orf9, CH1, OPT, SLP1 |
| 蛋白名称 | SUN domain-containing ossification factor |
| 蛋白大小 | 1254 aa / 139.4 kDa |
| UniProt ID | Q9UBS9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli fibrillar center, Cytosol; UniProt: Rough endoplasmic reticulum membrane |
| 蛋白大小 | 5/10 | ×1 | 5 | 1254 aa / 139.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=52.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR008979, IPR045120, IPR012919; Pfam: PF07738 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.0/180** | |
| **归一化总分** | | | **62.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli fibrillar center, Cytosol | Approved |
| UniProt | Rough endoplasmic reticulum membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- membrane (GO:0016020)
- rough endoplasmic reticulum (GO:0005791)
- rough endoplasmic reticulum membrane (GO:0030867)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 52 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C1orf9, CH1, OPT, SLP1 |

**关键文献**:
1. High Frequencies of Genetic Variants in Patients with Atypical Femoral Fractures.. *International journal of molecular sciences*. PMID: 38396997
2. TAPT1 interacts with SUCO to maintain the homeostasis of newly synthesized proteins and brain development in mice.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 41379998
3. Recessive genomic and phenotypic variation in consanguineous families with cerebral palsy.. *medRxiv : the preprint server for health sciences*. PMID: 41282771
4. SUCO as a Promising Diagnostic Biomarker of Hepatocellular Carcinoma: Integrated Analysis and Experimental Validation.. *Medical science monitor : international medical journal of experimental and clinical research*. PMID: 31434866
5. Exome sequencing identifies SUCO mutations in mesial temporal lobe epilepsy.. *Neuroscience letters*. PMID: 25668491

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 52.4 |
| 高置信度残基 (pLDDT>90) 占比 | 16.8% |
| 置信残基 (pLDDT 70-90) 占比 | 11.2% |
| 中等置信 (pLDDT 50-70) 占比 | 5.9% |
| 低置信 (pLDDT<50) 占比 | 66.1% |
| 有序区域 (pLDDT>70) 占比 | 28.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=52.4），有序残基占 28.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008979, IPR045120, IPR012919; Pfam: PF07738 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MYL3 | 0.890 | 0.000 | — |
| HIF1A | 0.870 | 0.000 | — |
| FCGRT | 0.735 | 0.000 | — |
| EP300 | 0.687 | 0.000 | — |
| TAPT1 | 0.686 | 0.683 | — |
| EPAS1 | 0.663 | 0.000 | — |
| HSP90AA1 | 0.656 | 0.000 | — |
| AHSA1 | 0.640 | 0.000 | — |
| P4HB | 0.635 | 0.617 | — |
| ARHGAP33 | 0.618 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PSTPIP1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| YWHAH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAZ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAQ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| P4HB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| H4C16 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| DNASE2B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TRAPPC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KCNS3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=52.4 + PDB: 无 | pLDDT=52.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Rough endoplasmic reticulum membrane / Nucleoli fibrillar center, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. SUCO — SUN domain-containing ossification factor，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1254 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=52.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UBS9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000094975-SUCO/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SUCO
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UBS9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli fibrillar center (approved)。来源: https://www.proteinatlas.org/ENSG00000094975-SUCO/subcellular

![](https://images.proteinatlas.org/47251/827_F5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/47251/827_F5_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/47251/829_F5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/47251/829_F5_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/47251/977_F5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/47251/977_F5_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UBS9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UBS9 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 284..453; /note="SUN"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00802" |
| InterPro | IPR008979;IPR045120;IPR012919; |
| Pfam | PF07738; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000094975-SUCO/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ELOVL5 | Biogrid | false |
| FBXO2 | Bioplex | false |
| P4HB | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

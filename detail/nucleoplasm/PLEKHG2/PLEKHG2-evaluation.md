---
type: protein-evaluation
gene: "PLEKHG2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PLEKHG2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PLEKHG2 |
| 蛋白名称 | Pleckstrin homology domain-containing family G member 2 |
| 蛋白大小 | 1386 aa / 148.0 kDa |
| UniProt ID | Q9H7P9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 5/10 | ×1 | 5 | 1386 aa / 148.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=21 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=47.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR035899, IPR000219, IPR011993, IPR001849, IPR043 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **103.0/180** | |
| **归一化总分** | | | **57.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 21 |
| PubMed broad count | 28 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Specific activation of PLEKHG2-induced serum response element-dependent gene transcription by four-and-a-half LIM domains (FHL) 1, but not FHL2 or FHL3.. *Small GTPases*. PMID: 28489964
2. PLEKHG2 promotes heterotrimeric G protein βγ-stimulated lymphocyte migration via Rac and Cdc42 activation and actin polymerization.. *Molecular and cellular biology*. PMID: 24001768
3. The interaction between PLEKHG2 and ABL1 suppresses cell growth via the NF-κB signaling pathway in HEK293 cells.. *Cellular signalling*. PMID: 31100317
4. Four-and-a-half LIM Domains 1 (FHL1) Protein Interacts with the Rho Guanine Nucleotide Exchange Factor PLEKHG2/FLJ00018 and Regulates Cell Morphogenesis.. *The Journal of biological chemistry*. PMID: 27765816
5. Impaired Function of PLEKHG2, a Rho-Guanine Nucleotide-Exchange Factor, Disrupts Corticogenesis in Neurodevelopmental Phenotypes.. *Cells*. PMID: 35203342

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 47.3 |
| 高置信度残基 (pLDDT>90) 占比 | 14.6% |
| 置信残基 (pLDDT 70-90) 占比 | 7.1% |
| 中等置信 (pLDDT 50-70) 占比 | 6.5% |
| 低置信 (pLDDT<50) 占比 | 71.8% |
| 有序区域 (pLDDT>70) 占比 | 21.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=47.3），有序残基占 21.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR035899, IPR000219, IPR011993, IPR001849, IPR043324; Pfam: PF00621, PF22697 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDC42 | 0.820 | 0.371 | — |
| GNB1 | 0.771 | 0.512 | — |
| RHOA | 0.753 | 0.319 | — |
| GNG2 | 0.671 | 0.292 | — |
| FHL1 | 0.656 | 0.525 | — |
| CHRM2 | 0.648 | 0.000 | — |
| RABIF | 0.615 | 0.000 | — |
| RAC1 | 0.577 | 0.319 | — |
| GNAS | 0.574 | 0.292 | — |
| CCNA2 | 0.573 | 0.570 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| inhA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| dxs | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ENSP00000392906.2 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| YWHAH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ACTN3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:29892012|doi:10.1038/s4 |
| UQCC2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| PRPF6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| SLC16A1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| SPTLC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| TMEM33 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=47.3 + PDB: 无 | pLDDT=47.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. PLEKHG2 — Pleckstrin homology domain-containing family G member 2，非常新颖，仅有少数基础研究。
2. 蛋白大小1386 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 21 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=47.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H7P9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000090924-PLEKHG2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PLEKHG2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H7P9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000090924-PLEKHG2/subcellular

![](https://images.proteinatlas.org/48054/735_H9_4_red_green.jpg)
![](https://images.proteinatlas.org/48054/735_H9_7_red_green.jpg)
![](https://images.proteinatlas.org/48054/749_H9_1_red_green.jpg)
![](https://images.proteinatlas.org/48054/749_H9_2_red_green.jpg)
![](https://images.proteinatlas.org/48054/751_A7_1_red_green.jpg)
![](https://images.proteinatlas.org/48054/751_A7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H7P9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H7P9 |
| SMART | SM00233;SM00325; |
| UniProt Domain [FT] | DOMAIN 102..283; /note="DH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00062"; DOMAIN 313..411; /note="PH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00145" |
| InterPro | IPR035899;IPR000219;IPR011993;IPR001849;IPR043324;IPR055251; |
| Pfam | PF00621;PF22697; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000090924-PLEKHG2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ACTN3 | Biogrid | false |
| CDC42 | Biogrid | false |
| FHL1 | Biogrid | false |
| GNB1 | Biogrid | false |
| GNG2 | Biogrid | false |
| PIN1 | Intact | false |
| YWHAH | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

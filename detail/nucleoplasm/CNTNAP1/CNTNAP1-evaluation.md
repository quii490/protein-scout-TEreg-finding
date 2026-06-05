---
type: protein-evaluation
gene: "CNTNAP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CNTNAP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CNTNAP1 / CASPR, NRXN4 |
| 蛋白名称 | Contactin-associated protein 1 |
| 蛋白大小 | 1384 aa / 156.3 kDa |
| UniProt ID | P78357 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Nucleoplasm; UniProt: Membrane; Cell junction, paranodal septate junction |
| 蛋白大小 | 5/10 | x1 | 5 | 1384 aa / 156.3 kDa |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed strict=51 篇 (<=60->6) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=81.1; PDB: 无 |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR013320, IPR000742, IPR000421, IPR036056, IPR002 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **98.5/180** | |
| **归一化总分** | | | **54.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Membrane; Cell junction, paranodal septate junction | Swiss-Prot/TremBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- glutamatergic synapse (GO:0098978)
- membrane (GO:0016020)
- paranodal junction (GO:0033010)
- paranode region of axon (GO:0033270)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 51 |
| PubMed broad count | 181 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CASPR, NRXN4 |

**关键文献**:
1. Phenotypic spectrum and genomics of undiagnosed arthrogryposis multiplex congenita.. *Journal of medical genetics*. PMID: 33820833
2. CNTNAP1-Related Congenital Hypomyelinating Neuropathy.. *Pediatric neurology*. PMID: 30686628
3. A case of CNTNAP1 gene-related abnormality and literature review.. *Technology and health care : official journal of the European Society for Engineering and Medicine*. PMID: 41989346
4. M2-polarization-related CNTNAP1 gene might be a novel immunotherapeutic target and biomarker for clear cell renal cell carcinoma.. *IUBMB life*. PMID: 35023290
5. CNTNAP1 mutations cause CNS hypomyelination and neuropathy with or without arthrogryposis.. *Neurology. Genetics*. PMID: 28374019

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.1 |
| 高置信度残基 (pLDDT>90) 占比 | 48.6% |
| 置信残基 (pLDDT 70-90) 占比 | 32.2% |
| 中等置信 (pLDDT 50-70) 占比 | 7.1% |
| 低置信 (pLDDT<50) 占比 | 12.1% |
| 有序区域 (pLDDT>70) 占比 | 80.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=81.1，有序区 80.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013320, IPR000742, IPR000421, IPR036056, IPR002181; Pfam: PF00754, PF02210 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CNTN1 | 0.999 | 0.141 | — |
| NFASC | 0.999 | 0.127 | — |
| CNTN2 | 0.940 | 0.141 | — |
| KCNA2 | 0.900 | 0.314 | — |
| EPB41 | 0.866 | 0.120 | — |
| PTPRZ1 | 0.861 | 0.095 | — |
| EPB41L5 | 0.857 | 0.000 | — |
| KCNA1 | 0.853 | 0.314 | — |
| MBP | 0.820 | 0.000 | — |
| NXN | 0.809 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NCK1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| vpu | psi-mi:"MI:0096"(pull down) | imex:IM-17346|pubmed:22190034| |
| FYN | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| GRB2 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| ABL1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| CRK | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| Cyfip2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |
| Syngap1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |
| TAFA4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HAVCR2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.1 + PDB: 无 | pLDDT=81.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane; Cell junction, paranodal septate junctio / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ***

**核心优势**:
1. CNTNAP1 -- Contactin-associated protein 1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小1384 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 51 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P78357
- Protein Atlas: https://www.proteinatlas.org/ENSG00000108797-CNTNAP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CNTNAP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P78357
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000108797-CNTNAP1/subcellular

![](https://images.proteinatlas.org/11772/1044_F7_1_red_green.jpg)
![](https://images.proteinatlas.org/11772/1044_F7_2_red_green.jpg)
![](https://images.proteinatlas.org/11772/50_C6_1_red_green.jpg)
![](https://images.proteinatlas.org/11772/50_C6_2_red_green.jpg)
![](https://images.proteinatlas.org/11772/52_C6_1_red_green.jpg)
![](https://images.proteinatlas.org/11772/52_C6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P78357-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

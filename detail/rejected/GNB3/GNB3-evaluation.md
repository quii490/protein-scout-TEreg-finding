---
type: protein-evaluation
gene: "GNB3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GNB3 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=462，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GNB3 |
| 蛋白名称 | Guanine nucleotide-binding protein G(I)/G(S)/G(T) subunit beta-3 |
| 蛋白大小 | 340 aa / 37.2 kDa |
| UniProt ID | P16520 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Plasma membrane; 额外: Golgi apparatus; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 340 aa / 37.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=462 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=97.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR016346, IPR015943, IPR001632, IPR020472, IPR019 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **68.5/180** | |
| **归一化总分** | | | **38.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Golgi apparatus | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell body (GO:0044297)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- dendrite (GO:0030425)
- extracellular exosome (GO:0070062)
- heterotrimeric G-protein complex (GO:0005834)
- plasma membrane (GO:0005886)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 462 |
| PubMed broad count | 547 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Gene Polymorphisms Affecting Erectile Dysfunction.. *Sexual medicine reviews*. PMID: 32169432
2. Association polymorphism of guanine nucleotide-binding protein β3 subunit (GNB3) C825T and insertion/deletion of the angiotensin-converting enzyme (ACE) gene with peripartum cardiomyopathy.. *Frontiers in cardiovascular medicine*. PMID: 37089887
3. Upper Gastrointestinal Sensitization And Symptom Generation.. *Journal of medicine and life*. PMID: 32025247
4. Gene Polymorphisms and Susceptibility to Functional Dyspepsia: A Systematic Review and Meta-Analysis.. *Gastroenterology research and practice*. PMID: 31178907
5. G-Protein β3-Subunit Gene C825T Polymorphism and Cardiovascular Risk: An Updated Review.. *High blood pressure & cardiovascular prevention : the official journal of the Italian Society of Hypertension*. PMID: 25903425

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 97.2 |
| 高置信度残基 (pLDDT>90) 占比 | 97.4% |
| 置信残基 (pLDDT 70-90) 占比 | 2.4% |
| 中等置信 (pLDDT 50-70) 占比 | 0.3% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 99.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=97.2，有序区 99.8%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016346, IPR015943, IPR001632, IPR020472, IPR019775; Pfam: PF25391 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GNGT1 | 0.999 | 0.995 | — |
| GNG13 | 0.999 | 0.995 | — |
| GNG4 | 0.999 | 0.996 | — |
| GNGT2 | 0.999 | 0.995 | — |
| GNG2 | 0.999 | 0.996 | — |
| GNG7 | 0.999 | 0.995 | — |
| GNG3 | 0.998 | 0.995 | — |
| GNG5 | 0.998 | 0.995 | — |
| GNG11 | 0.998 | 0.995 | — |
| GNG12 | 0.998 | 0.995 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ESR2 | psi-mi:"MI:0004"(affinity chromatography technolog | imex:IM-13781|pubmed:21182203 |
| NS | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:22810585|imex:IM-17331 |
| P/V | psi-mi:"MI:0096"(pull down) | pubmed:21911578|imex:IM-17703 |
| GNAI2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CIDEB | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| ZNF131 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SLC36A3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RCAN2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ERBB2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:24189400|imex:IM-21413 |
| GNGT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:25733868|imex:IM-24787 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=97.2 + PDB: 无 | pLDDT=97.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Plasma membrane; 额外: Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. GNB3 — Guanine nucleotide-binding protein G(I)/G(S)/G(T) subunit beta-3，研究基础较多，新颖性有限。
2. 蛋白大小340 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 462 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P16520
- Protein Atlas: https://www.proteinatlas.org/ENSG00000111664-GNB3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GNB3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P16520
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000111664-GNB3/subcellular

![](https://images.proteinatlas.org/40736/2147_F4_20_blue_red_green.jpg)
![](https://images.proteinatlas.org/40736/2147_F4_79_blue_red_green.jpg)
![](https://images.proteinatlas.org/40736/2152_B10_31_blue_red_green.jpg)
![](https://images.proteinatlas.org/40736/2152_B10_40_blue_red_green.jpg)
![](https://images.proteinatlas.org/40736/2171_G8_78_blue_red_green.jpg)
![](https://images.proteinatlas.org/40736/2171_G8_9_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P16520-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

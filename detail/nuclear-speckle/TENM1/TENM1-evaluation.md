---
type: protein-evaluation
gene: "TENM1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TENM1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TENM1 / ODZ1, TNM1 |
| 蛋白名称 | Teneurin-1 |
| 蛋白大小 | 2725 aa / 305.0 kDa |
| UniProt ID | Q9UKZ4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Plasma membrane; UniProt: Cell membrane; Nucleus; Nucleus speckle; Nucleus matrix; Cyt |
| 蛋白大小 | 2/10 | ×1 | 2 | 2725 aa / 305.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=21 篇 (≤40→8) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011042, IPR000742, IPR057627, IPR056823, IPR009 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **106.0/180** | |
| **归一化总分** | | | **58.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Plasma membrane | Approved |
| UniProt | Cell membrane; Nucleus; Nucleus speckle; Nucleus matrix; Cytoplasm, cytoskeleton; Nucleus; Cytoplasm... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytoskeleton (GO:0005856)
- endoplasmic reticulum (GO:0005783)
- extracellular region (GO:0005576)
- Golgi apparatus (GO:0005794)
- neuron projection (GO:0043005)
- nuclear matrix (GO:0016363)
- nuclear speck (GO:0016607)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 21 |
| PubMed broad count | 30 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ODZ1, TNM1 |

**关键文献**:
1. Cartography of teneurin and latrophilin expression reveals spatiotemporal axis heterogeneity in the mouse hippocampus during development.. *PLoS biology*. PMID: 38713721
2. HOXA10, EMX2 and TENM1 expression in the mid-secretory endometrium of infertile women with a Müllerian duct anomaly.. *Reproductive biomedicine online*. PMID: 26896429
3. A role for TENM1 mutations in congenital general anosmia.. *Clinical genetics*. PMID: 27040985
4. Screening and validation of lymph node metastasis risk-factor genes in papillary thyroid carcinoma.. *Frontiers in endocrinology*. PMID: 36465624
5. A Potential Four-Gene Signature and Nomogram for Predicting the Overall Survival of Papillary Thyroid Cancer.. *Disease markers*. PMID: 36193505

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011042, IPR000742, IPR057627, IPR056823, IPR009471; Pfam: PF25024, PF24329, PF23093 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ADGRL3 | 0.988 | 0.967 | — |
| ADGRL1 | 0.986 | 0.967 | — |
| ADGRL2 | 0.986 | 0.967 | — |
| SORBS1 | 0.937 | 0.292 | — |
| EGF | 0.582 | 0.000 | — |
| AFF2 | 0.538 | 0.046 | — |
| ADGRG2 | 0.507 | 0.176 | — |
| DAG1 | 0.505 | 0.000 | — |
| HINT1 | 0.502 | 0.230 | — |
| FAM122C | 0.456 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| H2BC21 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| P | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:unassigned2293|imex:IM- |
| YES1 | psi-mi:"MI:0084"(phage display) | imex:IM-29361|pubmed:35044719 |
| HCN1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:37207277|imex:IM-29810 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 无 | pLDDT=0, v? | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane; Nucleus; Nucleus speckle; Nucleus m / Nucleoplasm, Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

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
1. TENM1 — Teneurin-1，非常新颖，仅有少数基础研究。
2. 蛋白大小2725 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 21 篇，已有一定研究基础
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UKZ4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000009694-TENM1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TENM1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UKZ4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000009694-TENM1/subcellular

![](https://images.proteinatlas.org/63910/2096_C9_1_red_green.jpg)
![](https://images.proteinatlas.org/63910/2096_C9_4_red_green.jpg)
![](https://images.proteinatlas.org/63910/2116_H2_3_red_green.jpg)
![](https://images.proteinatlas.org/63910/2116_H2_4_red_green.jpg)
![](https://images.proteinatlas.org/63910/2144_C2_1_red_green.jpg)
![](https://images.proteinatlas.org/63910/2144_C2_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UKZ4 |
| SMART | SM00181; |
| UniProt Domain [FT] | DOMAIN 1..318; /note="Teneurin N-terminal"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00694"; DOMAIN 528..559; /note="EGF-like 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 560..591; /note="EGF-like 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 592..624; /note="EGF-like 3"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 625..657; /note="EGF-like 4"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 658..691; /note="EGF-like 5"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 692..721; /note="EGF-like 6"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 722..753; /note="EGF-like 7"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076"; DOMAIN 761..796; /note="EGF-like 8"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00076" |
| InterPro | IPR011042;IPR000742;IPR057627;IPR056823;IPR009471;IPR056822;IPR056820;IPR051216;IPR057629;IPR028916;IPR006530; |
| Pfam | PF25024;PF24329;PF23093;PF06484;PF25021;PF25023;PF23538;PF15636;PF25020; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000009694-TENM1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HINT1 | Biogrid | false |
| SORBS1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

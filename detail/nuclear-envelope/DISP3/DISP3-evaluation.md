---
type: protein-evaluation
gene: "DISP3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DISP3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DISP3 / KIAA1337, PTCHD2 |
| 蛋白名称 | Protein dispatched homolog 3 |
| 蛋白大小 | 1392 aa / 153.0 kDa |
| UniProt ID | Q9P2K9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Endoplasmic reticulum membrane; Nucleus membrane; Cytoplasmi |
| 蛋白大小 | 5/10 | ×1 | 5 | 1392 aa / 153.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=70.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR042480, IPR053954, IPR053958, IPR004869, IPR000 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 7 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **125.0/180** | |
| **归一化总分** | | | **69.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Uncertain |
| UniProt | Endoplasmic reticulum membrane; Nucleus membrane; Cytoplasmic vesicle membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytoplasmic vesicle membrane (GO:0030659)
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)
- membrane (GO:0016020)
- nuclear membrane (GO:0031965)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 16 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1337, PTCHD2 |

**关键文献**:
1. Identification and characterization of DISP3 gene in silico.. *International journal of oncology*. PMID: 15645143
2. Conserved Genes in Highly Regenerative Metazoans Are Associated with Planarian Regeneration.. *Genome biology and evolution*. PMID: 38652806
3. DISP3, a sterol-sensing domain-containing protein that links thyroid hormone action and cholesterol metabolism.. *Molecular endocrinology (Baltimore, Md.)*. PMID: 19179482
4. Modulated DISP3/PTCHD2 expression influences neural stem cell fate decisions.. *Scientific reports*. PMID: 28134287
5. DISP3 promotes proliferation and delays differentiation of neural progenitor cells.. *FEBS letters*. PMID: 25281927

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.5 |
| 高置信度残基 (pLDDT>90) 占比 | 10.8% |
| 置信残基 (pLDDT 70-90) 占比 | 54.5% |
| 中等置信 (pLDDT 50-70) 占比 | 13.4% |
| 低置信 (pLDDT<50) 占比 | 21.3% |
| 有序区域 (pLDDT>70) 占比 | 65.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=70.5，有序区 65.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR042480, IPR053954, IPR053958, IPR004869, IPR000731; Pfam: PF22894, PF03176, PF12349 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MYCBP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CA2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| MDFI | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| RASGRP2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| RPS14 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| DDX21 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| MTNR1B | psi-mi:"MI:0112"(ubiquitin reconstruction) | pubmed:26514267|imex:IM-24624 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 7
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 7 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.5 + PDB: 无 | pLDDT=70.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Nucleus membrane;  / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 0 + 7 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DISP3 — Protein dispatched homolog 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1392 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9P2K9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000204624-DISP3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DISP3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P2K9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000204624-DISP3/subcellular

![](https://images.proteinatlas.org/54579/1335_C2_1_red_green.jpg)
![](https://images.proteinatlas.org/54579/1335_C2_2_red_green.jpg)
![](https://images.proteinatlas.org/54579/1352_C2_1_red_green.jpg)
![](https://images.proteinatlas.org/54579/1352_C2_2_red_green.jpg)
![](https://images.proteinatlas.org/54579/1381_D4_1_red_green.jpg)
![](https://images.proteinatlas.org/54579/1381_D4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9P2K9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

---
type: protein-evaluation
gene: "FAM110A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM110A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM110A / C20orf55, F10 |
| 蛋白名称 | Protein FAM110A |
| 蛋白大小 | 295 aa / 31.3 kDa |
| UniProt ID | Q9BQ89 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Vesicles; 额外: Cytosol; UniProt: Cytoplasm; Cytoplasm, cytoskeleton, microtubule organizing c |
| 蛋白大小 | 10/10 | ×1 | 10 | 295 aa / 31.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR025740, IPR025741, IPR025739; Pfam: PF14160, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles; 额外: Cytosol | Uncertain |
| UniProt | Cytoplasm; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Cytoplasm, cytoskelet... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cell cortex (GO:0005938)
- centrosome (GO:0005813)
- cytosol (GO:0005829)
- nucleus (GO:0005634)
- spindle microtubule (GO:0005876)
- spindle pole (GO:0000922)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 14 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C20orf55, F10 |

**关键文献**:
1. Pan-cancer analysis reveals potential of FAM110A as a prognostic and immunological biomarker in human cancer.. *Frontiers in immunology*. PMID: 36923407
2. Characterization of the FAM110 gene family.. *Genomics*. PMID: 17499476
3. CK1-mediated phosphorylation of FAM110A promotes its interaction with mitotic spindle and controls chromosomal alignment.. *EMBO reports*. PMID: 34080749
4. Comprehensive gene- and pathway-based analysis of depressive symptoms in older adults.. *Journal of Alzheimer's disease : JAD*. PMID: 25690665
5. FAM110A promotes mitotic spindle formation by linking microtubules with actin cytoskeleton.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 38995965

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.1 |
| 高置信度残基 (pLDDT>90) 占比 | 2.0% |
| 置信残基 (pLDDT 70-90) 占比 | 27.8% |
| 中等置信 (pLDDT 50-70) 占比 | 40.3% |
| 低置信 (pLDDT<50) 占比 | 29.8% |
| 有序区域 (pLDDT>70) 占比 | 29.8% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM110A/FAM110A-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=61.1），有序残基占 29.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR025740, IPR025741, IPR025739; Pfam: PF14160, PF14161 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CSPP1 | 0.947 | 0.000 | — |
| TM2D2 | 0.510 | 0.000 | — |
| ZMAT4 | 0.489 | 0.000 | — |
| ZDHHC18 | 0.479 | 0.000 | — |
| KCTD3 | 0.479 | 0.072 | — |
| IRS4 | 0.472 | 0.000 | — |
| PLEKHA2 | 0.470 | 0.000 | — |
| GPR101 | 0.460 | 0.000 | — |
| GPANK1 | 0.451 | 0.000 | — |
| SMIM13 | 0.446 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PYGM | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| CSNK1E | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| NCK1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| FYN | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| GRB2 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| ABL1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| KRT31 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| COG6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| LDOC1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 14，IntAct interactions: 15
- 调控相关比例: 0 / 14 = 0%

**评价**: STRING 14 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.1 + PDB: 无 | pLDDT=61.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, cytoskeleton, microtubule or / Nucleoplasm, Vesicles; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 14 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FAM110A — Protein FAM110A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小295 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=61.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BQ89
- Protein Atlas: https://www.proteinatlas.org/ENSG00000125898-FAM110A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM110A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BQ89
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FAM110A/FAM110A-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000125898-FAM110A/subcellular

![](https://images.proteinatlas.org/69240/1324_G9_4_red_green.jpg)
![](https://images.proteinatlas.org/69240/1324_G9_5_red_green.jpg)
![](https://images.proteinatlas.org/69240/1325_G9_1_red_green.jpg)
![](https://images.proteinatlas.org/69240/1325_G9_2_red_green.jpg)
![](https://images.proteinatlas.org/69240/1547_F4_5_red_green.jpg)
![](https://images.proteinatlas.org/69240/1547_F4_6_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

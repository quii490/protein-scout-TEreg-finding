---
type: protein-evaluation
gene: "NCKAP5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NCKAP5 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NCKAP5 / ERIH, NAP5 |
| 蛋白名称 | Nck-associated protein 5 |
| 蛋白大小 | 1909 aa / 208.5 kDa |
| UniProt ID | O14513 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli; 额外: Golgi apparatus, Plasma membrane, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 5/10 | ×1 | 5 | 1909 aa / 208.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=17 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=43.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR032769, IPR026163; Pfam: PF15246 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 4 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.0/180** | |
| **归一化总分** | | | **62.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Golgi apparatus, Plasma membrane, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- microtubule plus-end (GO:0035371)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17 |
| PubMed broad count | 25 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ERIH, NAP5 |

**关键文献**:
1. Single-cell RNA sequencing analysis of vestibular schwannoma reveals functionally distinct macrophage subsets.. *British journal of cancer*. PMID: 38480935
2. Whole-Exome Sequencing Among Chinese Patients With Hereditary Diffuse Gastric Cancer.. *JAMA network open*. PMID: 36484990
3. A susceptibility gene signature for ERBB2-driven mammary tumour development and metastasis in collaborative cross mice.. *EBioMedicine*. PMID: 39067134
4. Immune infiltration patterns and identification of new diagnostic biomarkers GDF10, NCKAP5, and RTKN2 in non-small cell lung cancer.. *Translational oncology*. PMID: 36628881
5. Maternal and Parent-of-Origin Gene-Environment Effects on the Etiology of Orofacial Clefting.. *Genes*. PMID: 40004524

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 43.1 |
| 高置信度残基 (pLDDT>90) 占比 | 8.6% |
| 置信残基 (pLDDT 70-90) 占比 | 3.4% |
| 中等置信 (pLDDT 50-70) 占比 | 6.2% |
| 低置信 (pLDDT<50) 占比 | 81.8% |
| 有序区域 (pLDDT>70) 占比 | 12.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=43.1），有序残基占 12.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR032769, IPR026163; Pfam: PF15246 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NCK1 | 0.785 | 0.194 | — |
| KIF3C | 0.482 | 0.482 | — |
| KIF3B | 0.435 | 0.435 | — |
| OR2T27 | 0.424 | 0.052 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GRB2 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| FYN | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| ABL1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| NCK1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| VAV2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-13772|pubmed:18654987 |
| APC | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:20936779|imex:IM-17049 |
| KHDRBS1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| DISC1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| KIF3C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| KIF3B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 4，IntAct interactions: 15
- 调控相关比例: 0 / 4 = 0%

**评价**: STRING 4 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=43.1 + PDB: 无 | pLDDT=43.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoli; 额外: Golgi apparatus, Plasma membrane, Cy | 一致 |
| PPI | STRING + IntAct | 4 + 15 interactions | 数据充分 |

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
1. NCKAP5 — Nck-associated protein 5，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1909 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 17 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=43.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O14513
- Protein Atlas: https://www.proteinatlas.org/ENSG00000176771-NCKAP5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NCKAP5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O14513
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000176771-NCKAP5/subcellular

![](https://images.proteinatlas.org/44859/780_H3_1_red_green.jpg)
![](https://images.proteinatlas.org/44859/780_H3_2_red_green.jpg)
![](https://images.proteinatlas.org/44859/788_H3_1_red_green.jpg)
![](https://images.proteinatlas.org/44859/788_H3_2_red_green.jpg)
![](https://images.proteinatlas.org/44859/864_H7_1_red_green.jpg)
![](https://images.proteinatlas.org/44859/864_H7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O14513-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

---
type: protein-evaluation
gene: "DENND1C"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DENND1C 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DENND1C / FAM31C |
| 蛋白名称 | DENN domain-containing protein 1C |
| 蛋白大小 | 801 aa / 87.1 kDa |
| UniProt ID | Q8IV53 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nucleoplasm, Centrosome; UniProt: Cytoplasm, cytosol; Cytoplasmic vesicle, clathrin-coated ves |
| 蛋白大小 | 8/10 | ×1 | 8 | 801 aa / 87.1 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001194, IPR005112, IPR043153, IPR040032, IPR037 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.0/180** | |
| **归一化总分** | | | **71.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm, Centrosome | Approved |
| UniProt | Cytoplasm, cytosol; Cytoplasmic vesicle, clathrin-coated vesicle | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- clathrin-coated vesicle (GO:0030136)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 13 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FAM31C |

**关键文献**:
1. Identification of shared pathophysiological molecules of major psychiatric disorders: A comprehensive analysis of serum immune complex antigens before and after electroconvulsive therapy.. *Journal of neuroimmunology*. PMID: 40306147
2. Connecdenn 3/DENND1C binds actin linking Rab35 activation to the actin cytoskeleton.. *Molecular biology of the cell*. PMID: 22072793
3. Biological significance of genome-wide DNA methylation profiles in keloids.. *The Laryngoscope*. PMID: 27312686
4. IL-17A Recruits Rab35 to IL-17R to Mediate PKCα-Dependent Stress Fiber Formation and Airway Smooth Muscle Contractility.. *Journal of immunology (Baltimore, Md. : 1950)*. PMID: 30683702
5. An analysis of DNA methylation in human adipose tissue reveals differential modification of obesity genes before and after gastric bypass and weight loss.. *Genome biology*. PMID: 25651499

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.9 |
| 高置信度残基 (pLDDT>90) 占比 | 38.8% |
| 置信残基 (pLDDT 70-90) 占比 | 6.6% |
| 中等置信 (pLDDT 50-70) 占比 | 6.0% |
| 低置信 (pLDDT<50) 占比 | 48.6% |
| 有序区域 (pLDDT>70) 占比 | 45.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=62.9），有序残基占 45.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001194, IPR005112, IPR043153, IPR040032, IPR037516; Pfam: PF03455, PF02141, PF03456 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RAB35 | 0.978 | 0.526 | — |
| RAB13 | 0.742 | 0.000 | — |
| CLTC | 0.734 | 0.068 | — |
| RAB8A | 0.513 | 0.000 | — |
| RAB8B | 0.512 | 0.000 | — |
| TBC1D10C | 0.504 | 0.000 | — |
| DENND1A | 0.501 | 0.000 | — |
| RASAL3 | 0.499 | 0.000 | — |
| DENND1B | 0.491 | 0.000 | — |
| MADD | 0.486 | 0.109 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| cysJ | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| HSPA8 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| SNAPIN | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| DAPK1 | psi-mi:"MI:0089"(protein array) | pubmed:29513927|doi:10.1002/pm |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.9 + PDB: 无 | pLDDT=62.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol; Cytoplasmic vesicle, clathrin- / Cytosol; 额外: Nucleoplasm, Centrosome | 一致 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

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
1. DENND1C — DENN domain-containing protein 1C，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小801 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=62.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IV53
- Protein Atlas: https://www.proteinatlas.org/ENSG00000205744-DENND1C/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DENND1C
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IV53
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000205744-DENND1C/subcellular

![](https://images.proteinatlas.org/42758/1825_B1_11_cr5afa870716d27_blue_red_green.jpg)
![](https://images.proteinatlas.org/42758/1825_B1_9_cr5ab924ae438f3_blue_red_green.jpg)
![](https://images.proteinatlas.org/42758/563_F5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/42758/563_F5_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/42758/566_F5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/42758/566_F5_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IV53-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

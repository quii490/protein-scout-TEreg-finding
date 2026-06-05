---
type: protein-evaluation
gene: "FNDC3A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FNDC3A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FNDC3A / FNDC3, HUGO, KIAA0970 |
| 蛋白名称 | Fibronectin type-III domain-containing protein 3A |
| 蛋白大小 | 1198 aa / 131.9 kDa |
| UniProt ID | Q9Y2H6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Golgi apparatus, Centrosome; 额外: Cytosol; UniProt: Golgi apparatus membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 1198 aa / 131.9 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=22 篇 (≤40→8) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=77.7; PDB: 1WK0, 1X3D, 1X4X, 1X5X, 2CRM, 2CRZ |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050617, IPR003961, IPR036116, IPR013783; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.0/180** | |
| **归一化总分** | | | **66.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Golgi apparatus, Centrosome; 额外: Cytosol | Approved |
| UniProt | Golgi apparatus membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- acrosomal vesicle (GO:0001669)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- Golgi apparatus (GO:0005794)
- Golgi membrane (GO:0000139)
- membrane (GO:0016020)
- vesicle membrane (GO:0012506)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 22 |
| PubMed broad count | 32 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FNDC3, HUGO, KIAA0970 |

**关键文献**:
1. Silencing of fibronectin type III domain-containing protein 3A (FNDC3A) attenuates epithelial-to-mesenchymal transition (EMT), cancer invasion, and stemness in triple-negative breast cancer (TNBC).. *Biochimica et biophysica acta. Molecular cell research*. PMID: 40120859
2. Exosomal or follicular FNDC3A decreases FOLR1 mRNA abundance and progesterone and lactate synthesis in bovine granulosa cells.. *Reproduction (Cambridge, England)*. PMID: 38513348
3. The fusiform gyrus exhibits differential gene-gene co-expression in Alzheimer's disease.. *Frontiers in aging neuroscience*. PMID: 37255536
4. Microarray expression profiling of fndc3a zebrafish mutants.. *microPublication biology*. PMID: 36254247
5. FAM46C and FNDC3A Are Multiple Myeloma Tumor Suppressors That Act in Concert to Impair Clearing of Protein Aggregates and Autophagy.. *Cancer research*. PMID: 32963011

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.7 |
| 高置信度残基 (pLDDT>90) 占比 | 44.0% |
| 置信残基 (pLDDT 70-90) 占比 | 29.2% |
| 中等置信 (pLDDT 50-70) 占比 | 9.1% |
| 低置信 (pLDDT<50) 占比 | 17.7% |
| 有序区域 (pLDDT>70) 占比 | 73.2% |
| 可用 PDB 条目 | 1WK0, 1X3D, 1X4X, 1X5X, 2CRM, 2CRZ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1WK0, 1X3D, 1X4X, 1X5X, 2CRM, 2CRZ）+ AlphaFold极高置信度预测（pLDDT=77.7），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050617, IPR003961, IPR036116, IPR013783; Pfam: PF00041 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDADC1 | 0.702 | 0.000 | — |
| MLNR | 0.670 | 0.091 | — |
| CAB39L | 0.644 | 0.000 | — |
| RCBTB2 | 0.565 | 0.000 | — |
| LPAR6 | 0.562 | 0.091 | — |
| SETDB2 | 0.552 | 0.000 | — |
| CYSLTR2 | 0.524 | 0.091 | — |
| PHF11 | 0.516 | 0.000 | — |
| FNDC4 | 0.505 | 0.000 | — |
| FNDC3B | 0.492 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000441831.1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| trmD | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| EBI-2851229 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| LAMP1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| PLGRKT | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| CANX | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| THAP7 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| TRIT1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| FPR2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.7 + PDB: 1WK0, 1X3D, 1X4X, 1X5X, 2CRM,  | pLDDT=77.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Golgi apparatus membrane / Nucleoplasm, Golgi apparatus, Centrosome; 额外: Cyto | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FNDC3A — Fibronectin type-III domain-containing protein 3A，非常新颖，仅有少数基础研究。
2. 蛋白大小1198 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 22 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y2H6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000102531-FNDC3A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FNDC3A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y2H6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000102531-FNDC3A/subcellular

![](https://images.proteinatlas.org/12555/1875_C3_1_cr5b7c11e71d251_blue_red_green.jpg)
![](https://images.proteinatlas.org/12555/1875_C3_24_cr5b7c11e71e486_blue_red_green.jpg)
![](https://images.proteinatlas.org/12555/1913_J15_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/12555/1913_J15_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/12555/1936_E5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/12555/1936_E5_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y2H6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

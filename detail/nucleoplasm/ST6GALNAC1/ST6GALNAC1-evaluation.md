---
type: protein-evaluation
gene: "ST6GALNAC1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ST6GALNAC1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ST6GALNAC1 / SIAT7A |
| 蛋白名称 | Alpha-N-acetylgalactosaminide alpha-2,6-sialyltransferase 1 |
| 蛋白大小 | 600 aa / 68.6 kDa |
| UniProt ID | Q9NSC7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Golgi apparatus; 额外: Nucleoplasm; UniProt: Golgi apparatus membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 600 aa / 68.6 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=37 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=72.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001675, IPR038578; Pfam: PF00777 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.5/180** | |
| **归一化总分** | | | **61.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nucleoplasm | Approved |
| UniProt | Golgi apparatus membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Golgi membrane (GO:0000139)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 37 |
| PubMed broad count | 58 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SIAT7A |

**关键文献**:
1. ST6GALNAC1-mediated sialylation in uterine endometrial epithelium facilitates the epithelium-embryo attachment.. *Journal of advanced research*. PMID: 39111624
2. Differential expression of ST6GALNAC1 and ST6GALNAC2 and their clinical relevance to colorectal cancer progression.. *PloS one*. PMID: 39348343
3. The Role of Sialyl-Tn in Cancer.. *International journal of molecular sciences*. PMID: 26927062
4. Analysis of cancer-associated glycosyltransferases reveals novel targets of non-small cell lung cancer pathogenesis.. *Frontiers in oncology*. PMID: 40718829
5. Cross-talk between Colon Cells and Macrophages Increases ST6GALNAC1 and MUC1-sTn Expression in Ulcerative Colitis and Colitis-Associated Colon Cancer.. *Cancer immunology research*. PMID: 31831633

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.4 |
| 高置信度残基 (pLDDT>90) 占比 | 54.0% |
| 置信残基 (pLDDT 70-90) 占比 | 5.8% |
| 中等置信 (pLDDT 50-70) 占比 | 3.0% |
| 低置信 (pLDDT<50) 占比 | 37.2% |
| 有序区域 (pLDDT>70) 占比 | 59.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=72.4，有序区 59.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001675, IPR038578; Pfam: PF00777 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| C1GALT1 | 0.980 | 0.000 | — |
| C1GALT1C1 | 0.973 | 0.000 | — |
| GCNT1 | 0.965 | 0.000 | — |
| B3GNT6 | 0.959 | 0.000 | — |
| GALNT6 | 0.950 | 0.000 | — |
| EEF1A2 | 0.944 | 0.231 | — |
| GALNT4 | 0.942 | 0.000 | — |
| GALNT5 | 0.942 | 0.000 | — |
| GALNT2 | 0.939 | 0.000 | — |
| GALNT1 | 0.938 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Q74YL2 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| EEF1A2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| VAT1L | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 3
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.4 + PDB: 无 | pLDDT=72.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus membrane / Golgi apparatus; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 3 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. ST6GALNAC1 — Alpha-N-acetylgalactosaminide alpha-2,6-sialyltransferase 1，非常新颖，仅有少数基础研究。
2. 蛋白大小600 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 37 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NSC7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000070526-ST6GALNAC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ST6GALNAC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NSC7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (approved)。来源: https://www.proteinatlas.org/ENSG00000070526-ST6GALNAC1/subcellular

![](https://images.proteinatlas.org/14767/1847_E1_4_red_green.jpg)
![](https://images.proteinatlas.org/14767/1847_E1_6_red_green.jpg)
![](https://images.proteinatlas.org/14767/1913_H2_6_red_green.jpg)
![](https://images.proteinatlas.org/14767/1913_H2_7_red_green.jpg)
![](https://images.proteinatlas.org/14767/1993_A1_2_red_green.jpg)
![](https://images.proteinatlas.org/14767/1993_A1_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NSC7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

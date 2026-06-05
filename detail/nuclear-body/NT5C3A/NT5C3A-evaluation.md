---
type: protein-evaluation
gene: "NT5C3A"
date: 2026-06-04
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NT5C3A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NT5C3A / NT5C3, P5N1, UMPH1 |
| 蛋白名称 | Cytosolic 5'-nucleotidase 3A |
| 蛋白大小 | 336 aa / 37.9 kDa |
| UniProt ID | Q9H0P0 |
| 评估日期 | 2026-06-04 |

**功能简介** (UniProt): Nucleotidase which shows specific activity towards cytidine monophosphate (CMP) and 7-methylguanosine monophosphate (m(7)GMP) (PubMed:24603684). CMP seems to be the preferred substrate (PubMed:15968458)

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm; Endoplasmic reticulum |
| 蛋白大小 | 10/10 | ×1 | 10 | 336 aa / 37.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=91.8; PDB: 2CN1, 2JGA, 2VKQ |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR036412, IPR023214, IPR006434; Pfam: PF05822 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.0/180** | |
| **归一化总分** | | | **72.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm; Endoplasmic reticulum | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- endoplasmic reticulum (GO:0005783)
- mitochondrion (GO:0005739)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 38 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NT5C3, P5N1, UMPH1 |

**关键文献**:
1. The plasma peptides of Alzheimer's disease.. *Clinical proteomics*. PMID: 34182925
2. Proximity extension assay-based discovery of biomarkers for disease activity in chronic inflammatory demyelinating polyneuropathy.. *Journal of neurology, neurosurgery, and psychiatry*. PMID: 37879899
3. Identification and Validation of Nicotinamide Metabolism-Related Gene Signatures as a Novel Prognostic Model for Hepatocellular Carcinoma.. *OncoTargets and therapy*. PMID: 38827823
4. The intracellular pyrimidine 5'-nucleotidase NT5C3A is a negative epigenetic factor in interferon and cytokine signaling.. *Science signaling*. PMID: 29463777
5. DIA-based quantitative proteomic analysis on the meat quality of porcine Longissimus thoracis et lumborum cooked by different procedures.. *Food chemistry*. PMID: 34619635

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.8 |
| 高置信度残基 (pLDDT>90) 占比 | 83.3% |
| 置信残基 (pLDDT 70-90) 占比 | 6.5% |
| 中等置信 (pLDDT 50-70) 占比 | 8.0% |
| 低置信 (pLDDT<50) 占比 | 2.1% |
| 有序区域 (pLDDT>70) 占比 | 89.8% |
| 可用 PDB 条目 | 2CN1, 2JGA, 2VKQ |

**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2CN1, 2JGA, 2VKQ）+ AlphaFold高质量预测（pLDDT=91.8），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036412, IPR023214, IPR006434; Pfam: PF05822 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NT5C | 0.995 | 0.000 | — |
| NT5M | 0.976 | 0.000 | — |
| NT5C2 | 0.961 | 0.000 | — |
| NT5C1A | 0.957 | 0.000 | — |
| DCK | 0.947 | 0.000 | — |
| NT5C1B | 0.947 | 0.000 | — |
| NT5C1B-RDH14 | 0.943 | 0.000 | — |
| CMPK2 | 0.939 | 0.000 | — |
| CDA | 0.933 | 0.000 | — |
| ENPP3 | 0.933 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%，尚无实验验证互作。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.8 + PDB: 2CN1, 2JGA, 2VKQ | pLDDT=91.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Endoplasmic reticulum / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. NT5C3A — Cytosolic 5'-nucleotidase 3A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小336 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H0P0
- Protein Atlas: https://www.proteinatlas.org/search/NT5C3A
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NT5C3A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H0P0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live via harvest pipeline; evaluated 2026-06-04

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Endoplasmic reticulum (supported)。来源: https://www.proteinatlas.org/ENSG00000122643-NT5C3A/subcellular

![](https://images.proteinatlas.org/10520/2013_A7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/10520/2013_A7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/10520/2030_G1_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/10520/2030_G1_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/10520/2051_D1_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/10520/2051_D1_4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

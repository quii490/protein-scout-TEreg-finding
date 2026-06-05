---
type: protein-evaluation
gene: "DOP1A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DOP1A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DOP1A / DOPEY1, KIAA1117 |
| 蛋白名称 | Protein DOP1A |
| 蛋白大小 | 2465 aa / 277.4 kDa |
| UniProt ID | Q5JWR5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: Golgi apparatus membrane |
| 蛋白大小 | 2/10 | ×1 | 2 | 2465 aa / 277.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR040314, IPR056457, IPR007249, IPR056459, IPR056 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **110.0/180** | |
| **归一化总分** | | | **61.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Approved |
| UniProt | Golgi apparatus membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- endosome (GO:0005768)
- Golgi membrane (GO:0000139)
- Golgi-associated vesicle (GO:0005798)
- trans-Golgi network (GO:0005802)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 10 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DOPEY1, KIAA1117 |

**关键文献**:
1. Impaired maturation and differentiation of oligodendrocytes in the vacuole formation myelin mutant rat.. *Veterinary pathology*. PMID: 41067867
2. Genomic analyses of claw disorders in Holstein cows: Genetic parameters, trait associations, and genome-wide associations considering interactions of SNP and heat stress.. *Journal of dairy science*. PMID: 36028345
3. Whole exome sequencing identified a homozygous novel variant in DOP1A gene in the Pakistan family with neurodevelopmental disabilities: case report and literature review.. *Frontiers in genetics*. PMID: 38818041
4. Removal of developmentally regulated microexons has a minimal impact on larval zebrafish brain morphology and function.. *eLife*. PMID: 41252186

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.9 |
| 高置信度残基 (pLDDT>90) 占比 | 14.9% |
| 置信残基 (pLDDT 70-90) 占比 | 45.0% |
| 中等置信 (pLDDT 50-70) 占比 | 10.0% |
| 低置信 (pLDDT<50) 占比 | 30.1% |
| 有序区域 (pLDDT>70) 占比 | 59.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=66.9），有序残基占 59.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR040314, IPR056457, IPR007249, IPR056459, IPR056458; Pfam: PF24598, PF04118, PF24601 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MON2 | 0.981 | 0.840 | — |
| NEO1 | 0.595 | 0.000 | — |
| ATP9B | 0.578 | 0.093 | — |
| ATP9A | 0.564 | 0.093 | — |
| WASHC4 | 0.455 | 0.000 | — |
| SNX3 | 0.452 | 0.000 | — |
| SLC66A2 | 0.447 | 0.291 | — |
| EFHD2 | 0.429 | 0.000 | — |
| KIAA0355 | 0.416 | 0.000 | — |
| CZIB | 0.409 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ACTC1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| VAPB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NPTN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| GPR17 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TACSTD2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| YWHAG | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:36931259|imex:IM-29717 |
| YWHAQ | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:36931259|imex:IM-29717 |
| YWHAH | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:36931259|imex:IM-29717 |
| SFN | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:36931259|imex:IM-29717 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 9
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.9 + PDB: 无 | pLDDT=66.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus membrane / Nucleoplasm; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 9 interactions | 数据充分 |

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
1. DOP1A — Protein DOP1A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小2465 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=66.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5JWR5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000083097-DOP1A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DOP1A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5JWR5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000083097-DOP1A/subcellular

![](https://images.proteinatlas.org/27902/301_E3_1_red_green.jpg)
![](https://images.proteinatlas.org/27902/301_E3_2_red_green.jpg)
![](https://images.proteinatlas.org/27902/303_E3_3_red_green.jpg)
![](https://images.proteinatlas.org/27902/303_E3_4_red_green.jpg)
![](https://images.proteinatlas.org/27902/342_E3_1_red_green.jpg)
![](https://images.proteinatlas.org/27902/342_E3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q5JWR5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

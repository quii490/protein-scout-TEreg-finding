---
type: protein-evaluation
gene: "SZT2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SZT2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SZT2 / C1orf84, KIAA0467 |
| 蛋白名称 | KICSTOR complex protein SZT2 |
| 蛋白大小 | 3432 aa / 378.0 kDa |
| UniProt ID | Q5T011 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Vesicles, Actin filaments; UniProt: Lysosome membrane; Peroxisome |
| 蛋白大小 | 0/10 | ×1 | 0 | 3432 aa / 378.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=37 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=83.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR033228 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **101.5/180** | |
| **归一化总分** | | | **56.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles, Actin filaments | Approved |
| UniProt | Lysosome membrane; Peroxisome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- KICSTOR complex (GO:0140007)
- lysosomal membrane (GO:0005765)
- peroxisome (GO:0005777)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 37 |
| PubMed broad count | 54 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C1orf84, KIAA0467 |

**关键文献**:
1. Clinical phenotype and genetic characteristics of SZT2 related diseases: A case report and literature review.. *Seizure*. PMID: 38134649
2. KICSTOR recruits GATOR1 to the lysosome and is necessary for nutrients to regulate mTORC1.. *Nature*. PMID: 28199306
3. Architecture of the human KICSTOR and GATOR1-KICSTOR complexes.. *Nature structural & molecular biology*. PMID: 41198956
4. SZT2 variants associated with partial epilepsy or epileptic encephalopathy and the genotype-phenotype correlation.. *Frontiers in molecular neuroscience*. PMID: 37213690
5. Structure of the lysosomal KICSTOR-GATOR1-SAMTOR nutrient-sensing supercomplex.. *Cell*. PMID: 41512879

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.1 |
| 高置信度残基 (pLDDT>90) 占比 | 48.9% |
| 置信残基 (pLDDT 70-90) 占比 | 33.7% |
| 中等置信 (pLDDT 50-70) 占比 | 6.7% |
| 低置信 (pLDDT<50) 占比 | 10.7% |
| 有序区域 (pLDDT>70) 占比 | 82.6% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=83.1，有序区 82.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR033228 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ITFG2 | 0.999 | 0.994 | — |
| KPTN | 0.999 | 0.994 | — |
| C12orf66 | 0.999 | 0.994 | — |
| DEPDC5 | 0.999 | 0.994 | — |
| WDR59 | 0.998 | 0.994 | — |
| NPRL2 | 0.998 | 0.994 | — |
| NPRL3 | 0.998 | 0.994 | — |
| WDR24 | 0.998 | 0.994 | — |
| LAMP1 | 0.994 | 0.994 | — |
| BMT2 | 0.968 | 0.779 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DEPDC5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TEPSIN | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ZNF655 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ITFG2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DOCK5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SAMTOR | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KPTN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| C1QTNF2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Sesn2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| CRX | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.1 + PDB: 无 | pLDDT=83.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Lysosome membrane; Peroxisome / Nucleoplasm, Vesicles, Actin filaments | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. SZT2 — KICSTOR complex protein SZT2，非常新颖，仅有少数基础研究。
2. 蛋白大小3432 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 37 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5T011
- Protein Atlas: https://www.proteinatlas.org/ENSG00000198198-SZT2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SZT2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5T011
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000198198-SZT2/subcellular

![](https://images.proteinatlas.org/29012/301_F1_3_red_green.jpg)
![](https://images.proteinatlas.org/29012/301_F1_5_red_green.jpg)
![](https://images.proteinatlas.org/29012/303_F1_3_red_green.jpg)
![](https://images.proteinatlas.org/29012/303_F1_5_red_green.jpg)
![](https://images.proteinatlas.org/29012/342_F1_1_red_green.jpg)
![](https://images.proteinatlas.org/29012/342_F1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

---
type: protein-evaluation
gene: "NCAPG2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NCAPG2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NCAPG2 / LUZP5 |
| 蛋白名称 | Condensin-2 complex subunit G2 |
| 蛋白大小 | 1143 aa / 131.0 kDa |
| UniProt ID | Q86XI2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nuclear speckles; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 1143 aa / 131.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=40 篇 (≤40→8) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v6 pLDDT=0; PDB: 9F5W |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011989, IPR016024, IPR024741; Pfam: PF12422 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **112.0/180** | |
| **归一化总分** | | | **62.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear speckles | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- condensed nuclear chromosome (GO:0000794)
- condensin complex (GO:0000796)
- membrane (GO:0016020)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 40 |
| PubMed broad count | 53 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: LUZP5 |

**关键文献**:
1. Condensin dysfunction is a reproductive isolating barrier in mice.. *Nature*. PMID: 37914934
2. MYC and NCAPG2 as molecular targets of colorectal cancer and gastric cancer in nursing.. *Medicine*. PMID: 38701261
3. Predictive gene expression signature diagnoses neonatal sepsis before clinical presentation.. *EBioMedicine*. PMID: 39472236
4. Circular RNA circ0001955 promotes cervical cancer tumorigenesis and metastasis via the miR-188-3p/NCAPG2 axis.. *Journal of translational medicine*. PMID: 37248471
5. Identification of a circRNA/miRNA/mRNA ceRNA Network as a Cell Cycle-Related Regulator for Chronic Sinusitis with Nasal Polyps.. *Journal of inflammation research*. PMID: 35494315

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 9F5W |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR024741; Pfam: PF12422 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NCAPD3 | 0.999 | 0.859 | — |
| NCAPH2 | 0.999 | 0.899 | — |
| SMC4 | 0.999 | 0.188 | — |
| SMC2 | 0.994 | 0.795 | — |
| NCAPD2 | 0.988 | 0.098 | — |
| NCAPH | 0.979 | 0.098 | — |
| NCAPG | 0.947 | 0.000 | — |
| PLK1 | 0.919 | 0.301 | — |
| PHF8 | 0.906 | 0.000 | — |
| SHCBP1 | 0.854 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PHLDA3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MYC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| NEK6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TANK | psi-mi:"MI:2289"(virotrap) | pubmed:30561431|imex:IM-26500 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| CCP110 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| RAF1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| EPHA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28169297|imex:IM-25584 |
| PB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28169297|imex:IM-25584 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 2 / 15 = 13%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 13%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 9F5W | pLDDT=0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. NCAPG2 — Condensin-2 complex subunit G2，非常新颖，仅有少数基础研究。
2. 蛋白大小1143 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 40 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86XI2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000146918-NCAPG2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NCAPG2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86XI2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000146918-NCAPG2/subcellular

![](https://images.proteinatlas.org/26631/212_B5_1_red_green.jpg)
![](https://images.proteinatlas.org/26631/212_B5_2_red_green.jpg)
![](https://images.proteinatlas.org/26631/213_B5_1_red_green.jpg)
![](https://images.proteinatlas.org/26631/213_B5_2_red_green.jpg)
![](https://images.proteinatlas.org/26631/214_B5_1_red_green.jpg)
![](https://images.proteinatlas.org/26631/214_B5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86XI2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

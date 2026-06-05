---
type: protein-evaluation
gene: "TBC1D1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TBC1D1 — REJECTED (研究热度过高 (PubMed strict=153，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TBC1D1 / KIAA1108 |
| 蛋白名称 | TBC1 domain family member 1 |
| 蛋白大小 | 1168 aa / 133.1 kDa |
| UniProt ID | Q86TI0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 1168 aa / 133.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=153 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=70.6; PDB: 3QYE |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR021785, IPR011993, IPR006020, IPR000195, IPR035 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **85.0/180** | |
| **归一化总分** | | | **47.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Golgi apparatus (GO:0005794)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 153 |
| PubMed broad count | 235 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1108 |

**关键文献**:
1. Novel prognostic biomarker TBC1D1 is associated with immunotherapy resistance in gliomas.. *Frontiers in immunology*. PMID: 38529286
2. Roles of TBC1D1 and TBC1D4 in insulin- and exercise-stimulated glucose transport of skeletal muscle.. *Diabetologia*. PMID: 25280670
3. The TBC1D1 gene: structure, function, and association with obesity and related traits.. *Vitamins and hormones*. PMID: 23374713
4. TBC1D1 functions as a negative regulator of satellite cells for muscle regeneration.. *Nature communications*. PMID: 41253787
5. Tbc1d1 deletion suppresses obesity in leptin-deficient mice.. *International journal of obesity (2005)*. PMID: 27089993

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.6 |
| 高置信度残基 (pLDDT>90) 占比 | 34.9% |
| 置信残基 (pLDDT 70-90) 占比 | 26.0% |
| 中等置信 (pLDDT 50-70) 占比 | 7.4% |
| 低置信 (pLDDT<50) 占比 | 31.7% |
| 有序区域 (pLDDT>70) 占比 | 60.9% |
| 可用 PDB 条目 | 3QYE |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=70.6，有序区 60.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR021785, IPR011993, IPR006020, IPR000195, IPR035969; Pfam: PF11830, PF00640, PF00566 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RAB10 | 0.961 | 0.057 | — |
| RAB8A | 0.955 | 0.057 | — |
| PRKAB1 | 0.938 | 0.000 | — |
| PRKAG3 | 0.937 | 0.000 | — |
| PRKAB2 | 0.935 | 0.000 | — |
| RAB14 | 0.933 | 0.091 | — |
| PRKAG1 | 0.932 | 0.000 | — |
| PRKAG2 | 0.927 | 0.000 | — |
| PRKAA1 | 0.923 | 0.000 | — |
| RAB2A | 0.923 | 0.067 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| YWHAG | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| EBI-1257113 | psi-mi:"MI:0096"(pull down) | imex:IM-15829|pubmed:23416715 |
| YWHAH | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11897|pubmed:17979178 |
| UBE2E2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-11696|pubmed:19549727 |
| ROR1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-18118|pubmed:23153538 |
| HSPB1 | psi-mi:"MI:0097"(reverse ras recruitment system) | imex:IM-20864|pubmed:25277244 |
| YWHAZ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAQ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PDGFRB | psi-mi:"MI:0096"(pull down) | doi:10.1016/j.cell.2019.09.008 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.6 + PDB: 3QYE | pLDDT=70.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. TBC1D1 — TBC1 domain family member 1，研究基础较多，新颖性有限。
2. 蛋白大小1168 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 153 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 153 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86TI0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000065882-TBC1D1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TBC1D1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86TI0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (supported)。来源: https://www.proteinatlas.org/ENSG00000065882-TBC1D1/subcellular

![](https://images.proteinatlas.org/58158/1112_B8_1_red_green.jpg)
![](https://images.proteinatlas.org/58158/1112_B8_2_red_green.jpg)
![](https://images.proteinatlas.org/58158/1446_E8_1_red_green.jpg)
![](https://images.proteinatlas.org/58158/1446_E8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86TI0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

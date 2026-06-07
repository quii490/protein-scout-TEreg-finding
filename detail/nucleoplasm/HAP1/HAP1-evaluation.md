---
type: protein-evaluation
gene: "HAP1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## HAP1 — REJECTED (研究热度过高 (PubMed strict=751，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HAP1 / HAP2, HLP1 |
| 蛋白名称 | Huntingtin-associated protein 1 |
| 蛋白大小 | 671 aa / 75.5 kDa |
| UniProt ID | P54257 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nucleoli; UniProt: Cytoplasm; Cell projection, axon; Presynapse; Cytoplasm, cyt |
| 蛋白大小 | 10/10 | ×1 | 10 | 671 aa / 75.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=751 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR006933, IPR051946; Pfam: PF04849 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoli | Supported |
| UniProt | Cytoplasm; Cell projection, axon; Presynapse; Cytoplasm, cytoskeleton; Cell projection, dendritic sp... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629)
- autophagosome (GO:0005776)
- axon cytoplasm (GO:1904115)
- centriole (GO:0005814)
- centrosome (GO:0005813)
- cytoplasmic vesicle (GO:0031410)
- cytoskeleton (GO:0005856)
- cytosol (GO:0005829)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 751 |
| PubMed broad count | 1025 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HAP2, HLP1 |

**关键文献**:
1. Defining mitochondrial protein functions through deep multiomic profiling.. *Nature*. PMID: 35614220
2. The OsbZIP35-COR1-OsTCP19 module modulates cell proliferation to regulate grain length and weight in rice.. *Science advances*. PMID: 40929276
3. Variations in OsSPL10 confer drought tolerance by directly regulating OsNAC2 expression and ROS production in rice.. *Journal of integrative plant biology*. PMID: 36401566
4. The Huntingtin Transport Complex.. *Biochemistry*. PMID: 39909923
5. HAP1, a new revolutionary cell model for gene editing using CRISPR-Cas9.. *Frontiers in cell and developmental biology*. PMID: 36936678

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.2 |
| 高置信度残基 (pLDDT>90) 占比 | 25.9% |
| 置信残基 (pLDDT 70-90) 占比 | 18.9% |
| 中等置信 (pLDDT 50-70) 占比 | 11.8% |
| 低置信 (pLDDT<50) 占比 | 43.4% |
| 有序区域 (pLDDT>70) 占比 | 44.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=63.2），有序残基占 44.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006933, IPR051946; Pfam: PF04849 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HTT | 0.999 | 0.822 | — |
| DCTN1 | 0.997 | 0.518 | — |
| NFYC | 0.943 | 0.000 | — |
| GABRD | 0.939 | 0.045 | — |
| GABRB1 | 0.938 | 0.086 | — |
| GABRB2 | 0.935 | 0.086 | — |
| GABRA1 | 0.935 | 0.000 | — |
| REPIN1 | 0.934 | 0.000 | — |
| AHI1 | 0.926 | 0.345 | — |
| GABRE | 0.920 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-994554 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-14428|pubmed:16339760 |
| BARD1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15383276|mint:MINT-5217 |
| LRIF1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15383276|mint:MINT-5217 |
| CEP126 | psi-mi:"MI:0018"(two hybrid) | pubmed:15383276|mint:MINT-5217 |
| ZNF33B | psi-mi:"MI:0018"(two hybrid) | pubmed:15383276|mint:MINT-5217 |
| ELP2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| ELP3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| IKI1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| ATP5MF | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| CDK5RAP2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.2 + PDB: 无 | pLDDT=63.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Cell projection, axon; Presynapse; Cyto / Cytosol; 额外: Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. HAP1 — Huntingtin-associated protein 1，研究基础较多，新颖性有限。
2. 蛋白大小671 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 751 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=63.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 751 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P54257
- Protein Atlas: https://www.proteinatlas.org/ENSG00000173805-HAP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HAP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P54257
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000173805-HAP1/subcellular

![](https://images.proteinatlas.org/23394/1779_A4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23394/1779_A4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/23394/181_H7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23394/181_H7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/23394/182_H7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/23394/182_H7_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P54257-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P27695 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR004808;IPR020847;IPR020848;IPR036691;IPR005135; |
| Pfam | PF03372; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000173805-HAP1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| C8orf33 | Intact, Biogrid | true |
| HGS | Intact, Biogrid | true |
| HMOX2 | Intact, Biogrid | true |
| RPS10 | Intact, Biogrid | true |
| TAF1D | Intact, Biogrid | true |
| AHI1 | Intact | false |
| ATXN3 | Biogrid | false |
| BARD1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

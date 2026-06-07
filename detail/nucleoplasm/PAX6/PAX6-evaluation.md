---
type: protein-evaluation
gene: "PAX6"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PAX6 — REJECTED (研究热度过高 (PubMed strict=2566，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PAX6 / AN2 |
| 蛋白名称 | Paired box protein Pax-6 |
| 蛋白大小 | 422 aa / 46.7 kDa |
| UniProt ID | P26367 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Nucleus; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 422 aa / 46.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=2566 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.4; PDB: 2CUE, 6PAX |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001356, IPR017970, IPR009057, IPR043182, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.5/180** | |
| **归一化总分** | | | **44.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus; Nucleus; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2566 |
| PubMed broad count | 4360 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: AN2 |

**关键文献**:
1. PAX6 mutations reviewed.. *Human mutation*. PMID: 9482572
2. PAX6 mutations: genotype-phenotype correlations.. *BMC genetics*. PMID: 15918896
3. PAX6 Alternative Splicing and Corneal Development.. *Stem cells and development*. PMID: 29343211
4. Functional properties of natural human PAX6 and PAX6(5a) mutants.. *Investigative ophthalmology & visual science*. PMID: 14744876
5. Correlation of novel PAX6 gene abnormalities in aniridia and clinical presentation.. *Canadian journal of ophthalmology. Journal canadien d'ophtalmologie*. PMID: 29217025

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.4 |
| 高置信度残基 (pLDDT>90) 占比 | 39.3% |
| 置信残基 (pLDDT 70-90) 占比 | 6.4% |
| 中等置信 (pLDDT 50-70) 占比 | 15.9% |
| 低置信 (pLDDT<50) 占比 | 38.4% |
| 有序区域 (pLDDT>70) 占比 | 45.7% |
| 可用 PDB 条目 | 2CUE, 6PAX |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=68.4），有序残基占 45.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR017970, IPR009057, IPR043182, IPR001523; Pfam: PF00046, PF00292 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DCAF7 | 0.993 | 0.000 | — |
| SOX2 | 0.977 | 0.309 | — |
| BANF1 | 0.952 | 0.000 | — |
| SIX3 | 0.951 | 0.292 | — |
| TBR1 | 0.915 | 0.071 | — |
| MITF | 0.911 | 0.295 | — |
| NEUROG2 | 0.908 | 0.045 | — |
| INS | 0.906 | 0.000 | — |
| MAF | 0.900 | 0.095 | — |
| SOX1 | 0.899 | 0.065 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| IPO13 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ey | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| Rala | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| NKIRAS2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| Antp | psi-mi:"MI:0045"(experimental interaction detectio | pubmed:unassigned4 |
| Dynll1 | psi-mi:"MI:0018"(two hybrid) | pubmed:16098226|imex:IM-18993 |
| HOMER3 | psi-mi:"MI:0018"(two hybrid) | pubmed:16098226|imex:IM-18993 |
| TRIM11 | psi-mi:"MI:0018"(two hybrid) | pubmed:16098226|imex:IM-18993 |
| Dmel\CG17450 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| 4E-T | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.4 + PDB: 2CUE, 6PAX | pLDDT=68.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus; Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. PAX6 — Paired box protein Pax-6，研究基础较多，新颖性有限。
2. 蛋白大小422 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2566 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=68.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 2566 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P26367
- Protein Atlas: https://www.proteinatlas.org/ENSG00000007372-PAX6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PAX6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P26367
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000007372-PAX6/subcellular

![](https://images.proteinatlas.org/30775/1182_F2_2_red_green.jpg)
![](https://images.proteinatlas.org/30775/1182_F2_3_red_green.jpg)
![](https://images.proteinatlas.org/30775/371_A12_1_red_green.jpg)
![](https://images.proteinatlas.org/30775/371_A12_2_red_green.jpg)
![](https://images.proteinatlas.org/30775/372_A12_1_red_green.jpg)
![](https://images.proteinatlas.org/30775/372_A12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P26367-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P26367 |
| SMART | SM00389;SM00351; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001356;IPR017970;IPR009057;IPR043182;IPR001523;IPR043565;IPR036388; |
| Pfam | PF00046;PF00292; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000007372-PAX6/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ACOT12 | Intact | false |
| AP1M1 | Intact | false |
| APP | Intact | false |
| AR | Biogrid | false |
| ARIH2 | Intact | false |
| ATP6V0D2 | Intact | false |
| BCL2L15 | Intact | false |
| C1orf109 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

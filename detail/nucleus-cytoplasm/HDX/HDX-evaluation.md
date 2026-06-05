---
type: protein-evaluation
gene: "HDX"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## HDX — REJECTED (研究热度过高 (PubMed strict=1060，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HDX / CXorf43 |
| 蛋白名称 | Highly divergent homeobox |
| 蛋白大小 | 690 aa / 77.2 kDa |
| UniProt ID | Q7Z353 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 690 aa / 77.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1060 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.5; PDB: 2DA4 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001356, IPR009057, IPR050255 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 4 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.5/180** | |
| **归一化总分** | | | **44.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1060 |
| PubMed broad count | 1715 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CXorf43 |

**关键文献**:
1. Fundamentals of HDX-MS.. *Essays in biochemistry*. PMID: 36251047
2. Enhancement of Protein-Protein Interactions by Destabilizing Mutations Revealed by HDX-MS.. *Biomolecules*. PMID: 40867645
3. HDX-MS in micelles and membranes for small molecule and biopharmaceutical development.. *Current opinion in structural biology*. PMID: 40482399
4. Developments in rapid hydrogen-deuterium exchange methods.. *Essays in biochemistry*. PMID: 36636941
5. HDX-MS: An Analytical Tool to Capture Protein Motion in Action.. *Biomedicines*. PMID: 32709043

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.5 |
| 高置信度残基 (pLDDT>90) 占比 | 20.9% |
| 置信残基 (pLDDT 70-90) 占比 | 8.4% |
| 中等置信 (pLDDT 50-70) 占比 | 10.3% |
| 低置信 (pLDDT<50) 占比 | 60.4% |
| 有序区域 (pLDDT>70) 占比 | 29.3% |
| 可用 PDB 条目 | 2DA4 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=55.5），有序残基占 29.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR009057, IPR050255 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SMIM1 | 0.572 | 0.000 | — |
| RINT1 | 0.556 | 0.479 | — |
| HOMEZ | 0.417 | 0.075 | — |
| STX18 | 0.403 | 0.292 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| POLR1E | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| Arhgap18 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| Arhgap33 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| BOLA1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| BOLA2-SMG1P6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TTC5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TSGA10 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MID2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| FHL5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| POLR1C | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 4，IntAct interactions: 15
- 调控相关比例: 0 / 4 = 0%

**评价**: STRING 4 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.5 + PDB: 2DA4 | pLDDT=55.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Cytosol | 一致 |
| PPI | STRING + IntAct | 4 + 15 interactions | 数据充分 |

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
1. HDX — Highly divergent homeobox，研究基础较多，新颖性有限。
2. 蛋白大小690 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1060 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=55.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1060 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z353
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165259-HDX/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HDX
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7Z353
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000165259-HDX/subcellular

![](https://images.proteinatlas.org/47189/616_H7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/47189/616_H7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/47189/619_H7_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/47189/619_H7_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/47189/622_H7_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/47189/622_H7_4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q7Z353-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

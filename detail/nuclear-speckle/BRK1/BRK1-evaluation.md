---
type: protein-evaluation
gene: "BRK1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BRK1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BRK1 / C3orf10 |
| 蛋白名称 | Protein BRICK1 |
| 蛋白大小 | 75 aa / 8.7 kDa |
| UniProt ID | Q8WUW1 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 03:45:32 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | x4 | 36 | HPA: Nuclear speckles; UniProt: Cytop... |
| 蛋白大小 | 4/10 | x1 | 4 | 75 aa / 8.7 kDa |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed strict=43 篇 (41-60->6) |
| 三维结构 | 10/10 | x3 | 30 | AlphaFold v6 pLDDT=93.7; PDB: 3P8C, 4N78, ... |
| 调控结构域 | 3/10 | x2 | 6 | InterPro: 1; Pfam: 0; IPR033378 |
| PPI 网络 | 6/10 | x3 | 18 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 2.0 | PDB + AlphaFold 双源验证: +0.5; 多库定位一致 (3源): +0.5; 结构域 + AlphaFold 质量: +0.5; PDB 多条目覆盖: +0.5 |
| **原始总分** | | | **126.0/180** | |
| **归一化总分 (/1.83)** | | | **68.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles; 额外: Nuclear speckles, Cell Junctions | Approved |
| UniProt | Cytoplasm, cytoskeleton | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- cytoskeleton (GO:0005856)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- lamellipodium (GO:0030027)
- SCAR complex (GO:0031209)

**结论**: 核定位证据充分，多个数据源一致支持核定位，定位特异性高。

#### 3.2 蛋白大小评估

**评价**: 75 aa，蛋白较小，但仍在可操作范围。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 43 |
| PubMed broad count | 66 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C3orf10 |

**关键文献**:
1. Systems Analysis Implicates WAVE2 Complex in the Pathogenesis of Developmental Left-Sided Obstructive Heart Defects.. *JACC. Basic to translational science*. PMID: 32368696
2. Plug-in strategy for resistance engineering inspired by potato NLRome.. *Nature*. PMID: 41162714
3. Proteogenomic network analysis reveals dysregulated mechanisms and potential mediators in Parkinson's disease.. *Nature communications*. PMID: 39080267
4. Extracellular BRICK1 drives heart repair after myocardial infarction in mice.. *Science translational medicine*. PMID: 41499524
5. Alzheimer's Disease polygenic risk, the plasma proteome, and dementia incidence among UK older adults.. *GeroScience*. PMID: 39586964

**评价**: 中等新颖性，有一定研究基础但仍有探索空间（PubMed 41-60篇）。新颖性评分 6/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.7 |
| 高置信度残基 (pLDDT>90) 占比 | 85.3% |
| 置信残基 (pLDDT 70-90) 占比 | 6.7% |
| 中等置信 (pLDDT 50-70) 占比 | 6.7% |
| 低置信 (pLDDT<50) 占比 | 1.3% |
| 有序区域 (pLDDT>70) 占比 | 92.0% |
| 可用 PDB 条目 | 3P8C, 4N78, 7USC, 7USD, 7USE |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构 + AlphaFold高质量预测（pLDDT=93.7），结构可信度高。三维结构评分 10/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR033378; Pfam: 无 |

**染色质调控潜力分析**: 存在 1 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作**: 暂无数据或查询失败。

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Q9ZQ49 | pull down | pubmed:21798944|imex:IM-16043 |
| Wasf2 | two hybrid | pubmed:15102471 |
| EBI-4444334 | two hybrid array | pubmed:21798944|imex:IM-16043 |
| HUB1 | two hybrid array | pubmed:21798944|imex:IM-16043 |
| ICR5 | two hybrid array | pubmed:21798944|imex:IM-16043 |
| ARP3 | two hybrid | pubmed:17267444|imex:IM-19126 |
| ARPC3 | two hybrid | pubmed:17267444|imex:IM-19126 |
| ABIL1 | two hybrid | pubmed:17267444|imex:IM-19126 |
| ABIL2 | two hybrid | pubmed:17267444|imex:IM-19126 |
| ABIL3 | two hybrid | pubmed:17267444|imex:IM-19126 |

**PPI 互证分析**:
- 仅 IntAct 有数据 (15 interactions)

**评价**: 互作网络中等：STRING 0 预测 + IntAct 15 实验互作。PPI 评分 6/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.7 + PDB: 3P8C, 4N78, 7USC | pLDDT=93.7, v6 | 预测+实验 |
| 定位 | HPA | Nuclear speckles | 单一来源 |
| PPI | IntAct | 15 interactions | 单一来源 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0.5
**总分**: +2.0 / max +3

### 4. 总体评价

**归一化总分**: 68.9/100

**核心优势**:
1. AlphaFold高质量预测（pLDDT=93.7），结构可信度高。
2. 已有PDB实验结构：3P8C, 4N78, 7USC。
3. 存在 1 个已知结构域，有明确的结构-功能切入点。
4. 核定位信号明确，多个数据源一致支持。

**风险/不确定性**:
1. 蛋白过小（75 aa），实验操作受限

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q8WUW1
- Protein Atlas: https://www.proteinatlas.org/search/BRK1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BRK1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WUW1
- STRING: https://string-db.org/network/9606.BRK1
- Packet data timestamp: 2026-06-03 03:45:32

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000254999-BRK1/subcellular

![](https://images.proteinatlas.org/60391/1018_E12_1_red_green.jpg)
![](https://images.proteinatlas.org/60391/1018_E12_2_red_green.jpg)
![](https://images.proteinatlas.org/60391/1226_C3_1_red_green.jpg)
![](https://images.proteinatlas.org/60391/1226_C3_2_red_green.jpg)
![](https://images.proteinatlas.org/60391/1579_E1_1_red_green.jpg)
![](https://images.proteinatlas.org/60391/1579_E1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8WUW1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8WUW1 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR033378; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000254999-BRK1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ACTG1 | Biogrid, Opencell | true |
| BAIAP2 | Biogrid, Opencell | true |
| DTNBP1 | Intact, Biogrid | true |
| HSBP1 | Intact, Biogrid | true |
| NCKAP1 | Biogrid, Opencell | true |
| NDEL1 | Intact, Biogrid | true |
| WASF1 | Biogrid, Opencell | true |
| WASF2 | Biogrid, Opencell | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

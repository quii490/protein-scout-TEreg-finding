---
type: protein-evaluation
gene: "RITA1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RITA1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RITA1 / C12orf52, RITA |
| 蛋白名称 | RBPJ-interacting and tubulin-associated protein 1 |
| 蛋白大小 | 269 aa / 28.6 kDa |
| UniProt ID | Q96K30 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Golgi apparatus, Primary cilium, Primary ci; UniProt: Cytoplasm; Nucleus; Cytoplasm, cytoskeleton, microtubule org |
| 蛋白大小 | 10/10 | ×1 | 10 | 269 aa / 28.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.3; PDB: 5EG6 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR031418; Pfam: PF17066 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 13 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.5/180** | |
| **归一化总分** | | | **72.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Golgi apparatus, Primary cilium, Primary cilium tip, Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centrosome (GO:0005813)
- cytoplasm (GO:0005737)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 17 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C12orf52, RITA |

**关键文献**:
1. Linking DNA methylation in brain regions to Alzheimer's disease risk: a Mendelian randomization study.. *Human molecular genetics*. PMID: 40267236
2. CK1 Is a Druggable Regulator of Microtubule Dynamics and Microtubule-Associated Processes.. *Cancers*. PMID: 35267653
3. Combining information from genome-wide association and multi-tissue gene expression studies to elucidate factors underlying genetic variation for residual feed intake in Australian Angus cattle.. *BMC genomics*. PMID: 31810463
4. The molecular and functional characterization of an Opaque2 homologue gene from Coix and a new classification of plant bZIP proteins.. *Plant molecular biology*. PMID: 9484437
5. The rice bZIP transcriptional activator RITA-1 is highly expressed during seed development.. *The Plant cell*. PMID: 7919992

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.3 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 22.3% |
| 中等置信 (pLDDT 50-70) 占比 | 52.0% |
| 低置信 (pLDDT<50) 占比 | 25.7% |
| 有序区域 (pLDDT>70) 占比 | 22.3% |
| 可用 PDB 条目 | 5EG6 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=59.3），有序残基占 22.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR031418; Pfam: PF17066 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RBPJ | 0.729 | 0.411 | — |
| DCP1A | 0.619 | 0.619 | — |
| JMJD4 | 0.616 | 0.000 | — |
| COLGALT1 | 0.610 | 0.610 | — |
| COL4A2 | 0.586 | 0.586 | — |
| PPP2R3C | 0.586 | 0.586 | — |
| LPP | 0.533 | 0.000 | — |
| CFAP73 | 0.532 | 0.000 | — |
| PEX10 | 0.511 | 0.000 | — |
| MRPL15 | 0.481 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Q81Z98 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| DCP1A | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| GOLGA2 | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |
| PLOD3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CEP43 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| COL4A2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PPP3CC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CEP350 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| COLGALT2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 13
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 13 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.3 + PDB: 5EG6 | pLDDT=59.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Cytoplasm, cytoskeleton, micro / Nucleoplasm; 额外: Golgi apparatus, Primary cilium,  | 一致 |
| PPI | STRING + IntAct | 15 + 13 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. RITA1 — RBPJ-interacting and tubulin-associated protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小269 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=59.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96K30
- Protein Atlas: https://www.proteinatlas.org/ENSG00000139405-RITA1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RITA1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96K30
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000139405-RITA1/subcellular

![](https://images.proteinatlas.org/39095/2248_H8_113_red_green.jpg)
![](https://images.proteinatlas.org/39095/2248_H8_138_red_green.jpg)
![](https://images.proteinatlas.org/39095/2249_C8_21_red_green.jpg)
![](https://images.proteinatlas.org/39095/2249_C8_9_red_green.jpg)
![](https://images.proteinatlas.org/39095/2252_F10_104_red_green.jpg)
![](https://images.proteinatlas.org/39095/2252_F10_74_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96K30-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

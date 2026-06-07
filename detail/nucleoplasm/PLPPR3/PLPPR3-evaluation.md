---
type: protein-evaluation
gene: "PLPPR3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PLPPR3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PLPPR3 / LPPR3, PHP2, PRG2 |
| 蛋白名称 | Phospholipid phosphatase-related protein type 3 |
| 蛋白大小 | 718 aa / 76.0 kDa |
| UniProt ID | Q6T4P5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Golgi apparatus; 额外: Nucleoplasm, Cytosol; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 718 aa / 76.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.5; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR043216, IPR000326, IPR036938; Pfam: PF01569 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 14 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nucleoplasm, Cytosol | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 5 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: LPPR3, PHP2, PRG2 |

**关键文献**:
1. Phosphorylation of presynaptic PLPPR3 controls synaptic vesicle release.. *iScience*. PMID: 41054519
2. [The Interaction of miRNA-5p and miRNA-3p with the mRNAs of Orthologous Genes].. *Molekuliarnaia biologiia*. PMID: 31397443
3. Transcriptome profiling reveals signaling conditions dictating human spermatogonia fate in vitro.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 32661178
4. Precursor types predict the stability of neuronal branches.. *Journal of cell science*. PMID: 34766183
5. Cell type-specific and subcellular expression of phospholipid phosphatase-related proteins to modulate lyso-phosphatidic acid synaptic signaling in the developing and adult CNS.. *Journal of neurochemistry*. PMID: 38994820

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.5 |
| 高置信度残基 (pLDDT>90) 占比 | 20.2% |
| 置信残基 (pLDDT 70-90) 占比 | 13.0% |
| 中等置信 (pLDDT 50-70) 占比 | 13.1% |
| 低置信 (pLDDT<50) 占比 | 53.8% |
| 有序区域 (pLDDT>70) 占比 | 33.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=58.5），有序残基占 33.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR043216, IPR000326, IPR036938; Pfam: PF01569 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ADCY1 | 0.655 | 0.000 | — |
| PLPPR1 | 0.590 | 0.547 | — |
| PTH | 0.582 | 0.000 | — |
| STX16 | 0.564 | 0.051 | — |
| GNAS | 0.562 | 0.000 | — |
| TSPAN33 | 0.529 | 0.000 | — |
| TMEM259 | 0.512 | 0.000 | — |
| MED16 | 0.493 | 0.000 | — |
| GRIN3B | 0.463 | 0.000 | — |
| ANKRD13B | 0.435 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| STRN4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| BAG6 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PLPPR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CHRND | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HTR3A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ADGRG5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NKAIN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CHRNA4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SIDT2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SYNGAP1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:37207277|imex:IM-29810 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 14
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 14 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.5 + PDB: 无 | pLDDT=58.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Golgi apparatus; 额外: Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 14 interactions | 数据充分 |

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
1. PLPPR3 — Phospholipid phosphatase-related protein type 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小718 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=58.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6T4P5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000129951-PLPPR3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PLPPR3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6T4P5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (approved)。来源: https://www.proteinatlas.org/ENSG00000129951-PLPPR3/subcellular

![](https://images.proteinatlas.org/57034/1038_D2_1_red_green.jpg)
![](https://images.proteinatlas.org/57034/1038_D2_2_red_green.jpg)
![](https://images.proteinatlas.org/57034/1040_D2_1_red_green.jpg)
![](https://images.proteinatlas.org/57034/1040_D2_2_red_green.jpg)
![](https://images.proteinatlas.org/57034/1319_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/57034/1319_B1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6T4P5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6T4P5 |
| SMART | SM00014; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR043216;IPR000326;IPR036938; |
| Pfam | PF01569; |

### humanPPI / HPA Interaction
Source: 未找到 HPA interaction 页面

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

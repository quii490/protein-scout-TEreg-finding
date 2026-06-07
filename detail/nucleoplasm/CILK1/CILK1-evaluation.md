---
type: protein-evaluation
gene: "CILK1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CILK1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CILK1 / ICK, KIAA0936 |
| 蛋白名称 | Serine/threonine-protein kinase ICK |
| 蛋白大小 | 632 aa / 71.4 kDa |
| UniProt ID | Q9UPZ9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Golgi apparatus, Vesicles; 额外: Primary cilium, Primary ciliu; UniProt: Nucleus; Cytoplasm, cytosol; Cell projection, cilium; Cytopl |
| 蛋白大小 | 10/10 | ×1 | 10 | 632 aa / 71.4 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=23 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011009, IPR050117, IPR000719, IPR017441, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **120.0/180** | |
| **归一化总分** | | | **66.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus, Vesicles; 额外: Primary cilium, Primary cilium tip | Approved |
| UniProt | Nucleus; Cytoplasm, cytosol; Cell projection, cilium; Cytoplasm, cytoskeleton, cilium basal body; Cy... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- ciliary basal body (GO:0036064)
- ciliary base (GO:0097546)
- ciliary tip (GO:0097542)
- cilium (GO:0005929)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 23 |
| PubMed broad count | 65 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ICK, KIAA0936 |

**关键文献**:
1. Ciliogenesis associated kinase 1: targets and functions in various organ systems.. *FEBS letters*. PMID: 31506943
2. The Scaffold Protein KATNIP Enhances CILK1 Control of Primary Cilia.. *Molecular and cellular biology*. PMID: 37665596
3. A homozygous frameshift variant in the CILK1 gene causes cranioectodermal dysplasia.. *European journal of human genetics : EJHG*. PMID: 40615527
4. KLC3 Regulates Ciliary Trafficking and Cyst Progression in CILK1 Deficiency-Related Polycystic Kidney Disease.. *Journal of the American Society of Nephrology : JASN*. PMID: 35961787
5. An epilepsy-associated CILK1 variant compromises KATNIP regulation and impairs primary cilia and Hedgehog signaling.. *bioRxiv : the preprint server for biology*. PMID: 38798407

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.8 |
| 高置信度残基 (pLDDT>90) 占比 | 32.0% |
| 置信残基 (pLDDT 70-90) 占比 | 10.1% |
| 中等置信 (pLDDT 50-70) 占比 | 4.3% |
| 低置信 (pLDDT<50) 占比 | 53.6% |
| 有序区域 (pLDDT>70) 占比 | 42.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=60.8），有序残基占 42.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011009, IPR050117, IPR000719, IPR017441, IPR008271; Pfam: PF00069 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CCNL2 | 0.865 | 0.000 | — |
| CDC6 | 0.800 | 0.782 | — |
| MCM3 | 0.800 | 0.782 | — |
| MCM7 | 0.797 | 0.789 | — |
| ORC3 | 0.792 | 0.782 | — |
| MCM4 | 0.789 | 0.782 | — |
| MCM5 | 0.788 | 0.782 | — |
| MCM2 | 0.787 | 0.782 | — |
| CDT1 | 0.787 | 0.782 | — |
| MCM6 | 0.782 | 0.782 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MCM7 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:23764002|imex:IM-20916 |
| HSP90AB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-17906|pubmed:22939624| |
| CPSF1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |
| PPP2CB | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |
| TP53 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |
| PSMD1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |
| NUP188 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |
| SPTAN1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| CLUAP1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| IFT88 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.8 + PDB: 无 | pLDDT=60.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, cytosol; Cell projection, cili / Golgi apparatus, Vesicles; 额外: Primary cilium, Pri | 一致 |
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
1. CILK1 — Serine/threonine-protein kinase ICK，非常新颖，仅有少数基础研究。
2. 蛋白大小632 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 23 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=60.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UPZ9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000112144-CILK1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CILK1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UPZ9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CILK1/IF_images/CILK1_IF_80_G1_1_blue_red_green.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (approved)。来源: https://www.proteinatlas.org/ENSG00000112144-CILK1/subcellular

![](https://images.proteinatlas.org/1113/2171_A1_41_blue_red_green.jpg)
![](https://images.proteinatlas.org/1113/2171_A1_55_blue_red_green.jpg)
![](https://images.proteinatlas.org/1113/2186_G4_41_blue_red_green.jpg)
![](https://images.proteinatlas.org/1113/2186_G4_7_blue_red_green.jpg)
![](https://images.proteinatlas.org/1113/2206_F9_49_blue_red_green.jpg)
![](https://images.proteinatlas.org/1113/2206_F9_9_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UPZ9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UPZ9 |
| SMART | SM00220; |
| UniProt Domain [FT] | DOMAIN 4..284; /note="Protein kinase"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00159, ECO:0000305" |
| InterPro | IPR011009;IPR050117;IPR000719;IPR017441;IPR008271; |
| Pfam | PF00069; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000112144-CILK1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FKBP5 | Intact, Biogrid | true |
| KATNIP | Intact, Biogrid | true |
| SMYD2 | Intact, Biogrid | true |
| BAG6 | Biogrid | false |
| CDK20 | Biogrid | false |
| HSP90AA1 | Biogrid | false |
| HSP90AB1 | Intact | false |
| MAPK1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

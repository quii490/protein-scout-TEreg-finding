---
type: protein-evaluation
gene: "KATNIP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KATNIP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KATNIP / KIAA0556 |
| 蛋白名称 | Katanin-interacting protein |
| 蛋白大小 | 1618 aa / 180.9 kDa |
| UniProt ID | O60303 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Basal body; 额外: Primary cilium, Centriolar sate; UniProt: Cytoplasm, cytoskeleton, cilium axoneme; Cytoplasm, cytoskel |
| 蛋白大小 | 5/10 | ×1 | 5 | 1618 aa / 180.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026704, IPR027859; Pfam: PF14652 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **125.0/180** | |
| **归一化总分** | | | **69.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Basal body; 额外: Primary cilium, Centriolar satellite | Approved |
| UniProt | Cytoplasm, cytoskeleton, cilium axoneme; Cytoplasm, cytoskeleton, cilium basal body; Cytoplasm, cyto... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 9+2 motile cilium (GO:0097729)
- axoneme (GO:0005930)
- centriolar satellite (GO:0034451)
- ciliary basal body (GO:0036064)
- ciliary base (GO:0097546)
- cilium (GO:0005929)
- extracellular space (GO:0005615)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 18 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0556 |

**关键文献**:
1. Joubert Syndrome.. **. PMID: 20301500
2. Clinical and genetic spectrum from a prototype of ciliopathy: Joubert syndrome.. *Clinical neurology and neurosurgery*. PMID: 36580738
3. The Scaffold Protein KATNIP Enhances CILK1 Control of Primary Cilia.. *Molecular and cellular biology*. PMID: 37665596
4. Katnip is needed to maintain microtubule function and lysosomal delivery to autophagosomes and phagosomes.. *Molecular biology of the cell*. PMID: 36598819
5. Phenotypic and Genotypic Characterization of 171 Patients with Syndromic Inherited Retinal Diseases Highlights the Importance of Genetic Testing for Accurate Clinical Diagnosis.. *Genes*. PMID: 40725402

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.4 |
| 高置信度残基 (pLDDT>90) 占比 | 22.7% |
| 置信残基 (pLDDT 70-90) 占比 | 18.7% |
| 中等置信 (pLDDT 50-70) 占比 | 6.5% |
| 低置信 (pLDDT<50) 占比 | 52.1% |
| 有序区域 (pLDDT>70) 占比 | 41.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=58.4），有序残基占 41.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026704, IPR027859; Pfam: PF14652 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KATNB1 | 0.725 | 0.292 | — |
| CEP104 | 0.689 | 0.000 | — |
| IFT22 | 0.601 | 0.384 | — |
| KATNAL1 | 0.581 | 0.331 | — |
| KATNA1 | 0.563 | 0.331 | — |
| KIF7 | 0.561 | 0.057 | — |
| CEP290 | 0.557 | 0.320 | — |
| IFT81 | 0.553 | 0.446 | — |
| MAK | 0.549 | 0.528 | — |
| CSPP1 | 0.548 | 0.094 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TBC1D4 | psi-mi:"MI:0018"(two hybrid) | pubmed:unassigned5 |
| prmB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| CILK1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| MAK | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| LLGL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |
| KIF2A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Tmed2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Vps28 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 9
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.4 + PDB: 无 | pLDDT=58.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, cilium axoneme; Cytoplasm / Nucleoplasm, Basal body; 额外: Primary cilium, Centr | 一致 |
| PPI | STRING + IntAct | 15 + 9 interactions | 数据充分 |

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
1. KATNIP — Katanin-interacting protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1618 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=58.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O60303
- Protein Atlas: https://www.proteinatlas.org/ENSG00000047578-KATNIP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KATNIP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60303
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000047578-KATNIP/subcellular

![](https://images.proteinatlas.org/35090/2185_A7_38_red_green.jpg)
![](https://images.proteinatlas.org/35090/2185_A7_64_red_green.jpg)
![](https://images.proteinatlas.org/35090/2186_H5_19_red_green.jpg)
![](https://images.proteinatlas.org/35090/2186_H5_77_red_green.jpg)
![](https://images.proteinatlas.org/35090/2201_B8_28_red_green.jpg)
![](https://images.proteinatlas.org/35090/2201_B8_75_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O60303-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

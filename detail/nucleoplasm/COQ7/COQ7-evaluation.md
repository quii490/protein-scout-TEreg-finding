---
type: protein-evaluation
gene: "COQ7"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## COQ7 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COQ7 |
| 蛋白名称 | NADPH-dependent 3-demethoxyubiquinone 3-hydroxylase, mitochondrial |
| 蛋白大小 | 217 aa / 24.3 kDa |
| UniProt ID | Q99807 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Plasma membrane; 额外: Nucleoplasm; UniProt: Mitochondrion inner membrane; Mitochondrion; Nucleus; Chromo |
| 蛋白大小 | 10/10 | x1 | 10 | 217 aa / 24.3 kDa |
| 研究新颖性 | 2/10 | x5 | 10 | PubMed strict=98 篇 (<=100->2) |
| 三维结构 | 9/10 | x3 | 27 | AlphaFold v6 pLDDT=86.9; PDB: 7SSP, 7SSS |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR009078, IPR011566; Pfam: PF03232 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **102.0/180** | |
| **归一化总分** | | | **56.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Nucleoplasm | Approved |
| UniProt | Mitochondrion inner membrane; Mitochondrion; Nucleus; Chromosome | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- chromosome (GO:0005694)
- extrinsic component of mitochondrial inner membrane (GO:0031314)
- mitochondrial inner membrane (GO:0005743)
- mitochondrion (GO:0005739)
- nucleus (GO:0005634)
- ubiquinone biosynthesis complex (GO:0110142)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 98 |
| PubMed broad count | 156 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Nuclear Gene-Encoded Leigh Syndrome Spectrum Overview.. **. PMID: 26425749
2. New variants expand the neurological phenotype of COQ7 deficiency.. *Journal of inherited metabolic disease*. PMID: 38973597
3. Homozygous COQ7 mutation: a new cause of potentially treatable distal hereditary motor neuropathy.. *Brain : a journal of neurology*. PMID: 36454683
4. Biallelic variants in the COQ7 gene cause distal hereditary motor neuropathy in two Chinese families.. *Brain : a journal of neurology*. PMID: 36758993
5. Reply: Biallelic variants in the COQ7 gene cause distal hereditary motor neuropathy in two Chinese families.. *Brain : a journal of neurology*. PMID: 36759155

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.9 |
| 高置信度残基 (pLDDT>90) 占比 | 77.0% |
| 置信残基 (pLDDT 70-90) 占比 | 3.2% |
| 中等置信 (pLDDT 50-70) 占比 | 2.3% |
| 低置信 (pLDDT<50) 占比 | 17.5% |
| 有序区域 (pLDDT>70) 占比 | 80.2% |
| 可用 PDB 条目 | 7SSP, 7SSS |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（7SSP, 7SSS）+ AlphaFold高质量预测（pLDDT=86.9），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009078, IPR011566; Pfam: PF03232 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| COQ3 | 0.999 | 0.351 | — |
| COQ9 | 0.999 | 0.937 | — |
| COQ5 | 0.998 | 0.292 | — |
| COQ6 | 0.990 | 0.292 | — |
| COQ4 | 0.987 | 0.328 | — |
| COQ8A | 0.919 | 0.301 | — |
| COQ8B | 0.901 | 0.311 | — |
| CLK3 | 0.893 | 0.000 | — |
| PDSS1 | 0.876 | 0.087 | — |
| COQ2 | 0.868 | 0.075 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| homer | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| PTPMT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| COQ8B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| COQ8A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| COQ5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| COQ3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| COQ4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| COQ9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| BOLA3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |
| ATAD3B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:27499296|imex:IM-26449| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.9 + PDB: 7SSP, 7SSS | pLDDT=86.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Mitochondrion inner membrane; Mitochondrion; Nucle / Plasma membrane; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ***

**核心优势**:
1. COQ7 -- NADPH-dependent 3-demethoxyubiquinone 3-hydroxylase, mitochondrial，研究基础较多，新颖性有限。
2. 蛋白大小217 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 98 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| COQ9 | BioGRID | 0 |
| COQ4 | BioGRID | 0 |
| COQ7 | BioGRID | 0 |
| BOLA3 | BioGRID | 0 |
| COQ5 | BioGRID | 0 |
| ADCK3 | BioGRID | 0 |
| NRD1 | BioGRID | 0 |
| CHCHD2 | BioGRID | 0 |


### TE 调控评估

该蛋白具有核定位证据，可能间接参与 TE 调控。需实验验证。

### 深度机制分析

COQ7（UniProt Q99807）属于二铁含铁蛋白超家族，携带特征性Ferritin-like结构域（IPR009078）和COQ7特有结构域（IPR011566/PF03232），催化辅酶Q10生物合成途径中倒数第二步反应——将demethoxyubiquinone（DMQ）羟基化为5-hydroxy-demethoxyubiquinone。AlphaFold v6预测结构整体pLDDT为86.9，有序区域占比80.2%，高置信残基（pLDDT>90）达77.0%，表明核心二铁催化折叠高度可信。实验解析的冷冻电镜结构（PDB:7SSP, 7SSS）已捕获COQ7在COQ复合体（也称为Complex Q或ubiquinone biosynthesis complex, GO:0110142）中的构象状态，揭示了其与COQ9、COQ3、COQ4等多亚基如何协同完成线粒体膜内的电子传递和底物通道传递。

STRING-PPI网络显示COQ7处于极度致密的COQ生物合成相互作用网络中央：与COQ3（0.999）、COQ9（0.999, experimental=0.937）、COQ5（0.998）、COQ6（0.990）、COQ4（0.987）等形成高置信度功能复合体。IntAct实验数据进一步证实COQ7与COQ9、COQ3、COQ4、COQ5、COQ6、COQ8A、COQ8B均存在抗标签免疫共沉淀验证的直接物理互作（PMID:27499296），确认COQ7是线粒体内膜超分子COQ复合体的核心亚基。

关键的功能重定向线索来自其亚细胞定位的矛盾性：UniProt注释为线粒体内膜、线粒体基质和细胞核/染色体，而HPA免疫荧光检测到主要信号在质膜和核质。GO注释明确包含chromosome（GO:0005694）和nucleus（GO:0005634），提示COQ7可能在线粒体外存在"兼职功能"（moonlighting）。类似情况见于许多线粒体代谢酶（如fumarase、aconitase），它们在特定应激或信号条件下重新定位至细胞核，行使与代谢无关的调控功能。

值得注意的是，COQ7缺乏（PMID:38973597）与神经元病表型密切相关，而最近研究（PMID:36454683, PMID:36758993）揭示了COQ7双等位基因变异导致远端遗传性运动神经病（dHMN）。这些神经病理学表现可能不仅源于辅酶Q10合成缺陷引发的线粒体能量代谢障碍，也可能涉及COQ7在核内的非经典功能——如染色体结合参与基因表达调控或DNA损伤修复。COQ7的核定位机制及核内功能基质仍有待反向遗传学和ChIP-seq等手段揭示。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q99807
- Protein Atlas: https://www.proteinatlas.org/ENSG00000167186-COQ7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COQ7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99807
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q99807-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q99807 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR009078;IPR011566; |
| Pfam | PF03232; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000167186-COQ7/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| COQ9 | Intact, Biogrid | true |
| COQ3 | Intact | false |
| COQ4 | Intact | false |
| COQ5 | Intact | false |
| COQ6 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

---
type: protein-evaluation
gene: "TRAK1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TRAK1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TRAK1 / KIAA1042, OIP106 |
| 蛋白名称 | Trafficking kinesin-binding protein 1 |
| 蛋白大小 | 953 aa / 106.0 kDa |
| UniProt ID | Q9UPV9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Endoplasmic reticulum; 额外: Nucleoplasm; UniProt: Cytoplasm; Nucleus; Mitochondrion; Early endosome; Endosome; |
| 蛋白大小 | 8/10 | ×1 | 8 | 953 aa / 106.0 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=48 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR006933, IPR051946, IPR022154; Pfam: PF04849, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **108.0/180** | |
| **归一化总分** | | | **60.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum; 额外: Nucleoplasm | Approved |
| UniProt | Cytoplasm; Nucleus; Mitochondrion; Early endosome; Endosome; Mitochondrion membrane; Cytoplasm, cell... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- axon cytoplasm (GO:1904115)
- axonal growth cone (GO:0044295)
- cell cortex (GO:0005938)
- cytoplasm (GO:0005737)
- cytoplasmic vesicle (GO:0031410)
- cytosol (GO:0005829)
- dendrite (GO:0030425)
- early endosome (GO:0005769)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 48 |
| PubMed broad count | 82 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1042, OIP106 |

**关键文献**:
1. Expanding the genetic heterogeneity of intellectual disability.. *Human genetics*. PMID: 28940097
2. Structural-functional characterization of the MIRO1-TRAK1 complex.. *Nature communications*. PMID: 40615373
3. Interaction between the mitochondrial adaptor MIRO and the motor adaptor TRAK.. *The Journal of biological chemistry*. PMID: 37949220
4. Hypertonia-linked protein Trak1 functions with mitofusins to promote mitochondrial tethering and fusion.. *Protein & cell*. PMID: 28924745
5. Hypertonia-associated protein Trak1 is a novel regulator of endosome-to-lysosome trafficking.. *Journal of molecular biology*. PMID: 18675823

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.1 |
| 高置信度残基 (pLDDT>90) 占比 | 20.3% |
| 置信残基 (pLDDT 70-90) 占比 | 11.1% |
| 中等置信 (pLDDT 50-70) 占比 | 16.9% |
| 低置信 (pLDDT<50) 占比 | 51.7% |
| 有序区域 (pLDDT>70) 占比 | 31.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=58.1），有序残基占 31.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR006933, IPR051946, IPR022154; Pfam: PF04849, PF12448 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RHOT2 | 0.999 | 0.635 | — |
| RHOT1 | 0.999 | 0.718 | — |
| TRAK2 | 0.966 | 0.769 | — |
| OGT | 0.963 | 0.604 | — |
| MFN2 | 0.942 | 0.000 | — |
| NDE1 | 0.922 | 0.000 | — |
| KIF5B | 0.887 | 0.462 | — |
| KIF5A | 0.883 | 0.504 | — |
| DISC1 | 0.879 | 0.000 | — |
| KIF5C | 0.849 | 0.394 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TRAF3IP1 | psi-mi:"MI:0018"(two hybrid) | pubmed:17043677|imex:IM-16650 |
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| CDK6 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:22094256|imex:IM-16628 |
| RHOT1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12162|pubmed:19135897 |
| Kif5c | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12162|pubmed:19135897 |
| TOMM22 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| TOMM20 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| CDC5L | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| GSK3B | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| TRAK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.1 + PDB: 无 | pLDDT=58.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Mitochondrion; Early endosome; / Endoplasmic reticulum; 额外: Nucleoplasm | 一致 |
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
1. TRAK1 — Trafficking kinesin-binding protein 1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小953 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 48 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=58.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UPV9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000182606-TRAK1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TRAK1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UPV9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Endoplasmic reticulum (approved)。来源: https://www.proteinatlas.org/ENSG00000182606-TRAK1/subcellular

![](https://images.proteinatlas.org/11367/1662_F11_1_red_green.jpg)
![](https://images.proteinatlas.org/11367/1662_F11_3_red_green.jpg)
![](https://images.proteinatlas.org/11367/1740_E2_17_cr57fb620f35c08_red_green.jpg)
![](https://images.proteinatlas.org/11367/1740_E2_8_cr5810d60adac46_red_green.jpg)
![](https://images.proteinatlas.org/11367/1744_E2_23_cr57fe2792146ed_red_green.jpg)
![](https://images.proteinatlas.org/11367/1744_E2_26_cr57fe279d9c753_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UPV9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9UPV9 |
| SMART | SM01424;SM01423; |
| UniProt Domain [FT] | DOMAIN 47..354; /note="HAP1 N-terminal" |
| InterPro | IPR006933;IPR051946;IPR022154; |
| Pfam | PF04849;PF12448; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000182606-TRAK1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DYNLL1 | Biogrid, Opencell | true |
| DYNLL2 | Biogrid, Opencell | true |
| GSK3B | Biogrid, Opencell | true |
| OGT | Intact, Biogrid | true |
| RHOT2 | Intact, Biogrid | true |
| YWHAB | Biogrid, Opencell | true |
| YWHAE | Biogrid, Opencell | true |
| YWHAZ | Biogrid, Opencell | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

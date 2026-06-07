---
type: protein-evaluation
gene: "BUB1B"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BUB1B — REJECTED (研究热度过高 (PubMed strict=423，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BUB1B / BUBR1, MAD3L, SSK1 |
| 蛋白名称 | Mitotic checkpoint serine/threonine-protein kinase BUB1 beta |
| 蛋白大小 | 1050 aa / 119.5 kDa |
| UniProt ID | O60566 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Basal body; UniProt: Cytoplasm; Nucleus; Chromosome, centromere, kinetochore; Cyt |
| 蛋白大小 | 8/10 | ×1 | 8 | 1050 aa / 119.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=423 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.6; PDB: 2WVI, 3SI5, 4GGD, 5JJA, 5K6S, 5KHU, 5LCW |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR015661, IPR011009, IPR013212; Pfam: PF08311 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.5/180** | |
| **归一化总分** | | | **44.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Basal body | Supported |
| UniProt | Cytoplasm; Nucleus; Chromosome, centromere, kinetochore; Cytoplasm, cytoskeleton, microtubule organi... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- anaphase-promoting complex (GO:0005680)
- centrosome (GO:0005813)
- ciliary basal body (GO:0036064)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- kinetochore (GO:0000776)
- mitotic checkpoint complex (GO:0033597)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 423 |
| PubMed broad count | 610 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BUBR1, MAD3L, SSK1 |

**关键文献**:
1. Positive feedback regulation between glycolysis and histone lactylation drives oncogenesis in pancreatic ductal adenocarcinoma.. *Molecular cancer*. PMID: 38711083
2. Deleterious Germline Mutations in Patients With Apparently Sporadic Pancreatic Adenocarcinoma.. *Journal of clinical oncology : official journal of the American Society of Clinical Oncology*. PMID: 28767289
3. BUB1b impairs chemotherapy sensitivity via resistance to ferroptosis in lung adenocarcinoma.. *Cell death & disease*. PMID: 39043653
4. Differentially Expressed Genes Associated with the Development of Cervical Cancer.. *International journal of molecular sciences*. PMID: 41516135
5. Correlation of BUB1 and BUB1B with the development and prognosis of endometrial cancer.. *Scientific reports*. PMID: 39048649

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.6 |
| 高置信度残基 (pLDDT>90) 占比 | 14.5% |
| 置信残基 (pLDDT 70-90) 占比 | 34.3% |
| 中等置信 (pLDDT 50-70) 占比 | 13.9% |
| 低置信 (pLDDT<50) 占比 | 37.3% |
| 有序区域 (pLDDT>70) 占比 | 48.8% |
| 可用 PDB 条目 | 2WVI, 3SI5, 4GGD, 5JJA, 5K6S, 5KHU, 5LCW, 5SWF, 6TLJ |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=63.6），有序残基占 48.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR015661, IPR011009, IPR013212; Pfam: PF08311 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NEK2 | 0.999 | 0.994 | — |
| PLK1 | 0.999 | 0.845 | — |
| ANAPC2 | 0.999 | 0.993 | — |
| AURKB | 0.999 | 0.327 | — |
| CDC23 | 0.999 | 0.999 | — |
| ANAPC4 | 0.999 | 0.999 | — |
| BUB1 | 0.999 | 0.919 | — |
| CDC20 | 0.999 | 0.999 | — |
| CENPF | 0.999 | 0.000 | — |
| CDC16 | 0.999 | 0.992 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000287598.7 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| ENSMUSP00000037126.8 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| COMMD4 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| BUB3 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| CENPE | psi-mi:"MI:0018"(two hybrid) | pubmed:9763420|imex:IM-18999 |
| CDC20 | psi-mi:"MI:0018"(two hybrid) | pubmed:11030144|imex:IM-19387 |
| CDC16 | psi-mi:"MI:0096"(pull down) | pubmed:11030144|imex:IM-19387 |
| CDC27 | psi-mi:"MI:0096"(pull down) | pubmed:11030144|imex:IM-19387 |
| DNMBP | psi-mi:"MI:0018"(two hybrid) | imex:IM-13772|pubmed:18654987 |
| Anapc16 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.6 + PDB: 2WVI, 3SI5, 4GGD, 5JJA, 5K6S,  | pLDDT=63.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Chromosome, centromere, kineto / Cytosol; 额外: Basal body | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. BUB1B — Mitotic checkpoint serine/threonine-protein kinase BUB1 beta，研究基础较多，新颖性有限。
2. 蛋白大小1050 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 423 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=63.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 423 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O60566
- Protein Atlas: https://www.proteinatlas.org/ENSG00000156970-BUB1B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BUB1B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60566
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000156970-BUB1B/subcellular

![](https://images.proteinatlas.org/8419/2176_E9_31_blue_red_green.jpg)
![](https://images.proteinatlas.org/8419/2176_E9_47_blue_red_green.jpg)
![](https://images.proteinatlas.org/8419/2178_H10_19_blue_red_green.jpg)
![](https://images.proteinatlas.org/8419/2178_H10_9_blue_red_green.jpg)
![](https://images.proteinatlas.org/8419/2201_A10_77_blue_red_green.jpg)
![](https://images.proteinatlas.org/8419/2201_A10_97_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O60566-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O60566 |
| SMART | SM00777; |
| UniProt Domain [FT] | DOMAIN 62..226; /note="BUB1 N-terminal"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00822"; DOMAIN 766..1050; /note="Protein kinase" |
| InterPro | IPR015661;IPR011009;IPR013212; |
| Pfam | PF08311; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000156970-BUB1B/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ANAPC16 | Biogrid, Opencell | true |
| ANAPC2 | Biogrid, Opencell | true |
| ANAPC4 | Intact, Biogrid, Opencell | true |
| ANAPC7 | Intact, Biogrid | true |
| BUB1 | Intact, Biogrid | true |
| BUB3 | Intact, Biogrid, Opencell | true |
| CDC16 | Biogrid, Opencell | true |
| CDC20 | Intact, Biogrid, Opencell | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

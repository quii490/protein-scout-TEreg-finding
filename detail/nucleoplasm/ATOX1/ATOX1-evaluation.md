---
type: protein-evaluation
gene: "ATOX1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: rejected
---

## ATOX1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ATOX1 / HAH1 |
| 蛋白名称 | Copper transport protein ATOX1 |
| 蛋白大小 | 68 aa / 7.4 kDa |
| UniProt ID | O00244 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 03:26:11 |

### 2. 评分总览

**评估状态：REJECTED**
**拒因：PubMed strict count 259 > 100**

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 10/10 | x4 | 40 | HPA: Nucleoplasm |
| 蛋白大小 | 4/10 | x1 | 4 | 68 aa / 7.4 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=259 篇 |
| 三维结构 | 1/10 | x3 | 3 | AlphaFold pLDDT 不可用; PDB: 1FE0, 1FE4, 1FEE |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: 4; Pfam: 1; IPR051881, IPR017969... |
| PPI 网络 | 8/10 | x3 | 24 | STRING 15 partners; IntAct 13 interactions |
| 互证加分 | -- | max +3 | 1.0 | STRING + IntAct 双源验证: +0.5; PDB 多条目覆盖: +0.5 |
| **原始总分** | | | **86.0/180** | |
| **归一化总分 (/1.83)** | | | **47.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoplasm, Plasma membrane | Approved |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- cytosol (GO:0005829)

**结论**: 核定位证据充分，多个数据源一致支持核定位，定位特异性高。

#### 3.2 蛋白大小评估

**评价**: 68 aa，蛋白较小，但仍在可操作范围。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 259 |
| PubMed broad count | 407 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HAH1 |

**关键文献**:
1. Copper metabolism in cell death and autophagy.. *Autophagy*. PMID: 37055935
2. Copper homeostasis and neurodegenerative diseases.. *Neural regeneration research*. PMID: 39589160
3. Targeting copper homeostasis: Akkermansia-derived OMVs co-deliver Atox1 siRNA and elesclomol for cancer therapy.. *Acta pharmaceutica Sinica. B*. PMID: 40487636
4. Roles of Copper Transport Systems Members in Breast Cancer.. *Cancer medicine*. PMID: 39676279
5. Balancing between cuproplasia and copper-dependent cell death: molecular basis and clinical implications of ATOX1 in cancer.. *Journal of experimental & clinical cancer research : CR*. PMID: 40721800


#### 3.4 三维结构分析

**AlphaFold pLDDT 统计数据不可用（获取失败）。**

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: 三维结构数据有限。三维结构评分 1/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051881, IPR017969, IPR006121, IPR036163; Pfam: PF00403 |

**染色质调控潜力分析**: 存在 5 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score > 0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SCO2 | 0.846 | 0.000 | -- |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Dmel\CG15576 | two hybrid | pubmed:14605208|imex:IM-16524|mint:MINT-5216804 |
| Dmel\CG15109 | two hybrid | pubmed:14605208|imex:IM-16524|mint:MINT-5216804 |
| COMP | two hybrid array | pubmed:32296183|imex:IM-25472 |
| NECAB1 | validated two hybrid | pubmed:32296183|imex:IM-25472 |
| FAM118A | validated two hybrid | pubmed:32296183|imex:IM-25472 |
| CFAP410 | two hybrid prey pooling approach | imex:IM-23318|pubmed:25416956 |
| GGPS1 | two hybrid prey pooling approach | imex:IM-23318|pubmed:25416956 |
| ATP7B | pull down | imex:IM-25076|pubmed:12968035 |
| HTRA4 | pull down | imex:IM-28152|pubmed:31470122 |
| "BcDNA:AT08210" | two hybrid array | pubmed:37061542|imex:IM-28761 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 13

**评价**: 互作网络中等：STRING 15 预测 + IntAct 13 实验互作。PPI 评分 8/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | -- | 不可用 | -- |
| 定位 | HPA | Nucleoplasm | 单一来源 |
| PPI | STRING + IntAct | 15 + 13 interactions | 数据充分 |

**互证加分明细**:
- STRING + IntAct 双源验证: +0.5
- PDB 多条目覆盖: +0.5
**总分**: +1.0 / max +3

### 4. 总体评价

**归一化总分**: 47.0/100
**状态**: REJECTED -- PubMed strict count 259 > 100

**核心优势**:
1. 已有PDB实验结构：1FE0, 1FE4, 1FEE。
2. 存在 5 个已知结构域，有明确的结构-功能切入点。
3. 核定位信号明确，多个数据源一致支持。

**风险/不确定性**:
1. 蛋白过小（68 aa），实验操作受限

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/O00244
- Protein Atlas: https://www.proteinatlas.org/search/ATOX1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ATOX1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O00244
- STRING: https://string-db.org/network/9606.ATOX1
- Packet data timestamp: 2026-06-03 03:26:11

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000177556-ATOX1/subcellular

![](https://images.proteinatlas.org/55036/875_H1_2_red_green.jpg)
![](https://images.proteinatlas.org/55036/875_H1_3_red_green.jpg)
![](https://images.proteinatlas.org/55036/883_H1_2_red_green.jpg)
![](https://images.proteinatlas.org/55036/883_H1_3_red_green.jpg)
![](https://images.proteinatlas.org/55036/908_F3_1_red_green.jpg)
![](https://images.proteinatlas.org/55036/908_F3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O00244-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O00244 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 1..63; /note="HMA"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00280" |
| InterPro | IPR051881;IPR017969;IPR006121;IPR036163; |
| Pfam | PF00403; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000177556-ATOX1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ATP7B | Intact, Biogrid | true |
| ATP7A | Biogrid | false |
| CFAP410 | Intact | false |
| COMP | Intact | false |
| FAM118A | Intact | false |
| GGPS1 | Intact | false |
| NECAB1 | Intact | false |
| TRAF4 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

---
type: protein-evaluation
gene: "HSBP1L1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HSBP1L1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HSBP1L1 |
| 蛋白名称 | Heat shock factor-binding protein 1-like protein 1 |
| 蛋白大小 | 74 aa / 8.4 kDa |
| UniProt ID | C9JCN9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 5/10 | ×1 | 5 | 74 aa / 8.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=1 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=88.0; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR009643; Pfam: PF06825 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 11 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1 |
| PubMed broad count | 1 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Gene signature associated with neuro-endocrine activity predicting prognosis of pancreatic carcinoma.. *Molecular genetics & genomic medicine*. PMID: 31102348

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.0 |
| 高置信度残基 (pLDDT>90) 占比 | 67.6% |
| 置信残基 (pLDDT 70-90) 占比 | 18.9% |
| 中等置信 (pLDDT 50-70) 占比 | 12.2% |
| 低置信 (pLDDT<50) 占比 | 1.4% |
| 有序区域 (pLDDT>70) 占比 | 86.5% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=88.0，有序区 86.5%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009643; Pfam: PF06825 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HSPA4 | 0.655 | 0.000 | — |
| WASHC3 | 0.639 | 0.411 | — |
| RBX1 | 0.528 | 0.000 | — |
| SLC66A2 | 0.490 | 0.000 | — |
| TXNL4A | 0.482 | 0.000 | — |
| ARPP19 | 0.469 | 0.000 | — |
| IREB2 | 0.466 | 0.000 | — |
| RBFA | 0.462 | 0.000 | — |
| STOML2 | 0.448 | 0.000 | — |
| LAMTOR1 | 0.448 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NR2F6 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| AGTRAP | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MESD | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PBX4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TNFRSF10D | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| FKBP7 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| CMTM4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| NFKBID | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SYNGR3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ALAS1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 11
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 11 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.0 + PDB: 无 | pLDDT=88.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 11 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. HSBP1L1 — Heat shock factor-binding protein 1-like protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小74 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 1 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 深度机制分析

HSBP1L1（Heat shock factor-binding protein 1-like protein 1）属于HSBP1蛋白家族。InterPro注释为IPR009643（Heat shock factor-binding protein 1-like），Pfam对应PF06825（HSBP1）。该家族的原型成员HSFBP1（HSBP1）已被表征为热休克因子（HSF）转录活性的负调控因子——HSBP1结合HSF的三聚化结构域，抑制其DNA结合活性，从而减弱热休克应答。HSBP1L1作为"like"家族成员，其序列与HSBP1具有同源性，但功能域可能呈简并化或新功能化（neofunctionalization）。AlphaFold v6预测整体pLDDT=88.0，高置信度残基占67.6%，有序区域占86.5%——对于一个仅74个氨基酸的小蛋白而言，这种结构置信度表明它形成了一个高度紧凑且折叠良好的球形结构域。

HSBP1L1的蛋白大小（74 aa / 8.4 kDa）是该候选名单中最小的蛋白之一，甚至接近肽段量级。如此小的尺寸限制了其独立酶活性的可能性，但其完整的HSBP1-like折叠暗示其保留蛋白-蛋白相互作用的能力——可能作为HSF调控网络的竞争性抑制剂、变构调节因子或接头蛋白发挥功能。PPI网络支持这一功能模型：STRING记录HSPA4（combined score=0.655）是HSP70家族应激诱导伴侣蛋白，HSBP1L1可能通过与HSPA4互作桥接HSF-热休克蛋白信号通路。WASHC3（0.639, experimental=0.411）是WASH复合体亚基，参与内体分选和自噬。

IntAct实验验证互作中，NR2F6（PMID:20195357, display technology）是核孤儿受体/转录因子，参与免疫应答调控。AGTRAP（PMID:32296183, validated Y2H）是1型血管紧张素II受体相关蛋白，介导受体信号转导。PBX4（PMID:32296183, Y2H array）是pre-B细胞白血病同源框转录因子。这些互作提示HSBP1L1可能与核激素受体和发育转录因子的调控相关。BioGRID还记录了TNIP2（TNFAIP3相互作用蛋白2，NF-κB负调控因子）的互作，进一步支持HSBP1L1在应激信号和炎症通路中的功能交集。

HSBP1L1的HPA IF定位于核质（Nucleoplasm, Approved），GO-CC注释同时包含nucleus（GO:0005634）和cytosol（GO:0005829）。核质定位与小蛋白的特征一致——低于40 kDa的蛋白可通过核孔自由扩散。但HPA IF的approved可靠性提示其核质富集可能是主动保留（nuclear retention）而非被动扩散的结果——可能通过与核内蛋白（如转录因子、核受体）结合后的复合物形成来实现核内驻留。

从TE调控角度看，HSBP1L1的潜在机制包括：（1）通过调控HSF/HSPA4介导的应激应答影响TE在应激条件下的转录激活——热休克应激已知激活特定TE家族（如HERV和LINE-1）的转录；（2）通过与NR2F6和PBX4等转录因子的互作间接参与TE衍生调控元件的转录调控；（3）作为小分子蛋白接头，整合应激信号与核转录调控。其极端的研究新颖性（PubMed strict=1篇）、高置信度结构、明确的核定位和与应激-转录调控的机制关联，使其成为TE调控研究中一个高风险高回报的候选靶点。

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TNIP2 | BioGRID | 1 |
| ALAS1 | BioGRID | 1 |
| PBX4 | BioGRID | 1 |
| NFKBID | BioGRID | 1 |
| FKBP7 | BioGRID | 0 |
| PLP2 | BioGRID | 0 |
| MESDC2 | BioGRID | 0 |
| SYNGR3 | BioGRID | 0 |


### TE 调控评估

该蛋白具有核定位证据，可能间接参与 TE 调控。需实验验证。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/C9JCN9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000226742-HSBP1L1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HSBP1L1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/C9JCN9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000226742-HSBP1L1/subcellular

![](https://images.proteinatlas.org/48273/1898_D7_17_cr5ba8a7dea6638_red_green.jpg)
![](https://images.proteinatlas.org/48273/1898_D7_9_cr5ba8a7dea5ca1_red_green.jpg)
![](https://images.proteinatlas.org/48273/735_G11_1_red_green.jpg)
![](https://images.proteinatlas.org/48273/735_G11_2_red_green.jpg)
![](https://images.proteinatlas.org/48273/979_E3_1_red_green.jpg)
![](https://images.proteinatlas.org/48273/979_E3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-C9JCN9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | C9JCN9 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR009643; |
| Pfam | PF06825; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000226742-HSBP1L1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ALAS1 | Intact | false |
| FKBP7 | Intact | false |
| MESD | Intact | false |
| NFKBID | Intact | false |
| PBX4 | Intact | false |
| PLP2 | Intact | false |
| SYNGR3 | Intact | false |
| TNFRSF10D | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

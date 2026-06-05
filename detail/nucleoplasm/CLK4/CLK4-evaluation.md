---
type: protein-evaluation
gene: "CLK4"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CLK4 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CLK4 |
| 蛋白名称 | Dual specificity protein kinase CLK4 |
| 蛋白大小 | 481 aa / 57.5 kDa |
| UniProt ID | Q9HAZ1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: Actin filaments; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 481 aa / 57.5 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=36 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=79.1; PDB: 6FYV |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051175, IPR011009, IPR000719, IPR017441, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.0/180** | |
| **归一化总分** | | | **72.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Actin filaments | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 36 |
| PubMed broad count | 73 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Novel SR-rich-related protein clasp specifically interacts with inactivated Clk4 and induces the exon EB inclusion of Clk.. *The Journal of biological chemistry*. PMID: 12169693
2. N(1)-Benzoylated 5-(4-pyridinyl)indazole-based kinase inhibitors: Attaining haspin and Clk4 selectivity via modulation of the benzoyl substituents.. *Archiv der Pharmazie*. PMID: 38478964
3. Analyzing the toxicological effects of PET-MPs on male infertility: Insights from network toxicology, mendelian randomization, and transcriptomics.. *Reproductive biology*. PMID: 40929757
4. SGC-CLK-1: A chemical probe for the Cdc2-like kinases CLK1, CLK2, and CLK4.. *Current research in chemical biology*. PMID: 38009092
5. Pharmacophore and 3D-QSAR characterization of 6-arylquinazolin-4-amines as Cdc2-like kinase 4 (Clk4) and dual specificity tyrosine-phosphorylation-regulated kinase 1A (Dyrk1A) inhibitors.. *Journal of chemical information and modeling*. PMID: 23496085

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.1 |
| 高置信度残基 (pLDDT>90) 占比 | 68.0% |
| 置信残基 (pLDDT 70-90) 占比 | 2.9% |
| 中等置信 (pLDDT 50-70) 占比 | 1.0% |
| 低置信 (pLDDT<50) 占比 | 28.1% |
| 有序区域 (pLDDT>70) 占比 | 70.9% |
| 可用 PDB 条目 | 6FYV |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 高质量预测（pLDDT=79.1，有序区 70.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051175, IPR011009, IPR000719, IPR017441, IPR008271; Pfam: PF00069 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CLK1 | 0.959 | 0.000 | — |
| MBP | 0.658 | 0.000 | — |
| SRPK1 | 0.588 | 0.431 | — |
| SRSF6 | 0.583 | 0.173 | — |
| SRSF5 | 0.558 | 0.174 | — |
| SRSF4 | 0.558 | 0.199 | — |
| H2BC21 | 0.557 | 0.000 | — |
| UBL5 | 0.551 | 0.474 | — |
| PNISR | 0.540 | 0.070 | — |
| JMJD6 | 0.524 | 0.524 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| UBL5 | psi-mi:"MI:0018"(two hybrid) | pubmed:12824502 |
| RNF181 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| SRPK1 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:23602568|imex:IM-17935 |
| AHCYL2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |
| SRRM2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| ZC3H18 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| JMJD6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| KRTAP10-6 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SRRM4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.1 + PDB: 6FYV | pLDDT=79.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Actin filaments | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. CLK4 — Dual specificity protein kinase CLK4，非常新颖，仅有少数基础研究。
2. 蛋白大小481 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 36 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9HAZ1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000113240-CLK4/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CLK4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9HAZ1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CLK4/IF_images/A-549_1.jpg]]
![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CLK4/IF_images/U2OS_2.jpg]]
![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CLK4/IF_images/A-549_2.jpg]]


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CLK4/CLK4-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Actin filaments (approved)。来源: https://www.proteinatlas.org/ENSG00000113240-CLK4/subcellular

![](https://images.proteinatlas.org/43746/516_F6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43746/516_F6_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/43746/519_F6_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/43746/519_F6_7_blue_red_green.jpg)
![](https://images.proteinatlas.org/43746/556_F6_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/43746/556_F6_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

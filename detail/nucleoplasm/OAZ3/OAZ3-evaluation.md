---
type: protein-evaluation
gene: "OAZ3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## OAZ3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | OAZ3 |
| 蛋白名称 | Ornithine decarboxylase antizyme 3 |
| 蛋白大小 | 235 aa / 27.4 kDa |
| UniProt ID | Q9UMX2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Mid piece, Principal piece; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 235 aa / 27.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=18 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR016181, IPR002993, IPR038581; Pfam: PF02100 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Mid piece, Principal piece | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- blood microparticle (GO:0072562)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- sperm midpiece (GO:0097225)
- sperm principal piece (GO:0097228)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 18 |
| PubMed broad count | 24 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Identification of Potential Biomarkers Associated with Spermatogenesis in Azoospermia.. *Clinical laboratory*. PMID: 39506588
2. Ornithine decarboxylase antizyme Oaz3 modulates protein phosphatase activity.. *The Journal of biological chemistry*. PMID: 21712390
3. Testicular Toxicity in Rats Exposed to AlCl(3): a Proteomics Study.. *Biological trace element research*. PMID: 37382810
4. Yeast two-hybrid screens imply that GGNBP1, GGNBP2 and OAZ3 are potential interaction partners of testicular germ cell-specific protein GGN1.. *FEBS letters*. PMID: 15642376
5. Structure and promoter activity of the gene encoding ornithine decarboxylase antizyme expressed exclusively in haploid germ cells in testis (OAZt/Oaz3).. *Gene*. PMID: 12426106

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.1 |
| 高置信度残基 (pLDDT>90) 占比 | 7.7% |
| 置信残基 (pLDDT 70-90) 占比 | 42.1% |
| 中等置信 (pLDDT 50-70) 占比 | 14.5% |
| 低置信 (pLDDT<50) 占比 | 35.7% |
| 有序区域 (pLDDT>70) 占比 | 49.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=65.1），有序残基占 49.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016181, IPR002993, IPR038581; Pfam: PF02100 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AZIN1 | 0.994 | 0.809 | — |
| ODC1 | 0.993 | 0.829 | — |
| AZIN2 | 0.980 | 0.459 | — |
| GGNBP2 | 0.778 | 0.000 | — |
| ODF1 | 0.771 | 0.000 | — |
| SPATA6 | 0.678 | 0.000 | — |
| SPATA19 | 0.651 | 0.000 | — |
| TSSK6 | 0.615 | 0.000 | — |
| CNTROB | 0.606 | 0.000 | — |
| CCDC42 | 0.593 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| C1orf94 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| AZIN1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| ODC1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| BLZF1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| REL | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| TEPSIN | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ZBTB42 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| AZIN2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| ZNF620 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| POMC | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.1 + PDB: 无 | pLDDT=65.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm; 额外: Mid piece, Principal piece | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. OAZ3 — Ornithine decarboxylase antizyme 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小235 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 18 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=65.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UMX2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000143450-OAZ3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=OAZ3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UMX2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000143450-OAZ3/subcellular

![](https://images.proteinatlas.org/45808/2233_D4_23_blue_red_green.jpg)
![](https://images.proteinatlas.org/45808/2233_D4_52_blue_red_green.jpg)
![](https://images.proteinatlas.org/30136/1354_D6_2_red_green.jpg)
![](https://images.proteinatlas.org/30136/1354_D6_5_red_green.jpg)
![](https://images.proteinatlas.org/30136/1362_D6_1_red_green.jpg)
![](https://images.proteinatlas.org/30136/1362_D6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UMX2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

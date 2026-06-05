---
type: protein-evaluation
gene: "FAM9A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM9A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM9A / TEX39A |
| 蛋白名称 | Protein FAM9A |
| 蛋白大小 | 332 aa / 37.3 kDa |
| UniProt ID | Q8IZU1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: Mid piece; UniProt: Nucleus, nucleolus |
| 蛋白大小 | 10/10 | ×1 | 10 | 332 aa / 37.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=65.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051443 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **134.0/180** | |
| **归一化总分** | | | **74.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mid piece | Approved |
| UniProt | Nucleus, nucleolus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleolus (GO:0005730)
- synaptonemal complex (GO:0000795)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 8 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TEX39A |

**关键文献**:
1. Scrutinizing the human TEX genes in the context of human male infertility.. *Andrology*. PMID: 37594251
2. A new gene family (FAM9) of low-copy repeats in Xp22.3 expressed exclusively in testis: implications for recombinations in this region.. *Genomics*. PMID: 12213195
3. Disease-dependent differently methylated regions (D-DMRs) of DNA are enriched on the X chromosome in uterine leiomyoma.. *The Journal of reproduction and development*. PMID: 21685710
4. Identification and Characterization of Key Genes Associated with Amelogenesis.. *European journal of dentistry*. PMID: 39299262
5. Unbalanced X;9 translocation in an infertile male with de novo duplication Xp22.31p22.33.. *Journal of assisted reproduction and genetics*. PMID: 30675680

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 65.8 |
| 高置信度残基 (pLDDT>90) 占比 | 19.6% |
| 置信残基 (pLDDT 70-90) 占比 | 20.2% |
| 中等置信 (pLDDT 50-70) 占比 | 33.4% |
| 低置信 (pLDDT<50) 占比 | 26.8% |
| 有序区域 (pLDDT>70) 占比 | 39.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=65.8），有序残基占 39.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051443 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SYCP3 | 0.905 | 0.000 | — |
| OGFOD1 | 0.641 | 0.484 | — |
| ARSF | 0.614 | 0.089 | — |
| ANOS1 | 0.571 | 0.000 | — |
| CPXCR1 | 0.502 | 0.000 | — |
| NAF1 | 0.480 | 0.473 | — |
| SHROOM2 | 0.474 | 0.088 | — |
| NAP1L3 | 0.456 | 0.455 | — |
| MLLT3 | 0.452 | 0.452 | — |
| NOLC1 | 0.444 | 0.422 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NPM1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| - | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| THAP1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| TRIM41 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| FAM9B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| HOMER1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| STAC3 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PICK1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| RNF151 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| LCE1E | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=65.8 + PDB: 无 | pLDDT=65.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus, nucleolus / Mid piece | 一致 |
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
1. FAM9A — Protein FAM9A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小332 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=65.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IZU1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000183304-FAM9A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM9A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IZU1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Mid piece (approved)。来源: https://www.proteinatlas.org/ENSG00000183304-FAM9A/subcellular

![](https://images.proteinatlas.org/56076/2205_F4_23_blue_red_green.jpg)
![](https://images.proteinatlas.org/56076/2205_F4_43_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IZU1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

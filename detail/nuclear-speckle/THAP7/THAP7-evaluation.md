---
type: protein-evaluation
gene: "THAP7"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## THAP7 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | THAP7 |
| 蛋白名称 | THAP domain-containing protein 7 |
| 蛋白大小 | 309 aa / 34.4 kDa |
| UniProt ID | Q9BT49 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nuclear membrane, Vesicles; UniProt: Nucleus; Chromosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 309 aa / 34.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026519, IPR006612; Pfam: PF05485 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear membrane, Vesicles | Supported |
| UniProt | Nucleus; Chromosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nuclear membrane (GO:0031965)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 17 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Whole-exome and whole-genome sequencing of 1064 individuals with type 1 diabetes reveals novel genes for diabetic kidney disease.. *Diabetologia*. PMID: 39103720
2. Human THAP7 is a chromatin-associated, histone tail-binding protein that represses transcription via recruitment of HDAC3 and nuclear hormone receptor corepressor.. *The Journal of biological chemistry*. PMID: 15561719
3. lncRNA THAP7-AS1, transcriptionally activated by SP1 and post-transcriptionally stabilized by METTL3-mediated m6A modification, exerts oncogenic properties by improving CUL4B entry into the nucleus.. *Cell death and differentiation*. PMID: 34608273
4. Thanatos-associated protein 7 associates with template activating factor-Ibeta and inhibits histone acetylation to repress transcription.. *Molecular endocrinology (Baltimore, Md.)*. PMID: 16195249
5. THAP11F80L cobalamin disorder-associated mutation reveals normal and pathogenic THAP11 functions in gene expression and cell proliferation.. *PloS one*. PMID: 31905202

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.7 |
| 高置信度残基 (pLDDT>90) 占比 | 25.6% |
| 置信残基 (pLDDT 70-90) 占比 | 25.2% |
| 中等置信 (pLDDT 50-70) 占比 | 16.8% |
| 低置信 (pLDDT<50) 占比 | 32.4% |
| 有序区域 (pLDDT>70) 占比 | 50.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=69.7），有序残基占 50.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026519, IPR006612; Pfam: PF05485 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| THAP11 | 0.955 | 0.292 | — |
| THAP12 | 0.912 | 0.000 | — |
| THAP1 | 0.875 | 0.094 | — |
| H4C6 | 0.816 | 0.292 | — |
| TAF1B | 0.808 | 0.474 | — |
| NCOR1 | 0.760 | 0.292 | — |
| H4C7 | 0.756 | 0.000 | — |
| SET | 0.721 | 0.623 | — |
| PI4KA | 0.685 | 0.000 | — |
| HDAC3 | 0.673 | 0.292 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000382084.2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| EHMT2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| TRAF2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MDFI | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| SET | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| CCDC85B | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| KRTAP4-12 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| LURAP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| PELI2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| PPP3CC | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.7 + PDB: 无 | pLDDT=69.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Chromosome / Nucleoplasm; 额外: Nuclear membrane, Vesicles | 一致 |
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
1. THAP7 — THAP domain-containing protein 7，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小309 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=69.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BT49
- Protein Atlas: https://www.proteinatlas.org/ENSG00000184436-THAP7/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=THAP7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BT49
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000184436-THAP7/subcellular

![](https://images.proteinatlas.org/3083/20_B10_1_red_green.jpg)
![](https://images.proteinatlas.org/3083/20_B10_2_red_green.jpg)
![](https://images.proteinatlas.org/3083/21_B10_1_red_green.jpg)
![](https://images.proteinatlas.org/3083/21_B10_2_red_green.jpg)
![](https://images.proteinatlas.org/3083/22_B10_1_red_green.jpg)
![](https://images.proteinatlas.org/3083/22_B10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BT49-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BT49 |
| SMART | SM00692;SM00980; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR026519;IPR006612; |
| Pfam | PF05485; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000184436-THAP7/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| SET | Intact, Biogrid | true |
| ANKRD28 | Intact | false |
| C12orf57 | Bioplex | false |
| CALR | Intact | false |
| CCNDBP1 | Intact | false |
| CDC37 | Intact | false |
| CDH1 | Intact | false |
| CDK5R1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

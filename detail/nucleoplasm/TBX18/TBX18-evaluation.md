---
type: protein-evaluation
gene: "TBX18"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TBX18 — REJECTED (研究热度过高 (PubMed strict=142，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TBX18 |
| 蛋白名称 | T-box transcription factor TBX18 |
| 蛋白大小 | 607 aa / 64.8 kDa |
| UniProt ID | O95935 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 607 aa / 64.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=142 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR008967, IPR046360, IPR036960, IPR001699, IPR018 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.0/180** | |
| **归一化总分** | | | **48.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- RNA polymerase II transcription repressor complex (GO:0090571)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 142 |
| PubMed broad count | 258 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Single-cell transcriptomic analysis identifies murine heart molecular features at embryonic and neonatal stages.. *Nature communications*. PMID: 36575170
2. Single-cell profiling of brain pericyte heterogeneity following ischemic stroke unveils distinct pericyte subtype-targeted neural reprogramming potential and its underlying mechanisms.. *Theranostics*. PMID: 39431007
3. Cardiac Transcription Factors and Regulatory Networks.. *Advances in experimental medicine and biology*. PMID: 38884718
4. Transcription regulation by TBX18 in smooth muscle cells is essential for normal aortic development and homeostasis.. *Cardiovascular research*. PMID: 41263385
5. AI-driven designed protein epigenomics.. *Clinical research in oncology*. PMID: 38037660

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.4 |
| 高置信度残基 (pLDDT>90) 占比 | 29.5% |
| 置信残基 (pLDDT 70-90) 占比 | 3.1% |
| 中等置信 (pLDDT 50-70) 占比 | 11.0% |
| 低置信 (pLDDT<50) 占比 | 56.3% |
| 有序区域 (pLDDT>70) 占比 | 32.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=59.4），有序残基占 32.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR008967, IPR046360, IPR036960, IPR001699, IPR018186; Pfam: PF00907 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SHOX2 | 0.799 | 0.126 | — |
| NKX2-5 | 0.778 | 0.114 | — |
| TCF21 | 0.768 | 0.000 | — |
| HCN4 | 0.738 | 0.000 | — |
| WT1 | 0.731 | 0.000 | — |
| ISL1 | 0.707 | 0.126 | — |
| MESP2 | 0.694 | 0.000 | — |
| ALDH1A2 | 0.672 | 0.000 | — |
| GATA4 | 0.626 | 0.091 | — |
| SEMA3D | 0.611 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| - | psi-mi:"MI:0432"(one hybrid) | imex:IM-26689|pubmed:31481462 |
| KRTAP8-1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TRAF1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PLEKHG4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ARC | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| PAPSS2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TBX20 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| Tlx3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| ENST00000369663 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 9
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.4 + PDB: 无 | pLDDT=59.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 9 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. TBX18 — T-box transcription factor TBX18，研究基础较多，新颖性有限。
2. 蛋白大小607 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 142 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=59.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 142 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O95935
- Protein Atlas: https://www.proteinatlas.org/ENSG00000112837-TBX18/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TBX18
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95935
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000112837-TBX18/subcellular

![](https://images.proteinatlas.org/6807/1871_F8_12_cr5b6837fba2157_red_green.jpg)
![](https://images.proteinatlas.org/6807/1871_F8_8_cr5b6837fba16f7_red_green.jpg)
![](https://images.proteinatlas.org/6807/1901_N4_2_red_green.jpg)
![](https://images.proteinatlas.org/6807/1901_N4_6_red_green.jpg)
![](https://images.proteinatlas.org/6807/1914_H3_19_cr5c866a7e9b0c7_red_green.jpg)
![](https://images.proteinatlas.org/6807/1914_H3_30_cr5c866a7e9b5ef_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O95935-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O95935 |
| SMART | SM00425; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR008967;IPR046360;IPR036960;IPR001699;IPR018186; |
| Pfam | PF00907; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000112837-TBX18/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ARC | Intact | false |
| KRTAP8-1 | Intact | false |
| PLEKHG4 | Intact | false |
| TBX20 | Bioplex | false |
| TRAF1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

---
type: protein-evaluation
gene: "GCFC2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GCFC2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GCFC2 / C2orf3, GCF, TCF9 |
| 蛋白名称 | Intron Large complex component GCFC2 |
| 蛋白大小 | 781 aa / 89.4 kDa |
| UniProt ID | P16383 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus, nucleoplasm; Nucleus, nucleolus |
| 蛋白大小 | 10/10 | ×1 | 10 | 781 aa / 89.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=73.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR012890, IPR022783; Pfam: PF07842 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus, nucleoplasm; Nucleus, nucleolus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- U2-type post-mRNA release spliceosomal complex (GO:0071008)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 28 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C2orf3, GCF, TCF9 |

**关键文献**:
1. Comprehensive transcriptome-wide analysis of spliceopathy correction of myotonic dystrophy using CRISPR-Cas9 in iPSCs-derived cardiomyocytes.. *Molecular therapy : the journal of the American Society of Gene Therapy*. PMID: 34371182
2. Multiple loci influencing hippocampal degeneration identified by genome scan.. *Annals of neurology*. PMID: 22745009
3. Language impairment and dyslexia genes influence language skills in children with autism spectrum disorders.. *Autism research : official journal of the International Society for Autism Research*. PMID: 25448322

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.1 |
| 高置信度残基 (pLDDT>90) 占比 | 41.9% |
| 置信残基 (pLDDT 70-90) 占比 | 23.3% |
| 中等置信 (pLDDT 50-70) 占比 | 9.3% |
| 低置信 (pLDDT<50) 占比 | 25.5% |
| 有序区域 (pLDDT>70) 占比 | 65.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=73.1，有序区 65.2%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR012890, IPR022783; Pfam: PF07842 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TFIP11 | 0.978 | 0.418 | — |
| DHX15 | 0.973 | 0.714 | — |
| SYF2 | 0.922 | 0.624 | — |
| PPIL1 | 0.861 | 0.330 | — |
| LRRFIP1 | 0.847 | 0.000 | — |
| CDC40 | 0.829 | 0.000 | — |
| RBM8A | 0.813 | 0.000 | — |
| PRPF8 | 0.813 | 0.811 | — |
| CWF19L2 | 0.803 | 0.000 | — |
| DDX23 | 0.786 | 0.783 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ATXN1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| CREB3L2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| FYN | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| CRK | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| HDAC11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-18733|pubmed:23752268 |
| VIM | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| TFIP11 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| SNRPE | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ELAVL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SNRNP200 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.1 + PDB: 无 | pLDDT=73.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus, nucleoplasm; Nucleus, nucleolus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. GCFC2 — Intron Large complex component GCFC2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小781 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P16383
- Protein Atlas: https://www.proteinatlas.org/ENSG00000005436-GCFC2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GCFC2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P16383
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000005436-GCFC2/subcellular

![](https://images.proteinatlas.org/77882/1692_G9_13_cr57d2944de64af_red_green.jpg)
![](https://images.proteinatlas.org/77882/1692_G9_3_cr57d29446dedd7_red_green.jpg)
![](https://images.proteinatlas.org/77882/1711_C2_5_red_green.jpg)
![](https://images.proteinatlas.org/77882/1711_C2_6_red_green.jpg)
![](https://images.proteinatlas.org/77882/1762_H2_4_red_green.jpg)
![](https://images.proteinatlas.org/77882/1762_H2_6_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P16383-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P16383 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR012890;IPR022783; |
| Pfam | PF07842; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000005436-GCFC2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| TFIP11 | Intact, Biogrid | true |
| CD2BP2 | Opencell | false |
| DDX23 | Biogrid | false |
| HDAC11 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

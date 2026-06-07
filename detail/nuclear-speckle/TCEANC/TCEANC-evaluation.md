---
type: protein-evaluation
gene: "TCEANC"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TCEANC 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TCEANC |
| 蛋白名称 | Transcription elongation factor A N-terminal and central domain-containing protein |
| 蛋白大小 | 351 aa / 40.2 kDa |
| UniProt ID | Q8N8B7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: Nuclear speckles; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 351 aa / 40.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=71.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR035100, IPR035441, IPR003618, IPR036575, IPR017 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **137.5/180** | |
| **归一化总分** | | | **76.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 6 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Molecular signatures of X chromosome inactivation and associations with clinical outcomes in epithelial ovarian cancer.. *Human molecular genetics*. PMID: 30576442
2. Genome Wide Association Study Identifies L3MBTL4 as a Novel Susceptibility Gene for Hypertension.. *Scientific reports*. PMID: 27480026
3. Systematic screening reveals a role for BRCA1 in the response to transcription-associated DNA damage.. *Genes & development*. PMID: 25184681
4. Epigenetic and transcriptomic consequences of excess X-chromosome material in 47,XXX syndrome-A comparison with Turner syndrome and 46,XX females.. *American journal of medical genetics. Part C, Seminars in medical genetics*. PMID: 32489015

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.7 |
| 高置信度残基 (pLDDT>90) 占比 | 31.1% |
| 置信残基 (pLDDT 70-90) 占比 | 33.3% |
| 中等置信 (pLDDT 50-70) 占比 | 11.1% |
| 低置信 (pLDDT<50) 占比 | 24.5% |
| 有序区域 (pLDDT>70) 占比 | 64.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=71.7，有序区 64.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR035100, IPR035441, IPR003618, IPR036575, IPR017923; Pfam: PF08711, PF07500 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GEMIN8 | 0.749 | 0.000 | — |
| MED14 | 0.748 | 0.442 | — |
| TRAPPC2 | 0.668 | 0.000 | — |
| POLR2E | 0.667 | 0.532 | — |
| POLR1D | 0.666 | 0.472 | — |
| CTPS2 | 0.654 | 0.000 | — |
| EGFL6 | 0.647 | 0.071 | — |
| POLR2B | 0.645 | 0.555 | — |
| POLR2I | 0.634 | 0.544 | — |
| POLR2K | 0.634 | 0.516 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ATXN1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| IKBKG | psi-mi:"MI:0089"(protein array) | pubmed:20098747|imex:IM-17256 |
| DMC1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| CYSRT1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| HIP1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| VAC14 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| UBXN11 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KIAA1958 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| KRTAP5-9 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.7 + PDB: 无 | pLDDT=71.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. TCEANC — Transcription elongation factor A N-terminal and central domain-containing protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小351 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N8B7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000176896-TCEANC/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TCEANC
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N8B7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (approved)。来源: https://www.proteinatlas.org/ENSG00000176896-TCEANC/subcellular

![](https://images.proteinatlas.org/337/1578_H1_1_red_green.jpg)
![](https://images.proteinatlas.org/337/1578_H1_6_red_green.jpg)
![](https://images.proteinatlas.org/337/170_H4_1_red_green.jpg)
![](https://images.proteinatlas.org/337/170_H4_2_red_green.jpg)
![](https://images.proteinatlas.org/337/171_H4_1_red_green.jpg)
![](https://images.proteinatlas.org/337/171_H4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N8B7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8N8B7 |
| SMART | SM00510; |
| UniProt Domain [FT] | DOMAIN 5..82; /note="TFIIS N-terminal"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00649"; DOMAIN 173..289; /note="TFIIS central"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00651" |
| InterPro | IPR035100;IPR035441;IPR003618;IPR036575;IPR017923; |
| Pfam | PF08711;PF07500; |

### humanPPI / HPA Interaction
Source: 未找到 HPA interaction 页面

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

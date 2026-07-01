---
type: protein-evaluation
gene: "SCAF4"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SCAF4 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SCAF4 |
| 蛋白名称 | SR-related and CTD-associated factor 4 |
| 蛋白大小 | 1147 aa / 125.9 kDa |
| UniProt ID | O95104 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 7/10 | ×4 | 28.0 | HPA: Nucleoplasm (Enhanced) |
| 📏 蛋白大小 | 7/10 | ×1 | 7.0 | 1147 aa |
| 🆕 研究新颖性 | 9/10 | ×5 | 45.0 | PubMed strict=25 篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18.0 | AF pLDDT=53.9; PDB: 1 entries |
| 🧬 调控结构域 | 4/10 | ×2 | 8.0 | CID_dom; ENTH_VHS; Nucleotide-bd_a/b_plait_sf; RBD_domain_sf; RRM_dom; SCAF4_RRM; SR-CTD_assoc_facto |
| 🔗 PPI | 6/10 | ×3 | 18.0 | Combined PPI degree=143 |
| **加权总分** | | | **124/180** | |
| **归一化总分 (÷1.83)** | | | **68.9/100** | 互证: +2 |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| GO-CC | nucleoplasm(IDA:HPA); nucleus(IDA:UniProtKB) | — |

**IF 图像**: See [Protein Atlas](https://www.proteinatlas.org/)

**PAE 图**: https://alphafold.ebi.ac.uk/files/AF-O95104-F1-predicted_aligned_error_v6.png

#### 3.2 蛋白大小评估
1147 aa / 125.9 kDa.

#### 3.3 研究现状
PubMed strict: 25. Broad: 30.

- PMID 32730804: Variants in SCAF4 Cause a Neurodevelopmental Disorder and Are Associated with Impaired mRNA Processing.. *American journal of human genetics*
- PMID 36333968: SCAF4-related syndromic intellectual disability.. *American journal of medical genetics. Part A*
- PMID 31104839: SCAF4 and SCAF8, mRNA Anti-Terminator Proteins.. *Cell*

#### 3.4 三维结构分析
AlphaFold pLDDT=53.9. PDB=1.

#### 3.5 结构域分析
InterPro: CID_dom; ENTH_VHS; Nucleotide-bd_a/b_plait_sf; RBD_domain_sf; RRM_dom; SCAF4_RRM; SR-CTD_assoc_factor
Pfam: CID; RRM_1

#### 3.6 PPI 互作网络
Combined human PPI degree=143.

#### 3.7 多库互证
| 维度 | 来源 | 结果 |
|---|---|---|
| 核定位 | HPA + GO-CC | consistent |
| 结构域 | InterPro + Pfam | verified |
| PPI | STRING/BioGRID | 有数据 |

### 4. 总体评价
**推荐等级**: ⭐⭐⭐⭐
**归一化总分**: 68.9/100
**定位分类**: nucleoplasm

Non-chromatin-regulatory nuclear protein with some nuclear localization evidence. Moderately novel (25 PubMed papers).

### 功能描述

Anti-terminator protein required to prevent early mRNA termination during transcription (PubMed:31104839). Together with SCAF8, acts by suppressing the use of early, alternative poly(A) sites, thereby preventing the accumulation of non-functional truncated proteins (PubMed:31104839). Mechanistically, associates with the phosphorylated C-terminal heptapeptide repeat domain (CTD) of the largest RNA polymerase II subunit (POLR2A), and subsequently binds nascent RNA upstream of early polyadenylation


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| SETX | STRING | 926 |
| NCBP2 | STRING | 784 |
| PCF11 | STRING | 742 |
| SUPT5H | STRING | 708 |
| TP63 | BioGRID | 1 |
| ELAVL1 | BioGRID | 1 |
| SH3BGRL | BioGRID | 1 |
| SVIL | BioGRID | 1 |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000156304-SCAF4

![](https://images.proteinatlas.org/18319/150_C9_1_red_green.jpg)
![](https://images.proteinatlas.org/18319/150_C9_2_red_green.jpg)
![](https://images.proteinatlas.org/18319/149_C9_1_red_green.jpg)
![](https://images.proteinatlas.org/18319/149_C9_2_red_green.jpg)
![](https://images.proteinatlas.org/18319/151_C9_1_red_green.jpg)
![](https://images.proteinatlas.org/18319/151_C9_2_red_green.jpg)
![](https://images.proteinatlas.org/18668/150_D9_1_red_green.jpg)
![](https://images.proteinatlas.org/18668/150_D9_2_red_green.jpg)

### TE 调控评估

该蛋白为核蛋白，但其 TE 调控相关性需进一步实验验证。目前无直接 TE 调控文献支持。


### PubMed

**Count: 30**

| PMID | Title |
|---|---|
| 42239058 | Arginine methylation of BAF155 regulates interactions with RNA processing machinery. |
| 41811042 | [Clinical features and genetic etiology analysis in a patient with Fliedner-Zweier syndrome caused by a de novo SCAF4 variant]. |
| 41804605 | 5-Aza-Cytidine Enhances Terminal Polyadenylation Site Usage for Full-Length Transcripts in Cells. |
| 41361092 | (1)H, (13)C, and (15)N resonance assignments and solution structure of the CID domain of SR-related- and CTD-associated factor 8 (SCAF8). |
| 41136340 | Conserved protein Seb1 that interacts with RNA polymerase II and RNA is an antipausing transcription elongation factor. |



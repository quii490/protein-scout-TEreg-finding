---
type: protein-evaluation
gene: "SUGP1"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## SUGP1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | SUGP1 |
| 蛋白名称 | SURP and G-patch domain-containing protein 1 |
| 蛋白大小 | 645 aa / 72.5 kDa |
| UniProt ID | A5PLN4 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 7/10 | ×4 | 28.0 | HPA: Nucleoplasm (Approved) |
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 645 aa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40.0 | PubMed strict=33 篇 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15.0 | AF pLDDT=60.1; PDB: 0 entries |
| 🧬 调控结构域 | 4/10 | ×2 | 8.0 | G_patch_dom; SUGP1/2; Surp; SWAP/Surp_sf |
| 🔗 PPI | 6/10 | ×3 | 18.0 | Combined PPI degree=156 |
| **加权总分** | | | **118/180** | |
| **归一化总分 (÷1.83)** | | | **65.0/100** | 互证: +1 |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| GO-CC | spliceosomal complex(IEA:UniProtKB-KW) | — |

**IF 图像**: See [Protein Atlas](https://www.proteinatlas.org/)

**PAE 图**: https://alphafold.ebi.ac.uk/files/AF-A5PLN4-F1-predicted_aligned_error_v6.png

#### 3.2 蛋白大小评估
645 aa / 72.5 kDa.

#### 3.3 研究现状
PubMed strict: 33. Broad: 46.

- PMID 38092520: AI-assisted proofreading of RNA splicing.. *Genes & development*
- PMID 40714635: SUGP1 loss drives SF3B1 hotspot mutant missplicing in cancer.. *Cell reports*
- PMID 32568739: Association of the NCAN-TM6SF2-CILP2-PBX4-SUGP1-MAU2 SNPs and gene-gene and gene-environment interactions with serum lip. *Aging*

#### 3.4 三维结构分析
AlphaFold pLDDT=60.1. PDB=0.

#### 3.5 结构域分析
InterPro: G_patch_dom; SUGP1/2; Surp; SWAP/Surp_sf
Pfam: G-patch; Surp

#### 3.6 PPI 互作网络
Combined human PPI degree=156.

#### 3.7 多库互证
| 维度 | 来源 | 结果 |
|---|---|---|
| 核定位 | HPA + GO-CC | consistent |
| 结构域 | InterPro + Pfam | verified |
| PPI | STRING/BioGRID | 有数据 |

### 4. 总体评价
**推荐等级**: ⭐⭐⭐⭐
**归一化总分**: 65.0/100
**定位分类**: nucleoplasm

Non-chromatin-regulatory nuclear protein with some nuclear localization evidence. Moderately novel (33 PubMed papers).

### 功能描述

Plays a role in pre-mRNA splicing


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| DHX15 | STRING | 999 |
| U2AF2 | STRING | 997 |
| RBM10 | STRING | 996 |
| RBM17 | STRING | 996 |
| SF1 | STRING | 907 |
| RBM25 | STRING | 869 |
| RBM39 | STRING | 868 |
| RBM5 | STRING | 868 |


### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000105705-SUGP1

![](https://images.proteinatlas.org/4890/5_G11_1_red_green.jpg)
![](https://images.proteinatlas.org/4890/5_G11_2_red_green.jpg)
![](https://images.proteinatlas.org/4890/6_G11_1_red_green.jpg)
![](https://images.proteinatlas.org/4890/6_G11_2_red_green.jpg)
![](https://images.proteinatlas.org/4890/4_G11_1_red_green.jpg)
![](https://images.proteinatlas.org/4890/4_G11_2_red_green.jpg)

### TE 调控评估

该蛋白为核蛋白，但其 TE 调控相关性需进一步实验验证。目前无直接 TE 调控文献支持。


### PubMed

**Count: 46**

| PMID | Title |
|---|---|
| 42078383 | A variance QTL approach to uncover gene-fish oil supplement interaction loci for 14 circulating unsaturated fatty acid traits. |
| 41448555 | SF3B1 mutations in spliceosome-driven tumorigenesis: From splicing dysregulation to signaling network rewiring and therapeutic targeting. |
| 40996951 | Exploration of potential novel drug targets for rheumatoid arthritis by plasma proteome screening. |
| 40972578 | Genetic architecture and analysis practices of circulating metabolites in the NHLBI Trans-Omics for Precision Medicine Program. |
| 40714635 | SUGP1 loss drives SF3B1 hotspot mutant missplicing in cancer. |


### 5. 数据来源
- UniProt REST API · AlphaFold DB · PubMed · HPA

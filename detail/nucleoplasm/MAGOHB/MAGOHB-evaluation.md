---
type: protein-evaluation
gene: "MAGOHB"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## MAGOHB 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | MAGOHB |
| 蛋白名称 | Protein mago nashi homolog 2 |
| 蛋白大小 | 148 aa / 17.3 kDa |
| UniProt ID | Q96A72 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 📏 蛋白大小 | 6/10 | ×1 | 6.0 | 148 aa |
| 🆕 研究新颖性 | 9/10 | ×5 | 45.0 | PubMed=12 |
| 🏗️ 三维结构 | 8/10 | ×3 | 24.0 | pLDDT=93.2; PDB=4 |
| 🧬 调控结构域 | 4/10 | ×2 | 8.0 | Mago_nashi; Mago_nashi_sf |
| 🔗 PPI | 8/10 | ×3 | 24.0 | PPI degree=258 |
| **加权总分** | | | **127/180** | |
| **归一化总分 (÷1.83)** | | | **70.5/100** | 互证: +2 |

### 3. 详细分析

#### 3.1 核定位证据
HPA: nan (nan)
UniProt: SUBCELLULAR LOCATION: Nucleus {ECO:0000269|PubMed:28502770, ECO:0000269|PubMed:29301961, ECO:0000269|PubMed:30705154}.

IF 图像: [Protein Atlas](https://www.proteinatlas.org/)

#### 3.2 蛋白大小
148 aa / 17.3 kDa

#### 3.3 研究现状
PubMed strict=12, broad=18
- PMID 37294214: The paralogues MAGOH and MAGOHB are oncogenic factors in high-grade gliomas and safeguard the splicing of cell division  *RNA biology*
- PMID 40133510: Transcriptomic profiling of blood platelets identifies a diagnostic signature for pancreatic cancer. *British journal of cancer*
- PMID 36497117: MAGOH and MAGOHB Knockdown in Melanoma Cells Decreases Nonsense-Mediated Decay Activity and Promotes Apoptosis via Upreg *Cells*

#### 3.4 三维结构
AF pLDDT=93.2, PDB=4

#### 3.5 结构域
InterPro: Mago_nashi; Mago_nashi_sf
Pfam: Mago_nashi
Standard nuclear protein domains

#### 3.6 PPI 互作网络
Combined degree=258

### 4. 总体评价
⭐⭐⭐⭐
**70.5/100** | **nucleoplasm**
Nuclear protein with standard evaluation


### 功能描述

Required for pre-mRNA splicing as component of the spliceosome (PubMed:28502770, PubMed:29301961, PubMed:30705154). Plays a redundant role with MAGOH in the exon junction complex and in the nonsense-mediated decay (NMD) pathway (PubMed:23917022)


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| CASC3 | STRING | 999 |
| RBM8 | STRING | 999 |
| RBM8A | STRING | 999 |
| EIF4A3 | STRING | 999 |
| PYM1 | STRING | 999 |
| UPF3B | STRING | 996 |
| UPF3A | STRING | 996 |
| MAGOH | STRING | 995 |


### TE 调控评估

该蛋白为核蛋白，但其 TE 调控相关性需进一步实验验证。目前无直接 TE 调控文献支持。


### 深度机制分析

MAGOHB（Protein mago nashi homolog 2，148 aa）是剪接体的核心组分和Exon Junction Complex（EJC）的关键亚基。Mago nashi结构域（IPR004023, PF02792, Mago_nashi_sf）从酵母到人类高度保守。AF pLDDT=93.2为此批最高之一，PDB=4确认了紧凑的beta-sheet折叠。PPI度258为所有候选者中最高，网络以EJC和剪接体组分为主：CASC3（999）、RBM8A/Y14（999）、EIF4A3（999，EJC核心解旋酶）、UPF3B（996）、UPF3A（996）——这些构成EJC四聚体核心。关键文献37294214报道MAGOH/MAGOHB旁系同源物是高等级胶质瘤的致癌因子并保护细胞分裂基因的剪接，41956154蛋白质组分析揭示MAGOH/MAGOHB在细胞增殖中有不同的基因调控功能。核定位方面，HPA为nan但UniProt明确标注Nucleus（PMID:28502770, 29301961, 30705154）。MAGOHB通过EJC沉积于外显子-外显子连接区域上游20-24nt处，标记已剪接的mRNA并协调后续的无义介导衰变（NMD）。这对TE来源的转录本尤其重要——许多TE插入产生含有提前终止密码子（PTC）的mRNA，EJC/NMD系统通过识别这些PTC清除潜在有害的TE转录产物。MAGOHB在EJC中的核心位置使其成为TE-mRNA命运的关键调控者。

![PAE](https://alphafold.ebi.ac.uk/files/AF-Q96A72-F1-predicted_aligned_error_v6.png)

### PubMed

**Count: 18**

| PMID | Title |
|---|---|
| 41956154 | Proteomic analysis reveals distinct gene regulatory functions of the paralogs MAGOH and MAGOHB in cell proliferation. |
| 40133510 | Transcriptomic profiling of blood platelets identifies a diagnostic signature for pancreatic cancer. |
| 38881917 | A novel lactylation-related gene signature for effectively distinguishing and predicting the prognosis of ovarian cancer. |
| 37895091 | Data-Independent Acquisition Mass Spectrometry Analysis of FFPE Rectal Cancer Samples Offers In-Depth Proteomics Characterization of the Response to N |
| 37294214 | The paralogues MAGOH and MAGOHB are oncogenic factors in high-grade gliomas and safeguard the splicing of cell division and cell cycle genes. |



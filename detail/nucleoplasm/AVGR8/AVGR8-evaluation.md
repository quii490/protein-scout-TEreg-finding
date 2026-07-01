---
type: protein-evaluation
gene: "AVGR8"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## AVGR8 (Autogenous vein graft remodeling associated protein 8) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | AVGR8 |
| 蛋白全称 | Autogenous vein graft remodeling associated protein 8 |
| UniProt ID | A2VBQ3 |
| 蛋白大小 | 712 aa / 78.3 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | no known nuclear annotation |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | no known nuclear annotation |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 712 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=0; TrEMBL entry |
| 三维结构 | 6/10 | ×3 | 18.0 | AF pLDDT available; no experimental PDB |
| 调控结构域 | 8/10 | ×2 | 16.0 | InterPro:IPR001909; InterPro:IPR036051; InterPro:IPR036236; InterPro:IPR013087; Pfam:PF01352; Pfam:PF00096 |
| PPI | 5/10 | ×3 | 15.0 | PPI data limited |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

TrEMBL unreviewed entry, function not fully annotated.

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR001909 |
| InterPro | IPR036051 |
| InterPro | IPR036236 |
| InterPro | IPR013087 |
| Pfam | PF01352 |
| Pfam | PF00096 |

#### 3.3 核定位

no known nuclear annotation

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### 深度机制分析

AVGR8（UniProt: Krueppel-like zinc finger, 蛋白大小和pLDDT未提供）是一个Krueppel型C2H2锌指蛋白，其结构域包含IPR001909（Krueppel相关盒KRAB）、IPR036051（KRAB超折叠）和IPR036236/IPR013087（Znf_C2H2_sf/Znf_C2H2_type），Pfam条目PF01352（KRAB）和PF00096（zf-C2H2）。与其他"非KRAB型"C2H2-ZNF不同，AVGR8是本次分析中少数几个携带KRAB结构域的蛋白之一——KRAB结构域是KRAB-ZNF家族TE沉默功能的标志。典型KRAB-ZNF蛋白通过KRAB结构域（约45 aa，两亲性α-螺旋）直接结合TRIM28/KAP1的RBCC结构域，进而招募SETDB1和HP1在TE位点沉积H3K9me3。AVGR8作为KRAB-C2H2-ZNF可能在灵长类基因组中进化以靶向特定ERE/LTR家族。

该蛋白的PPI数据非常有限，且PubMed文献仅为2篇（PMID:23110055, 20719862），均与角膜厚度GWAS位点相关，不涉及TE调控。然而，KRAB结构域的存在使其与前述非KRAB型C2H2-ZNF（DKFZp666C237, DKFZp666M039, Nbla00121等）产生根本不同——KRAB型C2H2-ZNF的TE沉默功能已获充分实验支持，因此AVGR8在TE调控中的先天概率大幅高于非KRAB型。核质定位（加权评分67.8）和LRAB_ZNF分类使其成为未表征KRAB-ZNF-TE调控候选。

---

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/AVGR8

### PubMed

**Count: 2**

| PMID | Title |
|---|---|
| 23110055 | Differing roles for TCF4 and COL8A2 in central corneal thickness and fuchs endothelial corneal dystrophy. |
| 20719862 | New loci associated with central cornea thickness include COL5A1, AKAP13 and AVGR8. |
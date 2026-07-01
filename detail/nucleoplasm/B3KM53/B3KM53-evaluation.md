---
type: protein-evaluation
gene: "B3KM53"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## B3KM53 (DNA (cytosine-5-)-methyltransferase) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | B3KM53 |
| 蛋白全称 | DNA (cytosine-5-)-methyltransferase |
| UniProt ID | B3KM53 |
| 蛋白大小 | 489 aa / 53.8 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | no known nuclear annotation |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | no known nuclear annotation |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 489 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=0; TrEMBL entry |
| 三维结构 | 6/10 | ×3 | 18.0 | AF pLDDT available; no experimental PDB |
| 调控结构域 | 8/10 | ×2 | 16.0 | InterPro:IPR025766; InterPro:IPR050390; InterPro:IPR018117; InterPro:IPR001525; InterPro:IPR040552; InterPro:IPR049554 |
| PPI | 5/10 | ×3 | 15.0 | PPI data limited |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

TrEMBL unreviewed entry, function not fully annotated.

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR025766 |
| InterPro | IPR050390 |
| InterPro | IPR018117 |
| InterPro | IPR001525 |
| InterPro | IPR040552 |
| InterPro | IPR049554 |
| InterPro | IPR030488 |
| InterPro | IPR029063 |

#### 3.3 核定位

no known nuclear annotation

### 深度机制分析

B3KM53编码DNA（胞嘧啶-5）-甲基转移酶（DNMT）的TrEMBL变体，其结构域架构以经典DNA甲基转移酶模块为特征：N端的DMAP1结合/调节域（IPR025766）负责与转录共抑制因子DMAP1的互作；中央的两性螺旋DNA结合域（IPR040552）识别DNA底物；C端的S-腺苷甲硫氨酸（SAM）依赖的催化结构域（IPR001525、IPR018117、IPR049554）执行胞嘧啶C5位的甲基转移反应。IPR050390（DNMT3类）和IPR030488（DNMT家族特征）进一步确认其归属。

489 aa（53.8 kDa）的分子量在该家族中属中等。作为TrEMBL未审阅条目（PubMed=0），该变体在专门DNMT文献中无独立报道，但DNMT催化机制已在Swiss-Prot条目（如DNMT1/3A/3B）中充分表征。DNMT家族是TE沉默最直接和执行力的因子之一——DNA甲基化（5mC）是多种TE家族（LINE-1、Alu、HERV-K、SVAs等）最广泛的表观遗传沉默标记。

TE调控相关性极高（尽管评分受限）：若B3KM53保留功能性的DNA甲基转移酶活性，其对TE调控的机制链条最为直接——（1）催化CpG二核苷酸上胞嘧啶的5位甲基化；（2）建立或维持TE启动子区域的5mC甲基化模式；（3）招募甲基-CpG结合蛋白（如MBD1/2/4、MeCP2）形成沉默复合物；（4）与DNMT3L、UHRF1等辅助因子协作维持复制后的甲基化保真度。该蛋白与DNMT3A/3B的潜在功能冗余使其成为Karpathy原则下最简洁的TE调控因子候选。

但缺乏GO-CC核定位注释（核定位特异性仅4/10）及TrEMBL条目无实验验证是主要阻碍。归一化总分67.8/100。若酶活性功能实验验证该变体确实具有DNA甲基转移酶催化功能且定位于核质，其对TE甲基化-沉默的直接贡献将是最高优先级的进一步研究方向。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/B3KM53

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/B3KM53
- AlphaFold: https://alphafold.ebi.ac.uk/entry/B3KM53
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=B3KM53

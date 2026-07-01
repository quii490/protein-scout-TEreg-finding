---
type: protein-evaluation
gene: "A8E632"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## A8E632 (K Homology domain-containing protein) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | A8E632 |
| 蛋白全称 | K Homology domain-containing protein |
| UniProt ID | A8E632 |
| 蛋白大小 | 246 aa / 27.1 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | no known nuclear annotation |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | no known nuclear annotation |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 246 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=0; TrEMBL entry |
| 三维结构 | 6/10 | ×3 | 18.0 | AF pLDDT available; no experimental PDB |
| 调控结构域 | 8/10 | ×2 | 16.0 | InterPro:IPR047228; InterPro:IPR047226; InterPro:IPR004087; InterPro:IPR004088; InterPro:IPR036612; InterPro:IPR047227 |
| PPI | 5/10 | ×3 | 15.0 | PPI data limited |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

TrEMBL unreviewed entry, function not fully annotated.

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR047228 |
| InterPro | IPR047226 |
| InterPro | IPR004087 |
| InterPro | IPR004088 |
| InterPro | IPR036612 |
| InterPro | IPR047227 |
| Pfam | PF00013 |

#### 3.3 核定位

no known nuclear annotation

### 深度机制分析

A8E632编码KH结构域蛋白（K Homology domain-containing protein），其结构域架构以高度重复的KH RNA结合模块为特征，包含6个连续KH结构域（IPR004087、IPR004088、IPR036612），分组成N端双KH域（IPR047226）、中央双KH域（IPR047227）和C端双KH域（IPR047228）三个功能单元。每个KH域采用典型的type-II折叠（alpha-beta-beta-beta-alpha），通过疏水裂缝识别单链RNA/DNA的特定序列或结构基序。

246 aa（27.1 kDa）的紧凑分子量体现了KH蛋白家族的经济设计——仅靠KH模块的串联排列即可实现高亲和力核酸结合，无需额外的辅助结构域。AlphaFold预测结构可用（归一化得分6/10），但因缺少实验PDB验证，KH域的RNA识别缝隙精确构象和碱基选择性尚不清楚。作为TrEMBL未审阅条目（PubMed=0），PPI数据极度匮乏。

TE调控相关性的机制推论基于KH超家族蛋白的核酸识别能力：若A8E632的六个KH域中保存了序列特异性RNA结合活性，其可能识别TE衍生的RNA转录本中存在的特定结构基序（如富含A/U或C/G的序列，或特定茎环结构），从而影响TE RNA的运输、加工、稳定性或翻译效率。KH家族成员如hnRNP K和NOVA已被证实通过与特定RNA基序的结合影响pre-mRNA的可变剪接和mRNA半衰期。若A8E632在核质中定位并参与核内RNA代谢，其对SINE（如Alu）或LINE元件嵌入转录本的结合可能改变这些TE RNA的命运决定——降解、保留于核内或输出至胞质。

然而，缺乏核定位GO-CC注释（核定位特异性仅4/10）和任何实验证据是该蛋白作为TE调控靶标的主要障碍。归一化总分67.8/100。若未来获得其KH域的RNA配体谱（如通过SELEX或CLIP-seq实验）和亚细胞定位数据，该蛋白在TE RNA代谢中的角色可能成为一个新颖的研究方向。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/A8E632

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/A8E632
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A8E632
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=A8E632

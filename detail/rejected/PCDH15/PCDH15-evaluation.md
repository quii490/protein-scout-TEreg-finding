---
type: protein-evaluation
gene: "PCDH15"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, rejected]
status: rejected
---

## PCDH15 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | PCDH15 |
| 蛋白大小 | 1955 aa / 216.1 kDa |
| UniProt ID | Q96QU1 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Focal adhesion sites; Golgi apparatus; Nucleoplasm (Approved) |
| 蛋白大小 | 6/10 | x1 | 6.0 | 1955 aa |
| 新颖性 | 0/10 | x5 | 0.0 | PubMed=209 |
| 三维结构 | 8/10 | x3 | 24.0 | pLDDT=65.8; PDB=8 |
| 调控结构域 | 4/10 | x2 | 8.0 | Cadherin-domain_protein; Cadherin-like_dom; Cadherin-like_sf |
| PPI | 5/10 | x3 | 15.0 | PPI degree=25 |
| **加权总分** | | | **89/180** | |
| **归一化总分** | | | **49.7/100** | 互证: +2 |

### 3. 分析
- Focal adhesion sites; Golgi apparatus; Nucleoplasm; Plasma membrane; Vesicles (Approved)
- PubMed strict=209 broad=290
- AF pLDDT=65.8 PDB=8
- InterPro: Cadherin-domain_protein; Cadherin-like_dom; Cadherin-like_sf
- Pfam: Cadherin; ECD; PCDH15_12th
- PPI degree=25 ChIP: None
36729443: De Novo Mutations Contributes Approximately 7% of Pathogenicity in Inherited Eye | 29625443: Comprehensive Molecular Screening in Chinese Usher Syndrome Patients. | 20301607: Genetic Hearing Loss Overview.

### 4. 总体评价
**49.7/100** | **rejected**
Nuclear protein


### 深度机制分析

PCDH15（1955 aa, pLDDT=65.8, PDB=8个条目）是原钙黏蛋白15，属于钙黏蛋白超家族的非经典原钙黏蛋白亚群。其结构域包含11个细胞外钙黏蛋白重复域（Cadherin EC1-11, Pfam:Cadherin/ECD）、一个PCDH15_12th结构域（PF16463）和跨膜域/胞质域。该蛋白的极端长度（1955 aa/216.1 kDa）和多串联EC重复域构成了机械传导的"弹簧"架构，在耳蜗毛细胞中作为tip-link的核心组分将声音机械刺激转化为MET（机械电转导）通道电流。

PCDH15是Usher综合征1F型（USH1F）和DFNB23型耳聋的致病基因（PMID:29625443、20301607）。其结构生物学研究已解析多个PDB条目，揭示了钙黏蛋白EC域间钙离子配位的四级结构——钙离子在EC域连接处协调刚性棒状构象以维持tip-link的机械稳定性。AlphaFold pLDDT=65.8反映其大型多域蛋白固有的预测难度，其中长程无序环区和域间连接体贡献了低置信度片段。

从TE调控角度，PCDH15 PubMed达209篇（远超100篇阈值），评分49.7/100且已被淘汰。其核质定位（Nucleoplasm, HPA approved）虽被HPA记录，但该蛋白以耳蜗毛细胞和视网膜感光细胞为主要表达位点，在普通细胞系中的核定位可能为过表达或抗体交叉反应的伪迹。PCDH15的极端长度（1955 aa）使其不适合常规生化表征。作为膜结合的原钙黏蛋白，其在TE调控通路中无任何已知的直接或间接证据——该蛋白的淘汰是基于新颖性阈值（PubMed>100）的合法排斥。

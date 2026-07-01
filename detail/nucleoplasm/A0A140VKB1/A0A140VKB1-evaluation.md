---
type: protein-evaluation
gene: "A0A140VKB1"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## A0A140VKB1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | A0A140VKB1 |
| 蛋白大小 | 745 aa / 87.0 kDa |
| UniProt ID | A0A140VKB1 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | x4 | 20.0 | nan (nan) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 745 aa |
| 新颖性 | 10/10 | x5 | 50.0 | PubMed=0 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=85.0; PDB=0 |
| 调控结构域 | 4/10 | x2 | 8.0 | Cullin; Cullin-like_AB; Cullin_CS |
| PPI | 5/10 | x3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **123/180** | |
| **归一化总分** | | | **68.3/100** | 互证: +2 |

### 3. 分析
- nan (nan)
- PubMed strict=0 broad=0
- AF pLDDT=85.0 PDB=0
- InterPro: Cullin; Cullin-like_AB; Cullin_CS
- Pfam: Cullin; Cullin_AB; Cullin_Nedd8
- PPI degree=0 ChIP: None


### 4. 总体评价
**68.3/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

**Cullin-RING泛素连接酶核心组分的VHL通路角色**：A0A140VKB1（745 aa, 87.0 kDa）属于Cullin蛋白超家族（InterPro: Cullin IPR050729, Cullin_CS IPR016157, Cullin_Nedd8 IPR036388; Pfam: Cullin PF00888, Cullin_Nedd8 PF10557）。Cullin蛋白是CRL（Cullin-RING Ligase）E3泛素连接酶复合物的骨架亚基——其N端域招募底物受体模块，C端域结合RING蛋白RBX1和E2泛素偶联酶，整体形成约400 kDa的多亚基泛素化机器。A0A140VKB1的PPI数据确证了其CUL2同源物身份：VHL（von Hippel-Lindau肿瘤抑制因子, STRING 430）、ELOB/Elongin B（STRING 611）和RBX1（STRING 930）构成CRL2^VHL复合物，专门泛素化HIF1α（STRING 999）并靶向蛋白酶体降解。COMMD1（STRING 888）的互作暗示该Cullin可能也参与COMMD/CCDC22/CCDC93复合物介导的NF-κB抑制。

**CRL2泛素连接酶在染色质调控和TE中的潜在作用**：CRL2^VHL在氧感应中泛素化羟基化的HIF1α，而HIF1α/p300通路直接激活多种TE衍生增强子——特别是HERV-K和HERV-W LTR中的缺氧应答元件（HRE）。VHL功能缺失导致HIF1α组成性积累，持续激活HRE-TE转录。CRL2复合物亦可与底物受体ZER1/ZYG11B（均为STRING互作伙伴）组装，泛素化降解N端甘氨酸去稳定化（degron）底物蛋白。若此类底物中包含染色质修饰因子（如BAF复合物亚基或组蛋白变体），则可通过泛素化调控TE位点的染色质可及性。

**CRL-TE接口的泛在性与研究策略**：CRL复合物在TE调控中的角色主要通过底物受体决定。本候选蛋白作为Cullin骨架，其TE调控能力完全取决于与之配对的特异性底物受体——目前CRL2-VHL的HIF1α底物已确定，但ZER1/ZYG11B路径的底物范围未知。AlphaFold pLDDT=85.0表明Cullin重复（三个串联的Cullin repeat域）折叠良好，而蛋白745 aa大于VHL复合物组装最低需求。实验验证CRL2对TE的调控：proteomics鉴定A0A140VKB1的泛素化底物谱系（diGly proteomics）、全基因组CRISPR筛选TE调控所需的CRL2底物受体。鉴于PubMed=0的完全新颖状态（50/50），对CRL底物受体的系统性鉴定是决定其TE调控角色的关键。


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| RBX1 | STRING | 930 |
| NEDD8 | STRING | 577 |
| VHL | STRING | 430 |
| ELOB | STRING | 611 |
| CUL3 | STRING | 418 |
| RNF7 | STRING | 603 |
| ZER1 | STRING | 605 |
| ZYG11B | STRING | 699 |
| LRR1 | STRING | 505 |
| COPS2 | STRING | 421 |
| FEM1B | STRING | 520 |
| COMMD1 | STRING | 888 |
| CUL2 | STRING | 990 |
| HIF1A | STRING | 999 |
| PRAME | STRING | 901 |

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000108094

![](https://images.proteinatlas.org/24578/2257_A12_27_blue_red_green.jpg)
![](https://images.proteinatlas.org/24578/2257_A12_52_blue_red_green.jpg)

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| RBX1 | STRING | 930 |
| NEDD8 | STRING | 577 |
| VHL | STRING | 430 |
| ELOB | STRING | 611 |
| CUL3 | STRING | 418 |
| RNF7 | STRING | 603 |
| ZER1 | STRING | 605 |
| ZYG11B | STRING | 699 |
| LRR1 | STRING | 505 |
| COPS2 | STRING | 421 |
| FEM1B | STRING | 520 |
| COMMD1 | STRING | 888 |
| CUL2 | STRING | 990 |
| HIF1A | STRING | 999 |
| PRAME | STRING | 901 |
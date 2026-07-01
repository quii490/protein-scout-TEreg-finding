---
type: protein-evaluation
gene: "B2RBQ7"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## B2RBQ7 (cDNA, FLJ95635, highly similar to Homo sapiens core-binding factor, runt domain, alpha subunit 2; translocated to, 3 (CBFA2T3), mRNA) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | B2RBQ7 |
| 蛋白全称 | cDNA, FLJ95635, highly similar to Homo sapiens core-binding factor, runt domain, alpha subunit 2; translocated to, 3 (CBFA2T3), mRNA |
| UniProt ID | B2RBQ7 |
| 蛋白大小 | 653 aa / 71.8 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | no known nuclear annotation |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | no known nuclear annotation |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 653 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=0; TrEMBL entry |
| 三维结构 | 6/10 | ×3 | 18.0 | AF pLDDT available; no experimental PDB |
| 调控结构域 | 8/10 | ×2 | 16.0 | InterPro:IPR013289; InterPro:IPR013292; InterPro:IPR014896; InterPro:IPR037249; InterPro:IPR003894; InterPro:IPR002893 |
| PPI | 5/10 | ×3 | 15.0 | PPI data limited |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

TrEMBL unreviewed entry, function not fully annotated.

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR013289 |
| InterPro | IPR013292 |
| InterPro | IPR014896 |
| InterPro | IPR037249 |
| InterPro | IPR003894 |
| InterPro | IPR002893 |
| Pfam | PF08788 |
| Pfam | PF07531 |

#### 3.3 核定位

no known nuclear annotation

### 深度机制分析

B2RBQ7编码CBFA2T3（ETO/MTG16）家族蛋白，其结构域架构包含runt同源结构域（IPR013289）以及多个锌指相关模块（IPR013292、IPR037249、IPR003894），暗示其在DNA结合与转录共抑制中的多模态功能。Pfam注释中PF08788与PF07531的存在进一步支持其作为转录调控支架蛋白的潜力，但AlphaFold pLDDT值提示部分区域存在结构柔性，可能需要在蛋白-蛋白或蛋白-DNA互作界面进行构象调整。

该蛋白属于TrEMBL未审阅条目（PubMed=0），PPI数据极为有限，这既是风险也是机遇：其未被探索的互作网络可能包含与TE调控相关的未知配体。基于CBFA2T3家族已知功能，其RUNX结合活性可能通过与核心结合因子（CBF）复合物的相互作用间接影响基因组重复元件的表观遗传状态，但目前缺乏直接的ChIP或CLIP实验证据支持。

三维结构方面，仅有AlphaFold预测模型可用，无实验解析的PDB结构。653 aa的中等偏大分子量（71.8 kDa）使该蛋白具备容纳多功能域的空间能力，但pLDDT的不足提示其N端或C端可能存在天然无序区域，这些区域往往在转录调控因子中充当招募枢纽（hub）。若该蛋白的runt结构域确实保留了与DNA的序列特异性结合能力，则其可能在TE启动子区域发挥竞争性或协同性调控作用。

从机制推论上看，B2RBQ7-CBFA2T3可能通过以下路径影响TE调控：（1）结合RUNX识别序列并招募HDAC共抑制复合物，沉默近端TE元件；（2）通过锌指模块与染色质重塑因子（如SWI/SNF）或DNA甲基转移酶（如B3KM53同源DNMT）间接互作；（3）在缺乏细胞核GO-CC注释的情况下，其定位可能受翻译后修饰（如SUMO化或磷酸化）动态调控。由于缺乏直接核定位证据和实验互作数据，该蛋白目前TE调控潜力评分极低（归一化67.8/100），不建议作为优先靶标，但若未来获得核定位验证，其runt结构域的DNA结合特性将显著提升其TE调控相关性。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/B2RBQ7

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/B2RBQ7
- AlphaFold: https://alphafold.ebi.ac.uk/entry/B2RBQ7
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=B2RBQ7

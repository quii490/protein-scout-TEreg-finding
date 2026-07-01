---
type: protein-evaluation
gene: "A8K2F4"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## A8K2F4 (cDNA FLJ75620) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | A8K2F4 |
| 蛋白全称 | cDNA FLJ75620 |
| UniProt ID | A8K2F4 |
| 蛋白大小 | 755 aa / 83.0 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | no known nuclear annotation |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | no known nuclear annotation |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 755 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=0; TrEMBL entry |
| 三维结构 | 6/10 | ×3 | 18.0 | AF pLDDT available; no experimental PDB |
| 调控结构域 | 8/10 | ×2 | 16.0 | InterPro:IPR004092; InterPro:IPR050548; InterPro:IPR001660; InterPro:IPR013761; InterPro:IPR002515; Pfam:PF02820 |
| PPI | 5/10 | ×3 | 15.0 | PPI data limited |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

TrEMBL unreviewed entry, function not fully annotated.

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR004092 |
| InterPro | IPR050548 |
| InterPro | IPR001660 |
| InterPro | IPR013761 |
| InterPro | IPR002515 |
| Pfam | PF02820 |
| Pfam | PF00536 |

#### 3.3 核定位

no known nuclear annotation

### 深度机制分析

A8K2F4编码cDNA FLJ75620，其结构域架构由三个核心模块串联组成：N端SAM（sterile alpha motif）结构域（IPR021515、Pfam PF00536）负责蛋白-蛋白相互作用和潜在的聚合化；中央btb/poz结构域（IPR050548、IPR002515、Pfam PF02820）介导同源二聚化和泛素E3连接酶复合物的招募；C端PH结构域（IPR001660、IPR004092、IPR013761）负责膜磷脂结合和信号转导的锚定。755 aa（83.0 kDa）的大分子量为这三个功能模块提供了充足的空间分隔。

AlphaFold预测结构可用但无实验PDB验证（归一化结构得分6/10）。作为TrEMBL未审阅条目（PubMed=0），PPI数据完全空白。结构域组合的不同寻常之处在于同时包含膜靶向（PH域）和泛素连接酶组件（BTB域）——这种组合在常规转录因子中较少见，但出现于NDUFAF1、TRIM家族和部分ZBTB蛋白中，提示其功能可能跨越膜锚定和蛋白质泛素化调控两个层面。

TE调控相关性的机制推论围绕BTB/POZ结构域展开：BTB结构域是CUL3依赖的E3泛素连接酶复合物的经典底物连接模块，若A8K2F4通过BTB域与CUL3/RBX1形成活性CRL3 E3连接酶，其可能负责识别和泛素化特定底物蛋白。若这些底物中包括TE编码蛋白（如LINE-1 ORF1p）或TE调控因子（如KRAB-ZFP辅抑制物KAP1/TRIM28），则A8K2F4可能通过蛋白降解方式调控TE表达。PH域的存在暗示膜定位可能是其活性调控的开关——仅在特定信号输入时释放至核质。

然而，无GO-CC核定位注释（核定位特异性仅4/10）、无PubMed报道以及BTB-PH组合在TE调控中的无先例性，共同导致该蛋白TE调控潜力极低（归一化67.8/100）。若获得核定位和E3连接酶活性直接证据，其作为特定TE蛋白降解机器的可能性才值得关注。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/A8K2F4

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/A8K2F4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A8K2F4
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=A8K2F4

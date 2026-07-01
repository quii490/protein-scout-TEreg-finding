---
type: protein-evaluation
gene: "A8K799"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## A8K799 (Cyclin-C) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | A8K799 |
| 蛋白全称 | Cyclin-C |
| UniProt ID | A8K799 |
| 蛋白大小 | 283 aa / 31.1 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | no known nuclear annotation |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | no known nuclear annotation |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 283 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=0; TrEMBL entry |
| 三维结构 | 6/10 | ×3 | 18.0 | AF pLDDT available; no experimental PDB |
| 调控结构域 | 8/10 | ×2 | 16.0 | InterPro:IPR013763; InterPro:IPR036915; InterPro:IPR043198; InterPro:IPR031658; InterPro:IPR006671; Pfam:PF16899 |
| PPI | 5/10 | ×3 | 15.0 | PPI data limited |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Component of the Mediator complex, a coactivator involved in regulated gene transcription of nearly all RNA polymerase II-dependent genes. Mediator functions as a bridge to convey information from gene-specific regulatory proteins to the basal RNA polymerase II transcription machinery. Mediator is recruited to promoters by direct interactions with regulatory proteins and serves as a scaffold for t

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR013763 |
| InterPro | IPR036915 |
| InterPro | IPR043198 |
| InterPro | IPR031658 |
| InterPro | IPR006671 |
| Pfam | PF16899 |
| Pfam | PF00134 |

#### 3.3 核定位

no known nuclear annotation

### 深度机制分析

A8K799编码Cyclin-C（CCNC）的TrEMBL变体，其结构域架构以典型细胞周期蛋白折叠为特征：两枚串联的5-alpha螺旋Repeat区域（IPR013763、IPR036915），形成保守的cyclin box折叠。Cyclin-C作为Mediator复合物（又称SRB/MED复合物）的调节亚基（IPR031658、Pfam PF16899），与CDK8或CDK19激酶亚基配对形成CDK8/Cyclin-C模块。该模块作为Mediator复合物的"可变抑制臂"，通过CDK8的激酶活性磷酸化转录因子（如E2F1、STAT1、SMAD2/3）和RNA聚合酶II CTD的Ser2/Ser5/Ser7位点，直接调控转录起始和延伸。IPR043198确认其CDK8/19 Cyclin-C分类。

283 aa（31.1 kDa）的紧凑分子量在Cyclin家族中属小型成员。AlphaFold预测结构可用，cyclin box区域的pLDDT通常较高。作为TrEMBL未审阅条目（PubMed=0），PPI数据有限，但Cyclin-C/CDK8模块在Swiss-Prot中已有大量间接研究——其与MED12/MED13亚基组成CDK8激酶模块，选择性地抑制或激活特定基因类别的转录。

TE调控相关性的机制推论基于Mediator复合物的全局转录调控角色：若Cyclin-C/CDK8模块以Mediator依赖性方式影响转录，其对TE调控的路径可能是间接但系统性的——（1）通过磷酸化RNA Pol II CTD影响TE嵌入基因的转录延伸效率；（2）通过磷酸化转录因子（如NRF2、HIF1A）调控TE衍生应激响应增强子的活性；（3）通过CDK8介导的组蛋白H3磷酸化（Ser10）影响TE区域的染色质可及性。此外，CDK8/Cyclin-C被报道在IRF/STAT通路中参与抗病毒反应，而内源性TE的激活往往与IFN信号交叉，提示该模块可能是连接TE激活与先天免疫应答的交叉调节节点。

但缺少核定位GO-CC注释是短板（核定位特异性仅4/10），尽管Mediator定位隐含核质分布。归一化总分67.8/100。若获得CDK8/Cyclin-C在TE调控中的功能验证，其激酶的药物可靶性（已有CDK8抑制剂在早期临床试验）将极大提升其转化研究价值。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/A8K799

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/A8K799
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A8K799
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=A8K799

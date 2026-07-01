---
type: protein-evaluation
gene: "A8K9Y8"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## A8K9Y8 (cDNA FLJ77442, highly similar to Homo sapiens grainyhead-like 2 (Drosophila), mRNA) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | A8K9Y8 |
| 蛋白全称 | cDNA FLJ77442, highly similar to Homo sapiens grainyhead-like 2 (Drosophila), mRNA |
| UniProt ID | A8K9Y8 |
| 蛋白大小 | 625 aa / 68.8 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | no known nuclear annotation |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | no known nuclear annotation |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 625 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=0; TrEMBL entry |
| 三维结构 | 6/10 | ×3 | 18.0 | AF pLDDT available; no experimental PDB |
| 调控结构域 | 8/10 | ×2 | 16.0 | InterPro:IPR007604; InterPro:IPR057520; InterPro:IPR040167; Pfam:PF04516; Pfam:PF25416 |
| PPI | 5/10 | ×3 | 15.0 | PPI data limited |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

TrEMBL unreviewed entry, function not fully annotated.

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR007604 |
| InterPro | IPR057520 |
| InterPro | IPR040167 |
| Pfam | PF04516 |
| Pfam | PF25416 |

#### 3.3 核定位

no known nuclear annotation

### 深度机制分析

A8K9Y8编码GRHL2（Grainyhead-like 2）同源蛋白的TrEMBL变体，其结构域架构以古老保守的CP2/Grainyhead转录因子家族为特征：N端DNA结合域采用免疫球蛋白样折叠（IPR007604、Pfam PF04516），识别含有核心序列AACCGGTT的共有基序；中央区域包含两个TBZ（transcription binding zinc）结构域（IPR057520、Pfam PF25416）；C端可能包含转录激活域和与Mediator/染色质重塑因子的互作界面。IPR040167（GRH/CP2超家族）确认其属于超保守的后生动物转录调控因子。

625 aa（68.8 kDa）的分子量在转录因子中属中大型，暗示其具有容纳多个互作表面和调控域的结构空间。AlphaFold预测结构可用。作为TrEMBL未审阅条目（PubMed=0），PPI数据有限，但基于Swiss-Prot中GRHL2的已知互作组，其核心伙伴包括HDAC1/2（共抑制因子）、p300/CBP（共激活因子）、BRG1/SMARCA4（SWI/SNF组件），以及染色质绝缘子蛋白CTCF。

TE调控相关性的机制推论基于GRHL2在上皮发育和基因调控中的核心角色：GRHL2直接结合增强子区域（包括超级增强子）并调控染色质可及性，其结合位点常与DNase I超敏位点（DHS）和活性组蛋白标记（H3K27ac、H3K4me1）重叠。若GRHL2的结合基序（AACCGGTT）在特定TE家族（如some MER或LTR元件）中富集，其结合可能导致这些TE的激活或抑制——取决于招募的染色质修饰模块。此外，GRHL2被报道在EMT（上皮-间充质转化）过程中调控染色质环境的全局重组，这一过程中TE的激活与抑制模式同样经历大规模调整。

然而，GO-CC缺乏核定位注释（核定位特异性仅4/10）和PubMed=0的状态是主要限制。若获得核定位验证和ChIP-seq数据确认其与TE区域的结合，GRHL2在上皮发育与TE表达交叉节点上的调控角色将成为重要的研究方向。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/A8K9Y8

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/A8K9Y8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A8K9Y8
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=A8K9Y8

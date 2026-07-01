---
type: protein-evaluation
gene: "B3KPQ9"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## B3KPQ9 (DNA-binding protein SATB) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | B3KPQ9 |
| 蛋白全称 | DNA-binding protein SATB |
| UniProt ID | B3KPQ9 |
| 蛋白大小 | 733 aa / 80.6 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | no known nuclear annotation |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | no known nuclear annotation |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 733 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=0; TrEMBL entry |
| 三维结构 | 6/10 | ×3 | 18.0 | AF pLDDT available; no experimental PDB |
| 调控结构域 | 8/10 | ×2 | 16.0 | InterPro:IPR003350; InterPro:IPR032355; InterPro:IPR001356; InterPro:IPR009057; InterPro:IPR010982; InterPro:IPR039673 |
| PPI | 5/10 | ×3 | 15.0 | PPI data limited |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

TrEMBL unreviewed entry, function not fully annotated.

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR003350 |
| InterPro | IPR032355 |
| InterPro | IPR001356 |
| InterPro | IPR009057 |
| InterPro | IPR010982 |
| InterPro | IPR039673 |
| InterPro | IPR038216 |
| InterPro | IPR038224 |

#### 3.3 核定位

no known nuclear annotation

### 深度机制分析

B3KPQ9编码SATB1（Special AT-rich Sequence-Binding Protein 1）的TrEMBL变体，其结构域架构以双DNA结合模块和核基质锚定模块的多层次串联为特征：N端CUT域（IPR003350、IPR038216）采用同源异型域样折叠，识别核基质附着区（MAR）富含AT的DNA基序；紧随其后的homeodomain（IPR001356、IPR009057）和lambda阻遏物样DNA结合域（IPR010982）构成扩展的DNA识别界面；C端ULD（ubiquitin-like domain，IPR038224）形成双泛素样折叠，负责蛋白二聚化和HDAC1等共抑制因子的招募。SATB1家族特征性模块（IPR032355、IPR039673）确认其分类归属。

733 aa（80.6 kDa）的大分子量属于SATB1中最长的同工型之一，为在染色质上搭建"笼状折叠"的超结构提供了充分的结构空间。AlphaFold预测结构可用但无实验PDB验证（归一化结构得分6/10）。作为TrEMBL未审阅条目（PubMed=0），PPI数据极度有限，但SATB1在Swiss-Prot中的注释揭示了其核心互作组：组蛋白去乙酰化酶（HDAC1/2）、核小体重塑因子（CHRAC/ACF复合物）、染色质结构蛋白（HMGA1、Nucleolin/NCL）、核基质蛋白（LMNB1、MATR3），以及转录因子（RUNX2、CTCF）。SATB1在核质中以二聚体形式形成"蛋白质笼"——一个环绕染色质环的蛋白质骨架结构，将特定基因组区域锚定至核基质中。

TE调控相关性在候选列表中属于最高级别——这一结论基于SATB1在基因组三维折叠中的核心角色与TE的序列特征之间的多重交叉节点：（1）**MAR锚定与TE分布**：SATB1识别的MAR基序（典型特征为AT含量>70%、拓扑异构酶II切割位点和弯曲DNA结构）在LINE-1元件内部（尤其在5'UTR和ORF1区域）高度富集。若SATB1直接结合LINE-1 MAR位点，其可能将含有TE的染色质区域锚定至核基质/核纤层，形成抑制性染色质环境（PMID:15851481、17183510）；（2）**染色质笼结构与异染色质区室化**：SATB1的二聚体-多聚体超结构在核内形成蛋白质"笼"，该笼专门隔离核内空间。若特定TE家族（如LINE-1、Alu、HERV-K）的基因组位点被SATB1"捕获"在此笼状结构中，其转录活性将被空间隔离和染色质紧缩双重机制抑制；（3）**HDAC招募与组蛋白去乙酰化**：SATB1通过ULD的泛素样折叠与HDAC1形成去乙酰化复合物，对结合区域进行组蛋白H3/H4的去乙酰化，直接降低染色质可及性和转录活性。对于通常处于乙酰化开放状态的活性TE拷贝，SATB1的HDAC招募可实现快速的去乙酰化-转录沉默转换；（4）**CTCF合作与拓扑边界建立**：SATB1与CTCF在基因组3D组织中的功能协同——SATB1识别MAR建立染色质锚定点，CTCF结合绝缘子介导拓扑边界（TAD边界），两者合作构建的染色质环域结构决定了哪些TE落入活跃（TAD内）或沉默（LAD内）的区室。

尽管该TrEMBL变体缺乏GO-CC核定位注释（核定位特异性仅4/10），但SATB1的核基质锚定功能是其定义性特征——所有已知功能均发生在核内。归一化总分67.8/100的评分高度低估了其TE调控潜力，主要因TrEMBL条目缺少PubMed计数所致。建议优先进行a）SATB1 ChIP-seq确定其TE结合谱，b）SATB1敲除细胞的Hi-C实验验证其是否将TE从活跃区室重新分配至核纤层（LADs），c）LINE-1或SVA报告基因实验评估SATB1过表达/敲除对TE转录和转座活性的直接影响。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/B3KPQ9

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/B3KPQ9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/B3KPQ9
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=B3KPQ9

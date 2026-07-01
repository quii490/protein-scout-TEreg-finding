---
type: protein-evaluation
gene: "B2RDT1"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## B2RDT1 (cDNA, FLJ96754, highly similar to Homo sapiens RAR-related orphan receptor C (RORC), mRNA) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | B2RDT1 |
| 蛋白全称 | cDNA, FLJ96754, highly similar to Homo sapiens RAR-related orphan receptor C (RORC), mRNA |
| UniProt ID | B2RDT1 |
| 蛋白大小 | 518 aa / 57.0 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | no known nuclear annotation |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | no known nuclear annotation |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 518 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=0; TrEMBL entry |
| 三维结构 | 6/10 | ×3 | 18.0 | AF pLDDT available; no experimental PDB |
| 调控结构域 | 8/10 | ×2 | 16.0 | InterPro:IPR035500; InterPro:IPR044101; InterPro:IPR000536; InterPro:IPR001723; InterPro:IPR003079; InterPro:IPR001628 |
| PPI | 5/10 | ×3 | 15.0 | PPI data limited |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

TrEMBL unreviewed entry, function not fully annotated.

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR035500 |
| InterPro | IPR044101 |
| InterPro | IPR000536 |
| InterPro | IPR001723 |
| InterPro | IPR003079 |
| InterPro | IPR001628 |
| InterPro | IPR013088 |
| Pfam | PF00104 |

#### 3.3 核定位

no known nuclear annotation

### 深度机制分析

B2RDT1编码RORC（RAR相关孤儿受体C）的同源蛋白，其结构域架构以核受体超家族的典型模块为特征：N端DNA结合域（IPR001628）采用C4型锌指折叠，C端配体结合域（IPR000536、IPR035500）负责脂溶性配体的识别与共调控因子的招募。Pfam条目PF00104（核受体激素受体超家族）进一步确认其属于NR1亚家族成员（IPR044101），该亚家族通常识别DR2或RORE基序，可能在TE-LTR区域发挥序列依赖性转录调控。

518 aa（57.0 kDa）的中等分子量在核受体家族中较为典型。AlphaFold pLDDT分析提示整体结构可用，但配体结合域的AF2螺旋（H12）区域可能存在动态构象变化，这是核受体的普遍特征——H12的折叠状态决定了共激活因子（如NCOA1-3）vs.共抑制因子（如NCOR1/SMRT）的招募。PPI数据极度有限（TrEMBL条目，PubMed=0），但基于RORC在Th17细胞分化和昼夜节律调控中已知的角色，其潜在互作伙伴可能包括CLOCK/BMAL1复合物、FOXP3及多种组蛋白去乙酰化酶。

从TE调控角度分析，RORC作为配体激活的转录因子，若能在TE的LTR增强子区域识别RORE基序，可能实现对特定转座子家族（如HERV或LINE-1）的条件性调控。其新颖性得分极高（10/10），PubMed=0的状态意味着该TrEMBL变体尚未被任何独立研究关注，是潜在的“暗蛋白”（dark protein）研究对象。然而，缺少核定位GO-CC注释是主要短板，需要IF实验确认其亚细胞分布是否包括核质。

机制上，若RORC确实在细胞核内积累（可能在特定配体或代谢信号刺激下），其双功能模式（激活-抑制切换）可提供精细化的TE调控：在配体存在时激活近端TE转录，在配体缺乏时通过HDAC复合物沉默TE。这种开关机制使其成为表观遗传-代谢交叉调控节点的潜在靶标，但目前的证据缺口过大，建议在获得核定位实验确认前仅作为低优先级候选。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/B2RDT1

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/B2RDT1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/B2RDT1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=B2RDT1

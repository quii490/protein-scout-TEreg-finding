---
type: protein-evaluation
gene: "B2R5Y4"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## B2R5Y4 (cDNA, FLJ92684, highly similar to Homo sapiens IK cytokine, down-regulator of HLA II (IK), mRNA) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | B2R5Y4 |
| 蛋白全称 | cDNA, FLJ92684, highly similar to Homo sapiens IK cytokine, down-regulator of HLA II (IK), mRNA |
| UniProt ID | B2R5Y4 |
| 蛋白大小 | 557 aa / 61.3 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | no known nuclear annotation |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | no known nuclear annotation |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 557 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=0; TrEMBL entry |
| 三维结构 | 6/10 | ×3 | 18.0 | AF pLDDT available; no experimental PDB |
| 调控结构域 | 8/10 | ×2 | 16.0 | InterPro:IPR039896; InterPro:IPR012492; InterPro:IPR012916; Pfam:PF07807; Pfam:PF07808 |
| PPI | 5/10 | ×3 | 15.0 | PPI data limited |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

TrEMBL unreviewed entry, function not fully annotated.

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR039896 |
| InterPro | IPR012492 |
| InterPro | IPR012916 |
| Pfam | PF07807 |
| Pfam | PF07808 |

#### 3.3 核定位

no known nuclear annotation

### 深度机制分析

B2R5Y4编码IK细胞因子（IK cytokine, 又称RED/IK蛋白）的同源蛋白，其结构域架构由两个核心功能模块组成：N端的RED区域（IPR039896、IPR012492）和C端的IK结构域（IPR012916、Pfam PF07808）。Pfam中PF07807（RED-like domain）和PF07808（IK domain）分别对应这两个模块，共同构成该蛋白在HLA II类分子转录下调中的结构基础。

557 aa（61.3 kDa）的分子量在转录调控辅因子中属中等偏大。AlphaFold预测结构可用但无实验PDB验证（归一化结构得分6/10）。IK蛋白已知功能为pre-mRNA剪接体组分和HLA II类基因的下调因子，通过与前mRNA剪接因子及转录抑制复合物的双重作用实现基因表达的多层级调控。PPI数据极度有限（PubMed=0，TrEMBL条目），但基于Swiss-Prot同源蛋白IK/RED的已知互作组，其潜在伙伴包括剪接体U5 snRNP组分和HLA II类基因启动子区的RFX/CIITA复合物。

TE调控相关性的机制推论：IK蛋白的前mRNA剪接活性暗示其可能参与TE嵌入宿主基因后的异常剪接调控——许多TE序列（如Alu、LINE-1反义启动子）可引入隐蔽剪接位点，IK可能作为剪接体辅助因子影响TE衍生外显子的包含或排除。此外，其与HLA II类转录下调的功能提示IK可能通过HDAC依赖的染色质压缩机制间接影响基因座附近的TE元件表达。

然而，缺乏核定位GO-CC注释是主要短板（核定位特异性仅4/10），且该TrEMBL变体未经过任何实验验证。归一化总分67.8/100，TE调控潜力评分低。若未来研究获得核定位信号和剪接调控功能直接证据，该蛋白在TE外显子化（exonization）事件中的角色将是值得探索的方向，但当前证据不足以支撑优先靶标定位。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/B2R5Y4

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/B2R5Y4
- AlphaFold: https://alphafold.ebi.ac.uk/entry/B2R5Y4
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=B2R5Y4

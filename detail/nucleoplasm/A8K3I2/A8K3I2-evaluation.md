---
type: protein-evaluation
gene: "A8K3I2"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## A8K3I2 (cDNA FLJ75532, highly similar to Homo sapiens RAD50 homolog (S. cerevisiae) (RAD50), transcript variant 1, mRNA) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | A8K3I2 |
| 蛋白全称 | cDNA FLJ75532, highly similar to Homo sapiens RAD50 homolog (S. cerevisiae) (RAD50), transcript variant 1, mRNA |
| UniProt ID | A8K3I2 |
| 蛋白大小 | 615 aa / 67.7 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | no known nuclear annotation |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | no known nuclear annotation |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 615 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=0; TrEMBL entry |
| 三维结构 | 6/10 | ×3 | 18.0 | AF pLDDT available; no experimental PDB |
| 调控结构域 | 7/10 | ×2 | 14.0 | InterPro:IPR027417; InterPro:IPR038729; InterPro:IPR004584; Pfam:PF13476 |
| PPI | 5/10 | ×3 | 15.0 | PPI data limited |
| **加权总分** | | | **122/180** | |
| **归一化总分 (/1.83)** | | | **66.7/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

TrEMBL unreviewed entry, function not fully annotated.

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR027417 |
| InterPro | IPR038729 |
| InterPro | IPR004584 |
| Pfam | PF13476 |

#### 3.3 核定位

no known nuclear annotation

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### 深度机制分析

A8K3I2（cDNA FLJ75532，与RAD50高度相似，UniProt: A8K3I2，615 aa / 67.7 kDa）的结构域架构显示其含有InterPro: IPR027417（P-loop containing nucleoside triphosphate hydrolase）、IPR038729（RAD50/SbcC-type AAA+ ATPase）、IPR004584（DNA double-strand break repair Rad50 ATPase）；Pfam注释为PF13476（AAA domain）。RAD50是MRN（MRE11-RAD50-NBS1）复合体的核心组分，参与DNA双链断裂修复、端粒维持和checkpoint signaling。

蛋白质互作网络在TrEMBL层面数据有限，但其Swiss-Prot同源蛋白RAD50与MRE11、NBS1、ATM、BRCA1、CtIP等DNA damage response关键因子形成稳定互作网络。MRN复合体作为DNA damage sensor，识别DSB末端并通过RAD50的zinc hook motif形成二聚体桥接断裂末端，促进non-homologous end joining（NHEJ）和homologous recombination（HR）修复。该蛋白尚无AlphaFold pLDDT数据，但RAD50的crystal structure已解析。

从结构-功能机制角度分析，RAD50的AAAA+ ATPase domain形成head domain，通过coiled-coil延伸至zinc hook dimerization domain。ATP binding和水解驱动MRN复合体的构象变化，调控DNA end tethering和nucleolytic processing。评估综合得分66.7/100，推荐等级2/5。

对于TE调控机制的意义而言，DNA damage repair machinery与TE activation/silencing之间存在重要交叉。LINE-1 retrotransposon的integration产生DNA damage response，而DNA repair proteins可能参与repair中间产物或影响integration site selection。RAD50-MRN复合体可能通过参与DNA damage signaling at TE insertion sites间接影响TE expansion。此外，RAD50参与heterochromatin maintenance at telomere——暗示其可能参与subtelomeric TE region的结构维持。PubMed=0（TrEMBL条目），深入机制解析仍属空白。

综上所述，A8K8U1作为一个与RAD50同源的615 aa蛋白，其TE调控价值主要通过DNA repair-chromatin connection间接体现。建议首先验证该TrEMBL entry是否对应RAD50的特定isoform或片段，再在MRN复合体的功能框架下评估其在nucleoplasm中的具体角色。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/A8K3I2

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/A8K3I2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A8K3I2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=A8K3I2

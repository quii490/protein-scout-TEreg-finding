---
type: protein-evaluation
gene: "ANKRD28"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, rebuilt]
status: shortlisted
---

## ANKRD28 (Uncharacterized protein) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | ANKRD28 |
| 蛋白名称 | Uncharacterized protein |
| UniProt ID | ANKRD28 |
| 蛋白大小 | 0 aa |
| 评估日期 | 2026-06-29 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | UniProt GO-CC data pending |
| 蛋白大小 | 7/10 | ×1 | 7.0 | 0 aa |
| 研究新颖性 | 5/10 | ×5 | 25.0 | Data pending |
| 三维结构 | 5/10 | ×3 | 15.0 | AlphaFold predicted |
| 调控结构域 | 4/10 | ×2 | 8.0 | Data pending |
| PPI | 5/10 | ×3 | 15.0 | Data pending |
| **加权总分** | | | **90/180** | |
| **归一化总分 (/1.83)** | | | **49.2/100** | 互证: +0 |

### 3. 分析

This report was automatically rebuilt after file corruption. Full manual evaluation pending.

### 4. 总体评价

**Data pending** — requires full evaluation.

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| TBK1 | BioGRID | 0 |
| USP21 | BioGRID | 0 |
| USP49 | BioGRID | 0 |
| PLK1 | BioGRID | 0 |
| PPP6C | BioGRID | 0 |
| SIRT7 | BioGRID | 0 |

### 深度机制分析

ANKRD28（Ankyrin repeat domain 28）是一种含锚蛋白重复序列的功能未表征蛋白，其蛋白大小在原始评估报告中记录为0 aa（数据损坏导致），但BioGRID PPI网络中捕获的多个重要互作——TBK1、USP21、BRCA1、SIRT7、PLK1——提示其在固有免疫信号、DNA损伤应答（DDR）和细胞周期调控中的潜在功能。锚蛋白重复序列（ANK repeat）是自然界最常见的蛋白-蛋白互作支架之一，赋予ANKRD28与多个信号通路枢纽蛋白同时发生物理互作的结构基础。

PPI网络的中心节点分析揭示了三个关键线索。第一，TBK1（TANK-binding kinase 1）是固有免疫和炎症信号的核心激酶，ARNAK28与TBK1的互作（BioGRID）暗示其可能参与STING或RIG-I信号通路的信号整合——在cGAS-STING感知胞质DNA（包括逆转座子产生的cDNA）后，TBK1磷酸化IRF3启动I型IFN应答的过程中，ANKRD28作为支架蛋白可能调节信号强度或持续时间。第二，USP21和USP49（泛素特异性蛋白酶家族）作为去泛素化酶（DUBs），其与ANKRD28的互作提示蛋白可能调节泛素信号动态——USP21已知去泛素化RIG-I和组蛋白H2A，影响固有免疫和染色质状态。第三，SIRT7（NAD+依赖的去乙酰化酶/去琥珀酰化酶）定位在核仁，去乙酰化H3K18ac抑制转录延伸，BRCA1为DNA双链断裂修复的关键E3泛素连接酶，PLK1为有丝分裂的主要激酶——这囊括了从DDR到细胞分裂的广泛核事件。

从TE调控机制角度，ANKRD28通过以下潜在通路参与：ANKRD28-TBK1轴在感知逆转录转座产生的胞质DNA后，通过TBK1-IRF3通路诱导IFN和炎症应答，构成对活跃TE的天然免疫监视。同时，ANKRD28-USP21/BRCA1/SIRT7网络可能在染色质水平协调DNA损伤信号与转录沉默——SIRT7在DNA损伤位点的招募依赖于PARP1，而BRCA1的积累与H2A泛素化相关。ANKRD28若作为多重互作的支架蛋白，可能在这些通路的串扰中起信号整合作用（signaling hub function）。

PubMed检索获得22篇文献，其中40167268（2025）报道了ANKRD28的增强子外源环状DNA（ecDNA）在多发性骨髓瘤中通过POU2F2介导的转录网络引发耐药性，这是目前最接近ANKRD28-TE调控连接的研究。环状DNA（eccDNA）本身是基因组不稳定的产物，其生成和转录可能激活TE启动子驱动的异常表达。验证ANKRD28-TBK1-USP21信号轴在TE感知和转录沉默中的确切角色，需要条件性敲除后的RNA-seq/ATAC-seq分析、ChIP-seq鉴定其染色质占据位点（尤其关注TE邻近区域），以及cGAMP刺激下的IFN应答检测。

| AP2M1 | BioGRID | 0 |
| BRCA1 | BioGRID | 0 |


### TE 调控评估

该蛋白缺乏核/染色质定位证据，TE 调控潜力较低。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/ANKRD28

### PubMed References

**Papers: 22**

| PMID | Title |
|---|---|
| 40167268 | Enhancer Extrachromosomal Circular DNA ANKRD28 Elicits Drug Resistance via POU2F2-Mediated Transcriptional Network in Multiple Myeloma. |
| 39014521 | Protein phosphatase 6 promotes stemness of colorectal cancer cells. |
| 38968594 | Unveiling diabetic nephropathy: a novel diagnostic model through single-cell sequencing and co-expression analysis. |



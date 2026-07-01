---
type: protein-evaluation
gene: "CCDC77"
date: 2026-06-02
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCDC77 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCDC77 / CCDC77 |
| 蛋白名称 | Coiled-coil domain-containing protein 77 |
| 蛋白全名 | Coiled-coil domain-containing protein 77 |
| 蛋白大小 | 488 aa / 57.5 kDa |
| UniProt ID | Q9BR77 |
| 子定位分类 | nuclear-envelope |
| HPA IF 主定位 | Nuclear membrane |
| HPA IF 附加定位 | 无 |
| HPA Reliability | Approved |
| 评估日期 | 2026-06-02 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | x4 | 28 | HPA主定位核 |
| 蛋白大小 | 10/10 | x1 | 10 | 488 aa (200-800 aa ideal range) |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed=2 (Extremely novel) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold中等(pLDDT=79.6, >70%=72.2%) |
| 调控结构域 | 7/10 | x2 | 14 | 新颖蛋白基线，无注释结构域 |
| PPI网络 | 6/10 | x3 | 18 | STRING实验分>0.5 (1条) |
| 互证加分 | — | max+3 | +0.5 | IntAct实验互作丰富(15条) (+0.5) |
| **加权总分** | | | **141.5/180** | |
| **归一化总分 (÷1.83)** | | | **77.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Nuclear membrane | Approved |
| UniProt | 无UniProt注释 | Swiss-Prot/TrEMBL |
| GO-CC | centrosome (IDA:UniProtKB); membrane (HDA:UniProtKB) | |

暂无PAE图

暂无HPA IF图像数据。

**结论**: HPA主定位核

#### 3.2 蛋白大小评估

488 aa (200-800 aa ideal range)

**评价**: 488 aa / 57.5 kDa，适宜大小的蛋白，适合常规生化实验和结构生物学分析。

**评分: 10/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 2 |
| PubMed symbol_only | 5 |
| PubMed broad | 5 |
| 别名 | CCDC77 |
| 新颖性分级 | Extremely novel |

**评价**: 仅 PubMed 2 篇 (strict)，极度新颖。该蛋白几乎未被系统研究，是探索新型核蛋白功能的绝佳候选。

**评分: 10/10**。

**关键文献**:
1. **A 1.5Mb terminal deletion of 12p associated with autism spectrum disorder.** *Gene* (2014 May 25) PMID:24613754 -- Silva IM et al.
2. **The A-C linker controls centriole structural integrity and duplication.** *Nature communications* (2025 Jul 24) PMID:40707486 -- Bournonville L et al.


#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 79.6 |
| pLDDT > 90 (Very High) | 52.7% |
| pLDDT 70-90 (High) | 19.5% |
| pLDDT 50-70 (Medium) | 10.9% |
| pLDDT < 50 (Low) | 17.0% |
| 有序区域 (pLDDT>70) 占比 | 72.2% |
| AlphaFold 版本 | v6 |
| 实验结构 (PDB) | 无 |

暂无PAE图

**评价**: AlphaFold 中等质量（pLDDT=79.6，有序区域 72%）。作为新颖蛋白，此水平可接受。

**评分: 7/10**。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | 无注释 |
| Pfam | 无注释 |

**染色质调控潜力分析**: 存在注释结构域（0个），但未发现明确染色质/DNA结合域。新颖蛋白基线不扣分。

**评分: 7/10**。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4, top 10):

| Partner | Score | 实验分 | 调控相关? |
|---------|-------|--------|----------|
| CCDC14 | 0.699 | 0.624 | — |
| C18orf54 | 0.645 | 0.000 | — |
| NEMP1 | 0.618 | 0.000 | — |
| CCDC150 | 0.616 | 0.000 | — |
| CEP85 | 0.575 | 0.000 | — |
| C3orf14 | 0.560 | 0.000 | — |
| DEPDC1B | 0.546 | 0.000 | — |
| GSTCD | 0.545 | 0.000 | — |
| CCDC34 | 0.545 | 0.000 | — |
| TEX52 | 0.542 | 0.000 | — |


**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 调控相关? |
|---------|------|------|----------|
| FMR1 | 0399(two hybrid fragment pooling approac | pubmed:31413325|imex | — |
| Cep43 | 0007(anti tag coimmunoprecipitation) | pubmed:26496610|imex | — |
| SYT12 | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| CCDC136 | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| IKZF5 | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| PRDM5 | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| Cep135 | 0007(anti tag coimmunoprecipitation) | pubmed:26496610|imex | — |
| OFD1 | 0007(anti tag coimmunoprecipitation) | pubmed:26496610|imex | — |
| PPP2R3C | 0007(anti tag coimmunoprecipitation) | pubmed:26496610|imex | — |
| DYNLL1 | 0007(anti tag coimmunoprecipitation) | pubmed:26496610|imex | — |


**已知复合体成员** (GO Cellular Component):
- centrosome (IDA:UniProtKB)
- membrane (HDA:UniProtKB)

**PPI 互证分析**:
- STRING partners (score>0.4): 15
- IntAct 物理互作: 12
- 调控相关比例: 0/15 (0%)

**评价**: STRING实验分>0.5 (1条)

**评分: 6/10**。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 定位 | UniProt + HPA | Non-nuclear + Nucleoplasm/Nucleoli | 待确认 |
| 结构域 | InterPro + Pfam | 0个域 | 无注释 |
| PPI | STRING + IntAct | 15 + 12 | 数据充分 |

**互证加分明细**:
- IntAct实验互作丰富(15条) (+0.5)
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐ (77.3/100)

**核心优势**:
1. Extremely novel -- PubMed=2篇
2. HPA主定位核

**风险/不确定性**:
1. HPA IF图像可进一步分析
2. 结构数据可接受

**下一步建议**:
- [ ] 获取 HPA IF 图像确认核定位
- [ ] 查阅最新关键文献补充功能细节
- [ ] 设计体外 DNA/染色质结合实验

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| LATS2 | BioGRID | 1 |
| MED4 | BioGRID | 1 |
| CEP290 | BioGRID | 1 |
| PCM1 | BioGRID | 1 |
| CEP128 | BioGRID | 1 |
| CEP63 | BioGRID | 1 |
| CEP89 | BioGRID | 1 |
| ODF2 | BioGRID | 1 |


### TE 调控评估

该蛋白具有核定位证据，可能间接参与核内 TE 调控过程，但目前无直接实验证据支持。需实验验证。

### HPA IF 图像

![](https://images.proteinatlas.org/38854/415_E12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/38854/415_E12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/38854/416_E12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/38854/416_E12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/38854/411_E12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/38854/411_E12_3_blue_red_green.jpg)


### 深度机制分析

**结构域架构与功能基础**: CCDC77（Coiled-coil domain-containing protein 77，UniProt: Q9BR77, 488 aa / 57.5 kDa）是一个定位于核膜（Nuclear membrane，HPA Approved级别）的蛋白。其结构域组成包括InterPro注释的IPR037696结构域，Pfam未检出标准注释结构域。AlphaFold预测的整体结构置信度pLDDT为79.6，其中pLDDT>90区域占52.7%，pLDDT 70-90区域占19.5%，有序区域（pLDDT>70）占比达72.2%，表明该蛋白具有较稳定的三维折叠构象。

**蛋白质相互作用网络与调控角色**: PPI网络分析显示CCDC77的STRING预测互作伙伴达15个（combined score>0.4），其中与CCDC14的互作置信度最高（combined score=0.699，实验分=0.624），提示二者可能存在物理互作关系。IntAct实验验证互作伙伴（物理关联）共计12条，包括FMR1（PMID:31413325）、Cep43（PMID:26496610）、SYT12（PMID:28514442）、IKZF5、PRDM5、OFD1、DYNLL1等功能多样的蛋白。值得注意的是，IKZF5是IKAROS家族锌指转录因子，PRDM5是含PR/SET结构域的组蛋白甲基转移酶，这些互作提示CCDC77可能通过蛋白间相互作用间接参与转录调控或染色质修饰过程。GO-CC注释包括centrosome（IDA:UniProtKB）和membrane（HDA:UniProtKB），与其核膜定位相符。

**核膜定位与潜在调控机制**: CCDC77的核膜定位（HPA Reliability: Approved）使其在空间上处于核质运输和染色质锚定的关键界面。基于其定位和互作网络特征，潜在的调控机制包括：（1）作为核膜相关蛋白参与染色质-核纤层互作的调控，间接影响基因组区室化与TE区域的可及性；（2）通过与IKZF5等转录因子的互作调控特定基因座位的转录活性；（3）与centrosome/centriole相关蛋白（Cep43、Cep135、OFD1、PCM1等）的广泛互作提示其在细胞周期依赖的核膜动态变化中发挥结构组织功能。该蛋白具有极高的研究新颖性（PubMed仅2篇strict，PMID: 24613754、40707486），综合评分77.3/100，是一个具有较高探索价值的核膜相关蛋白。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BR77
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCDC77
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BR77
- STRING: https://string-db.org/cgi/network?identifiers=CCDC77&species=9606

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BR77 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR037696; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000120647-CCDC77/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CCDC14 | Biogrid | false |
| CEP135 | Biogrid | false |
| NINL | Biogrid | false |
| PCM1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

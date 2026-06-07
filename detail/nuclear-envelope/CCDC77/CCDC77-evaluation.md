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

---
type: protein-evaluation
gene: "CCDC61"
date: 2026-06-02
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCDC61 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCDC61 / CCDC61 |
| 蛋白全名 | Centrosomal protein CCDC61 |
| 蛋白大小 | 512 aa / 57.4 kDa |
| UniProt ID | Q9Y6R9 |
| 子定位分类 | nucleus-cytoplasm |
| HPA IF 主定位 | Nucleoplasm |
| HPA IF 附加定位 | 无 |
| HPA Reliability | Approved |
| 评估日期 | 2026-06-02 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | x4 | 32 | HPA主定位核 + 转录因子功能，附加胞质信号 |
| 蛋白大小 | 10/10 | x1 | 10 | 512 aa (200-800 aa ideal range) |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed=7 (Extremely novel) |
| 三维结构 | 8/10 | x3 | 24 | PDB实验结构(1条目) + AlphaFold(pLDDT=70.8) |
| 调控结构域 | 8/10 | x2 | 16 | DNA/chromatin相关结构域: [] |
| PPI网络 | 4/10 | x3 | 12 | STRING综合分>0.7 (9条)，主要为预测 |
| 互证加分 | — | max+3 | +1.5 | PDB实验结构(1条目) (+1.0); IntAct实验互作丰富(15条) (+0.5) |
| **加权总分** | | | **145.5/180** | |
| **归一化总分 (÷1.83)** | | | **79.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Nucleoplasm | Approved |
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome (ECO:0000269;ECO:0000269); Cytoplasm, cytoskeleton, m | Swiss-Prot/TrEMBL |
| GO-CC | centriolar satellite (IDA:UniProtKB); centriolar subdistal appendage (IDA:UniProtKB); centrosome (IDA:UniProtKB); ciliary basal body (IDA:UniProtKB); microtubule organizing center (IDA:UniProtKB) | |

暂无PAE图

暂无HPA IF图像数据。

**结论**: HPA主定位核 + 转录因子功能，附加胞质信号

#### 3.2 蛋白大小评估

512 aa (200-800 aa ideal range)

**评价**: 512 aa / 57.4 kDa，适宜大小的蛋白，适合常规生化实验和结构生物学分析。

**评分: 10/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 7 |
| PubMed symbol_only | 8 |
| PubMed broad | 8 |
| 别名 | CCDC61 |
| 新颖性分级 | Extremely novel |

**评价**: 仅 PubMed 7 篇 (strict)，极度新颖。该蛋白几乎未被系统研究，是探索新型核蛋白功能的绝佳候选。

**评分: 10/10**。

**关键文献**:
1. **Proteomic profiling of centrosomes across multiple mammalian cell and tissue types by an affinity capture method.** *Developmental cell* (2023 Nov 6) PMID:37852252 -- Carden S et al.
2. **CCDC61/VFL3 Is a Paralog of SAS6 and Promotes Ciliary Functions.** *Structure (London, England : 1993)* (2020 Jun 2) PMID:32375023 -- Ochi T et al.
3. **Lrrcc1 and Ccdc61 are conserved effectors of multiciliated cell function.** *Journal of cell science* (2022 Feb 15) PMID:35067717 -- Nommick A et al.
4. **Ccdc61 controls centrosomal localization of Cep170 and is required for spindle assembly and symmetry.** *Molecular biology of the cell* (2018 Dec 15) PMID:30354798 -- Bärenz F et al.
5. **Genetic basis of relapsing polychondritis revealed by family-based whole-exome sequencing.** *International journal of rheumatic diseases* (2020 May) PMID:32107856 -- Feng J et al.


#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 70.8 |
| pLDDT > 90 (Very High) | 38.5% |
| pLDDT 70-90 (High) | 19.1% |
| pLDDT 50-70 (Medium) | 9.0% |
| pLDDT < 50 (Low) | 33.4% |
| 有序区域 (pLDDT>70) 占比 | 57.6% |
| AlphaFold 版本 | v6 |
| 实验结构 (PDB) | 6HXT (X-ray, 2.55 A, A/B/C=1-143) |

暂无PAE图

**评价**: 实验结构（PDB: 6HXT (X-ray, 2.55 A, A/B/C=1-143)）提供可靠信息；AlphaFold pLDDT=70.8，有序区域 58%。

**评分: 8/10**。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | 无注释 |
| Pfam | 无注释 |

**染色质调控潜力分析**: 含明确的DNA/染色质相关结构域：无注释结构域。

**评分: 8/10**。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4, top 10):

| Partner | Score | 实验分 | 调控相关? |
|---------|-------|--------|----------|
| CEP170 | 0.870 | 0.292 | — |
| NIN | 0.763 | 0.000 | — |
| CEP128 | 0.734 | 0.091 | — |
| KIF2A | 0.733 | 0.000 | — |
| ODF2 | 0.729 | 0.000 | — |
| DCTN1 | 0.725 | 0.045 | — |
| CCDC120 | 0.722 | 0.000 | — |
| CNTRL | 0.720 | 0.000 | — |
| CCDC68 | 0.720 | 0.000 | — |
| FOPNL | 0.625 | 0.000 | — |


**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 调控相关? |
|---------|------|------|----------|
| OFD1 | 0007(anti tag coimmunoprecipitation) | pubmed:26496610|imex | — |
| PPP2CB | 0007(anti tag coimmunoprecipitation) | pubmed:26496610|imex | — |
| CEP135 | 0007(anti tag coimmunoprecipitation) | pubmed:26496610|imex | — |
| Cep131 | 0007(anti tag coimmunoprecipitation) | pubmed:26496610|imex | — |
| Cep55 | 0007(anti tag coimmunoprecipitation) | pubmed:26496610|imex | — |
| Cep120 | 0007(anti tag coimmunoprecipitation) | pubmed:26496610|imex | — |
| CSNK1E | 0007(anti tag coimmunoprecipitation) | pubmed:26496610|imex | — |
| Pcm1 | 0007(anti tag coimmunoprecipitation) | pubmed:26496610|imex | — |
| SLAIN2 | 0007(anti tag coimmunoprecipitation) | pubmed:26496610|imex | — |
| CEP43 | 0007(anti tag coimmunoprecipitation) | pubmed:26496610|imex | — |


**已知复合体成员** (GO Cellular Component):
- centriolar satellite (IDA:UniProtKB)
- centriolar subdistal appendage (IDA:UniProtKB)
- centrosome (IDA:UniProtKB)
- ciliary basal body (IDA:UniProtKB)
- microtubule organizing center (IDA:UniProtKB)

**PPI 互证分析**:
- STRING partners (score>0.4): 15
- IntAct 物理互作: 15
- 调控相关比例: 0/15 (0%)

**评价**: STRING综合分>0.7 (9条)，主要为预测

**评分: 4/10**。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 定位 | UniProt + HPA | Non-nuclear + Nucleoplasm/Nucleoli | 待确认 |
| 结构域 | InterPro + Pfam | 0个域 | 无注释 |
| PPI | STRING + IntAct | 15 + 15 | 数据充分 |

**互证加分明细**:
- PDB实验结构(1条目) (+1.0)
- IntAct实验互作丰富(15条) (+0.5)
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐ (79.5/100)

**核心优势**:
1. Extremely novel -- PubMed=7篇
2. HPA主定位核 + 转录因子功能，附加胞质信号

**风险/不确定性**:
1. HPA IF图像可进一步分析
2. 结构数据可接受

**下一步建议**:
- [ ] 获取 HPA IF 图像确认核定位
- [ ] 查阅最新关键文献补充功能细节
- [ ] 设计体外 DNA/染色质结合实验

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y6R9
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCDC61
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y6R9
- STRING: https://string-db.org/cgi/network?identifiers=CCDC61&species=9606

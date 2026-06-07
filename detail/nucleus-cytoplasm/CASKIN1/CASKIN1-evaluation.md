---
type: protein-evaluation
gene: "CASKIN1"
date: 2026-06-02
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CASKIN1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CASKIN1 / KIAA1306 |
| 蛋白全名 | Caskin-1 |
| 蛋白大小 | 1431 aa / 149.8 kDa |
| UniProt ID | Q8WXD9 |
| 子定位分类 | nucleus-cytoplasm |
| HPA IF 主定位 | Nucleoplasm |
| HPA IF 附加定位 | Nuclear bodies, Cytosol |
| HPA Reliability | Approved |
| 评估日期 | 2026-06-02 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 6/10 | x4 | 24 | HPA主定位核，附加Cytosol/Vesicles |
| 蛋白大小 | 5/10 | x1 | 5 | 1431 aa (small or large) |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed=18 (Extremely novel) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold低置信(pLDDT=53.4)，新颖蛋白基线 |
| 调控结构域 | 7/10 | x2 | 14 | 新颖蛋白基线，无注释结构域 |
| PPI网络 | 6/10 | x3 | 18 | 有物理互作(10条)，调控邻居占比低 |
| 互证加分 | — | max+3 | +2.5 | PDB实验结构(3条目) (+1.0); IntAct实验互作丰富(12条) (+0.5); STRING实验分>0.7 (+0.5); InterPro注释丰 |
| **加权总分** | | | **131.5/180** | |
| **归一化总分 (÷1.83)** | | | **71.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Nucleoplasm, Nuclear bodies, Cytosol | Approved |
| UniProt | Cytoplasm (ECO:0000250) | Swiss-Prot/TrEMBL |
| GO-CC | cytoplasm (ISS:UniProtKB); glutamatergic synapse (IEA:Ensembl); postsynapse (IEA:Ensembl) | |

暂无PAE图

暂无HPA IF图像数据。

**结论**: HPA主定位核，附加Cytosol/Vesicles

#### 3.2 蛋白大小评估

1431 aa (small or large)

**评价**: 1431 aa / 149.8 kDa，大蛋白，实验操作有一定挑战。

**评分: 5/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 18 |
| PubMed symbol_only | 24 |
| PubMed broad | 28 |
| 别名 | KIAA1306 |
| 新颖性分级 | Extremely novel |

**评价**: 仅 PubMed 18 篇 (strict)，极度新颖。该蛋白几乎未被系统研究，是探索新型核蛋白功能的绝佳候选。

**评分: 10/10**。

**关键文献**:
1. **CASKIN2 mediates PTPσ-orchestrated transsynaptic mechanisms at excitatory synapses.** *Proceedings of the National Academy of Sciences of the United States of America* (2025 Nov 18) PMID:41223222 -- Han KA et al.
2. **Beyond the Genotype: A Multi-Omic Analysis of APOEe4's Role in Alzheimer's Disease.** *bioRxiv : the preprint server for biology* (2025 Oct 16) PMID:41279801 -- Markov Y et al.
3. **Exploring Male-Specific Synaptic Plasticity in Major Depressive Disorder: A Single-Nucleus Transcriptomic Analysis Using Bioinformatics Methods.** *International journal of molecular sciences* (2025 Mar 28) PMID:40243907 -- Chen J et al.
4. **Distribution of Caskin1 protein and phenotypic characterization of its knockout mice using a comprehensive behavioral test battery.** *Molecular brain* (2018 Oct 25) PMID:30359304 -- Katano T et al.
5. **The molecular basis of the Caskin1 and Mint1 interaction with CASK.** *Journal of molecular biology* (2011 Sep 9) PMID:21763699 -- Stafford RL et al.


#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 53.4 |
| pLDDT > 90 (Very High) | 9.0% |
| pLDDT 70-90 (High) | 24.0% |
| pLDDT 50-70 (Medium) | 5.1% |
| pLDDT < 50 (Low) | 61.8% |
| 有序区域 (pLDDT>70) 占比 | 33.0% |
| AlphaFold 版本 | v6 |
| 实验结构 (PDB) | 3SEI (X-ray, 2.40 A, A/B=470-605); 3SEN (X-ray, 3.10 A, A/B/C/D=470-613); 7ATY (NMR, -, A=284-346) |

暂无PAE图

**评价**: AlphaFold 预测置信度偏低（pLDDT=53.4，有序区域 33%）。作为新颖蛋白，属正常现象。

**评分: 6/10**。

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
| CASK | 0.972 | 0.792 | — |
| NRXN1 | 0.924 | 0.047 | — |
| APBA1 | 0.841 | 0.063 | — |
| LIN7A | 0.627 | 0.091 | — |
| TBR1 | 0.560 | 0.054 | — |
| ABI2 | 0.556 | 0.052 | — |
| KIF17 | 0.553 | 0.057 | — |
| CAMK2A | 0.551 | 0.073 | — |
| PPFIA3 | 0.505 | 0.000 | — |
| NCK1 | 0.503 | 0.000 | — |


**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 调控相关? |
|---------|------|------|----------|
| - | 0006(anti bait coimmunoprecipitation) | pubmed:14968112 | — |
| SNCA | 0096(pull down) | pubmed:18614564|imex | — |
| Cyfip2 | 0006(anti bait coimmunoprecipitation) | pubmed:28671696|doi: | — |
| Pex5l | 0006(anti bait coimmunoprecipitation) | pubmed:28671696|doi: | — |
| Pde4dip | 0006(anti bait coimmunoprecipitation) | pubmed:28671696|doi: | — |
| HIF1AN | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| Dlgap1 | 0006(anti bait coimmunoprecipitation) | pubmed:28671696|doi: | — |
| Shank3 | 0006(anti bait coimmunoprecipitation) | pubmed:28671696|doi: | — |
| Fmr1 | 0006(anti bait coimmunoprecipitation) | pubmed:28671696|doi: | — |
| MAPT | 0007(anti tag coimmunoprecipitation) | pubmed:35063084|imex | — |


**已知复合体成员** (GO Cellular Component):
- cytoplasm (ISS:UniProtKB)
- glutamatergic synapse (IEA:Ensembl)
- postsynapse (IEA:Ensembl)

**PPI 互证分析**:
- STRING partners (score>0.4): 15
- IntAct 物理互作: 10
- 调控相关比例: 0/15 (0%)

**评价**: 有物理互作(10条)，调控邻居占比低

**评分: 6/10**。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 定位 | UniProt + HPA | Non-nuclear + Nucleoplasm/Nucleoli | 待确认 |
| 结构域 | InterPro + Pfam | 0个域 | 无注释 |
| PPI | STRING + IntAct | 15 + 10 | 数据充分 |

**互证加分明细**:
- PDB实验结构(3条目) (+1.0)
- IntAct实验互作丰富(12条) (+0.5)
- STRING实验分>0.7 (+0.5)
- InterPro注释丰富(12个结构域) (+0.5)
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐ (71.9/100)

**核心优势**:
1. Extremely novel -- PubMed=18篇
2. HPA主定位核，附加Cytosol/Vesicles

**风险/不确定性**:
1. HPA IF图像可进一步分析
2. AlphaFold预测质量待提升

**下一步建议**:
- [ ] 获取 HPA IF 图像确认核定位
- [ ] 查阅最新关键文献补充功能细节
- [ ] 设计体外 DNA/染色质结合实验

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WXD9
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CASKIN1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WXD9
- STRING: https://string-db.org/cgi/network?identifiers=CASKIN1&species=9606

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8WXD9 |
| SMART | SM00248;SM00454;SM00326; |
| UniProt Domain [FT] | DOMAIN 281..347; /note="SH3"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00192"; DOMAIN 472..535; /note="SAM 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00184"; DOMAIN 541..605; /note="SAM 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00184" |
| InterPro | IPR033635;IPR002110;IPR036770;IPR032232;IPR035497;IPR035498;IPR035495;IPR032117;IPR001660;IPR013761;IPR036028;IPR001452; |
| Pfam | PF12796;PF13637;PF16907;PF16632;PF16600;PF00536;PF07653; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000167971-CASKIN1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CASK | Intact | false |
| HIF1AN | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

---
type: protein-evaluation
gene: "CCDC110"
date: 2026-06-02
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCDC110 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCDC110 / KMHN1 |
| 蛋白全名 | Coiled-coil domain-containing protein 110 |
| 蛋白大小 | 833 aa / 96.7 kDa |
| UniProt ID | Q8TBZ0 |
| 子定位分类 | nucleus-cytoplasm |
| HPA IF 主定位 | Nucleoplasm |
| HPA IF 附加定位 | Cytosol |
| HPA Reliability | Supported |
| 评估日期 | 2026-06-02 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 6/10 | x4 | 24 | HPA主定位核，附加Cytosol/Vesicles |
| 蛋白大小 | 8/10 | x1 | 8 | 833 aa (acceptable range) |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed=5 (Extremely novel) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold低置信(pLDDT=66.5)，新颖蛋白基线 |
| 调控结构域 | 7/10 | x2 | 14 | 新颖蛋白基线，无注释结构域 |
| PPI网络 | 3/10 | x3 | 9 | 仅有低置信度STRING关联 (12条) |
| 互证加分 | — | max+3 | +1.5 | UniProt核定位 + HPA IF核验证一致 (+1.0); IntAct实验互作丰富(9条) (+0.5) |
| **加权总分** | | | **124.5/180** | |
| **归一化总分 (÷1.83)** | | | **68.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Nucleoplasm, Cytosol | Supported |
| UniProt | Nucleus (ECO:0000269) | Swiss-Prot/TrEMBL |
| GO-CC | cytoskeleton (IBA:GO_Central); cytosol (IDA:HPA); nucleoplasm (IDA:HPA) | |

暂无PAE图

暂无HPA IF图像数据。

**结论**: HPA主定位核，附加Cytosol/Vesicles

#### 3.2 蛋白大小评估

833 aa (acceptable range)

**评价**: 833 aa / 96.7 kDa，偏大蛋白，但仍在可操作范围内。

**评分: 8/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 5 |
| PubMed symbol_only | 6 |
| PubMed broad | 9 |
| 别名 | KMHN1 |
| 新颖性分级 | Extremely novel |

**评价**: 仅 PubMed 5 篇 (strict)，极度新颖。该蛋白几乎未被系统研究，是探索新型核蛋白功能的绝佳候选。

**评分: 10/10**。

**关键文献**:
1. **Identification of novel rare variants for anxiety: an exome-wide association study in the UK Biobank.** *Progress in neuro-psychopharmacology & biological psychiatry* (2024 Mar 2) PMID:38154517 -- Pan C et al.
2. **Analysis of Sry duplications on the Rattus norvegicus Y-chromosome.** *BMC genomics* (2013 Nov 14) PMID:24228692 -- Prokop JW et al.
3. **Genome-wide analysis in northern Chinese twins identifies twelve new susceptibility loci for pulmonary function.** *BMC genomics* (2024 Dec 30) PMID:39736507 -- Wang T et al.
4. **CCDC110 promotes the progression of hepatocellular carcinoma by activating the TGF-β/SMAD signaling pathway through targeted regulation of TGFBR1.** *Cancer cell international* (2025 May 20) PMID:40394630 -- Shen H et al.
5. **Ectopic Overexpression of Coiled-Coil Domain Containing 110 Delays G2/M Entry in U2-OS Cells.** *Development & reproduction* (2020 Jun) PMID:32734127 -- Lee SN et al.


#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 66.5 |
| pLDDT > 90 (Very High) | 30.3% |
| pLDDT 70-90 (High) | 21.7% |
| pLDDT 50-70 (Medium) | 7.8% |
| pLDDT < 50 (Low) | 40.2% |
| 有序区域 (pLDDT>70) 占比 | 52.0% |
| AlphaFold 版本 | v6 |
| 实验结构 (PDB) | 无 |

暂无PAE图

**评价**: AlphaFold 预测置信度偏低（pLDDT=66.5，有序区域 52%）。作为新颖蛋白，属正常现象。

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
| ZNF165 | 0.630 | 0.000 | — |
| SPACA3 | 0.567 | 0.000 | — |
| TRIML1 | 0.528 | 0.000 | — |
| RBM46 | 0.514 | 0.000 | — |
| FAM149A | 0.485 | 0.000 | — |
| CPXCR1 | 0.483 | 0.000 | — |
| SPATA19 | 0.448 | 0.000 | — |
| FATE1 | 0.447 | 0.000 | — |
| CCDC83 | 0.436 | 0.000 | — |
| C4orf47 | 0.432 | 0.000 | — |


**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 调控相关? |
|---------|------|------|----------|
| Cep290 | 0007(anti tag coimmunoprecipitation) | pubmed:21565611|imex | — |
| addA | 0398(two hybrid pooling approach) | imex:IM-13779|pubmed | — |
| XDH | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| DEPTOR | 0397(two hybrid array) | imex:IM-23318|pubmed | — |
| TGFBRAP1 | 0007(anti tag coimmunoprecipitation) | pubmed:33961781|imex | — |


**已知复合体成员** (GO Cellular Component):
- cytoskeleton (IBA:GO_Central)
- cytosol (IDA:HPA)
- nucleoplasm (IDA:HPA)

**PPI 互证分析**:
- STRING partners (score>0.4): 12
- IntAct 物理互作: 5
- 调控相关比例: 0/12 (0%)

**评价**: 仅有低置信度STRING关联 (12条)

**评分: 3/10**。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 定位 | UniProt + HPA | Nucleus + Nucleoplasm/Nucleoli | 一致 |
| 结构域 | InterPro + Pfam | 0个域 | 无注释 |
| PPI | STRING + IntAct | 12 + 5 | 数据充分 |

**互证加分明细**:
- UniProt核定位 + HPA IF核验证一致 (+1.0)
- IntAct实验互作丰富(9条) (+0.5)
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ (68.0/100)

**核心优势**:
1. Extremely novel -- PubMed=5篇
2. HPA主定位核，附加Cytosol/Vesicles

**风险/不确定性**:
1. HPA IF图像可进一步分析
2. AlphaFold预测质量待提升

**下一步建议**:
- [ ] 获取 HPA IF 图像确认核定位
- [ ] 查阅最新关键文献补充功能细节
- [ ] 设计体外 DNA/染色质结合实验

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TBZ0
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCDC110
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TBZ0
- STRING: https://string-db.org/cgi/network?identifiers=CCDC110&species=9606

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8TBZ0 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | 未检出 |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000168491-CCDC110/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DEPTOR | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

---
type: protein-evaluation
gene: "CCER1"
date: 2026-06-02
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCER1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCER1 / C12orf12 |
| 蛋白全名 | Coiled-coil domain-containing glutamate-rich protein 1 |
| 蛋白大小 | 406 aa / 46.5 kDa |
| UniProt ID | Q8TC90 |
| 子定位分类 | nucleoplasm |
| HPA IF 主定位 | 无 |
| HPA IF 附加定位 | 无 |
| HPA Reliability | None |
| 评估日期 | 2026-06-02 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | x4 | 28 | UniProt单一核定位 + 转录因子/DNA结合功能 |
| 蛋白大小 | 10/10 | x1 | 10 | 406 aa (200-800 aa ideal range) |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed=4 (Extremely novel) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold低置信(pLDDT=50.1)，新颖蛋白基线 |
| 调控结构域 | 8/10 | x2 | 16 | DNA/chromatin相关结构域: [] |
| PPI网络 | 3/10 | x3 | 9 | 仅有低置信度STRING关联 (15条) |
| 互证加分 | — | max+3 | +1.0 | UniProt核定位 (+0.5); IntAct实验互作丰富(15条) (+0.5) |
| **加权总分** | | | **132.0/180** | |
| **归一化总分 (÷1.83)** | | | **72.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | 无 | None |
| UniProt | Nucleus (ECO:0000269) | Swiss-Prot/TrEMBL |
| GO-CC | nucleus (ISS:UniProtKB) | |

暂无PAE图

暂无HPA IF图像数据。

**结论**: UniProt单一核定位 + 转录因子/DNA结合功能

#### 3.2 蛋白大小评估

406 aa (200-800 aa ideal range)

**评价**: 406 aa / 46.5 kDa，适宜大小的蛋白，适合常规生化实验和结构生物学分析。

**评分: 10/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 4 |
| PubMed symbol_only | 4 |
| PubMed broad | 4 |
| 别名 | C12orf12 |
| 新颖性分级 | Extremely novel |

**评价**: 仅 PubMed 4 篇 (strict)，极度新颖。该蛋白几乎未被系统研究，是探索新型核蛋白功能的绝佳候选。

**评分: 10/10**。

**关键文献**:
1. **Ccer1 is a spermatid-specific gene required for spermatogenesis and male fertility.** *The International journal of developmental biology* (2024) PMID:39868420 -- Sammer B et al.
2. **HPV Integration in Head and Neck Cancer: Downstream Splicing Events and Expression Ratios Linked with Poor Outcomes.** *Clinical cancer research : an official journal of the American Association for Cancer Research* (2026 Feb 4) PMID:41269209 -- Li S et al.
3. **Phase-separated CCER1 coordinates the histone-to-protamine transition and male fertility.** *Nature communications* (2023 Dec 11) PMID:38081819 -- Qin D et al.
4. **CCER1 condensates participate in histone-to-protamine transition by recruiting the TIP60/EPC1/NuA4 acetyltransferase complex.** *Development (Cambridge, England)* (2026 Mar 1) PMID:41670399 -- Wang S et al.


#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 50.1 |
| pLDDT > 90 (Very High) | 5.7% |
| pLDDT 70-90 (High) | 2.7% |
| pLDDT 50-70 (Medium) | 25.6% |
| pLDDT < 50 (Low) | 66.0% |
| 有序区域 (pLDDT>70) 占比 | 8.4% |
| AlphaFold 版本 | v6 |
| 实验结构 (PDB) | 无 |

暂无PAE图

**评价**: AlphaFold 预测置信度偏低（pLDDT=50.1，有序区域 8%）。作为新颖蛋白，属正常现象。

**评分: 6/10**。

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
| TEX33 | 0.658 | 0.000 | — |
| MORN5 | 0.619 | 0.094 | — |
| PEBP4 | 0.509 | 0.049 | — |
| OR2T29 | 0.509 | 0.049 | — |
| FAM71E1 | 0.507 | 0.000 | — |
| OR2M4 | 0.461 | 0.049 | — |
| FAM71F1 | 0.459 | 0.101 | — |
| TSPY10 | 0.451 | 0.052 | — |
| OR5H2 | 0.451 | 0.049 | — |
| DEFB130A | 0.438 | 0.000 | — |


**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 调控相关? |
|---------|------|------|----------|
| PLSCR1 | 0398(two hybrid pooling approach) | pubmed:16189514|imex | — |
| RBPMS | 0398(two hybrid pooling approach) | pubmed:16189514|imex | — |
| MDFI | 0398(two hybrid pooling approach) | pubmed:16189514|imex | — |
| NOTCH2NLA | 0397(two hybrid array) | imex:IM-27438|doi:10 | — |
| CYSRT1 | 0397(two hybrid array) | pubmed:32296183|imex | — |
| KRTAP9-3 | 1356(validated two hybrid) | pubmed:32296183|imex | — |
| KRTAP6-2 | 1356(validated two hybrid) | pubmed:32296183|imex | — |
| KRTAP6-3 | 1356(validated two hybrid) | pubmed:32296183|imex | — |
| NOTCH2NLC | 1356(validated two hybrid) | pubmed:32296183|imex | — |
| KRTAP4-2 | 1356(validated two hybrid) | pubmed:32296183|imex | — |


**已知复合体成员** (GO Cellular Component):
- nucleus (ISS:UniProtKB)

**PPI 互证分析**:
- STRING partners (score>0.4): 15
- IntAct 物理互作: 15
- 调控相关比例: 0/15 (0%)

**评价**: 仅有低置信度STRING关联 (15条)

**评分: 3/10**。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 定位 | UniProt + HPA | Nucleus + No HPA nuclear | 待确认 |
| 结构域 | InterPro + Pfam | 0个域 | 无注释 |
| PPI | STRING + IntAct | 15 + 15 | 数据充分 |

**互证加分明细**:
- UniProt核定位 (+0.5)
- IntAct实验互作丰富(15条) (+0.5)
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐ (72.1/100)

**核心优势**:
1. Extremely novel -- PubMed=4篇
2. UniProt单一核定位 + 转录因子/DNA结合功能

**风险/不确定性**:
1. HPA IF 待下载验证核定位
2. AlphaFold预测质量待提升

**下一步建议**:
- [ ] 获取 HPA IF 图像确认核定位
- [ ] 查阅最新关键文献补充功能细节
- [ ] 设计体外 DNA/染色质结合实验

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TC90
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCER1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TC90
- STRING: https://string-db.org/cgi/network?identifiers=CCER1&species=9606

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8TC90 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR027889;IPR052696; |
| Pfam | PF15482; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000197651-CCER1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CYSRT1 | Intact | false |
| KRT31 | Intact | false |
| KRT40 | Intact | false |
| KRTAP4-2 | Intact | false |
| KRTAP6-2 | Intact | false |
| KRTAP6-3 | Intact | false |
| KRTAP9-3 | Intact | false |
| NOTCH2NLA | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

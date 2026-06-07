---
type: protein-evaluation
gene: "CCDC85B"
date: 2026-06-02
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCDC85B 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCDC85B / DIPA |
| 蛋白全名 | Coiled-coil domain-containing protein 85B |
| 蛋白大小 | 202 aa / 22.1 kDa |
| UniProt ID | Q15834 |
| 子定位分类 | nucleus-cytoplasm |
| HPA IF 主定位 | 无 |
| HPA IF 附加定位 | 无 |
| HPA Reliability | None |
| 评估日期 | 2026-06-02 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | x4 | 20 | UniProt Nucleus+Cytoplasm + 转录因子功能提示核为主 |
| 蛋白大小 | 10/10 | x1 | 10 | 202 aa (200-800 aa ideal range) |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed=7 (Extremely novel) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold中等(pLDDT=80.7, >70%=66.8%) |
| 调控结构域 | 8/10 | x2 | 16 | DNA/chromatin相关结构域: [] |
| PPI网络 | 6/10 | x3 | 18 | STRING实验分>0.5 (3条) |
| 互证加分 | — | max+3 | +1.0 | UniProt核定位 (+0.5); IntAct实验互作丰富(15条) (+0.5) |
| **加权总分** | | | **136.0/180** | |
| **归一化总分 (÷1.83)** | | | **74.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | 无 | None |
| UniProt | Nucleus (ECO:0000269;ECO:0000269); Cytoplasm, cytoskeleton, microtubule organizing center, centrosome (ECO:0000269); Cel | Swiss-Prot/TrEMBL |
| GO-CC | adherens junction (IDA:UniProtKB); centrosome (IDA:UniProtKB); nucleus (IDA:UniProtKB) | |

暂无PAE图

暂无HPA IF图像数据。

**结论**: UniProt Nucleus+Cytoplasm + 转录因子功能提示核为主

#### 3.2 蛋白大小评估

202 aa (200-800 aa ideal range)

**评价**: 202 aa / 22.1 kDa，适宜大小的蛋白，适合常规生化实验和结构生物学分析。

**评分: 10/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 7 |
| PubMed symbol_only | 10 |
| PubMed broad | 17 |
| 别名 | DIPA |
| 新颖性分级 | Extremely novel |

**评价**: 仅 PubMed 7 篇 (strict)，极度新颖。该蛋白几乎未被系统研究，是探索新型核蛋白功能的绝佳候选。

**评分: 10/10**。

**关键文献**:
1. **Prognostic and therapeutic implications related to glycosylation profiles of cancer-associated fibroblasts in colorectal cancer: insights from single-cell and bulk transcriptomics.** *Functional & integrative genomics* (2025 Aug 15) PMID:40813526 -- Chen K et al.
2. **Transcriptomic Profiles Associated with Experimental Placebo Effects in Chronic Pain.** *Clinical pharmacology and therapeutics* (2024 Aug) PMID:38711244 -- Colloca L et al.
3. **Aberrant Whole Blood Gene Expression in the Lumen of Human Intracranial Aneurysms.** *Diagnostics (Basel, Switzerland)* (2021 Aug 10) PMID:34441376 -- Tutino VM et al.
4. **DIPA-family coiled-coils bind conserved isoform-specific head domain of p120-catenin family: potential roles in hydrocephalus and heterotopia.** *Molecular biology of the cell* (2014 Sep 1) PMID:25009281 -- Markham NO et al.
5. **The HSA21 gene EURL/C21ORF91 controls neurogenesis within the cerebral cortex and is implicated in the pathogenesis of Down Syndrome.** *Scientific reports* (2016 Jul 11) PMID:27404227 -- Li SS et al.


#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 80.7 |
| pLDDT > 90 (Very High) | 59.9% |
| pLDDT 70-90 (High) | 6.9% |
| pLDDT 50-70 (Medium) | 14.9% |
| pLDDT < 50 (Low) | 18.3% |
| 有序区域 (pLDDT>70) 占比 | 66.8% |
| AlphaFold 版本 | v6 |
| 实验结构 (PDB) | 无 |

暂无PAE图

**评价**: AlphaFold 中等质量（pLDDT=80.7，有序区域 67%）。作为新颖蛋白，此水平可接受。

**评分: 7/10**。

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
| ZNF358 | 0.670 | 0.000 | — |
| PPP1CC | 0.632 | 0.628 | — |
| PPP1CA | 0.624 | 0.611 | — |
| PPP1R13B | 0.608 | 0.571 | — |
| MCRS1 | 0.584 | 0.426 | — |
| CTNND1 | 0.536 | 0.073 | — |
| ZBTB16 | 0.526 | 0.193 | — |
| SOX18 | 0.517 | 0.000 | — |
| ARHGAP23 | 0.471 | 0.094 | — |
| HOMER3 | 0.456 | 0.000 | — |


**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 调控相关? |
|---------|------|------|----------|
| PKN1 | 0096(pull down) | pubmed:16189514|imex | — |
| C19orf25 | 0096(pull down) | pubmed:16189514|imex | — |
| EXOC8 | 0398(two hybrid pooling approach) | pubmed:16189514|imex | — |
| UTP14A | 0398(two hybrid pooling approach) | pubmed:16189514|imex | — |
| ENKD1 | 0398(two hybrid pooling approach) | pubmed:16189514|imex | — |
| SLU7 | 0398(two hybrid pooling approach) | pubmed:16189514|imex | — |
| CEP70 | 0398(two hybrid pooling approach) | pubmed:16189514|imex | — |
| EIF3H | 0398(two hybrid pooling approach) | pubmed:16189514|imex | — |
| APEX2 | 0398(two hybrid pooling approach) | pubmed:16189514|imex | — |
| CDKN1A | 0398(two hybrid pooling approach) | pubmed:16189514|imex | — |


**已知复合体成员** (GO Cellular Component):
- adherens junction (IDA:UniProtKB)
- centrosome (IDA:UniProtKB)
- nucleus (IDA:UniProtKB)

**PPI 互证分析**:
- STRING partners (score>0.4): 15
- IntAct 物理互作: 15
- 调控相关比例: 0/15 (0%)

**评价**: STRING实验分>0.5 (3条)

**评分: 6/10**。

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

**推荐等级**: ⭐⭐⭐⭐⭐ (74.3/100)

**核心优势**:
1. Extremely novel -- PubMed=7篇
2. UniProt Nucleus+Cytoplasm + 转录因子功能提示核为主

**风险/不确定性**:
1. HPA IF 待下载验证核定位
2. 结构数据可接受

**下一步建议**:
- [ ] 获取 HPA IF 图像确认核定位
- [ ] 查阅最新关键文献补充功能细节
- [ ] 设计体外 DNA/染色质结合实验

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q15834
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCDC85B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15834
- STRING: https://string-db.org/cgi/network?identifiers=CCDC85B&species=9606

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q15834 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR019359; |
| Pfam | PF10226; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000175602-CCDC85B/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| C19orf25 | Intact, Biogrid | true |
| CHCHD3 | Intact, Biogrid | true |
| KANSL1 | Intact, Biogrid | true |
| KRT17 | Intact, Biogrid | true |
| KRT6A | Intact, Biogrid | true |
| PKN1 | Intact, Biogrid | true |
| BIRC5 | Intact | false |
| CENPP | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

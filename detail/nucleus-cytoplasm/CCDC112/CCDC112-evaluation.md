---
type: protein-evaluation
gene: "CCDC112"
date: 2026-06-02
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCDC112 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCDC112 / MBC1 |
| 蛋白全名 | Coiled-coil domain-containing protein 112 |
| 蛋白大小 | 446 aa / 53.6 kDa |
| UniProt ID | Q8NEF3 |
| 子定位分类 | nucleus-cytoplasm |
| HPA IF 主定位 | Plasma membrane, Cytosol |
| HPA IF 附加定位 | Nucleoplasm |
| HPA Reliability | Approved |
| 评估日期 | 2026-06-02 |

### 2. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16 | HPA核为附加定位，主定位非核 |
| 蛋白大小 | 10/10 | x1 | 10 | 446 aa (200-800 aa ideal range) |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed=7 (Extremely novel) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold中等(pLDDT=81.6, >70%=80.7%) |
| 调控结构域 | 7/10 | x2 | 14 | 新颖蛋白基线，无注释结构域 |
| PPI网络 | 6/10 | x3 | 18 | STRING实验分>0.5 (1条) |
| 互证加分 | — | max+3 | +0.5 | IntAct实验互作丰富(15条) (+0.5) |
| **加权总分** | | | **129.5/180** | |
| **归一化总分 (÷1.83)** | | | **70.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA (IF) | Nucleoplasm, Plasma membrane, Cytosol | Approved |
| UniProt | Cytoplasm, cytoskeleton, microtubule organizing center, centrosome, centriolar satellite (ECO:0000269) | Swiss-Prot/TrEMBL |
| GO-CC | centriolar satellite (IDA:UniProtKB) | |

暂无PAE图

暂无HPA IF图像数据。

**结论**: HPA核为附加定位，主定位非核

#### 3.2 蛋白大小评估

446 aa (200-800 aa ideal range)

**评价**: 446 aa / 53.6 kDa，适宜大小的蛋白，适合常规生化实验和结构生物学分析。

**评分: 10/10**。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict_count | 7 |
| PubMed symbol_only | 11 |
| PubMed broad | 11 |
| 别名 | MBC1 |
| 新颖性分级 | Extremely novel |

**评价**: 仅 PubMed 7 篇 (strict)，极度新颖。该蛋白几乎未被系统研究，是探索新型核蛋白功能的绝佳候选。

**评分: 10/10**。

**关键文献**:
1. **Single-Cell RNA Sequencing Analysis Reveals Sequential Cell Fate Transition during Human Spermatogenesis.** *Cell stem cell* (2018 Oct 4) PMID:30174296 -- Wang M et al.
2. **A novel mechanism of sperm midpiece epididymal maturation and the role of CCDC112 in sperm midpiece formation and establishing an optimal flagella waveform.** *Cell communication and signaling : CCS* (2025 Jul 1) PMID:40598224 -- Graffeo ML et al.
3. **A novel CCDC112-dependent process of sperm midpiece formation and epididymal maturation.** *bioRxiv : the preprint server for biology* (2024 Nov 5) PMID:39574653 -- Graffeo ML et al.
4. **Comprehensive DNA methylation profiling of COVID-19 and hepatocellular carcinoma to identify common pathogenesis and potential therapeutic targets.** *Clinical epigenetics* (2023 Jun 12) PMID:37309005 -- Luo H et al.
5. **The Functionally Unannotated Proteome of Human Male Tissues: A Shared Resource to Uncover New Protein Functions Associated with Reproductive Biology.** *Journal of proteome research* (2020 Dec 4) PMID:33064489 -- Vandenbrouck Y et al.


#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 81.6 |
| pLDDT > 90 (Very High) | 42.6% |
| pLDDT 70-90 (High) | 38.1% |
| pLDDT 50-70 (Medium) | 11.4% |
| pLDDT < 50 (Low) | 7.8% |
| 有序区域 (pLDDT>70) 占比 | 80.7% |
| AlphaFold 版本 | v6 |
| 实验结构 (PDB) | 无 |

暂无PAE图

**评价**: AlphaFold 中等质量（pLDDT=81.6，有序区域 81%）。作为新颖蛋白，此水平可接受。

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
| TEX9 | 0.869 | 0.698 | — |
| ESYT1 | 0.774 | 0.080 | — |
| PGGT1B | 0.720 | 0.056 | — |
| TEX29 | 0.669 | 0.000 | — |
| MCOLN3 | 0.505 | 0.000 | — |
| CCDC14 | 0.496 | 0.101 | — |
| NEXMIF | 0.444 | 0.000 | — |
| ODF2L | 0.443 | 0.100 | — |
| LTBR | 0.441 | 0.422 | — |
| KIAA0753 | 0.438 | 0.000 | — |


**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 调控相关? |
|---------|------|------|----------|
| LURAP1 | 0398(two hybrid pooling approach) | pubmed:16189514|imex | — |
| TEX9 | 0398(two hybrid pooling approach) | pubmed:16189514|imex | — |
| CCDC85B | 0398(two hybrid pooling approach) | pubmed:16189514|imex | — |
| FSD2 | 0397(two hybrid array) | imex:IM-23318|pubmed | — |
| TNIP1 | 0397(two hybrid array) | imex:IM-23318|pubmed | — |
| KRT31 | 0397(two hybrid array) | imex:IM-23318|pubmed | — |
| KRT40 | 0397(two hybrid array) | imex:IM-23318|pubmed | — |
| CINP | 1356(validated two hybrid) | pubmed:32296183|imex | — |
| TRIM44 | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |
| TNFRSF8 | 0007(anti tag coimmunoprecipitation) | pubmed:28514442|doi: | — |


**已知复合体成员** (GO Cellular Component):
- centriolar satellite (IDA:UniProtKB)

**PPI 互证分析**:
- STRING partners (score>0.4): 12
- IntAct 物理互作: 11
- 调控相关比例: 0/12 (0%)

**评价**: STRING实验分>0.5 (1条)

**评分: 6/10**。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 定位 | UniProt + HPA | Non-nuclear + Nucleoplasm/Nucleoli | 待确认 |
| 结构域 | InterPro + Pfam | 0个域 | 无注释 |
| PPI | STRING + IntAct | 12 + 11 | 数据充分 |

**互证加分明细**:
- IntAct实验互作丰富(15条) (+0.5)
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐ (70.8/100)

**核心优势**:
1. Extremely novel -- PubMed=7篇
2. HPA核为附加定位，主定位非核

**风险/不确定性**:
1. HPA IF图像可进一步分析
2. 结构数据可接受

**下一步建议**:
- [ ] 获取 HPA IF 图像确认核定位
- [ ] 查阅最新关键文献补充功能细节
- [ ] 设计体外 DNA/染色质结合实验

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NEF3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCDC112
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NEF3
- STRING: https://string-db.org/cgi/network?identifiers=CCDC112&species=9606

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8NEF3 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR039902; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000164221-CCDC112/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| LURAP1 | Intact, Biogrid | true |
| TEX9 | Intact, Biogrid | true |
| FSD2 | Intact | false |
| KRT31 | Intact | false |
| KRT40 | Intact | false |
| PCM1 | Biogrid | false |
| TNIP1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

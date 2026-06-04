---
type: protein-evaluation
gene: "DYNLRB2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DYNLRB2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DYNLRB2 |
| 蛋白名称 | Dynein light chain roadblock-type 2 |
| 蛋白大小 | 125 aa / 13.9 kDa |
| UniProt ID | H3BQI1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm, cytoskeleton |
| 蛋白大小 | 8/10 | ×1 | 8 | 125 aa / 13.9 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=32 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=78.4; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 16 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **99.0/180** | |
| **归一化总分** | | | **55.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | No data |
| UniProt | Cytoplasm, cytoskeleton | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 32 |
| PubMed broad count | 34 |
| 别名(未计入scoring) |  |

**关键文献**:
1. CRISPR knockout screens reveal genes and pathways essential for neuronal differentiation and implicate PEDS1 in neurodevelopment.. *Nat Neurosci*. PMID: 41491239
2. VPA targets Mid1 to improve disrupted retrograde axonal transport in hippocampal neurons and alleviate lithium manganate-induced learning and memory dysfunction.. *J Adv Res*. PMID: 41651028
3. Genome-Wide Association Study of First-Parity Reproductive Traits in Suzi Pig.. *Genes (Basel)*. PMID: 41300787
4. Genome-Wide Association Analyses in Family Triads and Dyads Following Assisted Reproductive Technology.. *Genet Epidemiol*. PMID: 40457613
5. Identification and bioinformatics analysis of cilia-associated gene families in Euplotes amieti (Ciliophora, Hypotrichia).. *Front Microbiol*. PMID: 40432967

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.4 |
| 高置信度残基 (pLDDT>90) 占比 | 22.4% |
| 置信残基 (pLDDT 70-90) 占比 | 50.4% |
| 中等置信 (pLDDT 50-70) 占比 | 20.8% |
| 低置信 (pLDDT<50) 占比 | 6.4% |
| 有序区域 (pLDDT>70) 占比 | 72.8% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 中等质量（pLDDT=78.4，有序区 72.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TCTEX1D2 | 0.000 | 0.000 | — |
| DYNLT1 | 0.000 | 0.000 | — |
| DYNLT3 | 0.000 | 0.000 | — |
| WDR34 | 0.000 | 0.000 | — |
| WDR60 | 0.000 | 0.000 | — |
| DYNLL1 | 0.000 | 0.000 | — |
| DYNC1I1 | 0.000 | 0.000 | — |
| DYNLL2 | 0.000 | 0.000 | — |
| DYNC1I2 | 0.000 | 0.000 | — |
| DYNC2H1 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:P35579 | psi-mi:"MI:0030"(cross-linking study) | pubmed:- |
| uniprotkb:Q8TF09 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:- |
| uniprotkb:Q8WW35 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:- |
| uniprotkb:Q96EX3 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:- |
| uniprotkb:Q6P1K8 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:- |
| uniprotkb:Q8WVS4 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P63172 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q2M1P5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P43034 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 16
- 调控相关比例: 1 / 20 = 5%

**评价**: STRING 25 个预测互作，IntAct 16 个实验互作。调控相关配体占比 5%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.4 + PDB: 无 | pLDDT=78.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 25 + 16 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. DYNLRB2 — Dynein light chain roadblock-type 2，非常新颖，仅有少数基础研究。
2. 蛋白大小125 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 32 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/H3BQI1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000168589-DYNLRB2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DYNLRB2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/H3BQI1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

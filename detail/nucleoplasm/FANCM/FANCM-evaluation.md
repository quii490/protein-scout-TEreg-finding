---
type: protein-evaluation
gene: "FANCM"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FANCM — REJECTED (研究热度过高 (PubMed strict=231，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FANCM / KIAA1596 |
| 蛋白名称 | Fanconi anemia group M protein |
| 蛋白大小 | 2048 aa / 232.2 kDa |
| UniProt ID | Q8IYD8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 2/10 | ×1 | 2 | 2048 aa / 232.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=231 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=51.7; PDB: 4BXO, 4DAY, 4DRB, 4E45, 4M6W, 9EL5, 9HJO |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011545, IPR006166, IPR031879, IPR039686, IPR044 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **73.5/180** | |
| **归一化总分** | | | **40.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- FANCM-MHF complex (GO:0071821)
- Fanconi anaemia nuclear complex (GO:0043240)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 231 |
| PubMed broad count | 420 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1596 |

**关键文献**:
1. Fanconi Anemia.. **. PMID: 20301575
2. FANCM regulates repair pathway choice at stalled replication forks.. *Molecular cell*. PMID: 33882298
3. Bloom syndrome.. *International journal of dermatology*. PMID: 24602044
4. FANCM branchpoint translocase: Master of traverse, reverse and adverse DNA repair.. *DNA repair*. PMID: 38878565
5. Structural basis of Fanconi anemia pathway activation by FANCM.. *The EMBO journal*. PMID: 40447800

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 51.7 |
| 高置信度残基 (pLDDT>90) 占比 | 12.7% |
| 置信残基 (pLDDT 70-90) 占比 | 23.2% |
| 中等置信 (pLDDT 50-70) 占比 | 3.8% |
| 低置信 (pLDDT<50) 占比 | 60.4% |
| 有序区域 (pLDDT>70) 占比 | 35.9% |
| 可用 PDB 条目 | 4BXO, 4DAY, 4DRB, 4E45, 4M6W, 9EL5, 9HJO |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=51.7），有序残基占 35.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011545, IPR006166, IPR031879, IPR039686, IPR044749; Pfam: PF00270, PF02732, PF16783 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FAAP20 | 0.999 | 0.994 | — |
| TOP3A | 0.999 | 0.996 | — |
| FANCL | 0.999 | 0.994 | — |
| FAAP100 | 0.999 | 0.994 | — |
| RMI1 | 0.999 | 0.999 | — |
| RMI2 | 0.999 | 0.999 | — |
| FANCG | 0.999 | 0.994 | — |
| BLM | 0.999 | 0.999 | — |
| FANCA | 0.999 | 0.994 | — |
| CENPX | 0.999 | 0.999 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| CUL4B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:23238014|imex:IM-18592 |
| FAAP24 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| COX5B | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| PLEC | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| EME1 | psi-mi:"MI:0096"(pull down) | pubmed:17289582|imex:IM-25488 |
| RMI1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17289582|imex:IM-25488 |
| FANCE | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17289582|imex:IM-25488 |
| FANCC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17289582|imex:IM-25488 |
| FANCF | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17289582|imex:IM-25488 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=51.7 + PDB: 4BXO, 4DAY, 4DRB, 4E45, 4M6W,  | pLDDT=51.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. FANCM — Fanconi anemia group M protein，研究基础较多，新颖性有限。
2. 蛋白大小2048 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 231 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=51.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 231 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IYD8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000187790-FANCM/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FANCM
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IYD8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IYD8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8IYD8 |
| SMART | SM00487;SM00891;SM00490; |
| UniProt Domain [FT] | DOMAIN 98..266; /note="Helicase ATP-binding"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00541"; DOMAIN 452..627; /note="Helicase C-terminal"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00542" |
| InterPro | IPR011545;IPR006166;IPR031879;IPR039686;IPR044749;IPR014001;IPR001650;IPR027417;IPR011335;IPR010994;IPR047418; |
| Pfam | PF00270;PF02732;PF16783;PF00271; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000187790-FANCM/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CENPS | Intact, Biogrid, Bioplex | true |
| FAAP24 | Intact, Biogrid, Bioplex | true |
| BLM | Biogrid | false |
| CENPX | Biogrid | false |
| COX5B | Biogrid | false |
| FAAP100 | Biogrid | false |
| FAAP20 | Biogrid | false |
| FANCA | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

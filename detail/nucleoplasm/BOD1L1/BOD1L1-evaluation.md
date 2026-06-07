---
type: protein-evaluation
gene: "BOD1L1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BOD1L1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BOD1L1 / BOD1L, FAM44A, KIAA1327 |
| 蛋白名称 | Biorientation of chromosomes in cell division protein 1-like 1 |
| 蛋白大小 | 3051 aa / 330.5 kDa |
| UniProt ID | Q8NFC6 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 03:42:10 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 10/10 | x4 | 40 | HPA: Nucleoplasm; UniProt: Chromosome |
| 蛋白大小 | 2/10 | x1 | 2 | 3051 aa / 330.5 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=8 篇 (<=20->10) |
| 三维结构 | 1/10 | x3 | 3 | AlphaFold pLDDT 不可用 |
| 调控结构域 | 5/10 | x2 | 10 | InterPro: 2; Pfam: 1; IPR055264, IPR043244 |
| PPI 网络 | 10/10 | x3 | 30 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 1.0 | 多库定位一致 (3源): +0.5; STRING + IntAct 双源验证: +0.5 |
| **原始总分** | | | **136.0/180** | |
| **归一化总分 (/1.83)** | | | **74.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoplasm | Approved |
| UniProt | Chromosome | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- chromosome (GO:0005694)
- nucleoplasm (GO:0005654)
- Set1C/COMPASS complex (GO:0048188)

**结论**: 核定位证据充分，多个数据源一致支持核定位，定位特异性高。

#### 3.2 蛋白大小评估

**评价**: 3051 aa，蛋白偏大（> 1200 aa），表达纯化难度增加，但结构域丰富。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed broad count | 9 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BOD1L, FAM44A, KIAA1327 |

**关键文献**:
1. A Polygenic Risk Score for Late Bladder Toxicity Following Radiotherapy for Non-Metastatic Prostate Cancer.. *Cancer epidemiology, biomarkers & prevention : a publication of the American Association for Cancer Research, cosponsored by the American Society of Preventive Oncology*. PMID: 40029246
2. Causal and Candidate Gene Variants in a Large Cohort of Women With Primary Ovarian Insufficiency.. *The Journal of clinical endocrinology and metabolism*. PMID: 34718612
3. An Aurora kinase A-BOD1L1-PP2A B56 Axis promotes chromosome segregation fidelity.. *bioRxiv : the preprint server for biology*. PMID: 37609141
4. Identification of Potentially Novel Molecular Targets of Endometrial Cancer Using a Non-Biased Proteomic Approach.. *Cancers*. PMID: 37760635
5. Identification of Gene Coexpression Modules and Prognostic Genes Associated with Papillary Thyroid Cancer.. *Journal of oncology*. PMID: 36245994

**评价**: 极度新颖，几乎未被系统研究（PubMed <= 20篇）。新颖性评分 10/10。

#### 3.4 三维结构分析

**AlphaFold pLDDT 统计数据不可用（获取失败）。**

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: 三维结构数据有限。三维结构评分 1/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR055264, IPR043244; Pfam: PF05205 |

**染色质调控潜力分析**: 存在 3 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score > 0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CXXC1 | 0.928 | 0.835 | -- |
| SETD1A | 0.927 | 0.628 | -- |
| RBBP5 | 0.915 | 0.777 | -- |
| WDR5 | 0.885 | 0.729 | -- |
| HCFC2 | 0.851 | 0.688 | -- |
| ASH2L | 0.848 | 0.620 | -- |
| SETD1B | 0.761 | 0.316 | -- |
| PAXIP1 | 0.706 | 0.237 | -- |
| WDR82 | 0.698 | 0.000 | -- |
| HCFC1 | 0.686 | 0.316 | -- |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| VAV2 | two hybrid | imex:IM-13772|pubmed:18654987 |
| DLEC1 | cross-linking study | pubmed:30021884|imex:IM-26653|doi:10.1074/mcp.ra118.000924 |
| CNPY3 | cross-linking study | pubmed:30021884|imex:IM-26653|doi:10.1074/mcp.ra118.000924 |
| H1-2 | cross-linking study | pubmed:30021884|imex:IM-26653|doi:10.1074/mcp.ra118.000924 |
| M | anti tag coimmunoprecipitation | imex:IM-27674|pubmed:33208464 |
| PLEKHA7 | anti bait coimmunoprecipitation | imex:IM-25739|pubmed:28877994 |
| NUP50 | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| EPB41L5 | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| WDR5 | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| CAMK2D | anti tag coimmunoprecipitation | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15

**评价**: 互作网络丰富：STRING 15 预测 + IntAct 15 实验互作。PPI 评分 10/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | -- | 不可用 | -- |
| 定位 | HPA | Nucleoplasm | 单一来源 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
**总分**: +1.0 / max +3

### 4. 总体评价

**归一化总分**: 74.3/100

**核心优势**:
1. BOD1L1 -- Biorientation of chromosomes in cell division protein 1-like 1，极度新颖，几乎未被系统研究（PubMed <= 20篇）。
2. 存在 3 个已知结构域，有明确的结构-功能切入点。
3. 核定位信号明确，多个数据源一致支持。

**风险/不确定性**:
1. 暂无PDB实验结构，结构证据完全依赖AlphaFold预测
2. 蛋白偏大（3051 aa），表达纯化难度大

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] 考虑通过AlphaFold预测 + MD模拟获取结构信息

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q8NFC6
- Protein Atlas: https://www.proteinatlas.org/search/BOD1L1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BOD1L1
- STRING: https://string-db.org/network/9606.BOD1L1
- Packet data timestamp: 2026-06-03 03:42:10

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000038219-BOD1L1/subcellular

![](https://images.proteinatlas.org/37362/430_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/37362/430_G1_2_red_green.jpg)
![](https://images.proteinatlas.org/37362/432_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/37362/432_G1_2_red_green.jpg)
![](https://images.proteinatlas.org/37362/441_G1_1_red_green.jpg)
![](https://images.proteinatlas.org/37362/441_G1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8NFC6 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR055264;IPR043244; |
| Pfam | PF05205; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000038219-BOD1L1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HCFC2 | Biogrid, Bioplex | true |
| WDR5 | Intact, Biogrid | true |
| ASH2L | Biogrid | false |
| BRD4 | Biogrid | false |
| CXXC1 | Biogrid | false |
| EIF4B | Biogrid | false |
| HCFC1 | Biogrid | false |
| HNRNPAB | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

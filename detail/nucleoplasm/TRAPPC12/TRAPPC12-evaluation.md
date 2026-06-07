---
type: protein-evaluation
gene: "TRAPPC12"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TRAPPC12 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TRAPPC12 / TRAMM, TTC15 |
| 蛋白名称 | Trafficking protein particle complex subunit 12 |
| 蛋白大小 | 735 aa / 79.4 kDa |
| UniProt ID | Q8WVT3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Golgi apparatus; UniProt: Endoplasmic reticulum-Golgi intermediate compartment; Nucleu |
| 蛋白大小 | 10/10 | ×1 | 10 | 735 aa / 79.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011990, IPR019734; Pfam: PF14559, PF13174 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Golgi apparatus | Supported |
| UniProt | Endoplasmic reticulum-Golgi intermediate compartment; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- endoplasmic reticulum-Golgi intermediate compartment (GO:0005793)
- Golgi apparatus (GO:0005794)
- kinetochore (GO:0000776)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- TRAPP complex (GO:0030008)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 22 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TRAMM, TTC15 |

**关键文献**:
1. Mammalian TRAPPIII Complex positively modulates the recruitment of Sec13/31 onto COPII vesicles.. *Scientific reports*. PMID: 28240221
2. Distinct Roles of TRAPPC8 and TRAPPC12 in Ciliogenesis via Their Interactions With OFD1.. *Frontiers in cell and developmental biology*. PMID: 32258032
3. Integrative Approaches Identify Genetic Determinants of Levodopa Induced Dyskinesia.. *Molecular neurobiology*. PMID: 40299300
4. Genome-wide pleiotropy analysis of neuropathological traits related to Alzheimer's disease.. *Alzheimer's research & therapy*. PMID: 29458411
5. Expanding Clinical Phenotype of TRAPPC12-Related Childhood Encephalopathy: Two Cases and Review of Literature.. *Neuropediatrics*. PMID: 32369837

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.9 |
| 高置信度残基 (pLDDT>90) 占比 | 37.3% |
| 置信残基 (pLDDT 70-90) 占比 | 20.7% |
| 中等置信 (pLDDT 50-70) 占比 | 2.3% |
| 低置信 (pLDDT<50) 占比 | 39.7% |
| 有序区域 (pLDDT>70) 占比 | 58.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=66.9），有序残基占 58.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011990, IPR019734; Pfam: PF14559, PF13174 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TRAPPC8 | 0.999 | 0.838 | — |
| TRAPPC11 | 0.999 | 0.854 | — |
| TRAPPC13 | 0.998 | 0.811 | — |
| TRAPPC2L | 0.997 | 0.823 | — |
| TRAPPC3 | 0.997 | 0.834 | — |
| TRAPPC2 | 0.997 | 0.820 | — |
| TRAPPC4 | 0.996 | 0.786 | — |
| TRAPPC5 | 0.994 | 0.785 | — |
| TRAPPC6B | 0.992 | 0.828 | — |
| TRAPPC1 | 0.991 | 0.837 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| comEC | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| HUB1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| HSP23.6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| GAMMACA2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| NAC59 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| FES1C | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| T12E18_80 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| LSU1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| TRFL5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| AHK2 | psi-mi:"MI:0018"(two hybrid) | pubmed:18642946 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.9 + PDB: 无 | pLDDT=66.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum-Golgi intermediate compartme / Nucleoplasm, Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TRAPPC12 — Trafficking protein particle complex subunit 12，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小735 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=66.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8WVT3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000171853-TRAPPC12/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TRAPPC12
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8WVT3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000171853-TRAPPC12/subcellular

![](https://images.proteinatlas.org/43196/712_B3_2_red_green.jpg)
![](https://images.proteinatlas.org/43196/712_B3_3_red_green.jpg)
![](https://images.proteinatlas.org/43196/804_B3_1_red_green.jpg)
![](https://images.proteinatlas.org/43196/804_B3_2_red_green.jpg)
![](https://images.proteinatlas.org/43196/964_B3_1_red_green.jpg)
![](https://images.proteinatlas.org/43196/964_B3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8WVT3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8WVT3 |
| SMART | SM00028; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR011990;IPR019734; |
| Pfam | PF14559;PF13174; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000171853-TRAPPC12/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| TRAPPC1 | Biogrid, Opencell, Bioplex | true |
| TRAPPC11 | Biogrid, Opencell, Bioplex | true |
| TRAPPC2 | Biogrid, Opencell | true |
| TRAPPC4 | Biogrid, Bioplex | true |
| TRAPPC6B | Biogrid, Bioplex | true |
| LIN7B | Intact | false |
| TRAPPC2L | Biogrid | false |
| TRAPPC3 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

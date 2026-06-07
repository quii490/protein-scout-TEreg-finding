---
type: protein-evaluation
gene: "LINS1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## LINS1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LINS1 / LINS, WINS1 |
| 蛋白名称 | Protein Lines homolog 1 |
| 蛋白大小 | 757 aa / 85.9 kDa |
| UniProt ID | Q8NG48 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 757 aa / 85.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=71.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR029415, IPR032794, IPR024875; Pfam: PF14695, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.0/180** | |
| **归一化总分** | | | **73.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 14 |
| PubMed broad count | 40 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: LINS, WINS1 |

**关键文献**:
1. Domain-specific phenotypes in LINS1-related disorder-A Chinese family with the Q92X variant and literature review.. *American journal of medical genetics. Part C, Seminars in medical genetics*. PMID: 38563234
2. Hyd/UBR5 defines a tumor suppressor pathway that links Polycomb repressive complex to regulated protein degradation in tissue growth control and tumorigenesis.. *Genes & development*. PMID: 39137945
3. LINS1-associated neurodevelopmental disorder: Family with novel mutation expands the phenotypic spectrum.. *Neurology. Genetics*. PMID: 32802957
4. Identification of a novel nonsense homozygous mutation of LINS1 gene in two sisters with intellectual disability, schizophrenia, and anxiety.. *Biomedical journal*. PMID: 34450347
5. Novel LINS1 missense mutation in a family with non-syndromic intellectual disability.. *American journal of medical genetics. Part A*. PMID: 28181389

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.4 |
| 高置信度残基 (pLDDT>90) 占比 | 38.7% |
| 置信残基 (pLDDT 70-90) 占比 | 26.4% |
| 中等置信 (pLDDT 50-70) 占比 | 9.4% |
| 低置信 (pLDDT<50) 占比 | 25.5% |
| 有序区域 (pLDDT>70) 占比 | 65.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=71.4，有序区 65.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029415, IPR032794, IPR024875; Pfam: PF14695, PF14694 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PLRG1 | 0.630 | 0.625 | — |
| PRPF19 | 0.623 | 0.623 | — |
| MT-CO1 | 0.597 | 0.000 | — |
| POLR2B | 0.575 | 0.000 | — |
| PFAS | 0.542 | 0.000 | — |
| BCAS2 | 0.479 | 0.479 | — |
| THAP6 | 0.455 | 0.000 | — |
| RBM48 | 0.449 | 0.000 | — |
| MT-CYB | 0.447 | 0.000 | — |
| NPAT | 0.443 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PLRG1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| BCAS2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PRPF19 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ENST00000314742 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.4 + PDB: 无 | pLDDT=71.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. LINS1 — Protein Lines homolog 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小757 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 14 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NG48
- Protein Atlas: https://www.proteinatlas.org/ENSG00000140471-LINS1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LINS1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NG48
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000140471-LINS1/subcellular

![](https://images.proteinatlas.org/38578/1177_B1_1_red_green.jpg)
![](https://images.proteinatlas.org/38578/1177_B1_4_red_green.jpg)
![](https://images.proteinatlas.org/38578/537_B12_1_red_green.jpg)
![](https://images.proteinatlas.org/38578/537_B12_2_red_green.jpg)
![](https://images.proteinatlas.org/38578/540_B12_1_red_green.jpg)
![](https://images.proteinatlas.org/38578/540_B12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NG48-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8NG48 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR029415;IPR032794;IPR024875; |
| Pfam | PF14695;PF14694; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000140471-LINS1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PRPF19 | Biogrid, Opencell | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

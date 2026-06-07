---
type: protein-evaluation
gene: "SRFBP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SRFBP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SRFBP1 |
| 蛋白名称 | Serum response factor-binding protein 1 |
| 蛋白大小 | 429 aa / 48.6 kDa |
| UniProt ID | Q8NEF9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli rim; UniProt: Cytoplasm, perinuclear region |
| 蛋白大小 | 10/10 | ×1 | 10 | 429 aa / 48.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR037393, IPR015158; Pfam: PF09073 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **129.5/180** | |
| **归一化总分** | | | **71.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli rim | Approved |
| UniProt | Cytoplasm, perinuclear region | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 90S preribosome (GO:0030686)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 15 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Whole Exome Sequencing Reveals Novel Candidate Genes in Familial Forms of Glaucomatous Neurodegeneration.. *Genes*. PMID: 36833422
2. [The diagnostic value of inflammation-related genes in bronchopulmonary dysplasia].. *Zhonghua yu fang yi xue za zhi [Chinese journal of preventive medicine]*. PMID: 38955739
3. Does p49/STRAP, a SRF-binding protein (SRFBP1), modulate cardiac mitochondrial function in aging?. *Experimental gerontology*. PMID: 27337995
4. Quantitative Proteomics Identifies Serum Response Factor Binding Protein 1 as a Host Factor for Hepatitis C Virus Entry.. *Cell reports*. PMID: 26212323
5. Real-time imaging of RNA polymerase I activity in living human cells.. *The Journal of cell biology*. PMID: 36282216

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.9 |
| 高置信度残基 (pLDDT>90) 占比 | 23.1% |
| 置信残基 (pLDDT 70-90) 占比 | 12.1% |
| 中等置信 (pLDDT 50-70) 占比 | 18.9% |
| 低置信 (pLDDT<50) 占比 | 45.9% |
| 有序区域 (pLDDT>70) 占比 | 35.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=61.9），有序残基占 35.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037393, IPR015158; Pfam: PF09073 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BYSL | 0.971 | 0.886 | — |
| SRF | 0.919 | 0.292 | — |
| POLRMT | 0.898 | 0.834 | — |
| WDR36 | 0.874 | 0.297 | — |
| PWP2 | 0.858 | 0.445 | — |
| IMP4 | 0.851 | 0.309 | — |
| WDR3 | 0.849 | 0.322 | — |
| DDX10 | 0.843 | 0.784 | — |
| NOL6 | 0.842 | 0.457 | — |
| LOC102724159 | 0.840 | 0.445 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.9 + PDB: 无 | pLDDT=61.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, perinuclear region / Nucleoli rim | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SRFBP1 — Serum response factor-binding protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小429 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=61.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NEF9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000151304-SRFBP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SRFBP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NEF9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli rim (approved)。来源: https://www.proteinatlas.org/ENSG00000151304-SRFBP1/subcellular

![](https://images.proteinatlas.org/42737/504_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/42737/504_G6_3_red_green.jpg)
![](https://images.proteinatlas.org/42737/506_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/42737/506_G6_2_red_green.jpg)
![](https://images.proteinatlas.org/42737/555_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/42737/555_G6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NEF9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8NEF9 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR037393;IPR015158; |
| Pfam | PF09073; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000151304-SRFBP1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| DDX10 | Bioplex | false |
| DUSP14 | Bioplex | false |
| FBL | Biogrid | false |
| H2AC11 | Bioplex | false |
| H2AC13 | Bioplex | false |
| H2AC15 | Bioplex | false |
| H2AC16 | Bioplex | false |
| H2AC17 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

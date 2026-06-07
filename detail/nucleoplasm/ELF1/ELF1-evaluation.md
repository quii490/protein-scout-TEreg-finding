---
type: protein-evaluation
gene: "ELF1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ELF1 — REJECTED (研究热度过高 (PubMed strict=311，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ELF1 |
| 蛋白名称 | ETS-related transcription factor Elf-1 |
| 蛋白大小 | 619 aa / 67.5 kDa |
| UniProt ID | P32519 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 619 aa / 67.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=311 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=52.8; PDB: 8BZM |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000418, IPR046328, IPR022084, IPR036388, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.0/180** | |
| **归一化总分** | | | **48.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 311 |
| PubMed broad count | 414 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. The molecular landscape of pediatric acute myeloid leukemia reveals recurrent structural alterations and age-specific mutational interactions.. *Nature medicine*. PMID: 29227476
2. Robust gene expression programs underlie recurrent cell states and phenotype switching in melanoma.. *Nature cell biology*. PMID: 32753671
3. Integrative network-based analysis on multiple Gene Expression Omnibus datasets identifies novel immune molecular markers implicated in non-alcoholic steatohepatitis.. *Frontiers in endocrinology*. PMID: 37008925
4. ELF1/PRR11/ARP2/3 promoted trophoblast cells proliferation and motility in early pregnancy.. *American journal of reproductive immunology (New York, N.Y. : 1989)*. PMID: 37641376
5. ELF1-mediated transactivation of METTL3/YTHDF2 promotes nucleus pulposus cell senescence via m6A-dependent destabilization of E2F3 mRNA in intervertebral disc degeneration.. *Cell death discovery*. PMID: 40467575

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 52.8 |
| 高置信度残基 (pLDDT>90) 占比 | 12.0% |
| 置信残基 (pLDDT 70-90) 占比 | 4.2% |
| 中等置信 (pLDDT 50-70) 占比 | 19.7% |
| 低置信 (pLDDT<50) 占比 | 64.1% |
| 有序区域 (pLDDT>70) 占比 | 16.2% |
| 可用 PDB 条目 | 8BZM |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=52.8），有序残基占 16.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000418, IPR046328, IPR022084, IPR036388, IPR036390; Pfam: PF12310, PF00178 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GABPA | 0.696 | 0.127 | — |
| RUNX1 | 0.681 | 0.306 | — |
| EFNA5 | 0.667 | 0.000 | — |
| PAX5 | 0.595 | 0.000 | — |
| NFKB1 | 0.594 | 0.510 | — |
| ELF2 | 0.581 | 0.057 | — |
| BLK | 0.578 | 0.074 | — |
| CBFB | 0.563 | 0.000 | — |
| IL3 | 0.499 | 0.000 | — |
| ZNF821 | 0.495 | 0.068 | — |

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
| 三维结构 | AlphaFold pLDDT=52.8 + PDB: 8BZM | pLDDT=52.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. ELF1 — ETS-related transcription factor Elf-1，研究基础较多，新颖性有限。
2. 蛋白大小619 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 311 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=52.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 311 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P32519
- Protein Atlas: https://www.proteinatlas.org/ENSG00000120690-ELF1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ELF1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P32519
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000120690-ELF1/subcellular

![](https://images.proteinatlas.org/5172/1144_C1_1_red_green.jpg)
![](https://images.proteinatlas.org/5172/1144_C1_2_red_green.jpg)
![](https://images.proteinatlas.org/5172/954_A1_2_red_green.jpg)
![](https://images.proteinatlas.org/5172/954_A1_4_red_green.jpg)
![](https://images.proteinatlas.org/5172/956_A1_1_red_green.jpg)
![](https://images.proteinatlas.org/5172/956_A1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P32519-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P32519 |
| SMART | SM00413; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR000418;IPR046328;IPR022084;IPR036388;IPR036390; |
| Pfam | PF12310;PF00178; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000120690-ELF1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HOXC13 | Intact | false |
| HSPBP1 | Intact, Bioplex | false |
| NFIA | Biogrid | false |
| NFIX | Biogrid | false |
| NFKB1 | Biogrid | false |
| SP1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

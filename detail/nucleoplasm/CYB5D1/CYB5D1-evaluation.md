---
type: protein-evaluation
gene: "CYB5D1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CYB5D1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CYB5D1 |
| 蛋白名称 | Cytochrome b5 domain-containing protein 1 |
| 蛋白大小 | 228 aa / 26.7 kDa |
| UniProt ID | Q6P9G0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Nucleoli, Golgi apparatus; UniProt: Cytoplasm, cytoskeleton, cilium axoneme |
| 蛋白大小 | 10/10 | x1 | 10 | 228 aa / 26.7 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 8/10 | x3 | 24 | AlphaFold v6 pLDDT=86.8; PDB: 8J07 |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR001199, IPR036400, IPR052320; Pfam: PF00173 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Golgi apparatus | Approved |
| UniProt | Cytoplasm, cytoskeleton, cilium axoneme | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- axoneme (GO:0005930)

**结论**: 核定位信号较弱，多个数据源显示混合定位。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 5 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Heme-binding protein CYB5D1 is a radial spoke component required for coordinated ciliary beating.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 33875586
2. DNA methylation in peripheral blood is associated with renal aging and renal function decline: a national community study.. *Clinical epigenetics*. PMID: 38879526
3. Can survival prediction be improved by merging gene expression data sets?. *PloS one*. PMID: 19851466
4. Developmental Toxicity of Zinc Oxide Nanoparticles to Zebrafish (Danio rerio): A Transcriptomic Analysis.. *PloS one*. PMID: 27504894
5. Characterization of eQTLs associated with androstenone by RNA sequencing in porcine testis.. *Physiological genomics*. PMID: 31373884

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.8 |
| 高置信度残基 (pLDDT>90) 占比 | 51.3% |
| 置信残基 (pLDDT 70-90) 占比 | 42.1% |
| 中等置信 (pLDDT 50-70) 占比 | 4.4% |
| 低置信 (pLDDT<50) 占比 | 2.2% |
| 有序区域 (pLDDT>70) 占比 | 93.4% |
| 可用 PDB 条目 | 8J07 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度（pLDDT=86.8，有序区 93.4%）。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001199, IPR036400, IPR052320; Pfam: PF00173 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DNALI1 | 0.700 | 0.000 | — |
| SLC4A8 | 0.607 | 0.000 | — |
| RNF113B | 0.517 | 0.251 | — |
| TEKT1 | 0.514 | 0.000 | — |
| DNAJC24 | 0.498 | 0.190 | — |
| DNAJC3 | 0.492 | 0.190 | — |
| SUOX | 0.490 | 0.000 | — |
| MRPS31 | 0.489 | 0.000 | — |
| RSPH3 | 0.487 | 0.307 | — |
| CYB5R4 | 0.481 | 0.095 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 3 / 15 = 20%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 20%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.8 + PDB: 8J07 | pLDDT=86.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, cilium axoneme / Nucleoli, Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. CYB5D1 -- Cytochrome b5 domain-containing protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小228 aa，大小适中（200-800 aa），适合常规生化实验。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6P9G0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000182224-CYB5D1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CYB5D1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6P9G0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000182224-CYB5D1/subcellular

![](https://images.proteinatlas.org/21632/187_H10_1_red_green.jpg)
![](https://images.proteinatlas.org/21632/187_H10_2_red_green.jpg)
![](https://images.proteinatlas.org/21632/246_H10_1_red_green.jpg)
![](https://images.proteinatlas.org/21632/246_H10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6P9G0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q6P9G0 |
| SMART | SM01117; |
| UniProt Domain [FT] | DOMAIN 17..83; /note="Cytochrome b5 heme-binding"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00279" |
| InterPro | IPR001199;IPR036400;IPR052320; |
| Pfam | PF00173; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000182224-CYB5D1/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

---
type: protein-evaluation
gene: "CENPO"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation, E-batch]
status: scored
---

## CENPO 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CENPO / ICEN36 / MCM21R |
| 蛋白名称 | Centromere protein O |
| 蛋白大小 | 300 aa / 33.8 kDa |
| UniProt ID | Q9BU64 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 10/10 | ×4 | 40 | HPA: Nucleoplasm; 额外: Nuclear bodies; UniProt: Nucleus; Chromosome, centromere; Chromosome, centrome |
| 蛋白大小 | 10/10 | ×1 | 10 | 300 aa / 33.8 kDa |
| 研究新颖性 | 9/10 | ×5 | 45 | PubMed strict=28 篇 |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=85.2; PDB: 暂无 |
| 调控结构域 | 9/10 | ×2 | 18 | InterPro: IPR018464; Pfam: PF09496 |
| PPI 网络 | 10/10 | ×3 | 30 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.2 | AlphaFold 结构预测: +0.25 |
| **原始总分** | | | **171.2/180** | |
| **归一化总分 (÷1.83)** | | | **93.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | —
| UniProt | Chromosome, centromere | —
| UniProt | Chromosome, centromere, kinetochore | —

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- cytosol (GO:0005829) [TAS:Reactome]
- inner kinetochore (GO:0000939) [IPI:ComplexPortal]
- Mis6-Sim4 complex (GO:0031511) [IBA:GO_Central]
- nuclear body (GO:0016604) [IDA:HPA]
- nucleoplasm (GO:0005654) [IDA:HPA]
- nucleus (GO:0005634) [NAS:ComplexPortal]

**结论**: HPA: Nucleoplasm; 额外: Nuclear bodies; UniProt: Nucleus; Chromosome, centromere; Chromosome, centromere, kinetochore

#### 3.2 蛋白大小评估

**评价**: 300 aa / 33.8 kDa，大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 28 |
| PubMed 搜索链接 | [CENPO PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=CENPO) |

**关键文献**:
暂无文献记录。

**评价**: 较新颖，研究关注度低。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.2 |
| 高置信度残基 (pLDDT>90) 占比 | 61.3% |
| 置信残基 (pLDDT 70-90) 占比 | 22.0% |
| 中等置信 (pLDDT 50-70) 占比 | 8.0% |
| 低置信 (pLDDT<50) 占比 | 8.7% |
| 有序区域 (pLDDT>70) 占比 | 83.3% |
| 可用 PDB 条目 | 暂无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR018464; Pfam: PF09496 |

**染色质调控潜力分析**: 存在染色质/调控相关结构域/功能特征: nucleosome, centromere, kinetochore

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CENPQ | 0.999 | 0.986 | — |
| CENPH | 0.999 | 0.941 | — |
| ITGB3BP | 0.999 | 0.986 | — |
| CENPU | 0.999 | 0.973 | — |
| CENPK | 0.999 | 0.941 | — |
| CENPT | 0.999 | 0.918 | — |
| CENPI | 0.999 | 0.969 | — |
| CENPL | 0.999 | 0.805 | — |
| CENPN | 0.999 | 0.976 | — |
| CENPP | 0.999 | 0.988 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CEP170P1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 |
| RNF40 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-11695|pubmed:19447967 |
| ITGB3BP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| MTFR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| CENPU | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| CENPQ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| ARL5B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| CENPP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/nature22366|imex:IM-25778 |
| DCDC2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| FOSB | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0/15。

**评价**: STRING + IntAct 双源 PPI 数据充分。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold | pLDDT=85.2, v6 | 预测 |
| 定位 | UniProt + HPA | Nucleus; Chromosome, centromere; Chromosome, centromere, kinetochore / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- AlphaFold 结构预测: +0.25
- 多库定位一致 (HPA+UniProt): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域注释 + AlphaFold 预测: +0.25

**总分**: +1.2 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐⭐

**归一化总分**: 93.6/100

**核心优势**:
1. CENPO — Centromere protein O，极度新颖，几乎未被系统研究（PubMed 28 篇）。
2. 蛋白大小300 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。
3. AlphaFold pLDDT=85.2，结构预测质量高。

**风险/不确定性**:
1. 功能研究较少，具体调控机制待阐明

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计 ChIP-seq/CUT&RUN 验证染色质结合
- [ ] 设计体外实验验证核定位及潜在调控功能

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BU64
- Protein Atlas: https://www.proteinatlas.org/search/CENPO
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CENPO
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BU64
- STRING: https://string-db.org/network/9606.CENPO
- Packet data timestamp: 2026-06-03 04:46:40

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000138092-CENPO/subcellular

![](https://images.proteinatlas.org/46189/1609_C5_1_red_green.jpg)
![](https://images.proteinatlas.org/46189/1609_C5_4_red_green.jpg)
![](https://images.proteinatlas.org/46189/1625_C12_2_red_green.jpg)
![](https://images.proteinatlas.org/46189/1625_C12_4_red_green.jpg)
![](https://images.proteinatlas.org/46189/1841_A4_1_red_green.jpg)
![](https://images.proteinatlas.org/46189/1841_A4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BU64-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BU64 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR018464; |
| Pfam | PF09496; |

### humanPPI / HPA Interaction
Source: 未找到 HPA interaction 页面

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

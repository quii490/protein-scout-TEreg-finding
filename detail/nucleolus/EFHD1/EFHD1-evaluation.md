---
type: protein-evaluation
gene: "EFHD1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EFHD1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EFHD1 |
| 蛋白名称 | EF-hand domain-containing protein D1 |
| 蛋白大小 | 239 aa / 26.9 kDa |
| UniProt ID | Q9BUP0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Golgi apparatus; 额外: Nucleoli fibrillar center; UniProt: Mitochondrion inner membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 239 aa / 26.9 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=47 篇 (≤60→6) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=77.2; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 6 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **99.5/180** | |
| **归一化总分** | | | **55.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nucleoli fibrillar center | Supported |
| UniProt | Mitochondrion inner membrane | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 47 |
| PubMed broad count | 47 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Synovial lymphatic system structure and function in rheumatoid arthritis: lymphatic phases, telocytes, and therapeutic modulation through Eexercise.. *Curr Opin Rheumatol*. PMID: 41782549
2. Linking Mitochondrial Dysfunction to the Immune Microenvironment in HFpEF: An Integrated Bioinformatics and Experimental Approach.. *Immun Inflamm Dis*. PMID: 42021460
3. Telocyte Deletion Associated With Loss of Lymphatic Drainage and Exacerbation of Inflammatory-Erosive Arthritis in Mice.. *Arthritis Rheumatol*. PMID: 41838025
4. Transcriptional Modulation of Infertility-Associated Genes Following Chlamydia trachomatis Infection in Human Fallopian Tube Mesenchymal Cells: In Silico Study.. *Genes (Basel)*. PMID: 41898836
5. Excessive Ca(2+)-dependent ER-mitochondrial contact stabilization by EFHD1 drives liver injury.. *bioRxiv*. PMID: 41756893

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 77.2 |
| 高置信度残基 (pLDDT>90) 占比 | 24.3% |
| 置信残基 (pLDDT 70-90) 占比 | 52.3% |
| 中等置信 (pLDDT 50-70) 占比 | 11.7% |
| 低置信 (pLDDT<50) 占比 | 11.7% |
| 有序区域 (pLDDT>70) 占比 | 76.6% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 中等质量（pLDDT=77.2，有序区 76.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RHAG | 0.000 | 0.000 | — |
| ERMN | 0.000 | 0.000 | — |
| SLC24A1 | 0.000 | 0.000 | — |
| OPN4 | 0.000 | 0.000 | — |
| TEX44 | 0.000 | 0.000 | — |
| RRH | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q9BUP0 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:- |
| uniprotkb:Q14525 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:- |
| uniprotkb:Q07283 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:- |
| uniprotkb:P49768 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q6GP23 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 6，IntAct interactions: 30
- 调控相关比例: 0 / 6 = 0%

**评价**: STRING 6 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=77.2 + PDB: 无 | pLDDT=77.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Mitochondrion inner membrane / Golgi apparatus; 额外: Nucleoli fibrillar center | 一致 |
| PPI | STRING + IntAct | 6 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. EFHD1 — EF-hand domain-containing protein D1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小239 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 47 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BUP0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000115468-EFHD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EFHD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BUP0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9BUP0 |
| SMART | SM00054; |
| UniProt Domain [FT] | DOMAIN 90..125; /note="EF-hand 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00448"; DOMAIN 126..161; /note="EF-hand 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00448" |
| InterPro | IPR011992;IPR002048;IPR040365; |
| Pfam | PF13499; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000115468-EFHD1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ANXA9 | Bioplex | false |
| CALD1 | Opencell | false |
| CALM3 | Opencell | false |
| CAPZA2 | Bioplex | false |
| CTTN | Opencell | false |
| ESR1 | Biogrid | false |
| EZR | Biogrid | false |
| IFITM1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

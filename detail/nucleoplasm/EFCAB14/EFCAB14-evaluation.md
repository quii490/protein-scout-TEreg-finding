---
type: protein-evaluation
gene: "EFCAB14"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EFCAB14 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EFCAB14 |
| 蛋白名称 | EF-hand calcium-binding domain-containing protein 14 |
| 蛋白大小 | 495 aa / 55.0 kDa |
| UniProt ID | O75071 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cytosol; 额外: Nucleoli, Golgi apparatus; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 495 aa / 55.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=3 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.2; PDB: 无 |
| 调控结构域 | 5/10 | ×2 | 10 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 11 partners; IntAct 18 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.5/180** | |
| **归一化总分** | | | **63.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoli, Golgi apparatus | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3 |
| PubMed broad count | 3 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Tumor immune microenvironment score predicts efficacy of immune checkpoint inhibitors-based regimens in advanced non-small cell lung cancer.. *J Transl Med*. PMID: 41387877
2. A plasma proteome-mediated Mendelian randomization study reveals the impact of rheumatoid arthritis on mental disorders in a European population.. *J Affect Disord*. PMID: 40592408
3. Metalloproteins as risk factors for osteoarthritis: improving and understanding causal estimates using Mendelian randomization.. *Clin Rheumatol*. PMID: 38720162

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.2 |
| 高置信度残基 (pLDDT>90) 占比 | 19.2% |
| 置信残基 (pLDDT 70-90) 占比 | 38.0% |
| 中等置信 (pLDDT 50-70) 占比 | 13.7% |
| 低置信 (pLDDT<50) 占比 | 29.1% |
| 有序区域 (pLDDT>70) 占比 | 57.2% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 预测质量有限（pLDDT=67.2），有序残基占 57.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GRAMD2B | 0.000 | 0.000 | — |
| TEX38 | 0.000 | 0.000 | — |
| ZNF782 | 0.000 | 0.000 | — |
| ATPAF1 | 0.000 | 0.000 | — |
| CSNK2A2 | 0.000 | 0.000 | — |
| CSNK2A1 | 0.000 | 0.000 | — |
| TSTD2 | 0.000 | 0.000 | — |
| TTC9C | 0.000 | 0.000 | — |
| UNC80 | 0.000 | 0.000 | — |
| CACUL1 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:O75071 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q0WJT0 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q06408 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:- |
| intact:EBI-25591227 | psi-mi:"MI:2195"(clash) | pubmed:- |
| intact:EBI-25372272 | psi-mi:"MI:2195"(clash) | pubmed:- |
| intact:EBI-54262002 | psi-mi:"MI:2195"(clash) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 11，IntAct interactions: 18
- 调控相关比例: 0 / 11 = 0%

**评价**: STRING 11 个预测互作，IntAct 18 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.2 + PDB: 无 | pLDDT=67.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Cytosol; 额外: Nucleoli, Golgi apparatus | 待确认 |
| PPI | STRING + IntAct | 11 + 18 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. EFCAB14 — EF-hand calcium-binding domain-containing protein 14，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小495 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=67.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75071
- Protein Atlas: https://www.proteinatlas.org/ENSG00000159658-EFCAB14/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EFCAB14
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75071
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O75071 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 434..463; /note="EF-hand 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00448"; DOMAIN 464..495; /note="EF-hand 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00448" |
| InterPro | IPR011992;IPR002048;IPR042352; |
| Pfam | 未检出 |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000159658-EFCAB14/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CSNK2A1 | Biogrid, Opencell | true |
| CSNK2A2 | Biogrid, Opencell | true |
| CSNK2B | Opencell | false |
| GRAMD2B | Bioplex | false |
| LGALS1 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

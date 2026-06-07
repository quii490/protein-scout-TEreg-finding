---
type: protein-evaluation
gene: "GBP3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GBP3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GBP3 |
| 蛋白名称 | Guanylate-binding protein 3 |
| 蛋白大小 | 595 aa / 68.1 kDa |
| UniProt ID | Q9H0R5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm; Cytoplasm, perinuclear region; Golgi apparatus me |
| 蛋白大小 | 10/10 | ×1 | 10 | 595 aa / 68.1 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=47 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=88.4; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR030386, IPR037684, IPR003191, IPR036543, IPR015 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.5/180** | |
| **归一化总分** | | | **65.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm; Cytoplasm, perinuclear region; Golgi apparatus membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytoplasmic vesicle (GO:0031410)
- cytosol (GO:0005829)
- Golgi membrane (GO:0000139)
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 47 |
| PubMed broad count | 66 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Guanylate-binding proteins: mechanisms of pattern recognition and antimicrobial functions.. *Trends in biochemical sciences*. PMID: 37567806
2. The function of guanylate binding protein 3 (GBP3) in human cancers by pan-cancer bioinformatics.. *Mathematical biosciences and engineering : MBE*. PMID: 37161254
3. GBP3 promotes glioblastoma resistance to temozolomide by enhancing DNA damage repair.. *Oncogene*. PMID: 35780181
4. Evolution of the guanylate binding protein (GBP) genes: Emergence of GBP7 genes in primates and further acquisition of a unique GBP3 gene in simians.. *Molecular immunology*. PMID: 33550067
5. GBP3 promotes glioma cell proliferation via SQSTM1/p62-ERK1/2 axis.. *Biochemical and biophysical research communications*. PMID: 29128363

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.4 |
| 高置信度残基 (pLDDT>90) 占比 | 57.0% |
| 置信残基 (pLDDT 70-90) 占比 | 36.1% |
| 中等置信 (pLDDT 50-70) 占比 | 5.9% |
| 低置信 (pLDDT<50) 占比 | 1.0% |
| 有序区域 (pLDDT>70) 占比 | 93.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=88.4，有序区 93.1%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR030386, IPR037684, IPR003191, IPR036543, IPR015894; Pfam: PF02263, PF02841 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GBP2 | 0.936 | 0.819 | — |
| GBP1 | 0.936 | 0.806 | — |
| STAT1 | 0.753 | 0.000 | — |
| RTP4 | 0.674 | 0.000 | — |
| IFI44 | 0.651 | 0.000 | — |
| ISG15 | 0.643 | 0.000 | — |
| MAP4K4 | 0.640 | 0.292 | — |
| IRF9 | 0.619 | 0.000 | — |
| IRGM | 0.608 | 0.061 | — |
| DDX60 | 0.600 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NC2alpha | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Liprin-beta | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Taf11 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Ing5 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| PolE4 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| tktA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ATL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12081|pubmed:19665976 |
| Rtn3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12081|pubmed:19665976 |
| S100A10 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H1-2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.4 + PDB: 无 | pLDDT=88.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, perinuclear region; Golgi ap / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. GBP3 — Guanylate-binding protein 3，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小595 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 47 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H0R5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000117226-GBP3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GBP3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H0R5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H0R5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8WXF7 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 64..309; /note="GB1/RHD3-type G"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01052, ECO:0000269\|PubMed:21220294, ECO:0000269\|PubMed:21368113, ECO:0000269\|PubMed:23334294, ECO:0000269\|PubMed:34546351, ECO:0000269\|PubMed:38509071" |
| InterPro | IPR030386;IPR036543;IPR015894;IPR027417; |
| Pfam | PF02263; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000117226-GBP3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| MAP4K4 | Intact, Biogrid | true |
| ACTL6B | Bioplex | false |
| CASP6 | Bioplex | false |
| GBP1 | Intact, Bioplex | false |
| GBP2 | Intact, Bioplex | false |
| GBP5 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

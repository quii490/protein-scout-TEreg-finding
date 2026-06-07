---
type: protein-evaluation
gene: "TPRN"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TPRN 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TPRN / C9orf75 |
| 蛋白名称 | Taperin |
| 蛋白大小 | 711 aa / 75.6 kDa |
| UniProt ID | Q4KMQ1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane; UniProt: Cell projection, stereocilium; Cell projection, microvillus; |
| 蛋白大小 | 10/10 | ×1 | 10 | 711 aa / 75.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=54.4; PDB: 6Y9Q |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR025903, IPR025907, IPR026671; Pfam: PF13914, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.5/180** | |
| **归一化总分** | | | **72.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane | Approved |
| UniProt | Cell projection, stereocilium; Cell projection, microvillus; Nucleus, nucleoplasm; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- microvillus (GO:0005902)
- nucleoplasm (GO:0005654)
- stereocilium (GO:0032420)
- stereocilium base (GO:0120044)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 29 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C9orf75 |

**关键文献**:
1. Genetic Hearing Loss Overview.. **. PMID: 20301607
2. Critical role of TPRN rings in the stereocilia for hearing.. *Molecular therapy : the journal of the American Society of Gene Therapy*. PMID: 37952086
3. Whole-genome resequencing reveals new mutations in candidate genes for Beichuan-white goat prolificacya.. *Animal biotechnology*. PMID: 37729465
4. Progressive hearing loss and degeneration of hair cell stereocilia in taperin gene knockout mice.. *Biochemical and biophysical research communications*. PMID: 27693694
5. Mutations in TPRN cause a progressive form of autosomal-recessive nonsyndromic hearing loss.. *American journal of human genetics*. PMID: 20170898

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 54.4 |
| 高置信度残基 (pLDDT>90) 占比 | 2.4% |
| 置信残基 (pLDDT 70-90) 占比 | 18.0% |
| 中等置信 (pLDDT 50-70) 占比 | 28.1% |
| 低置信 (pLDDT<50) 占比 | 51.5% |
| 有序区域 (pLDDT>70) 占比 | 20.4% |
| 可用 PDB 条目 | 6Y9Q |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=54.4），有序残基占 20.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR025903, IPR025907, IPR026671; Pfam: PF13914, PF13916 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CLIC5 | 0.997 | 0.839 | — |
| WHRN | 0.958 | 0.810 | — |
| GRXCR1 | 0.928 | 0.000 | — |
| GRXCR2 | 0.923 | 0.000 | — |
| RDX | 0.918 | 0.000 | — |
| MYO7A | 0.895 | 0.000 | — |
| PPP1CB | 0.886 | 0.780 | — |
| RIPOR2 | 0.875 | 0.000 | — |
| CLIC4 | 0.871 | 0.841 | — |
| MYH9 | 0.868 | 0.167 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EPS8 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| PPP1CC | psi-mi:"MI:0018"(two hybrid) | pubmed:21382349|imex:IM-17664 |
| PPP1CA | psi-mi:"MI:0018"(two hybrid) | imex:IM-16965|pubmed:22321011 |
| CLIC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CLIC4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CLIC2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| WHRN | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CLIC5 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CAPZA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| MYO15B | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=54.4 + PDB: 6Y9Q | pLDDT=54.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell projection, stereocilium; Cell projection, mi / Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TPRN — Taperin，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小711 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=54.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q4KMQ1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000176058-TPRN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TPRN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q4KMQ1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000176058-TPRN/subcellular

![](https://images.proteinatlas.org/20899/177_A9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/20899/177_A9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/20899/178_A9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/20899/178_A9_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/20899/247_A9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/20899/247_A9_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q4KMQ1-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q4KMQ1 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR025903;IPR025907;IPR026671; |
| Pfam | PF13914;PF13916; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000176058-TPRN/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PPP1CA | Intact, Biogrid, Bioplex | true |
| PPP1CB | Biogrid, Bioplex | true |
| ANLN | Biogrid | false |
| CLIC1 | Biogrid | false |
| CLIC2 | Biogrid | false |
| CLIC4 | Biogrid | false |
| CLIC5 | Biogrid | false |
| FTL | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

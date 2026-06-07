---
type: protein-evaluation
gene: "PAX2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PAX2 — REJECTED (研究热度过高 (PubMed strict=1063，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PAX2 |
| 蛋白名称 | Paired box protein Pax-2 |
| 蛋白大小 | 417 aa / 44.7 kDa |
| UniProt ID | Q02962 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 417 aa / 44.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1063 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=60.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR009057, IPR043182, IPR001523, IPR022130, IPR043 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- centriolar satellite (GO:0034451)
- chromatin (GO:0000785)
- microtubule organizing center (GO:0005815)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- protein-containing complex (GO:0032991)
- protein-DNA complex (GO:0032993)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1063 |
| PubMed broad count | 1925 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. PAX2-Related Disorder.. **. PMID: 20301624
2. The Role of PAX2 in Neurodevelopment and Disease.. *Neuropsychiatric disease and treatment*. PMID: 34908837
3. Renal coloboma syndrome.. *Ophthalmology*. PMID: 11581073
4. PAX2 Gene Mutation in Pediatric Renal Disorders-A Narrative Review.. *International journal of molecular sciences*. PMID: 37628926
5. PAX proteins and their role in pancreas.. *Diabetes research and clinical practice*. PMID: 31325538

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 60.9 |
| 高置信度残基 (pLDDT>90) 占比 | 26.1% |
| 置信残基 (pLDDT 70-90) 占比 | 9.1% |
| 中等置信 (pLDDT 50-70) 占比 | 11.8% |
| 低置信 (pLDDT<50) 占比 | 53.0% |
| 有序区域 (pLDDT>70) 占比 | 35.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=60.9），有序残基占 35.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009057, IPR043182, IPR001523, IPR022130, IPR043565; Pfam: PF00292, PF12403 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PAXIP1 | 0.981 | 0.310 | — |
| TLX1 | 0.953 | 0.000 | — |
| LMX1B | 0.882 | 0.355 | — |
| EYA1 | 0.872 | 0.000 | — |
| WT1 | 0.856 | 0.047 | — |
| EN1 | 0.841 | 0.000 | — |
| SIX1 | 0.832 | 0.000 | — |
| GBX2 | 0.826 | 0.060 | — |
| OTX2 | 0.823 | 0.000 | — |
| LHX1 | 0.805 | 0.127 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| sv | psi-mi:"MI:0397"(two hybrid array) | doi:10.1016/j.celrep.2019.03.0 |
| BBS1 | psi-mi:"MI:0018"(two hybrid) | pubmed:18000879 |
| BBS4 | psi-mi:"MI:0018"(two hybrid) | pubmed:18000879 |
| BBS2 | psi-mi:"MI:0018"(two hybrid) | pubmed:18000879 |
| BBS7 | psi-mi:"MI:0018"(two hybrid) | pubmed:18000879 |
| PAX8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NFIA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:35140242|imex:IM-28767 |
| NFIB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:35140242|imex:IM-28767 |
| NFIC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:35140242|imex:IM-28767 |
| KMT2C | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:35140242|imex:IM-28767 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=60.9 + PDB: 无 | pLDDT=60.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. PAX2 — Paired box protein Pax-2，研究基础较多，新颖性有限。
2. 蛋白大小417 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1063 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=60.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1063 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q02962
- Protein Atlas: https://www.proteinatlas.org/ENSG00000075891-PAX2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PAX2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q02962
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000075891-PAX2/subcellular

![](https://images.proteinatlas.org/47704/1335_C5_1_red_green.jpg)
![](https://images.proteinatlas.org/47704/1335_C5_3_red_green.jpg)
![](https://images.proteinatlas.org/47704/1789_E10_1_cr596499ea0dcfb_red_green.jpg)
![](https://images.proteinatlas.org/47704/1789_E10_20_cr596499ea0e140_red_green.jpg)
![](https://images.proteinatlas.org/47704/1830_D12_68_red_green.jpg)
![](https://images.proteinatlas.org/47704/1830_D12_69_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q02962-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q02962 |
| SMART | SM00351; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR009057;IPR043182;IPR001523;IPR022130;IPR043565;IPR036388; |
| Pfam | PF00292;PF12403; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000075891-PAX2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| NFIA | Intact | false |
| NFIB | Intact | false |
| PAXIP1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

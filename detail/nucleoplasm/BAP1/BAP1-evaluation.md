---
type: protein-evaluation
gene: "BAP1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BAP1 — REJECTED (研究热度过高 (PubMed strict=1377，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BAP1 / KIAA0272 |
| 蛋白名称 | Ubiquitin carboxyl-terminal hydrolase BAP1 |
| 蛋白大小 | 729 aa / 80.4 kDa |
| UniProt ID | Q92560 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm; Nucleus; Chromosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 729 aa / 80.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1377 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.9; PDB: 7VPW, 8H1T, 8SVF |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR038765, IPR001578, IPR036959, IPR041507; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus; Chromosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromosome (GO:0005694)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- PR-DUB complex (GO:0035517)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1377 |
| PubMed broad count | 2390 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0272 |

**关键文献**:
1. BAP1 links metabolic regulation of ferroptosis to tumour suppression.. *Nature cell biology*. PMID: 30202049
2. An overview of BAP1 biological functions and current therapeutics.. *Biochimica et biophysica acta. Reviews on cancer*. PMID: 39842618
3. Comprehensive Study of the Clinical Phenotype of Germline BAP1 Variant-Carrying Families Worldwide.. *Journal of the National Cancer Institute*. PMID: 30517737
4. Tumor suppressor BAP1 suppresses disulfidptosis through the regulation of SLC7A11 and NADPH levels.. *Oncogenesis*. PMID: 39266549
5. FOXO3a-BAP1 axis regulates neuronal ferroptosis in early brain injury after subarachnoid hemorrhage.. *Redox biology*. PMID: 40080966

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.9 |
| 高置信度残基 (pLDDT>90) 占比 | 31.1% |
| 置信残基 (pLDDT 70-90) 占比 | 12.5% |
| 中等置信 (pLDDT 50-70) 占比 | 9.7% |
| 低置信 (pLDDT<50) 占比 | 46.6% |
| 有序区域 (pLDDT>70) 占比 | 43.6% |
| 可用 PDB 条目 | 7VPW, 8H1T, 8SVF |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=62.9），有序残基占 43.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR038765, IPR001578, IPR036959, IPR041507; Pfam: PF01088, PF18031 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ASXL2 | 0.999 | 0.992 | — |
| ASXL1 | 0.999 | 0.922 | — |
| HCFC1 | 0.998 | 0.892 | — |
| BRCA1 | 0.995 | 0.292 | — |
| BARD1 | 0.994 | 0.070 | — |
| FOXK1 | 0.982 | 0.838 | — |
| OGT | 0.978 | 0.832 | — |
| RBBP7 | 0.969 | 0.688 | — |
| KDM1B | 0.960 | 0.765 | — |
| FOXK2 | 0.941 | 0.838 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSMUSP00000022458.5 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| MAGI1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RNF2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| UBC7 | psi-mi:"MI:0397"(two hybrid array) | pubmed:14690591 |
| NAF1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:14690591 |
| BZW1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| gyrB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| BON2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| BON1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.9 + PDB: 7VPW, 8H1T, 8SVF | pLDDT=62.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Chromosome / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. BAP1 — Ubiquitin carboxyl-terminal hydrolase BAP1，研究基础较多，新颖性有限。
2. 蛋白大小729 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1377 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=62.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1377 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92560
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163930-BAP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BAP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92560
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000163930-BAP1/subcellular

![](https://images.proteinatlas.org/28815/1469_D12_1_red_green.jpg)
![](https://images.proteinatlas.org/28815/1469_D12_2_red_green.jpg)
![](https://images.proteinatlas.org/28815/1478_D12_3_red_green.jpg)
![](https://images.proteinatlas.org/28815/1478_D12_5_red_green.jpg)
![](https://images.proteinatlas.org/28815/2189_B7_1_red_green.jpg)
![](https://images.proteinatlas.org/28815/2189_B7_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q92560-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q92560 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 4..235; /note="UCH catalytic"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01393"; DOMAIN 670..698; /note="ULD"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01394" |
| InterPro | IPR038765;IPR001578;IPR036959;IPR041507; |
| Pfam | PF01088;PF18031; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000163930-BAP1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ASXL1 | Intact, Biogrid, Bioplex | true |
| ASXL2 | Biogrid, Bioplex | true |
| BRCA1 | Intact, Biogrid | true |
| CBX5 | Intact, Biogrid | true |
| FOXK1 | Biogrid, Bioplex | true |
| HCFC1 | Intact, Biogrid, Bioplex | true |
| ITPR3 | Intact, Biogrid | true |
| OGT | Biogrid, Bioplex | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

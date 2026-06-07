---
type: protein-evaluation
gene: "NFE2L3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NFE2L3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NFE2L3 / NRF3 |
| 蛋白名称 | Nuclear factor erythroid 2-related factor 3 |
| 蛋白大小 | 694 aa / 76.2 kDa |
| UniProt ID | Q9Y4A8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Vesicles; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 694 aa / 76.2 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=62 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=53.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR004827, IPR004826, IPR046347, IPR047167, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 8 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **100.0/180** | |
| **归一化总分** | | | **55.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)
- RNA polymerase II transcription regulator complex (GO:0090575)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 62 |
| PubMed broad count | 105 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NRF3 |

**关键文献**:
1. NFE2L3 regulates inflammation and oxidative stress-related genes in the colon.. *Biochimica et biophysica acta. Molecular cell research*. PMID: 40360021
2. NFE2L3 (NRF3): the Cinderella of the Cap'n'Collar transcription factors.. *Cellular and molecular life sciences : CMLS*. PMID: 21687990
3. Identification roles of NFE2L3 in digestive system cancers.. *Journal of cancer research and clinical oncology*. PMID: 38514488
4. NFE2L3 promotes tumor progression and predicts a poor prognosis of bladder cancer.. *Carcinogenesis*. PMID: 35022660
5. Nfe2l3 promotes neuroprotection and long-distance axon regeneration after injury in vivo.. *Experimental neurology*. PMID: 38395216

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 53.6 |
| 高置信度残基 (pLDDT>90) 占比 | 15.3% |
| 置信残基 (pLDDT 70-90) 占比 | 7.5% |
| 中等置信 (pLDDT 50-70) 占比 | 13.5% |
| 低置信 (pLDDT<50) 占比 | 63.7% |
| 有序区域 (pLDDT>70) 占比 | 22.8% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=53.6），有序残基占 22.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004827, IPR004826, IPR046347, IPR047167, IPR008917; Pfam: PF03131 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MAFK | 0.969 | 0.766 | — |
| MAFG | 0.937 | 0.842 | — |
| MAF | 0.905 | 0.184 | — |
| MAFF | 0.844 | 0.681 | — |
| FOS | 0.770 | 0.048 | — |
| JUND | 0.731 | 0.091 | — |
| JUN | 0.727 | 0.045 | — |
| NFE2 | 0.691 | 0.541 | — |
| KEAP1 | 0.663 | 0.280 | — |
| HCFC1 | 0.629 | 0.601 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FMR1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| MAFF | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MAFG | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MAFK | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HCFC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HCFC2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PSCA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| DSCR9 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:35914814|imex:IM-27626 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 8
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 8 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=53.6 + PDB: 无 | pLDDT=53.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 8 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. NFE2L3 — Nuclear factor erythroid 2-related factor 3，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小694 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 62 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=53.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y4A8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000050344-NFE2L3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NFE2L3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y4A8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000050344-NFE2L3/subcellular

![](https://images.proteinatlas.org/55889/1027_E1_3_red_green.jpg)
![](https://images.proteinatlas.org/55889/1027_E1_4_red_green.jpg)
![](https://images.proteinatlas.org/55889/893_A10_1_red_green.jpg)
![](https://images.proteinatlas.org/55889/893_A10_2_red_green.jpg)
![](https://images.proteinatlas.org/55889/895_A10_1_red_green.jpg)
![](https://images.proteinatlas.org/55889/895_A10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y4A8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9Y4A8 |
| SMART | SM00338; |
| UniProt Domain [FT] | DOMAIN 578..641; /note="bZIP"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00978" |
| InterPro | IPR004827;IPR004826;IPR046347;IPR047167;IPR008917; |
| Pfam | PF03131; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000050344-NFE2L3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| MAFF | Intact, Biogrid, Bioplex | true |
| MAFG | Intact, Biogrid | true |
| GSK3B | Biogrid | false |
| MAFK | Biogrid | false |
| NFE2 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

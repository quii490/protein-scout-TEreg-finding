---
type: protein-evaluation
gene: "NFAT5"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NFAT5 — REJECTED (研究热度过高 (PubMed strict=400，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NFAT5 / KIAA0827, TONEBP |
| 蛋白名称 | Nuclear factor of activated T-cells 5 |
| 蛋白大小 | 1531 aa / 165.8 kDa |
| UniProt ID | O94916 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Cytoplasm; Chromosome |
| 蛋白大小 | 5/10 | ×1 | 5 | 1531 aa / 165.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=400 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=44.6; PDB: 1IMH |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR013783, IPR014756, IPR002909, IPR008366, IPR015 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **75.5/180** | |
| **归一化总分** | | | **41.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Enhanced |
| UniProt | Nucleus; Cytoplasm; Chromosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 400 |
| PubMed broad count | 688 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0827, TONEBP |

**关键文献**:
1. Inhibition of NFAT5-Dependent Astrocyte Swelling Alleviates Neuropathic Pain.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 38195869
2. Sodium chloride drives autoimmune disease by the induction of pathogenic TH17 cells.. *Nature*. PMID: 23467095
3. Macrophage transcription factor TonEBP promotes systemic lupus erythematosus and kidney injury via damage-induced signaling pathways.. *Kidney international*. PMID: 37088425
4. NLRC3 expression in macrophage impairs glycolysis and host immune defense by modulating the NF-κB-NFAT5 complex during septic immunosuppression.. *Molecular therapy : the journal of the American Society of Gene Therapy*. PMID: 36068919
5. SLC6A6 imports taurine into mitochondria to sustain mitochondrial translation and tumour growth.. *Nature metabolism*. PMID: 41652173

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 44.6 |
| 高置信度残基 (pLDDT>90) 占比 | 15.9% |
| 置信残基 (pLDDT 70-90) 占比 | 2.4% |
| 中等置信 (pLDDT 50-70) 占比 | 0.6% |
| 低置信 (pLDDT<50) 占比 | 81.1% |
| 有序区域 (pLDDT>70) 占比 | 18.3% |
| 可用 PDB 条目 | 1IMH |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=44.6），有序残基占 18.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013783, IPR014756, IPR002909, IPR008366, IPR015646; Pfam: PF16179, PF00554 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SLC6A12 | 0.817 | 0.000 | — |
| FOS | 0.816 | 0.292 | — |
| SLC5A3 | 0.796 | 0.000 | — |
| AKR1B1 | 0.785 | 0.000 | — |
| VEGFC | 0.759 | 0.000 | — |
| STAT3 | 0.748 | 0.000 | — |
| JUN | 0.687 | 0.292 | — |
| KMT2C | 0.680 | 0.000 | — |
| REL | 0.670 | 0.045 | — |
| CREB1 | 0.661 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TBC1D4 | psi-mi:"MI:0018"(two hybrid) | pubmed:unassigned5 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| ORF | psi-mi:"MI:0096"(pull down) | imex:IM-17346|pubmed:22190034| |
| Smyd5 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG3880 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| mtfA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| NFAT | psi-mi:"MI:0397"(two hybrid array) | pubmed:unassigned1513|imex:IM- |
| Dmel\CG4956 | psi-mi:"MI:0397"(two hybrid array) | doi:10.1016/j.celrep.2019.03.0 |
| retn | psi-mi:"MI:0397"(two hybrid array) | doi:10.1016/j.celrep.2019.03.0 |
| NFE2L2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32911434|imex:IM-27648 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=44.6 + PDB: 1IMH | pLDDT=44.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Chromosome / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. NFAT5 — Nuclear factor of activated T-cells 5，研究基础较多，新颖性有限。
2. 蛋白大小1531 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 400 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=44.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 400 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O94916
- Protein Atlas: https://www.proteinatlas.org/ENSG00000102908-NFAT5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NFAT5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O94916
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000102908-NFAT5/subcellular

![](https://images.proteinatlas.org/51528/1309_C8_2_red_green.jpg)
![](https://images.proteinatlas.org/51528/1309_C8_5_red_green.jpg)
![](https://images.proteinatlas.org/51528/808_C8_1_red_green.jpg)
![](https://images.proteinatlas.org/51528/808_C8_2_red_green.jpg)
![](https://images.proteinatlas.org/51528/908_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/51528/908_H6_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O94916-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O94916 |
| SMART | SM00429; |
| UniProt Domain [FT] | DOMAIN 264..443; /note="RHD"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00265" |
| InterPro | IPR013783;IPR014756;IPR002909;IPR008366;IPR015646;IPR008967;IPR032397;IPR011539;IPR037059; |
| Pfam | PF16179;PF00554; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000102908-NFAT5/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| NFE2L2 | Intact, Biogrid | true |
| ABL1 | Biogrid | false |
| ATM | Biogrid | false |
| DDX17 | Intact | false |
| DDX5 | Intact | false |
| EPHA3 | Biogrid | false |
| EZH2 | Biogrid | false |
| SHPRH | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

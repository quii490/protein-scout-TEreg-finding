---
type: protein-evaluation
gene: "LMX1A"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## LMX1A — REJECTED (研究热度过高 (PubMed strict=159，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LMX1A |
| 蛋白名称 | LIM homeobox transcription factor 1-alpha |
| 蛋白大小 | 382 aa / 42.7 kDa |
| UniProt ID | Q8TE12 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Golgi apparatus, Vesicles; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 382 aa / 42.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=159 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.6; PDB: 8IK5, 8IKE, 8ILW |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001356, IPR017970, IPR009057, IPR050453, IPR042 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Golgi apparatus, Vesicles | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 159 |
| PubMed broad count | 337 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Molecular ontology of the parabrachial nucleus.. *The Journal of comparative neurology*. PMID: 35134251
2. RNF38 promotes gilteritinib resistance in acute myeloid leukemia via inducing autophagy by regulating ubiquitination of LMX1A.. *Cell biology and toxicology*. PMID: 39604755
3. Cell fate determination, neuronal maintenance and disease state: The emerging role of transcription factors Lmx1a and Lmx1b.. *FEBS letters*. PMID: 26526610
4. Overlapping function of Lmx1a and Lmx1b in anterior hindbrain roof plate formation and cerebellar growth.. *The Journal of neuroscience : the official journal of the Society for Neuroscience*. PMID: 19741143
5. Lmx1a and Lmx1b regulate mitochondrial functions and survival of adult midbrain dopaminergic neurons.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 27407143

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.6 |
| 高置信度残基 (pLDDT>90) 占比 | 37.4% |
| 置信残基 (pLDDT 70-90) 占比 | 17.3% |
| 中等置信 (pLDDT 50-70) 占比 | 8.1% |
| 低置信 (pLDDT<50) 占比 | 37.2% |
| 有序区域 (pLDDT>70) 占比 | 54.7% |
| 可用 PDB 条目 | 8IK5, 8IKE, 8ILW |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=68.6），有序残基占 54.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR017970, IPR009057, IPR050453, IPR042688; Pfam: PF00046, PF00412 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NEUROG2 | 0.872 | 0.048 | — |
| NR4A2 | 0.849 | 0.000 | — |
| MSX1 | 0.805 | 0.071 | — |
| FOXA2 | 0.803 | 0.052 | — |
| ASCL1 | 0.801 | 0.048 | — |
| WNT1 | 0.764 | 0.058 | — |
| OTX2 | 0.760 | 0.091 | — |
| NKX2-2 | 0.754 | 0.045 | — |
| PAX2 | 0.706 | 0.127 | — |
| SHH | 0.687 | 0.071 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| GRB2 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25814554|imex:IM-22632 |
| rep | psi-mi:"MI:1356"(validated two hybrid) | pmc:PPR297270|pubmed:36217029| |
| Ssbp2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| Ldb1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| Phf10 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| Ldb2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| Chi | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Cyp312a1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| spz3 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Tom70 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.6 + PDB: 8IK5, 8IKE, 8ILW | pLDDT=68.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Golgi apparatus, Vesicles | 一致 |
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
1. LMX1A — LIM homeobox transcription factor 1-alpha，研究基础较多，新颖性有限。
2. 蛋白大小382 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 159 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=68.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 159 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TE12
- Protein Atlas: https://www.proteinatlas.org/ENSG00000162761-LMX1A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LMX1A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TE12
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000162761-LMX1A/subcellular

![](https://images.proteinatlas.org/30088/402_G8_1_red_green.jpg)
![](https://images.proteinatlas.org/30088/402_G8_2_red_green.jpg)
![](https://images.proteinatlas.org/30088/405_G8_1_red_green.jpg)
![](https://images.proteinatlas.org/30088/405_G8_2_red_green.jpg)
![](https://images.proteinatlas.org/30088/409_G8_1_red_green.jpg)
![](https://images.proteinatlas.org/30088/409_G8_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8TE12-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

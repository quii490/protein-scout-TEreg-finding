---
type: protein-evaluation
gene: "EPHX2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EPHX2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=292，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EPHX2 |
| 蛋白名称 | Bifunctional epoxide hydrolase 2 |
| 蛋白大小 | 555 aa / 62.6 kDa |
| UniProt ID | P34913 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Cytosol; UniProt: Cytoplasm; Peroxisome |
| 蛋白大小 | 10/10 | ×1 | 10 | 555 aa / 62.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=292 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=93.3; PDB: 1S8O, 1VJ5, 1ZD2, 1ZD3, 1ZD4, 1ZD5, 3ANS |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000073, IPR029058, IPR000639, IPR036412, IPR006 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 6 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **76.0/180** | |
| **归一化总分** | | | **42.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Enhanced |
| UniProt | Cytoplasm; Peroxisome | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- peroxisomal matrix (GO:0005782)
- peroxisome (GO:0005777)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 292 |
| PubMed broad count | 502 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Systematic druggable genome-wide Mendelian randomisation identifies therapeutic targets for Alzheimer's disease.. *Journal of neurology, neurosurgery, and psychiatry*. PMID: 37349091
2. Integrative single-cell RNA sequencing and metabolomics decipher the imbalanced lipid-metabolism in maladaptive immune responses during sepsis.. *Frontiers in immunology*. PMID: 37180171
3. EETs Reduction Contributes to Granulosa Cell Senescence and Endometriosis-Associated Infertility via the PI3K/AKT/mTOR Signaling Pathway.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 40827571
4. Enhancement of the liver's neuroprotective role ameliorates traumatic brain injury pathology.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 37339206
5. Proteomics and bioinformatics analysis of mouse hypothalamic neurogenesis with or without EPHX2 gene deletion.. *International journal of clinical and experimental pathology*. PMID: 26722453

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.3 |
| 高置信度残基 (pLDDT>90) 占比 | 80.0% |
| 置信残基 (pLDDT 70-90) 占比 | 17.3% |
| 中等置信 (pLDDT 50-70) 占比 | 1.8% |
| 低置信 (pLDDT<50) 占比 | 0.9% |
| 有序区域 (pLDDT>70) 占比 | 97.3% |
| 可用 PDB 条目 | 1S8O, 1VJ5, 1ZD2, 1ZD3, 1ZD4, 1ZD5, 3ANS, 3ANT, 3I1Y, 3I28 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1S8O, 1VJ5, 1ZD2, 1ZD3, 1ZD4, 1ZD5, 3ANS, 3ANT, 3I1Y, 3I28）+ AlphaFold极高置信度预测（pLDDT=93.3），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000073, IPR029058, IPR000639, IPR036412, IPR006439; Pfam: PF00561, PF00702 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CYP2J2 | 0.981 | 0.068 | — |
| CYP2C8 | 0.973 | 0.068 | — |
| CYP2C9 | 0.967 | 0.068 | — |
| CYP2B6 | 0.944 | 0.068 | — |
| PNP | 0.927 | 0.000 | — |
| IMPDH2 | 0.884 | 0.162 | — |
| MTAP | 0.877 | 0.000 | — |
| NUDT12 | 0.865 | 0.088 | — |
| GMPR2 | 0.860 | 0.000 | — |
| IMPDH1 | 0.859 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NIPSNAP3A | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| MVP | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| ENSP00000430269.1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| CAT | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| Snta1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:24952909|imex:IM-26422 |
| Cav3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:24952909|imex:IM-26422 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 6
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 6 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.3 + PDB: 1S8O, 1VJ5, 1ZD2, 1ZD3, 1ZD4,  | pLDDT=93.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Peroxisome / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 6 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. EPHX2 — Bifunctional epoxide hydrolase 2，研究基础较多，新颖性有限。
2. 蛋白大小555 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 292 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P34913
- Protein Atlas: https://www.proteinatlas.org/ENSG00000120915-EPHX2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EPHX2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P34913
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P34913-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

---
type: protein-evaluation
gene: "NFATC1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NFATC1 — REJECTED (研究热度过高 (PubMed strict=1913，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NFATC1 / NFAT2, NFATC |
| 蛋白名称 | Nuclear factor of activated T-cells, cytoplasmic 1 |
| 蛋白大小 | 943 aa / 101.2 kDa |
| UniProt ID | O95644 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear bodies; 额外: Nucleoplasm; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 943 aa / 101.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1913 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.8; PDB: 1A66, 1NFA, 5SVE |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR013783, IPR014756, IPR002909, IPR008366, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.5/180** | |
| **归一化总分** | | | **44.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies; 额外: Nucleoplasm | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1913 |
| PubMed broad count | 3619 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NFAT2, NFATC |

**关键文献**:
1. NFATc1 signaling drives chronic ER stress responses to promote NAFLD progression.. *Gut*. PMID: 35365570
2. Long noncoding RNA Malat1 protects against osteoporosis and bone metastasis.. *Nature communications*. PMID: 38493144
3. Aconine inhibits RANKL-induced osteoclast differentiation in RAW264.7 cells by suppressing NF-κB and NFATc1 activation and DC-STAMP expression.. *Acta pharmacologica Sinica*. PMID: 26592521
4. Where it all started.. *eLife*. PMID: 37017508
5. SKAP1 Expression in Cancer Cells Enhances Colon Tumor Growth and Impairs Cytotoxic Immunity by Promoting Neutrophil Extracellular Trap Formation via the NFATc1/CXCL8 Axis.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 39269257

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.8 |
| 高置信度残基 (pLDDT>90) 占比 | 22.9% |
| 置信残基 (pLDDT 70-90) 占比 | 8.3% |
| 中等置信 (pLDDT 50-70) 占比 | 7.3% |
| 低置信 (pLDDT<50) 占比 | 61.5% |
| 有序区域 (pLDDT>70) 占比 | 31.2% |
| 可用 PDB 条目 | 1A66, 1NFA, 5SVE |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=56.8），有序残基占 31.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013783, IPR014756, IPR002909, IPR008366, IPR008967; Pfam: PF16179, PF00554 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PPP3CA | 0.999 | 0.976 | — |
| PPP3R1 | 0.998 | 0.944 | — |
| NFATC2 | 0.979 | 0.166 | — |
| JUN | 0.963 | 0.330 | — |
| GATA4 | 0.957 | 0.051 | — |
| PPP3CC | 0.956 | 0.463 | — |
| SP7 | 0.955 | 0.000 | — |
| ACP5 | 0.954 | 0.000 | — |
| GSK3B | 0.953 | 0.166 | — |
| MAPK8 | 0.951 | 0.234 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| PPP3CC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| OBSL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SEMA7A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HMGCS2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PPP3R1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PLOD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PPP3CA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| LRRC28 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ARMC8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZMYND19 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.8 + PDB: 1A66, 1NFA, 5SVE | pLDDT=56.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nuclear bodies; 额外: Nucleoplasm | 一致 |
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
1. NFATC1 — Nuclear factor of activated T-cells, cytoplasmic 1，研究基础较多，新颖性有限。
2. 蛋白大小943 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 1913 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=56.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1913 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O95644
- Protein Atlas: https://www.proteinatlas.org/ENSG00000131196-NFATC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NFATC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O95644
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (supported)。来源: https://www.proteinatlas.org/ENSG00000131196-NFATC1/subcellular

![](https://images.proteinatlas.org/71732/1357_F12_1_red_green.jpg)
![](https://images.proteinatlas.org/71732/1357_F12_2_red_green.jpg)
![](https://images.proteinatlas.org/71732/1359_F12_4_red_green.jpg)
![](https://images.proteinatlas.org/71732/1359_F12_5_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O95644-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O95644 |
| SMART | SM00429; |
| UniProt Domain [FT] | DOMAIN 410..592; /note="RHD"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00265" |
| InterPro | IPR013783;IPR014756;IPR002909;IPR008366;IPR008967;IPR032397;IPR011539;IPR037059; |
| Pfam | PF16179;PF00554; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000131196-NFATC1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CREB1 | Intact, Biogrid | true |
| JUN | Intact, Biogrid | true |
| ATF1 | Intact | false |
| ATF2 | Intact | false |
| ATF3 | Intact | false |
| CHEK1 | Biogrid | false |
| CREBBP | Biogrid | false |
| EP300 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

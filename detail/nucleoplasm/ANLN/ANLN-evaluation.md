---
type: protein-evaluation
gene: "ANLN"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ANLN — REJECTED (研究热度过高 (PubMed strict=258，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ANLN |
| 蛋白名称 | Anillin |
| 蛋白大小 | 1124 aa / 124.2 kDa |
| UniProt ID | Q9NQW6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Midbody; UniProt: Nucleus; Cytoplasm, cytoskeleton; Cytoplasm, cell cortex; Ce |
| 蛋白大小 | 8/10 | ×1 | 8 | 1124 aa / 124.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=258 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.2; PDB: 2Y7B, 4XH3, 4XOI |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR012966, IPR031970, IPR051364, IPR011993, IPR037 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.5/180** | |
| **归一化总分** | | | **44.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Midbody | Supported |
| UniProt | Nucleus; Cytoplasm, cytoskeleton; Cytoplasm, cell cortex; Cell projection, bleb | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- actin cytoskeleton (GO:0015629)
- actomyosin contractile ring (GO:0005826)
- bleb (GO:0032059)
- cell cortex (GO:0005938)
- cytosol (GO:0005829)
- midbody (GO:0030496)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 258 |
| PubMed broad count | 342 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Targeting USP10 induces degradation of oncogenic ANLN in esophageal squamous cell carcinoma.. *Cell death and differentiation*. PMID: 36526897
2. Mechanotransduction and YAP-dependent matrix remodelling is required for the generation and maintenance of cancer-associated fibroblasts.. *Nature cell biology*. PMID: 23708000
3. A Therapeutically Targetable TAZ-TEAD2 Pathway Drives the Growth of Hepatocellular Carcinoma via ANLN and KIF23.. *Gastroenterology*. PMID: 36894036
4. Penfluridol suppresses MYC-driven ANLN expression and liver cancer progression by disrupting the KEAP1-NRF2 interaction.. *Pharmacological research*. PMID: 39643070
5. Integrating machine learning models with multi-omics analysis to decipher the prognostic significance of mitotic catastrophe heterogeneity in bladder cancer.. *Biology direct*. PMID: 40259382

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.2 |
| 高置信度残基 (pLDDT>90) 占比 | 23.8% |
| 置信残基 (pLDDT 70-90) 占比 | 13.5% |
| 中等置信 (pLDDT 50-70) 占比 | 7.6% |
| 低置信 (pLDDT<50) 占比 | 55.2% |
| 有序区域 (pLDDT>70) 占比 | 37.3% |
| 可用 PDB 条目 | 2Y7B, 4XH3, 4XOI |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=59.2），有序残基占 37.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR012966, IPR031970, IPR051364, IPR011993, IPR037840; Pfam: PF08174, PF16018, PF00169 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RHOA | 0.999 | 0.959 | — |
| RACGAP1 | 0.997 | 0.416 | — |
| ECT2 | 0.994 | 0.292 | — |
| KIF23 | 0.989 | 0.331 | — |
| DIAPH3 | 0.988 | 0.000 | — |
| KIF20A | 0.949 | 0.328 | — |
| KIF11 | 0.947 | 0.000 | — |
| CEP55 | 0.930 | 0.292 | — |
| TPX2 | 0.923 | 0.000 | — |
| BUB1 | 0.917 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000265748.2 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| eprs1.S | psi-mi:"MI:0029"(cosedimentation through density g | pubmed:20174651|imex:IM-17228 |
| eef1a1o.S | psi-mi:"MI:0029"(cosedimentation through density g | pubmed:20174651|imex:IM-17228 |
| hdlbp.S | psi-mi:"MI:0029"(cosedimentation through density g | pubmed:20174651|imex:IM-17228 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| MAGI1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SSH2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| MRPL16 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| AAK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=59.2 + PDB: 2Y7B, 4XH3, 4XOI | pLDDT=59.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, cytoskeleton; Cytoplasm, cell  / Nucleoplasm; 额外: Midbody | 一致 |
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
1. ANLN — Anillin，研究基础较多，新颖性有限。
2. 蛋白大小1124 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 258 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=59.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 258 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NQW6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000011426-ANLN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ANLN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NQW6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000011426-ANLN/subcellular

![](https://images.proteinatlas.org/50556/1773_B9_5_red_green.jpg)
![](https://images.proteinatlas.org/50556/1773_B9_7_red_green.jpg)
![](https://images.proteinatlas.org/50556/694_G8_1_red_green.jpg)
![](https://images.proteinatlas.org/50556/694_G8_2_red_green.jpg)
![](https://images.proteinatlas.org/50556/790_B10_1_red_green.jpg)
![](https://images.proteinatlas.org/50556/790_B10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NQW6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NQW6 |
| SMART | SM00233; |
| UniProt Domain [FT] | DOMAIN 983..1107; /note="PH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00145" |
| InterPro | IPR012966;IPR031970;IPR051364;IPR011993;IPR037840;IPR001849; |
| Pfam | PF08174;PF16018;PF00169; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000011426-ANLN/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| POLR1E | Biogrid, Opencell | true |
| AAR2 | Biogrid | false |
| ABCD3 | Biogrid | false |
| ABCF2 | Biogrid | false |
| ABLIM1 | Biogrid | false |
| ACIN1 | Biogrid | false |
| ACTC1 | Biogrid | false |
| ACTN1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

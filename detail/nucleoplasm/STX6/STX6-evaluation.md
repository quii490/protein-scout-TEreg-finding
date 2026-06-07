---
type: protein-evaluation
gene: "STX6"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## STX6 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | STX6 |
| 蛋白名称 | Syntaxin-6 |
| 蛋白大小 | 255 aa / 29.2 kDa |
| UniProt ID | O43752 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Golgi apparatus; 额外: Nucleoplasm, Cytosol; UniProt: Golgi apparatus membrane; Golgi apparatus, trans-Golgi netwo |
| 蛋白大小 | 10/10 | ×1 | 10 | 255 aa / 29.2 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=65 篇 (≤80→4) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=81.8; PDB: 2NPS, 4J2C |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR010989, IPR015260, IPR006012, IPR000727; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **112.0/180** | |
| **归一化总分** | | | **62.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nucleoplasm, Cytosol | Supported |
| UniProt | Golgi apparatus membrane; Golgi apparatus, trans-Golgi network membrane; Recycling endosome membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- clathrin-coated vesicle (GO:0030136)
- cytosol (GO:0005829)
- early endosome (GO:0005769)
- endomembrane system (GO:0012505)
- Golgi apparatus (GO:0005794)
- Golgi membrane (GO:0000139)
- nucleoplasm (GO:0005654)
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 65 |
| PubMed broad count | 104 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Syntaxin6 contributes to hepatocellular carcinoma tumorigenesis via enhancing STAT3 phosphorylation.. *Cancer cell international*. PMID: 38834986
2. A Spanish-Portuguese GWAS of progressive supranuclear palsy reveals a novel risk locus in NFASC.. *European journal of human genetics : EJHG*. PMID: 40379966
3. Multiomic analyses direct hypotheses for Creutzfeldt-Jakob disease risk genes.. *Brain : a journal of neurology*. PMID: 39865733
4. Characterisation and prion transmission study in mice with genetic reduction of sporadic Creutzfeldt-Jakob disease risk gene Stx6.. *Neurobiology of disease*. PMID: 37996040
5. Genetic risk factors for Creutzfeldt-Jakob disease.. *Neurobiology of disease*. PMID: 32565065

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.8 |
| 高置信度残基 (pLDDT>90) 占比 | 36.5% |
| 置信残基 (pLDDT 70-90) 占比 | 47.1% |
| 中等置信 (pLDDT 50-70) 占比 | 11.4% |
| 低置信 (pLDDT<50) 占比 | 5.1% |
| 有序区域 (pLDDT>70) 占比 | 83.6% |
| 可用 PDB 条目 | 2NPS, 4J2C |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2NPS, 4J2C）+ AlphaFold高质量预测（pLDDT=81.8），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR010989, IPR015260, IPR006012, IPR000727; Pfam: PF05739, PF09177 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| VAMP4 | 0.999 | 0.996 | — |
| STX12 | 0.999 | 0.988 | — |
| VAMP8 | 0.999 | 0.971 | — |
| SNAP29 | 0.999 | 0.994 | — |
| VTI1A | 0.999 | 0.997 | — |
| VAMP3 | 0.999 | 0.876 | — |
| VTI1B | 0.999 | 0.888 | — |
| STX16 | 0.999 | 0.782 | — |
| SNAP23 | 0.998 | 0.791 | — |
| STX4 | 0.998 | 0.828 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EEA1 | psi-mi:"MI:0018"(two hybrid) | pubmed:10506127 |
| SCAMP5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:19234194|imex:IM-20480 |
| Slc2a4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:16396496|mint:MINT-5218 |
| NSF | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| Clstn1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:20925061|imex:IM-15783 |
| TGOLN2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| DNAJC5 | psi-mi:"MI:0012"(bioluminescence resonance energy  | pubmed:29997244|imex:IM-26441| |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| VAMP5 | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |
| NAPA | psi-mi:"MI:0096"(pull down) | pubmed:30833792|imex:IM-26691 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.8 + PDB: 2NPS, 4J2C | pLDDT=81.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Golgi apparatus membrane; Golgi apparatus, trans-G / Golgi apparatus; 额外: Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. STX6 — Syntaxin-6，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小255 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 65 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43752
- Protein Atlas: https://www.proteinatlas.org/ENSG00000135823-STX6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=STX6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43752
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (supported)。来源: https://www.proteinatlas.org/ENSG00000135823-STX6/subcellular

![](https://images.proteinatlas.org/38557/537_C12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/38557/537_C12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/38557/540_C12_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/38557/540_C12_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/38557/553_C12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/38557/553_C12_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O43752-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O43752 |
| SMART | SM00397; |
| UniProt Domain [FT] | DOMAIN 163..225; /note="t-SNARE coiled-coil homology"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00202" |
| InterPro | IPR010989;IPR015260;IPR006012;IPR000727; |
| Pfam | PF05739;PF09177; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000135823-STX6/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| GOSR2 | Intact, Biogrid | true |
| NAPA | Biogrid, Opencell, Bioplex | true |
| NAPB | Intact, Biogrid, Bioplex | true |
| NSF | Biogrid, Opencell, Bioplex | true |
| SCFD1 | Biogrid, Opencell, Bioplex | true |
| SEC22B | Biogrid, Bioplex | true |
| SNAP23 | Biogrid, Opencell | true |
| STX10 | Biogrid, Bioplex | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

---
type: protein-evaluation
gene: "FOXK1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FOXK1 — REJECTED (研究热度过高 (PubMed strict=137，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FOXK1 / MNF |
| 蛋白名称 | Forkhead box protein K1 |
| 蛋白大小 | 733 aa / 75.5 kDa |
| UniProt ID | P85037 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nucleoli fibrillar center; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 733 aa / 75.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=137 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.7; PDB: 8BZM |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR047394, IPR000253, IPR001766, IPR008984, IPR018 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.5/180** | |
| **归一化总分** | | | **44.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli fibrillar center | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 137 |
| PubMed broad count | 230 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MNF |

**关键文献**:
1. Forkhead Box Protein K1 Promotes Chronic Kidney Disease by Driving Glycolysis in Tubular Epithelial Cells.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 39083268
2. ATF3 -activated accelerating effect of LINC00941/lncIAPF on fibroblast-to-myofibroblast differentiation by blocking autophagy depending on ELAVL1/HuR in pulmonary fibrosis.. *Autophagy*. PMID: 35427207
3. FoxK1 and FoxK2 cooperate with ORF45 to promote late lytic replication of Kaposi's sarcoma-associated herpesvirus.. *Journal of virology*. PMID: 39494902
4. Epigenetic regulation of ACSL4 via H2A monoubiquitylation connects lipid metabolism to BAP1-mediated ferroptosis.. *Cell death and differentiation*. PMID: 41310183
5. Forkhead box protein FOXK1 disrupts the circadian rhythm to promote breast tumorigenesis in response to insulin resistance.. *Cancer letters*. PMID: 39094826

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.7 |
| 高置信度残基 (pLDDT>90) 占比 | 21.0% |
| 置信残基 (pLDDT 70-90) 占比 | 9.1% |
| 中等置信 (pLDDT 50-70) 占比 | 9.3% |
| 低置信 (pLDDT<50) 占比 | 60.6% |
| 有序区域 (pLDDT>70) 占比 | 30.1% |
| 可用 PDB 条目 | 8BZM |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=56.7），有序残基占 30.1%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR047394, IPR000253, IPR001766, IPR008984, IPR018122; Pfam: PF00498, PF00250 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ASXL1 | 0.987 | 0.698 | — |
| BAP1 | 0.982 | 0.838 | — |
| OGT | 0.971 | 0.048 | — |
| ASXL2 | 0.962 | 0.697 | — |
| HCFC1 | 0.957 | 0.308 | — |
| SIN3A | 0.946 | 0.368 | — |
| KDM1B | 0.911 | 0.046 | — |
| SIN3B | 0.826 | 0.154 | — |
| MBD5 | 0.812 | 0.000 | — |
| YY1 | 0.786 | 0.096 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Sin3b | psi-mi:"MI:0018"(two hybrid) | pubmed:10620510|imex:IM-19242 |
| ENSMUSP00000072616.6 | psi-mi:"MI:0413"(electrophoretic mobility shift as | pubmed:10620510|imex:IM-19242 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| MAP1LC3A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| MAP1LC3B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| BAP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| AMOT | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| FYCO1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| comEA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| IRF2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21903422|imex:IM-17322 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.7 + PDB: 8BZM | pLDDT=56.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm; 额外: Nucleoli fibrillar center | 一致 |
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
1. FOXK1 — Forkhead box protein K1，研究基础较多，新颖性有限。
2. 蛋白大小733 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 137 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=56.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 137 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P85037
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164916-FOXK1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FOXK1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P85037
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000164916-FOXK1/subcellular

![](https://images.proteinatlas.org/17998/143_D7_1_red_green.jpg)
![](https://images.proteinatlas.org/17998/143_D7_2_red_green.jpg)
![](https://images.proteinatlas.org/17998/144_D7_1_red_green.jpg)
![](https://images.proteinatlas.org/17998/144_D7_2_red_green.jpg)
![](https://images.proteinatlas.org/17998/145_D7_1_red_green.jpg)
![](https://images.proteinatlas.org/17998/145_D7_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P85037-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P85037 |
| SMART | SM00339;SM00240; |
| UniProt Domain [FT] | DOMAIN 123..175; /note="FHA"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00086" |
| InterPro | IPR047394;IPR000253;IPR001766;IPR008984;IPR018122;IPR030456;IPR036388;IPR036390; |
| Pfam | PF00498;PF00250; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000164916-FOXK1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BAP1 | Biogrid, Bioplex | true |
| DCAF7 | Intact, Biogrid | true |
| ING2 | Biogrid, Bioplex | true |
| IRF2 | Intact, Biogrid | true |
| SAP30 | Biogrid, Bioplex | true |
| YWHAB | Biogrid, Opencell | true |
| YWHAG | Biogrid, Opencell | true |
| ARID4A | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

---
type: protein-evaluation
gene: "NSMAF"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## NSMAF 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NSMAF / FAN |
| 蛋白名称 | Protein FAN |
| 蛋白大小 | 917 aa / 104.4 kDa |
| UniProt ID | Q92636 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 917 aa / 104.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=88.3; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR000409, IPR036372, IPR050865, IPR057496, IPR004 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.0/180** | |
| **归一化总分** | | | **67.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 46 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FAN |

**关键文献**:
1. Screening for Immune-Related RNA Biomarkers of Aneurysmal Subarachnoid Hemorrhage.. *Clinical and investigative medicine. Medecine clinique et experimentale*. PMID: 35752978
2. Exosomal MicroRNAs modulate the cognitive function in fasudil treated APPswe/PSEN1dE9 transgenic (APP/PS1) mice model of Alzheimer's disease.. *Metabolic brain disease*. PMID: 39088109
3. Selected Clinical Features Fail to Predict Inflammatory Gene Expressions for TNF-α, TNFR1, NSMAF, Casp3 and IL-8 in Tendons of Patients with Rotator Cuff Tendinopathy.. *Archivum immunologiae et therapiae experimentalis*. PMID: 33683459
4. The LC3-conjugation machinery specifies cargo loading and secretion of extracellular vesicles.. *Autophagy*. PMID: 32401566
5. Alterations in TNF- and IL-related gene expression in space-flown WI38 human fibroblasts.. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology*. PMID: 12039873

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.3 |
| 高置信度残基 (pLDDT>90) 占比 | 70.3% |
| 置信残基 (pLDDT 70-90) 占比 | 20.1% |
| 中等置信 (pLDDT 50-70) 占比 | 4.0% |
| 低置信 (pLDDT<50) 占比 | 5.6% |
| 有序区域 (pLDDT>70) 占比 | 90.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=88.3，有序区 90.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000409, IPR036372, IPR050865, IPR057496, IPR004182; Pfam: PF02138, PF02893, PF25400 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000038176.3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| MAP1LC3A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| GABARAPL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| GABARAP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| GABARAPL2 | psi-mi:"MI:0096"(pull down) | pubmed:20562859|imex:IM-15184 |
| MAP1LC3B | psi-mi:"MI:0096"(pull down) | pubmed:20562859|imex:IM-15184 |
| MAP1LC3C | psi-mi:"MI:0096"(pull down) | pubmed:20562859|imex:IM-15184 |
| NEK9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| KRT4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| XIRP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.3 + PDB: 无 | pLDDT=88.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nucleoli | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. NSMAF — Protein FAN，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小917 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92636
- Protein Atlas: https://www.proteinatlas.org/ENSG00000035681-NSMAF/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NSMAF
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92636
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (approved)。来源: https://www.proteinatlas.org/ENSG00000035681-NSMAF/subcellular

![](https://images.proteinatlas.org/23151/237_F5_1_red_green.jpg)
![](https://images.proteinatlas.org/23151/237_F5_2_red_green.jpg)
![](https://images.proteinatlas.org/23151/268_F5_1_red_green.jpg)
![](https://images.proteinatlas.org/23151/268_F5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q92636-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q92636 |
| SMART | SM01026;SM00568;SM00320; |
| UniProt Domain [FT] | DOMAIN 176..247; /note="GRAM"; DOMAIN 189..286; /note="BEACH-type PH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01119"; DOMAIN 290..575; /note="BEACH"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00026" |
| InterPro | IPR000409;IPR036372;IPR050865;IPR057496;IPR004182;IPR023362;IPR011993;IPR015943;IPR036322;IPR001680; |
| Pfam | PF02138;PF02893;PF25400;PF00400; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000035681-NSMAF/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ACTB | Intact, Biogrid | true |
| DCP1A | Intact, Biogrid | true |
| DCP1B | Intact, Biogrid | true |
| GABARAPL1 | Intact, Biogrid | true |
| GABARAP | Intact | false |
| RACK1 | Biogrid | false |
| TNFRSF1A | Biogrid | false |
| VASP | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

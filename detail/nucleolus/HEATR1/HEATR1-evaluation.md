---
type: protein-evaluation
gene: "HEATR1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HEATR1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HEATR1 / BAP28, UTP10 |
| 蛋白名称 | HEAT repeat-containing protein 1 |
| 蛋白大小 | 2144 aa / 242.4 kDa |
| UniProt ID | Q9H583 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli fibrillar center; 额外: Mitochondria; UniProt: Nucleus, nucleolus |
| 蛋白大小 | 2/10 | ×1 | 2 | 2144 aa / 242.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=19 篇 (≤20→10) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=78.7; PDB: 7MQ8, 7MQ9, 7MQA |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011989, IPR016024, IPR012954, IPR056473, IPR022 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.0/180** | |
| **归一化总分** | | | **73.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli fibrillar center; 额外: Mitochondria | Enhanced |
| UniProt | Nucleus, nucleolus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 90S preribosome (GO:0030686)
- fibrillar center (GO:0001650)
- membrane (GO:0016020)
- mitochondrion (GO:0005739)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- small-subunit processome (GO:0032040)
- t-UTP complex (GO:0034455)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 19 |
| PubMed broad count | 24 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BAP28, UTP10 |

**关键文献**:
1. Nucleolar HEAT Repeat Containing 1 Up-regulated by the Mechanistic Target of Rapamycin Complex 1 Signaling Promotes Hepatocellular Carcinoma Growth by Dominating Ribosome Biogenesis and Proteome Homeostasis.. *Gastroenterology*. PMID: 37247644
2. HEATR1 deficiency promotes pancreatic cancer proliferation and gemcitabine resistance by up-regulating Nrf2 signaling.. *Redox biology*. PMID: 31785531
3. HEATR1 promotes proliferation in gastric cancer in vitro and in vivo.. *Acta biochimica et biophysica Sinica*. PMID: 32634230
4. HEATR1, a novel interactor of Pontin/Reptin, stabilizes Pontin/Reptin and promotes cell proliferation of oral squamous cell carcinoma.. *Biochemical and biophysical research communications*. PMID: 33894417
5. HEATR1 Deficiency Promotes Chemoresistance via Upregulating ZNF185 and Downregulating SMAD4 in Pancreatic Cancer.. *Journal of oncology*. PMID: 32565799

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.7 |
| 高置信度残基 (pLDDT>90) 占比 | 13.2% |
| 置信残基 (pLDDT 70-90) 占比 | 67.6% |
| 中等置信 (pLDDT 50-70) 占比 | 14.4% |
| 低置信 (pLDDT<50) 占比 | 4.8% |
| 有序区域 (pLDDT>70) 占比 | 80.8% |
| 可用 PDB 条目 | 7MQ8, 7MQ9, 7MQA |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（7MQ8, 7MQ9, 7MQA）+ AlphaFold高质量预测（pLDDT=78.7），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR012954, IPR056473, IPR022125; Pfam: PF08146, PF23243, PF12397 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| WDR36 | 0.999 | 0.991 | — |
| TBL3 | 0.999 | 0.991 | — |
| BMS1 | 0.999 | 0.991 | — |
| PDCD11 | 0.999 | 0.966 | — |
| UTP20 | 0.999 | 0.991 | — |
| PWP2 | 0.999 | 0.967 | — |
| RRP9 | 0.999 | 0.991 | — |
| WDR3 | 0.999 | 0.980 | — |
| UTP18 | 0.999 | 0.991 | — |
| NAT10 | 0.999 | 0.981 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Hrs | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| SkpB | psi-mi:"MI:0018"(two hybrid) | pubmed:15575970|mint:MINT-7952 |
| SkpA | psi-mi:"MI:0018"(two hybrid) | pubmed:15575970|mint:MINT-7952 |
| XRN1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| Sirt1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| PTP4A3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MYC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TTBK1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| VCAM1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-17358|pubmed:22623428 |
| EBI-6248077 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-17346|pubmed:22190034| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.7 + PDB: 7MQ8, 7MQ9, 7MQA | pLDDT=78.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleolus / Nucleoli fibrillar center; 额外: Mitochondria | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. HEATR1 — HEAT repeat-containing protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小2144 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 19 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H583
- Protein Atlas: https://www.proteinatlas.org/ENSG00000119285-HEATR1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HEATR1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H583
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli fibrillar center (enhanced)。来源: https://www.proteinatlas.org/ENSG00000119285-HEATR1/subcellular

![](https://images.proteinatlas.org/46917/715_D5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/46917/715_D5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/46917/725_D5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/46917/725_D5_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/46917/812_D5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/46917/812_D5_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H583-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H583 |
| SMART | SM01036; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR011989;IPR016024;IPR012954;IPR056473;IPR022125;IPR040191; |
| Pfam | PF08146;PF23243;PF12397; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000119285-HEATR1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ANLN | Biogrid | false |
| CA14 | Bioplex | false |
| CCNF | Biogrid | false |
| CD40 | Bioplex | false |
| CD70 | Bioplex | false |
| COMTD1 | Bioplex | false |
| F2RL1 | Bioplex | false |
| FAM174A | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->

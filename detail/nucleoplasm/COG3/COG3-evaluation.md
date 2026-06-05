---
type: protein-evaluation
gene: "COG3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## COG3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | COG3 / SEC34 |
| 蛋白名称 | Conserved oligomeric Golgi complex subunit 3 |
| 蛋白大小 | 828 aa / 94.1 kDa |
| UniProt ID | Q96JB2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Golgi apparatus, Plasma membrane; 额外: Nucleoplasm, Cytosol; UniProt: Golgi apparatus, Golgi stack membrane |
| 蛋白大小 | 8/10 | x1 | 8 | 828 aa / 94.1 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=25 篇 (<=40->8) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=78.4; PDB: 无 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR048685, IPR048320, IPR007265; Pfam: PF20671, PF |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **109.5/180** | |
| **归一化总分** | | | **60.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus, Plasma membrane; 额外: Nucleoplasm, Cytosol | Supported |
| UniProt | Golgi apparatus, Golgi stack membrane | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- cis-Golgi network (GO:0005801)
- cytosol (GO:0005829)
- Golgi apparatus (GO:0005794)
- Golgi cisterna membrane (GO:0032580)
- Golgi membrane (GO:0000139)
- Golgi transport complex (GO:0017119)
- plasma membrane (GO:0005886)
- trans-Golgi network membrane (GO:0032588)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 25 |
| PubMed broad count | 55 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SEC34 |

**关键文献**:
1. COG3 confers the chilling tolerance to mediate OsFtsH2-D1 module in rice.. *The New phytologist*. PMID: 38173177
2. Arabidopsis COG Complex Subunits COG3 and COG8 Modulate Golgi Morphology, Vesicle Trafficking Homeostasis and Are Essential for Pollen Tube Growth.. *PLoS genetics*. PMID: 27448097
3. Tumor Targeting via siRNA-COG3 to Suppress Tumor Progression in Mice and Inhibit Cancer Metastasis and Angiogenesis in Ovarian Cancer Cell Lines.. *MicroRNA (Shariqah, United Arab Emirates)*. PMID: 38243930
4. Meta-Analysis of Keratoconus Transcriptomic Data Revealed Altered RNA Editing Levels Impacting Keratin Genomic Clusters.. *Investigative ophthalmology & visual science*. PMID: 37279397
5. COG1-congenital disorders of glycosylation: Milder presentation and review.. *Clinical genetics*. PMID: 33960418

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 78.4 |
| 高置信度残基 (pLDDT>90) 占比 | 38.6% |
| 置信残基 (pLDDT 70-90) 占比 | 35.5% |
| 中等置信 (pLDDT 50-70) 占比 | 15.1% |
| 低置信 (pLDDT<50) 占比 | 10.7% |
| 有序区域 (pLDDT>70) 占比 | 74.1% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=78.4，有序区 74.1%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR048685, IPR048320, IPR007265; Pfam: PF20671, PF04136 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| COG7 | 0.999 | 0.930 | — |
| COG1 | 0.999 | 0.946 | — |
| COG8 | 0.999 | 0.951 | — |
| COG6 | 0.999 | 0.985 | — |
| COG5 | 0.999 | 0.919 | — |
| COG2 | 0.999 | 0.953 | — |
| COG4 | 0.999 | 0.965 | — |
| COPB1 | 0.927 | 0.000 | — |
| VPS52 | 0.918 | 0.091 | — |
| GOSR2 | 0.909 | 0.088 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| rpr | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| COG5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| COG1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| COG2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| COG4 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| COG6 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| COG7 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| COG8 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| SSA2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| MED2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=78.4 + PDB: 无 | pLDDT=78.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus, Golgi stack membrane / Golgi apparatus, Plasma membrane; 额外: Nucleoplasm, | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ***

**核心优势**:
1. COG3 -- Conserved oligomeric Golgi complex subunit 3，非常新颖，仅有少数基础研究。
2. 蛋白大小828 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 25 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96JB2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000136152-COG3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=COG3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96JB2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96JB2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

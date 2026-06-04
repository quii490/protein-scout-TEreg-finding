---
type: protein-evaluation
gene: "SHTN1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SHTN1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SHTN1 / KIAA1598 |
| 蛋白名称 | Shootin-1 |
| 蛋白大小 | 631 aa / 71.6 kDa |
| UniProt ID | A0MZ66 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane, Cytosol; 额外: Nucleoplasm, Centrosome, Basal; UniProt: Perikaryon; Cell projection, axon; Cell projection, growth c |
| 蛋白大小 | 10/10 | ×1 | 10 | 631 aa / 71.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=70.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR024849 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cytosol; 额外: Nucleoplasm, Centrosome, Basal body | Approved |
| UniProt | Perikaryon; Cell projection, axon; Cell projection, growth cone; Cytoplasm, cytoskeleton; Cell proje... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- axon (GO:0030424)
- axonal growth cone (GO:0044295)
- cell leading edge (GO:0031252)
- cytoplasm (GO:0005737)
- filopodium (GO:0030175)
- growth cone (GO:0030426)
- lamellipodium (GO:0030027)
- microtubule (GO:0005874)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 30 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1598 |

**关键文献**:
1. Shootin1 Regulates Retinal Ganglion Cell Neurite Development: Insights From an RGC Direct Somatic Cell Reprogramming Model.. *Investigative ophthalmology & visual science*. PMID: 38935030
2. Exploring Shootin1's oncogenic role within FGFR2 gene fusions.. *Turkish journal of biology = Turk biyoloji dergisi*. PMID: 41496852
3. Whole-Transcriptome Analysis Reveals Dysregulation of Actin-Cytoskeleton Pathway in Intellectual Disability Patients.. *Neuroscience*. PMID: 30742961
4. Data-mining-based biomarker evaluation and experimental validation of SHTN1 for bladder cancer.. *Cancer genetics*. PMID: 39260052
5. Axonogenesis Is Coordinated by Neuron-Specific Alternative Splicing Programming and Splicing Regulator PTBP2.. *Neuron*. PMID: 30733148

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.8 |
| 高置信度残基 (pLDDT>90) 占比 | 39.9% |
| 置信残基 (pLDDT 70-90) 占比 | 15.4% |
| 中等置信 (pLDDT 50-70) 占比 | 11.3% |
| 低置信 (pLDDT<50) 占比 | 33.4% |
| 有序区域 (pLDDT>70) 占比 | 55.3% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=70.8，有序区 55.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR024849 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| L1CAM | 0.980 | 0.051 | — |
| RUFY3 | 0.966 | 0.000 | — |
| LNX1 | 0.760 | 0.532 | — |
| HCLS1 | 0.649 | 0.098 | — |
| CTTN | 0.641 | 0.098 | — |
| AHCYL1 | 0.604 | 0.225 | — |
| TACC3 | 0.596 | 0.098 | — |
| BICC1 | 0.588 | 0.000 | — |
| HSPA12A | 0.555 | 0.102 | — |
| PPHLN1 | 0.545 | 0.097 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000376636.3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| ENSP00000347532.4 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| MEGF10 | psi-mi:"MI:0018"(two hybrid) | pubmed:unassigned5 |
| YWHAG | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| IKBKG | psi-mi:"MI:0089"(protein array) | pubmed:20098747|imex:IM-17256 |
| Mycbp2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |
| ARL6IP5 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| PRAF2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| DISC1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| EPHA1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.8 + PDB: 无 | pLDDT=70.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Perikaryon; Cell projection, axon; Cell projection / Plasma membrane, Cytosol; 额外: Nucleoplasm, Centros | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SHTN1 — Shootin-1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小631 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A0MZ66
- Protein Atlas: https://www.proteinatlas.org/ENSG00000187164-SHTN1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SHTN1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A0MZ66
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

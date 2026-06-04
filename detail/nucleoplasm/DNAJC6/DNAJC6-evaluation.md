---
type: protein-evaluation
gene: "DNAJC6"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DNAJC6 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DNAJC6 / KIAA0473 |
| 蛋白名称 | Auxilin |
| 蛋白大小 | 913 aa / 100.0 kDa |
| UniProt ID | O75061 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cytosol; 额外: Nucleoplasm, Plasma membrane; UniProt: Cytoplasmic vesicle, clathrin-coated vesicle |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 913 aa / 100.0 kDa |
| 🆕 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=93 篇 (≤100→2) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.9; PDB: 无 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR035892, IPR001623, IPR036869, IPR029021, IPR014 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| ➕ 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **75.5/180** | |
| **归一化总分** | | | **41.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm, Plasma membrane | Approved |
| UniProt | Cytoplasmic vesicle, clathrin-coated vesicle | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- clathrin-coated vesicle (GO:0030136)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extrinsic component of presynaptic endocytic zone membrane (GO:0098894)
- postsynaptic density (GO:0014069)
- vesicle (GO:0031982)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 93 |
| PubMed broad count | 131 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0473 |

**关键文献**:
1. Monogenic Parkinson's Disease: Genotype, Phenotype, Pathophysiology, and Genetic Testing.. *Genes*. PMID: 35328025
2. Parkinson's disease - genetic cause.. *Current opinion in neurology*. PMID: 37366140
3. Whole-exome Sequencing of Nigerian Prostate Tumors from the Prostate Cancer Transatlantic Consortium (CaPTC) Reveals DNA Repair Genes Associated with African Ancestry.. *Cancer research communications*. PMID: 36922933
4. Neurodevelopmental and synaptic defects in DNAJC6 parkinsonism, amenable to gene therapy.. *Brain : a journal of neurology*. PMID: 38242634
5. Gene regulation of RMR-related DNAJC6 on adipogenesis and mitochondria function in 3T3-L1 preadipocytes.. *Biochemical and biophysical research communications*. PMID: 37331165

**评价**: 有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.9 |
| 高置信度残基 (pLDDT>90) 占比 | 28.1% |
| 置信残基 (pLDDT 70-90) 占比 | 17.7% |
| 中等置信 (pLDDT 50-70) 占比 | 6.7% |
| 低置信 (pLDDT<50) 占比 | 47.4% |
| 有序区域 (pLDDT>70) 占比 | 45.8% |
| 可用 PDB 条目 | 无 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=62.9），有序残基占 45.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR035892, IPR001623, IPR036869, IPR029021, IPR014020; Pfam: PF10409 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HSPA8 | 0.999 | 0.904 | — |
| CLTC | 0.998 | 0.983 | — |
| CLTCL1 | 0.996 | 0.969 | — |
| CLHC1 | 0.974 | 0.967 | — |
| SYNJ1 | 0.913 | 0.070 | — |
| CLTA | 0.899 | 0.532 | — |
| CLINT1 | 0.839 | 0.529 | — |
| DNAJC13 | 0.824 | 0.000 | — |
| SH3GL2 | 0.824 | 0.000 | — |
| VPS35 | 0.817 | 0.067 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 3 / 15 = 20%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 20%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.9 + PDB: 无 | pLDDT=62.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasmic vesicle, clathrin-coated vesicle / Cytosol; 额外: Nucleoplasm, Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. DNAJC6 — Auxilin，有一定研究基础，但仍存在niche空间。
2. 蛋白大小913 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 93 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=62.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75061
- Protein Atlas: https://www.proteinatlas.org/ENSG00000116675-DNAJC6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DNAJC6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75061
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 12:17:44

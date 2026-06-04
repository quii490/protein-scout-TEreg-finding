---
type: protein-evaluation
gene: "EIF3B"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EIF3B — REJECTED (研究热度过高 (PubMed strict=144，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EIF3B |
| 蛋白名称 | Eukaryotic translation initiation factor 3 subunit B |
| 蛋白大小 | 814 aa / 92.5 kDa |
| UniProt ID | P55884 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cytosol; 额外: Nucleoplasm; UniProt: Cytoplasm; Cytoplasm, Stress granule |
| 蛋白大小 | 8/10 | ×1 | 8 | 814 aa / 92.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=144 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=73.2; PDB: 无 |
| 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **67.5/180** | |
| **归一化总分** | | | **37.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm | Supported |
| UniProt | Cytoplasm; Cytoplasm, Stress granule | Swiss-Prot/TrEMBL |

**IF/PAE 图像：已延迟**，核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。图像可后续通过 download_if.py / download_pae.py 下载。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 144 |
| PubMed broad count | 147 |
| 别名(未计入scoring) |  |

**关键文献**:
1. ADAM12 Stabilizes EIF3B to Promote Glycolysis and Tumor Progression in Hepatocellular Carcinoma.. *J Hepatocell Carcinoma*. PMID: 42117088
2. Inhibition of eukaryotic translation initiation factor 1 A (eIF1A) and 3B (eIF3B) diminishes the psoriatic phenotype in two mouse models and human 3D model samples.. *J Dermatol Sci*. PMID: 41916779
3. From Initiation to Elongation: eIF3 as a Dual-Phase Guardian of Mitochondrial Integrity and Protein Homeostasis in Skeletal Muscle.. *FASEB J*. PMID: 41989318
4. Endothelial USP2a-METTL16 loop potentiates IL-6 signaling via m(6)A-mediated IL-6R stabilization in pulmonary vascular remodeling.. *Cell Death Differ*. PMID: 42034790
5. SND1 regulates the androgen signaling axis by stabilizing EIF3B mRNA to facilitate the deterioration of prostate cancer.. *Mol Genet Genomics*. PMID: 41986545

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.2 |
| 高置信度残基 (pLDDT>90) 占比 | 21.6% |
| 置信残基 (pLDDT 70-90) 占比 | 48.0% |
| 中等置信 (pLDDT 50-70) 占比 | 11.4% |
| 低置信 (pLDDT<50) 占比 | 18.9% |
| 有序区域 (pLDDT>70) 占比 | 69.6% |
| 可用 PDB 条目 | 无 |

**PAE**: **PAE**: 已延迟，结构判断基于 AlphaFold pLDDT 统计。可后续通过 download_pae.py 下载。

**评价**: AlphaFold 中等质量（pLDDT=73.2，有序区 69.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EIF5 | 0.000 | 0.000 | — |
| RACK1 | 0.000 | 0.000 | — |
| EIF3L | 0.000 | 0.000 | — |
| EIF3A | 0.000 | 0.000 | — |
| EIF3K | 0.000 | 0.000 | — |
| EIF3G | 0.000 | 0.000 | — |
| EIF3F | 0.000 | 0.000 | — |
| EIF3E | 0.000 | 0.000 | — |
| EIF3M | 0.000 | 0.000 | — |
| EIF3H | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q0E940 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q14152 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:O75821 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q13347 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:O75822 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:- |
| uniprotkb:P55884 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q9U3Z7 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q8JZQ9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 0 / 20 = 0%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.2 + PDB: 无 | pLDDT=73.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, Stress granule / Cytosol; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 25 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. EIF3B — Eukaryotic translation initiation factor 3 subunit B，研究基础较多，新颖性有限。
2. 蛋白大小814 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 144 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 144 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P55884
- Protein Atlas: https://www.proteinatlas.org/ENSG00000106263-EIF3B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EIF3B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P55884
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

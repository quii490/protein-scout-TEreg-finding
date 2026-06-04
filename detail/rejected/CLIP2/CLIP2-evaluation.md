---
type: protein-evaluation
gene: "CLIP2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CLIP2 — REJECTED (核定位证据不足 (核定位得分 2/10 <= 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CLIP2 |
| 蛋白名称 | CAP-Gly domain-containing linker protein 2 |
| 蛋白大小 | 1046 aa / 115.8 kDa |
| UniProt ID | Q9UDT6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | x4 | 8 | HPA: Golgi apparatus, Plasma membrane; UniProt: Cytoplasm; Cytoplasm, cytoskeleton |
| 蛋白大小 | 8/10 | x1 | 8 | 1046 aa / 115.8 kDa |
| 研究新颖性 | 4/10 | x5 | 20 | PubMed strict=65 篇 (≤80→4) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=73.8; PDB: 无 |
| 调控结构域 | 6/10 | x2 | 12 | 无注释结构域 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 25 partners; IntAct 30 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.5/180** | |
| **归一化总分** | | | **44.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus, Plasma membrane | Approved |
| UniProt | Cytoplasm; Cytoplasm, cytoskeleton | Swiss-Prot/TremBL |

**IF 图像状态**: HPA检测到可靠IF图像信号（可能可用）。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 65 |
| PubMed broad count | 151 |
| 别名(未计入scoring) |  |

**关键文献**:
1. CLIP2 is a potential biomarker for platinum resistance and prognosis in ovarian cancer: a bioinformatics analysis.. *Transl Cancer Res*. PMID: 42180947
2. Genome-wide CRISPR interference screen identifies Clip2 as a novel regulator of osteocyte maturation and morphology.. *J Biol Chem*. PMID: 42055327
3. Modeling Williams syndrome from a neurodevelopmental perspective: recent advances, model-based translational insights and future directions.. *World J Pediatr*. PMID: 41845159
4. Insights Into the Antigenic Repertoire of Unclassified Synaptic Antibodies.. *Ann Clin Transl Neurol*. PMID: 41195642
5. A CLIP on the Ear: Spitz Melanocytoma Harbouring a CLIP2-BRAF Gene Fusion.. *Case Rep Dermatol Med*. PMID: 41608505

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.8 |
| 高置信度残基 (pLDDT>90) 占比 | 44.3% |
| 置信残基 (pLDDT 70-90) 占比 | 24.0% |
| 中等置信 (pLDDT 50-70) 占比 | 6.7% |
| 低置信 (pLDDT<50) 占比 | 25.0% |
| 有序区域 (pLDDT>70) 占比 | 68.3% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=73.8，有序区 68.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CLASRP | 0.000 | 0.000 | — |
| CLASP2 | 0.000 | 0.000 | — |
| CLASP1 | 0.000 | 0.000 | — |
| GTF2IRD1 | 0.000 | 0.000 | — |
| LIMK1 | 0.000 | 0.000 | — |
| TBL2 | 0.000 | 0.000 | — |
| EIF4H | 0.000 | 0.000 | — |
| MAPRE3 | 0.000 | 0.000 | — |
| MAPRE1 | 0.000 | 0.000 | — |
| GTF2I | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:O55156 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q80TV8 | psi-mi:"MI:0018"(two hybrid) | pubmed:- |
| uniprotkb:Q9Z0H8 | psi-mi:"MI:0096"(pull down) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P61244 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:Q9UDT6 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:- |
| uniprotkb:P51572 | psi-mi:"MI:0030"(cross-linking study) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 25，IntAct interactions: 30
- 调控相关比例: 1 / 20 = 5%

**评价**: STRING 25 个预测互作，IntAct 30 个实验互作。调控相关配体占比 5%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.8 + PDB: 无 | pLDDT=73.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, cytoskeleton / Golgi apparatus, Plasma membrane | 一致 |
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
1. CLIP2 -- CAP-Gly domain-containing linker protein 2，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小1046 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 65 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UDT6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000106665-CLIP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CLIP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UDT6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

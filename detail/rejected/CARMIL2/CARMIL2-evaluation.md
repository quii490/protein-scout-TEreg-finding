---
type: protein-evaluation
gene: "CARMIL2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CARMIL2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CARMIL2 |
| 蛋白名称 | Capping protein, Arp2/3 and myosin-I linker protein 2 |
| 蛋白大小 | 1435 aa / 154.7 kDa |
| UniProt ID | Q6F5E8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm; Cytoplasm, cytoskeleton; Cell membrane; Cell proj |
| 📏 蛋白大小 | 5/10 | ×1 | 5 | 1435 aa / 154.7 kDa |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=48 篇 (≤60→6) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=61.1; PDB: 无 |
| 🧬 调控结构域 | 5/10 | ×2 | 10 | 无注释结构域 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 18 partners; IntAct 30 interactions |
| ➕ 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.5/180** | |
| **归一化总分** | | | **44.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | No data |
| UniProt | Cytoplasm; Cytoplasm, cytoskeleton; Cell membrane; Cell projection, lamellipodiu... | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 48 |
| PubMed broad count | 50 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Gastrointestinal stenosis: an underrecognized complication of CARMIL2 deficiency.. *Allergol Immunopathol (Madr)*. PMID: 42115812
2. Gallic acid chemoprevention of oral carcinogenesis is associated with HSD11β2 upregulation and immune remodeling.. *Sci Rep*. PMID: 42045397
3. Iparomlimab and tuvonralimab (QL1706) combined definitive chemoradiotherapy in patients with locally advanced esophageal squamous cell carcinoma (QL1706-IIT-02): a single arm, phase 2 trial.. *EClinicalMedicine*. PMID: 41623855
4. EBV-associated smooth muscle tumour: a clinicopathological and genetic study of nine cases revealing heterogeneous immune statuses and novel pathogenic mutations.. *Histopathology*. PMID: 40955557
5. Allergic manifestations of actinopathies: A review.. *J Allergy Clin Immunol*. PMID: 40633594

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 61.1 |
| 高置信度残基 (pLDDT>90) 占比 | 11.8% |
| 置信残基 (pLDDT 70-90) 占比 | 39.7% |
| 中等置信 (pLDDT 50-70) 占比 | 8.3% |
| 低置信 (pLDDT<50) 占比 | 40.1% |
| 有序区域 (pLDDT>70) 占比 | 51.5% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/CARMIL2/CARMIL2-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=61.1），有序残基占 51.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TMOD4 | 0.000 | 0.000 | — |
| TMOD2 | 0.000 | 0.000 | — |
| TMOD3 | 0.000 | 0.000 | — |
| TMOD1 | 0.000 | 0.000 | — |
| CAPZB | 0.000 | 0.000 | — |
| CAPZA1 | 0.000 | 0.000 | — |
| CD28 | 0.000 | 0.000 | — |
| TTK | 0.000 | 0.000 | — |
| CAPZA2 | 0.000 | 0.000 | — |
| NFKBIL1 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q3V3V9 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:- |
| uniprotkb:Q6F5E8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q8C2K5 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:Q8C503 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P06800 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P47753 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P47757 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P47754 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P29351 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:psi-mi:"MI:1060"(spoke  |
| uniprotkb:P27870 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:psi-mi:"MI:1060"(spoke  |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 18，IntAct interactions: 30
- 调控相关比例: 0 / 18 = 0%

**评价**: STRING 18 个预测互作，IntAct 30 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=61.1 + PDB: 无 | pLDDT=61.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, cytoskeleton; Cell membrane; / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 18 + 30 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CARMIL2 — Capping protein, Arp2/3 and myosin-I linker protein 2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小1435 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 48 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=61.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6F5E8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000159753-CARMIL2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CARMIL2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6F5E8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/CARMIL2/CARMIL2-PAE.png]]

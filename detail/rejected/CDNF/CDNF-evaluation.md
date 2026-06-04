---
type: protein-evaluation
gene: "CDNF"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CDNF — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3); 研究热度过高 (PubMed strict=163，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CDNF |
| 蛋白名称 | Cerebral dopamine neurotrophic factor |
| 蛋白大小 | 187 aa / 21.0 kDa |
| UniProt ID | Q49AH0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Secreted |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 187 aa / 21.0 kDa |
| 🆕 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=163 篇 (>100→REJECTED) |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=79.8; PDB: 无 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | 无注释结构域 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 19 partners; IntAct 2 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **59.0/180** | |
| **归一化总分** | | | **32.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | No data |
| UniProt | Secreted | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 163 |
| PubMed broad count | 173 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Delivery of CDNF in collagen hydrogels modulates N-glycosylation while improving motor function in a rodent model of Parkinson's disease.. *Biomaterials*. PMID: 41934825
2. The C-domain of the cerebral dopamine neurotrophic factor (CDNF) is responsible for its cardioprotective activity by binding to the KDEL receptor relocated to the plasma membrane under endoplasmic reticulum stress conditions.. *J Mol Cell Cardiol*. PMID: 41587634
3. Redefining Parkinson's Disease management: the synergistic role of neurotrophic factors and mitochondria.. *Cell Mol Life Sci*. PMID: 41814010
4. Exosome-derived CDNF Inhibits Astrocyte and T Cell Activation by Regulating HSPA5 and Promotes Repair and Regeneration after Peripheral Nerve Injury.. *Appl Biochem Biotechnol*. PMID: 41504843
5. Cerebral dopamine neurotrophic factor and its functional fragments induce calcium signal through sigma-1 receptor and protect neurons against glutamate-induced excitotoxicity.. *Biomed Pharmacother*. PMID: 41604891

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.8 |
| 高置信度残基 (pLDDT>90) 占比 | 52.4% |
| 置信残基 (pLDDT 70-90) 占比 | 19.8% |
| 中等置信 (pLDDT 50-70) 占比 | 10.2% |
| 低置信 (pLDDT<50) 占比 | 17.6% |
| 有序区域 (pLDDT>70) 占比 | 72.2% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/CDNF/CDNF-PAE.png]]

**评价**: AlphaFold 中等质量（pLDDT=79.8，有序区 72.2%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GDNF | 0.000 | 0.000 | — |
| TH | 0.000 | 0.000 | — |
| NRTN | 0.000 | 0.000 | — |
| PSAPL1 | 0.000 | 0.000 | — |
| HSPA5 | 0.000 | 0.000 | — |
| BDNF | 0.000 | 0.000 | — |
| LRRC30 | 0.000 | 0.000 | — |
| PSAP | 0.000 | 0.000 | — |
| PSPN | 0.000 | 0.000 | — |
| ANKRD45 | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| uniprotkb:Q9Y697-2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:- |
| uniprotkb:Q9Y697 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:- |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 19，IntAct interactions: 2
- 调控相关比例: 0 / 19 = 0%

**评价**: STRING 19 个预测互作，IntAct 2 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.8 + PDB: 无 | pLDDT=79.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Secreted / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 19 + 2 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CDNF — Cerebral dopamine neurotrophic factor，研究基础较多，新颖性有限。
2. 蛋白大小187 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 163 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q49AH0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000185267-CDNF/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CDNF
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q49AH0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/CDNF/CDNF-PAE.png]]

---
type: protein-evaluation
gene: "DPP3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DPP3 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DPP3 |
| 蛋白名称 | Dipeptidyl peptidase 3 |
| 蛋白大小 | 737 aa / 82.6 kDa |
| UniProt ID | Q9NY33 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/DPP3/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/rejected/DPP3/IF_images/U2OS_1.jpg|U2OS]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 2/10 | ×4 | 8 | HPA: Cytosol; UniProt: Cytoplasm, cytosol |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 737 aa / 82.6 kDa |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=49 篇 (≤60→6) |
| 🏗️ 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=95.3; PDB: 3FVY, 3T6B, 3T6J, 5E2Q, 5E33, 5E3A, 5E3C |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR005317, IPR039461; Pfam: PF03571 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| ➕ 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **105.5/180** | |
| **归一化总分** | | | **58.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Supported |
| UniProt | Cytoplasm, cytosol | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 49 |
| PubMed broad count | 135 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Dipeptidylamino-tripeptidylcarboxypeptidase NEMP3 and DPP3 (DPP III) are the same protein.. *Biochemical and biophysical research communications*. PMID: 35653825
2. Dipeptidyl peptidase 3 modulates the renin-angiotensin system in mice.. *The Journal of biological chemistry*. PMID: 32546481
3. Involvement of DPP3 in modulating oncological features and oxidative stress response in esophageal squamous cell carcinoma.. *Bioscience reports*. PMID: 37531267
4. An outlook on biomarkers in cardiogenic shock.. *Current opinion in critical care*. PMID: 32452847
5. Dipeptidyl peptidase 3 induces myocardial ischemia-reperfusion injury by mediating mitophagy and the intrinsic apoptotic pathway.. *European journal of pharmacology*. PMID: 40189079

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 95.3 |
| 高置信度残基 (pLDDT>90) 占比 | 91.6% |
| 置信残基 (pLDDT 70-90) 占比 | 6.5% |
| 中等置信 (pLDDT 50-70) 占比 | 0.5% |
| 低置信 (pLDDT<50) 占比 | 1.4% |
| 有序区域 (pLDDT>70) 占比 | 98.1% |
| 可用 PDB 条目 | 3FVY, 3T6B, 3T6J, 5E2Q, 5E33, 5E3A, 5E3C, 5EGY, 5EHH, 7OUP |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3FVY, 3T6B, 3T6J, 5E2Q, 5E33, 5E3A, 5E3C, 5EGY, 5EHH, 7OUP）+ AlphaFold极高置信度预测（pLDDT=95.3），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR005317, IPR039461; Pfam: PF03571 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KEAP1 | 0.992 | 0.841 | — |
| AGT | 0.697 | 0.000 | — |
| DPP7 | 0.694 | 0.000 | — |
| PALB2 | 0.690 | 0.000 | — |
| CUL3 | 0.686 | 0.000 | — |
| AMER1 | 0.670 | 0.000 | — |
| OSBPL10 | 0.657 | 0.622 | — |
| PREP | 0.646 | 0.000 | — |
| THOP1 | 0.645 | 0.000 | — |
| RNPEP | 0.640 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=95.3 + PDB: 3FVY, 3T6B, 3T6J, 5E2Q, 5E33,  | pLDDT=95.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytosol / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. DPP3 — Dipeptidyl peptidase 3，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小737 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 49 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NY33
- Protein Atlas: https://www.proteinatlas.org/ENSG00000254986-DPP3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DPP3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NY33
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 12:19:11

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NY33-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

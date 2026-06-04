---
type: protein-evaluation
gene: "CARMIL3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CARMIL3 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CARMIL3 |
| 蛋白名称 | Capping protein, Arp2/3 and myosin-I linker protein 3 |
| 蛋白大小 | 1372 aa / 150.2 kDa |
| UniProt ID | Q8ND23 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm; Cell membrane |
| 📏 蛋白大小 | 5/10 | ×1 | 5 | 1372 aa / 150.2 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=7 篇 (≤20→10) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.4; PDB: 无 |
| 🧬 调控结构域 | 5/10 | ×2 | 10 | 无注释结构域 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 7 partners; IntAct 0 interactions |
| ➕ 互证加分 | — | max +3 | 0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **100/180** | |
| **归一化总分** | | | **55.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | No data |
| UniProt | Cytoplasm; Cell membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7 |
| PubMed broad count | 7 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Differential somatic coding variant landscapes between laser microdissected luminal epithelial cells from canine mammary invasive ductal solid carcinoma and comedocarcinoma.. *BMC Cancer*. PMID: 39696035
2. CARMIL3 is important for cell migration and morphogenesis during early development in zebrafish.. *Dev Biol*. PMID: 34599906
3. Capping Protein Regulator and Myosin 1 Linker 3 (CARMIL3) as a Molecular Signature of Ischemic Neurons in the DWI-T2 Mismatch Areas After Stroke.. *Front Mol Neurosci*. PMID: 34975397
4. Capping protein regulator and myosin 1 linker 3 regulates transcription of key cytokines in activated phagocytic cells.. *Cell Signal*. PMID: 33246003
5. Capping Protein Regulator and Myosin 1 Linker 3 Is Required for Tumor Metastasis.. *Mol Cancer Res*. PMID: 31694931

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.4 |
| 高置信度残基 (pLDDT>90) 占比 | 23.9% |
| 置信残基 (pLDDT 70-90) 占比 | 29.8% |
| 中等置信 (pLDDT 50-70) 占比 | 6.7% |
| 低置信 (pLDDT<50) 占比 | 39.6% |
| 有序区域 (pLDDT>70) 占比 | 53.7% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/rejected/CARMIL3/CARMIL3-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=64.4），有序残基占 53.7%。

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
| SRGAP2 | 0.000 | 0.000 | — |
| TMEM145 | 0.000 | 0.000 | — |
| ZBBX | 0.000 | 0.000 | — |
| RUNDC3A | 0.000 | 0.000 | — |
| FAM110C | 0.000 | 0.000 | — |
| WASHC2C | 0.000 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 7，IntAct interactions: 0
- 调控相关比例: 0 / 7 = 0%

**评价**: STRING 7 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.4 + PDB: 无 | pLDDT=64.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Cell membrane / 暂无HPA定位数据 | 待确认 |
| PPI | STRING + IntAct | 7 + 0 interactions | 数据有限 |

**互证加分明细**:
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CARMIL3 — Capping protein, Arp2/3 and myosin-I linker protein 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1372 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 7 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=64.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8ND23
- Protein Atlas: https://www.proteinatlas.org/ENSG00000186648-CARMIL3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CARMIL3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8ND23
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/CARMIL3/CARMIL3-PAE.png]]

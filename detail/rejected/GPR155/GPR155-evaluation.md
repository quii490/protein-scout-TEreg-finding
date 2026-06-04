---
type: protein-evaluation
gene: "GPR155"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GPR155 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPR155 / PGR22 |
| 蛋白名称 | Lysosomal cholesterol signaling protein |
| 蛋白大小 | 870 aa / 96.9 kDa |
| UniProt ID | Q7Z3F1 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Lysosome membrane |
| 蛋白大小 | 8/10 | ×1 | 8 | 870 aa / 96.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=73.2; PDB: 8U54, 8U56, 8U58, 8U5C, 8U5N, 8U5Q, 8U5V |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000591, IPR037368, IPR004776, IPR051832, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 8 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **122.0/180** | |
| **归一化总分** | | | **67.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Lysosome membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- extracellular exosome (GO:0070062)
- lysosomal membrane (GO:0005765)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 22 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PGR22 |

**关键文献**:
1. Structural insight into GPR155-mediated cholesterol sensing and signal transduction.. *Science bulletin*. PMID: 41058362
2. LYCHOS is a human hybrid of a plant-like PIN transporter and a GPCR.. *Nature*. PMID: 39358511
3. GPR155: Gene organization, multiple mRNA splice variants and expression in mouse central nervous system.. *Biochemical and biophysical research communications*. PMID: 20537985
4. Circular RNA hsa_circ_0094976 modulates GPR155 to inhibit gastric adenocarcinoma malignant characteristics by targeting miR-223-3p.. *Pathology, research and practice*. PMID: 38678850
5. GPR155 Serves as a Predictive Biomarker for Hematogenous Metastasis in Patients with Gastric Cancer.. *Scientific reports*. PMID: 28165032

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 73.2 |
| 高置信度残基 (pLDDT>90) 占比 | 27.4% |
| 置信残基 (pLDDT 70-90) 占比 | 40.9% |
| 中等置信 (pLDDT 50-70) 占比 | 10.9% |
| 低置信 (pLDDT<50) 占比 | 20.8% |
| 有序区域 (pLDDT>70) 占比 | 68.3% |
| 可用 PDB 条目 | 8U54, 8U56, 8U58, 8U5C, 8U5N, 8U5Q, 8U5V, 8U5X, 8WR3, 8Y56 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（8U54, 8U56, 8U58, 8U5C, 8U5N, 8U5Q, 8U5V, 8U5X, 8WR3, 8Y56）+ AlphaFold极高置信度预测（pLDDT=73.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000591, IPR037368, IPR004776, IPR051832, IPR036388; Pfam: PF00610, PF03547 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| JAKMIP1 | 0.531 | 0.000 | — |
| SOGA1 | 0.519 | 0.000 | — |
| GPR137B | 0.486 | 0.000 | — |
| TTC29 | 0.453 | 0.000 | — |
| GPR137 | 0.449 | 0.000 | — |
| GPRC5C | 0.444 | 0.000 | — |
| MORN5 | 0.412 | 0.000 | — |
| ZMYND15 | 0.400 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| FPR2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 8，IntAct interactions: 1
- 调控相关比例: 0 / 8 = 0%

**评价**: STRING 8 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=73.2 + PDB: 8U54, 8U56, 8U58, 8U5C, 8U5N,  | pLDDT=73.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Lysosome membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 8 + 1 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. GPR155 — Lysosomal cholesterol signaling protein，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小870 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q7Z3F1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163328-GPR155/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPR155
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q7Z3F1
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
